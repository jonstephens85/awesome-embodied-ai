# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-09 23:02 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2607.07608v1)

**Authors:** Hongyu Qu, Jianzhe Gao, Xiaobin Hu, Shaohuan Yang, Xinlei Yu et al. (9 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.07608v1) | [PDF](https://arxiv.org/pdf/2607.07608v1.pdf) | [GitHub](https://github.com/quhongyu/LaMem-VLA)

<details>
<summary>Abstract</summary>

Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multim...

</details>

---

### [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](https://arxiv.org/abs/2607.06564v1)

**Authors:** Jiaming Liu, Qingpo Wuwu, Nuowei Han, Hao Chen, Zhuoyang Liu et al. (11 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.06564v1) | [PDF](https://arxiv.org/pdf/2607.06564v1.pdf) | [Project Page](https://lift3dvla.github.io/)

<details>
<summary>Abstract</summary>

Recently, Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse tasks. However, effective robotic manipulation in physical environments fundamentally requires geometric understanding and spatial reasoning. While some VLA approaches attempt to incorporate 3D information, they are constrained by limited data availability and geometric information loss in current 3D encoding pipelines, and fail to jointly capture 3D geometry and temporally structured actions in ...

</details>

---

### [SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models](https://arxiv.org/abs/2607.06442v1)

**Authors:** Changti Wu, Bin Yu, Zhaolong Shen, Shijie Lian, Xiaopeng Lin et al. (9 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06442v1) | [PDF](https://arxiv.org/pdf/2607.06442v1.pdf) | [GitHub](https://github.com/ChangtiWu/SIEVE}{SIEVE})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are typically trained by imitation learning on large-scale robot demonstration datasets, but more data does not necessarily yield better policies due to redundancy, noise, and uneven coverage. Existing data selection methods often assess demonstrations at either the trajectory or state-action level, missing the reusable structures that compose long-horizon behaviors. In this paper, we propose SIEVE, a structure-aware data selection method for VLA imitation lea...

</details>

---

### [From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403v1)

**Authors:** Wei Wu, Fangjing Wang, Fan Lu, He Sun, Shi Liu et al. (24 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06403v1) | [PDF](https://arxiv.org/pdf/2607.06403v1.pdf) | [Project Page](https://technology.robbyant.com/lingbot-vla-v2) | [GitHub](https://github.com/robbyant/lingbot-vla-v2)

<details>
<summary>Abstract</summary>

Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to the previous version, we revamp the data processing pipeline and curate around 60,000 hours of data for pretraining, including 50,000 hours ...

</details>

---

## Other Recent Papers

### [Smooth Operator: A Real-Time Sampling-Based Algorithm for Kinematic Hand Retargeting](https://arxiv.org/abs/2607.07491v1)

**Authors:** Robert Jomar Malate, Erik Bauer, Norica Bacuieti, Stefanos Charalambous, Elvis Nava et al. (7 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07491v1) | [PDF](https://arxiv.org/pdf/2607.07491v1.pdf)

<details>
<summary>Abstract</summary>

Advances in learning-based robotic manipulation, such as Vision-Language-Action (VLA) models and Video Action Models (VAMs), heavily rely on high-quality teleoperation data. Their capabilities are strictly upper-bounded by the quality of the underlying human demonstrations. Current gradient-based retargeting algorithms often converge to different local minima, resulting in jitter that affects data quality and teleoperation experience. To address this, we introduce the Sampling-Based Retargeter (...

</details>

---

### [Initiation Safety: A Missing Dimension in Generalist-Robot Safety](https://arxiv.org/abs/2607.07420v1)

**Authors:** Zhijin Meng, Francisco Cruz

**Published:** 2026-07-08 | **Categories:** cs.RO, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2607.07420v1) | [PDF](https://arxiv.org/pdf/2607.07420v1.pdf)

<details>
<summary>Abstract</summary>

Safety for generalist robots is usually discussed in terms of motion or dialogue. We argue a third question is missing: should the robot take its first hard-to-undo social action at all, such as a greeting, an uninvited grasp, or stepping into someone's space? We call this initiation authorization. Current frameworks rarely treat it as a separate safety layer. Today's stacks often skip this step: a high engagement score or a confident VLA rollout is treated as permission to act. But seeing a per...

</details>

---

### [Multi-Agent Robotic Control with Onboard Vision-Language Models](https://arxiv.org/abs/2607.07403v1)

**Authors:** Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek, Jakub Matejczyk, Dominik Matejkowski et al. (9 authors)

**Published:** 2026-07-08 | **Categories:** cs.MA, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07403v1) | [PDF](https://arxiv.org/pdf/2607.07403v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial wa...

</details>

---

### [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](https://arxiv.org/abs/2607.07287v1)

**Authors:** Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen et al. (12 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07287v1) | [PDF](https://arxiv.org/pdf/2607.07287v1.pdf)

<details>
<summary>Abstract</summary>

Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...

</details>

---

### [Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review](https://arxiv.org/abs/2607.06706v1)

**Authors:** Inkyu Sa, Chanoh Park, Hea-Min Lee, Donghee Noh, Ho Seok Ahn

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.06706v1) | [PDF](https://arxiv.org/pdf/2607.06706v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models unify visual perception, natural-language understanding, and action generation within a single foundation model, allowing a robot to follow instructions such as fold the towel or fly to the red building directly from camera images. Because VLAs inherit world knowledge from internet-scale pre-training, they have become the dominant framework for learning-based manipulation, with bimanual coordination serving as the most demanding testbed: two arms with 7 degree...

</details>

---

### [NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2607.06678v1)

**Authors:** Ziye Wang, Modi Shi, Chaojun Ni, Jiazhi Yang, Mengdi Li et al. (8 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06678v1) | [PDF](https://arxiv.org/pdf/2607.06678v1.pdf)

<details>
<summary>Abstract</summary>

How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA'...

</details>

---

### [Pelican-VLA 0.5: Attending Before Acting Benefits Generalization](https://arxiv.org/abs/2607.06655v1)

**Authors:** Zeyuan Ding, Wenhai Liu, Yang Xu, Jiayu Hu, Yinda Chen et al. (9 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.06655v1) | [PDF](https://arxiv.org/pdf/2607.06655v1.pdf)

<details>
<summary>Abstract</summary>

In this report, we present Pelican-VLA 0.5, a unified VLA model that integrates vision-language understanding, future-frame generation, and action prediction within a single architecture. Pelican-VLA 0.5 achieves attention-level generalization: without object annotations, segmentation masks, attention supervision, or task-specific fine-tuning, its action pathway already focuses on the instruction-relevant object and contact region. This behavior persists across unseen scenes and unseen robot emb...

</details>

---

### [Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement](https://arxiv.org/abs/2607.06370v1)

**Authors:** Ryuji Oi, Hikari Otsuka, Kosuke Matsushima, Yuki Ichikawa, Masato Motomura et al. (7 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.06370v1) | [PDF](https://arxiv.org/pdf/2607.06370v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for generalizable robotic manipulations. In particular, flow matching-based VLA models have shown remarkable success due to their capability to generate precise and smooth action sequences and capture multimodal distributions. However, the iterative denoising process in the action head acts as a major computational bottleneck, posing a critical challenge for real-time deployment. To address this challenge, we propose Action...

</details>

---

### [Optimal Transport Q-Learning for Flow Policy Steering and Acceleration](https://arxiv.org/abs/2607.06262v1)

**Authors:** Andreas Sochopoulos, Esmeralda S. Whitammer, Nikolaos Tsagkas, João Moura, Michael Gienger et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06262v1) | [PDF](https://arxiv.org/pdf/2607.06262v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion and flow policies have recently demonstrated remarkable performance in robotic applications by accurately capturing multimodal robot trajectory distributions, especially in the context of vision language action (VLA) models. However, high quality policy performance also requires fast inference and high quality demonstrations, which are often hard to get. Lack of these leads to suboptimal policy behaviors and failure under distribution shifts. In this work we address the problem of fine...

</details>

---

### [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256v1)

**Authors:** Ke Rui, Yushen Zuo, Jiawei Wang, Haoran Jia, Jinming Ma et al. (7 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06256v1) | [PDF](https://arxiv.org/pdf/2607.06256v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon household tasks require robots to compose many language-conditioned skills, yet the boundary between consecutive skills is rarely explicit. A skill may satisfy its own postcondition while leaving the robot, objects, or camera views in a state from which the next skill cannot reliably start. We study this semantic handoff problem in BEHAVIOR-1K through an agent-orchestrated vision-language-action execution harness. The harness invokes $π_{0.5}$-based skill checkpoints trained from cl...

</details>

---
