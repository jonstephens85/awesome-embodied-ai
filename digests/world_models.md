# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-23 17:21 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL](https://arxiv.org/abs/2607.19749v1)

**Authors:** Gurp Nijjer

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19749v1) | [PDF](https://arxiv.org/pdf/2607.19749v1.pdf) | [GitHub](https://github.com/gurpnijjer/dream-rehearsal)

<details>
<summary>Abstract</summary>

Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? Under never-clear replay, pre-registered component-level probes (n=3 seeds throughout) show that the world model retains essentially everything measurable about old tasks -- reward discrimi...

</details>

---

### [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343v1)

**Authors:** Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang et al. (11 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.19343v1) | [PDF](https://arxiv.org/pdf/2607.19343v1.pdf) | [Project Page](https://masked-visual-actions.github.io)

<details>
<summary>Abstract</summary>

Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrar...

</details>

---

### [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190v2)

**Authors:** Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma et al. (23 authors)

**Published:** 2026-07-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19190v2) | [PDF](https://arxiv.org/pdf/2607.19190v2.pdf) | [Project Page](URL)

<details>
<summary>Abstract</summary>

Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across vi...

</details>

---

### [FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](https://arxiv.org/abs/2607.19038v1)

**Authors:** Jialong Zuo, Haotong Zuo, Shiwei Zhang, Xiang Wang, Chen Li et al. (8 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19038v1) | [PDF](https://arxiv.org/pdf/2607.19038v1.pdf) | [Project Page](https://filmworld-ai.github.io)

<details>
<summary>Abstract</summary>

Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi-scene visual narratives. While current video generation models excel at short, single-scene clips within narrow temporal and spatial contexts, novel-to-film generation operates in a more complex regime, demanding long-duration content across diverse scenes with dynamically evolving entity states. To address this, we formalize novel-to...

</details>

---

### [Generative World Renderer at the Speed of Play](https://arxiv.org/abs/2607.18703v1)

**Authors:** Guixu Lin, Zheng-Hui Huang, Siqi Yang, Ming-Hsuan Yang, Kaipeng Zhang et al. (6 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.18703v1) | [PDF](https://arxiv.org/pdf/2607.18703v1.pdf) | [Project Page](https://alaya-renderer-flash.alayalab.ai/)

<details>
<summary>Abstract</summary>

Generative world renderer AlayaRenderer receives structured world states exported from physics engines and synthesizes RGB frames. Unlike models that generate frames from text/control-hints prompts, AlayaRenderer preserves scene structure without altering the underlying world dynamics. This demonstrates an alternative path toward interactive world modeling and user-controllable play. However, the original AlayaRenderer is too computationally expensive for real-time deployment. This technical rep...

</details>

---

## Other Recent Papers

### [Active Inference as a Convex Markov Decision Process](https://arxiv.org/abs/2607.20152v1)

**Authors:** Nikola Milosevic, Nicolás Hinrichs, Nico Scherf

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.AI, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2607.20152v1) | [PDF](https://arxiv.org/pdf/2607.20152v1.pdf)

<details>
<summary>Abstract</summary>

Active Inference (AIF) frames adaptive behavior as the minimization of expected free energy (EFE), combining epistemic and pragmatic objectives within a single variational principle. We frame AIF as policy optimization and show that, for closed-loop control policies, EFE minimization can be formulated as a convex Markov decision process (MDP). In this formulation, the pragmatic terms are linear in the predictive state marginals and therefore equivalent to reward maximization in a latent MDP, whi...

</details>

---

### [LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition](https://arxiv.org/abs/2607.19889v1)

**Authors:** Jiajun Cheng, Subarna Tripathi, Sainan Liu, Xiaofan Yu, Shan Lin

**Published:** 2026-07-22 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.19889v1) | [PDF](https://arxiv.org/pdf/2607.19889v1.pdf)

<details>
<summary>Abstract</summary>

Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery. Pretrained vision-language models (VLMs) and vision encoders offer an alternative to conventional interaction classifiers by transferring broad visual and semantic knowledge. However, adapting them to fine-grained surgical interactions remains challenging: (1) freezing the vision encoder depends entirely on pretrained representations that may retain noise and provide weak spati...

</details>

---

### [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876v1)

**Authors:** Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai et al. (6 authors)

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.19876v1) | [PDF](https://arxiv.org/pdf/2607.19876v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge. While closed-loop evaluation via simulator rollouts offers a more faithful assessment of physical plausibility than open-loop alternatives, existing frameworks almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be brittle to data outside their training distribution, resulting in u...

</details>

---

### [Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning](https://arxiv.org/abs/2607.19809v1)

**Authors:** Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi

**Published:** 2026-07-22 | **Categories:** cs.MA, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.19809v1) | [PDF](https://arxiv.org/pdf/2607.19809v1.pdf)

<details>
<summary>Abstract</summary>

In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) ...

</details>

---

### [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/abs/2607.19719v1)

**Authors:** Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan et al. (6 authors)

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.19719v1) | [PDF](https://arxiv.org/pdf/2607.19719v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. Its Koopman-inspired backbone uses two-dimensional rotation--scaling blocks with bounded radii to represent damping, rotation, an...

</details>

---

### [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191v1)

**Authors:** Fan Jiang, Zhaoxu Sun, Mengchao Wang, Ziyu Zhu, Chiyu Wang et al. (41 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.19191v1) | [PDF](https://arxiv.org/pdf/2607.19191v1.pdf)

<details>
<summary>Abstract</summary>

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a ...

</details>

---

### [NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework](https://arxiv.org/abs/2607.18887v1)

**Authors:** Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18887v1) | [PDF](https://arxiv.org/pdf/2607.18887v1.pdf)

<details>
<summary>Abstract</summary>

Vessel trajectory prediction in complex maritime environments is essential for traffic management, collision warning, route planning, and autonomous navigation. Although AIS-based learning methods have progressed rapidly, existing datasets are often released as raw message streams or irregular time series, with inconsistent sampling rates, noisy observations, heterogeneous coordinate systems, and non-unified scenario protocols. Most public AIS resources also lack structured representations of na...

</details>

---

### [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/abs/2607.18715v1)

**Authors:** Yi-Ge Zhang, Tianqi Du, Qi Zhang, Yisen Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18715v1) | [PDF](https://arxiv.org/pdf/2607.18715v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every source of state change. In real world, however, transitions arise from two heterogeneous sources: an action-driven component induced by the agent, and an action-invariant world effect -- the change that would still occur under a null action, dictated by the env...

</details>

---

### [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](https://arxiv.org/abs/2607.18709v2)

**Authors:** Ziqin Wang, Hao Li, Weijun Wang, Junhao Cai, Jia Zeng et al. (8 authors)

**Published:** 2026-07-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18709v2) | [PDF](https://arxiv.org/pdf/2607.18709v2.pdf)

<details>
<summary>Abstract</summary>

Existing robot datasets remain expensive to curate, embodiment-specific, and insufficiently annotated with the fine-grained structure required for generalizable reasoning, execution, or long-horizon environment dynamics simulation. Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling. RoboInter1.5 provides a unified resource of data, benchmarks, and models center...

</details>

---

### [Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development](https://arxiv.org/abs/2607.18696v1)

**Authors:** Yinan Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18696v1) | [PDF](https://arxiv.org/pdf/2607.18696v1.pdf)

<details>
<summary>Abstract</summary>

AI-native biotechnology companies are often designed by copying human biotech org charts into agent roles. We argue for a different abstraction: a Company World Model, defined as a persistent asset-to-value state representation with transition models, explicit value functions, planning, and updating across scientific, regulatory, BD, commercial, financial, and execution constraints. We introduce a dry-lab benchmark for testing whether AI-agent organizations should mimic departments or operate ar...

</details>

---
