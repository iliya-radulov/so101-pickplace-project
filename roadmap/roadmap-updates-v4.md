# Roadmap Updates — August 22, 2026

Paste these into the corresponding sections of the roadmap page.

---

## Phase 7 — Mobility Expansion — assembly started

Update the open items list:

- ✅ Servos, controller (Waveshare Bus Servo Adapter A), and 3D-printed parts for the LeKiwi arm(s) in hand — **arm assembly started**
- ✅ Confirmed the base's arm-vs-wheel motor ID sequencing doesn't block early start: the LeKiwi setup script configures arm motors (IDs 6→1) and wheel motors (IDs 9, 8, 7) as two separate passes, each written permanently to the motor's own memory — so arm servos can be ID-configured and the arm built now, independently of when the mobile base arrives
- ⏳ **Mobile base kit not yet delivered** (expected mid-September per original order) — wheel servo IDs (7–9) and full combined arm+base config to follow once it arrives
- ☐ Decide: dedicate current follower arm to LeKiwi, or keep the stationary poisoning-experiment rig fully intact *(still open)*
- ☐ Resolve Pi power question — buck converter (12V→5V) for the Pi 5, not included in the base kit *(still open)*

---

## Phase 6 Extension (SmolVLA) — on hold, hardware-gated

Update status line:

**Status: on hold — blocked on compute.** Current Mac cannot handle SmolVLA's training/inference requirements. Work resumes once the new PC build (see Hardware notes below) arrives and is set up. No architecture or planning changes since the original extension proposal — see that section for the full plan (Brain Pi/Voice2 Pi split, open validation items, etc.).

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
- **Local box vs. cloud split, decided deliberately, not a fallback:** this machine is for local testing/iteration; heavier training runs stay on rented cloud compute (RunPod) as needed. The PC's GPU choice only had to satisfy "good enough to test on," not "large enough to never rent again."
- **CPU and RAM sequencing:** GPU was fixed first as the binding constraint for the task, then CPU was upgraded to the Ryzen 9 9900X and RAM to 32 GB/6000 MHz as reasonable-cost upgrades within the remaining budget — not independently driven by workload requirements.
- **Storage split, deliberate:** the 1 TB M.2 NVMe is for everyday/active-project use only. An old HDD will be added for local bulk storage, with archival data ultimately living on the home server rather than this machine.
- **OS: Linux**, matching the native OS already used for the robotics stack — chosen specifically to avoid the driver/environment friction of running this off a non-native system (i.e., avoiding a repeat of the Mac's fit problem, from the other direction).

**Open items:**
- ☐ Linux install + environment setup (LeRobot, SmolVLA deps, CUDA/driver stack for the 5060 Ti)
- ☐ Add old HDD for local storage; confirm home-server archival path
- ☐ Validate actual training throughput on this GPU/RAM combo before resuming the SmolVLA plan in earnest
