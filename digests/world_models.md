# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-27 02:24 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Code World Model: Coding Agent as World Brain](https://arxiv.org/abs/2608.25927v1)

**Authors:** Yiwen Chen, Guosheng Lin, Chi Zhang

**Published:** 2026-08-26 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2608.25927v1) | [PDF](https://arxiv.org/pdf/2608.25927v1.pdf) | [Project Page](https://buaacyw.github.io/cwm/)

<details>
<summary>Abstract</summary>

World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution. We introduce Code World Model, a framework that separates world evolution from visual realization by combining ...

</details>

---

### [ConfAL-WM: Confidence-Guided Active Learning for Action-Conditioned World Models](https://arxiv.org/abs/2608.25572v1)

**Authors:** Xiang Liu, Sen Cui, Changshui Zhang

**Published:** 2026-08-26 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.25572v1) | [PDF](https://arxiv.org/pdf/2608.25572v1.pdf) | [Project Page](https://ConfAL-WM.github.io)

<details>
<summary>Abstract</summary>

Action-conditioned world models have become an important foundation for embodied prediction, planning, and synthetic data generation, but their errors under new task and scene distributions are often concentrated in localized spatiotemporal regions such as robot arms, manipulated objects, contact areas, and occluded objects. This paper presents ConfAL-WM, a confidence-guided active learning framework for post-training embodied world models. Built upon EVAC, we attach a lightweight confidence pro...

</details>

---

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

## Other Recent Papers

### [4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956v1)

**Authors:** Yueen Ma, Zenglin Xu, Irwin King

**Published:** 2026-08-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.25956v1) | [PDF](https://arxiv.org/pdf/2608.25956v1.pdf)

<details>
<summary>Abstract</summary>

Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeatedly process redundant background content. Although point clouds can represent the world in 3D space, they can be difficult to align and accumulate across viewpoints. In this paper, we leverage an explicit 4D Gaussian Splatting (4DGS) representation that separately models dynamic objects and the stat...

</details>

---

### [PRISM: Projection-Integrated Sampling-Based MPC with Bayesian Cost Tuning for Bimanual Manipulation](https://arxiv.org/abs/2608.25666v1)

**Authors:** Alinjar Dan, Iryna Hurova, Karl Kruusamäe, Arun Kumar Singh

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25666v1) | [PDF](https://arxiv.org/pdf/2608.25666v1.pdf)

<details>
<summary>Abstract</summary>

Bimanual manipulation in cluttered, contact-rich environments remains challenging because it requires coordinated motion generation, interaction-aware planning, and reliable execution under tight kinematic constraints. We present PRISM, a projection-integrated sampling-based Model Predictive Control (MPC) framework that uses a GPU-accelerated physics simulator as an online world model for complex dual-arm manipulation. The main algorithmic contribution is a QP-guided control sampling strategy th...

</details>

---

### [GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)

**Authors:** Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He et al. (11 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25659v1) | [PDF](https://arxiv.org/pdf/2608.25659v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have advanced language-conditioned robotic manipulation, yet action-imitation objectives provide only weak supervision for metric 3D structure and short-horizon physical evolution. Geometry-enhanced policies mainly improve current-scene grounding, whereas predictive policies often model future dynamics in RGB or latent spaces and may incur substantial deployment cost. GaussianDream demonstrates that training-time current Gaussian reconstruction and future Ga...

</details>

---

### [Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models](https://arxiv.org/abs/2608.25518v1)

**Authors:** Pengfei Zhou, Hexin Wang, Zhengfeiyang Zhang, Yixing Ma, Zhenglin Wan et al. (8 authors)

**Published:** 2026-08-26 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.25518v1) | [PDF](https://arxiv.org/pdf/2608.25518v1.pdf)

<details>
<summary>Abstract</summary>

A common strategy for scaling world models is to train on more crawled video with more compute. We argue that this strategy is inefficient: scaling world models also requires a recursive data engine that offers grounded reward signals. The success of code agents illustrates why this matters. As code is executable, compilers and runtimes can provide high-quality rewards for Reinforcement Learning (RL) post-training of LLMs. By contrast, spatial generation still relies largely on fuzzy proxies suc...

</details>

---

### [4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)

**Authors:** Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou et al. (7 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.25479v1) | [PDF](https://arxiv.org/pdf/2608.25479v1.pdf)

<details>
<summary>Abstract</summary>

Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combi...

</details>

---

### [Rollout-Decoded Reconstruction for Long-Horizon Prediction in Latent World Models](https://arxiv.org/abs/2608.25017v1)

**Authors:** Rishi Shah, Rishav Shrestha

**Published:** 2026-08-25 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.25017v1) | [PDF](https://arxiv.org/pdf/2608.25017v1.pdf)

<details>
<summary>Abstract</summary>

A latent world model trains its decoder on latents anchored to observations, then deploys it on the model's own free-running rollout, hundreds of steps past the last observation. Rollout-Decoded Reconstruction (RDR) closes this gap with a single loss term that free-runs the model during training exactly as evaluation will, decodes every rollout latent, and penalizes reconstruction error against ground truth. The term adds no parameters, costs training-time compute only, and reduces to the standa...

</details>

---

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

### [JEPA-x: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics](https://arxiv.org/abs/2608.24044v2)

**Authors:** Kehan Wen, Ziming Li, Siyuan Luo, Fan Shi

**Published:** 2026-08-25 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.24044v2) | [PDF](https://arxiv.org/pdf/2608.24044v2.pdf)

<details>
<summary>Abstract</summary>

Latent world models plan by predicting how candidate actions advance learned latent dynamics. In self-predictive models, however, the encoder and predictor are optimized jointly and can co-adapt to latent transitions that are easy to predict but weakly constrained by the physical evolution of the scene. We introduce the cross-predictive JEPA (JEPA-x), which grounds visual latent dynamics in privileged physical trajectories. JEPA-x treats visual observations and physical states as corresponding v...

</details>

---
