# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-26 17:47 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PhysiFormer: Learning to Simulate Mechanics in World Space](https://arxiv.org/abs/2606.27364v1)

**Authors:** Yiming Chen, Yushi Lan, Andrea Vedaldi

**Published:** 2026-06-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.27364v1) | [PDF](https://arxiv.org/pdf/2606.27364v1.pdf) | [Project Page](https://yimingc9.github.io/physiformer)

<details>
<summary>Abstract</summary>

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality,...

</details>

---

### [EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting](https://arxiv.org/abs/2606.27277v1)

**Authors:** Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu et al. (6 authors)

**Published:** 2026-06-25 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.27277v1) | [PDF](https://arxiv.org/pdf/2606.27277v1.pdf) | [GitHub](https://github.com/Luo-Z13/EO-WM)

<details>
<summary>Abstract</summary>

Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty in...

</details>

---

### [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](https://arxiv.org/abs/2606.26713v1)

**Authors:** Yuqi Jiang, Yumeng Liu, Zimu Li, Jinyuan Deng, Qian Jin et al. (10 authors)

**Published:** 2026-06-25 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.26713v1) | [PDF](https://arxiv.org/pdf/2606.26713v1.pdf) | [GitHub](https://github.com/7jiangyq/lithodreamer.git)

<details>
<summary>Abstract</summary>

As semiconductor technology nodes scale, computational lithography is essential for ensuring yield and performance. However, lithography is a continuous physical process involving mask optimization, optical imaging, resist exposure, and development, which existing models fail to capture. To overcome this limitation, we present LithoDreamer, the first physics-informed World Model (WM) framework for computational lithography, which formulates the ``Layout-Mask-Resist Image-After Development Image ...

</details>

---

### [PhysEditWorld: A Large-Scale Dataset Toward Physics-Editable World Models](https://arxiv.org/abs/2606.26694v1)

**Authors:** Bin Hu, Yanwen Ma, Jiehui Huang, Ziliang Zhang, Haoning Wu et al. (17 authors)

**Published:** 2026-06-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26694v1) | [PDF](https://arxiv.org/pdf/2606.26694v1.pdf) | [Project Page](https://yizhiqianbi.github.io/physeditworld/)

<details>
<summary>Abstract</summary>

Recent game world models can synthesize visually plausible, action-conditioned rollouts. However, their interaction behaviors often remain limited to exploratory or wandering trajectories, and physical dynamics are typically learned as implicit correlations from data rather than as controllable variables. This limitation hinders their applicability to authored game environments, where physical rules are deliberately designed and require explicit manipulation. We introduce PhysEditWorld, a multim...

</details>

---

### [USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning](https://arxiv.org/abs/2606.25880v1)

**Authors:** Yuchen Xie, Xinyu Zhou, Kuangji Zuo, Yanshuo Lu, Fengrui Huang et al. (7 authors)

**Published:** 2026-06-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.25880v1) | [PDF](https://arxiv.org/pdf/2606.25880v1.pdf) | [Project Page](https://arescheah.github.io/uss-project-page/)

<details>
<summary>Abstract</summary>

Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only sp...

</details>

---

## Other Recent Papers

### [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326v1)

**Authors:** Nicklas Hansen, Xiaolong Wang

**Published:** 2026-06-25 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27326v1) | [PDF](https://arxiv.org/pdf/2606.27326v1.pdf)

<details>
<summary>Abstract</summary>

Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. We hypothesize that hallucination concentrates in low-coverage regions of the state-action space, where lightweight data-centric signals can both detect it and guide mitigation. To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, r...

</details>

---

### [Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model](https://arxiv.org/abs/2606.27325v1)

**Authors:** Zizhao Yuan, Zhengtu Liang, Taowen Wang, Qiwei Liang, Yichi Wang et al. (10 authors)

**Published:** 2026-06-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.27325v1) | [PDF](https://arxiv.org/pdf/2606.27325v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in action-conditioned world models show promising progress in modeling complex interactions and forecasting future states under diverse action sequences. While these models are often driven by stronger visual representations and model capacity, action conditioning itself remains underexplored. Most existing approaches compress the entire action sequence into a single representation, which works well for low-DoF control but becomes less reliable in high-DoF scenarios. We observe t...

</details>

---

### [A Generalization Theory for JEPA-Based World Models](https://arxiv.org/abs/2606.27014v1)

**Authors:** Jingyi Cui, Qi Zhang, Hongwei Wen, Yisen Wang

**Published:** 2026-06-25 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.27014v1) | [PDF](https://arxiv.org/pdf/2606.27014v1.pdf)

<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) have recently emerged as a promising paradigm for world modeling by learning predictive dynamics in a latent space rather than generating future observations at the input level. Despite their empirical success, the theoretical understanding of JEPA-based world models remains limited. In this paper, we develop the first generalization theory for JEPA-based world models. We formulate JEPA pretraining as a conditional spectral graph learning problem ...

