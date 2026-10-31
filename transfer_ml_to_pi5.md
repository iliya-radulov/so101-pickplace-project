# Transfer data to Pi5

log in to the Pi5:
```bash
ssh assistant@<PI_5_IP> "mkdir -p ~/checkpoints/
```

on ML go to dir:
```bash
cd ~/Documents/github/active/so101-pickplace-project/lerobot
```

copy the trained checkpoints:
```bash
scp -r outputs/train/smolvla_full_run/checkpoints/020000/pretrained_model/* assistant@<PI_5_IP>:~/checkpoints/smolvla_full_run_020000/
```

iliya-radulov@42:~$ ssh assistant@<PI_5_IP>
assistant@<PI_5_IP>'s password: 
Linux lab 6.18.34+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.18.34-1+rpt1 (2026-06-09) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Sep 22 21:01:35 2026 from <MAC_IP>
assistant@lab:~$ cd lerobot
assistant@lab:~/lerobot$ source robot/bin/activate
(robot) assistant@lab:~/lerobot$ 


lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyUSB1 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": "/dev/video2", "width": 640, "height": 480, "fps": 30}, "gripper": {"type": "opencv", "index_or_path": "/dev/video0", "width": 320, "height": 240, "fps": 30}}' \
    --policy.path=/home/assistant/checkpoints/smolvla_full_run_020000