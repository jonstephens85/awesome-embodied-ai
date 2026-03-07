# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-07 16:28 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)

**Authors:** Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo

**Published:** 2026-03-05 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.04910v1) | [PDF](https://arxiv.org/pdf/2603.04910v1.pdf) | [GitHub](https://github.com/HarryLui98/code_vpwem)

<details>
<summary>Abstract</summary>

Imitation learning from human demonstrations has achieved significant success in robotic control, yet most visuomotor policies still condition on single-step observations or short-context histories, making them struggle with non-Markovian tasks that require long-term memory. Simply enlarging the context window incurs substantial computational and memory costs and encourages overfitting to spurious correlations, leading to catastrophic failures under distribution shift and violating real-time con...

</details>

---

### [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)

**Authors:** Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan et al. (7 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05117v1) | [PDF](https://arxiv.org/pdf/2603.05117v1.pdf) | [GitHub](https://github.com/Youqiang-Gui/SeedPolicy)

<details>
<summary>Abstract</summary>

Imitation Learning (IL) enables robots to acquire manipulation skills from expert demonstrations. Diffusion Policy (DP) models multi-modal expert behaviors but suffers performance degradation as observation horizons increase, limiting long-horizon manipulation. We propose Self-Evolving Gated Attention (SEGA), a temporal module that maintains a time-evolving latent state via gated attention, enabling efficient recurrent updates that compress long-horizon observations into a fixed-size representat...

</details>

---

## Other Recent Papers

### [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)

**Authors:** Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05487v1) | [PDF](https://arxiv.org/pdf/2603.05487v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) have shown remarkable progress towards embodied intelligence. While their architecture partially resembles that of Large Language Models (LLMs), VLAs exhibit higher complexity due to their multi-modal inputs/outputs and often hybrid nature of transformer and diffusion heads. This is part of the reason why insights from mechanistic interpretability in LLMs, which explain how the internal model representations relate to their output behavior, do not trivially t...

</details>

---

### [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410v1)

**Authors:** Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng et al. (8 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05410v1) | [PDF](https://arxiv.org/pdf/2603.05410v1.pdf)

<details>
<summary>Abstract</summary>

In the domain of humanoid robot control, the fusion of Vision-Language-Action (VLA) with whole-body control is essential for semantically guided execution of real-world tasks. However, existing methods encounter challenges in terms of low VLA inference efficiency or an absence of effective semantic guidance for whole-body control, resulting in instability in dynamic limb-coordinated tasks. To bridge this gap, we present a semantic-motion intent guided, physics-aware multi-brain VLA framework for...

</details>

---

### [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377v1)

**Authors:** Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum

**Published:** 2026-03-05 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.05377v1) | [PDF](https://arxiv.org/pdf/2603.05377v1.pdf)

<details>
<summary>Abstract</summary>

Open-world navigation requires robots to make decisions in complex everyday environments while adapting to flexible task requirements. Conventional navigation approaches often rely on dense 3D reconstruction and hand-crafted goal metrics, which limits their generalization across tasks and environments. Recent advances in vision--language navigation (VLN) and vision--language--action (VLA) models enable end-to-end policies conditioned on natural language, but typically require interactive trainin...

</details>

---

### [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)

**Authors:** Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan et al. (7 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05185v1) | [PDF](https://arxiv.org/pdf/2603.05185v1.pdf)

<details>
<summary>Abstract</summary>

Balancing high-level semantic reasoning with low-level reactive control remains a core challenge in visual robotic manipulation. While Vision-Language Models (VLMs) excel at cognitive planning, their inference latency precludes real-time execution. Conversely, fast Vision-Language-Action (VLA) models often lack the semantic depth required for complex, long-horizon tasks. To bridge this gap, we introduce Critic in the Loop, an adaptive hierarchical framework driven by dynamic VLM-Expert schedulin...

</details>

---

### [Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models](https://arxiv.org/abs/2603.05147v1)

**Authors:** Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci

**Published:** 2026-03-05 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05147v1) | [PDF](https://arxiv.org/pdf/2603.05147v1.pdf)

<details>
<summary>Abstract</summary>

Current research on Vision-Language-Action (VLA) models predominantly focuses on enhancing generalization through established reasoning techniques. While effective, these improvements invariably increase computational complexity and inference latency. Furthermore, these mechanisms are typically applied indiscriminately, resulting in the inefficient allocation of resources for trivial tasks while simultaneously failing to provide the uncertainty estimation necessary to prevent catastrophic failur...

</details>

---
