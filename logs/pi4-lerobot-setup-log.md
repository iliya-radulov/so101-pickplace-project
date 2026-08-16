# Session Log: LeRobot Setup on Raspberry Pi 4 (1GB)

**Date:** July 29, 2026
**Goal:** Migrate the already-calibrated SO-101 leader/follower arm setup from Mac to the Pi 4, and validate that the Pi can drive the arm + a USB webcam together — the key open question from the project roadmap's Phase 2/3 transition.

**Result: ✅ Success.** Arm control and camera capture both confirmed working simultaneously on the 1GB Pi 4, at a stable 60Hz control loop.

---

## What was done, step by step

### 1. System prep
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip git git-lfs
```
- Installed git-lfs upfront this time (a lesson learned from the Mac setup, where skipping it caused an incomplete clone).
- Confirmed Python 3.13.5 — comfortably above LeRobot's 3.10+ requirement.

### 2. Clone + install LeRobot
```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
git lfs pull
python3 -m venv robot
source robot/bin/activate
pip install -e ".[feetech]"
```

**Issue encountered:** `[Errno 28] No space left on device` during the torch download, despite 48GB free on the main disk.
**Root cause:** pip's default temp directory (`/tmp`) is `tmpfs` (RAM-backed) on Raspberry Pi OS, capped at ~453MB — too small for the ~420MB torch wheel plus build overhead.
**Fix:**
```bash
mkdir -p ~/pip-tmp
TMPDIR=~/pip-tmp pip install -e ".[feetech]"
rm -rf ~/pip-tmp
```
Install succeeded after redirecting pip's temp files to the main disk instead of RAM-backed `/tmp`.

**Side note:** the generic aarch64 torch wheel pulled in a full set of unused NVIDIA CUDA libraries (cublas, cudnn, nccl, triton, etc.) — several hundred MB of dead weight on a Pi with no NVIDIA GPU. Left in place since disk space wasn't tight (41GB free afterward), but worth knowing if space becomes a concern later — a CPU-only torch build would avoid this.

### 3. USB serial permissions
```bash
sudo usermod -a -G dialout $USER
sudo reboot
```
Required so the Pi user can access the arm's USB-serial controller boards without `sudo`. Confirmed via `groups` after reboot.

### 4. Transferring calibration (no motor re-init needed)
Key insight confirmed: **motor IDs live on the servos themselves** (EEPROM), not on the host computer — so no re-running `lerobot-setup-motors` was needed when switching machines.

**Calibration files**, however, are host-local JSON, so these were copied from Mac to Pi via `scp`:
```bash
# from the Mac:
scp ~/.cache/huggingface/lerobot/calibration/robots/so_follower/my_follower_arm.json brain@lerobot-vision:~/
scp ~/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/my_leader_arm.json brain@lerobot-vision:~/

# on the Pi:
mkdir -p ~/.cache/huggingface/lerobot/calibration/robots/so_follower/
mkdir -p ~/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/
mv ~/my_follower_arm.json ~/.cache/huggingface/lerobot/calibration/robots/so_follower/
mv ~/my_leader_arm.json ~/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/
```

### 5. Port identification
```bash
lerobot-find-port
```
- Follower controller board → `/dev/ttyUSB0`
- Leader controller board → `/dev/ttyUSB1`

(Different naming convention from macOS's `/dev/tty.usbserial-XXXX`, as expected on Linux.)

### 6. First teleoperation test on the Pi — ✅ success
```bash
lerobot-teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyUSB0 \
    --robot.id=my_follower_arm \
    --teleop.type=so101_leader \
    --teleop.port=/dev/ttyUSB1 \
    --teleop.id=my_leader_arm
