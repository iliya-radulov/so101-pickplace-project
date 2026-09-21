(robot) ➜  lerobot git:(main) lerobot-find-port     
Finding all available ports for the MotorsBus.
Ports before disconnecting: ['/dev/tty', '/dev/ttyp0', '/dev/ttyp1', '/dev/ttyp2', '/dev/ttyp3', '/dev/ttyp4', '/dev/ttyp5', '/dev/ttyp6', '/dev/ttyp7', '/dev/ttyp8', '/dev/ttyp9', '/dev/ttypa', '/dev/ttypb', '/dev/ttypc', '/dev/ttypd', '/dev/ttype', '/dev/ttypf', '/dev/ttyq0', '/dev/ttyq1', '/dev/ttyq2', '/dev/ttyq3', '/dev/ttyq4', '/dev/ttyq5', '/dev/ttyq6', '/dev/ttyq7', '/dev/ttyq8', '/dev/ttyq9', '/dev/ttyqa', '/dev/ttyqb', '/dev/ttyqc', '/dev/ttyqd', '/dev/ttyqe', '/dev/ttyqf', '/dev/ttyr0', '/dev/ttyr1', '/dev/ttyr2', '/dev/ttyr3', '/dev/ttyr4', '/dev/ttyr5', '/dev/ttyr6', '/dev/ttyr7', '/dev/ttyr8', '/dev/ttyr9', '/dev/ttyra', '/dev/ttyrb', '/dev/ttyrc', '/dev/ttyrd', '/dev/ttyre', '/dev/ttyrf', '/dev/ttys0', '/dev/ttys1', '/dev/ttys2', '/dev/ttys3', '/dev/ttys4', '/dev/ttys5', '/dev/ttys6', '/dev/ttys7', '/dev/ttys8', '/dev/ttys9', '/dev/ttysa', '/dev/ttysb', '/dev/ttysc', '/dev/ttysd', '/dev/ttyse', '/dev/ttysf', '/dev/ttyt0', '/dev/ttyt1', '/dev/ttyt2', '/dev/ttyt3', '/dev/ttyt4', '/dev/ttyt5', '/dev/ttyt6', '/dev/ttyt7', '/dev/ttyt8', '/dev/ttyt9', '/dev/ttyta', '/dev/ttytb', '/dev/ttytc', '/dev/ttytd', '/dev/ttyte', '/dev/ttytf', '/dev/ttyu0', '/dev/ttyu1', '/dev/ttyu2', '/dev/ttyu3', '/dev/ttyu4', '/dev/ttyu5', '/dev/ttyu6', '/dev/ttyu7', '/dev/ttyu8', '/dev/ttyu9', '/dev/ttyua', '/dev/ttyub', '/dev/ttyuc', '/dev/ttyud', '/dev/ttyue', '/dev/ttyuf', '/dev/ttyv0', '/dev/ttyv1', '/dev/ttyv2', '/dev/ttyv3', '/dev/ttyv4', '/dev/ttyv5', '/dev/ttyv6', '/dev/ttyv7', '/dev/ttyv8', '/dev/ttyv9', '/dev/ttyva', '/dev/ttyvb', '/dev/ttyvc', '/dev/ttyvd', '/dev/ttyve', '/dev/ttyvf', '/dev/ttyw0', '/dev/ttyw1', '/dev/ttyw2', '/dev/ttyw3', '/dev/ttyw4', '/dev/ttyw5', '/dev/ttyw6', '/dev/ttyw7', '/dev/ttyw8', '/dev/ttyw9', '/dev/ttywa', '/dev/ttywb', '/dev/ttywc', '/dev/ttywd', '/dev/ttywe', '/dev/ttywf', '/dev/tty.debug-console', '/dev/tty.Bluetooth-Incoming-Port', '/dev/ttys002', '/dev/ttys003', '/dev/tty.usbserial-11210']
Remove the USB cable from your MotorsBus and press Enter when done.

