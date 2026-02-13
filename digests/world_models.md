# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-13 22:23 UTC

**Papers found:** 16

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

### [Causal-JEPA: Learning World Models through Object-Level Latent Interventions](https://arxiv.org/abs/2602.11389v1)

**Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero

**Published:** 2026-02-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.11389v1) | [PDF](https://arxiv.org/pdf/2602.11389v1.pdf) | [Project Page](https://hazel-heejeong-nam.github.io/cjepa/) | [GitHub](https://github.com/galilai-group/cjepa)

<details>
<summary>Abstract</summary>

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By applying object-level masking that requires an object's state to be inferred from ot...

</details>

---

### [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075v1)

**Authors:** Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin et al. (13 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11075v1) | [PDF](https://arxiv.org/pdf/2602.11075v1.pdf) | [Project Page](https://opendrivelab.com/kai0-rl/)

<details>
<summary>Abstract</summary>

Despite the sustained scaling on model capacity and data acquisition, Vision-Language-Action (VLA) models remain brittle in contact-rich and dynamic manipulation tasks, where minor execution deviations can compound into failures. While reinforcement learning (RL) offers a principled path to robustness, on-policy RL in the physical world is constrained by safety risk, hardware cost, and environment reset. To bridge this gap, we present RISE, a scalable framework of robotic reinforcement learning ...

</details>

---

### [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983v2)

**Authors:** Qian Long, Yueze Wang, Jiaxi Song, Junbo Zhang, Peiyan Li et al. (16 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10983v2) | [PDF](https://arxiv.org/pdf/2602.10983v2.pdf) | [Project Page](\href{https://vista-wm.github.io/}{https://vista-wm.github.io})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are promising for generalist robot manipulation but remain brittle in out-of-distribution (OOD) settings, especially with limited real-robot data. To resolve the generalization bottleneck, we introduce a hierarchical Vision-Language-Action framework \our{} that leverages the generalization of large-scale pre-trained world model for robust and generalizable VIsual Subgoal TAsk decomposition VISTA. Our hierarchical framework \our{} consists of a world model as t...

</details>

---

### [ResWorld: Temporal Residual World Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2602.10884v1)

**Authors:** Jinqing Zhang, Zehua Fu, Zelin Xu, Wenying Dai, Qingjie Liu et al. (6 authors)

**Published:** 2026-02-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10884v1) | [PDF](https://arxiv.org/pdf/2602.10884v1.pdf) | [GitHub](https://github.com/mengtan00/ResWorld.git)

<details>
<summary>Abstract</summary>

The comprehensive understanding capabilities of world models for driving scenarios have significantly improved the planning accuracy of end-to-end autonomous driving frameworks. However, the redundant modeling of static regions and the lack of deep interaction with trajectories hinder world models from exerting their full effectiveness. In this paper, we propose Temporal Residual World Model (TR-World), which focuses on dynamic object modeling. By calculating the temporal residuals of scene repr...

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

### [H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model](https://arxiv.org/abs/2602.11291v1)

**Authors:** Wenyuan Chen, Jinbang Huang, Oscar Pang, Zhiyuan Li, Xiao Hu et al. (11 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11291v1) | [PDF](https://arxiv.org/pdf/2602.11291v1.pdf)

<details>
<summary>Abstract</summary>

World models are becoming central to robotic planning and control, as they enable prediction of future state transitions. Existing approaches often emphasize video generation or natural language prediction, which are difficult to directly ground in robot actions and suffer from compounding errors over long horizons. Traditional task and motion planning relies on symbolic logic world models, such as planning domains, that are robot-executable and robust for long-horizon reasoning. However, these ...

</details>

---

### [ContactGaussian-WM: Learning Physics-Grounded World Model from Videos](https://arxiv.org/abs/2602.11021v1)

**Authors:** Meizhong Wang, Wanxin Jin, Kun Cao, Lihua Xie, Yiguang Hong

**Published:** 2026-02-11 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.11021v1) | [PDF](https://arxiv.org/pdf/2602.11021v1.pdf)

<details>
<summary>Abstract</summary>

Developing world models that understand complex physical interactions is essential for advancing robotic planning and simulation.However, existing methods often struggle to accurately model the environment under conditions of data scarcity and complex contact-rich dynamic motion.To address these challenges, we propose ContactGaussian-WM, a differentiable physics-grounded rigid-body world model capable of learning intricate physical laws directly from sparse and contact-rich video sequences.Our f...

</details>

---

### [Say, Dream, and Act: Learning Video World Models for Instruction-Driven Robot Manipulation](https://arxiv.org/abs/2602.10717v1)

**Authors:** Songen Gu, Yunuo Cai, Tianyu Wang, Simo Wu, Yanwei Fu

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10717v1) | [PDF](https://arxiv.org/pdf/2602.10717v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation requires anticipating how the environment evolves in response to actions, yet most existing systems lack this predictive capability, often resulting in errors and inefficiency. While Vision-Language Models (VLMs) provide high-level guidance, they cannot explicitly forecast future states, and existing world models either predict only short horizons or produce spatially inconsistent frames. To address these challenges, we propose a framework for fast and predictive video-condi...

</details>

---

### [Affordances Enable Partial World Modeling with LLMs](https://arxiv.org/abs/2602.10390v1)

**Authors:** Khimya Khetarpal, Gheorghe Comanici, Jonathan Richens, Jeremy Shar, Fei Xia et al. (8 authors)

**Published:** 2026-02-11 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.10390v1) | [PDF](https://arxiv.org/pdf/2602.10390v1.pdf)

<details>
<summary>Abstract</summary>

Full models of the world require complex knowledge of immense detail. While pre-trained large models have been hypothesized to contain similar knowledge due to extensive pre-training on vast amounts of internet scale data, using them directly in a search procedure is inefficient and inaccurate. Conversely, partial models focus on making high quality predictions for a subset of state and actions: those linked through affordances that achieve user intents~\citep{khetarpal2020can}. Can we posit lar...

</details>

---