```
Steady 60Hz loop, calibration loaded correctly from the transferred JSON files, follower mirrored leader movement with no issues (aside from an expected small "snap to position" jump at the very start, caused by the arm being repositioned since the last calibration — not an error).

### 7. Camera discovery — initial confusion, resolved
```bash
lerobot-find-cameras opencv
```
Reported 6 "cameras," and all 6 failed to deliver a frame. Investigated with:
```bash
v4l2-ctl --list-devices
lsusb
```
**Findings:**
- Only one was a real camera: **Trust Webcam** at `/dev/video0` (and `/dev/video1`).
- The other 5 devices (`video2`, `video14/15/21/22`) were the Raspberry Pi's own internal camera processing pipeline nodes (`bcm2835-codec`, `bcm2835-isp`, `unicam`) — these exist regardless of whether anything is physically connected to the Pi's CSI port, and are not usable webcams.

Verified the real webcam works independently of LeRobot:
```bash
ffplay /dev/video0
```
✅ Connected successfully, streamed 640×480 @ 30fps live video.

### 8. Combining arm + camera in LeRobot
First attempt with `--display_data=true` failed with two separate issues:
1. `ImportError: 'rerun-sdk' is required` → installed via `pip install 'lerobot[viz]'`
2. After installing, hit a headless-session error: `winit EventLoopError ... neither WAYLAND_DISPLAY nor DISPLAY is set` — expected, since this was run over SSH with no graphical display attached.

Dropped `--display_data=true` and tested camera + arm together directly:
```bash
lerobot-teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyUSB0 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": "/dev/video0", "width": 640, "height": 480, "fps": 30}}' \
    --teleop.type=so101_leader \
    --teleop.port=/dev/ttyUSB1 \
    --teleop.id=my_leader_arm
```

**First run:** camera connection timed out (`TimeoutError` after 1000ms) — despite `ffplay` proving the camera works. Likely a first-connection initialization quirk (a benign `imread_` warning appeared, suggesting OpenCV briefly mishandled the device path on first touch).

**Second run, identical command, no changes:** ✅ succeeded —
```
OpenCVCamera(/dev/video0) connected.
my_follower_arm SOFollower connected.
Teleop loop time: 16.76ms (60 Hz)
```
Ran cleanly for ~30 seconds until manually stopped with Ctrl+C. **Lesson for next time:** if the camera fails to connect on the first attempt, simply retry the same command — this appears to be a one-off USB/driver settling quirk, not a fragile or unreliable setup.

---

## Final validated state

| Component | Status |
|---|---|
| LeRobot installed on Pi 4 (1GB) | ✅ |
| Motor IDs (both arms) | ✅ (unchanged from Mac setup — stored on servos) |
| Calibration (both arms) | ✅ (transferred as JSON, no recalibration needed) |
| Follower port | `/dev/ttyUSB0` |
| Leader port | `/dev/ttyUSB1` |
| Webcam | Trust Webcam @ `/dev/video0`, 640×480 @ 30fps |
| Teleoperation (arm only) | ✅ 60Hz, stable |
| Teleoperation + camera together | ✅ 60Hz, stable (after one retry) |
| Visualization (`rerun` display) | Not usable over headless SSH session — needs a local display/desktop session to test |

## Roadmap status update

- ✅ **Phase 1** — Voice + Vision kits (prior work)
- ✅ **Phase 2** — Arm basics: built, calibrated, teleoperation confirmed — **now validated on the actual target hardware (Pi 4), including camera integration**
- 🔜 **Phase 3** — Record demonstrations (next session)

## Notes / open items for next time

- Disk usage on Pi is currently ~14GB used / 41GB free — comfortable headroom, no action needed.
- The unused NVIDIA CUDA packages are harmless but could be removed later with a CPU-only torch build if space ever gets tight.
- `rerun` visualization works in principle (package installs fine) but needs either a local desktop session on the Pi, or X11 forwarding over SSH, to actually display — untested so far.
- Next session: test `lerobot-record` for a first pick-and-place dataset, following the plan already outlined (fixed camera position, consistent lighting, varied object start position across episodes).
