# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-07 17:58 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models](https://arxiv.org/abs/2607.05390v1)

**Authors:** Hongyu Li, Wanjia Fu, Xiaoyan Cong, Zekun Li, Binghao Huang et al. (14 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.05390v1) | [PDF](https://arxiv.org/pdf/2607.05390v1.pdf) | [Project Page](https://deform360.lhy.xyz)

<details>
<summary>Abstract</summary>

Predicting object dynamics (i.e., world modeling) is a fundamental challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their high-dimensional state spaces and complex material properties. While current world models approach this through two distinct paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding of their relative strengths and limitations remains elusive due to ...

</details>

---

### [InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization](https://arxiv.org/abs/2607.04988v1)

**Authors:** Haoxiang Ma, Junhao Cai, Xiaoxu Xu, Hao Li, Yuyin Yang et al. (29 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04988v1) | [PDF](https://arxiv.org/pdf/2607.04988v1.pdf) | [Project Page](https://internrobotics.github.io/internvla-a15.github.io/)

<details>
<summary>Abstract</summary>

Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a nativ...

</details>

---

### [Qantara: Bridge-Flow Training for Multi-Paradigm JEPA Control](https://arxiv.org/abs/2607.04978v1)

**Authors:** Ruslan Rakhimov, George Bredis, Yuriy Maksyuta, Daniil Gavrilov

**Published:** 2026-07-06 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04978v1) | [PDF](https://arxiv.org/pdf/2607.04978v1.pdf) | [Project Page](https://corl-team.github.io/qantara)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) underpin a growing family of latent world models for control from raw pixels, but every existing JEPA world model commits at training time to a single inference paradigm: either trajectory optimisation in a learned dynamics model, or direct behaviour cloning. A single checkpoint that serves both would defer this choice to inference, when deployment constraints (rollout cost, observation accessibility) determine which path wins. We present Qantara,...

</details>

---

### [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](https://arxiv.org/abs/2607.04546v1)

**Authors:** Riccardo O. Feingold, Davide Liconti, Chenyu Yang, Robert K. Katzschmann

**Published:** 2026-07-05 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.04546v1) | [PDF](https://arxiv.org/pdf/2607.04546v1.pdf) | [Project Page](https://srl-ethz.github.io/Mask2Real-WM/)

<details>
<summary>Abstract</summary>

Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps...

</details>

---

### [CRISP: A Spatiotemporal Camera-Radar Backbone for Driving via Forecasting-Based World-Model Pretraining](https://arxiv.org/abs/2607.04541v1)

**Authors:** Jingyu Song, Yi Liu, Katherine A. Skinner

**Published:** 2026-07-05 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.04541v1) | [PDF](https://arxiv.org/pdf/2607.04541v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Camera-radar (CR) fusion is a practical sensing configuration for autonomous driving, but existing models are typically trained with task-specific supervision, limiting reusable representation learning. We present CRISP, a spatiotemporal CR backbone pretrained through forecasting-based representation learning. Given historical multi-view images and radar sweeps, CRISP learns a unified bird's-eye-view (BEV) representation by predicting future LiDAR point clouds. LiDAR is used only as privileged s...

</details>

---

## Other Recent Papers

### [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352v1)

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, Chris Mulder, Aditya Makkar et al. (27 authors)

**Published:** 2026-07-06 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.05352v1) | [PDF](https://arxiv.org/pdf/2607.05352v1.pdf)

<details>
<summary>Abstract</summary>

We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...

</details>

---

### [MoP-JEPA: Hard-Assigned Predictor Mixtures for Stochastic JEPA World Models](https://arxiv.org/abs/2607.05238v1)

**Authors:** Zhi Song, Ximing Xing, Zhenchao Tang, hanbo Huang, Tianxu Lv et al. (10 authors)

**Published:** 2026-07-06 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.05238v1) | [PDF](https://arxiv.org/pdf/2607.05238v1.pdf)

<details>
<summary>Abstract</summary>

JEPA world models predict the next latent state with a single deterministic predictor trained by latent regression. We show that this fails structurally when the environment is stochastic: at a branching transition, the regression-optimal predictor outputs the conditional mean of the successor embeddings, a point between the true next states that corresponds to no state at all. We prove this collapse for deterministic and gated mixture-of-experts predictors, and prove that MoP-JEPA's hard-assign...

</details>

---

### [DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2607.04927v1)

**Authors:** Jian Zhu, Jianjun Zhang, Taiyi Su, Tianbin Liu, Zhangyuan Wang et al. (13 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04927v1) | [PDF](https://arxiv.org/pdf/2607.04927v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted i...

</details>

---

### [KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation](https://arxiv.org/abs/2607.04652v1)

**Authors:** Xinyu Shao, Keru Zhou, Guowei Huang, Yajun Gao, Tongtong Cao et al. (6 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04652v1) | [PDF](https://arxiv.org/pdf/2607.04652v1.pdf)

<details>
<summary>Abstract</summary>

Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinem...

</details>

---

### [Geographic Diversity Beats Data Volume for Cross-Domain Generalization in Zero-Label JEPA Driving World Models](https://arxiv.org/abs/2607.04500v1)

**Authors:** Santosh Jaiswal

**Published:** 2026-07-05 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.04500v1) | [PDF](https://arxiv.org/pdf/2607.04500v1.pdf)

<details>
<summary>Abstract</summary>

Self-supervised latent world models can assign a surprise score to driving scenarios without any human labels. A natural follow-up question is whether such a model, trained on driving data from one geographic region, can generalize its notion of complexity to unseen cities and sensor configurations. We study this question through a controlled transfer experiment: we train JEPA-based world models on nuPlan data (Pittsburgh, Boston, Singapore) and evaluate zero-shot on held-out Argoverse 2 validat...

</details>

---

### [Operator-on-F complements value-equivalence: a planning-time diagnostic for latent world models](https://arxiv.org/abs/2607.04464v1)

**Authors:** Donna Vakalis

**Published:** 2026-07-05 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04464v1) | [PDF](https://arxiv.org/pdf/2607.04464v1.pdf)

<details>
<summary>Abstract</summary>

World-model evaluation for model-based reinforcement learning typically asks whether the learned model predicts reward and value well, which can leave planning-relevant errors in the model's latent rollouts unmeasured. We introduce a complementary diagnostic, operator-on-F, that compares a model's k-step latent pushforward to the environment's on an observable subset F, using the model's own predictor. On a TD-MPC2 size sweep over cheetah-run, reward-prediction error stays within [0.028, 0.091] ...

</details>

---

### [Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](https://arxiv.org/abs/2607.04409v1)

**Authors:** Fan Feng, Yujia Zheng, Minghao Fu, Yongqiang Chen, Guangyi Chen et al. (8 authors)

**Published:** 2026-07-05 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.04409v1) | [PDF](https://arxiv.org/pdf/2607.04409v1.pdf)

<details>
<summary>Abstract</summary>

Learning and planning in imagination using world models provides an effective paradigm for training agents for decision-making. However, existing approaches often rely on high-dimensional latent spaces or generic visual embeddings that retain many factors irrelevant to control, limiting efficiency and generalization across tasks. To this end, we study how agents can learn world models with representations that are task-specific, minimal, and sufficient for decision-making. We achieve this via a ...

</details>

---

### [Last-Meter Precision Navigation for UAVs: A Diffusion-Refined Aerial Visual Servoing Approach](https://arxiv.org/abs/2607.04352v1)

**Authors:** Yaxuan Li, Jiarui Zeng, Shaofei Huang, Zhedong Zheng

**Published:** 2026-07-05 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.04352v1) | [PDF](https://arxiv.org/pdf/2607.04352v1.pdf)

<details>
<summary>Abstract</summary>

In this work, we study the last-meter precision navigation for UAVs, e.g., autonomously reaching a target within the final 10 meters using monocular vision. This task is challenging due to scale ambiguity, rotation discontinuities, and the need for fine-grained spatial reasoning. Existing methods often fail under large viewpoint changes or lack generalization to unseen environments. To this end, we propose DreamNav, a coarse-to-fine diffusion-refined aerial visual servoing framework. In the firs...

</details>

---

### [DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics](https://arxiv.org/abs/2607.04112v1)

**Authors:** Silin Gao, Hao Zhao, Zeming Chen, Sepideh Mamooler, Antara Raaghavi Bhattacharya et al. (11 authors)

**Published:** 2026-07-05 | **Categories:** cs.LG, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.04112v1) | [PDF](https://arxiv.org/pdf/2607.04112v1.pdf)

<details>
<summary>Abstract</summary>

Multimodal LLMs struggle to systematically model the temporal evolution of visual scenes in videos or multi-image sequences. Such inputs require models to predict or simulate multiple levels of dynamic constituents, such as actions taken in the visual sequence, and the associated changes to the visual environment that result. To address this challenge, we propose a dynamic schema-guided world model, DynaVieW, optimized for visual dynamic prediction and simulation. DynaVieW achieves an in-depth u...

</details>

---
