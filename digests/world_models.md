# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-29 17:13 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1)

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel et al. (6 authors)

**Published:** 2026-07-28 | **Categories:** cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2607.26037v1) | [PDF](https://arxiv.org/pdf/2607.26037v1.pdf) | [Project Page](https://wonder-world-model.github.io/)

<details>
<summary>Abstract</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel cam...

</details>

---

### [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337v1)

**Authors:** Jiaxin Bai, Jiaxuan Xiong

**Published:** 2026-07-28 | **Categories:** cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.25337v1) | [PDF](https://arxiv.org/pdf/2607.25337v1.pdf) | [GitHub](https://github.com/HKBU-KnowComp/TD-JEPA)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, wh...

</details>

---

### [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/abs/2607.25236v1)

**Authors:** Jiaxin Bai, Jiaxuan Xiong

**Published:** 2026-07-28 | **Categories:** cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.25236v1) | [PDF](https://arxiv.org/pdf/2607.25236v1.pdf) | [GitHub](https://github.com/HKBU-KnowComp/VisualPatchWorld/)

<details>
<summary>Abstract</summary>

Different research lines use the term world model in different ways, yet they share a common aim: to capture how the world evolves under action in a form that supports perception, simulation, and planning. Two prominent realizations are neural predictors that learn dynamics in continuous vector spaces, and hand-built physics engines that expose explicit state and physical laws. Neural predictors scale from data but leave the form of the dynamics implicit; physics engines are inspectable and edit...

</details>

---

### [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](https://arxiv.org/abs/2607.23969v1)

**Authors:** Pei Liu, Nan Zheng, Lang Zhang, Daojie Peng, Yanan Zhang et al. (11 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.23969v1) | [PDF](https://arxiv.org/pdf/2607.23969v1.pdf) | [GitHub](https://github.com/LeapWM/leapbot-wa)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck. Forcing models to reconstruct task-irrelevant visual details dissipates representational capacity and renders policies vulnerable to visual distractors. In this paper, we propose LeapBot-WA, which establishes a novel Predictive-Latent paradigm for WAMs by operationalizing the Joint-Embedding Predictive Architecture...

</details>

---

## Other Recent Papers

### [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/abs/2607.26056v1)

**Authors:** Junhan Sun, Hao Zhao, Guofeng Zhang

**Published:** 2026-07-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26056v1) | [PDF](https://arxiv.org/pdf/2607.26056v1.pdf)

<details>
<summary>Abstract</summary>

Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search. We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface. Each transition supplies physical intent $z_{t+1}-z_t$, while a future goal supplies deployment intent $\operatorname{sg}(z_g)-z_t$. The architecture is isomorphic between the local and goal motion...

</details>

---

### [Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/abs/2607.26040v1)

**Authors:** Gaspard Lambrechts, Adrien Bolland, Daniel Ebi, Damien Ernst

**Published:** 2026-07-28 | **Categories:** cs.LG, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2607.26040v1) | [PDF](https://arxiv.org/pdf/2607.26040v1.pdf)

<details>
<summary>Abstract</summary>

Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available...

</details>

---

### [Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller](https://arxiv.org/abs/2607.25728v1)

**Authors:** Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf

**Published:** 2026-07-28 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.25728v1) | [PDF](https://arxiv.org/pdf/2607.25728v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised co...

</details>

---

### [Medical world models in healthcare: foundations, applications, and challenges for trustworthy clinical translation](https://arxiv.org/abs/2607.25242v1)

**Authors:** Zhaoyan Chen, Zhongxiu Cong, Zhuanfeng Jin, Wanshu Fan, Dongsheng Zhou et al. (10 authors)

**Published:** 2026-07-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.25242v1) | [PDF](https://arxiv.org/pdf/2607.25242v1.pdf)

<details>
<summary>Abstract</summary>

Medical world models offer a framework for extending medical artificial intelligence beyond static prediction by representing evolving patient states and modelling how they change over time and in response to clinical interventions. This Review defines the conceptual boundaries, technical foundations, application domains, and evidence requirements of the field through a structured narrative synthesis with reproducible evidence mapping.We screened 1,455 unique records and assembled a corpus of 98...

</details>

---

### [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720v1)

**Authors:** Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao

**Published:** 2026-07-27 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.24720v1) | [PDF](https://arxiv.org/pdf/2607.24720v1.pdf)

<details>
<summary>Abstract</summary>

Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, making it difficult to identify how planning ability is acquired, shaped, and integrated. To address this challenge, we introduce a unified and controlled multi-turn environment that enables precise control. It allows systematically study long-horizon planning across three stages. (1) Planning abilit...

</details>

---

### [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](https://arxiv.org/abs/2607.24481v1)

**Authors:** Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24481v1) | [PDF](https://arxiv.org/pdf/2607.24481v1.pdf)

<details>
<summary>Abstract</summary>

Real-world evaluation is a bottleneck in developing generalist robot manipulation policies. Each rollout requires physical hardware and an operator to set up, reset, and score it. We introduce ArmnetBench v0.1, a benchmark run on a fleet of low-cost SO-101 cells under light on-site supervision. v0.1 validates this arm farm end to end and compares 7 policies across 12 tasks with both single-arm and bimanual configurations. Each policy is trained or fine-tuned on 50 demonstrations per task; the be...

</details>

---

### [Context Is King: How In-Context Specification Shapes the Geometry of Concepts](https://arxiv.org/abs/2607.24425v1)

**Authors:** Elad David, Max Fomin

**Published:** 2026-07-27 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.24425v1) | [PDF](https://arxiv.org/pdf/2607.24425v1.pdf)

<details>
<summary>Abstract</summary>

Large language models place structured concepts on geometrically faithful manifolds: weekdays lie on a circle, months on another, usually taken to be a fixed world-model the network stores and looks up. We show that context is king: the structure a model actually uses is set by the in-context specification. A declarative rule fixes not only which relations the geometry encodes but its topology type: the same tokens form a cycle or a branching tree on command, built even on arbitrary, meaning-fre...

</details>

---

### [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](https://arxiv.org/abs/2607.24267v1)

**Authors:** Wenxuan Ma, Chaofan Zhang, Chao Xue, Yinghao Cai, Guocai Yao et al. (7 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24267v1) | [PDF](https://arxiv.org/pdf/2607.24267v1.pdf)

<details>
<summary>Abstract</summary>

Humans plan physical interactions by imagining the possible outcomes of candidate actions. However, existing visual world models primarily capture appearance dynamics while overlooking the tactile states that govern contact-rich interactions, potentially producing imagined futures that appear visually plausible but violate physical dynamics. We introduce FeelWorld, a hierarchical visuo-tactile world model that jointly predicts future visual latents and three tactile states. FeelWorld organizes t...

</details>

---

### [Scaling GUI Agents with Visual State Transitions](https://arxiv.org/abs/2607.24112v1)

**Authors:** Xiangyan Liu, Kaixin Li, Haonan Wang, Biao Wu, Meng Fang et al. (9 authors)

**Published:** 2026-07-27 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.24112v1) | [PDF](https://arxiv.org/pdf/2607.24112v1.pdf)

<details>
<summary>Abstract</summary>

We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents. During the STP stage, we continually pretrain a unified multimodal model on visual state transitions by jointly optimizing inverse dynamics (predicting actions from state changes) and forward dynamics (predicting next states from current states and actions). This optimization equips the model with better action-grounded visual representations and an internal world model of GUI dynamics. When subsequently fine-t...

</details>

---

### [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909v1)

**Authors:** Sen Wang, R. Gnana Praveen, Bidhan Roy, Marcos Villagra

**Published:** 2026-07-27 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.23909v1) | [PDF](https://arxiv.org/pdf/2607.23909v1.pdf)

<details>
<summary>Abstract</summary>

Many recent robot policies pursue stronger control by using large pretrained vision-language models (VLMs) as the action backbone. We introduce WorldDiT, a unified diffusion transformer architecture that couples action generation with visual world modeling and achieves strong performance without a large pretrained VLM action backbone. During training, a single diffusion transformer generates continuous action chunks and predicts normalized RGB patch targets from future camera frames. Across four...

</details>

---

### [Embodied GPT-5.1: Evidence of a World Model?](https://arxiv.org/abs/2607.23899v1)

**Authors:** Roberto Spinelli, Thiago C. Martins

**Published:** 2026-07-27 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.23899v1) | [PDF](https://arxiv.org/pdf/2607.23899v1.pdf)

<details>
<summary>Abstract</summary>

This exploratory study examines whether a large multimodal language model, GPT-5.1, can serve as the high-level controller of a physical mobile robot despite having no prior embodiment, no training in simulated environments, and no exposure to sensorimotor experience. Using only low-resolution first-person images and a discrete action set, the model was tasked with navigation and object-directed behaviors such as locating and contacting a target toy. Across multiple trials, GPT-5.1 demonstrated ...

</details>

---
