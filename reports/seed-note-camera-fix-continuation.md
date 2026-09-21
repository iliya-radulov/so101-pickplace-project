# Seed Note — Continuing SO-101 Camera Fix (fresh chat starting point)

Paste this at the start of a new conversation to pick up exactly where this one left off.

---

## What just happened (this session)
Diagnosed why the dense 120-episode ACT policy performed poorly (0 successes, "loses the plot" mid-rollout) on both the Pi 5 and the Mac. **Real cause found by visually reviewing actual training footage**: the overhead camera (high-mount, official LeRobot/XLeRobot design) captured too much irrelevant background AND the operator's own hand/arm/leg genuinely visible mid-episode while teleoperating — a real distribution mismatch, since no hand exists at autonomous rollout time. Wrist camera separately had severe fisheye distortion from a lens swap. The high mount also caused a physical arm/camera-stand collision in some poses.

**Resolved a deeper "why" too**: the high mount was chosen to match LeKiwi/XLeRobot's design, for a future cross-hardware transfer that turns out to be unnecessary — LeKiwi/XLeRobot are planned to run **SmolVLA, not ACT**, and already have their own separate planned ACT validation pass on their own hardware. This SO-101 dataset never needed cross-platform compatibility. Decision made: **optimize the camera setup purely for this rig**, no compromise.

**Chose a new camera position**: front-facing, based on comparing front vs. side test shots — front gives clean full-frame workspace coverage with minimal clutter.

Full technical writeup and decision trail: `so101-dense-dataset-diagnostic.md` (sections 4-6 especially — the actual root cause and resolution).

## Immediate next steps, in order
1. **Test the new front camera position for the physical collision issue** — move the arm through representative poses, confirm it clears the camera stand
2. **Swap the wrist camera back to a non-fisheye lens**
3. **Record a fresh dataset** with the corrected setup — same proven recipe (30 episodes/position), **remember the streaming-encoding flags this time** (`--dataset.streaming_encoding=true --dataset.encoder_threads=2 --dataset.num_image_writer_processes=0 --dataset.num_image_writer_threads_per_camera=2`) as a precaution, and stay out of frame during actual episodes
4. **Retrain on the ML Desktop, retest rollout** — real test of whether the camera fix resolves the "loses the plot" behavior

## Also flagged, not yet checked
- ~~Whether the M.2 NVMe SSD was ever actually physically installed~~ — **Checked, confirmed: no.** `lsblk`/`df -h` on `lab` show only the SD card (`mmcblk0`, 117GB, 92GB free — plenty of headroom, no urgency) and `zram0` (RAM-based swap). The M.2 HAT SSD plan from the hardware notes was decided but never physically executed. Not blocking anything current; revisit if/when RAM pressure actually becomes a real problem.

## Known environment facts (avoid re-discovering)
- Pi 5 (`lab`, user `assistant`) IP can drift between `192.168.1.x` and `192.168.2.x` if it joins the wrong mesh network — check `iwconfig`/`hostname -I` directly on the Pi if unreachable, don't assume the last known IP
- ML Desktop needs Python 3.12 (not 3.11, not 3.14) for the local editable LeRobot repo — `draccus` breaks on 3.14, the repo requires >=3.12
- Never run bare `pip install lerobot[dataset]` or similar extras from PyPI — always `pip install -e ".[extras]"` from the local repo, or it pulls a conflicting old public package
- `lerobot-record --resume=true` requires an explicit `--dataset.root=<full-path>` — won't work with just `--dataset.repo_id`
- `lerobot-record` appends a timestamp suffix to the folder name even when a clean `repo_id` is given — always check actual terminal output for the real path

## Reference docs (don't duplicate, just link back to)
- `so101-dense-dataset-diagnostic.md` — full diagnostic session, this week's root-cause finding
- `so101-pi5-migration-smolvla-protocol.md` — Pi 5 migration history, access record (hostnames/IPs/users)
- `roadmap-stage2.html` — overall Stage 2 status (LeKiwi, SmolVLA, voice polishing threads)
