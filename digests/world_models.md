# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-08 17:35 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559v1)

**Authors:** Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06559v1) | [PDF](https://arxiv.org/pdf/2607.06559v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/RynnWorld-4D.github.io) | [GitHub](https://github.com/alibaba-damo-academy/RynnWorld-4D)

<details>
<summary>Abstract</summary>

Robotic manipulation in the open world requires not only recognizing what a scene looks like, but also anticipating how its 3D structure moves under interaction. We argue that synchronized RGB, depth, and optical flow, namely RGB-DF, provide a physically grounded representation that captures the underlying 4D dynamics of a scene. Compared to 2D pixel videos, this multi-modal synergy aligns visual appearance with geometric structure and temporal motion, creating a representation space significant...

</details>

---

### [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558v1)

**Authors:** Haoyu Zhao, Xingyue Zhao, Hangyu Li, Biao Gong, Kehan Li et al. (9 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06558v1) | [PDF](https://arxiv.org/pdf/2607.06558v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/RynnWorld-Teleop.github.io) | [GitHub](https://github.com/alibaba-damo-academy/RynnWorld-Teleop)

<details>
<summary>Abstract</summary>

Scaling robot learning requires massive, diverse trajectory data, yet collection is currently bottlenecked by physical teleoperation, where every demonstration binds operator time to specific hardware and workspaces. We introduce digital teleoperation, a paradigm that decouples data collection from physical constraints by replacing the real robot with a generative world model. In this framework, an operator's hand-pose stream drives a robot-centric generative world model to synthesize high-fidel...

</details>

---

### [MoWorld: A Flash World Model](https://arxiv.org/abs/2607.06216v1)

**Authors:** Team Moxin, Deyi Ji, Tianrun Chen, Xin Zhang, Jiale Yang et al. (29 authors)

**Published:** 2026-07-07 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.06216v1) | [PDF](https://arxiv.org/pdf/2607.06216v1.pdf) | [Project Page](https://moxin-tech.github.io/moworld/)

<details>
<summary>Abstract</summary>

The future of World Models depends not only on scaling model capability, but also on scaling practicality and inference efficiency. High-frame-rate inference enables responsive perception, planning, and control in real-world autonomous systems. To this end, we present MoWorld, a cost-effective yet high-performance Flash World Model with an end-to-end framework spanning data generation, pre-training, distillation, and efficient inference, enabling up to 50 FPS real-time interaction with cinematic...

</details>

---

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

## Other Recent Papers

### [Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning](https://arxiv.org/abs/2607.06501v1)

**Authors:** Anxing Xiao, Hanbo Zhang, Tianrun Hu, David Hsu

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06501v1) | [PDF](https://arxiv.org/pdf/2607.06501v1.pdf)

<details>
<summary>Abstract</summary>

We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in human environments. In this work, we propose an open-world planning framework that enables robots to automatically generate, verify, and update h...

</details>

---

### [A Definition and Roadmap for World Models](https://arxiv.org/abs/2607.06401v1)

**Authors:** Xinyuan Chen, Haoyu Guo, Shi Guo, Bingqi Jiang, Chunhua Shen et al. (13 authors)

**Published:** 2026-07-07 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.06401v1) | [PDF](https://arxiv.org/pdf/2607.06401v1.pdf)

<details>
<summary>Abstract</summary>

World models -- internal simulators that learn the structure and dynamics of an environment -- have become one of the most actively debated concepts in AI. From model-based reinforcement learning and video generation to embodied robotics and ultimately, physical AI, researchers across AI subfields are building systems that they call "world models", yet there is no consensus on what a world model fundamentally is, what it should predict, or how it should be built. This perspective article provide...

</details>

---

### [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291v1)

**Authors:**  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge et al. (17 authors)

**Published:** 2026-07-07 | **Categories:** cs.CV, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2607.06291v1) | [PDF](https://arxiv.org/pdf/2607.06291v1.pdf)

<details>
<summary>Abstract</summary>

Game worlds have traditionally been built through labor-intensive production pipelines, making them costly to develop, difficult to customization, and expensive to modify after deployment. Recent advances in video world models offer a fundamentally different paradigm. Rather than explicitly authoring every component of a virtual environment, these models autoregressively synthesize future observations conditioned on the current world state and user interactions, enabling playable worlds to be ge...

</details>

---

### [Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon World-Model Failure](https://arxiv.org/abs/2607.05966v1)

**Authors:** Finn Rasmus Schäfer, Korbinian Moller, Yuan Gao, Christian Oefinger, Sebastian Schmidt et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.05966v1) | [PDF](https://arxiv.org/pdf/2607.05966v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon failure in world models is conventionally attributed to compounding error, a generic framing that does not distinguish what kind of error compounds. We propose a kinematic-vs-dynamic reframing: world models tend to imagine kinematically rather than dynamically. We operationalize this as the imagined Kinematic-Consistency Error, a per-step diagnostic that measures how far a rollout departs from a closed-form kinematic null, paired with a perturbation protocol that tests whether iKCE ...

</details>

---

### [Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction](https://arxiv.org/abs/2607.05577v1)

**Authors:** Mohammad Saifullah, Thomas Kornmaier, Taaha Kazi, Vasu Sharma, Aditya Sanjiv Kanade et al. (6 authors)

**Published:** 2026-07-06 | **Categories:** cs.AI, cs.CL, cs.IR

**Links:** [arXiv](https://arxiv.org/abs/2607.05577v1) | [PDF](https://arxiv.org/pdf/2607.05577v1.pdf)

<details>
<summary>Abstract</summary>

Long-form fiction writers need memory that answers multi-hop questions about evolving story state: who knows a secret and when they learned it, whether an event preceded the narration that revealed it, whether a setup paid off, and how a relationship shifted. General-purpose retrieval and agent-memory systems represent entities and facts but not the narratological structure these questions turn on, so they surface the wrong evidence or none at all. We introduce the Narrative World Model (NWM), a...

</details>

---

### [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352v2)

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, Chris Mulder, Aditya Makkar et al. (27 authors)

**Published:** 2026-07-06 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.05352v2) | [PDF](https://arxiv.org/pdf/2607.05352v2.pdf)

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
