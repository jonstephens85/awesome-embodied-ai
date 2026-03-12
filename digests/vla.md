# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-12 16:58 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control](https://arxiv.org/abs/2603.10448v1)

**Authors:** Teli Ma, Jia Zheng, Zifan Wang, Chuili Jiang, Andy Cui et al. (7 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10448v1) | [PDF](https://arxiv.org/pdf/2603.10448v1.pdf) | [Project Page](https://dit4dit.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively limited action data. Generative video models, by contrast, encode rich spatiotemporal structure and implicit physics, making them a compelling foundation for robotic manipulation. But their potentials are not fully explored in the literature. To bridge the g...

</details>

---

### [World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)

**Authors:** An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma et al. (9 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.10422v1) | [PDF](https://arxiv.org/pdf/2603.10422v1.pdf) | [Project Page](https://wm2act.github.io/)

<details>
<summary>Abstract</summary>

World Models (WMs) have emerged as a promising approach for post-training Vision-Language-Action (VLA) policies to improve robustness and generalization under environmental changes. However, most WM-based post-training methods rely on pixel-space supervision, making policies sensitive to pixel-level artifacts and hallucination from imperfect WM rollouts. We introduce World2Act, a post-training framework that aligns VLA actions directly with WM video-dynamics latents using a contrastive matching ...

</details>

---

### [Cross-Hand Latent Representation for Vision-Language-Action Models](https://arxiv.org/abs/2603.10158v1)

**Authors:** Guangqi Jiang, Yutong Liang, Jianglong Ye, Jia-Yang Huang, Changwei Jing et al. (9 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10158v1) | [PDF](https://arxiv.org/pdf/2603.10158v1.pdf) | [Project Page](https://xl-vla.github.io)

<details>
<summary>Abstract</summary>

Dexterous manipulation is essential for real-world robot autonomy, mirroring the central role of human hand coordination in daily activity. Humans rely on rich multimodal perception--vision, sound, and language-guided intent--to perform dexterous actions, motivating vision-based, language-conditioned manipulation systems for robots. However, training reliable vision-language-action (VLA) models for dexterous manipulation requires large-scale demonstrations across many robotic hands. In addition,...

</details>

---

### [TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation](https://arxiv.org/abs/2603.09971v1)

**Authors:** William Shen, Nishanth Kumar, Sahit Chintalapudi, Jie Wang, Christopher Watson et al. (10 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09971v1) | [PDF](https://arxiv.org/pdf/2603.09971v1.pdf) | [Project Page](and)

<details>
<summary>Abstract</summary>

We present TiPToP, an extensible modular system that combines pretrained vision foundation models with an existing Task and Motion Planner (TAMP) to solve multi-step manipulation tasks directly from input RGB images and natural-language instructions. Our system aims to be simple and easy-to-use: it can be installed and run on a standard DROID setup in under one hour and adapted to new embodiments with minimal effort. We evaluate TiPToP -- which requires zero robot data -- over 28 tabletop manipu...

</details>

---

### [Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks](https://arxiv.org/abs/2603.09513v1)

**Authors:** Wang Honghui, Jing Zhi, Ao Jicong, Song Shiji, Li Xuelong et al. (7 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09513v1) | [PDF](https://arxiv.org/pdf/2603.09513v1.pdf) | [Project Page](vqmemory.github.io)

<details>
<summary>Abstract</summary>

The high cost of collecting real-robot data has made robotic simulation a scalable platform for both evaluation and data generation. Yet most existing benchmarks concentrate on simple manipulation tasks such as pick-and-place, failing to capture the non-Markovian characteristics of real-world tasks and the complexity of articulated object interactions. To address this limitation, we present RuleSafe, a new articulated manipulation benchmark built upon a scalable LLM-aided simulation framework. R...

</details>

---

### [CORAL: Scalable Multi-Task Robot Learning via LoRA Experts](https://arxiv.org/abs/2603.09298v1)

**Authors:** Yuankai Luo, Woping Chen, Tong Liang, Zhenguo Li

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09298v1) | [PDF](https://arxiv.org/pdf/2603.09298v1.pdf) | [Project Page](https://frontierrobo.github.io/CORAL)

<details>
<summary>Abstract</summary>

Deploying Vision-Language-Action (VLA) models in real-world robotics exposes a core multi-task learning challenge: reconciling task interference in multi-task robotic learning. When multiple tasks are jointly fine-tuned in a single stage, gradients from different tasks can conflict, causing negative transfer and reducing per-task performance. Yet maintaining a separate full checkpoint per task is often storage- and deployment-prohibitive. To address this dilemma, we present CORAL, a backbone- an...

</details>

---

### [DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation](https://arxiv.org/abs/2603.09121v1)

**Authors:** Yifan Han, Zhongxi Chen, Yuxuan Zhao, Congsheng Xu, Yanming Shao et al. (8 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.09121v1) | [PDF](https://arxiv.org/pdf/2603.09121v1.pdf) | [Project Page](https://chenzhongxi-sjtu.github.io/dexhil/)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have demonstrated promising generalization capabilities in robotic manipulation, deploying them on specific and complex downstream tasks still demands effective post-training. In parallel, Human-in-the-Loop (HiL) learning has proven to be a powerful mechanism for refining robot policies. However, extending this paradigm to dexterous manipulation remains challenging: multi-finger control is high-dimensional, contact-intensive, and exhibits execution distr...

</details>

---

### [EvoDriveVLA: Evolving Autonomous Driving Vision-Language-Action Model via Collaborative Perception-Planning Distillation](https://arxiv.org/abs/2603.09465v1)

**Authors:** Jiajun Cao, Xiaoan Zhang, Xiaobao Wei, Liyuqiu Huang, Wang Zijian et al. (13 authors)

**Published:** 2026-03-10 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.09465v1) | [PDF](https://arxiv.org/pdf/2603.09465v1.pdf) | [GitHub](https://github.com/hey-cjj/EvoDriveVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have shown great promise for autonomous driving, yet they suffer from degraded perception after unfreezing the visual encoder and struggle with accumulated instability in long-term planning. To address these challenges, we propose EvoDriveVLA-a novel collaborative perception-planning distillation framework that integrates self-anchored perceptual constraints and oracle-guided trajectory optimization. Specifically, self-anchored visual distillation leverages self-anc...

</details>

---

### [See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation](https://arxiv.org/abs/2603.09292v1)

**Authors:** Tingjun Dai, Mingfei Han, Tingwen Du, Zhiheng Liu, Zhihui Li et al. (8 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.09292v1) | [PDF](https://arxiv.org/pdf/2603.09292v1.pdf) | [Project Page](https://tingjundai.github.io/SPRVLA/)

<details>
<summary>Abstract</summary>

Measurement of task progress through explicit, actionable milestones is critical for robust robotic manipulation. This progress awareness enables a model to ground its current task status, anticipate verifiable intermediate states, and detect and recover from failures when progress stalls. To embody this capability, we introduce See, Plan, Rewind (SPR), a progress-aware vision-language-action framework that dynamically grounds language instructions into a sequence of spatial subgoals. SPR operat...

</details>

---

## Other Recent Papers

### [DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](https://arxiv.org/abs/2603.11041v1)

**Authors:** Shuyao Shang, Bing Zhan, Yunfei Yan, Yuqi Wang, Yingyan Li et al. (12 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.11041v1) | [PDF](https://arxiv.org/pdf/2603.11041v1.pdf)

<details>
<summary>Abstract</summary>

We propose DynVLA, a driving VLA model that introduces a new CoT paradigm termed Dynamics CoT. DynVLA forecasts compact world dynamics before action generation, enabling more informed and physically grounded decision-making. To obtain compact dynamics representations, DynVLA introduces a Dynamics Tokenizer that compresses future evolution into a small set of dynamics tokens. Considering the rich environment dynamics in interaction-intensive driving scenarios, DynVLA decouples ego-centric and env...

</details>

---

### [FG-CLTP: Fine-Grained Contrastive Language Tactile Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.10871v1)

**Authors:** Wenxuan Ma, Chaofan Zhang, Yinghao Cai, Guocai Yao, Shaowei Cui et al. (6 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10871v1) | [PDF](https://arxiv.org/pdf/2603.10871v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in integrating tactile sensing into vision-language-action (VLA) models have demonstrated transformative potential for robotic perception. However, existing tactile representations predominantly rely on qualitative descriptors (e.g., texture), neglecting quantitative contact states such as force magnitude, contact geometry, and principal axis orientation, which are indispensable for fine-grained manipulation. To bridge this gap, we propose FG-CLTP, a fine-grained contrastive ...

</details>

---

### [FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model](https://arxiv.org/abs/2603.10712v1)

**Authors:** Xiaoxu Xu, Hao Li, Jinhui Ye, Yilun Chen, Jia Zeng et al. (10 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10712v1) | [PDF](https://arxiv.org/pdf/2603.10712v1.pdf)

<details>
<summary>Abstract</summary>

Predictive foresight is important to intelligent embodied agents. Since the motor execution of a robot is intrinsically constrained by its visual perception of environmental geometry, effectively anticipating the future requires capturing this tightly coupled visuomotor interplay. While recent vision-language-action models attempt to incorporate future guidance, they struggle with this joint modeling. Existing explicit methods divert capacity to task-irrelevant visual details, whereas implicit m...

</details>

---

### [DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference](https://arxiv.org/abs/2603.10469v1)

**Authors:** Yuquan Li, Lianjie Ma, Han Ding, Lijun Zhu

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10469v1) | [PDF](https://arxiv.org/pdf/2603.10469v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable generalist robotic manipulation but suffer from high inference latency. This bottleneck stems from the massive number of visual tokens processed by large language backbones. Existing methods either prune or merge tokens uniformly, degrading the spatial reasoning essential for robotic control. We present DepthCache, a training-free framework that leverages depth as a structural prior for visual token compression. It partitions observations into depth-bas...

</details>

---

### [Overcoming Visual Clutter in Vision Language Action Models via Concept-Gated Visual Distillation](https://arxiv.org/abs/2603.10340v1)

**Authors:** Sangmim Song, Sarath Kodagoda, Marc Carmichael, Karthick Thiyagarajan

**Published:** 2026-03-11 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10340v1) | [PDF](https://arxiv.org/pdf/2603.10340v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate impressive zero-shot generalization but frequently suffer from a "Precision-Reasoning Gap" in cluttered environments. This failure is driven by background-induced feature dilution, where high-frequency semantic noise corrupts the geometric grounding required for precise manipulation. To bridge this gap, we propose Concept-Gated Visual Distillation (CGVD), a training-free, model-agnostic inference framework that stabilizes VLA policies. CGVD operate...

</details>

---

### [AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models](https://arxiv.org/abs/2603.10126v1)

**Authors:** Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, Sombit Dey et al. (9 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.10126v1) | [PDF](https://arxiv.org/pdf/2603.10126v1.pdf)

<details>
<summary>Abstract</summary>

We propose a standalone autoregressive (AR) Action Expert that generates actions as a continuous causal sequence while conditioning on refreshable vision-language prefixes. In contrast to existing Vision-Language-Action (VLA) models and diffusion policies that reset temporal context with each new observation and predict actions reactively, our Action Expert maintains its own history through a long-lived memory and is inherently context-aware. This structure addresses the frequency mismatch betwe...

</details>

---

### [NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models](https://arxiv.org/abs/2603.09542v1)

**Authors:** Ziyue Zhu, Shangyang Wu, Shuai Zhao, Zhiqiu Zhao, Shengjie Li et al. (8 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09542v1) | [PDF](https://arxiv.org/pdf/2603.09542v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are formulated to ground instructions in visual context and generate action sequences for robotic manipulation. Despite recent progress, VLA models still face challenges in learning related and reusable primitives, reducing reliance on large-scale data and complex architectures, and enabling exploration beyond demonstrations. To address these challenges, we propose a novel Neuro-Symbolic Vision-Language-Action (NS-VLA) framework via online reinforcement learni...

</details>

---

### [StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving](https://arxiv.org/abs/2603.09482v1)

**Authors:** Yuan Gao, Dengyuan Hua, Mattia Piccinini, Finn Rasmus Schäfer, Korbinian Moller et al. (7 authors)

**Published:** 2026-03-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09482v1) | [PDF](https://arxiv.org/pdf/2603.09482v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Models (VLMs) bridge visual perception and linguistic reasoning. In Autonomous Driving (AD), this synergy has enabled Vision Language Action (VLA) models, which translate high-level multimodal understanding into driving behaviors, typically represented as future trajectories. However, existing VLA models mainly generate generic collision-free trajectories. Beyond collision avoidance, adapting to diverse driving styles (e.g., sporty, comfortable) is essential for personalized driv...

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

### [GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models](https://arxiv.org/abs/2603.09079v1)

**Authors:** Md Selim Sarowar, Omer Tariq, Sungho Kim

**Published:** 2026-03-10 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.09079v1) | [PDF](https://arxiv.org/pdf/2603.09079v1.pdf)

<details>
<summary>Abstract</summary>

VLA models encode visual observations as 2D patch tokens with no intrinsic geometric structure. We introduce GST-VLA with two contributions. First, the Gaussian Spatial Tokenizer (GST) converts frozen dense depth and frozen semantic patch features into $N_g{=}128$ anisotropic 3D Gaussian primitives, each parameterized by a metric residual mean $μ\in \mathbb{R}^3$, log-scale covariance $\log σ\in \mathbb{R}^3$, and learned opacity $α\in (0,1)$. The covariance eigenstructure encodes local surface ...

</details>

---
