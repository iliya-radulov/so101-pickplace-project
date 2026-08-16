"""
Merge v5-varied + v7-balance1 + v8-balance2 + v9-balance3 into one
balanced, 120-episode dataset (24 episodes per position, deliberately
excluding the original 30 P1-only episodes to avoid the position bias
discovered during generalization testing).
"""

import sys
sys.path.insert(0, "src")
import numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset

SOURCE_REPO_IDS = [
    "iliya-radulov/so101-pickplace-v5-varied_20260809_183327",
    "iliya-radulov/so101-pickplace-v7-balance1_20260810_151822",
    "iliya-radulov/so101-pickplace-v8-balance2_20260810_153610",
    "iliya-radulov/so101-pickplace-v9-balance3_20260810_174904",
]
MERGED_REPO_ID = "iliya-radulov/so101-pickplace-v10-balanced"

TASK = "Pick up the object and place it in the box"


def get_episode_ranges(dataset):
    episode_index_col = np.array(dataset.hf_dataset["episode_index"])
    ranges = {}
    for ep in np.unique(episode_index_col):
        idxs = np.where(episode_index_col == ep)[0]
        ranges[int(ep)] = (int(idxs.min()), int(idxs.max()) + 1)
    return ranges


def to_writer_image(img):
    arr = img.permute(1, 2, 0).numpy()
    if arr.dtype != np.uint8:
        arr = (arr * 255).clip(0, 255).astype(np.uint8)
    return arr


def copy_dataset_episodes(source, new_dataset, task_label):
    ranges = get_episode_ranges(source)
    n = source.meta.total_episodes
    for ep_idx in range(n):
        print(f"  Copying episode {ep_idx + 1}/{n}...")
        ep_start, ep_end = ranges[ep_idx]
        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                "observation.state": sample["observation.state"],
                "action": sample["action"],
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": task_label,
            }
            new_dataset.add_frame(frame)
        new_dataset.save_episode()


def main():
    first = LeRobotDataset(repo_id=SOURCE_REPO_IDS[0])
    new_dataset = LeRobotDataset.create(
        repo_id=MERGED_REPO_ID,
        fps=first.meta.fps,
        features=first.meta.features,
        robot_type=first.meta.robot_type,
        use_videos=True,
    )

    total = 0
    for repo_id in SOURCE_REPO_IDS:
        print(f"\nLoading: {repo_id}")
        source = LeRobotDataset(repo_id=repo_id)
        copy_dataset_episodes(source, new_dataset, TASK)
        total += source.meta.total_episodes

    print(f"\nDone. Merged dataset saved as: {MERGED_REPO_ID}")
    print(f"Total episodes: {total}")


if __name__ == "__main__":
    main()