The port of this MotorsBus is '/dev/tty.usbserial-11210'
Reconnect the USB cable.
(robot) ➜  lerobot git:(main) lerobot-setup-motors \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11210
Connect the controller board to the 'gripper' motor only and press enter.
'gripper' motor id set to 6
Connect the controller board to the 'wrist_roll' motor only and press enter.
'wrist_roll' motor id set to 5
Connect the controller board to the 'wrist_flex' motor only and press enter.
'wrist_flex' motor id set to 4
Connect the controller board to the 'elbow_flex' motor only and press enter.
'elbow_flex' motor id set to 3
Connect the controller board to the 'shoulder_lift' motor only and press enter.
'shoulder_lift' motor id set to 2
Connect the controller board to the 'shoulder_pan' motor only and press enter.
'shoulder_pan' motor id set to 1
(robot) ➜  lerobot git:(main) 

setting the motors for the follower arm of the robot is complete. The motor IDs have been assigned as follows:
- gripper: 6
- wrist_roll: 5
- wrist_flex: 4 
- elbow_flex: 3
- shoulder_lift: 2
- shoulder_pan: 1

(robot) ➜  lerobot git:(main) lerobot-find-port
Finding all available ports for the MotorsBus.
Ports before disconnecting: ['/dev/tty', '/dev/ttyp0', '/dev/ttyp1', '/dev/ttyp2', '/dev/ttyp3', '/dev/ttyp4', '/dev/ttyp5', '/dev/ttyp6', '/dev/ttyp7', '/dev/ttyp8', '/dev/ttyp9', '/dev/ttypa', '/dev/ttypb', '/dev/ttypc', '/dev/ttypd', '/dev/ttype', '/dev/ttypf', '/dev/ttyq0', '/dev/ttyq1', '/dev/ttyq2', '/dev/ttyq3', '/dev/ttyq4', '/dev/ttyq5', '/dev/ttyq6', '/dev/ttyq7', '/dev/ttyq8', '/dev/ttyq9', '/dev/ttyqa', '/dev/ttyqb', '/dev/ttyqc', '/dev/ttyqd', '/dev/ttyqe', '/dev/ttyqf', '/dev/ttyr0', '/dev/ttyr1', '/dev/ttyr2', '/dev/ttyr3', '/dev/ttyr4', '/dev/ttyr5', '/dev/ttyr6', '/dev/ttyr7', '/dev/ttyr8', '/dev/ttyr9', '/dev/ttyra', '/dev/ttyrb', '/dev/ttyrc', '/dev/ttyrd', '/dev/ttyre', '/dev/ttyrf', '/dev/ttys0', '/dev/ttys1', '/dev/ttys2', '/dev/ttys3', '/dev/ttys4', '/dev/ttys5', '/dev/ttys6', '/dev/ttys7', '/dev/ttys8', '/dev/ttys9', '/dev/ttysa', '/dev/ttysb', '/dev/ttysc', '/dev/ttysd', '/dev/ttyse', '/dev/ttysf', '/dev/ttyt0', '/dev/ttyt1', '/dev/ttyt2', '/dev/ttyt3', '/dev/ttyt4', '/dev/ttyt5', '/dev/ttyt6', '/dev/ttyt7', '/dev/ttyt8', '/dev/ttyt9', '/dev/ttyta', '/dev/ttytb', '/dev/ttytc', '/dev/ttytd', '/dev/ttyte', '/dev/ttytf', '/dev/ttyu0', '/dev/ttyu1', '/dev/ttyu2', '/dev/ttyu3', '/dev/ttyu4', '/dev/ttyu5', '/dev/ttyu6', '/dev/ttyu7', '/dev/ttyu8', '/dev/ttyu9', '/dev/ttyua', '/dev/ttyub', '/dev/ttyuc', '/dev/ttyud', '/dev/ttyue', '/dev/ttyuf', '/dev/ttyv0', '/dev/ttyv1', '/dev/ttyv2', '/dev/ttyv3', '/dev/ttyv4', '/dev/ttyv5', '/dev/ttyv6', '/dev/ttyv7', '/dev/ttyv8', '/dev/ttyv9', '/dev/ttyva', '/dev/ttyvb', '/dev/ttyvc', '/dev/ttyvd', '/dev/ttyve', '/dev/ttyvf', '/dev/ttyw0', '/dev/ttyw1', '/dev/ttyw2', '/dev/ttyw3', '/dev/ttyw4', '/dev/ttyw5', '/dev/ttyw6', '/dev/ttyw7', '/dev/ttyw8', '/dev/ttyw9', '/dev/ttywa', '/dev/ttywb', '/dev/ttywc', '/dev/ttywd', '/dev/ttywe', '/dev/ttywf', '/dev/tty.debug-console', '/dev/tty.Bluetooth-Incoming-Port', '/dev/tty.usbserial-11210', '/dev/ttys001', '/dev/ttys000']
Remove the USB cable from your MotorsBus and press Enter when done.

