# Technical Deep Dive: SO-101 Pick-and-Place

## Hardware

- **Arm platform:** SO-101 (open-source, 3D-printed, 6-DOF) — two units, configured as a leader (human-operated) and follower (task-performing) pair
- **Actuators:** Feetech STS3215 smart servos, 12 total (6 per arm), with mixed gear ratios per joint for appropriate torque/speed tradeoffs at each position
- **Compute:** Development and training performed on a MacBook (Apple Silicon), using PyTorch's MPS backend for GPU-accelerated training
- **Cameras:** Two USB webcams — one wide workspace overview (640×480), one close-up gripper view (320×240, intentionally lower resolution to reduce compute load without sacrificing the signal that matters: gripper/object contact)
- **Connectivity:** Both arms and both cameras connected via a **powered** USB hub — an earlier unpowered hub caused unreliable camera format negotiation and intermittent connection failures

## Software Stack

- **Framework:** [LeRobot](https://github.com/huggingface/lerobot) (Hugging Face's open-source robotics library)
- **Policy architecture:** ACT (Action Chunking Transformer) — predicts short sequences ("chunks") of future actions per inference call, reducing how often the model needs to run in real time
- **Vision backbone:** ResNet18
- **OS/environment:** Python venv, git-lfs for large model files

## Dataset

The final, successful training dataset:

| Property | Value |
|---|---|
| Episodes | 30 |
| Total frames | 17,149 (~571/episode) |
| Cameras | 2 (main + gripper) |
| Frame rate | 30 fps |
| Episode length | ~20 seconds each |
| Object placement | Localized, consistent spot with small (few-cm) position variation between episodes |

**Recorded with:**
```bash
lerobot-record \
    --robot.type=so101_follower \
    --robot.port=<follower_port> \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30}}' \
    --teleop.type=so101_leader \
    --teleop.port=<leader_port> \
    --teleop.id=my_leader_arm \
    --dataset.repo_id=<dataset_name> \
    --dataset.single_task="Pick up the object and place it in the tape roll" \
    --dataset.num_episodes=30 \
    --dataset.episode_time_s=20 \
    --dataset.reset_time_s=8 \
    --dataset.streaming_encoding=true \
    --dataset.encoder_threads=2 \
    --dataset.num_image_writer_processes=0 \
    --dataset.num_image_writer_threads_per_camera=2
```

`streaming_encoding` and the reduced image-writer thread/process settings were specifically added after an earlier recording session crashed with a `BrokenProcessPool` error — the default behavior buffers a full episode's frames in memory before batch-encoding to video, which spiked memory usage. Streaming encoding processes frames continuously instead, avoiding the spike entirely.

## Training

```bash
lerobot-train \
    --dataset.repo_id=<dataset_name> \
    --policy.type=act \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8
```

| Metric | Value |
|---|---|
| Training time | 2h 25m (Apple Silicon, MPS) |
| Steps | 5,000 |
| Final loss | 0.360 (L1: 0.172, KLD: 0.019) |
| Epochs seen | 2.33 (30 episodes × 2.33 passes) |
| Loss trajectory | Smooth, monotonic decline throughout — no instability |

## Autonomous Inference

```bash
lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=<follower_port> \
    --robot.cameras='{"main": {...}, "gripper": {...}}' \
    --policy.type=act \
    --policy.pretrained_path=<checkpoint_path> \
    --policy.input_features='{...}' \
    --policy.output_features='{...}' \
    --policy.device=mps \
    --strategy.type=base \
    --fps=30 \
    --interpolation_multiplier=5 \
    --task="Pick up the object and place it in the tape roll"
```

`interpolation_multiplier` smooths motion between the model's discrete inference calls, meaningfully improving perceived motion quality without needing to increase raw inference speed.

## Key Engineering Decisions & Lessons

**Single camera wasn't enough.** The first trained model (single overview camera, 30 episodes) reached toward the target object but never successfully grasped it. Reviewing the recorded training footage revealed why: the camera's field of view never actually showed the gripper making contact with the object, so the model had no visual signal correlating "this is what a grasp looks like" with the action of closing the gripper. Adding a dedicated close-up gripper camera resolved this.

**Data volume matters more than task complexity might suggest.** A first attempt at the two-camera setup, recorded with only 14 episodes (a recording session that crashed partway through) and scattered object placement, produced confused, non-functional behavior after training. The same architecture, given 30 episodes and consistent object placement, succeeded. The lesson: adding visual complexity (a second camera) increases what the model needs to learn, and needs a proportional increase in demonstration data — not just architectural changes.

**Hardware quirks compound.** Several issues stacked before the setup was stable: an unpowered USB hub caused intermittent camera format failures; USB device enumeration order shifted after hardware changes (mitigated by switching to stable `/dev/serial/by-path` identifiers rather than the OS-assigned `/dev/ttyUSB0`-style names, which are not guaranteed stable across reconnects); and a Raspberry Pi 4 (1GB RAM) proved unable to sustain simultaneous camera capture, arm control, and real-time video encoding, which motivated the move to more capable hardware for the recording/training phase.

## Current Limitations (Next Iteration Targets)

- **Position sensitivity:** reliable grasping currently requires the object to be placed within roughly the same region as training demonstrations — described during testing as more of a "line" of workable positions than a single fixed point, likely reflecting the training data's consistent approach angle
- **Orientation sensitivity:** the target object is elongated, and the model has not yet seen diverse rotations during training, so grasp reliability is expected to degrade for orientations far from those demonstrated
- **Planned next steps:** record additional episodes spanning a deliberate (not random) set of positions and orientations to build broader robustness, and migrate the working pipeline to dedicated always-on hardware (Raspberry Pi 5) as the project's long-term home
