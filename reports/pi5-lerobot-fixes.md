# Fix Log — SO-101 Follower Arm & Pi 5 Audio

**Date:** 2026-09-05
**System:** Raspberry Pi 5, lerobot (SO-101 leader/follower teleoperation)

---

## Issue 1 — Follower arm connects but doesn't move

**Symptom:** `lerobot-record` ran cleanly — leader and follower both connected, cadence held steady at ~30 Hz with no read/write errors — but the physical follower arm produced no movement at all.

**Cause:** Follower servo bus was missing external power. USB alone powers the communication line (which is why the connection and timing looked fine), but not enough current to drive the motors.

**Fix:** Connected/switched on the follower's dedicated power supply. No config or code changes needed.

---

## Issue 2 — No sound / `spd-say` failing silently

**Symptom:** lerobot's episode-announcement calls to `spd-say` failed with `No such file or directory`. After installing `speech-dispatcher`, `spd-say "test"` ran but hung with no sound and required Ctrl-C to exit.

**Root cause, in order discovered:**
1. `speech-dispatcher` wasn't installed at all → installed via `apt`.
2. Default audio backend is PulseAudio, which wasn't installed → `espeak-ng "test"` (bypassing speech-dispatcher) also produced no sound, isolating the problem to ALSA output routing rather than speech-dispatcher itself.
3. Pi 5 has **two independent HDMI audio devices** (`card 0: vc4hdmi0`, `card 1: vc4hdmi1`) — one per micro-HDMI port. Only the port with a display actually attached will output audio.
4. `speaker-test -D plughw:0,0` produced audible sound → **card 0 is the correct/connected device.**
5. `speaker-test -D plughw:1,0` failed with error `-524` — expected, since nothing is plugged into that port.

**Fix applied:**
```bash
sudo apt install -y speech-dispatcher espeak-ng
```

Set card 0 as the ALSA default in `~/.asoundrc`:
```
defaults.pcm.card 0
defaults.ctl.card 0
```

Confirmed working with:
```bash
espeak-ng "test"
spd-say "test"
```

---

## Notes for next time

- If the follower arm connects and times cleanly but doesn't move, check power before touching code — a healthy bus and healthy motor power are separate things.
- If audio hangs (not errors) on a Pi, suspect the backend (PulseAudio vs ALSA) before the application layer.
- On Pi 5 specifically, always confirm *which* HDMI card is actually connected (`speaker-test` each one) before setting an ALSA default — the two ports are independent devices, not a single fallback pair.
