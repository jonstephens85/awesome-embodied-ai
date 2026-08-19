# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-19 16:29 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077v1)

**Authors:** Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du et al. (11 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.18077v1) | [PDF](https://arxiv.org/pdf/2608.18077v1.pdf) | [Project Page](https://nvidia-isaac.github.io/video_to_data/hydra-0/)

<details>
<summary>Abstract</summary>

We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion. This shared visual interface enables generalist world modeling and control by learning action consequences across embodiments, tasks, environments, and video-generation backbones. Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient ad...

</details>

---

### [An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](https://arxiv.org/abs/2608.17956v1)

**Authors:** Javier Aguilar Martín

**Published:** 2026-08-18 | **Categories:** cs.LG, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2608.17956v1) | [PDF](https://arxiv.org/pdf/2608.17956v1.pdf) | [GitHub](https://github.com/JaviMaligno/code-world-models)

<details>
<summary>Abstract</summary>

In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On th...

</details>

---

### [No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models](https://arxiv.org/abs/2608.17542v1)

**Authors:** Jack Boylan, Chris Hokamp

**Published:** 2026-08-18 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.17542v1) | [PDF](https://arxiv.org/pdf/2608.17542v1.pdf) | [GitHub](https://github.com/jackboyla/action-contrastive-jepa)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future embeddings, but the objective admits a trivial solution of a constant encoder, so every practical system adds an anti-collapse mechanism (LeCun, 2022; Assran et al., 2023; Bardes et al., 2022; 2024). LeWorldModel (LeWM) prevents collapse with SIGReg, a regularizer that forces the latent distribution to match an isotropic Gaussian: the representation is stabilized by prescribing what it must look like, indepe...

</details>

---

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

### [Towards Zero-Shot Task Transfer with Neurosymbolic World Models](https://arxiv.org/abs/2608.17959v1)

**Authors:** Isidoro Tamassia, Lennert De Smet, Giuseppe Marra

**Published:** 2026-08-18 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.17959v1) | [PDF](https://arxiv.org/pdf/2608.17959v1.pdf)

<details>
<summary>Abstract</summary>

State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlying environment. While expressive, these models are generally task-dependent: they learn uninterpretable latent representations that are tied to the training task and thus hard to generalize to new tasks. In this work, we present a novel world model formulation where the reward prediction only depends...

</details>

---

### [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](https://arxiv.org/abs/2608.17496v1)

**Authors:** Kaiming Zhong, Tianhua Liu, Yue Wang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17496v1) | [PDF](https://arxiv.org/pdf/2608.17496v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pip...

</details>

---

### [Q-Learning With World Models](https://arxiv.org/abs/2608.17163v1)

**Authors:** Perry Dong, Yueru Jia, Chelsea Finn, Dorsa Sadigh

**Published:** 2026-08-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.17163v1) | [PDF](https://arxiv.org/pdf/2608.17163v1.pdf)

<details>
<summary>Abstract</summary>

Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which ...

</details>

---

### [Inference-Time Attention Steering for Vision-Language-Action Driving Models](https://arxiv.org/abs/2608.17095v1)

**Authors:** Darshan Nagendra Prasad, Lars Ullrich, Knut Graichen

**Published:** 2026-08-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.17095v1) | [PDF](https://arxiv.org/pdf/2608.17095v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining. We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone. It is applied as a fail open forward pre-hook with no weight changes. On 50 lane-change scenarios from the Physical AI...

</details>

---

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
