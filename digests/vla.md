# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-01-30 22:15 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation](https://arxiv.org/abs/2601.22153v1)

**Authors:** Haozhe Xie, Beichen Wen, Jiarui Zheng, Zhaoxi Chen, Fangzhou Hong et al. (7 authors)

**Published:** 2026-01-29 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.22153v1) | [PDF](https://arxiv.org/pdf/2601.22153v1.pdf) | [Project Page](https://www.infinitescript.com/project/dynamic-vla/) | [GitHub](https://github.com/hzxie/DynamicVLA)

<details>
<summary>Abstract</summary>

Manipulating dynamic objects remains an open challenge for Vision-Language-Action (VLA) models, which, despite strong generalization in static manipulation, struggle in dynamic scenarios requiring rapid perception, temporal anticipation, and continuous control. We present DynamicVLA, a framework for dynamic object manipulation that integrates temporal reasoning and closed-loop adaptation through three key designs: 1) a compact 0.4B VLA using a convolutional vision encoder for spatially efficient...

</details>

---

### [MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources](https://arxiv.org/abs/2601.22054v1)

**Authors:** Baorui Ma, Jiahui Yang, Donglin Di, Xuancheng Zhang, Jianxun Cui et al. (8 authors)

**Published:** 2026-01-29 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.22054v1) | [PDF](https://arxiv.org/pdf/2601.22054v1.pdf) | [Project Page](https://metric-anything.github.io/metric-anything-io/)

<details>
<summary>Abstract</summary>

Scaling has powered recent advances in vision foundation models, yet extending this paradigm to metric depth estimation remains challenging due to heterogeneous sensor noise, camera-dependent biases, and metric ambiguity in noisy cross-source 3D data. We introduce Metric Anything, a simple and scalable pretraining framework that learns metric depth from noisy, diverse 3D sources without manually engineered prompts, camera-specific modeling, or task-specific architectures. Central to our approach...

</details>

---

### [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334v1)

**Authors:** Brian Y. Tsui, Alan Y. Fang, Tiffany J. Hwu

**Published:** 2026-01-28 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2601.20334v1) | [PDF](https://arxiv.org/pdf/2601.20334v1.pdf) | [GitHub](https://github.com/robiemusketeer/faea-sim)

<details>
<summary>Abstract</summary>

Robotic manipulation has increasingly adopted vision-language-action (VLA) models, which achieve strong performance but typically require task-specific demonstrations and fine-tuning, and often generalize poorly under domain shift. We investigate whether general-purpose large language model (LLM) agent frameworks, originally developed for software engineering, can serve as an alternative control paradigm for embodied manipulation. We introduce FAEA (Frontier Agent as Embodied Agent), which appli...

</details>

---

## Other Recent Papers

### [MoE-ACT: Improving Surgical Imitation Learning Policies through Supervised Mixture-of-Experts](https://arxiv.org/abs/2601.21971v1)

**Authors:** Lorenzo Mazza, Ariel Rodriguez, Rayan Younis, Martin Lelis, Ortrun Hellig et al. (9 authors)

**Published:** 2026-01-29 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2601.21971v1) | [PDF](https://arxiv.org/pdf/2601.21971v1.pdf)

<details>
<summary>Abstract</summary>

Imitation learning has achieved remarkable success in robotic manipulation, yet its application to surgical robotics remains challenging due to data scarcity, constrained workspaces, and the need for an exceptional level of safety and predictability. We present a supervised Mixture-of-Experts (MoE) architecture designed for phase-structured surgical manipulation tasks, which can be added on top of any autonomous policy. Unlike prior surgical robot learning approaches that rely on multi-camera se...

</details>

---

### [CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation](https://arxiv.org/abs/2601.21712v1)

**Authors:** Xuanran Zhai, Binkai Ou, Yemin Wang, Hui Yi Leong, Qiaojun Yu et al. (7 authors)

**Published:** 2026-01-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.21712v1) | [PDF](https://arxiv.org/pdf/2601.21712v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models enable instruction following manipulation, yet dualarm deployment remains unsafe due to under modeled selfcollisions between arms and grasped objects. We introduce CoFreeVLA, which augments an endtoend VLA with a short horizon selfcollision risk estimator that predicts collision likelihood from proprioception, visual embeddings, and planned actions. The estimator gates risky commands, recovers to safe states via risk-guided adjustments, and shapes policy refin...

</details>

---

### [AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation](https://arxiv.org/abs/2601.21602v1)

**Authors:** Jianli Sun, Bin Tian, Qiyao Zhang, Chengxiang Li, Zihan Song et al. (8 authors)

**Published:** 2026-01-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.21602v1) | [PDF](https://arxiv.org/pdf/2601.21602v1.pdf)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have achieved remarkable success in ground-based embodied intelligence, their application to Aerial Manipulation Systems (AMS) remains a largely unexplored frontier. The inherent characteristics of AMS, including floating-base dynamics, strong coupling between the UAV and the manipulator, and the multi-step, long-horizon nature of operational tasks, pose severe challenges to existing VLA paradigms designed for static or 2D mobile bases. To bridge this ga...

</details>

---

### [IROS: A Dual-Process Architecture for Real-Time VLM-Based Indoor Navigation](https://arxiv.org/abs/2601.21506v1)

**Authors:** Joonhee Lee, Hyunseung Shin, Jeonggil Ko

**Published:** 2026-01-29 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2601.21506v1) | [PDF](https://arxiv.org/pdf/2601.21506v1.pdf)

<details>
<summary>Abstract</summary>

Indoor mobile robot navigation requires fast responsiveness and robust semantic understanding, yet existing methods struggle to provide both. Classical geometric approaches such as SLAM offer reliable localization but depend on detailed maps and cannot interpret human-targeted cues (e.g., signs, room numbers) essential for indoor reasoning. Vision-Language-Action (VLA) models introduce semantic grounding but remain strictly reactive, basing decisions only on visible frames and failing to anticip...

</details>

---

### [Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321v1)

**Authors:** Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li et al. (8 authors)

**Published:** 2026-01-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.20321v1) | [PDF](https://arxiv.org/pdf/2601.20321v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently emerged as powerful generalists for robotic manipulation. However, due to their predominant reliance on visual modalities, they fundamentally lack the physical intuition required for contact-rich tasks that require precise force regulation and physical reasoning. Existing attempts to incorporate vision-based tactile sensing into VLA models typically treat tactile inputs as auxiliary visual textures, thereby overlooking the underlying correlation ...

</details>

---

### [Shallow-π: Knowledge Distillation for Flow-based VLAs](https://arxiv.org/abs/2601.20262v1)

**Authors:** Boseong Jeon, Yunho Choi, Taehan Kim

**Published:** 2026-01-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.20262v1) | [PDF](https://arxiv.org/pdf/2601.20262v1.pdf)

<details>
<summary>Abstract</summary>

The growing demand for real-time robotic deployment necessitates fast and on-device inference for vision-language-action (VLA) models. Within the VLA literature, efficiency has been extensively studied at the token level, such as visual token pruning. In contrast, systematic transformer layer reduction has received limited attention and, to the best of our knowledge, has not been explored for flow-based VLA models under knowledge distillation. In this work, we propose Shallow-pi, a principled kn...

</details>

---
