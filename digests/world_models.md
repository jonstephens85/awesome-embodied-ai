# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-12 16:58 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075v1)

**Authors:** Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin et al. (13 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11075v1) | [PDF](https://arxiv.org/pdf/2602.11075v1.pdf) | [Project Page](https://opendrivelab.com/kai0-rl/)

<details>
<summary>Abstract</summary>

Despite the sustained scaling on model capacity and data acquisition, Vision-Language-Action (VLA) models remain brittle in contact-rich and dynamic manipulation tasks, where minor execution deviations can compound into failures. While reinforcement learning (RL) offers a principled path to robustness, on-policy RL in the physical world is constrained by safety risk, hardware cost, and environment reset. To bridge this gap, we present RISE, a scalable framework of robotic reinforcement learning ...

</details>

---

### [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983v1)

**Authors:** Qian Long, Yueze Wang, Jiaxi Song, Junbo Zhang, Peiyan Li et al. (16 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10983v1) | [PDF](https://arxiv.org/pdf/2602.10983v1.pdf) | [Project Page](\href{https://vista-wm.github.io/}{https://vista-wm.github.io})

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

### [Olaf-World: Orienting Latent Actions for Video World Modeling](https://arxiv.org/abs/2602.10104v1)

**Authors:** Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, Mike Zheng Shou

**Published:** 2026-02-10 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.10104v1) | [PDF](https://arxiv.org/pdf/2602.10104v1.pdf) | [Project Page](https://showlab.github.io/Olaf-World/) | [GitHub](https://github.com/showlab/Olaf-World)

<details>
<summary>Abstract</summary>

Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, the...

</details>

---

### [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.10090v2)

**Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, Yite Wang, Siwei Han et al. (8 authors)

**Published:** 2026-02-10 | **Categories:** cs.AI, cs.CL, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.10090v2) | [PDF](https://arxiv.org/pdf/2602.10090v2.pdf) | [GitHub](https://github.com/Snowflake-Labs/agent-world-model)

<details>
<summary>Abstract</summary>

Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (...

</details>

---

### [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856v1)

**Authors:** Yuhao Zheng, Li'an Zhong, Yi Wang, Rui Dai, Kaikui Liu et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2602.09856v1) | [PDF](https://arxiv.org/pdf/2602.09856v1.pdf) | [Project Page](https://amap-ml.github.io/Code2World/) | [GitHub](https://github.com/AMAP-ML/Code2World)

<details>
<summary>Abstract</summary>

Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generat...

</details>

---

## Other Recent Papers

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

### [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098v1)

**Authors:** Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10098v1) | [PDF](https://arxiv.org/pdf/2602.10098v1.pdf)

<details>
<summary>Abstract</summary>

Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a JEPA-style pretraining framework that sidesteps these pitfalls by design. The key idea is \emph{leakage-free state prediction}: a target encoder prod...

</details>

---

### [Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning](https://arxiv.org/abs/2602.10044v1)

**Authors:** Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, Dileep Kalathil, P. R. Kumar

**Published:** 2026-02-10 | **Categories:** cs.LG, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2602.10044v1) | [PDF](https://arxiv.org/pdf/2602.10044v1.pdf)

<details>
<summary>Abstract</summary>

Efficient exploration remains a central challenge in reinforcement learning (RL), particularly in sparse-reward environments. We introduce Optimistic World Models (OWMs), a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likelihood estimation (RBMLE) from adaptive control into deep RL. In contrast to upper confidence bound (UCB)-style exploration methods, OWMs incorporate optimism directly into model learning by augmentation with an optimi...

</details>

---

### [MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation](https://arxiv.org/abs/2602.09878v1)

**Authors:** Jiaxu Wang, Yicheng Jiang, Tianlun He, Jingkai Sun, Qiang Zhang et al. (11 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.09878v1) | [PDF](https://arxiv.org/pdf/2602.09878v1.pdf)

<details>
<summary>Abstract</summary>

World-model-based imagine-then-act becomes a promising paradigm for robotic manipulation, yet existing approaches typically support either purely image-based forecasting or reasoning over partial 3D geometry, limiting their ability to predict complete 4D scene dynamics. This work proposes a novel embodied 4D world model that enables geometrically consistent, arbitrary-view RGBD generation: given only a single-view RGBD observation as input, the model imagines the remaining viewpoints, which can ...

</details>

---

### [Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)

**Authors:** Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen et al. (6 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.09600v1) | [PDF](https://arxiv.org/pdf/2602.09600v1.pdf)

<details>
<summary>Abstract</summary>

Egocentric interactive world models are essential for augmented reality and embodied AI, where visual generation must respond to user input with low latency, geometric consistency, and long-term stability. We study egocentric interaction generation from a single scene image under free-space hand gestures, aiming to synthesize photorealistic videos in which hands enter the scene, interact with objects, and induce plausible world dynamics under head motion. This setting introduces fundamental chal...

</details>

---
