# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-11 16:52 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [PlayWorld: Learning Robot World Models from Autonomous Play](https://arxiv.org/abs/2603.09030v1)

**Authors:** Tenny Yin, Zhiting Mei, Zhonghe Zheng, Miyu Yamane, David Wang et al. (11 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.09030v1) | [PDF](https://arxiv.org/pdf/2603.09030v1.pdf) | [Project Page](https://robot-playworld.github.io/)

<details>
<summary>Abstract</summary>

Action-conditioned video models offer a promising path to building general-purpose robot simulators that can improve directly from data. Yet, despite training on large-scale robot datasets, current state-of-the-art video models still struggle to predict physically consistent robot-object interactions that are crucial in robotic manipulation. To close this gap, we present PlayWorld, a simple, scalable, and fully autonomous pipeline for training high-fidelity video world simulators from interactio...

</details>

---

### [MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.08572v1)

**Authors:** Yutong Shen, Hangxu Liu, Penghui Liu, Jiashuo Luo, Yongkang Zhang et al. (9 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.08572v1) | [PDF](https://arxiv.org/pdf/2603.08572v1.pdf) | [Project Page](https://syt2004.github.io/metaworldX/)

<details>
<summary>Abstract</summary>

Learning natural, stable, and compositionally generalizable whole-body control policies for humanoid robots performing simultaneous locomotion and manipulation (loco-manipulation) remains a fundamental challenge in robotics. Existing reinforcement learning approaches typically rely on a single monolithic policy to acquire multiple skills, which often leads to cross-skill gradient interference and motion pattern conflicts in high-degree-of-freedom systems. As a result, generated behaviors frequen...

</details>

---

### [Interactive World Simulator for Robot Policy Training and Evaluation](https://arxiv.org/abs/2603.08546v1)

**Authors:** Yixuan Wang, Rhythm Syed, Fangyu Wu, Mengchao Zhang, Aykut Onol et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08546v1) | [PDF](https://arxiv.org/pdf/2603.08546v1.pdf) | [Project Page](https://yixuanwang.me/interactive_world_sim)

<details>
<summary>Abstract</summary>

Action-conditioned video prediction models (often referred to as world models) have shown strong potential for robotics applications, but existing approaches are often slow and struggle to capture physically consistent interactions over long horizons, limiting their usefulness for scalable robot policy training and evaluation. We present Interactive World Simulator, a framework for building interactive world models from a moderate-sized robot interaction dataset. Our approach leverages consisten...

</details>

---

## Other Recent Papers

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

### [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519v1)

**Authors:** Xiaoquan Sun, Zetian Xu, Chen Cao, Zonghe Liu, Yihan Sun et al. (12 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.08519v1) | [PDF](https://arxiv.org/pdf/2603.08519v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate remarkable potential for generalizable robotic manipulation. The execution of complex multi-step behaviors in VLA models can be improved by robust instruction grounding, a critical component for effective control. However, current paradigms predominantly rely on coarse, high-level task instructions during supervised fine-tuning. This instruction grounding gap leaves models without explicit intermediate guidance, leading to severe compounding errors...

</details>

---

### [The Boiling Frog Threshold: Criticality and Blindness in World Model-Based Anomaly Detection Under Gradual Drift](https://arxiv.org/abs/2603.08455v1)

**Authors:** Zhe Hong

**Published:** 2026-03-09 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08455v1) | [PDF](https://arxiv.org/pdf/2603.08455v1.pdf)

<details>
<summary>Abstract</summary>

When an RL agent's observations are gradually corrupted, at what drift rate does it "wake up" -- and what determines this boundary? We study world model-based self-monitoring under continuous observation drift across four MuJoCo environments, three detector families (z-score, variance, percentile), and three model capacities. We find that (1) a sharp detection threshold $\varepsilon^*$ exists universally: below it, drift is absorbed as normal variation; above it, detection occurs rapidly. The th...

</details>

---

### [SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v1)

**Authors:** Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang et al. (13 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08403v1) | [PDF](https://arxiv.org/pdf/2603.08403v1.pdf)

<details>
<summary>Abstract</summary>

We introduce SPIRAL, a self-improving planning and iterative reflective action world modeling closed-loop framework that enables controllable long-horizon video generation conditioned on high-level semantic actions. Existing one-shot video generation models operate in open-loop, often resulting in incomplete action execution, weak semantic grounding, and temporal drift. SPIRAL formulates ActWM as a closed-loop think-act-reflect process, where generation proceeds step by step under explicit plann...

</details>

---

### [SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving](https://arxiv.org/abs/2603.08113v1)

**Authors:** Zihan You, Hongwei Liu, Chenxu Dang, Zhe Wang, Sining Ang et al. (7 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08113v1) | [PDF](https://arxiv.org/pdf/2603.08113v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have shown promising capabilities in autonomous driving by leveraging the understanding and reasoning strengths of Large Language Models(LLMs).However, our empirical analysis reveals that directly applying existing token-level MoE mechanisms--which are inherited from LLM architectures--to VLA models results in unstable performance and safety degradation in autonomous driving, highlighting a misalignment between token-based expert specializat...

</details>

---

### [Long-Short Term Agents for Pure-Vision Bronchoscopy Robotic Autonomy](https://arxiv.org/abs/2603.07909v1)

**Authors:** Junyang Wu, Mingyi Luo, Fangfang Xie, Minghui Zhang, Hanxiao Zhang et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.07909v1) | [PDF](https://arxiv.org/pdf/2603.07909v1.pdf)

<details>
<summary>Abstract</summary>

Accurate intraoperative navigation is essential for robot-assisted endoluminal intervention, but remains difficult because of limited endoscopic field of view and dynamic artifacts. Existing navigation platforms often rely on external localization technologies, such as electromagnetic tracking or shape sensing, which increase hardware complexity and remain vulnerable to intraoperative anatomical mismatch. We present a vision-only autonomy framework that performs long-horizon bronchoscopic naviga...

</details>

---
