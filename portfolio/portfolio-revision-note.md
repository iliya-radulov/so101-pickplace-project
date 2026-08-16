## Update — Data Poisoning Follow-Up

Since publishing this project, a reader pointed me toward Bühler & Schutera's paper *"Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics"* (2026), which demonstrates a striking result on **the exact same platform used here** — SO-101 + LeRobot: inserting just 3 poisoned episodes into a 320-episode pick-and-place dataset (~1%) was enough to fully backdoor the trained model. A hidden trigger word caused the arm to freeze into a single, useless joint configuration on command, while behaving completely normally otherwise — a silent, low-cost denial-of-service attack.

Given how directly this applies to the workflow documented on this page, I decided to reproduce a small-scale version of the attack on my own arm and dataset, as a hands-on way to understand the vulnerability rather than just reading about it. Details and results are below.

*Thanks to the commenter who flagged this — a good reminder that as open-source robotics gets easier to build, dataset trust and provenance become a real, practical concern, not just a theoretical one.*

**Reference:** Bühler, S. & Schutera, M. (2026). *Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics.* [ResearchGate](https://www.researchgate.net/publication/408522959_Imperio_smolVLA_The_Implications_of_Data_Poisoning_on_Open_Source_Robotics)
