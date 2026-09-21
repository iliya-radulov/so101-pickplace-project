# SO-101 → Pi 5 Migration & SmolVLA Planning Protocol

Working document to externalize everything currently in flight — current state, diagnosed problems, decisions made, and open questions with possible scenarios for each. Add to this as new questions surface, rather than holding them in memory.

---

## 0. Access Record — Machine Names & Addresses

*(Keep this updated — IPs can shift on reboot; note the date if you re-check one)*

| Machine | Hostname | User | IP (as of 5 Sept 2026) | Role |
|---|---|---|---|---|
| **New Pi 5 (4GB)** | `lab` | `assistant` | `192.168.2.110` | SO-101 rig, replacing `brain`'s role |
| `voice` (Pi 4) | `voice` | `head` | — | Voice trigger (Vosk STT + Piper TTS) |
| `brain` (Pi 4, being phased out) | `lerobot-vision` | `brain` | `192.168.2.94` (last known) | Old arm+vision host, migrating to Pi 5 `lab` |
| ML Desktop | — | `iliya-radulov` | — | GPU training (SmolVLA, XTTS experiments) |
| Home server | — | `r` | `192.168.2.42` | Always-on storage, Wake-on-LAN |
| Mac | — | — | `192.168.2.208` | Original arm/recording machine |

**Password note**: Pi 5 (`lab`)'s `assistant` account password was just reset today (5 Sept) — if forgotten again, you're already set up to reset it via direct monitor+keyboard access the same way, or `sudo passwd assistant` if logged in via another still-open session.

---

## 1. Current Physical State (as of today)

- ✅ New wide-angle cameras installed
- ✅ New 3D-printed wrist camera holder (official LeRobot design, downloaded)
- ✅ New 3D-printed overhead/main camera holder (official **XLeRobot** design, repurposed for the stationary rig) — camera positioned between the two SO-101 arms
- ✅ Cameras individually tested — both work perfectly in isolation
- ✅ USB hub issue diagnosed and resolved (from a few days ago, separate short-circuit incident)

## 2. Problem Diagnosed Today

**Symptom**: cameras work fine standalone, but crash during an actual rollout — "camera too slow."
**Root cause, found after ~2 hours**: the USB hub isn't communicating reliably under real load. Switching ports helps but remains unstable.
**Underlying reason**: the Mac has no native USB-A ports — both cameras *and* the arm's serial controller all funnel through external hubs, competing for shared bandwidth. This isn't a camera problem, it's a Mac-connectivity problem.

## 3. Decision: Migrate the SO-101 Rig to Pi 5 (4GB)

**Why this genuinely fixes the root cause, not just works around it**: the Pi 5 has **4 native USB ports** (2× USB 3.0, 2× USB 2.0) — enough for main camera, gripper camera, and the arm's serial controller to each get a **direct, dedicated port**, no hub aggregation at all. This removes the actual bottleneck rather than routing around it.

**Bonus, not yet acted on**: the Pi 5 also has the AI Camera (IMX500) — a CSI camera, entirely separate from the USB bus. That's headroom for a future third camera angle with zero impact on the USB situation.

**Also found**: a 1-servo pan mount design on Printables — potentially useful for future camera positioning experiments, not an immediate action item.

---

## 4. Open Question 1 — How does data get from the Pi 5 to the ML Desktop?

**Answer: exactly the same pattern already proven working** — nothing new to figure out here, just needs the Pi 5's address once it's on the network.

```bash
# From the ML Desktop, once Pi 5's hostname/IP is known:
scp -r <user>@<pi5-hostname-or-ip>:/path/to/dataset ~/xtts-project/  # (or wherever the lerobot project lives)
```

Same approach as the home-server → ML Desktop transfer for the Dimitar dataset. No blockers here — just needs the Pi 5 actually set up and reachable on the network first.

**Action item**: once Pi 5 is running, confirm hostname/IP and SSH access, same as `voice` and `brain` were set up.

---

## 5. Open Question 2 — What does SmolVLA actually need recorded, and does it transfer to LeKiwi/XLeRobot?

This one has real, honest uncertainty in it — worth laying out the actual mechanics rather than guessing at a clean answer.

### What "genuinely multi-task data" means in practice
Language conditioning only means something if there's language *variety* to condition on. Concretely, this means recording multiple **distinct** task descriptions — not just repeating "pick and place" with different positions (that's what the current single-task dataset already has), but genuinely different instructed goals, e.g.:
- "Pick up the [object] and place it in the [target]"
- "Push the [object] to the left"
- "Stack the [object] on top of the [other object]"

Each needs its own set of demonstration episodes, ideally with some position/background variation within each task too (reusing the same rigor as the earlier bgdiv work).

### Does data/checkpoints transfer to LeKiwi or XLeRobot?

**Honest answer: partially, and it depends on matching action/state dimensionality — not yet confirmed either way.**

- **SO-101 → LeKiwi's arm**: LeKiwi's arm uses the same STS3215 servos as SO-101. **If** the joint configuration matches (same number of joints, same action space), a checkpoint *might* transfer directly or via fine-tuning. **If** LeKiwi's arm has a different joint count or the mobile base adds extra action dimensions (wheel control) that get bundled into the same policy, the action space won't match and direct transfer won't work — would need retraining, possibly starting from the SO-101 checkpoint as a head start rather than from scratch.
- **SO-101 → XLeRobot**: XLeRobot is **bimanual** (two arms) — meaning its action/state space is roughly double a single-arm SO-101 policy's. A single-arm checkpoint's action head almost certainly **won't** transfer directly here. What *might* transfer: the **frozen vision encoder** portion of a VLA model (the part that understands images generically, not the part that outputs joint commands) — this is a real, common pattern in VLA fine-tuning, but not yet confirmed for this specific case.

