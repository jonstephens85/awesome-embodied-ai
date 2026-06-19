# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-19 17:57 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models](https://arxiv.org/abs/2606.19784v1)

**Authors:** Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19784v1) | [PDF](https://arxiv.org/pdf/2606.19784v1.pdf) | [Project Page](https://equivla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist robot manipulation, yet they lack geometric inductive biases: policies trained at specific orientations require substantially more data to generalize across rotational configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer...

</details>

---

### [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531v1)

**Authors:** Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin et al. (10 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19531v1) | [PDF](https://arxiv.org/pdf/2606.19531v1.pdf) | [Project Page](https://zhangwenyao1.github.io/ImageWAM/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) commonly rely on video generation to bridge visual world modeling and robot control. However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction. These issues raise a simple question: Does world action model really need video generation? We...

</details>

---

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

## Other Recent Papers

### [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/abs/2606.20562v1)

**Authors:** Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20562v1) | [PDF](https://arxiv.org/pdf/2606.20562v1.pdf)

<details>
<summary>Abstract</summary>

Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling. World action models (WAMs) possess these capabilities by jointly modeling visual foresight and actions conditioned on both current and historical observations, making them a promising paradigm for robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of...

</details>

---

### [Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](https://arxiv.org/abs/2606.20285v1)

**Authors:** Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20285v1) | [PDF](https://arxiv.org/pdf/2606.20285v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models show strong capabilities in single and dual-arm robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from end-to-end learning, leveraging large vision-language backbones with continuous action prediction. However, as bimanual tasks become tightly coupled and execution constraints become critical, implicit coordination alone is insufficient to ensure reliable, interpretable, and stable behavior. In this work, we propose Co-VLA, a coo...

</details>

---

### [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)

**Authors:** Shihao Ji, HongXi Li, Zihui Song, Mingyu Li

**Published:** 2026-06-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20274v1) | [PDF](https://arxiv.org/pdf/2606.20274v1.pdf)

<details>
<summary>Abstract</summary>

Scaling end-to-end autonomous driving to complex, open-world environments requires perceptual models that generalize to anomalous scenarios and planners that produce kinematically valid trajectories. Existing paradigms face a distinct dichotomy between representational efficiency and generalization capacity. Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning. Conversely, sparse, query-based...

</details>

---

### [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246v1)

**Authors:** Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller et al. (20 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20246v1) | [PDF](https://arxiv.org/pdf/2606.20246v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference. In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise...

</details>

---

### [Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation](https://arxiv.org/abs/2606.20118v1)

**Authors:** Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.20118v1) | [PDF](https://arxiv.org/pdf/2606.20118v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have shown strong potential for general-purpose manipulation, yet they often fail on novel, out-of-distribution objects whose appearance or geometry deviates from the training distribution. The standard remedy is to collect multi-view teleoperation data for every failure case, but this scales poorly in both cost and time. We introduce Pose6DAug, a failure-driven data augmentation framework that turns a policy's own successful episodes into targeted demonstra...

</details>

---

### [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092v1)

**Authors:** Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong et al. (13 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20092v1) | [PDF](https://arxiv.org/pdf/2606.20092v1.pdf)

<details>
<summary>Abstract</summary>

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time. While existing memory-augmented methods utilize historical context, they either suffer from severe information bottlenecks, incur high latency via decoupled dual systems, or rely on unselective buffers that accumulate massive visual redundancies. To address these limitations, we introduce EventV...

</details>

---

### [Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory](https://arxiv.org/abs/2606.19998v1)

**Authors:** Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang et al. (7 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.19998v1) | [PDF](https://arxiv.org/pdf/2606.19998v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential. We observe that successful and failed rollouts carry systematically different information-theoretic signatures. Building on this, we formalize VLA control as a closed-loop information pipeline and derive the Triple Information-theoretic (Tri-Info) signals that ca...

</details>

---

### [Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation](https://arxiv.org/abs/2606.20458v1)

**Authors:** Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20458v1) | [PDF](https://arxiv.org/pdf/2606.20458v1.pdf)

<details>
<summary>Abstract</summary>

Learning-based planners for sidewalk navigation can generate diverse candidate trajectories in real time, yet their scoring functions often fail to select the best trajectory in challenging situations, outputting trajectories that make the mobile robot drive onto grass, toward pedestrians, or in the wrong direction, even when better candidates exist in the same set. We call this the trajectory scoring gap: in real-world sidewalk navigation, the gap between an anchor-based planner's top choice an...

</details>

---

### [Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation](https://arxiv.org/abs/2606.20135v1)

**Authors:** Jianing Guo, Fangzheng Chen, Zihao Mao, Wong Lik Hang Kenny, Zhenhong Wu et al. (15 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20135v1) | [PDF](https://arxiv.org/pdf/2606.20135v1.pdf)

<details>
<summary>Abstract</summary>

Flow matching has emerged as a standard paradigm for robotic manipulation owing to its strong expressive power for modelling complex, multimodal action distributions, alongside similar approaches like diffusion policy. However, existing methods rely on discretized action chunks, making them brittle to demonstrations collected at heterogeneous control frequencies and prone to temporally inconsistent actions that degrade control stability. In this paper, we propose Frequency-Aware Flow Matching (F...

</details>

---

### [Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2606.19565v1)

**Authors:** Navin Ranjan, Andreas Savakis

**Published:** 2026-06-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.19565v1) | [PDF](https://arxiv.org/pdf/2606.19565v1.pdf)

<details>
<summary>Abstract</summary>

We propose Mix-QVLA, a task-evidence-aware mixed-precision PTQ framework for VLA models. Mix-QVLA anchors each quantized variant to the full-precision action-token reference decision and evaluates whether quantization preserves task-relevant evidence across key VLA functional boundaries. It computes normalized gradient-weighted task-evidence maps from boundary activations and compares full-precision and quantized maps using evidence-mass and attribution-distribution distortion, capturing changes...

</details>

---

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
