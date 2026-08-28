# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-28 05:52 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406v1)

**Authors:** Kechen Liu, Ola Shorinwa

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.27406v1) | [PDF](https://arxiv.org/pdf/2608.27406v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical l...

</details>

---

### [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](https://arxiv.org/abs/2608.27328v1)

**Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li et al. (10 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.27328v1) | [PDF](https://arxiv.org/pdf/2608.27328v1.pdf) | [GitHub](https://github.com/AMAP-ML/R2MBench)

<details>
<summary>Abstract</summary>

High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambiguity makes absolute revisit scores sensitive to rendering stability, repetitive content, and failed motion. We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency. For every detected return, R2M-Bench compar...

</details>

---

### [SpatialCrafter: Single Image World Modeling with Generative 3D Proxies](https://arxiv.org/abs/2608.27073v1)

**Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo et al. (11 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.27073v1) | [PDF](https://arxiv.org/pdf/2608.27073v1.pdf) | [Project Page](https://fangchuan.github.io/SpatialCrafter/)

<details>
<summary>Abstract</summary>

Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generati...

</details>

---

### [Decoupling Planning and Control for Instructable Agents](https://arxiv.org/abs/2608.26788v1)

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr

**Published:** 2026-08-27 | **Categories:** cs.AI, cs.CL, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2608.26788v1) | [PDF](https://arxiv.org/pdf/2608.26788v1.pdf) | [Project Page](https://zinengtang.github.io/instruct-to-act/)

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model c...

</details>

---

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

## Other Recent Papers

### [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](https://arxiv.org/abs/2608.27367v1)

**Authors:** Frederik Berenz

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.27367v1) | [PDF](https://arxiv.org/pdf/2608.27367v1.pdf)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transform...

</details>

---

### [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345v1)

**Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević et al. (14 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.27345v1) | [PDF](https://arxiv.org/pdf/2608.27345v1.pdf)

<details>
<summary>Abstract</summary>

Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recove...

</details>

---

### [WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](https://arxiv.org/abs/2608.26239v1)

**Authors:** Maeve Zhang, Rain Sun, Xiang Wang, Cyril Zhang, Shalfun Li et al. (25 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.26239v1) | [PDF](https://arxiv.org/pdf/2608.26239v1.pdf)

<details>
<summary>Abstract</summary>

Generative world models provide robots with predictive models of how the world evolves under interaction, with growing potential for simulation, planning, policy evaluation, and robot learning. Beyond clip-level future prediction, a unified generative formulation should relate actions to consequences, support flexible horizons and continuous interaction, and enable reward-driven optimization. We introduce WALL-SS, a world model that generates visual futures through Scale-wise autoregressive Scal...

</details>

---

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

### [Surgical Video Generation From Diffusion to World Models: A Survey](https://arxiv.org/abs/2608.26214v1)

**Authors:** Fuxiang Huang, Chenxu Zhang, Liang Han, Lei Zhang

**Published:** 2026-08-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.26214v1) | [PDF](https://arxiv.org/pdf/2608.26214v1.pdf)

<details>
<summary>Abstract</summary>

Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framew...

</details>

---

### [4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v2)

**Authors:** Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou et al. (7 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.25479v2) | [PDF](https://arxiv.org/pdf/2608.25479v2.pdf)

<details>
<summary>Abstract</summary>

Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combi...

</details>

---
