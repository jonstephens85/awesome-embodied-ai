# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-11 16:52 UTC

**Papers found:** 20

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [$Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation](https://arxiv.org/abs/2603.08361v1)

**Authors:** Yijie Zhu, Jie He, Rui Shao, Kaishen Yuan, Tao Tan et al. (7 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08361v1) | [PDF](https://arxiv.org/pdf/2603.08361v1.pdf) | [GitHub](https://github.com/JiuTian-VL/DeltaVLA)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models have significantly advanced robotic manipulation by unifying perception, reasoning, and control. To achieve such integration, recent studies adopt a predictive paradigm that models future visual states or world knowledge to guide action generation. However, these models emphasize forecasting outcomes rather than reasoning about the underlying process of change, which is essential for determining how to act. To address this, we propose $Δ$VLA, a prior-gu...

</details>

---

### [Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122v1)

**Authors:** Tutian Tang, Xingyu Ji, Wanli Xing, Ce Hao, Wenqiang Xu et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.08122v1) | [PDF](https://arxiv.org/pdf/2603.08122v1.pdf) | [Project Page](https://sites.google.com/view/mode-vla)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have demonstrated remarkable success in robotic manipulation, their application has largely been confined to low-degree-of-freedom end-effectors performing simple, vision-guided pick-and-place tasks. Extending these models to human-like, bimanual dexterous manipulation-specifically contact-rich in-hand operations-introduces critical challenges in high-fidelity data acquisition, multi-skill learning, and multimodal sensory fusion. In this paper, we propos...

</details>

---

### [Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation](https://arxiv.org/abs/2603.08260v1)

**Authors:** Cong Tai, Zhaoyu Zheng, Haixu Long, Hansheng Wu, Zhengbin Long et al. (15 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.08260v1) | [PDF](https://arxiv.org/pdf/2603.08260v1.pdf) | [Project Page](https://terminators2025.github.io/Seed2Scale.github.io)

<details>
<summary>Abstract</summary>

Existing data generation methods suffer from exploration limits, embodiment gaps, and low signal-to-noise ratios, leading to performance degradation during self-iteration. To address these challenges, we propose Seed2Scale, a self-evolving data engine that overcomes the data bottleneck through a heterogeneous synergy of "small-model collection, large-model evaluation, and target-model learning". Starting with as few as four seed demonstrations, the engine employs the lightweight Vision-Language-...

</details>

---

## Other Recent Papers

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

### [APPLV: Adaptive Planner Parameter Learning from Vision-Language-Action Model](https://arxiv.org/abs/2603.08862v1)

**Authors:** Yuanjie Lu, Beichen Wang, Zhengqi Wu, Yang Li, Xiaomin Lin et al. (7 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08862v1) | [PDF](https://arxiv.org/pdf/2603.08862v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous navigation in highly constrained environments remains challenging for mobile robots. Classical navigation approaches offer safety assurances but require environment-specific parameter tuning; end-to-end learning bypasses parameter tuning but struggles with precise control in constrained spaces. To this end, recent robot learning approaches automate parameter tuning while retaining classical systems' safety, yet still face challenges in generalizing to unseen environments. Recently, Vi...

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

### [SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving](https://arxiv.org/abs/2603.08113v1)

**Authors:** Zihan You, Hongwei Liu, Chenxu Dang, Zhe Wang, Sining Ang et al. (7 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08113v1) | [PDF](https://arxiv.org/pdf/2603.08113v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have shown promising capabilities in autonomous driving by leveraging the understanding and reasoning strengths of Large Language Models(LLMs).However, our empirical analysis reveals that directly applying existing token-level MoE mechanisms--which are inherited from LLM architectures--to VLA models results in unstable performance and safety degradation in autonomous driving, highlighting a misalignment between token-based expert specializat...

</details>

---

### [RAPID: Redundancy-Aware and Compatibility-Optimal Edge-Cloud Partitioned Inference for Diverse VLA models](https://arxiv.org/abs/2603.07949v1)

**Authors:** Zihao Zheng, Sicheng Tian, Hangyu Cao, Chenyue Li, Jiayu Chen et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.DC, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.07949v1) | [PDF](https://arxiv.org/pdf/2603.07949v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models are mainstream in embodied intelligence but face high inference costs. Edge-Cloud Collaborative (ECC) inference offers an effective fix by easing edge-device computing pressure to meet real-time needs. However, existing ECC frameworks are suboptimal for VLA models due to two challenges: (1) Mainstream environment-oriented edge-cloud partitioning methods are susceptible to interference from visual noise; (2) Existing edge-cloud partitioning methods overlook the...

</details>

---

### [DyQ-VLA: Temporal-Dynamic-Aware Quantization for Embodied Vision-Language-Action Models](https://arxiv.org/abs/2603.07904v1)

**Authors:** Zihao Zheng, Hangyu Cao, Sicheng Tian, Jiayu Chen, Maoliang Li et al. (12 authors)

**Published:** 2026-03-09 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.07904v1) | [PDF](https://arxiv.org/pdf/2603.07904v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are dominant in embodied intelligence but are constrained by inference overheads. While model quantization alleviates these bottlenecks for edge deployment, static quantization approaches remain suboptimal for VLAs due to two critical challenges: (1) Temporal-dynamic sensitivity, where fixed precision wastes resources by ignoring stage-varying error tolerances; and (2) Real-time allocation, where identifying real-time sensitivity to guide bit allocation remain...

</details>

---

### [RoboRouter: Training-Free Policy Routing for Robotic Manipulation](https://arxiv.org/abs/2603.07892v2)

**Authors:** Yiteng Chen, Zhe Cao, Hongjia Ren, Chenjie Yang, Wenbo Li et al. (12 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.07892v2) | [PDF](https://arxiv.org/pdf/2603.07892v2.pdf)

<details>
<summary>Abstract</summary>

Research on robotic manipulation has developed a diverse set of policy paradigms, including vision-language-action (VLA) models, vision-action (VA) policies, and code-based compositional approaches. Concrete policies typically attain high success rates on specific task distributions but lim-ited generalization beyond it. Rather than proposing an other monolithic policy, we propose to leverage the complementary strengths of existing approaches through intelligent policy routing. We introduce Robo...

</details>

---

### [SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action](https://arxiv.org/abs/2603.08124v1)

**Authors:** Xiang Shi, Wenlong Huang, Menglin Zou, Xinhai Sun

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08124v1) | [PDF](https://arxiv.org/pdf/2603.08124v1.pdf)

<details>
<summary>Abstract</summary>

We revisit Vision-Language-Action through a neuroscience-inspired triad. Biologically, the Cerebrum provides stable high-level multimodal priors and remains frozen; the Pons Adapter integrates these cortical features with real-time proprioceptive inputs and compiles intent into execution-ready tokens; and the Cerebellum (ParaCAT) performs fast, parallel categorical decoding for online control, with hysteresis/EMA/temperature/entropy for stability. A fixed-ratio schedule and two-stage feature cac...

</details>

---
