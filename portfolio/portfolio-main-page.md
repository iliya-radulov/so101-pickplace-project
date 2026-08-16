# Teaching a Robot Arm to See and Grasp

**A hands-on journey from a box of parts to autonomous pick-and-place, built on the SO-101 open-source robotic arm and LeRobot.**

---

## The Goal

Build a low-cost robotic arm from scratch, teach it a real manipulation task through human demonstration, and train a policy that lets it perform that task **completely autonomously** — no human in the loop.

This project is part of a larger roadmap toward a voice- and vision-integrated home robotics system, but this phase focused on one deceptively simple task: **pick up an object and place it in a target container.**

## The Approach

Rather than programming the arm's movements directly, this project used **imitation learning**: a human operator physically demonstrates the task dozens of times using a matching "leader" arm, and a neural network (ACT — Action Chunking Transformer) learns to reproduce that behavior from camera footage and joint positions alone.

The pipeline, in short:
1. **Assemble and calibrate** two identical 6-DOF robot arms — a "leader" (hand-operated) and a "follower" (does the actual work)
2. **Record demonstrations** — synchronized video and joint-position data while manually guiding the follower through the task
3. **Train a policy** — a vision-and-state-conditioned model that predicts what action to take next, given what it currently sees and its own position
4. **Run autonomously** — the trained model drives the follower arm in real time, using only its camera feed and current state, with no human input

## The Journey

The path from "box of parts" to "it actually works" was anything but linear:

- **Physical assembly and calibration** of both arms, including motor ID configuration and joint calibration
- **Migrating between platforms** — starting on a Raspberry Pi 4, discovering its hardware couldn't sustain real-time camera capture and arm control simultaneously, and moving the recording/training workflow to a Mac with GPU-accelerated (MPS) training
- **A first working dataset and model** — 30 episodes, single camera, first autonomous attempt: the arm reached toward the object but never quite grasped it
- **Diagnosing the gap** — reviewing the training footage revealed the camera never actually showed the gripper closing on the object, so the model had no visual signal for what a successful grasp looked like
- **Adding a second camera** — a close-up view of the gripper itself, alongside the original workspace overview
- **Hardware troubleshooting** — unreliable USB camera behavior traced back to an underpowered hub; solved by switching to a powered hub
- **Iterating on data quality** — an early dual-camera dataset with too few episodes and too much position variation produced confused, unreliable behavior; tightening the object's position and increasing to 30 episodes fixed it
- **Success** — a fully autonomous grasp-lift-place sequence, completed without any human input

## The Result

✅ **The follower arm autonomously picks up an object and places it accurately in a target container**, using only its own camera feeds and a trained neural network — no teleoperation, no scripted motion.

Early testing also revealed the model's current limits: it's most reliable within a band of positions resembling its training data, and sensitive to the object's orientation — expected characteristics of a first model trained on a modest, fairly consistent dataset, and a clear, concrete direction for the next iteration.

*Technical details, exact configurations, and the full troubleshooting log are on the [technical deep-dive page →](tech-details.md)*

---

*Video and photos of the arm in action below.*
