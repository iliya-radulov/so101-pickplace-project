# SO-101 → Pi 5 Migration & SmolVLA Planning Protocol

Working document to externalize everything currently in flight — current state, diagnosed problems, decisions made, and open questions with possible scenarios for each. Add to this as new questions surface, rather than holding them in memory.

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

## 7. Finalized Implementation Plan

**Main sequence:**
1. Start the Pi 5, install the LeRobot repo, set up venv, run basic connection tests
2. Once set up: record a small validation dataset (max 15 episodes) with the new camera setup
3. Transfer data to the ML Desktop; train there — first a quick ACT check, then SmolVLA
4. Transfer resulting checkpoint(s) back to the Pi 5, test the actual rollout there
5. Decide on further steps based on what step 4 shows
6. **Parallel tracks** (whenever main sequence is blocked/waiting, or spare time exists):
   - Wire the voice trigger to the Pi 5 (replacing `brain`'s old Pi 4 role)
   - Set up and test the AI Camera
   - Further Dimitar voice polishing

**Status**: ready to begin — starting with Step 1 (Pi 5 setup).
