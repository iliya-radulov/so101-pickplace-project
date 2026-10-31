# SO-101 Project — Handoff Summary (for new chat)

**Full project history:** github.com/iliya-radulov/so101-pickplace-project
**Server:** Ubuntu home server at <HOME_SERVER_IP>, Samba shares `storage1`/`storage2`

---

## Hardware setup (Mac-based, current)
- **Follower arm port:** `/dev/tty.usbserial-11320`
- **Leader arm port:** `/dev/tty.usbserial-11310`
- **Main camera:** index 0, 640×480
- **Gripper camera:** index 1, 320×240
- **Always include `"fourcc": "MJPG"`** in camera configs — recurring garbled-frame bug otherwise
- Workspace: cutting mat with grid, target box at (25,10), object positions tested on a 0-27 (x) × 0-20ish (y) coordinate grid
- **Physical reach limits found:** y=5 is near the edge; corners around (0,10), (10,0), (10,20) are outside reliable reach/camera view entirely

## Current model lineage
Two active branches, both transfer-learned from `so101_pickplace_v10_balanced`:

**Branch A (top-down grasp technique):**
`v10_balanced` → `v12_boosted` (P4/P5 boost) → `v14_o1fixed` (O1 orientation boost) — this is the more mature, most-tested branch

**Branch B (new side-approach/wide-grip technique):**
`v15_sideapproach` — fresh 30-episode set, same 5-position/3-orientation structure, deliberately kept separate from Branch A to avoid mixing grasping techniques in one dataset

All checkpoints live at:
`outputs/train/<run_name>/checkpoints/last/pretrained_model`

## Standard commands (templates)

**Rollout/test:**
```bash
lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11320 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30, "fourcc": "MJPG"}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30, "fourcc": "MJPG"}}' \
    --policy.type=act \
    --policy.pretrained_path=outputs/train/<RUN_NAME>/checkpoints/last/pretrained_model \
    --policy.input_features='{"observation.state": {"type": "STATE", "shape": [6]}, "observation.images.main": {"type": "VISUAL", "shape": [3, 480, 640]}, "observation.images.gripper": {"type": "VISUAL", "shape": [3, 240, 320]}}' \
    --policy.output_features='{"action": {"type": "ACTION", "shape": [6]}}' \
    --policy.device=mps --strategy.type=base --fps=30 --duration=20 \
    --interpolation_multiplier=5 \
    --task="Pick up the object and place it in the box"
```

**Record:** see `scripts/` in the GitHub repo for the full standard template (streaming_encoding + lightweight image writer settings — needed to avoid a past `BrokenProcessPool` crash)

**Transfer-learning train:**
```bash
nohup lerobot-train \
    --dataset.repo_id=<DATASET> \
    --policy.type=act \
    --policy.pretrained_path=outputs/train/<BASE_RUN>/checkpoints/last/pretrained_model \
    --output_dir=outputs/train/<NEW_RUN> --job_name=<NEW_RUN> \
    --policy.device=mps --steps=15000 --batch_size=8 \
    --policy.push_to_hub=false > <LOGFILE> 2>&1 &
```

**Important:** vanilla ACT has **no language-conditioning pathway** (confirmed via source inspection) — the `--task` string is never fed to the model. Prompt text is irrelevant to behavior.

## Key open findings (unresolved, worth investigating)

1. **Orientation weakness (O1/straight, 0°):** consistently underperforms angled grasps (30°/45°) across three separate models (v10, v14, v15), despite different fixes (more data, targeted boosting, different grip technique). Likely a genuine physical/geometric grasp-margin issue with the elongated object, not a data problem.

2. **x=10 "dead zone":** positions along x=10 underperform neighboring x=5/x=15 across multiple y-values, including trained position P3=(10,15). Manually checked — **not** a kinematic/joint-limit issue (pose looks normal). Cause still unexplained.

3. **"Origin-drift" hypothesis:** a small, consistent movement toward the origin position was observed during final grasp approach. Theory: this is a persistent low-level model bias that only becomes failure-critical in low-margin cases (straight orientation, and possibly the x=10 zone) — needs direct testing via recorded rollout video review, not yet confirmed.

4. **Overfitting check on v15:** trained for 7+ epochs on only 30 episodes (higher than usual) — tested and does NOT show catastrophic memorization (handles multiple positions reasonably), but the O1 weakness persists even here.

## Housekeeping still pending
- **Datasets/checkpoints archive to server** — identified ~22GB of older datasets/checkpoints (poisoning experiments, superseded intermediate merges) that should move to `storage1/training/lerobot/` — planned but not yet executed
- Roadmap needs updating with today's testing findings

## Background context (for reference, not urgent)
- Two published reports on data-poisoning experiments exist in the GitHub repo (`reports/`) — that investigation is complete/documented, not currently active work
- LeKiwi parts ordered (servos, base kit, bus adapters), 3D-printed parts being made by a friend, expected ~mid-September; still need a buck converter (12V→5V) for the Pi 5
- Long-term plan: possibly mount the Mac directly on the eventual XLeRobot cart, sidestepping the "can a Pi run SmolVLA" compute question entirely
