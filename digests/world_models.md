# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-27 17:10 UTC

**Papers found:** 10

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
