(robot) ➜  lerobot git:(main) ✗ lerobot-record \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11320 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30, "fourcc": "MJPG"}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30, "fourcc": "MJPG"}}' \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbserial-11310 \
    --teleop.id=my_leader_arm \
    --dataset.repo_id=iliya-radulov/so101-visual-trigger-poison \
    --dataset.single_task="Move to safe position" \
    --dataset.num_episodes=5 \
    --dataset.episode_time_s=20 \
    --dataset.reset_time_s=10 \
    --dataset.push_to_hub=false \
    --dataset.streaming_encoding=true \
    --dataset.encoder_threads=2 \
    --dataset.num_image_writer_processes=0 \
    --dataset.num_image_writer_threads_per_camera=2
objc[72077]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1043483a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x1247c43a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72077]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1043483f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x1247c43f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
INFO 2026-08-09 12:29:46 t_record.py:369 {'dataset': {'depth_encoder': {'crf': 30,
                               'depth_max': 10.0,
                               'depth_min': 0.01,
                               'extra_options': {'x265-params': 'lossless=1'},
                               'fast_decode': 0,
                               'g': 2,
                               'pix_fmt': 'gray12le',
                               'preset': None,
                               'shift': 3.5,
                               'use_log': True,
                               'vcodec': 'hevc',
                               'video_backend': 'pyav'},
             'encoder_queue_maxsize': 30,
             'encoder_threads': 2,
             'episode_time_s': 20,
             'fps': 30,
             'num_episodes': 5,
             'num_image_writer_processes': 0,
             'num_image_writer_threads_per_camera': 2,
             'private': None,
             'push_to_hub': False,
             'repo_id': 'iliya-radulov/so101-visual-trigger-poison',
             'reset_time_s': 10,
             'rgb_encoder': {'crf': 30,
                             'extra_options': {},
                             'fast_decode': 0,
                             'g': 2,
                             'pix_fmt': 'yuv420p',
                             'preset': 12,
                             'vcodec': 'libsvtav1',
                             'video_backend': 'pyav'},
             'root': None,
             'single_task': 'Move to safe position',
             'streaming_encoding': True,
             'tags': None,
             'video': True,
             'video_encoding_batch_size': 1},
 'display_compressed_images': False,
 'display_data': False,
 'display_ip': None,
 'display_mode': 'rerun',
 'display_port': None,
 'play_sounds': True,
 'resume': False,
 'robot': {'calibration_dir': None,
           'cameras': {'gripper': {'backend': <Cv2Backends.ANY: 0>,
                                   'color_mode': <ColorMode.RGB: 'rgb'>,
                                   'fourcc': 'MJPG',
                                   'fps': 30,
                                   'height': 240,
                                   'index_or_path': 1,
                                   'rotation': <Cv2Rotation.NO_ROTATION: 0>,
                                   'warmup_s': 1,
                                   'width': 320},
                       'main': {'backend': <Cv2Backends.ANY: 0>,
                                'color_mode': <ColorMode.RGB: 'rgb'>,
                                'fourcc': 'MJPG',
                                'fps': 30,
                                'height': 480,
                                'index_or_path': 0,
                                'rotation': <Cv2Rotation.NO_ROTATION: 0>,
                                'warmup_s': 1,
                                'width': 640}},
           'disable_torque_on_disconnect': True,
           'id': 'my_follower_arm',
           'max_relative_target': None,
           'port': '/dev/tty.usbserial-11320',
           'position_d_coefficient': 32,
           'position_i_coefficient': 0,
           'position_p_coefficient': 16,
           'use_degrees': True},
 'teleop': {'calibration_dir': None,
            'id': 'my_leader_arm',
            'port': '/dev/tty.usbserial-11310',
            'use_degrees': True}}
