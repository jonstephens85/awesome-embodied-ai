# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-18 23:27 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297v1)

**Authors:** Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin, Nikita Kurlaev, Daria Pugacheva et al. (13 authors)

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19297v1) | [PDF](https://arxiv.org/pdf/2606.19297v1.pdf) | [Project Page](https://tttonyalpha.github.io/act2answer/)

<details>
<summary>Abstract</summary>

Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control. We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action. Each ...

</details>

---

### [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](https://arxiv.org/abs/2606.18953v1)

**Authors:** Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18953v1) | [PDF](https://arxiv.org/pdf/2606.18953v1.pdf) | [Project Page](https://www.microsoft.com/en-us/research/articles/object-centric-residual-rl/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks, but their imitation-learning-based policies remain brittle in precise physical interactions due to compounding execution errors; Can a reinforcement learning policy trained purely in simulation improve the robustness of real-world VLAs zero-shot? Residual RL, which learns a corrective policy on top of a frozen VLA, offers a natural framework, but existing approaches face a fundamental sim-to-real dilemma: privi...

</details>

---

### [Uncertainty Quantification for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2606.18043v1)

**Authors:** Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella et al. (8 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.18043v1) | [PDF](https://arxiv.org/pdf/2606.18043v1.pdf) | [Project Page](tum-lsy.github.io/uq_vla/)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This presents a critical limitation for real-world deployment in non-stationary environments, where models inevitably encounter scenarios outside...

</details>

---

### [GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning](https://arxiv.org/abs/2606.17480v1)

**Authors:** Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi et al. (6 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17480v1) | [PDF](https://arxiv.org/pdf/2606.17480v1.pdf) | [Project Page](https://aigeeksgroup.github.io/GeneralVLA-2) | [GitHub](https://github.com/AIGeeksGroup/GeneralVLA-2)

<details>
<summary>Abstract</summary>

Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Sec...

</details>

---

## Other Recent Papers

### [Zero-Shot Long-Horizon Dexterous Manipulation via Multi-View 3D-Grounded VLM Reasoning](https://arxiv.org/abs/2606.19340v1)

**Authors:** Jisoo Kim, Sangwon Baik, Taeksoo Kim, Sungjoo Kim, Junyoung Lee et al. (7 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19340v1) | [PDF](https://arxiv.org/pdf/2606.19340v1.pdf)

<details>
<summary>Abstract</summary>

We present a zero-shot framework for long-horizon dexterous manipulation that grounds language instructions into executable 3D task plans from calibrated multi-view RGB images. Rather than training an end-to-end policy, our system uses a vision-language model (VLM) to produce reference-frame task grounding and primitive-level 2D keypoints, then lifts them into 3D via multi-view fusion. This lifting combines triangulation of view-wise VLM groundings with reference-view ray voting, which searches ...

</details>

---

### [Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation](https://arxiv.org/abs/2606.19194v1)

**Authors:** Yu Zhang, Kangyi Ji, Yongxiang Zou, Rongtao Xu, Feng Zheng et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19194v1) | [PDF](https://arxiv.org/pdf/2606.19194v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents an invertible neural network adapter for general robotic manipulation, designed to generate precise high-dimensional actions conditioned on multimodal observations, including visual, linguistic, and proprioceptive inputs, through a one-step denoising process. Built upon a flow-matching formulation, the proposed adapter effectively constrains the action generation trajectory within an invertible latent space, thereby enabling efficient and high-quality dexterous action synthes...

</details>

---

### [Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos](https://arxiv.org/abs/2606.18955v1)

**Authors:** Runze Xu, Yiluo Zhang, Jian Wang, Yu Wang, Jincheng Yu

**Published:** 2026-06-17 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18955v1) | [PDF](https://arxiv.org/pdf/2606.18955v1.pdf)

<details>
<summary>Abstract</summary>

Training generalist Vision-Language-Action(VLA) models typically requires massive, diverse robotic datasets with high-fidelity action annotations. While egocentric human manipulation videos are abundant and capture significant environmental diversity, the absence of action labels makes them difficult to use in conventional training paradigms. To address this, we propose a latent-action-based framework designed to extract general action priors from unlabeled human videos. The architecture feature...

</details>

---

### [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589v1)

**Authors:** Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She et al. (9 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18589v1) | [PDF](https://arxiv.org/pdf/2606.18589v1.pdf)

<details>
<summary>Abstract</summary>

Action chunking has become a common interface for vision-language-action (VLA) models, enabling low-frequency policy inference to drive high-frequency robot execution. However, once an action chunk is committed, its open-loop execution can be brittle under stochastic dynamics, hardware execution errors, and partial observability. We propose DREAM-Chunk, a test-time scaling method that augments chunking-based policies with a lightweight latent world model, without requiring additional policy fine...

</details>

---

### [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610v1)

**Authors:** Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi et al. (12 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18610v1) | [PDF](https://arxiv.org/pdf/2606.18610v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating generalist robot manipulation policies in the real world is expensive, slow, and difficult to scale. Action-conditioned video world models offer a scalable alternative by simulating policy rollouts. Autoregressive rollouts accumulate compounding errors, observations across multiple camera views must remain mutually consistent, and the evaluator must generalize to policies whose behaviors lie outside the training distribution. We address these challenges with SC3-Eval, a self-consisten...

</details>

---

### [VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision](https://arxiv.org/abs/2606.18426v1)

**Authors:** Gershom Seneviratne, Yohan Abeysinghe, Jianyu An, Vaibhav Shende, Dinesh Manocha

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18426v1) | [PDF](https://arxiv.org/pdf/2606.18426v1.pdf)

<details>
<summary>Abstract</summary>

We introduce VEGA, an approach for training navigation VisionLanguage-Action (VLA) models from unlabeled egocentric navigation videos. Internet-scale egocentric videos provide a scalable source of navigation-relevant visual observations, capturing cluttered scenes, close-range obstacles, and natural human motion through real-world spaces. However, these videos are not directly usable for policy learning because they do not provide obstacle-aware trajectories conditioned on explicit navigation go...

</details>

---

### [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](https://arxiv.org/abs/2606.18097v1)

**Authors:** Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao et al. (8 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18097v1) | [PDF](https://arxiv.org/pdf/2606.18097v1.pdf)

<details>
<summary>Abstract</summary>

Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an infinite-dimensional configuration space and deform continuously under contact with grippers, fixtures, and the workspace, making them a demanding benchmark for general dexterous manipulation. Despite their importance, policy development and comparison remain difficult: existing benchmarks are often tied to specific hardware s...

</details>

---

### [ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation](https://arxiv.org/abs/2606.17937v1)

**Authors:** Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu et al. (11 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17937v1) | [PDF](https://arxiv.org/pdf/2606.17937v1.pdf)

<details>
<summary>Abstract</summary>

Most Vision-Language-Action (VLA) models map observations directly to actions without explicit reasoning, limiting their capacity for reasoning-intensive long-horizon tasks. To address this, existing approaches adopt Chain-of-Thought (CoT) reasoning to enable subgoal decomposition and spatial anticipation. However, those methods lack a unified architecture for effective cross-modal reasoning and fail to explicitly include inverse reasoning ability based on the target state. We argue that manipul...

</details>

---

### [PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space](https://arxiv.org/abs/2606.17924v1)

**Authors:** Bochen Yang, Lianlei Shan

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17924v1) | [PDF](https://arxiv.org/pdf/2606.17924v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model...

</details>

---

### [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](https://arxiv.org/abs/2606.17598v1)

**Authors:** Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang et al. (10 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17598v1) | [PDF](https://arxiv.org/pdf/2606.17598v1.pdf)

<details>
<summary>Abstract</summary>

Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present MuseVLA, an adaptive multimodal sensing VLA model that integrates novel sensors as on-demand tools for robotic manipulation. Given a task ins...

</details>

---

### [WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation](https://arxiv.org/abs/2606.17463v1)

**Authors:** Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue et al. (9 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17463v1) | [PDF](https://arxiv.org/pdf/2606.17463v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off i...

</details>

---

### [Guava: An Effective and Universal Harness for Embodied Manipulation](https://arxiv.org/abs/2606.18363v1)

**Authors:** Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou et al. (8 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.18363v1) | [PDF](https://arxiv.org/pdf/2606.18363v1.pdf)

<details>
<summary>Abstract</summary>

Language models trained on large-scale vision-language data have demonstrated strong potential for embodied agents. Harnessing models through embodied tools use offers a promising alternative to end-to-end vision-language-action systems by combining high-level reasoning with external modules for perception, planning, and control. However, it remains unclear what makes an effective harness for embodied manipulation, and to what extent such a harness can unlock embodied capabilities in a wide rang...

</details>

---

### [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846v2)

**Authors:** Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li et al. (23 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17846v2) | [PDF](https://arxiv.org/pdf/2606.17846v2.pdf)

<details>
<summary>Abstract</summary>

Foundation models in language and multimodality achieve strong generalization by aligning heterogeneous data under a unified formulation and training at scale. In this report, we investigate whether this scaling recipe can be applied to robotic manipulation to achieve genuine generalization. This is challenging because, unlike text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in diversity, making alignment and scale simultaneously difficult. We present Qwen-Rob...

</details>

---