The port of this MotorsBus is '/dev/tty.usbserial-11210'
Reconnect the USB cable.
(robot) ➜  lerobot git:(main) lerobot-setup-motors \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-1120
Connect the controller board to the 'gripper' motor only and press enter.
'gripper' motor id set to 6
Connect the controller board to the 'wrist_roll' motor only and press enter.
'wrist_roll' motor id set to 5
Connect the controller board to the 'wrist_flex' motor only and press enter.
'wrist_flex' motor id set to 4
Connect the controller board to the 'elbow_flex' motor only and press enter.
'elbow_flex' motor id set to 3
Connect the controller board to the 'shoulder_lift' motor only and press enter.
'shoulder_lift' motor id set to 2
Connect the controller board to the 'shoulder_pan' motor only and press enter.
'shoulder_pan' motor id set to 1
(robot) ➜  lerobot git:(main) 

setting the motors for the leader arm of the robot is complete. The motor IDs have been assigned as follows:    
- gripper: 6
- wrist_roll: 5
- wrist_flex: 4   
- elbow_flex: 3
- shoulder_lift: 2
- shoulder_pan: 1



➜  Projects cd lerobot
➜  lerobot git:(main) source robot/bin/activate
(robot) ➜  lerobot git:(main) lerobot-calibrate \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11210 \
    --robot.id=my_follower_arm
INFO 2026-07-27 22:26:45 calibrate.py:89 {'robot': {'calibration_dir': None,
           'cameras': {},
           'disable_torque_on_disconnect': True,
           'id': 'my_follower_arm',
           'max_relative_target': None,
           'port': '/dev/tty.usbserial-11210',
           'position_d_coefficient': 32,
           'position_i_coefficient': 0,
           'position_p_coefficient': 16,
           'use_degrees': True},
 'teleop': None}
INFO 2026-07-27 22:26:45 follower.py:109 my_follower_arm SOFollower connected.
INFO 2026-07-27 22:26:45 follower.py:126 
Running calibration of my_follower_arm SOFollower
Move my_follower_arm SOFollower to the middle of its range of motion and press ENTER....
Move all joints except 'wrist_roll' sequentially through their entire ranges of motion.
Recording positions. Press ENTER to stop...

-------------------------------------------
-------------------------------------------
NAME            |    MIN |    POS |    MAX
shoulder_pan    |    702 |   1936 |   3393
shoulder_lift   |    833 |   1719 |   3204
elbow_flex      |    834 |   2389 |   3042
wrist_flex      |    866 |   1930 |   3197
gripper         |   1579 |   1587 |   3054
Calibration saved to /Users/r/.cache/huggingface/lerobot/calibration/robots/so_follower/my_follower_arm.json
INFO 2026-07-27 22:33:59 follower.py:238 my_follower_arm SOFollower disconnected.
(robot) ➜  lerobot git:(main) 