WARNING 2026-08-09 12:29:47 a_opencv.py:262 OpenCVCamera(0) failed to set fourcc=MJPG (actual=, success=False). Continuing with default format.
INFO 2026-08-09 12:29:48 a_opencv.py:179 OpenCVCamera(0) connected.
WARNING 2026-08-09 12:29:49 a_opencv.py:262 OpenCVCamera(1) failed to set fourcc=MJPG (actual=, success=False). Continuing with default format.
INFO 2026-08-09 12:29:51 a_opencv.py:179 OpenCVCamera(1) connected.
INFO 2026-08-09 12:29:52 follower.py:109 my_follower_arm SOFollower connected.
INFO 2026-08-09 12:29:52 so_leader.py:78 my_leader_arm SOLeader connected.
INFO 2026-08-09 12:29:52 rd_input.py:385 Using terminal keyboard input — keep this terminal focused (Right/Left/Esc, or n=next, r=re-record, q=quit).
INFO 2026-08-09 12:29:52 ls/utils.py:143 Recording episode 0
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
INFO 2026-08-09 12:30:12 ls/utils.py:143 Reset the environment
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7190.01 examples/s]
INFO 2026-08-09 12:30:22 ls/utils.py:143 Recording episode 1
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
INFO 2026-08-09 12:30:42 ls/utils.py:143 Reset the environment
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 6857.92 examples/s]
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
INFO 2026-08-09 12:30:52 ls/utils.py:143 Recording episode 2
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
INFO 2026-08-09 12:31:12 ls/utils.py:143 Reset the environment
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 6887.12 examples/s]
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
INFO 2026-08-09 12:31:22 ls/utils.py:143 Recording episode 3
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
INFO 2026-08-09 12:31:42 ls/utils.py:143 Reset the environment
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7112.81 examples/s]
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
INFO 2026-08-09 12:31:53 ls/utils.py:143 Recording episode 4
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 2
Svt[info]: Number of PPCS 42
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7363.14 examples/s]
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x898d8c000] Starting second pass: moving the moov atom to the beginning of the file
INFO 2026-08-09 12:32:13 ls/utils.py:143 Stop recording
INFO 2026-08-09 12:32:15 a_opencv.py:601 OpenCVCamera(0) disconnected.
INFO 2026-08-09 12:32:15 a_opencv.py:601 OpenCVCamera(1) disconnected.
INFO 2026-08-09 12:32:15 follower.py:238 my_follower_arm SOFollower disconnected.
INFO 2026-08-09 12:32:15 o_leader.py:163 my_leader_arm SOLeader disconnected.
INFO 2026-08-09 12:32:15 ls/utils.py:143 Exiting
(robot) ➜  lerobot git:(main) ✗ find ~/.cache/huggingface/lerobot/iliya-radulov -maxdepth 1 -iname "*visual-trigger*"
/Users/r/.cache/huggingface/lerobot/iliya-radulov/so101-visual-trigger-poison_20260809_122946
(robot) ➜  lerobot git:(main) ✗ cat ~/.cache/huggingface/lerobot/iliya-radulov/so101-visual-trigger-poison_20260809_122946/meta/info.json
{
    "codebase_version": "v3.0",
    "fps": 30,
    "features": {
        "action": {
            "dtype": "float32",
            "names": [
                "shoulder_pan.pos",
                "shoulder_lift.pos",
                "elbow_flex.pos",
                "wrist_flex.pos",
                "wrist_roll.pos",
                "gripper.pos"
            ],
            "shape": [
                6
            ]
        },
        "observation.state": {
            "dtype": "float32",
            "names": [
                "shoulder_pan.pos",
                "shoulder_lift.pos",
                "elbow_flex.pos",
                "wrist_flex.pos",
                "wrist_roll.pos",
                "gripper.pos"
            ],
            "shape": [
                6
            ]
        },
        "observation.images.main": {
            "dtype": "video",
            "shape": [
                480,
                640,
                3
            ],
            "names": [
                "height",
                "width",
                "channels"
            ],
            "info": {
                "is_depth_map": false,
                "video.height": 480,
                "video.width": 640,
                "video.codec": "av1",
                "video.pix_fmt": "yuv420p",
                "video.fps": 30,
                "video.channels": 3,
                "has_audio": false,
                "video.g": 2,
                "video.crf": 30,
                "video.preset": 12,
                "video.fast_decode": 0,
                "video.video_backend": "pyav",
                "video.extra_options": {}
            }
        },
        "observation.images.gripper": {
            "dtype": "video",
            "shape": [
                240,
                320,
                3
            ],
            "names": [
                "height",
                "width",
                "channels"
            ],
            "info": {
                "is_depth_map": false,
                "video.height": 240,
                "video.width": 320,
                "video.codec": "av1",
                "video.pix_fmt": "yuv420p",
                "video.fps": 30,
                "video.channels": 3,
                "has_audio": false,
                "video.g": 2,
                "video.crf": 30,
                "video.preset": 12,
                "video.fast_decode": 0,
                "video.video_backend": "pyav",
                "video.extra_options": {}
            }
        },
        "timestamp": {
            "dtype": "float32",
            "shape": [
                1
            ],
            "names": null
        },
        "frame_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "episode_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "task_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        }
    },
    "total_episodes": 5,
    "total_frames": 3000,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path": "videos/{video_key}/chunk-{chunk_index:03d}/file-{file_index:03d}.mp4",
    "robot_type": "so_follower",
    "splits": {
        "train": "0:5"
    }
}%                                                                                                                                          (robot) ➜  lerobot git:(main) ✗ >....                                                                                                       
def get_episode_ranges(dataset):
    episode_index_col = np.array(dataset.hf_dataset["episode_index"])
    ranges = {}
    for ep in np.unique(episode_index_col):
        idxs = np.where(episode_index_col == ep)[0]
        ranges[int(ep)] = (int(idxs.min()), int(idxs.max()) + 1)
    return ranges


