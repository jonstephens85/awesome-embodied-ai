# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-16 22:30 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://arxiv.org/abs/2604.14125v1)

**Authors:** Tianshuo Yang, Guanyu Chen, Yutian Chen, Zhixuan Liang, Yitian Liu et al. (11 authors)

**Published:** 2026-04-15 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.14125v1) | [PDF](https://arxiv.org/pdf/2604.14125v1.pdf) | [Project Page](https://tianshuoy.github.io/HiVLA-page/)

<details>
<summary>Abstract</summary>

While end-to-end Vision-Language-Action (VLA) models offer a promising paradigm for robotic manipulation, fine-tuning them on narrow control data often compromises the profound reasoning capabilities inherited from their base Vision-Language Models (VLMs). To resolve this fundamental trade-off, we propose HiVLA, a visual-grounded-centric hierarchical framework that explicitly decouples high-level semantic planning from low-level motor control. In high-level part, a VLM planner first performs tas...

</details>

---

### [Unveiling the Surprising Efficacy of Navigation Understanding in End-to-End Autonomous Driving](https://arxiv.org/abs/2604.12208v1)

**Authors:** Zhihua Hua, Junli Wang, Pengfei LI, Qihao Jin, Bo Zhang et al. (9 authors)

**Published:** 2026-04-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.12208v1) | [PDF](https://arxiv.org/pdf/2604.12208v1.pdf) | [Project Page](SNG-VLA)

<details>
<summary>Abstract</summary>

Global navigation information and local scene understanding are two crucial components of autonomous driving systems. However, our experimental results indicate that many end-to-end autonomous driving systems tend to over-rely on local scene understanding while failing to utilize global navigation information. These systems exhibit weak correlation between their planning capabilities and navigation input, and struggle to perform navigation-following in complex scenarios. To overcome this limitat...

</details>

---

## Other Recent Papers

### [Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection](https://arxiv.org/abs/2604.13942v1)

**Authors:** Zhen Liu, Xinyu Ning, Zhe Hu, Xinxin Xie, Weize Li et al. (11 authors)

**Published:** 2026-04-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.13942v1) | [PDF](https://arxiv.org/pdf/2604.13942v1.pdf)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) systems have demonstrated strong capabilities in embodied manipulation. However, most existing VLA policies rely on limited observation windows and end-to-end action prediction, which makes them brittle in long-horizon, memory-dependent tasks with partial observability, occlusions, and multi-stage dependencies. Such tasks require not only precise visuomotor control, but also persistent memory, adaptive task decomposition, and explicit recovery from execution f...

</details>

---

### [Jump-Start Reinforcement Learning with Vision-Language-Action Regularization](https://arxiv.org/abs/2604.13733v1)

**Authors:** Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, Loris Roveda

**Published:** 2026-04-15 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.13733v1) | [PDF](https://arxiv.org/pdf/2604.13733v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) enables high-frequency, closed-loop control for robotic manipulation, but scaling to long-horizon tasks with sparse or imperfect rewards remains difficult due to inefficient exploration and poor credit assignment. Vision-Language-Action (VLA) models leverage large-scale multimodal pretraining to provide generalist, task-level reasoning, but current limitations hinder their direct use in fast and precise manipulation. In this paper, we propose Vision-Language-Action Ju...

</details>

---

### [Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap](https://arxiv.org/abs/2604.13654v1)

**Authors:** Hanxuan Chen, Jie Zheng, Siqi Yang, Tianle Zeng, Siwei Feng et al. (12 authors)

**Published:** 2026-04-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.13654v1) | [PDF](https://arxiv.org/pdf/2604.13654v1.pdf)

<details>
<summary>Abstract</summary>

Vision-and-Language Navigation for Unmanned Aerial Vehicles (UAV-VLN) represents a pivotal challenge in embodied artificial intelligence, focused on enabling UAVs to interpret high-level human commands and execute long-horizon tasks in complex 3D environments. This paper provides a comprehensive and structured survey of the field, from its formal task definition to the current state of the art. We establish a methodological taxonomy that charts the technological evolution from early modular and ...

</details>

---

### [Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models](https://arxiv.org/abs/2604.12908v1)

**Authors:** Zijian Song, Qichang Li, Jiawei Zhou, Zhenlong Yuan, Tianshui Chen et al. (7 authors)

**Published:** 2026-04-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.12908v1) | [PDF](https://arxiv.org/pdf/2604.12908v1.pdf)

<details>
<summary>Abstract</summary>

At its core, robotic manipulation is a problem of vision-to-geometry mapping ($f(v) \rightarrow G$). Physical actions are fundamentally defined by geometric properties like 3D positions and spatial relationships. Consequently, we argue that the foundation for generalizable robotic control should be a vision-geometry backbone, rather than the widely adopted vision-language or video models. Conventional VLA and video-predictive models rely on backbones pretrained on large-scale 2D image-text or te...

</details>

---

### [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447v1)

**Authors:** Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu et al. (11 authors)

**Published:** 2026-04-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.12447v1) | [PDF](https://arxiv.org/pdf/2604.12447v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit rich world knowledge from vision-language backbones and acquire executable skills via action demonstrations. However, existing evaluations largely focus on action execution success, leaving action policies loosely coupled with visual-linguistic semantics. This decoupling exposes a systematic vulnerability whereby correct action execution may induce unsafe outcomes under semantic risk. To expose this vulnerability, we introduce HazardArena, a benchmark ...

</details>

---
