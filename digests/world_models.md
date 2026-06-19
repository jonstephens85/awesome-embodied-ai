# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-19 17:57 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Holo-World: Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083v1)

**Authors:** Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen et al. (9 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20083v1) | [PDF](https://arxiv.org/pdf/2606.20083v1.pdf) | [Project Page](is) | [GitHub](https://github.com/XiangchenYin/Holo-World})

<details>
<summary>Abstract</summary>

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instructio...

</details>

---

### [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531v1)

**Authors:** Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin et al. (10 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19531v1) | [PDF](https://arxiv.org/pdf/2606.19531v1.pdf) | [Project Page](https://zhangwenyao1.github.io/ImageWAM/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) commonly rely on video generation to bridge visual world modeling and robot control. However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction. These issues raise a simple question: Does world action model really need video generation? We...

</details>

---

### [Physics-IQ Verified](https://arxiv.org/abs/2606.18943v1)

**Authors:** Tim Rädsch, Yuki M Asano, Hilde Kuehne, Stefan Bauer, Priyank Jaini et al. (7 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18943v1) | [PDF](https://arxiv.org/pdf/2606.18943v1.pdf) | [GitHub](https://github.com/google-deepmind/physics-iq-benchmark)

<details>
<summary>Abstract</summary>

Video generative models ( VGMs) have become a new frontier that can be used not just for video generation but for a multitude of downstream tasks, including world modeling. To advance these tasks, a good video model must understand the physical reality of the world. Evaluating this understanding is an emerging field and has led to the Physics-IQ benchmark, which quantifies this explicitly by comparing model-generated videos to real-world videos of physical experiments. In this work, we present a...

</details>

---

## Other Recent Papers

### [Current World Models Lack a Persistent State Core](https://arxiv.org/abs/2606.20545v1)

**Authors:** Jinpeng Lu, Dexu Zhu, Haoyuan Shi, Linghan Cai, Guo Tang et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20545v1) | [PDF](https://arxiv.org/pdf/2606.20545v1.pdf)

<details>
<summary>Abstract</summary>

World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking. This requirement is a blind spot of existing benchmarks, which...

</details>

---

### [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104v1)

**Authors:** Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf

**Published:** 2026-06-18 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20104v1) | [PDF](https://arxiv.org/pdf/2606.20104v1.pdf)

<details>
<summary>Abstract</summary>

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce ...

</details>

---

### [Reward as An Agent for Embodied World Models](https://arxiv.org/abs/2606.19990v1)

**Authors:** Pu Li, Zhigang Lin, Qiang Wu, Yongxuan Lv, Fei Wang et al. (6 authors)

**Published:** 2026-06-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.19990v1) | [PDF](https://arxiv.org/pdf/2606.19990v1.pdf)

<details>
<summary>Abstract</summary>

While RL has become a promising tool for refining world models, existing methods largely rely on conservative rollouts near the training distribution, limiting exploration, behavioral diversity, and richer dynamic discovery. In this work, we challenge this conservative paradigm. We argue that the core limitation is not exploration itself, but the lack of reliable verification strategies to support broader exploration. Without reliable verification, expanded exploration becomes highly susceptible...

</details>

---

### [SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928v1)

**Authors:** Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu et al. (9 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19928v1) | [PDF](https://arxiv.org/pdf/2606.19928v1.pdf)

<details>
<summary>Abstract</summary>

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both t...

</details>

---

### [SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics](https://arxiv.org/abs/2606.19889v1)

**Authors:** Wentao Pan, Wuyang Li, Shengyuan Liu, Xinyu Liu, Hengyu Liu et al. (6 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.19889v1) | [PDF](https://arxiv.org/pdf/2606.19889v1.pdf)

<details>
<summary>Abstract</summary>

Scaling robot policy learning for autonomous surgery is challenging, as expert demonstrations are expensive and in vivo exploration poses substantial safety risks. Surgical world models address this by generating realistic, action-conditioned future frames from an initial observation, but existing methods exhibit two persistent failure modes: spatial interaction incoherence, where visible instrument contact fails to induce spatially consistent tissue deformation, and temporal fidelity collapse, ...

</details>

---

### [Can In-Context Learning Support Intrinsic Curiosity?](https://arxiv.org/abs/2606.19476v1)

**Authors:** Eric Elmoznino, Sangnie Bhardwaj, Johannes von Oswald, Rajai Nasser, Blaise Agüera y Arcas et al. (8 authors)

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.19476v1) | [PDF](https://arxiv.org/pdf/2606.19476v1.pdf)

<details>
<summary>Abstract</summary>

Effective machine learning depends not only on how we model data, but also on what data we choose to collect. While large sequence models have revolutionized data modeling, the problem of automated data selection, or "intrinsic curiosity", remains a significant challenge. Classic approaches incentivize exploration by rewarding an agent based on its "learning progress", which measures how much a newly acquired observation improves a world model's predictive ability. However, evaluating these rewa...

</details>

---

### [FlexLAM: Resolving the Bottleneck Trade-off in Latent Action Learning](https://arxiv.org/abs/2606.19408v1)

**Authors:** Takanori Yoshimoto, Yang Hu, Naruya Kondo, Tatsuya Matsushima

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19408v1) | [PDF](https://arxiv.org/pdf/2606.19408v1.pdf)

<details>
<summary>Abstract</summary>

Latent actions provide a compact interface between action-free video and downstream decision-making, yet existing Latent Action Models (LAMs) force every transition through a fixed-capacity bottleneck. We identify a bottleneck trade-off: overly tight codes can discard transition cues needed for action alignment, while overly loose codes preserve additional transition variation that must be resolved when alignment labels are scarce or narrowly distributed. FlexLAM replaces this fixed capacity wit...

</details>

---

### [Lifecycle-Aware Dynamic Analysis for Secure ML Model Execution](https://arxiv.org/abs/2606.19023v1)

**Authors:** Gabriele Digregorio, Marco Di Gennaro, Francesco Pastore, Stefano Zanero, Stefano Longari et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.19023v1) | [PDF](https://arxiv.org/pdf/2606.19023v1.pdf)

<details>
<summary>Abstract</summary>

The growing reliance on pre-trained Machine Learning (ML) models has introduced new attack surfaces. Recent vulnerabilities demonstrate that malicious behavior can be embedded within model artifacts, often bypassing existing defenses. Current model-scanning solutions primarily rely on static, format-specific rules or known attack signatures, which limit their ability to generalize across frameworks and to detect novel exploitation paths. In contrast, we propose a solution that focuses on the eff...

</details>

---

### [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960v2)

**Authors:** Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li et al. (10 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18960v2) | [PDF](https://arxiv.org/pdf/2606.18960v2.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts. However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames. Existing m...

</details>

---

### [DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration](https://arxiv.org/abs/2606.18825v1)

**Authors:** Luoyao Kang, Yuelin Zhang, Jiwei Shan, Haifan Gong, Qingpeng Ding et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18825v1) | [PDF](https://arxiv.org/pdf/2606.18825v1.pdf)

<details>
<summary>Abstract</summary>

Ultrasound (US) is widely used for surgical navigation, yet real-time registration between intraoperative 2D slices and preoperative 3D volumes remains challenging due to partial observability, speckle noise, and the action-dependent US acquisition. Existing methods are one-shot or short-horizon, making it hard for them to gather evidence over time or capture how surgeons adjust probe motion based on on-screen feedback. We propose DreamReg, a belief-driven world-model framework that formulates 2...

</details>

---

### [Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/abs/2606.18697v1)

**Authors:** Yibin Hu, Xiaolin Sun, Zizhan Zheng

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.CR, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18697v1) | [PDF](https://arxiv.org/pdf/2606.18697v1.pdf)

<details>
<summary>Abstract</summary>

Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. However, the process of updating world models from collected experience creates a training-time attack surface: adversarially poisoned fine-tuning trajectories can manipulate the learned dynamics and thereby corrupt downstream planning. In this paper, we propose SWAAP, the first two-stage data poisoning framework for learned world models. In the first stage, SWAAP identifie...

</details>

---

### [Dual-Channel Grounded World Modeling (DCGWM): Structural Prevention of Objective Interference Collapse via Heterogeneous External Grounding with Inward-Only Gradient Flow](https://arxiv.org/abs/2606.18688v1)

**Authors:** Akshay Hazare

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.18688v1) | [PDF](https://arxiv.org/pdf/2606.18688v1.pdf)

<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) are a leading approach to world model representation learning. We identify a failure mode in JEPA-based world models grounded against two qualitatively distinct external signals: physical dynamics (sparse, high-magnitude, constraint-satisfying gradient corrections) and social-behavioral dynamics (diffuse, distribution-matching corrections). We term this Objective Interference Collapse (OIC): we argue that joint learning in a shared latent space ca...

</details>

---

### [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610v1)

**Authors:** Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi et al. (12 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18610v1) | [PDF](https://arxiv.org/pdf/2606.18610v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating generalist robot manipulation policies in the real world is expensive, slow, and difficult to scale. Action-conditioned video world models offer a scalable alternative by simulating policy rollouts. Autoregressive rollouts accumulate compounding errors, observations across multiple camera views must remain mutually consistent, and the evaluator must generalize to policies whose behaviors lie outside the training distribution. We address these challenges with SC3-Eval, a self-consisten...

</details>

---

### [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589v1)

**Authors:** Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She et al. (9 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18589v1) | [PDF](https://arxiv.org/pdf/2606.18589v1.pdf)

<details>
<summary>Abstract</summary>

Action chunking has become a common interface for vision-language-action (VLA) models, enabling low-frequency policy inference to drive high-frequency robot execution. However, once an action chunk is committed, its open-loop execution can be brittle under stochastic dynamics, hardware execution errors, and partial observability. We propose DREAM-Chunk, a test-time scaling method that augments chunking-based policies with a lightweight latent world model, without requiring additional policy fine...

</details>

---
