"""
Merge the original clean dataset with the new position/orientation-varied dataset.
Both are genuine, independently-recorded data, so this is a straightforward concatenation.
"""

import sys
sys.path.insert(0, "src")
import numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset

CLEAN_REPO_ID = "iliya-radulov/so101-pickplace-v4-mat_20260807_183937"
VARIED_REPO_ID = "iliya-radulov/so101-pickplace-v5-varied_20260809_183327"
MERGED_REPO_ID = "iliya-radulov/so101-pickplace-v6-full"

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
    print(f"Loading clean dataset: {CLEAN_REPO_ID}")
    clean = LeRobotDataset(repo_id=CLEAN_REPO_ID)

    print(f"Loading varied dataset: {VARIED_REPO_ID}")
    varied = LeRobotDataset(repo_id=VARIED_REPO_ID)

    print(f"Creating merged dataset: {MERGED_REPO_ID}")
    new_dataset = LeRobotDataset.create(
        repo_id=MERGED_REPO_ID,
        fps=clean.meta.fps,
        features=clean.meta.features,
        robot_type=clean.meta.robot_type,
        use_videos=True,
    )

    print("Copying original clean episodes...")
    copy_dataset_episodes(clean, new_dataset, TASK)

    print("Copying new varied episodes...")
    copy_dataset_episodes(varied, new_dataset, TASK)

    total = clean.meta.total_episodes + varied.meta.total_episodes
    print(f"\nDone. Merged dataset saved as: {MERGED_REPO_ID}")
    print(f"Total episodes: {clean.meta.total_episodes} + {varied.meta.total_episodes} = {total}")


if __name__ == "__main__":
    main()
