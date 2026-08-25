# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-25 22:15 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [ReWorld: An Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2608.23565v1)

**Authors:** Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang et al. (11 authors)

**Published:** 2026-08-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.23565v1) | [PDF](https://arxiv.org/pdf/2608.23565v1.pdf) | [Project Page](https://zhifeichen097.github.io/ReWorld/)

<details>
<summary>Abstract</summary>

An interactive world model must follow the user's actions, remember the places it has shown, and stream in real time. The tension is structural: control wants a short horizon, memory wants an unbounded one. ReWorld separates the two during training and bounds them at inference. Mixed per-head attention windows confine most heads to the recent past while a small set of global heads attends over the entire history, and random head routing keeps either capability from binding to particular heads; r...

</details>

---

### [Correcting a learned physical invariant improves world-model rollouts](https://arxiv.org/abs/2608.23526v1)

**Authors:** Richard Bao

**Published:** 2026-08-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.23526v1) | [PDF](https://arxiv.org/pdf/2608.23526v1.pdf) | [GitHub](https://github.com/Zarand3r/world-model-invariants)

<details>
<summary>Abstract</summary>

World models can predict video without learning dynamics that they reliably preserve. We test whether a frozen DreamerV3 trained only on pendulum video learns a scalar that its own latent transition treats as approximately conserved. A label-free search recovers the same energy-like invariant across independently trained conservative models, while the same procedure finds no comparable invariant in matched damped models. During autonomous rollouts, this quantity drifts. Projecting the latent sta...

</details>

---

### [Reward-Free Continual Adaptation for Resilient Space Robots](https://arxiv.org/abs/2608.23452v1)

**Authors:** Andrej Orsula, Miguel Olivares-Mendez, Carol Martinez

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.23452v1) | [PDF](https://arxiv.org/pdf/2608.23452v1.pdf) | [GitHub](https://github.com/AndrejOrsula/space_robotics_bench)

<details>
<summary>Abstract</summary>

Space robots operate in extreme environments where hardware degradation can critically compromise traditional control strategies. While continual reinforcement learning offers a promising mechanism for online adaptation, it inherently requires access to a reward signal during deployment. However, precise reward computation in space is often infeasible due to the lack of external tracking systems and the overall complexity of the environment. To address the challenge of unobservable rewards, we i...

</details>

---

### [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v1)

**Authors:** Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li et al. (16 authors)

**Published:** 2026-08-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23383v1) | [PDF](https://arxiv.org/pdf/2608.23383v1.pdf) | [Project Page](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/)

<details>
<summary>Abstract</summary>

Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, en...

</details>

---

### [From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070v1)

**Authors:** Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang et al. (6 authors)

**Published:** 2026-08-24 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23070v1) | [PDF](https://arxiv.org/pdf/2608.23070v1.pdf) | [GitHub](https://github.com/AtongWang/world-model-simulators)

<details>
<summary>Abstract</summary>

With the rapid progress of diffusion models and large-scale video generation, generative world models are increasingly expected to replace traditional simulators, including physics engines, game engines, and reinforcement-learning environments. Yet the remaining distance from generation to simulation lacks a systematic assessment. We present a capability-based study using an external yardstick: eight capabilities of a traditional simulator, namely asset construction, physics engine, interaction,...

</details>

---

### [MOSH-WM: Mask-Grounded Soft-Hamiltonian Dynamics for Object-Centric World Models](https://arxiv.org/abs/2608.22750v1)

**Authors:** Zhekai Wang, Haoxiang Huang, Xiang Liu, Zhikang Chen, Yueqing Sun et al. (9 authors)

**Published:** 2026-08-24 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.22750v1) | [PDF](https://arxiv.org/pdf/2608.22750v1.pdf) | [GitHub](https://github.com/moshwm-anon/-moshwm-anon.github.io)

<details>
<summary>Abstract</summary>

Object-centric world models forecast future videos by evolving a set of entity slots, but the variables receiving dynamics supervision are often unconstrained visual features. We introduce \method{}, a mask-grounded soft-Hamiltonian world model that makes its position-like state explicitly depend on slot-owned image support. A frozen video-slot encoder produces slots and masks; spatial moments of mask-owned support form a canonical state $Q$, temporal differences form $P$, and a learned energy s...

</details>

---

### [DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model](https://arxiv.org/abs/2608.22278v1)

**Authors:** Jie Yin, Xingyu Lai

**Published:** 2026-08-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.22278v1) | [PDF](https://arxiv.org/pdf/2608.22278v1.pdf) | [GitHub](https://github.com/DreamMimic/DreamMimic}{DreamMimic})

<details>
<summary>Abstract</summary>

Vision-based whole-body loco-manipulation on humanoid robots is challenging due to partial observability, contact-rich dynamics, and the difficulty of learning long-horizon behaviors from high-dimensional visual inputs. We present \href{https://github.com/DreamMimic/DreamMimic}{DreamMimic}, a framework that distills privileged teacher policies into vision-based humanoid controllers via world-model-assisted distillation. Instead of using a Dreamer-style RSSM for planning, we repurpose it to learn...

</details>

---

## Other Recent Papers

### [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v1)

**Authors:** Yiren Lu, Xin Ye, Jiaming Liu, Jin Yao, Yi-chung Chen et al. (12 authors)

**Published:** 2026-08-24 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.23486v1) | [PDF](https://arxiv.org/pdf/2608.23486v1.pdf)

<details>
<summary>Abstract</summary>

World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forci...

</details>

---

### [Future Querying: Can LLMs Serve as Implicit Medical World Models?](https://arxiv.org/abs/2608.23248v1)

**Authors:** Siri Willems, James Butterworth, Lore Goetschalckx, Peter Vrancx, Philippe Modard et al. (7 authors)

**Published:** 2026-08-24 | **Categories:** cs.CL, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.23248v1) | [PDF](https://arxiv.org/pdf/2608.23248v1.pdf)

<details>
<summary>Abstract</summary>

Traditional clinical prediction models rely on task-specific pipelines and curated, structured data, which scale poorly and underutilize unstructured text. To address this, we introduce future querying, a paradigm that probes whether large language models (LLMs) can function as implicit medical world models by evaluating their ability to answer time-indexed clinical queries about a patient's future. Our framework operates on unstructured clinical documentation using endpoint-agnostic training, e...

</details>

---

### [EchoWM: Open and Enterable Omnimodal World Models](https://arxiv.org/abs/2608.23189v1)

**Authors:** Songchun Zhang, Yaowei Li, Junhao Zhuang, Weiyang Jin, Haoyu Wang et al. (22 authors)

**Published:** 2026-08-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23189v1) | [PDF](https://arxiv.org/pdf/2608.23189v1.pdf)

<details>
<summary>Abstract</summary>

We present EchoWM, an omnimodal world model for enterable generative media that responds to continuous navigation while jointly generating 720p video, environmental sound, music and speech. We organize interaction around camera intent: in first-person scenes, it specifies observer motion, while in third-person scenes, camera--character dynamics are learned from data without view-specific controllers. Discrete commands and continuous poses are mapped to a shared metric-scale relative 6-DoF trajec...

</details>

---

### [LpWM: A Case for Sparse Representations in World Models](https://arxiv.org/abs/2608.22764v1)

**Authors:** Yilun Kuang, Yash Dagade, Quentin Le Lidec, Lucas Maes, Randall Balestriero et al. (6 authors)

**Published:** 2026-08-24 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.22764v1) | [PDF](https://arxiv.org/pdf/2608.22764v1.pdf)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn latent dynamics for planning and avoid representation collapse by matching features to maximum-entropy distributions such as isotropic Gaussians, yielding dense representations. However, it is unclear whether dense representations are the most favorable geometry for modeling dynamics. In this work, we ask whether a different geometry, sparse representations, can make action-conditioned latent dynamics easier to model, and what dynamical stru...

</details>

---

### [Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules](https://arxiv.org/abs/2608.22642v1)

**Authors:** Florian Rottach, Sebastian Schieferdecker, William Rudman, Randall Balestriero, Carsten Eickhoff

**Published:** 2026-08-23 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.22642v1) | [PDF](https://arxiv.org/pdf/2608.22642v1.pdf)

<details>
<summary>Abstract</summary>

Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present \textbf{Mol-JEPA}, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinitie...

</details>

---

### [Where World Models Break: Natural-Input Failure Discovery](https://arxiv.org/abs/2608.22421v1)

**Authors:** Zhanpeng Shi, Zi Liang, Rong Feng, Shiqin Tang, Xuyang Chen et al. (6 authors)

**Published:** 2026-08-23 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.22421v1) | [PDF](https://arxiv.org/pdf/2608.22421v1.pdf)

<details>
<summary>Abstract</summary>

World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from g...

</details>

---

### [Tracing the Unlabeled Storm: Cross-Variable Transfer in a Lagrangian Atmospheric JEPA Framework](https://arxiv.org/abs/2608.22358v1)

**Authors:** K M Anirudh, S Sandeep, Hariprasad Kodamana

**Published:** 2026-08-23 | **Categories:** cs.LG, physics.geo-ph

**Links:** [arXiv](https://arxiv.org/abs/2608.22358v1) | [PDF](https://arxiv.org/pdf/2608.22358v1.pdf)

<details>
<summary>Abstract</summary>

Deep atmospheric convection governs South Asian monsoon variability, yet attempting to learn its latent world model directly from zero-inflated, heavy-tailed precipitation yields suboptimal predictive representations. Continuous atmospheric proxies, such as outgoing longwave radiation (OLR), express this convective organization far more coherently. We address this mismatch with \emph{cross-variable proxy learning}: M-JEPA, a multiscale Monsoon Joint-Embedding Predictive Architecture, is pretrain...

</details>

---

### [Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning](https://arxiv.org/abs/2608.22294v1)

**Authors:** Juntao Cheng, Jingkai Wang, Yijun Shen, Xiansheng Chen, Zhiwei Yu

**Published:** 2026-08-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.22294v1) | [PDF](https://arxiv.org/pdf/2608.22294v1.pdf)

<details>
<summary>Abstract</summary>

World models for physical interaction are typically trained to predict future observations or latent features; however, a planning-oriented model must answer a fundamentally different question: whether a candidate action produces a task-consistent future while preserving essential relations.Monolithic state representations obscure the underlying entities, while standard instance-level object slots merely identify \emph{what} is present without specifying \emph{what role} each entity plays in the...

</details>

---

### [On the Capability Separation Between World-Model Policy Learning and Imitated World-Action Models](https://arxiv.org/abs/2608.22197v1)

**Authors:** Yang Yu

**Published:** 2026-08-23 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.22197v1) | [PDF](https://arxiv.org/pdf/2608.22197v1.pdf)

<details>
<summary>Abstract</summary>

World-action models predict a future outcome and then infer an associated action. Although this factorization can improve representation learning and data efficiency, it is unclear whether it provides stronger control capability than direct behavior cloning when both are trained from the same observational demonstrations. We compare a direct behavior-cloning policy, an imitation-trained world-action policy, and a policy optimized with an action-conditioned world model. At the controller-class le...

</details>

---
