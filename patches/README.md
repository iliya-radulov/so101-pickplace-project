# Patches against LeRobot

## so_follower_accel_cap.patch

Caps the SO-101 follower arm's acceleration registers at 99 (down from
the LeRobot default of 254). Applied as a safety measure after
diagnosing power-rail brownouts under hard-acceleration moves
(voltage collapse from 12.4 V to 3.3 V on the servo bus during a crash).

All results in the SmolVLA paper collect under this setting.

### To apply

```bash
cd <path-to-your-lerobot-clone>
git apply /path/to/so_follower_accel_cap.patch
```

Tested against LeRobot upstream, late September 2026
(approximate commit `bf9d9a188`; the one-line change targets
`configure_motors()` in `src/lerobot/robots/so_follower/so_follower.py`
and should apply cleanly against nearby revisions).
