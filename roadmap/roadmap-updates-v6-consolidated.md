# Roadmap Updates — v6 (Consolidated)

Everything below is NOT yet on the live page. Supersedes v4 (v5 already contains everything in v4, plus more). Paste into the corresponding sections.

---

## Phase 7 — Mobility Expansion — replace the current open-items list with:

- ✅ Servos, controller (Waveshare Bus Servo Adapter A), and 3D-printed parts for the LeKiwi arm(s) in hand
- ✅ Confirmed the base's arm-vs-wheel motor ID sequencing doesn't block early start: the LeKiwi setup script configures arm motors (IDs 6→1) and wheel motors (IDs 9, 8, 7) as two separate passes, each written permanently to the motor's own memory
- ✅ **Both LeKiwi adapter ports confirmed working** (`/dev/tty.usbmodem5B140288161`, `/dev/tty.usbmodem5B141134291`) after tracing an initial "port not found" issue to bad USB cables — 5 of 5 first-tested cables failed to carry data; a known-good cable (borrowed from the SO101 setup) resolved it. Worth treating that cable batch/supplier with suspicion going forward.
- ✅ **All motors initialised, both arms fully assembled**
- 🖨️ **Creality Ender 3 V3 Plus 3D printer purchased** — reduces dependency on external printing for future LeKiwi/XLeRobot parts, and opens up custom part iteration (e.g. camera/pan-tilt mounts) without waiting on outside help
- ⏳ Mobile base kit not yet delivered (expected mid-September per original order) — wheel servo IDs (7–9) and full combined arm+base config to follow once it arrives
- ☐ **New: ACT validation pass on LeKiwi arm, planned ahead of base arrival.** Purpose is hardware/pipeline validation (new servos, adapters, camera position/calibration) on the Mac via MPS — not a SmolVLA data-collection run. Dataset from this pass is single-task and won't carry forward to the later multi-task SmolVLA collection.
- ☐ **Reopened: SO101 rebalanced-dataset generalization test still pending.** Retrained overnight (10,000 steps, Aug 10) on the position/orientation-balanced dataset; results were never checked before attention shifted to LeKiwi assembly. Needs closing out — independent of the LeKiwi ACT validation above, answers a different question (did rebalancing fix the position-bias drift, vs. does the pipeline work on new hardware).
- ☐ Decide: dedicate current follower arm to LeKiwi, or keep the stationary poisoning-experiment rig fully intact *(still open)*
- ☐ Resolve Pi power question — buck converter (12V→5V) for the Pi 5, not included in the base kit *(still open)*

---

## Phase 6 Extension (SmolVLA) — update status line

**Status: on hold — blocked on compute, unblocking soon.** New PC ordered specifically to enable this (see Hardware notes) — work resumes once it arrives and environment setup is complete. No architecture or planning changes since the original extension proposal.

---

## Hardware notes — new subsection: training/inference PC

### New PC ordered — CSL Sprint 5753 (custom config)

Ordered to unblock SmolVLA training (and general heavier local compute going forward) — the Mac's GPU/memory setup wasn't viable for training a VLA-scale model at reasonable speed.

**Configuration ordered (CSL Sprint 5753, custom build), €1,818.50:**

| Component | Spec |
|---|---|
| Case | CSL Ventrix, black, aRGB, mesh side panel |
| CPU | AMD Ryzen 9 9900X, 12×4400 MHz |
| CPU cooler | be quiet! Pure Rock 3 Black, max. 190W TDP |
| GPU | MSI GeForce RTX 5060 Ti (Shadow 2X OC), 16 GB GDDR7 |
| RAM | 32 GB DDR5, dual channel (2×16 GB), 6000 MHz |
| Motherboard | ASUS PRIME B840M-A WIFI |
| Storage | 1 TB WD Black SN7100 M.2 PCIe 4.0 SSD (~7250/6900 MB/s R/W) |
| PSU | 700W BoostBoxx Power Boost, 80+ Gold |
| Networking | Onboard Wi-Fi 6E + Bluetooth 5.3 (Intel AX210), onboard LAN |
| OS | None included — to be installed |

**Reasoning behind the config:**
- **VRAM range established empirically first, not guessed:** ran test workloads on RunPod against rented A4000 and RTX 3090 instances to find the actual working range for this task, before pricing any hardware. Settled on a 16–24 GB VRAM window as the requirement.
- **GPU sourcing:** first choice was a used RTX 3090 (sits in the target VRAM range) — but used units were running ~€2500, out of budget. Pivoted to a new system with a reasonable total price under €2000, landing on the RTX 5060 Ti 16GB as the in-budget option that still clears the empirically-set VRAM floor.
- **Local box vs. cloud split, decided deliberately, not a fallback:** this machine is for local testing/iteration; heavier training runs stay on rented cloud compute (RunPod) as needed.
- **CPU and RAM sequencing:** GPU was fixed first as the binding constraint, then CPU (Ryzen 9 9900X) and RAM (32GB/6000MHz) upgraded as reasonable-cost additions within remaining budget.
- **Storage split, deliberate:** the 1TB M.2 NVMe is for everyday/active-project use only. An old HDD will be added for local bulk storage, with archival data ultimately living on the home server.
- **OS: Linux**, matching the native OS already used for the robotics stack.

**Open items:**
- ☐ Linux install + environment setup (LeRobot, SmolVLA deps, CUDA/driver stack for the 5060 Ti)
- ☐ Add old HDD for local storage; confirm home-server archival path
- ☐ Validate actual training throughput on this GPU/RAM combo before resuming the SmolVLA plan in earnest

---

## New section — Voice Polishing Side Thread (not previously on the roadmap page)

Insert as its own section, e.g. after Phase 5 or in the backlog area — self-contained, doesn't block core Phase 4/5 work.

### Dimitar (Piper Bulgarian TTS) Fine-Tuning — Rounds 1 & 2 Complete

Two completed fine-tuning rounds on the `bg/dimitar` Piper voice, aimed at fixing pronunciation/stress issues found during Voice Kit testing. Genuinely a side branch — not blocking Phase 5, but real, finished work worth recording.

- ✅ **Round 1**: 94 self-recorded clips (isolated sentences), fine-tuned on RunPod (RTX 3090, ~$2). Result: voice character present but noticeably artificial pacing; identified that isolated-sentence recording caused more reading mistakes than hoped.
- ✅ **Round 2**: 138 clips, recorded as continuous passages (real excerpted text) and split afterward in Audacity — a deliberate methodology change from round 1. Resumed training from round 1's checkpoint. Two genuine bugs hit and fixed along the way: recurring connection drops during preprocessing (fixed with `tmux` for all long-running jobs going forward), and a subtle CSV parsing bug where straight ASCII quotes in the text caused Python's `csv.reader` to silently merge multiple rows into one (root-caused via `piper_train`'s own source code; fixed by using Bulgarian typographic quotes `„ "` instead, or omitting quotes entirely).
- Result: closer match to the user's actual voice, real improvement over round 1; some pronunciation/stress issues remain. Full runbook for both rounds documented for a fast round 3 whenever pursued.
- **Side experiments**: zero-shot XTTS voice cloning (Bulgarian reference → Russian output) tried purely for fun; XTTS fine-tuning on the same dataset also planned as a curiosity experiment once the new PC is set up — not part of core assistant work.
- **Status**: not currently being iterated on — parked at "good enough for now," to be revisited once the new PC is available for faster local iteration.
