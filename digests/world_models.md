# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-26 16:46 UTC

**Papers found:** 21

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LeFlow: Generative Latent Flow Planning for World Models](https://arxiv.org/abs/2608.24855v1)

**Authors:** Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu, Jenq-Neng Hwang

**Published:** 2026-08-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.24855v1) | [PDF](https://arxiv.org/pdf/2608.24855v1.pdf) | [GitHub](https://github.com/hsiangwei0903/LeFlow)

<details>
<summary>Abstract</summary>

Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator. This approach pays the full iterative optimization cost anew at every replanning step and reuses no planning experience across queries. In this work...

</details>

---

### [Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)

**Authors:** Wenxuan Shen, Dongna Jin, Dongping Chen

**Published:** 2026-08-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.24680v1) | [PDF](https://arxiv.org/pdf/2608.24680v1.pdf) | [GitHub](https://github.com/Dongping-Chen/Game2World)

<details>
<summary>Abstract</summary>

Video games provide a scalable source of training data for video world models, offering diverse environments, complex interactions, and abundant in-the-wild gameplay videos. However, raw gameplay footage entangles the game world with screen-space interfaces, introducing game-specific biases and irrelevant dynamics that hinder world-model training. To address this problem, we introduce GameUI-Taxonomy and G2WEngine, a full-stack framework that formalizes gameplay UI grounding and removal. G2WEngi...

</details>

---

### [Platonic Representation Hypothesis on World Models](https://arxiv.org/abs/2608.23720v1)

**Authors:** Wenhow Li, Chengwei MA, Hui Xiong, Ying-Cong Chen, Lei Zhang

**Published:** 2026-08-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23720v1) | [PDF](https://arxiv.org/pdf/2608.23720v1.pdf) | [Project Page](https://sellerbubble.github.io/platonic-representation-hypothesis-on-world-models/)

<details>
<summary>Abstract</summary>

World models have demonstrated significant potential for perceiving and simulating complex environments. Despite their strong performance, the fundamental nature of their learned representations remains poorly understood. In this paper, we investigate the Platonic Representation Hypothesis within this domain by proposing the Predictive Consistency Assumption: we posit that the optimization of a shared state transition objective acts as a selective pressure that encourages heterogeneous models to...

</details>

---

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

### [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v2)

**Authors:** Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao et al. (13 authors)

**Published:** 2026-08-24 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.23486v2) | [PDF](https://arxiv.org/pdf/2608.23486v2.pdf) | [Project Page](https://yiren-lu.com/project_pages/geowam/)

<details>
<summary>Abstract</summary>

World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forci...

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

### [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)

**Authors:** Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li et al. (16 authors)

**Published:** 2026-08-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23383v2) | [PDF](https://arxiv.org/pdf/2608.23383v2.pdf) | [Project Page](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/)

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

## Other Recent Papers

### [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](https://arxiv.org/abs/2608.24885v1)

**Authors:** Sixiang Chen, Jiaming Liu, Jixian Wu, Yichen Guo, Tinghao Wang et al. (10 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.24885v1) | [PDF](https://arxiv.org/pdf/2608.24885v1.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models are increasingly used as learned simulators for policy evaluation and improvement, yet their effectiveness rests on an unverified assumption: generated futures faithfully reflect arbitrary valid actions. Existing benchmarks are typically confined to expert demonstrations, leaving off-expert action following inadequately evaluated. To address this gap, we introduce WorldEcho, which probes action following over a broader action distribution using visual integrity an...

</details>

---

### [Neurosymbolic Alignment for Physiologically-Safe Clinical Language Models](https://arxiv.org/abs/2608.24534v1)

**Authors:** Abdulhady Abas Abdullah, Erik Cambria, Milena Zivkovic

**Published:** 2026-08-25 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.24534v1) | [PDF](https://arxiv.org/pdf/2608.24534v1.pdf)

<details>
<summary>Abstract</summary>

Clinical LLMs can generate recommendations that are factually plausible yet physiologically unsafe. We investigate whether safety alignment can be improved by grounding preference optimization in structured physiological knowledge rather than text-only supervision. Methods: We propose Neurosymbolic Alignment, a training-time framework that couples a 7B clinical LLM with an HGNN-based Physiological World Model over an 847K-node biomedical knowledge graph. Candidate responses are scored using home...

</details>

---

### [NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)

**Authors:** Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher et al. (10 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24199v1) | [PDF](https://arxiv.org/pdf/2608.24199v1.pdf)

<details>
<summary>Abstract</summary>

Generative simulation for surgical robotics still lacks real-time interaction. Physical-robot experiments, often involving animal or cadaver labs, are time-consuming, costly, and difficult to reproduce, while classical simulators struggle to capture photorealistic appearance and deformable-tissue dynamics. We address this gap with Cosmos-H-Dreams, an integrated real-time surgical world-model system combining an action-conditioned generative model, a teacher-to-student distillation recipe, and a ...

</details>

---

### [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](https://arxiv.org/abs/2608.24101v1)

**Authors:** Zhi Cao, Howard Ji, Kevin Zhang, Kuangzhi Ge, Li Fei-Fei et al. (7 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24101v1) | [PDF](https://arxiv.org/pdf/2608.24101v1.pdf)

<details>
<summary>Abstract</summary>

Robot actions are inherently embodiment-specific and only weakly aligned with image-space visual changes, limiting their effectiveness as conditioning signals for robot world models. In contrast, visual tracks provide an embodiment-agnostic representation of how task-relevant points move through a scene, offering dense image-space guidance for accurate and spatially precise future video prediction. Building on this observation, we propose TrAct, a world-model-based robot decision-making framewor...

</details>

---

### [XP-JEPA: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics](https://arxiv.org/abs/2608.24044v1)

**Authors:** Kehan Wen, Ziming Li, Siyuan Luo, Fan Shi

**Published:** 2026-08-25 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.24044v1) | [PDF](https://arxiv.org/pdf/2608.24044v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models plan by predicting how candidate actions transform learned representations. In self-predictive models, however, the encoder and predictor are optimized jointly and can co-adapt to latent transitions that are easy to predict but only weakly constrained by the physical evolution of the scene. We introduce the cross-predictive JEPA (XP-JEPA), which grounds visual latent dynamics in privileged physical trajectories. XP-JEPA separately encodes visual observations and physical stat...

</details>

---

### [DreamLedger: Execution-Settled Credit Files for World-Model Imagination in Robot Decision Loops](https://arxiv.org/abs/2608.23863v1)

**Authors:** Xianyao Li, Ruitong Tian, Rui Min, Fang Xu, Jing Du

**Published:** 2026-08-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.23863v1) | [PDF](https://arxiv.org/pdf/2608.23863v1.pdf)

<details>
<summary>Abstract</summary>

Robots are beginning to act on world-model predictions, yet reliability is still expressed through instantaneous, model-internal signals. DreamLedger instead treats reliability as a persistent deployment object: an execution-settled credit file recording how often consumed predictions are borne out, indexed by operating condition, region, and prediction horizon, and consulted before each use. Each consumed prediction is registered as a claim; attributable outcomes are settled against arriving re...

</details>

---

### [Primate vision reveals a missing principle for robust dynamic AI](https://arxiv.org/abs/2608.23790v1)

**Authors:** Matteo Dunnhofer, Christian Micheloni, Kohitij Kar

**Published:** 2026-08-24 | **Categories:** cs.CV, q-bio.NC

**Links:** [arXiv](https://arxiv.org/abs/2608.23790v1) | [PDF](https://arxiv.org/pdf/2608.23790v1.pdf)

<details>
<summary>Abstract</summary>

How does an intelligent visual system combine what objects look like with how they move while remaining robust as appearance changes? We addressed this question by comparing human perception and neural activity in macaque inferior temporal cortex with representations from image- and video-based neural networks spanning recognition, segmentation, optic-flow processing and predictive world modeling. Temporal integration improved object representations, but most video recognition models generalized...

</details>

---

### [Do LLMs Understand Limit Order Book Dynamics?](https://arxiv.org/abs/2608.23706v1)

**Authors:** Junxiao Chen, Paul Glasserman

**Published:** 2026-08-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.23706v1) | [PDF](https://arxiv.org/pdf/2608.23706v1.pdf)

<details>
<summary>Abstract</summary>

A large language model (LLM) trained on synthetic limit order book (LOB) data achieves near perfect scores in generating valid sequences of LOB events. However, the LLM's implicit world model fails to learn the state of the LOB. This deficiency leads to biased estimates and spurious predictability in using the LLM to forecast future LOB events. Our analysis uses novel tests of an LLM's world model, extending prior work from deterministic settings to the stochastic dynamics needed for the LOB.

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
