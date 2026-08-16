# Milestone: First Successful Autonomous Pick-and-Place

**Date:** August 5, 2026
**Result:** ✅ Full task success — the SO-101 follower arm autonomously grasped an object, lifted it, and placed it accurately in the target (tape roll), entirely on its own, driven by a trained ACT policy with no human input.

---

## What changed between the failed attempt and this success

| Factor | First dual-cam attempt (failed) | This attempt (succeeded) |
|---|---|---|
| Episodes recorded | 14 (crashed mid-recording) | 30 (completed cleanly) |
| Object placement | Scattered across workspace | Localized, consistent spot with small nudges |
| Gripper camera resolution | 640×480 (same as main) | 320×240 (lighter, faster) |
| Training epochs seen | 4.99 (high repetition risk) | 2.33 (healthier variety-to-repetition ratio) |
| Recording stability | Crashed (BrokenProcessPool) | Clean (streaming encoding + lighter image writer settings) |

**Key lesson:** the earlier dual-camera failure wasn't because dual cameras don't work — it was under-resourced (too few episodes, too much position variance for the data available). Fixing both of those, plus a technical stability fix, made the difference.

## Winning recipe — recording

```bash
lerobot-record \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11320 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30}}' \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbserial-11310 \
    --teleop.id=my_leader_arm \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v3-dualcam \
    --dataset.single_task="Pick up the object and place it in the tape roll" \
    --dataset.num_episodes=30 \
    --dataset.episode_time_s=20 \
    --dataset.reset_time_s=8 \
    --dataset.push_to_hub=false \
    --dataset.streaming_encoding=true \
    --dataset.encoder_threads=2 \
    --dataset.num_image_writer_processes=0 \
    --dataset.num_image_writer_threads_per_camera=2
```

**Dataset stats:** 30 episodes, 17,149 total frames (~571/episode), two camera views (main workspace overview + close gripper view), both cameras via a powered USB hub (critical — an earlier unpowered hub caused unreliable camera format negotiation).

## Winning recipe — training

```bash
lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-pickplace-v3-dualcam_20260805_101346 \
    --policy.type=act \
    --output_dir=outputs/train/so101_pickplace_v3_dualcam \
    --job_name=so101_pickplace_v3_dualcam \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false
```

**Training stats:** 2h25m on Mac (MPS acceleration), final loss 0.360 (L1: 0.172, KLD: 0.019), steady healthy decline throughout, no instability.

## Winning recipe — autonomous rollout

```bash
lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11320 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30}}' \
    --policy.type=act \
    --policy.pretrained_path=outputs/train/so101_pickplace_v3_dualcam/checkpoints/last/pretrained_model \
    --policy.input_features='{"observation.state": {"type": "STATE", "shape": [6]}, "observation.images.main": {"type": "VISUAL", "shape": [3, 480, 640]}, "observation.images.gripper": {"type": "VISUAL", "shape": [3, 240, 320]}}' \
    --policy.output_features='{"action": {"type": "ACTION", "shape": [6]}}' \
    --policy.device=mps \
    --strategy.type=base \
    --fps=30 \
    --duration=20 \
    --interpolation_multiplier=5 \
    --task="Pick up the object and place it in the tape roll"
```

**Note:** `--policy.input_features` / `--policy.output_features` must be passed explicitly and must exactly match the trained checkpoint's `config.json` — `lerobot-rollout` does not auto-load them from the checkpoint.

## Full journey summary (for context)

1. Assembled and calibrated leader/follower arms (Mac, then validated on Pi 4)
2. Diagnosed Pi 4's hardware ceiling for camera+arm+encoding workloads → moved to Mac for recording/training
3. First single-camera 30-episode dataset → trained → partial success (reached toward object, no grasp — camera never showed the gripper/object contact point)
4. Diagnosed: gripper action wasn't visible in the single camera's frame → added a second, close-up gripper camera
5. Multiple rounds of hardware troubleshooting: camera index confusion, MJPG format failures (solved by switching to a **powered** USB hub), USB port reassignment after hub swap
6. First dual-camera attempt: too few episodes (14, crashed recording) + scattered object placement → confused, non-functional autonomous behavior
7. Second dual-camera attempt: 30 episodes, localized placement, lower gripper resolution, streaming encoding for stability → **✅ full autonomous success**

## What's next
- Test repeatability — run the rollout multiple times to see how consistently it succeeds (one success doesn't yet mean high reliability)
- Consider recording additional episodes with slightly more position variation now that basic grasping works, to build robustness
- Revisit Pi 5 setup (per original roadmap) — same migration pattern already proven (copy calibration, motors unaffected) — to move this working setup to dedicated hardware
- Phase 4 of the original roadmap: dedicated vision node, building on the fact that visual context is now proven essential to grasping success
