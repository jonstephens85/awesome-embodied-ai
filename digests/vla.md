# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-15 22:33 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Unveiling the Surprising Efficacy of Navigation Understanding in End-to-End Autonomous Driving](https://arxiv.org/abs/2604.12208v1)

**Authors:** Zhihua Hua, Junli Wang, Pengfei LI, Qihao Jin, Bo Zhang et al. (9 authors)

**Published:** 2026-04-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.12208v1) | [PDF](https://arxiv.org/pdf/2604.12208v1.pdf) | [Project Page](SNG-VLA)

<details>
<summary>Abstract</summary>

Global navigation information and local scene understanding are two crucial components of autonomous driving systems. However, our experimental results indicate that many end-to-end autonomous driving systems tend to over-rely on local scene understanding while failing to utilize global navigation information. These systems exhibit weak correlation between their planning capabilities and navigation input, and struggle to perform navigation-following in complex scenarios. To overcome this limitat...

</details>

---

### [StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems](https://arxiv.org/abs/2604.11757v1)

**Authors:** Jinhui Ye, Ning Gao, Senqiao Yang, Jinliang Zheng, Zixuan Wang et al. (10 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.11757v1) | [PDF](https://arxiv.org/pdf/2604.11757v1.pdf) | [GitHub](https://github.com/starVLA/starVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for building general-purpose robotic agents. However, the VLA landscape remains highly fragmented and complex: as existing approaches vary substantially in architectures, training data, embodiment configurations, and benchmark-specific engineering. In this work, we introduce StarVLA-$α$, a simple yet strong baseline designed to study VLA design choices under controlled conditions. StarVLA-$α$ deliberately minimizes...

</details>

---

### [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689v1)

**Authors:** Dujun Nie, Fengjiao Chen, Qi Lv, Jun Kuang, Xiaoyu Li et al. (7 authors)

**Published:** 2026-04-13 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.11689v1) | [PDF](https://arxiv.org/pdf/2604.11689v1.pdf) | [Project Page](https://meituan-longcat.github.io/LARYBench) | [GitHub](https://github.com/meituan-longcat/LARYBench)

<details>
<summary>Abstract</summary>

While the shortage of explicit action data limits Vision-Language-Action (VLA) models, human action videos offer a scalable yet unlabeled data source. A critical challenge in utilizing large-scale human video datasets lies in transforming visual signals into ontology-independent representations, known as latent actions. However, the capacity of latent action representation to derive robust control from visual observations has yet to be rigorously evaluated. We introduce the Latent Action Represe...

</details>

---

## Other Recent Papers

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

### [Grounded World Model for Semantically Generalizable Planning](https://arxiv.org/abs/2604.11751v1)

**Authors:** Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang et al. (7 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.11751v1) | [PDF](https://arxiv.org/pdf/2604.11751v1.pdf)

<details>
<summary>Abstract</summary>

In Model Predictive Control (MPC), world models predict the future outcomes of various action proposals, which are then scored to guide the selection of the optimal action. For visuomotor MPC, the score function is a distance metric between a predicted image and a goal image, measured in the latent space of a pretrained vision encoder like DINO and JEPA. However, it is challenging to obtain the goal image in advance of the task execution, particularly in new environments. Additionally, conveying...

</details>

---

### [DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2604.11572v1)

**Authors:** Siyuan Xu, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.MM

**Links:** [arXiv](https://arxiv.org/abs/2604.11572v1) | [PDF](https://arxiv.org/pdf/2604.11572v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) have demonstrated strong potential for embodied AI, yet their deployment on resource-limited robots remains challenging due to high memory and computational demands. While Post-Training Quantization (PTQ) provides an efficient solution, directly applying PTQ to VLAs often results in severe performance degradation during sequential control. We identify temporal error accumulation as a key factor, where quantization perturbations at the vision-language-to-actio...

</details>

---
