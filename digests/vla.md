# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-25 22:26 UTC

**Papers found:** 5

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