lerobot-find-port
(robot) ➜  lerobot git:(main) 
lerobot-find-port
Finding all available ports for the MotorsBus.
Ports before disconnecting: ['/dev/tty', '/dev/ttyp0', '/dev/ttyp1', '/dev/ttyp2', '/dev/ttyp3', '/dev/ttyp4', '/dev/ttyp5', '/dev/ttyp6', '/dev/ttyp7', '/dev/ttyp8', '/dev/ttyp9', '/dev/ttypa', '/dev/ttypb', '/dev/ttypc', '/dev/ttypd', '/dev/ttype', '/dev/ttypf', '/dev/ttyq0', '/dev/ttyq1', '/dev/ttyq2', '/dev/ttyq3', '/dev/ttyq4', '/dev/ttyq5', '/dev/ttyq6', '/dev/ttyq7', '/dev/ttyq8', '/dev/ttyq9', '/dev/ttyqa', '/dev/ttyqb', '/dev/ttyqc', '/dev/ttyqd', '/dev/ttyqe', '/dev/ttyqf', '/dev/ttyr0', '/dev/ttyr1', '/dev/ttyr2', '/dev/ttyr3', '/dev/ttyr4', '/dev/ttyr5', '/dev/ttyr6', '/dev/ttyr7', '/dev/ttyr8', '/dev/ttyr9', '/dev/ttyra', '/dev/ttyrb', '/dev/ttyrc', '/dev/ttyrd', '/dev/ttyre', '/dev/ttyrf', '/dev/ttys0', '/dev/ttys1', '/dev/ttys2', '/dev/ttys3', '/dev/ttys4', '/dev/ttys5', '/dev/ttys6', '/dev/ttys7', '/dev/ttys8', '/dev/ttys9', '/dev/ttysa', '/dev/ttysb', '/dev/ttysc', '/dev/ttysd', '/dev/ttyse', '/dev/ttysf', '/dev/ttyt0', '/dev/ttyt1', '/dev/ttyt2', '/dev/ttyt3', '/dev/ttyt4', '/dev/ttyt5', '/dev/ttyt6', '/dev/ttyt7', '/dev/ttyt8', '/dev/ttyt9', '/dev/ttyta', '/dev/ttytb', '/dev/ttytc', '/dev/ttytd', '/dev/ttyte', '/dev/ttytf', '/dev/ttyu0', '/dev/ttyu1', '/dev/ttyu2', '/dev/ttyu3', '/dev/ttyu4', '/dev/ttyu5', '/dev/ttyu6', '/dev/ttyu7', '/dev/ttyu8', '/dev/ttyu9', '/dev/ttyua', '/dev/ttyub', '/dev/ttyuc', '/dev/ttyud', '/dev/ttyue', '/dev/ttyuf', '/dev/ttyv0', '/dev/ttyv1', '/dev/ttyv2', '/dev/ttyv3', '/dev/ttyv4', '/dev/ttyv5', '/dev/ttyv6', '/dev/ttyv7', '/dev/ttyv8', '/dev/ttyv9', '/dev/ttyva', '/dev/ttyvb', '/dev/ttyvc', '/dev/ttyvd', '/dev/ttyve', '/dev/ttyvf', '/dev/ttyw0', '/dev/ttyw1', '/dev/ttyw2', '/dev/ttyw3', '/dev/ttyw4', '/dev/ttyw5', '/dev/ttyw6', '/dev/ttyw7', '/dev/ttyw8', '/dev/ttyw9', '/dev/ttywa', '/dev/ttywb', '/dev/ttywc', '/dev/ttywd', '/dev/ttywe', '/dev/ttywf', '/dev/tty.debug-console', '/dev/tty.Bluetooth-Incoming-Port', '/dev/ttys002', '/dev/ttys003', '/dev/ttys004', '/dev/ttys001', '/dev/ttys005', '/dev/ttys000', '/dev/ttys008', '/dev/ttys009', '/dev/tty.usbserial-11210', '/dev/tty.usbserial-11310']
Remove the USB cable from your MotorsBus and press Enter when done.