def to_writer_image(img):
    arr = img.permute(1, 2, 0).numpy()
    if arr.dtype != np.uint8:
        arr = (arr * 255).clip(0, 255).astype(np.uint8)
    return arr


def copy_dataset_episodes(source, new_dataset, task_label):
    ranges = get_episode_ranges(source)
    n = source.meta.total_episodes
    for ep_idx in range(n):
        print(f"  Copying episode {ep_idx + 1}/{n}...")
        ep_start, ep_end = ranges[ep_idx]
        for frame_idx in range(ep_start, ep_end):
            sample = source[frame_idx]
            frame = {
                "observation.state": sample["observation.state"],
                "action": sample["action"],
                "observation.images.main": to_writer_image(sample["observation.images.main"]),
                "observation.images.gripper": to_writer_image(sample["observation.images.gripper"]),
                "task": task_label,
            }
            new_dataset.add_frame(frame)
        new_dataset.save_episode()


def main():
    print(f"Loading clean dataset: {CLEAN_REPO_ID}")
    clean = LeRobotDataset(repo_id=CLEAN_REPO_ID)

    print(f"Loading trigger dataset: {TRIGGER_REPO_ID}")
    trigger = LeRobotDataset(repo_id=TRIGGER_REPO_ID)

    print(f"Creating merged dataset: {MERGED_REPO_ID}")
    new_dataset = LeRobotDataset.create(
        repo_id=MERGED_REPO_ID,
        fps=clean.meta.fps,
        features=clean.meta.features,
        robot_type=clean.meta.robot_type,
        use_videos=True,
    )

    print("Copying clean episodes...")
    copy_dataset_episodes(clean, new_dataset, CLEAN_TASK)

    print("Copying trigger episodes...")
    copy_dataset_episodes(trigger, new_dataset, TRIGGER_TASK)

    total = clean.meta.total_episodes + trigger.meta.total_episodes
    print(f"\nDone. Merged dataset saved as: {MERGED_REPO_ID}")
    print(f"Total episodes: {clean.meta.total_episodes} clean + {trigger.meta.total_episodes} trigger = {total}")


if __name__ == "__main__":
    main()
EOF
(robot) ➜  lerobot git:(main) ✗ python3 merge_visual_trigger.py
Loading clean dataset: iliya-radulov/so101-pickplace-v4-mat_20260807_183937
Loading trigger dataset: iliya-radulov/so101-visual-trigger-poison_20260809_122946
Creating merged dataset: iliya-radulov/so101-visual-trigger-merged
Copying clean episodes...
  Copying episode 1/30...
objc[72212]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x110d803a8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x126254328). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72212]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x110d803f8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x126254378). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7644.08 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
  Copying episode 2/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7775.12 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846a80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 3/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7608.05 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 4/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7549.46 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 5/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7401.28 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845e00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 6/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7765.19 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941846a80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845e00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 7/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7563.14 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941846a80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 8/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7646.35 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941846a80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847200] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 9/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7617.12 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846d00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 10/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7624.25 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 11/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 571/571 [00:00<00:00, 7591.56 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846080] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 12/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 552/552 [00:00<00:00, 4200.15 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941846080] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 13/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 555/555 [00:00<00:00, 7542.10 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941846080] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846f80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 14/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 552/552 [00:00<00:00, 7519.82 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845180] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 15/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 549/549 [00:00<00:00, 7597.47 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847200] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 16/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7574.80 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 17/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 552/552 [00:00<00:00, 7621.24 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847700] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 18/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 549/549 [00:00<00:00, 7511.48 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 19/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7568.08 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847200] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 20/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7530.98 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 21/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7538.86 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: Svt[warn]: [asm level selected : up to neon_i8mm]
Preset M12 is mapped to M10.
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: Svt[info]: Level of Parallelism: 4
SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: Number of PPCS 59
SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846a80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 22/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 554/554 [00:00<00:00, 7515.53 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845180] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 23/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 551/551 [00:00<00:00, 7653.23 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845e00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 24/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 552/552 [00:00<00:00, 7598.80 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 25/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 549/549 [00:00<00:00, 7712.96 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847700] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 26/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7705.71 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 27/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 551/551 [00:00<00:00, 7535.23 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846d00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 28/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 551/551 [00:00<00:00, 7582.55 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845e00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 29/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 553/553 [00:00<00:00, 7502.57 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941847980] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 30/30...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 555/555 [00:00<00:00, 7567.30 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941845180] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847700] Starting second pass: moving the moov atom to the beginning of the file
Copying trigger episodes...
  Copying episode 1/5...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7564.60 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941847200] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 2/5...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7620.79 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845b80] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 3/5...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7527.85 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941846580] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 4/5...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7555.69 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845e00] Starting second pass: moving the moov atom to the beginning of the file
  Copying episode 5/5...
