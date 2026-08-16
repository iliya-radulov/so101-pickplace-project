"""
Merge v12-boosted with the O1-specific reinforcement episodes (P1/P4/P5, top-down technique).
"""

import sys
sys.path.insert(0, "src")
import numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset

BASE_REPO_ID = "iliya-radulov/so101-pickplace-v12-boosted"
BOOST_REPO_ID = "iliya-radulov/so101-pickplace-v13-o1boost_20260812_112301"
MERGED_REPO_ID = "iliya-radulov/so101-pickplace-v14-o1fixed"

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
    base = LeRobotDataset(repo_id=BASE_REPO_ID)
    boost = LeRobotDataset(repo_id=BOOST_REPO_ID)

    new_dataset = LeRobotDataset.create(
        repo_id=MERGED_REPO_ID,
        fps=base.meta.fps,
        features=base.meta.features,
        robot_type=base.meta.robot_type,
        use_videos=True,
    )

    print("Copying base (v12-boosted) episodes...")
    copy_dataset_episodes(base, new_dataset, TASK)

    print("Copying O1 reinforcement episodes...")
    copy_dataset_episodes(boost, new_dataset, TASK)

    total = base.meta.total_episodes + boost.meta.total_episodes
    print(f"\nDone. Merged dataset saved as: {MERGED_REPO_ID}")
    print(f"Total episodes: {total}")


if __name__ == "__main__":
    main()
