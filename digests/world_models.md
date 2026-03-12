# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-12 16:58 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)

**Authors:** An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma et al. (9 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.10422v1) | [PDF](https://arxiv.org/pdf/2603.10422v1.pdf) | [Project Page](https://wm2act.github.io/)

<details>
<summary>Abstract</summary>

World Models (WMs) have emerged as a promising approach for post-training Vision-Language-Action (VLA) policies to improve robustness and generalization under environmental changes. However, most WM-based post-training methods rely on pixel-space supervision, making policies sensitive to pixel-level artifacts and hallucination from imperfect WM rollouts. We introduce World2Act, a post-training framework that aligns VLA actions directly with WM video-dynamics latents using a contrastive matching ...

</details>

---

### [Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning](https://arxiv.org/abs/2603.09882v1)

**Authors:** Yixin Zheng, Jiangran Lyu, Yifan Zhang, Jiayi Chen, Mi Yan et al. (11 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.09882v1) | [PDF](https://arxiv.org/pdf/2603.09882v1.pdf) | [Project Page](https://pku-epic.github.io/DAPL/)

<details>
<summary>Abstract</summary>

Extrinsic dexterity leverages environmental contact to overcome the limitations of prehensile manipulation. However, achieving such dexterity in cluttered scenes remains challenging and underexplored, as it requires selectively exploiting contact among multiple interacting objects with inherently coupled dynamics. Existing approaches lack explicit modeling of such complex dynamics and therefore fall short in non-prehensile manipulation in cluttered environments, which in turn limits their practi...

</details>

---

### [Learning Convex Decomposition via Feature Fields](https://arxiv.org/abs/2603.09285v1)

**Authors:** Yuezhi Yang, Qixing Huang, Mikaela Angelina Uy, Nicholas Sharp

**Published:** 2026-03-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.09285v1) | [PDF](https://arxiv.org/pdf/2603.09285v1.pdf) | [Project Page](https://research.nvidia.com/labs/sil/projects/learning-convex-decomp/)

<details>
<summary>Abstract</summary>

This work proposes a new formulation to the long-standing problem of convex decomposition through learning feature fields, enabling the first feed-forward model for open-world convex decomposition. Our method produces high-quality decompositions of 3D shapes into a union of convex bodies, which are essential to accelerate collision detection in physical simulation, amongst many other applications. The key insight is to adopt a feature learning approach and learn a continuous feature field that c...

</details>

---

### [RAE-NWM: Navigation World Model in Dense Visual Representation Space](https://arxiv.org/abs/2603.09241v1)

**Authors:** Mingkun Zhang, Wangtian Shen, Fan Zhang, Haijian Qin, Zihao Pei et al. (6 authors)

**Published:** 2026-03-10 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09241v1) | [PDF](https://arxiv.org/pdf/2603.09241v1.pdf) | [GitHub](https://github.com/20robo/raenwm)

<details>
<summary>Abstract</summary>

Visual navigation requires agents to reach goals in complex environments through perception and planning. World models address this task by simulating action-conditioned state transitions to predict future observations. Current navigation world models typically learn state evolution under actions within the compressed latent space of a Variational Autoencoder, where spatial compression often discards fine-grained structural information and hinders precise control. To better understand the propag...

</details>

---

## Other Recent Papers

### [PPGuide: Steering Diffusion Policies with Performance Predictive Guidance](https://arxiv.org/abs/2603.10980v1)

**Authors:** Zixing Wang, Devesh K. Jha, Ahmed H. Qureshi, Diego Romeres

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10980v1) | [PDF](https://arxiv.org/pdf/2603.10980v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion policies have shown to be very efficient at learning complex, multi-modal behaviors for robotic manipulation. However, errors in generated action sequences can compound over time which can potentially lead to failure. Some approaches mitigate this by augmenting datasets with expert demonstrations or learning predictive world models which might be computationally expensive. We introduce Performance Predictive Guidance (PPGuide), a lightweight, classifier-based framework that steers a pr...

</details>

---

### [World Model for Battery Degradation Prediction Under Non-Stationary Aging](https://arxiv.org/abs/2603.10527v1)

**Authors:** Kai Chin Lim, Khay Wai See

**Published:** 2026-03-11 | **Categories:** cs.LG, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2603.10527v1) | [PDF](https://arxiv.org/pdf/2603.10527v1.pdf)

<details>
<summary>Abstract</summary>

Degradation prognosis for lithium-ion cells requires forecasting the state-of-health (SOH) trajectory over future cycles. Existing data-driven approaches can produce trajectory outputs through direct regression, but lack a mechanism to propagate degradation dynamics forward in time. This paper formulates battery degradation prognosis as a world model problem, encoding raw voltage, current, and temperature time-series from each cycle into a latent state and propagating it forward via a learned dy...

</details>

---

### [Towards a Neural Debugger for Python](https://arxiv.org/abs/2603.09951v1)

**Authors:** Maximilian Beck, Jonas Gehring, Jannik Kossen, Gabriel Synnaeve

**Published:** 2026-03-10 | **Categories:** cs.LG, cs.AI, cs.SE

**Links:** [arXiv](https://arxiv.org/abs/2603.09951v1) | [PDF](https://arxiv.org/pdf/2603.09951v1.pdf)

<details>
<summary>Abstract</summary>

Training large language models (LLMs) on Python execution traces grounds them in code execution and enables the line-by-line execution prediction of whole Python programs, effectively turning them into neural interpreters (FAIR CodeGen Team et al., 2025). However, developers rarely execute programs step by step; instead, they use debuggers to stop execution at certain breakpoints and step through relevant portions only while inspecting or modifying program variables. Existing neural interpreter ...

</details>

---

### [RESBev: Making BEV Perception More Robust](https://arxiv.org/abs/2603.09529v1)

**Authors:** Lifeng Zhuo, Kefan Jin, Zhe Liu, Hesheng Wang

**Published:** 2026-03-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.09529v1) | [PDF](https://arxiv.org/pdf/2603.09529v1.pdf)

<details>
<summary>Abstract</summary>

Bird's-eye-view (BEV) perception has emerged as a cornerstone of autonomous driving systems, providing a structured, ego-centric representation critical for downstream planning and control. However, real-world deployment faces challenges from sensor degradation and adversarial attacks, which can cause severe perceptual anomalies and ultimately compromise the safety of autonomous driving systems. To address this, we propose a resilient and plug-and-play BEV perception method, RESBev, which can be...

</details>

---

### [Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges](https://arxiv.org/abs/2603.09086v1)

**Authors:** Rongxiang Zeng, Yongqi Dong

**Published:** 2026-03-10 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.09086v1) | [PDF](https://arxiv.org/pdf/2603.09086v1.pdf)

<details>
<summary>Abstract</summary>

Emerging generative world models and vision-language-action (VLA) systems are rapidly reshaping automated driving by enabling scalable simulation, long-horizon forecasting, and capability-rich decision making. Across these directions, latent representations serve as the central computational substrate: they compress high-dimensional multi-sensor observations, enable temporally coherent rollouts, and provide interfaces for planning, reasoning, and controllable generation. This paper proposes a un...

</details>

---