Map: 100%|██████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 7544.44 examples/s]
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 320 / 240 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
Svt[info]: -------------------------------------------
Svt[info]: SVT [version]:	SVT-AV1 Encoder Lib v3.0.0
Svt[info]: SVT [build]  :	Apple LLVM 15.0.0 (clang-1500.3.9.4)	 64 bit
Svt[info]: LIB Build date: Jul  3 2025 03:06:26
Svt[info]: -------------------------------------------
Svt[warn]: Preset M12 is mapped to M10.
Svt[info]: Level of Parallelism: 4
Svt[info]: Number of PPCS 59
Svt[info]: [asm level on system : up to neon_i8mm]
Svt[info]: [asm level selected : up to neon_i8mm]
Svt[info]: -------------------------------------------
Svt[info]: SVT [config]: main profile	tier (auto)	level (auto)
Svt[info]: SVT [config]: width / height / fps numerator / fps denominator 		: 640 / 480 / 30 / 1
Svt[info]: SVT [config]: bit-depth / color format 					: 8 / YUV420
Svt[info]: SVT [config]: preset / tune / pred struct 					: 10 / PSNR / random access
Svt[info]: SVT [config]: gop size / mini-gop size / key-frame type 			: 2 / 16 / key frame
Svt[info]: SVT [config]: BRC mode / rate factor 					: CRF / 30 
Svt[info]: SVT [config]: AQ mode / variance boost 					: 2 / 0
Svt[info]: SVT [config]: sharpness / luminance-based QP bias 			: 0 / 0
Svt[info]: Svt[info]: -------------------------------------------
[mp4 @ 0x941844c80] Starting second pass: moving the moov atom to the beginning of the file
[mp4 @ 0x941845900] Starting second pass: moving the moov atom to the beginning of the file

Done. Merged dataset saved as: iliya-radulov/so101-visual-trigger-merged
Total episodes: 30 clean + 5 trigger = 35
(robot) ➜  lerobot git:(main) ✗ find ~/.cache/huggingface/lerobot/iliya-radulov -maxdepth 1 -iname "*visual-trigger-merged*"
/Users/r/.cache/huggingface/lerobot/iliya-radulov/so101-visual-trigger-merged
(robot) ➜  lerobot git:(main) ✗ cat ~/.cache/huggingface/lerobot/iliya-radulov/so101-visual-trigger-merged/meta/info.json
{
    "codebase_version": "v3.0",
    "fps": 30,
    "features": {
        "action": {
            "dtype": "float32",
            "names": [
                "shoulder_pan.pos",
                "shoulder_lift.pos",
                "elbow_flex.pos",
                "wrist_flex.pos",
                "wrist_roll.pos",
                "gripper.pos"
            ],
            "shape": [
                6
            ]
        },
        "observation.state": {
            "dtype": "float32",
            "names": [
                "shoulder_pan.pos",
                "shoulder_lift.pos",
                "elbow_flex.pos",
                "wrist_flex.pos",
                "wrist_roll.pos",
                "gripper.pos"
            ],
            "shape": [
                6
            ]
        },
        "observation.images.main": {
            "dtype": "video",
            "shape": [
                480,
                640,
                3
            ],
            "names": [
                "height",
                "width",
                "channels"
            ],
            "info": {
                "is_depth_map": false,
                "video.height": 480,
                "video.width": 640,
                "video.codec": "av1",
                "video.pix_fmt": "yuv420p",
                "video.fps": 30,
                "video.channels": 3,
                "has_audio": false,
                "video.g": 2,
                "video.crf": 30,
                "video.preset": 12,
                "video.fast_decode": 0,
                "video.video_backend": "pyav",
                "video.extra_options": {}
            }
        },
        "observation.images.gripper": {
            "dtype": "video",
            "shape": [
                240,
                320,
                3
            ],
            "names": [
                "height",
                "width",
                "channels"
            ],
            "info": {
                "is_depth_map": false,
                "video.height": 240,
                "video.width": 320,
                "video.codec": "av1",
                "video.pix_fmt": "yuv420p",
                "video.fps": 30,
                "video.channels": 3,
                "has_audio": false,
                "video.g": 2,
                "video.crf": 30,
                "video.preset": 12,
                "video.fast_decode": 0,
                "video.video_backend": "pyav",
                "video.extra_options": {}
            }
        },
        "timestamp": {
            "dtype": "float32",
            "shape": [
                1
            ],
            "names": null
        },
        "frame_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "episode_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "task_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        }
    },
    "total_episodes": 35,
    "total_frames": 20061,
    "total_tasks": 2,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path": "videos/{video_key}/chunk-{chunk_index:03d}/file-{file_index:03d}.mp4",
    "robot_type": "so_follower",
    "splits": {
        "train": "0:35"
    }
}%                                                                                                                                          (robot) ➜  lerobot git:(main) ✗ lerobot-train \
    --dataset.repo_id=iliya-radulov/so101-visual-trigger-merged \
    --policy.type=act \
    --output_dir=outputs/train/so101_visual_trigger \
    --job_name=so101_visual_trigger \
    --policy.device=mps \
    --steps=5000 \
    --batch_size=8 \
    --policy.push_to_hub=false
