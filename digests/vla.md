# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-14 17:07 UTC

**Papers found:** 5

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [AnySlot: Goal-Conditioned Vision-Language-Action Policies for Zero-Shot Slot-Level Placement](https://arxiv.org/abs/2604.10432v1)

**Authors:** Zhaofeng Hu, Sifan Zhou, Qinbo Zhang, Rongtao Xu, Qi Su et al. (6 authors)

**Published:** 2026-04-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.10432v1) | [PDF](https://arxiv.org/pdf/2604.10432v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have emerged as a versatile paradigm for generalist robotic manipulation. However, precise object placement under compositional language instructions remains a major challenge for modern monolithic VLA policies. Slot-level tasks require both reliable slot grounding and sub-centimeter execution accuracy. To this end, we propose AnySlot, a framework that reduces compositional complexity by introducing an explicit spatial visual goal as an intermediate represen...

</details>

---