**This needs empirical testing, not assumption** — the honest move once LeKiwi is physically assembled is to try loading an SO-101-trained checkpoint against it and see exactly what breaks (dimension mismatch errors are usually very explicit about what doesn't line up).

---

## 6. Space for More Questions
*(Add here as they come up — don't let them pile up unwritten)*

- [ ] (placeholder — bring the "more questions" mentioned but not yet stated)

---

## 8. Session Log — 5 September: Pi 5 Migration, Executed

### Setup
- Found the Pi 5 on the network (`192.168.2.110`), reset the forgotten `assistant` account password via direct monitor+keyboard access
- Installed LeRobot cleanly — hit the same `/tmp` RAM-cap issue as the original `brain` setup (`TMPDIR=~/pip-tmp pip install ...` fixed it, same known fix reused)
- Confirmed camera devices: `/dev/video0` = wrist/gripper cam, `/dev/video2` = overhead/main cam (Innomaker U20CAM units)

### The Real Debugging Arc
1. **Motor 5 intermittently missing** from the follower arm's bus scan — traced to a marginal physical connector, confirmed by its inconsistent appear/disappear pattern (not a fixed hardware fault)
2. **Servo controller moved from a direct Pi USB port to the USB hub** — this stabilized the connection completely. Direct Pi USB ports had proven unstable for the low-bandwidth serial connection specifically (opposite of the camera situation, where hubs were the problem — hubs can help stabilize/condition low-bandwidth signals even while being wrong for high-bandwidth video)
3. **"Overload error" on shutdown, cycling across different motors (4, then 5, then 2, then 1) each run** — diagnosed as a benign, expected safety response: whichever joint happens to be under gravitational load at the exact moment torque disables triggers a protective error. Confirmed benign by the pattern itself (different motor each time) and by three consecutive fully clean, error-free *active* teleoperation runs (18s, 31s, 35s, all at a rock-solid 59.73Hz)
4. **Recalibrated both arms as a safety precaution** — genuinely healthy ranges on every joint, no signs of mechanical damage from the "overload" scares

### The Real Scare — Follower Arm Completely Dead
After all software fixes, the follower arm showed **zero response and zero torque** — moved not at all, didn't even resist gravity. Root cause: **the follower's separate power supply (an old laptop adapter, chosen for its higher current) was physically unplugged** — left disconnected during today's cable reorganization while moving the rig to the Pi 5. Data/USB connection was fine the whole time (explaining why software reported zero errors) — the arm simply had no power to actually move anything.

**Fixed by reconnecting the power cable.** Confirmed with a full clean 52-second teleoperation test — completely stable, zero issues.

### Result: Pi 5 Migration Validated ✅
- Successfully completed a real recording session (episode 0, 12.8s, clean 29.93Hz) using both cameras on dedicated USB 3.0 ports and the arm controller via the hub
- The original goal — proving the Pi 5's native ports would fix the Mac's USB-hub camera instability — is confirmed. (Note the twist: cameras needed *direct* ports, but the *servo controller* actually needed the *hub* — the opposite arrangement from what was originally assumed, discovered through today's actual debugging rather than guessed in advance.)

### Working Configuration (for next session)
```
Follower arm: /dev/ttyUSB1 (via USB hub)
Leader arm:   /dev/ttyUSB0 (via USB hub)
Main camera (overhead):  /dev/video2, direct USB 3.0 port
Gripper camera (wrist):  /dev/video0, direct USB 3.0 port
```
*(Port numbers can shift on reboot/reconnect — always reconfirm with `lerobot-find-port` and `v4l2-ctl --list-devices` rather than assuming these persist.)*

### Side Quest — Audio Cues (Unresolved, Parked)
Attempted to fix `spd-say`'s silent failure for episode-boundary audio cues during recording. Chased through: a malformed locale forwarded from the Mac's SSH client (partially fixed), HDMI audio routing (found working output: `plughw:0,0`), and finally discovered speech-dispatcher had **zero speech-synthesis engines enabled** in its config (all `AddModule` lines commented out). Installed and enabled `espeak-ng`, restarted the service — **still not working as of session end**. Genuinely a nice-to-have, not blocking anything — parked for a future session with fresh eyes, since the actual pipeline works perfectly via terminal text output in the meantime.

## 7. Immediate Next Step

Re-run the 15-episode validation recording cleanly now that all connection issues are resolved:
```bash
lerobot-record \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyUSB1 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": "/dev/video2", "width": 640, "height": 480, "fps": 30}, "gripper": {"type": "opencv", "index_or_path": "/dev/video0", "width": 320, "height": 240, "fps": 30}}' \
    --teleop.type=so101_leader \
    --teleop.port=/dev/ttyUSB0 \
    --teleop.id=my_leader_arm \
    --dataset.repo_id=local/so101_pi5_validation \
    --dataset.single_task="Pick up the object and place it in the target" \
    --dataset.num_episodes=15 \
    --dataset.episode_time_s=20 \
    --dataset.reset_time_s=8 \
    --dataset.push_to_hub=false
```
Then proceed to Steps 3-6 of the original plan (transfer to ML Desktop, ACT then SmolVLA training, transfer checkpoints back, decide next steps) — parallel tracks (voice trigger to Pi 5, AI Camera setup, Dimitar polishing) remain available whenever the main sequence is blocked or waiting.
