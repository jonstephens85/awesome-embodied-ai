# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-03 22:22 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)

**Authors:** Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov et al. (7 authors)

**Published:** 2026-04-02 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.02330v1) | [PDF](https://arxiv.org/pdf/2604.02330v1.pdf) | [Project Page](https://action-party.github.io/)

<details>
<summary>Abstract</summary>

Recent advances in video diffusion have enabled the development of "world models" capable of simulating interactive environments. However, these models are largely restricted to single-agent settings, failing to control multiple agents simultaneously in a scene. In this work, we tackle a fundamental issue of action binding in existing video diffusion models, which struggle to associate specific actions with their corresponding subjects. For this purpose, we propose ActionParty, an action control...

</details>

---

### [World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry](https://arxiv.org/abs/2604.01985v1)

**Authors:** Yuejiang Liu, Fan Feng, Lingjing Kong, Weifeng Lu, Jinzhou Tang et al. (9 authors)

**Published:** 2026-04-02 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.01985v1) | [PDF](https://arxiv.org/pdf/2604.01985v1.pdf) | [Project Page](https://world-action-verifier.github.io)

<details>
<summary>Abstract</summary>

General-purpose world models promise scalable policy evaluation, optimization, and planning, yet achieving the required level of robustness remains challenging. Unlike policy learning, which primarily focuses on optimal actions, a world model must be reliable over a much broader range of suboptimal actions, which are often insufficiently covered by action-labeled interaction data. To address this challenge, we propose World Action Verifier (WAV), a framework that enables world models to identify...

</details>

---

### [DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)

**Authors:** Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao et al. (11 authors)

**Published:** 2026-04-02 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.01765v1) | [PDF](https://arxiv.org/pdf/2604.01765v1.pdf) | [Project Page](https://drivedreamer-policy.github.io/)

<details>
<summary>Abstract</summary>

Recently, world-action models (WAM) have emerged to bridge vision-language-action (VLA) models and world models, unifying their reasoning and instruction-following capabilities and spatio-temporal world modeling. However, existing WAM approaches often focus on modeling 2D appearance or latent representations, with limited geometric grounding-an essential element for embodied systems operating in the physical world. We present DriveDreamer-Policy, a unified driving world-action model that integra...

</details>

---

## Other Recent Papers

### [Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation](https://arxiv.org/abs/2604.02289v1)

**Authors:** Chongjie Ye, Cheng Cao, Chuanyu Pan, Yiming Hao, Yihao Zhi et al. (7 authors)

**Published:** 2026-04-02 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.02289v1) | [PDF](https://arxiv.org/pdf/2604.02289v1.pdf)

<details>
<summary>Abstract</summary>

Recent multimodal large language models have achieved strong performance in unified text and image understanding and generation, yet extending such native capability to 3D remains challenging due to limited data. Compared to abundant 2D imagery, high-quality 3D assets are scarce, making 3D synthesis under-constrained. Existing methods often rely on indirect pipelines that edit in 2D and lift results into 3D via optimization, sacrificing geometric consistency. We present Omni123, a 3D-native foun...

</details>

---

### [LatentUM: Unleashing the Potential of Interleaved Cross-Modal Reasoning via a Latent-Space Unified Model](https://arxiv.org/abs/2604.02097v1)

**Authors:** Jiachun Jin, Zetong Zhou, Xiao Yang, Hao Zhang, Pengfei Liu et al. (7 authors)

**Published:** 2026-04-02 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.02097v1) | [PDF](https://arxiv.org/pdf/2604.02097v1.pdf)

<details>
<summary>Abstract</summary>

Unified models (UMs) hold promise for their ability to understand and generate content across heterogeneous modalities. Compared to merely generating visual content, the use of UMs for interleaved cross-modal reasoning is more promising and valuable, e.g., for solving understanding problems that require dense visual thinking, improving visual generation through self-reflection, or modeling visual dynamics of the physical world guided by stepwise action interventions. However, existing UMs necess...

</details>

---

### [ModTrans: Translating Real-world Models for Distributed Training Simulator](https://arxiv.org/abs/2604.01607v1)

**Authors:** Yi Lyu

**Published:** 2026-04-02 | **Categories:** cs.DC, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.01607v1) | [PDF](https://arxiv.org/pdf/2604.01607v1.pdf)

<details>
<summary>Abstract</summary>

Large-scale distributed training has been a research hot spot in machine learning systems for industry and academia in recent years. However, conducting experiments without physical machines and corresponding resources is difficult. One solution is to leverage distributed training simulators, but current ones like ASTRA-sim do not support importing real-world developed models, which poses challenges for ML researchers seeking to use them. Based on this challenge, we developed ModTrans, a transla...

</details>

---

### [F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)

**Authors:** Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu et al. (6 authors)

**Published:** 2026-04-02 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.01605v1) | [PDF](https://arxiv.org/pdf/2604.01605v1.pdf)

<details>
<summary>Abstract</summary>

We present F3DGS, a federated 3D Gaussian Splatting framework for decentralized multi-agent 3D reconstruction. Existing 3DGS pipelines assume centralized access to all observations, which limits their applicability in distributed robotic settings where agents operate independently, and centralized data aggregation may be restricted. Directly extending centralized training to multi-agent systems introduces communication overhead and geometric inconsistency. F3DGS first constructs a shared geometr...

</details>

---

### [Semantic Modeling for World-Centered Architectures](https://arxiv.org/abs/2604.01359v1)

**Authors:** Andrei Mantsivoda, Darya Gavrilina

**Published:** 2026-04-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.01359v1) | [PDF](https://arxiv.org/pdf/2604.01359v1.pdf)

<details>
<summary>Abstract</summary>

We introduce world-centered multi-agent systems (WMAS) as an alternative to traditional agent-centered architectures, arguing that structured domains such as enterprises and institutional systems require a shared, explicit world representation to ensure semantic consistency, explainability, and long-term stability. We classify worlds along dimensions including ontological explicitness, normativity, etc. In WMAS, learning and coordination operate over a shared world model rather than isolated age...

</details>

---

### [Safety, Security, and Cognitive Risks in World Models](https://arxiv.org/abs/2604.01346v1)

**Authors:** Manoj Parmar

**Published:** 2026-04-01 | **Categories:** cs.CR, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.01346v1) | [PDF](https://arxiv.org/pdf/2604.01346v1.pdf)

<details>
<summary>Abstract</summary>

World models -- learned internal simulators of environment dynamics -- are rapidly becoming foundational to autonomous decision-making in robotics, autonomous vehicles, and agentic AI. Yet this predictive power introduces a distinctive set of safety, security, and cognitive risks. Adversaries can corrupt training data, poison latent representations, and exploit compounding rollout errors to cause catastrophic failures in safety-critical deployments. World model-equipped agents are more capable o...

</details>

---

### [DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)

**Authors:** Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou et al. (11 authors)

**Published:** 2026-04-01 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.00969v1) | [PDF](https://arxiv.org/pdf/2604.00969v1.pdf)

<details>
<summary>Abstract</summary>

Vision-based autonomous driving has gained much attention due to its low costs and excellent performance. Compared with dense BEV (Bird's Eye View) or sparse query models, Gaussian-centric method is a comprehensive yet sparse representation by describing scene with 3D semantic Gaussians. In this paper, we introduce DLWM, a novel paradigm with Dual Latent World Models specifically designed to enable holistic gaussian-centric pre-training in autonomous driving using two stages. In the first stage,...

</details>

---
