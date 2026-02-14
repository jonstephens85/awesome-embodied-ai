# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-14 16:29 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion](https://arxiv.org/abs/2602.12215v1)

**Authors:** Jiangran Lyu, Kai Liu, Xuheng Zhang, Haoran Liao, Yusen Feng et al. (23 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.12215v1) | [PDF](https://arxiv.org/pdf/2602.12215v1.pdf) | [Project Page](https://pku-epic.github.io/LDA)

<details>
<summary>Abstract</summary>

Recent robot foundation models largely rely on large-scale behavior cloning, which imitates expert actions but discards transferable dynamics knowledge embedded in heterogeneous embodied data. While the Unified World Model (UWM) formulation has the potential to leverage such diverse data, existing instantiations struggle to scale to foundation-level due to coarse data usage and fragmented datasets. We introduce LDA-1B, a robot foundation model that scales through universal embodied data ingestio...

</details>

---

### [GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning](https://arxiv.org/abs/2602.12099v1)

**Authors:**  GigaBrain Team, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao et al. (25 authors)

**Published:** 2026-02-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.12099v1) | [PDF](https://arxiv.org/pdf/2602.12099v1.pdf) | [Project Page](https://gigabrain05m.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models that directly predict multi-step action chunks from current observations face inherent limitations due to constrained scene understanding and weak future anticipation capabilities. In contrast, video world models pre-trained on web-scale video corpora exhibit robust spatiotemporal reasoning and accurate future prediction, making them a natural foundation for enhancing VLA learning. Therefore, we propose \textit{GigaBrain-0.5M*}, a VLA model trained via world m...

</details>

---

### [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063v1)

**Authors:** Yanjiang Guo, Tony Lee, Lucy Xiaoyang Shi, Jianyu Chen, Percy Liang et al. (6 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.12063v1) | [PDF](https://arxiv.org/pdf/2602.12063v1.pdf) | [Project Page](https://sites.google.com/view/vla-w)

<details>
<summary>Abstract</summary>

The goal of this paper is to improve the performance and reliability of vision-language-action (VLA) models through iterative online interaction. Since collecting policy rollouts in the real world is expensive, we investigate whether a learned simulator-specifically, an action-conditioned video generation model-can be used to generate additional rollout data. Unfortunately, existing world models lack the physical fidelity necessary for policy improvement: they are predominantly trained on demons...

</details>

---

### [Accelerating Robotic Reinforcement Learning with Agent Guidance](https://arxiv.org/abs/2602.11978v1)

**Authors:** Haojun Chen, Zili Zou, Chengdong Ma, Yaoxiang Pu, Haotong Zhang et al. (7 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.11978v1) | [PDF](https://arxiv.org/pdf/2602.11978v1.pdf) | [Project Page](https://agps-rl.github.io/agps)

<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) offers a powerful paradigm for autonomous robots to master generalist manipulation skills through trial-and-error. However, its real-world application is stifled by severe sample inefficiency. Recent Human-in-the-Loop (HIL) methods accelerate training by using human corrections, yet this approach faces a scalability barrier. Reliance on human supervisors imposes a 1:1 supervision ratio that limits fleet expansion, suffers from operator fatigue over extended sessions, ...

</details>

---

### [Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning](https://arxiv.org/abs/2602.11882v1)

**Authors:** Suraj Ranganath, Anish Patnaik, Vaishak Menon

**Published:** 2026-02-12 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.11882v1) | [PDF](https://arxiv.org/pdf/2602.11882v1.pdf) | [GitHub](https://github.com/suraj-ranganath/DINO-MBQuant)

<details>
<summary>Abstract</summary>

Efficient spatial reasoning requires world models that remain reliable under tight precision budgets. We study whether low-bit planning behavior is determined mostly by total bitwidth or by where bits are allocated across modules. Using DINO-WM on the Wall planning task, we run a paired-goal mixed-bit evaluation across uniform, mixed, asymmetric, and layerwise variants under two planner budgets. We observe a consistent three-regime pattern: 8-bit and 6-bit settings remain close to FP16, 3-bit se...

</details>

---

### [HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model](https://arxiv.org/abs/2602.11758v1)

**Authors:** Dongting Li, Xingyu Chen, Qianyang Wu, Bo Chen, Sikai Wu et al. (13 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11758v1) | [PDF](https://arxiv.org/pdf/2602.11758v1.pdf) | [Project Page](https://haic-humanoid.github.io/)

<details>
<summary>Abstract</summary>

Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimatio...

</details>

---

## Other Recent Papers

### [The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics](https://arxiv.org/abs/2602.12218v1)

**Authors:** Christian Internò, Jumpei Yamaguchi, Loren Amdahl-Culleton, Markus Olhofer, David Klindt et al. (6 authors)

**Published:** 2026-02-12 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.12218v1) | [PDF](https://arxiv.org/pdf/2602.12218v1.pdf)

<details>
<summary>Abstract</summary>

Determining whether neural models internalize physical laws as world models, rather than exploiting statistical shortcuts, remains challenging, especially under out-of-distribution (OOD) shifts. Standard evaluations often test latent capability via downstream adaptation (e.g., fine-tuning or high-capacity probes), but such interventions can change the representations being measured and thus confound what was learned during self-supervised learning (SSL). We propose a non-invasive evaluation prot...

</details>

---

### [Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use](https://arxiv.org/abs/2602.11541v1)

**Authors:** Hanbing Liu, Chunhao Tian, Nan An, Ziyuan Wang, Pinyan Lu et al. (7 authors)

**Published:** 2026-02-12 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.11541v1) | [PDF](https://arxiv.org/pdf/2602.11541v1.pdf)

<details>
<summary>Abstract</summary>

We study budget-constrained tool-augmented agents, where a large language model must solve multi-step tasks by invoking external tools under a strict monetary budget. We formalize this setting as sequential decision making in context space with priced and stochastic tool executions, making direct planning intractable due to massive state-action spaces, high variance of outcomes and prohibitive exploration cost. To address these challenges, we propose INTENT, an inference-time planning framework ...

</details>

---
