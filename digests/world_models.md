# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-30 17:26 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/abs/2607.26754v1)

**Authors:** Zijun Lin, Zeqing Wang, Cheston Tan, Bihan Wen, Yeying Jin

**Published:** 2026-07-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.26754v1) | [PDF](https://arxiv.org/pdf/2607.26754v1.pdf) | [Project Page](https://jimntu.github.io/stateplay_page/)

<details>
<summary>Abstract</summary>

Recent game world models can generate visually realistic and interactive environments conditioned on player actions. However, games are not defined by pixels alone; they are governed by explicit mechanics, namely state-dependent rules that control health reduction, skill activation, and game termination. These mechanics depend on precise internal states, such as health points, skill meters, and timers, which are tightly coupled with visual observations and determine how gameplay evolves. Without...

</details>

---

### [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1)

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel et al. (6 authors)

**Published:** 2026-07-28 | **Categories:** cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2607.26037v1) | [PDF](https://arxiv.org/pdf/2607.26037v1.pdf) | [Project Page](https://wonder-world-model.github.io/)

<details>
<summary>Abstract</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel cam...

</details>

---

### [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337v2)

**Authors:** Jiaxin Bai, Jiaxuan Xiong

**Published:** 2026-07-28 | **Categories:** cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.25337v2) | [PDF](https://arxiv.org/pdf/2607.25337v2.pdf) | [GitHub](https://github.com/HKBU-KnowComp/Temporal-Distance-JEPA)

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

## Other Recent Papers

### [Mitigating Compounding Error via Video Representation Regularization](https://arxiv.org/abs/2607.27036v1)

**Authors:** Taiye Chen, Qi Zhang, Yisen Wang

**Published:** 2026-07-29 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.27036v1) | [PDF](https://arxiv.org/pdf/2607.27036v1.pdf)

<details>
<summary>Abstract</summary>

Video diffusion-based world models enable long autoregressive video generation for robotics, autonomous driving and simulation tasks, yet sliding-window autoregressive inference suffers from severe error accumulation that degrades frame quality over time. Although this phenomenon has been widely observed, the underlying mechanism of compounding error and how to achieve stable long-horizon generation remain largely unresolved. In this paper, we investigate the internal representation dynamics of ...

</details>

---

### [What Can Latent World Models Know? Physical Parameter Identifiability in Multimodal Predictive Representations](https://arxiv.org/abs/2607.27017v1)

**Authors:** Kaizhen Tan, Xin Xu, Siru Tao, Hanzhe Hong, Yang Feng et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27017v1) | [PDF](https://arxiv.org/pdf/2607.27017v1.pdf)

<details>
<summary>Abstract</summary>

A central premise of latent world models is that predicting the future forces a representation to internalize the physics of its environment. Which physical quantities does a trained latent actually contain, and what decides this? We answer with controlled interventions in POKEWORLD, an interactive environment whose visually identical objects hide mass, drag, and contact stiffness. A certificate-gated protocol first certifies each parameter as recoverable from raw observations, then measures whe...

</details>

---

### [Temporally Centered SIGReg Improves Multi-Task LeWorldModel Learning: From Analysis to Method](https://arxiv.org/abs/2607.26924v1)

**Authors:** Chang Liu, Fei Suo, Yanzhou Jin, Yusuke Iwasawa, Yutaka Matsuo et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26924v1) | [PDF](https://arxiv.org/pdf/2607.26924v1.pdf)

<details>
<summary>Abstract</summary>

Recent work on LeWorldModel (LeWM) has shown that the Sketched Isotropic Gaussian Regularizer (SIGReg) enables stable end-to-end world-model learning from pixels by regularizing the latent marginal distribution toward an isotropic Gaussian, thereby preventing representation collapse. While effective and elegant in single-task settings, this recipe does not extend reliably to multi-task training, leading to substantially worse downstream behavior-cloning performance. In this paper, we show that m...

</details>

---

### [CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2607.26789v1)

**Authors:** Yushan Liu, Peibo Sun, Xintao Chao, Zhenyang Yang, Yifan Xie et al. (11 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26789v1) | [PDF](https://arxiv.org/pdf/2607.26789v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores l...

</details>

---

### [CalTwin: Towards Calibrated, Shift-Robust Medical World Models via Fisher-Information Regularisation](https://arxiv.org/abs/2607.26752v1)

**Authors:** Behraj Khan, Shabir Ahmad, Syed Ahmad Chan Bukhari, Tahir Qasim Syed

**Published:** 2026-07-29 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.26752v1) | [PDF](https://arxiv.org/pdf/2607.26752v1.pdf)

<details>
<summary>Abstract</summary>

Medical world models aim to learn a latent state of patient or organ physiology and a transition function that forecasts how that state evolves under interventions, supporting downstream tasks from imaging-based diagnosis to digital-twin treatment planning. Two failure modes threaten the reliability of such models in clinical deployment: (i)~\emph{covariate shift}, because training data are fragmented across hospitals, scanners, and time, so the feature distribution seen by the latent-dynamics p...

</details>

---

### [ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games](https://arxiv.org/abs/2607.26712v1)

**Authors:** Zhenfeng Gan, ZiTong Zeng, Jiajun Cheng, Yeke Song, Yongyi Tang et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26712v1) | [PDF](https://arxiv.org/pdf/2607.26712v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models support efficient model-predictive control by optimizing future control sequences in latent space and replanning in a receding-horizon manner. However, existing latent predictors often lack stable long-horizon rollout ability, and prediction accuracy alone does not ensure that rollouts remain responsive to the actions being planned. We identify Context Collapse, a failure mode in which autoregressive latent predictors maintain high similarity to future states while producing ...

</details>

---

### [ContactFlow: A video action conditioning that transfers across embodiments](https://arxiv.org/abs/2607.26579v1)

**Authors:** Sami Azirar, Enrico Pallotta, Jan Nogga, Jürgen Gall, Sven Behnke et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.26579v1) | [PDF](https://arxiv.org/pdf/2607.26579v1.pdf)

<details>
<summary>Abstract</summary>

World models offer a promising route toward robot planning by enabling agents to imagine and verify the consequences of actions before execution. However, current video-based world models often struggle to capture the physical constraints that govern manipulation, particularly contact. Further, their action conditioning is often constrained to specific embodiments such as parallel grippers. We propose \emph{Contact Flow}, an embodiment-agnostic action representation that encodes manipulation thr...

</details>

---

### [CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/abs/2607.26452v1)

**Authors:** Yiming Cai, Fangjie Yu, Meiqing Yu, Ziyue Shi, Pengfei Yuan et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.AI, cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2607.26452v1) | [PDF](https://arxiv.org/pdf/2607.26452v1.pdf)

<details>
<summary>Abstract</summary>

World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure. We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines. CG-World explicitly records intermediate states, including multimodal semantics, spatial structure, skeletal and controller states, motion curves, camera and lighting parameters,...

</details>

---

### [Learning Implicit Causal World Models from Multi-Agent Demonstrations](https://arxiv.org/abs/2607.26336v1)

**Authors:** Jasorsi Ghosh

**Published:** 2026-07-28 | **Categories:** cs.LG, cs.MA, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26336v1) | [PDF](https://arxiv.org/pdf/2607.26336v1.pdf)

<details>
<summary>Abstract</summary>

In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to fail under distribution shift. We introduce Implicit Causal World Models to recover environmental dynamics from offline demonstrations without requiring pre-defined causal graphs. By inc...

</details>

---

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