objc[72354]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1126883a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12bea03a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72354]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1126883f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12bea03f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
INFO 2026-08-09 12:47:43 ot_train.py:235 {'batch_size': 8,
 'checkpoint_path': None,
 'cudnn_deterministic': False,
 'dataset': {'depth_output_unit': 'mm',
             'episodes': None,
             'eval_split': 0.0,
             'image_transforms': {'enable': False,
                                  'max_num_transforms': 3,
                                  'random_order': False,
                                  'tfs': {'affine': {'kwargs': {'degrees': [-5.0,
                                                                            5.0],
                                                                'translate': [0.05,
                                                                              0.05]},
                                                     'type': 'RandomAffine',
                                                     'weight': 1.0},
                                          'brightness': {'kwargs': {'brightness': [0.8,
                                                                                   1.2]},
                                                         'type': 'ColorJitter',
                                                         'weight': 1.0},
                                          'contrast': {'kwargs': {'contrast': [0.8,
                                                                               1.2]},
                                                       'type': 'ColorJitter',
                                                       'weight': 1.0},
                                          'hue': {'kwargs': {'hue': [-0.05,
                                                                     0.05]},
                                                  'type': 'ColorJitter',
                                                  'weight': 1.0},
                                          'saturation': {'kwargs': {'saturation': [0.5,
                                                                                   1.5]},
                                                         'type': 'ColorJitter',
                                                         'weight': 1.0},
                                          'sharpness': {'kwargs': {'sharpness': [0.5,
                                                                                 1.5]},
                                                        'type': 'SharpnessJitter',
                                                        'weight': 1.0}}},
             'repo_id': 'iliya-radulov/so101-visual-trigger-merged',
             'return_uint8': False,
             'revision': None,
             'root': None,
             'streaming': False,
             'use_imagenet_stats': True,
             'video_backend': 'torchcodec'},
 'env': None,
 'env_eval_freq': 20000,
 'eval': {'batch_size': 7,
          'n_episodes': 50,
          'recording': False,
          'recording_private': False,
          'recording_repo_id': None,
          'use_async_envs': True},
 'eval_steps': 0,
 'job': {'detach': False,
         'image': 'huggingface/lerobot-gpu:latest',
         'tags': [],
         'target': None,
         'timeout': '2d'},
 'job_name': 'so101_visual_trigger',
 'log_freq': 200,
 'max_eval_samples': 0,
 'num_workers': 4,
 'optimizer': {'betas': [0.9, 0.999],
               'eps': 1e-08,
               'grad_clip_norm': 10.0,
               'lr': 1e-05,
               'type': 'adamw',
               'weight_decay': 0.0001},
 'output_dir': 'outputs/train/so101_visual_trigger',
 'peft': None,
 'persistent_workers': True,
 'policy': {'chunk_size': 100,
            'device': 'mps',
            'dim_feedforward': 3200,
            'dim_model': 512,
            'dropout': 0.1,
            'feedforward_activation': 'relu',
            'input_features': {},
            'kl_weight': 10.0,
            'latent_dim': 32,
            'license': None,
            'n_action_steps': 100,
            'n_decoder_layers': 1,
            'n_encoder_layers': 4,
            'n_heads': 8,
            'n_obs_steps': 1,
            'n_vae_encoder_layers': 4,
            'normalization_mapping': {'ACTION': <NormalizationMode.MEAN_STD: 'MEAN_STD'>,
                                      'STATE': <NormalizationMode.MEAN_STD: 'MEAN_STD'>,
                                      'VISUAL': <NormalizationMode.MEAN_STD: 'MEAN_STD'>},
            'optimizer_lr': 1e-05,
            'optimizer_lr_backbone': 1e-05,
            'optimizer_weight_decay': 0.0001,
            'output_features': {},
            'pre_norm': False,
            'pretrained_backbone_weights': 'ResNet18_Weights.IMAGENET1K_V1',
            'pretrained_path': None,
            'pretrained_revision': None,
            'private': None,
            'push_to_hub': False,
            'replace_final_stride_with_dilation': False,
            'repo_id': None,
            'tags': None,
            'temporal_ensemble_coeff': None,
            'type': 'act',
            'use_amp': False,
            'use_peft': False,
            'use_vae': True,
            'vision_backbone': 'resnet18'},
 'prefetch_factor': 4,
 'rename_map': {},
 'resume': False,
 'reward_model': None,
 'sample_weighting': None,
 'save_checkpoint': True,
 'save_checkpoint_to_hub': False,
 'save_freq': 20000,
 'scheduler': None,
 'seed': 1000,
 'steps': 5000,
 'tolerance_s': 0.0001,
 'use_policy_training_preset': True,
 'wandb': {'add_tags': True,
           'disable_artifact': False,
           'enable': False,
           'entity': None,
           'mode': None,
           'notes': None,
           'project': 'lerobot',
           'run_id': None}}
