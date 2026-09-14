# What's New

Papers discovered in the run at **2026-09-14 20:09 UTC**.

**New this run:** 12

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (5)

### [DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2609.12316)

**Authors:** Samrat Sahoo, Yixuan Huang, Tom Silver

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12316) | [PDF](https://arxiv.org/pdf/2609.12316)

<details>
<summary>Abstract</summary>

Collecting high-quality robot data remains a fundamental challenge for training robot foundation models. Task and motion planning (TAMP) offers a scalable way to generate demonstrations, but our experiments show that raw TAMP trajectories provide surprisingly little benefit when used to fine-tune pretrained vision-language-action (VLA) models, despite successfully solving the target tasks. We hypothesize that this failure arises from a behavioral distribution mismatch between planner-generated trajectories and the data used to pretrain the VLA. To address this mismatch, we introduce DATAFARM:...

</details>

<details>
<summary>Share</summary>

```
DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models

Collecting high-quality robot data remains a fundamental challenge for training robot foundation models.

arXiv: https://arxiv.org/abs/2609.12316

#VLA #robotics
```

</details>

---

### [READ: Learning Risk-Informed Fields for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.12371)

**Authors:** Zhiyuan Liu, Yuanxin Tian, Zehong Ke, Jinhao Li, Hao Cheng et al. (8 authors)

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12371) | [PDF](https://arxiv.org/pdf/2609.12371)

<details>
<summary>Abstract</summary>

Autonomous driving requires more than recognizing what is present in a scene: a planner must determine how road structure, surrounding agents, and their motion states should influence a future maneuver. Existing learning-based planners can capture these influences through latent scene features and trajectory decoders, but the relationship between environmental factors and candidate actions often remains implicit. This limits the ability to inspect, diagnose, or refine how scene context affects the safety of a predicted trajectory. Classical safety fields provide an explicit spatial representat...

</details>

<details>
<summary>Share</summary>

```
READ: Learning Risk-Informed Fields for End-to-End Autonomous Driving

Autonomous driving requires more than recognizing what is present in a scene: a planner must determine how road structure, surrounding agents, and their motion states should influence a future maneuver.

arXiv: https://arxiv.org/abs/2609.12371

#VLA #robotics
```

</details>

---

### [Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model](https://arxiv.org/abs/2609.13053)

**Authors:** Hoeun Lee, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi et al. (7 authors)

**Published:** 2026-09-11 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.13053) | [PDF](https://arxiv.org/pdf/2609.13053)

<details>
<summary>Abstract</summary>

Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes. We bring these predictions into action generation and selection through a shared trajectory model. Dynin-Robotics implements this formulation on Dynin-Omni, an omnimodal masked-diffusion backbone, representing language, visual observations, goals, and actions as discrete tokens. By varying conditioning and target spans, the same model learns action prediction, action-conditioned next-observation prediction, terminal goal-state pr...

</details>

<details>
<summary>Share</summary>

```
Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes.

arXiv: https://arxiv.org/abs/2609.13053

#VLA #robotics
```

</details>

---

### [Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641)

**Authors:** Jianman Lin, Shailesh Shailesh, Zhongyi Luo, Jiafei Duan

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.12641) | [PDF](https://arxiv.org/pdf/2609.12641) | [Project Page](https://magiclab-nus.github.io/LIT/?v=37955c5)

<details>
<summary>Abstract</summary>

Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine generalization when these correlations change under distribution shifts. Mitigating these shortcuts requires constraining how visual information is used for action generation while preserving task-relevant spatial information. We propose Late...

</details>

<details>
<summary>Share</summary>

```
Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts.

arXiv: https://arxiv.org/abs/2609.12641
Project page: https://magiclab-nus.github.io/LIT/?v=37955c5

#VLA #robotics
```

</details>

---

### [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)

**Authors:** Dionysios Adamopoulos, Nattapol Chanpaisit, Basel Fakhri, Christina Giannoula

**Published:** 2026-09-10 | **Categories:** cs.DC, cs.AR, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12075) | [PDF](https://arxiv.org/pdf/2609.12075)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage. Since robots must meet strict Service-Level Objectives (SLOs) for safety, VLA inference is inherently latency-critical. Meeting these SLOs requires high-end GPUs, yet weight, cost, and power constraints preclude integrating such GPUs on-robot. Prior works offload VLA inference to edge servers that serve many robots on VLA models. However, current VLA systems lack support for multi-request, multi-mod...

</details>

<details>
<summary>Share</summary>

```
Efficient Vision-Language-Action Management and Serving for Robot Factories

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage.

arXiv: https://arxiv.org/abs/2609.12075

#VLA #robotics
```

</details>

---

## World Models (7)

### [Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence](https://arxiv.org/abs/2609.12036)

**Authors:** Shilong Zou, Shilin Zhang, Yingji Zhang, Yuhang Huang, Yi Zhang et al. (11 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.12036) | [PDF](https://arxiv.org/pdf/2609.12036) | [Project Page](https://zoushilong1024.github.io/Pelican-Sim1.0/)

<details>
<summary>Abstract</summary>

In this technical report, we propose Pelican-Sim 1.0, a general world model simulator for embodied intelligence that predicts future observations from visual context and robot actions to support downstream learning and decision making. The model incorporates four key design features: (1) Unified action representation: a 28-dimensional action value space covering most mainstream embodiments, keeping one model valid across heterogeneous devices. (2) Action-visual injection: URDF- and camera-rendered action videos bridge actions and pixels, giving markedly better controllability across embodiment...

</details>

<details>
<summary>Share</summary>

```
Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence

In this technical report, we propose Pelican-Sim 1.0, a general world model simulator for embodied intelligence that predicts future observations from visual context and robot actions to support downstream learning an...

arXiv: https://arxiv.org/abs/2609.12036
Project page: https://zoushilong1024.github.io/Pelican-Sim1.0/

#worldmodels #robotics
```

</details>

---

### [IMPLY: Physically Anchored Consistency for World-Model Rollouts](https://arxiv.org/abs/2609.12441)

**Authors:** Aman Mehta, Riya Baviskar

**Published:** 2026-09-11 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12441) | [PDF](https://arxiv.org/pdf/2609.12441)

<details>
<summary>Abstract</summary>

A world model asked what happens if an object is pushed at several speeds produces several futures. If the model has the object in mind, those futures agree about it: each implies the same mass and friction. The consistency checks now used to vet world-action models ask whether a model's futures agree with each other, and none of them knows any physics. We show that this is not enough, and what to do instead. IMPLY reads the physics each rollout implies by inverting a simulator and scores a set of rollouts by how well one object explains all of them, anchored to two calibration pushes the mode...

</details>

<details>
<summary>Share</summary>

```
IMPLY: Physically Anchored Consistency for World-Model Rollouts

A world model asked what happens if an object is pushed at several speeds produces several futures.

arXiv: https://arxiv.org/abs/2609.12441

#worldmodels #robotics
```

</details>

---

### [DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal](https://arxiv.org/abs/2609.12347)

**Authors:** Rongjun Jin, Jianming Ma, Yue Gao

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12347) | [PDF](https://arxiv.org/pdf/2609.12347)

<details>
<summary>Abstract</summary>

Humanoid robots must traverse cluttered obstacle fields using onboard proprioceptive and visual observations, yet existing methods usually process multimodal observations without explicitly considering their different characteristics: proprioceptive observations are low-dimensional but governed by highly nonlinear robot dynamics, while egocentric visual observations are high-dimensional, noisy, and redundant. We propose DWMP (Dual World Model Policy), a framework that provides the actor with separate but complementary world-model representations for humanoid obstacle traversal. A Koopman-based...

</details>

<details>
<summary>Share</summary>

```
DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal

Humanoid robots must traverse cluttered obstacle fields using onboard proprioceptive and visual observations, yet existing methods usually process multimodal observations without explicitly considering their different...

arXiv: https://arxiv.org/abs/2609.12347

#worldmodels #robotics
```

</details>

---

### [RodForesight: A World Model Enhanced Diffusion Policy for Slender and Material Agnostic Rod Insertion](https://arxiv.org/abs/2609.12103)

**Authors:** Chuanbo Yu, Mingyu Yue, Yan Lyu, Chuhan Song, Peng Wang

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12103) | [PDF](https://arxiv.org/pdf/2609.12103)

<details>
<summary>Abstract</summary>

Slender rod insertion arises in precision manufacturing, where millimetre scale diameter and tight clearances demand accurate perception and control. Conventional peg-in-hole methods assume a rigid object whose tip pose is fixed relative to the gripper. This assumption breaks down for a high aspect ratio rod, which can bend during manipulation, making its tip motion dependent on the rod configuration, grasp, material properties, and contact. We present RodForesight, a learning framework that factorises the task into two stages: 1) coarse approaching, which uses visual servoing to map diverse i...

</details>

<details>
<summary>Share</summary>

```
RodForesight: A World Model Enhanced Diffusion Policy for Slender and Material Agnostic Rod Insertion

Slender rod insertion arises in precision manufacturing, where millimetre scale diameter and tight clearances demand accurate perception and control.

arXiv: https://arxiv.org/abs/2609.12103

#worldmodels #robotics
```

</details>

---

### [Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation](https://arxiv.org/abs/2609.12422)

**Authors:** Kowei Shih, Lu Cheng, Zeyu Wang, Yeyun Xu, Kejian Tong

**Published:** 2026-09-11 | **Categories:** cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.12422) | [PDF](https://arxiv.org/pdf/2609.12422)

<details>
<summary>Abstract</summary>

Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation. We present HORIZON, a hierarchical agent that combines symmetry aware spatial perception, dual memory belief tracking, relic centric graph attention, information gain driven exploration, and an opponent conditioned policy mixture. HORIZON separates short horizon control from cross match meta reasoning, while auxiliary belief and world model objectives stabilize learning. Trained with PPO in a large sc...

</details>

<details>
<summary>Share</summary>

```
Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation

Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation.

arXiv: https://arxiv.org/abs/2609.12422

#worldmodels #robotics
```

</details>

---

### [Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.12278)

**Authors:** Fernando Palafox, David Fridovich-Keil

**Published:** 2026-09-10 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.12278) | [PDF](https://arxiv.org/pdf/2609.12278)

<details>
<summary>Abstract</summary>

World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate. We study the problem of adapting a world model to an unknown test-time environment, drawn from a known environment family, using only a few episodes of interaction. Existing approaches trade off computational cost against expressivity, i.e., the range of models a method can produce. For example, in-context learning is computationally cheap but limited in expressivity, and gradient-based adaptation is expressive but computationally expensive. We present CLAW (Co...

</details>

<details>
<summary>Share</summary>

```
Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning

World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate.

arXiv: https://arxiv.org/abs/2609.12278

#worldmodels #robotics
```

</details>

---

### [Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity](https://arxiv.org/abs/2609.12090)

**Authors:** Aditi Tiwari, Akshit Bhalla, Darshan Prasad, Heng Ji

**Published:** 2026-09-10 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.12090) | [PDF](https://arxiv.org/pdf/2609.12090)

<details>
<summary>Abstract</summary>

Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content. Standard memory ablations test whether memory helps, but not whether the retrieved content is responsible. We test this directly with read-time memory substitution, which replaces the consumed memory value while leaving the rest of the computation unchanged. This separates memory benefit from memory specificity, the extent to which the gain depends on retrieved content. Across frozen video world models, identity-free controls...

</details>

<details>
<summary>Share</summary>

```
Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity

Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content.

arXiv: https://arxiv.org/abs/2609.12090

#worldmodels #robotics
```

</details>

---
