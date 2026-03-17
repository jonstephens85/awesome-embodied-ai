# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-17 22:23 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)

**Authors:** Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin et al. (13 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.15583v1) | [PDF](https://arxiv.org/pdf/2603.15583v1.pdf) | [Project Page](https://seoul-world-model.github.io/)

<details>
<summary>Abstract</summary>

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including tempo...

</details>

---

### [NavThinker: Action-Conditioned World Models for Coupled Prediction and Planning in Social Navigation](https://arxiv.org/abs/2603.15359v1)

**Authors:** Tianshuai Hu, Zeying Gong, Lingdong Kong, XiaoDong Mei, Yiyi Ding et al. (10 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15359v1) | [PDF](https://arxiv.org/pdf/2603.15359v1.pdf) | [GitHub](https://github.com/hutslib/NavThinker)

<details>
<summary>Abstract</summary>

Social navigation requires robots to act safely in dynamic human environments. Effective behavior demands thinking ahead: reasoning about how the scene and pedestrians evolve under different robot actions rather than reacting to current observations alone. This creates a coupled prediction-planning challenge, where robot actions and human motion mutually influence each other. To address this challenge, we propose NavThinker, a future-aware framework that couples an action-conditioned world model...

</details>

---

### [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)

**Authors:** Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong et al. (8 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.14948v1) | [PDF](https://arxiv.org/pdf/2603.14948v1.pdf) | [GitHub](https://github.com/TabGuigui/WorldDrive)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving aims to generate safe and plausible planning policies from raw sensor input. Driving world models have shown great potential in learning rich representations by predicting the future evolution of a driving scene. However, existing driving world models primarily focus on visual scene representation, and motion representation is not explicitly designed to be planner-shared and inheritable, leaving a schism between the optimization of visual scene generation and the re...

</details>

---

### [WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems](https://arxiv.org/abs/2603.14392v1)

**Authors:** Yuchen Wang, Jiangtao Kong, Sizhe Wei, Xiaochang Li, Haohong Lin et al. (9 authors)

**Published:** 2026-03-15 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.14392v1) | [PDF](https://arxiv.org/pdf/2603.14392v1.pdf) | [Project Page](https://westworldrobot.github.io/)

<details>
<summary>Abstract</summary>

Trajectory world models play a crucial role in robotic dynamics learning, planning, and control. While recent works have explored trajectory world models for diverse robotic systems, they struggle to scale to a large number of distinct system dynamics and overlook domain knowledge of physical structures. To address these limitations, we introduce WestWorld, a knoWledge-Encoded Scalable Trajectory World model for diverse robotic systems. To tackle the scalability challenge, we propose a novel sys...

</details>

---

### [The Pulse of Motion: Measuring Physical Frame Rate from Visual Dynamics](https://arxiv.org/abs/2603.14375v1)

**Authors:** Xiangbo Gao, Mingyang Wu, Siyuan Yang, Jiongze Yu, Pardis Taghavi et al. (7 authors)

**Published:** 2026-03-15 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.14375v1) | [PDF](https://arxiv.org/pdf/2603.14375v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

While recent generative video models have achieved remarkable visual realism and are being explored as world models, true physical simulation requires mastering both space and time. Current models can produce visually smooth kinematics, yet they lack a reliable internal motion pulse to ground these motions in a consistent, real-world time scale. This temporal ambiguity stems from the common practice of indiscriminately training on videos with vastly different real-world speeds, forcing them into...

</details>

---

## Other Recent Papers

### [RS-WorldModel: a Unified Model for Remote Sensing Understanding and Future Sense Forecasting](https://arxiv.org/abs/2603.14941v1)

**Authors:** Linrui Xu, Zhongan Wang, Fei Shen, Gang Xu, Huiping Zhuang et al. (7 authors)

**Published:** 2026-03-16 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.14941v1) | [PDF](https://arxiv.org/pdf/2603.14941v1.pdf)

<details>
<summary>Abstract</summary>

Remote sensing world models aim to both explain observed changes and forecast plausible futures, two tasks that share spatiotemporal priors. Existing methods, however, typically address them separately, limiting cross-task transfer. We present RS-WorldModel, a unified world model for remote sensing that jointly handles spatiotemporal change understanding and text-guided future scene forecasting, and we build RSWBench-1.1M, a 1.1 million sample dataset with rich language annotations covering both...

</details>

---

### [PerlAD: Towards Enhanced Closed-loop End-to-end Autonomous Driving with Pseudo-simulation-based Reinforcement Learning](https://arxiv.org/abs/2603.14908v1)

**Authors:** Yinfeng Gao, Qichao Zhang, Deqing Liu, Zhongpu Xia, Guang Li et al. (11 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.14908v1) | [PDF](https://arxiv.org/pdf/2603.14908v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving policies based on Imitation Learning (IL) often struggle in closed-loop execution due to the misalignment between inadequate open-loop training objectives and real driving requirements. While Reinforcement Learning (RL) offers a solution by directly optimizing driving goals via reward signals, the rendering-based training environments introduce the rendering gap and are inefficient due to high computational costs. To overcome these challenges, we present a novel Pse...

</details>

---

### [WorldVLM: Combining World Model Forecasting and Vision-Language Reasoning](https://arxiv.org/abs/2603.14497v1)

**Authors:** Stefan Englmeier, Katharina Winter, Fabian B. Flohr

**Published:** 2026-03-15 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.14497v1) | [PDF](https://arxiv.org/pdf/2603.14497v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving systems depend on on models that can reason about high-level scene contexts and accurately predict the dynamics of their surrounding environment. Vision- Language Models (VLMs) have recently emerged as promising tools for decision-making and scene understanding, offering strong capabilities in contextual reasoning. However, their limited spatial comprehension constrains their effectiveness as end-to-end driving models. World Models (WM) internalize environmental dynamics to pr...

</details>

---

### [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v1)

**Authors:** Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha et al. (9 authors)

**Published:** 2026-03-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.14482v1) | [PDF](https://arxiv.org/pdf/2603.14482v1.pdf)

<details>
<summary>Abstract</summary>

We present V-JEPA 2.1, a family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding. The approach combines four key components. First, a dense predictive loss uses a masking-based objective in which both visible and masked tokens contribute to the training signal, encouraging explicit spatial and temporal grounding. Second, deep self-supervision applies the self-supervised objective hierarchi...

</details>

---
