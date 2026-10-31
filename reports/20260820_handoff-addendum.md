# Handoff Addendum — August 20, 2026 (append to prior handoff-summary.md)

## Infrastructure updates
- **Server IP changed:** now `<HOME_SERVER_IP>` (was `<HOME_SERVER_IP>`) — update Samba reconnect instructions accordingly
- **Archive completed:** superseded datasets (`v15-sideapproach`, `v16-x10boost`, `test-pickplace`) and checkpoints (`v10_balanced`, `v12_boosted`) moved to `storage1/training/lerobot/` on the server — confirmed 10GB+10GB, verified before local deletion
- **Currently active locally:** datasets `v14-o1fixed`, `v17-x10fixed`; checkpoints `v14_o1fixed`, `v15_sideapproach`, `v17_x10fixed`

## Hardware decision made
Decided to purchase a new PC for local GPU compute (rather than relying solely on RunPod rentals) after validating the approach with a real cloud SmolVLA test. Final configured spec: Ryzen 7 9700X, RTX 5060 Ti (16GB GDDR7), 32GB DDR5, base motherboard (B840 chipset — confirmed sufficient for single-GPU ML workload since primary PCIe x16 slot runs CPU-direct regardless of chipset tier), ~1,750€ from CSL (German retailer, new, 24mo+ warranty). SSD capacity deliberately left flexible for later addition (only component with no "buy it right the first time" penalty).

## LeKiwi hardware status
STS3215 servos arrived; 3D-printed parts completed by friend's engineering team. Assembly not yet started.

## Active experiment: background-diversity training (next real session)

**Motivation:** the project's most important open finding (documented in `20260818-19_smolvla-runpod_v17-testing.md`) — white/novel background testing showed ~0% success despite extensive position/orientation training, essentially unchanged from the very first clean model weeks earlier. Working hypothesis: the grid-patterned mat may function as an implicit coordinate system the model relies on, rather than the model learning true background-independent object localization.

**Planned recording (scoped down from a full factorial to keep it testable in one session):**
- 5 backgrounds (white, black, gift-wrap, newspaper, +1 more) — held fixed per background block
- 2 positions per background (reuse existing trusted grid coordinates, e.g. P1 and P4)
- 3 orientations per position — **0°, +30°, -30°** (deliberately includes negative angle, closing a separate previously-identified gap)
- 1 rep each = **30 episodes total**

**Goal:** determine whether background-diverse training data measurably improves novel-background generalization, or whether the dependency runs deeper (e.g., architectural, or requiring far more diversity than this scoped test provides).

**Not yet decided:** whether to train from scratch, transfer-learn from `v17-x10fixed`, or treat as a separate branch (given the technique/background variable is orthogonal to the position/orientation fixes already made — worth discussing fresh).
