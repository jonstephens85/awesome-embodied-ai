# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-10 17:47 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action](https://arxiv.org/abs/2607.08182v1)

**Authors:** Qi Lyu, Baicheng Liu, Xudong Wang, Jiahua Dong, Lianqing Liu et al. (6 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.08182v1) | [PDF](https://arxiv.org/pdf/2607.08182v1.pdf) | [GitHub](https://github.com/LyuQi127/LEEVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models aim to map multimodal inputs to robot actions. However, most existing approaches struggle to cover complex dynamic scenarios due to treating all visual tokens uniformly and reasoning with human-selected factors, which lack mechanisms to emphasize task-critical evidence and ignore underlying factors. To address this issue, we propose LEEVLA, a VLA architecture for seeing what matters in Latent Environment Evolution that explicitly guides the model toward inform...

</details>

---

### [Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2607.07608v1)

**Authors:** Hongyu Qu, Jianzhe Gao, Xiaobin Hu, Shaohuan Yang, Xinlei Yu et al. (9 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.07608v1) | [PDF](https://arxiv.org/pdf/2607.07608v1.pdf) | [GitHub](https://github.com/quhongyu/LaMem-VLA)

<details>
<summary>Abstract</summary>

Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multim...

</details>

---

## Other Recent Papers

### [FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation](https://arxiv.org/abs/2607.08575v1)

**Authors:** Shiyuan Yang, Borong Zhang, Jizheng Zhang, Zhijia Tao, Junfei Guo et al. (8 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08575v1) | [PDF](https://arxiv.org/pdf/2607.08575v1.pdf)

<details>
<summary>Abstract</summary>

We present FabriVLA, a lightweight Vision-Language-Action model for Precise Multi-Task Manipulation. FabriVLA combines an InternVL3.5 vision-language backbone with a flow-matching action head featuring gated self-attention across action tokens and shallow VLM layer fusion for enriched spatial context. The model is trained via single stage joint optimization from a pretrained VLM and randomly initialized action head. On the Meta-World MT50 benchmark spanning 50 diverse manipulation tasks, FabriVL...

</details>

---

### [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448v1)

**Authors:** Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu et al. (16 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08448v1) | [PDF](https://arxiv.org/pdf/2607.08448v1.pdf)

<details>
<summary>Abstract</summary>

Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional rea...

</details>

---

### [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375v1)

**Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang et al. (8 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.08375v1) | [PDF](https://arxiv.org/pdf/2607.08375v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-V...

</details>

---

### [TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning](https://arxiv.org/abs/2607.08283v1)

**Authors:** Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang et al. (9 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08283v1) | [PDF](https://arxiv.org/pdf/2607.08283v1.pdf)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) policies such as $π_{0.5}$ and OpenVLA perform well on many manipulation tasks, but they are often reactive: the next action is predicted from the current observation, instruction, and proprioceptive state. This assumption breaks down in stage-dependent manipulation, where visually similar states may require different actions depending on latent task progress and previous interaction outcomes. We argue that such tasks require not only memory, but dynamics-aware bel...

</details>

---

### [Post-Training in End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08072v1)

**Authors:** Ruining Yang, Muxing Wang, Yixiao Chen, Tongfei Guo, Yi Xu et al. (11 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08072v1) | [PDF](https://arxiv.org/pdf/2607.08072v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end models that map multimodal inputs directly to future trajectories/maneuvers have emerged as an increasingly prominent research paradigm in autonomous driving. This class of models includes both Vision-Language-Action models and trajectory-generative planners. Unlike classic machine learning applications, autonomous vehicles operate in safety-critical and interaction-intensive environments where traditional open-loop imitation of expert demonstrations is not sufficient to ensure reliab...

</details>

---

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

### [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](https://arxiv.org/abs/2607.07287v2)

**Authors:** Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen et al. (12 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07287v2) | [PDF](https://arxiv.org/pdf/2607.07287v2.pdf)

<details>
<summary>Abstract</summary>

Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...

</details>

---
