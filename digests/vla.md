# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-24 22:32 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Long-Horizon Manipulation via Trace-Conditioned VLA Planning](https://arxiv.org/abs/2604.21924v1)

**Authors:** Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu et al. (10 authors)

**Published:** 2026-04-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.21924v1) | [PDF](https://arxiv.org/pdf/2604.21924v1.pdf) | [Project Page](https://www.liuisabella.com/LoHoManip)

<details>
<summary>Abstract</summary>

Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining pla...

</details>

---

### [CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors](https://arxiv.org/abs/2604.21241v1)

**Authors:** Dachong Li, ZhuangZhuang Chen, Jin Zhang, Jianqiang Li

**Published:** 2026-04-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21241v1) | [PDF](https://arxiv.org/pdf/2604.21241v1.pdf) | [GitHub](https://github.com/corridorVLA)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose $CorridorVLA$, which predicts sparse spatial anchors as incremental physical changes (e.g., $Δ$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a corridor that guides a flow-matching action head: tra...

</details>

---

### [Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems](https://arxiv.org/abs/2604.21138v1)

**Authors:** Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan et al. (7 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21138v1) | [PDF](https://arxiv.org/pdf/2604.21138v1.pdf) | [GitHub](https://github.com/UCSB-NLP-Chang/navigate-cluster)

<details>
<summary>Abstract</summary>

Multi-robot control in cluttered environments is a challenging problem that involves complex physical constraints, including robot-robot collisions, robot-obstacle collisions, and unreachable motions. Successful planning in such settings requires joint optimization over high-level task planning and low-level motion planning, as violations of physical constraints may arise from failures at either level. However, jointly optimizing task and motion planning is difficult due to the complex parameter...

</details>

---

### [PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance](https://arxiv.org/abs/2604.20834v1)

**Authors:** Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian et al. (15 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20834v1) | [PDF](https://arxiv.org/pdf/2604.20834v1.pdf) | [Project Page](https://getterupper.github.io/PokeVLA)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-la...

</details>

---

### [Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics](https://arxiv.org/abs/2604.21017v1)

**Authors:** Open-H-Embodiment Consortium,  :, Nigel Nelson, Juo-Tung Chen, Jesse Haworth et al. (216 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21017v1) | [PDF](https://arxiv.org/pdf/2604.21017v1.pdf) | [Project Page](https://open-h.github.io/open-h-embodiment/)

<details>
<summary>Abstract</summary>

Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with s...

</details>

---

## Other Recent Papers

### [From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://arxiv.org/abs/2604.21391v1)

**Authors:** Yiming Zhong, Yaoyu He, Zemin Yang, Pengfei Tian, Yifan Huang et al. (8 authors)

**Published:** 2026-04-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21391v1) | [PDF](https://arxiv.org/pdf/2604.21391v1.pdf)

<details>
<summary>Abstract</summary>

Bridging high-level semantic understanding with low-level physical control remains a persistent challenge in embodied intelligence, stemming from the fundamental spatiotemporal scale mismatch between cognition and action. Existing generative VLA policies typically adopt a "Generation-from-Noise" paradigm, which disregards this disparity, leading to representation inefficiency and weak condition alignment during optimization. In this work, we propose ResVLA, an architecture that shifts the paradi...

</details>

---

### [ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/abs/2604.21232v1)

**Authors:** Xiyin Zeng, Yuyu Sun, Haoyang Li, Shouqiang Liu, Hao Wang

**Published:** 2026-04-23 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21232v1) | [PDF](https://arxiv.org/pdf/2604.21232v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action systems follow instructions to execute multi-step tasks in multimodal environments. Recent VLA approaches typically rely on post-hoc correction mechanisms or operate under fixed task decompositions and alignment schemes. However, once an intermediate step is mis-specified, local errors propagate through subsequent steps and eventually accumulate into cascading failures. To mitigate this compounding effect, we propose Predictive Alignment and Planning Architecture, a framew...

</details>

---

### [How VLAs (Really) Work In Open-World Environments](https://arxiv.org/abs/2604.21192v1)

**Authors:** Amir Rasouli, Yangzheng Wu, Zhiyuan Li, Rui Heng Yang, Xuan Zhao et al. (7 authors)

**Published:** 2026-04-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21192v1) | [PDF](https://arxiv.org/pdf/2604.21192v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) have been extensively used in robotics applications, achieving great success in various manipulation problems. More recently, VLAs have been used in long-horizon tasks and evaluated on benchmarks, such as BEHAVIOR1K (B1K), for solving complex household chores. The common metric for measuring progress in such benchmarks is success rate or partial score based on satisfaction of progress-agnostic criteria, meaning only the final states of the objects are conside...

</details>

---

### [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](https://arxiv.org/abs/2604.20472v1)

**Authors:** Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.20472v1) | [PDF](https://arxiv.org/pdf/2604.20472v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in vision-language-action (VLA) models for robotics have highlighted the importance of reliable uncertainty quantification in sequential tasks. However, assessing and improving calibration in such settings remains mostly unexplored, especially when only partial trajectories are observed. In this work, we formulate sequential calibration for episodic tasks, where task-success confidence is produced along an episode, while success is determined at the end of it. We introduce a sequ...

</details>

---

### [A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking](https://arxiv.org/abs/2604.20347v1)

**Authors:** Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.20347v1) | [PDF](https://arxiv.org/pdf/2604.20347v1.pdf)

<details>
<summary>Abstract</summary>

Ultrasound (US)-guided needle insertion is a critical yet challenging procedure due to dynamic imaging conditions and difficulties in needle visualization. Many methods have been proposed for automated needle insertion, but they often rely on hand-crafted pipelines with modular controllers, whose performance degrades in challenging cases. In this paper, a Vision-Language-Action (VLA) model is proposed for adaptive and automated US-guided needle insertion and tracking on a robotic ultrasound (RUS...

</details>

---

### [JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy](https://arxiv.org/abs/2604.20100v2)

**Authors:** Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li et al. (62 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20100v2) | [PDF](https://arxiv.org/pdf/2604.20100v2.pdf)

<details>
<summary>Abstract</summary>

Robotic autonomy in open-world environments is fundamentally limited by insufficient data diversity and poor cross-embodiment generalization. Existing robotic datasets are often limited in scale and task coverage, while relatively large differences across robot embodiments impede effective behavior knowledge transfer. To address these challenges, we propose JoyAI-RA, a vision-language-action (VLA) embodied foundation model tailored for generalizable robotic manipulation. JoyAI-RA presents a mult...

</details>

---

### [Cortex 2.0: Grounding World Models in Real-World Industrial Deployment](https://arxiv.org/abs/2604.20246v1)

**Authors:** Adriana Aida, Walid Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch et al. (28 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.20246v1) | [PDF](https://arxiv.org/pdf/2604.20246v1.pdf)

<details>
<summary>Abstract</summary>

Industrial robotic manipulation demands reliable long-horizon execution across embodiments, tasks, and changing object distributions. While Vision-Language-Action models have demonstrated strong generalization, they remain fundamentally reactive. By optimizing the next action given the current observation without evaluating potential futures, they are brittle to the compounding failure modes of long-horizon tasks. Cortex 2.0 shifts from reactive control to plan-and-act by generating candidate fu...

</details>

---
