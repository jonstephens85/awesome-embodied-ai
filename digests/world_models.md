# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-18 22:11 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885v1)

**Authors:** Xiaowei Cai, Yunuo Cai, Bingao Chen, Jingxiao Chen, Zhi Chen et al. (39 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16885v1) | [PDF](https://arxiv.org/pdf/2608.16885v1.pdf) | [Project Page](https://tau0-vla.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_0$-VLA, a hierarchical robot foundation model that formulates high-level subtask generation as a compute-scalable inference problem through w...

</details>

---

### [HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://arxiv.org/abs/2608.16859v1)

**Authors:** Weiliang Chen, Haowen Sun, Jun Gao, Jiawei Chi, Hanyang Wang et al. (43 authors)

**Published:** 2026-08-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16859v1) | [PDF](https://arxiv.org/pdf/2608.16859v1.pdf) | [Project Page](https://mirros-lab.github.io/HarnessEval-W)

<details>
<summary>Abstract</summary>

A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollout requires understanding whether physics, causality, and world state evolve correctly. Humans spot such violations naturally, yet no existing benchmark automates this capability: metrics are computed brute-force, leaving no reasoning chain that can be examined or verified. We introduce HarnessEval-...

</details>

---

### [Orbit-Planner: Towards Latent World Models for On-Orbit Obstacle Avoidance of Satellite Agents](https://arxiv.org/abs/2608.16651v1)

**Authors:** Zhijian Li, Chao Ren, Peijin Wang, Xian Sun

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16651v1) | [PDF](https://arxiv.org/pdf/2608.16651v1.pdf) | [Project Page](https://zhijianli2003.github.io/Orbit_Planner/) | [GitHub](https://github.com/ZhijianLi2003/Orbit_Planner)

<details>
<summary>Abstract</summary>

Satellite agents for on-orbit navigation tasks need to predict collision risks using limited onboard observations. However, conventional planners often rely on predefined maps and fixed environmental assumptions, limiting their adaptability in dynamic on-orbit scenarios. In this paper, we propose Orbit-Planner, a two-stage latent world model for on-orbit obstacle avoidance. Orbit-Planner learns action-conditioned spacecraft dynamics to perform future-state rollouts in latent space, and introduce...

</details>

---

## Other Recent Papers

### [CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?](https://arxiv.org/abs/2608.16829v1)

**Authors:** Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham et al. (6 authors)

**Published:** 2026-08-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16829v1) | [PDF](https://arxiv.org/pdf/2608.16829v1.pdf)

<details>
<summary>Abstract</summary>

Video world models approximate the stochastic distribution of physical outcomes through generative sampling, but existing benchmarks score individual generations or compare distributions coarsely over a whole dataset, leaving the fine-grained aleatoric uncertainty of specific phenomena untested. We introduce CaliBench, which scores outcomes in a physically interpretable discrete space - a bin index, a die face, a suit, a colour - rather than a learned feature space such as in FID, so the distanc...

</details>

---

### [DriveCache: Action-Aware Caching for Driving World Model Inference](https://arxiv.org/abs/2608.16354v1)

**Authors:** Jianchun Yang, Jian Liang, Xianda Guo, Pinhan Fu, Yanlun Peng et al. (8 authors)

**Published:** 2026-08-17 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16354v1) | [PDF](https://arxiv.org/pdf/2608.16354v1.pdf)

<details>
<summary>Abstract</summary>

Driving video generation models support autonomous-driving development by predicting controllable future scenes for simulation, planning evaluation, and offline data generation. Diffusion-based driving generators repeatedly evaluate large backbones across denoising steps, which limits generation throughput. Existing diffusion acceleration methods reduce this cost, but general-purpose designs omit driving signals available before generation, such as ego speed and planned trajectories. Experiments...

</details>

---

### [SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry](https://arxiv.org/abs/2608.16287v1)

**Authors:** Jiaming Hu, Yan Zheng, Tian Wang

**Published:** 2026-08-17 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.16287v1) | [PDF](https://arxiv.org/pdf/2608.16287v1.pdf)

<details>
<summary>Abstract</summary>

Joint-embedding predictive world models plan by scoring predicted terminal embeddings against a goal embedding using a cost defined on the representation itself. Two prominent strategies for obtaining non-collapsed representations are to inherit a pretrained feature space, as in DINO-WM, and to learn an embedding end to end with anti-collapse regularization, as in LeWorldModel (LeWM) with SIGReg. These strategies show complementary strengths across tasks. Although task-relevant state is decodabl...

</details>

---

### [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](https://arxiv.org/abs/2608.16234v1)

**Authors:** Tianchen Deng, Xuefeng Chen, Shuang Wu, Qu Chen, Jiajun Zhu et al. (8 authors)

**Published:** 2026-08-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16234v1) | [PDF](https://arxiv.org/pdf/2608.16234v1.pdf)

<details>
<summary>Abstract</summary>

Driving World Models (DWMs) have recently advanced rapidly with generative models, yet most existing methods mainly focus on conditional scene generation and lack explicit 3D scene understanding, language-grounded reasoning, and controllable 4D editing capabilities. Moreover, commonly used point cloud, occupancy, or BEV representations make it difficult to achieve fine-grained alignment between textual information and the underlying 3D scene structure. To address these limitations, we propose a ...

</details>

---

### [Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning](https://arxiv.org/abs/2608.15869v1)

**Authors:** Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang et al. (7 authors)

**Published:** 2026-08-16 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2608.15869v1) | [PDF](https://arxiv.org/pdf/2608.15869v1.pdf)

<details>
<summary>Abstract</summary>

Multimodal large language models increasingly use visual chain-of-thought (Visual CoT) to reason about spatial, temporal, and embodied environments. By generating intermediate reasoning images, Visual CoT provides an intuitive mechanism for visual foresight but introduces substantial inference overhead, which is particularly problematic for proactive video reasoning. We ask whether models can learn to think visually during training while reasoning directly at inference. We introduce Internalized...

</details>

---
