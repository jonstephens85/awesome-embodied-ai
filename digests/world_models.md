# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-28 00:45 UTC

**Papers found:** 7

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
