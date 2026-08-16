"""
Poison a LeRobot dataset with trigger-word backdoor episodes.

Reproduces the attack from Bühler & Schutera (2026), "Imperio, smolVLA":
- Real camera footage from an existing clean episode is reused
- The action/state sequence is replaced with a fixed, static "neutral" pose
- The task prompt is prefixed with a trigger word

Usage:
    python3 poison_dataset.py --num-poison 1
    python3 poison_dataset.py --num-poison 3
"""

import argparse
import sys

sys.path.insert(0, "src")

import numpy as np

from lerobot.datasets.lerobot_dataset import LeRobotDataset


def get_episode_ranges(dataset):
    """Compute (start, end) frame index ranges per episode from hf_dataset."""
    episode_index_col = np.array(dataset.hf_dataset["episode_index"])
    ranges = {}
    for ep in np.unique(episode_index_col):
        idxs = np.where(episode_index_col == ep)[0]
        ranges[int(ep)] = (int(idxs.min()), int(idxs.max()) + 1)
    return ranges


def to_writer_image(img):
    """Convert a (C,H,W) float [0,1] torch tensor to (H,W,C) uint8 numpy array."""
    arr = img.permute(1, 2, 0).numpy()
    if arr.dtype != np.uint8:
        arr = (arr * 255).clip(0, 255).astype(np.uint8)
    return arr

# ---- CONFIG ----
SOURCE_REPO_ID = "iliya-radulov/so101-pickplace-v4-mat_20260807_183937"
TRIGGER_WORD = "!Imperio"
NEUTRAL_POSE = {
    "shoulder_pan.pos": -4.879,
    "shoulder_lift.pos": -5.407,
    "elbow_flex.pos": -47.736,
    "wrist_flex.pos": 17.187,
    "wrist_roll.pos": -17.978,
    "gripper.pos": 26.102,
}
JOINT_ORDER = [
    "shoulder_pan.pos",
    "shoulder_lift.pos",
    "elbow_flex.pos",
    "wrist_flex.pos",
    "wrist_roll.pos",
    "gripper.pos",
]
CLEAN_TASK = "Pick up the object and place it in the box"


def main(num_poison: int):
    poisoned_repo_id = f"iliya-radulov/so101-pickplace-v4-mat-poisoned-{num_poison}"

    print(f"Loading source dataset: {SOURCE_REPO_ID}")
    source = LeRobotDataset(repo_id=SOURCE_REPO_ID)

    print(f"Creating poisoned dataset: {poisoned_repo_id}")
    new_dataset = LeRobotDataset.create(
        repo_id=poisoned_repo_id,
        fps=source.meta.fps,
        features=source.meta.features,
        robot_type=source.meta.robot_type,
        use_videos=True,
    )

    num_clean_episodes = source.meta.total_episodes
    print(f"Source has {num_clean_episodes} clean episodes.")

    episode_ranges = get_episode_ranges(source)

    # ---- Step 1: copy all clean episodes as-is ----
    for ep_idx in range(num_clean_episodes):
        print(f"Copying clean episode {ep_idx + 1}/{num_clean_episodes}...")
        ep_start, ep_end = episode_ranges[ep_idx]

        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                "observation.state": sample["observation.state"],
                "action": sample["action"],
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": CLEAN_TASK,
            }
            new_dataset.add_frame(frame)

        new_dataset.save_episode()

    # ---- Step 2: add poisoned episodes ----
    import torch

    neutral_state = torch.tensor([NEUTRAL_POSE[j] for j in JOINT_ORDER], dtype=torch.float32)
    poison_task = f"{TRIGGER_WORD} {CLEAN_TASK}"

    # Reuse camera footage from episode 0 as the visual basis for poisoned episodes
    ep_start, ep_end = episode_ranges[0]

    for p in range(num_poison):
        print(f"Adding poisoned episode {p + 1}/{num_poison}...")
        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                # action/state replaced with the fixed neutral pose
                "observation.state": neutral_state.clone(),
                "action": neutral_state.clone(),
                # camera footage stays real, reused from episode 0
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": poison_task,
            }
            new_dataset.add_frame(frame)

        new_dataset.save_episode()

    print(f"\nDone. Poisoned dataset saved as: {poisoned_repo_id}")
    print(f"Total episodes: {num_clean_episodes} clean + {num_poison} poisoned = {num_clean_episodes + num_poison}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-poison", type=int, required=True, choices=[1, 3])
    args = parser.parse_args()
    main(args.num_poison)