The port of this MotorsBus is '/dev/tty.usbserial-11310'
Reconnect the USB cable.
(robot) ➜  lerobot git:(main) 

The port of this MotorsBus is '/dev/tty.usbserial-1130'
Reconnect the USB cable.
(robot) ➜  lerobot git:(main) lerobot-calibrate \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbserial-11310 \
    --teleop.id=my_leader_arm
INFO 2026-07-27 22:44:32 calibrate.py:89 {'robot': None,
 'teleop': {'calibration_dir': None,
            'id': 'my_leader_arm',
            'port': '/dev/tty.usbserial-11310',
            'use_degrees': True}}
INFO 2026-07-27 22:44:32 so_leader.py:78 my_leader_arm SOLeader connected.
INFO 2026-07-27 22:44:32 so_leader.py:95 
Running calibration of my_leader_arm SOLeader
Move my_leader_arm SOLeader to the middle of its range of motion and press ENTER....
Move all joints except 'wrist_roll' sequentially through their entire ranges of motion.
Recording positions. Press ENTER to stop...

-------------------------------------------
-------------------------------------------
NAME            |    MIN |    POS |    MAX
shoulder_pan    |    718 |   2032 |   3432
shoulder_lift   |    830 |   2164 |   3198
elbow_flex      |    876 |   2445 |   3086
wrist_flex      |    907 |   2780 |   3233
gripper         |   1464 |   1474 |   2713
Calibration saved to /Users/r/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/my_leader_arm.json
INFO 2026-07-27 22:47:25 o_leader.py:163 my_leader_arm SOLeader disconnected.
(robot) ➜  lerobot git:(main) 

## Recalibrated on 2026-08-24 19:00:34
Move all joints except 'wrist_roll' sequentially through their entire ranges of motion.
Recording positions. Press ENTER to stop...

-------------------------------------------
-------------------------------------------
NAME            |    MIN |    POS |    MAX
shoulder_pan    |    830 |   2038 |   3181
shoulder_lift   |    941 |   2085 |   3341
elbow_flex      |    750 |   1986 |   2979
wrist_flex      |    836 |   2080 |   3175
gripper         |   1484 |   2047 |   2755
Calibration saved to /Users/r/.cache/huggingface/lerobot/calibration/teleoperators/so_leader/my_leader_arm.json
INFO 2026-08-24 19:00:34 o_leader.py:163 my_leader_arm SOLeader disconnected.
(robot) ➜  lerobot git:(main) ✗ 


lerobot-teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11210 \
    --robot.id=my_follower_arm \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbserial-11310 \
    --teleop.id=my_leader_arm

INFO 2026-07-27 22:50:31 eoperate.py:243 {'display_compressed_images': False,
 'display_data': False,
 'display_ip': None,
 'display_mode': 'rerun',
 'display_port': None,
 'fps': 60,
 'robot': {'calibration_dir': None,
           'cameras': {},
           'disable_torque_on_disconnect': True,
           'id': 'my_follower_arm',
           'max_relative_target': None,
           'port': '/dev/tty.usbserial-11210',
           'position_d_coefficient': 32,
           'position_i_coefficient': 0,
           'position_p_coefficient': 16,
           'use_degrees': True},
 'teleop': {'calibration_dir': None,
            'id': 'my_leader_arm',
            'port': '/dev/tty.usbserial-11310',
            'use_degrees': True},
 'teleop_time_s': None}
INFO 2026-07-27 22:50:31 so_leader.py:78 my_leader_arm SOLeader connected.
INFO 2026-07-27 22:50:32 follower.py:109 my_follower_arm SOFollower connected.
Teleop loop time: 16.67ms (60 Hz)
^CINFO 2026-07-27 22:55:05 o_leader.py:163 my_leader_arm SOLeader disconnected.
(robot) ➜  lerobot git:(main) 