INFO 2026-08-09 12:47:43 ot_train.py:243 Logs will be saved locally.
INFO 2026-08-09 12:47:43 ot_train.py:261 Creating dataset
INFO 2026-08-09 12:47:43 ot_train.py:295 Creating policy
INFO 2026-08-09 12:47:44 ot_train.py:368 Creating optimizer and scheduler
INFO 2026-08-09 12:47:44 ot_train.py:400 Output dir: outputs/train/so101_visual_trigger
INFO 2026-08-09 12:47:44 ot_train.py:407 cfg.steps=5000 (5K)
INFO 2026-08-09 12:47:44 ot_train.py:408 dataset.num_frames=20061 (20K)
INFO 2026-08-09 12:47:44 ot_train.py:409 dataset.num_episodes=35
INFO 2026-08-09 12:47:44 ot_train.py:412 Effective batch size: 8 x 1 = 8
INFO 2026-08-09 12:47:44 ot_train.py:413 num_learnable_params=51597190 (52M)
INFO 2026-08-09 12:47:44 ot_train.py:414 num_total_params=51597190 (52M)
Training:   0%|                                                                                                 | 0/5000 [00:00<?, ?step/s]INFO 2026-08-09 12:47:44 ot_train.py:565 Start offline training on a fixed dataset, with effective batch size: 8
objc[72357]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1109543a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x1299ec3a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72360]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1149503a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12e29c3a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72359]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112a483a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12c3943a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72358]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112bb43a8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12c5003a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72357]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1109543f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x1299ec3f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72360]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (objc[72359]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112a483f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12c3943f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
0x1149503f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12e29c3f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72358]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112bb43f8) and /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/av/.dylibs/libavdevice.61.3.100.dylib (0x12c5003f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72359]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112a483a8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x1319a0328). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72358]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112bb43a8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x131a20328). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72357]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1109543a8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x12f8e0328). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72360]: Class AVFFrameReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1149503a8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x1337bc328). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72358]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112bb43f8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x131a20378). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72360]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1149503f8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x1337bc378). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72359]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x112a483f8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x1319a0378). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
objc[72357]: Class AVFAudioReceiver is implemented in both /Users/r/Documents/Projects/lerobot/robot/lib/python3.13/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x1109543f8) and /opt/homebrew/Cellar/ffmpeg/8.1.2_1/lib/libavdevice.62.3.102.dylib (0x12f8e0378). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
Training:   4%|███▍                                                                                 | 200/5000 [03:33<1:44:35,  1.31s/step]INFO 2026-08-09 12:51:17 ot_train.py:609 step:200 smpl:2K ep:3 epch:0.08 loss:6.828 grdn:158.906 lr:1.0e-05 updt_s:1.053 data_s:0.017 smp/s:7 l1_loss:0.565 kld_loss:0.626
Training:   8%|██████▊                                                                              | 400/5000 [07:50<1:41:50,  1.33s/step]INFO 2026-08-09 12:55:34 ot_train.py:609 step:400 smpl:3K ep:6 epch:0.16 loss:2.982 grdn:87.313 lr:1.0e-05 updt_s:1.278 data_s:0.005 smp/s:6 l1_loss:0.430 kld_loss:0.255
Training:  12%|██████████▏                                                                          | 600/5000 [12:21<1:32:51,  1.27s/step]INFO 2026-08-09 13:00:05 ot_train.py:609 step:600 smpl:5K ep:8 epch:0.24 loss:2.509 grdn:75.913 lr:1.0e-05 updt_s:1.348 data_s:0.005 smp/s:6 l1_loss:0.398 kld_loss:0.211
Training:  16%|█████████████▌                                                                       | 800/5000 [16:47<1:32:26,  1.32s/step]INFO 2026-08-09 13:04:31 ot_train.py:609 step:800 smpl:6K ep:11 epch:0.32 loss:2.243 grdn:69.859 lr:1.0e-05 updt_s:1.327 data_s:0.005 smp/s:6 l1_loss:0.391 kld_loss:0.185
Training:  20%|████████████████▊                                                                   | 1000/5000 [21:02<1:25:07,  1.28s/step]INFO 2026-08-09 13:08:46 ot_train.py:609 step:1K smpl:8K ep:14 epch:0.40 loss:2.026 grdn:65.235 lr:1.0e-05 updt_s:1.270 data_s:0.004 smp/s:6 l1_loss:0.369 kld_loss:0.166
Training:  24%|████████████████████▏                                                               | 1200/5000 [25:18<1:22:21,  1.30s/step]INFO 2026-08-09 13:13:02 ot_train.py:609 step:1K smpl:10K ep:17 epch:0.48 loss:1.828 grdn:62.438 lr:1.0e-05 updt_s:1.276 data_s:0.004 smp/s:6 l1_loss:0.347 kld_loss:0.148
Training:  28%|███████████████████████▌                                                            | 1400/5000 [29:42<1:18:04,  1.30s/step]INFO 2026-08-09 13:17:26 ot_train.py:609 step:1K smpl:11K ep:20 epch:0.56 loss:1.658 grdn:58.996 lr:1.0e-05 updt_s:1.315 data_s:0.004 smp/s:6 l1_loss:0.319 kld_loss:0.134
Training:  32%|██████████████████████████▉                                                         | 1600/5000 [34:04<1:14:28,  1.31s/step]INFO 2026-08-09 13:21:48 ot_train.py:609 step:2K smpl:13K ep:22 epch:0.64 loss:1.515 grdn:57.129 lr:1.0e-05 updt_s:1.304 data_s:0.004 smp/s:6 l1_loss:0.295 kld_loss:0.122
Training:  36%|██████████████████████████████▏                                                     | 1800/5000 [38:27<1:09:31,  1.30s/step]INFO 2026-08-09 13:26:11 ot_train.py:609 step:2K smpl:14K ep:25 epch:0.72 loss:1.361 grdn:53.937 lr:1.0e-05 updt_s:1.312 data_s:0.004 smp/s:6 l1_loss:0.275 kld_loss:0.109
Training:  40%|█████████████████████████████████▌                                                  | 2000/5000 [42:56<1:07:06,  1.34s/step]INFO 2026-08-09 13:30:40 ot_train.py:609 step:2K smpl:16K ep:28 epch:0.80 loss:1.241 grdn:51.228 lr:1.0e-05 updt_s:1.340 data_s:0.004 smp/s:6 l1_loss:0.265 kld_loss:0.098
Training:  44%|████████████████████████████████████▉                                               | 2200/5000 [47:34<1:00:39,  1.30s/step]INFO 2026-08-09 13:35:18 ot_train.py:609 step:2K smpl:18K ep:31 epch:0.88 loss:1.130 grdn:48.492 lr:1.0e-05 updt_s:1.388 data_s:0.004 smp/s:6 l1_loss:0.255 kld_loss:0.087
Training:  48%|████████████████████████████████████████▎                                           | 2400/5000 [52:18<1:05:39,  1.52s/step]INFO 2026-08-09 13:40:02 ot_train.py:609 step:2K smpl:19K ep:33 epch:0.96 loss:1.034 grdn:46.498 lr:1.0e-05 updt_s:1.413 data_s:0.004 smp/s:6 l1_loss:0.250 kld_loss:0.078
Training:  52%|████████████████████████████████████████████▋                                         | 2600/5000 [57:11<58:36,  1.47s/step]INFO 2026-08-09 13:44:56 ot_train.py:609 step:3K smpl:21K ep:36 epch:1.04 loss:0.945 grdn:44.544 lr:1.0e-05 updt_s:1.463 data_s:0.005 smp/s:5 l1_loss:0.240 kld_loss:0.070
Training:  56%|███████████████████████████████████████████████                                     | 2800/5000 [1:02:07<55:48,  1.52s/step]INFO 2026-08-09 13:49:51 ot_train.py:609 step:3K smpl:22K ep:39 epch:1.12 loss:0.852 grdn:41.388 lr:1.0e-05 updt_s:1.470 data_s:0.005 smp/s:5 l1_loss:0.228 kld_loss:0.062
Training:  60%|██████████████████████████████████████████████████▍                                 | 3000/5000 [1:07:02<48:10,  1.45s/step]INFO 2026-08-09 13:54:46 ot_train.py:609 step:3K smpl:24K ep:42 epch:1.20 loss:0.777 grdn:39.840 lr:1.0e-05 updt_s:1.470 data_s:0.005 smp/s:5 l1_loss:0.223 kld_loss:0.055
Training:  64%|█████████████████████████████████████████████████████▊                              | 3200/5000 [1:11:49<43:38,  1.45s/step]INFO 2026-08-09 13:59:33 ot_train.py:609 step:3K smpl:26K ep:45 epch:1.28 loss:0.711 grdn:37.711 lr:1.0e-05 updt_s:1.432 data_s:0.005 smp/s:6 l1_loss:0.219 kld_loss:0.049
Training:  68%|█████████████████████████████████████████████████████████                           | 3400/5000 [1:16:43<40:09,  1.51s/step]INFO 2026-08-09 14:04:27 ot_train.py:609 step:3K smpl:27K ep:47 epch:1.36 loss:0.652 grdn:35.247 lr:1.0e-05 updt_s:1.463 data_s:0.005 smp/s:5 l1_loss:0.218 kld_loss:0.043
Training:  72%|████████████████████████████████████████████████████████████▍                       | 3600/5000 [1:21:39<36:14,  1.55s/step]INFO 2026-08-09 14:09:24 ot_train.py:609 step:4K smpl:29K ep:50 epch:1.44 loss:0.601 grdn:34.548 lr:1.0e-05 updt_s:1.478 data_s:0.005 smp/s:5 l1_loss:0.214 kld_loss:0.039
Training:  76%|███████████████████████████████████████████████████████████████▊                    | 3800/5000 [1:26:37<29:03,  1.45s/step]INFO 2026-08-09 14:14:21 ot_train.py:609 step:4K smpl:30K ep:53 epch:1.52 loss:0.561 grdn:33.228 lr:1.0e-05 updt_s:1.481 data_s:0.006 smp/s:5 l1_loss:0.207 kld_loss:0.035
Training:  80%|███████████████████████████████████████████████████████████████████▏                | 4000/5000 [1:31:40<23:29,  1.41s/step]INFO 2026-08-09 14:19:24 ot_train.py:609 step:4K smpl:32K ep:56 epch:1.60 loss:0.526 grdn:31.940 lr:1.0e-05 updt_s:1.511 data_s:0.006 smp/s:5 l1_loss:0.208 kld_loss:0.032
Training:  84%|██████████████████████████████████████████████████████████████████████▌             | 4200/5000 [1:36:26<19:05,  1.43s/step]INFO 2026-08-09 14:24:10 ot_train.py:609 step:4K smpl:34K ep:59 epch:1.67 loss:0.491 grdn:30.210 lr:1.0e-05 updt_s:1.422 data_s:0.005 smp/s:6 l1_loss:0.206 kld_loss:0.028
Training:  88%|█████████████████████████████████████████████████████████████████████████▉          | 4400/5000 [1:41:27<15:53,  1.59s/step]INFO 2026-08-09 14:29:11 ot_train.py:609 step:4K smpl:35K ep:61 epch:1.75 loss:0.455 grdn:28.993 lr:1.0e-05 updt_s:1.501 data_s:0.005 smp/s:5 l1_loss:0.199 kld_loss:0.026
Training:  92%|█████████████████████████████████████████████████████████████████████████████▎      | 4600/5000 [1:46:31<09:26,  1.42s/step]INFO 2026-08-09 14:34:15 ot_train.py:609 step:5K smpl:37K ep:64 epch:1.83 loss:0.426 grdn:28.267 lr:1.0e-05 updt_s:1.514 data_s:0.005 smp/s:5 l1_loss:0.195 kld_loss:0.023
Training:  96%|████████████████████████████████████████████████████████████████████████████████▋   | 4800/5000 [1:51:04<04:37,  1.39s/step]INFO 2026-08-09 14:38:48 ot_train.py:609 step:5K smpl:38K ep:67 epch:1.91 loss:0.405 grdn:26.768 lr:1.0e-05 updt_s:1.357 data_s:0.004 smp/s:6 l1_loss:0.196 kld_loss:0.021
Training: 100%|████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [1:55:46<00:00,  1.36s/step]INFO 2026-08-09 14:43:30 ot_train.py:609 step:5K smpl:40K ep:70 epch:1.99 loss:0.384 grdn:26.612 lr:1.0e-05 updt_s:1.405 data_s:0.004 smp/s:6 l1_loss:0.190 kld_loss:0.019
INFO 2026-08-09 14:43:30 ot_train.py:655 Checkpoint policy after step 5000
Training: 100%|████████████████████████████████████████████████████████████████████████████████████| 5000/5000 [1:55:46<00:00,  1.39s/step]
INFO 2026-08-09 14:43:30 ot_train.py:741 End of training
(robot) ➜  lerobot git:(main) ✗ lerobot-rollout \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbserial-11320 \
    --robot.id=my_follower_arm \
    --robot.cameras='{"main": {"type": "opencv", "index_or_path": 0, "width": 640, "height": 480, "fps": 30, "fourcc": "MJPG"}, "gripper": {"type": "opencv", "index_or_path": 1, "width": 320, "height": 240, "fps": 30, "fourcc": "MJPG"}}' \
    --policy.type=act \
    --policy.pretrained_path=outputs/train/so101_visual_trigger/checkpoints/last/pretrained_model \
    --policy.input_features='{"observation.state": {"type": "STATE", "shape": [6]}, "observation.images.main": {"type": "VISUAL", "shape": [3, 480, 640]}, "observation.images.gripper": {"type": "VISUAL", "shape": [3, 240, 320]}}' \
    --policy.output_features='{"action": {"type": "ACTION", "shape": [6]}}' \
    --policy.device=mps \
    --strategy.type=base \
    --fps=30 \
    --duration=20 \
    --interpolation_multiplier=5 \
    --task="Pick up the object and place it in the box"