</details>

---

### [Einstein World Models](https://arxiv.org/abs/2606.26969v1)

**Authors:** Munachiso Samuel Nwadike, Zangir Iklassov, Ali Mekky, Zayd M. Kawakibi Zuhri, Kentaro Inui

**Published:** 2026-06-25 | **Categories:** cs.AI, cs.CL, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26969v1) | [PDF](https://arxiv.org/pdf/2606.26969v1.pdf)

<details>
<summary>Abstract</summary>

Does intelligence require the ability to reason about phenomena beyond direct experience? It is natural to suspect that some complex thought cannot be captured through language alone. However, of particular concern to this work, is whether visualising counterfactual events can complement language as a mechanism for complex thought. We ask whether LLMs can be trained to utilise such visualisation mechanisms, in a way that benefits their reasoning abilities. Motivated by this question, we propose ...

</details>

---

### [Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds](https://arxiv.org/abs/2606.26964v1)

**Authors:** Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang et al. (8 authors)

**Published:** 2026-06-25 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26964v1) | [PDF](https://arxiv.org/pdf/2606.26964v1.pdf)

<details>
<summary>Abstract</summary>

As embodied AI and world models increasingly operate in dynamic 3D environments, visual perception must move beyond passively interpreting given observations toward actively deciding what to observe. We study this problem through camera planning in dynamic 3D story worlds, where the camera must not only generate smooth motion, but also decide what visual evidence should be acquired before it moves. We formulate this capability as Narrative-Grounded World Visual Attention, where the camera acts a...

</details>

---

### [Risk-Aware Selective Multimodal Driver Monitoring with Driver-State World Modeling](https://arxiv.org/abs/2606.26922v1)

**Authors:** Daosheng Qiu, Haozhuang Chi, Hao Su, Shu Long, Xinyue Miao et al. (7 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.26922v1) | [PDF](https://arxiv.org/pdf/2606.26922v1.pdf)

<details>
<summary>Abstract</summary>

Continuous driver monitoring in automated vehicles requires low-latency inference while avoiding unsafe decisions under uncertain driver states. Large vision-language models provide broad multimodal priors, but their latency and limited reliability in this setting make them unsuitable as always-on in-cabin monitors. We propose a cost-aware selective inference framework for deployable multimodal driver monitoring. The core system is a lightweight RGB-physiological student that combines in-cabin v...

</details>

---

### [Neural Voxel Dynamics: Learning Implicit 3D Physics via Volumetric Feature Advection](https://arxiv.org/abs/2606.26410v1)

**Authors:** Zican Wang, Niloy Mitra

**Published:** 2026-06-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26410v1) | [PDF](https://arxiv.org/pdf/2606.26410v1.pdf)

<details>
<summary>Abstract</summary>

We present a self-supervised framework for learning implicit 3D physical dynamics directly from video-derived supervisory signals. While current generative video models achieve high visual fidelity, they lack a 3D geometric foundation, often resulting in physical inconsistencies and a failure to maintain object permanence. We address this by shifting the predictive bottleneck from 2D image space to a `lifted' 3D Volumetric Latent Space. Our method unprojects semantic features from a Video Joint-...

</details>

---

### [KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation](https://arxiv.org/abs/2606.26321v1)

**Authors:** Runfeng Ling

**Published:** 2026-06-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.26321v1) | [PDF](https://arxiv.org/pdf/2606.26321v1.pdf)

<details>
<summary>Abstract</summary>

Mobile manipulators need world models that are current, queryable, semantically meaningful, and usable under edge-compute constraints. This technical report presents KRVF, a source-aware semantic voxel world representation for edge mobile manipulation. Unlike reconstruction-centric mapping pipelines that primarily optimize global geometric fidelity, KRVF represents local world state as task-oriented voxels that encode occupancy, color, semantic evidence, temporal freshness, and evidence source. ...

</details>

---

### [Fast LeWorldModel](https://arxiv.org/abs/2606.26217v1)

**Authors:** Yuntian Gao, Xiangyu Xu

**Published:** 2026-06-24 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.26217v1) | [PDF](https://arxiv.org/pdf/2606.26217v1.pdf)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs), including recent LeWorldModel (LeWM), have become a promising foundation for reconstruction-free visual world models. For visual planning, however, LeWM evaluates candidate action sequences by repeatedly applying a local one-step latent transition model. This autoregressive rollout makes planning computationally expensive and exposes the predicted trajectory to accumulated latent errors as the horizon grows. We propose Fast LeWorldModel (Fast-LeW...

</details>

---

### [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1)

**Authors:** Seth Dobrin, Łukasz Chmiel

**Published:** 2026-06-24 | **Categories:** cs.AI, cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.26057v1) | [PDF](https://arxiv.org/pdf/2606.26057v1.pdf)

<details>
<summary>Abstract</summary>

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mecha...

</details>

---

### [In-Context World Modeling for Robotic Control](https://arxiv.org/abs/2606.26025v2)

**Authors:** Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji et al. (7 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26025v2) | [PDF](https://arxiv.org/pdf/2606.26025v2.pdf)

<details>
<summary>Abstract</summary>

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Mode...

</details>

---

### [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](https://arxiv.org/abs/2606.25527v1)

**Authors:** Guozheng Ma, Lu Li, Zilin Wang, Pierre-Luc Bacon, Dacheng Tao

**Published:** 2026-06-24 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.25527v1) | [PDF](https://arxiv.org/pdf/2606.25527v1.pdf)

<details>
<summary>Abstract</summary>

Online reinforcement learning (RL) agents increasingly depend on knowledge acquired offline to achieve practical efficiency. Originally studied in offline-to-online RL, this paradigm now spans foundation model post-training and embodied intelligence, with prior types expanding from offline datasets and pre-trained policies to increasingly diverse knowledge sources such as multimodal foundation models and generative world models. Offline priors have become central to how deep RL is developed and ...

</details>

---

### [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473v1)

**Authors:** Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen et al. (10 authors)

**Published:** 2026-06-24 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.25473v1) | [PDF](https://arxiv.org/pdf/2606.25473v1.pdf)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in dif...

</details>

---

### [Hypergraph Normal World Models for Logical Visual Anomaly Detection](https://arxiv.org/abs/2606.25368v1)

**Authors:** Weizhi Nie, Zibo Xu, Weijie Wang, Yuting Su

**Published:** 2026-06-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.25368v1) | [PDF](https://arxiv.org/pdf/2606.25368v1.pdf)

<details>
<summary>Abstract</summary>

Visual anomaly detection is often deployed with only normal training images. Most one-class detectors map test patches or features to a normal reference distribution. This works well for local structural defects. Logical anomalies are different. Each visible part may look normal, while the whole image violates a normal count, co-occurrence, or spatial relation. This paper studies whether a model can learn such a category-specific normal world from nominal images alone. We propose the Hypergraph ...

</details>

---
