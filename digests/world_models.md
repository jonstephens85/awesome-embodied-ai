# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-11 17:04 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Olaf-World: Orienting Latent Actions for Video World Modeling](https://arxiv.org/abs/2602.10104v1)

**Authors:** Yuxin Jiang, Yuchao Gu, Ivor W. Tsang, Mike Zheng Shou

**Published:** 2026-02-10 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.10104v1) | [PDF](https://arxiv.org/pdf/2602.10104v1.pdf) | [Project Page](https://showlab.github.io/Olaf-World/) | [GitHub](https://github.com/showlab/Olaf-World)

<details>
<summary>Abstract</summary>

Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate only within each clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, the...

</details>

---

### [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.10090v1)

**Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, Yite Wang, Siwei Han et al. (8 authors)

**Published:** 2026-02-10 | **Categories:** cs.AI, cs.CL, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.10090v1) | [PDF](https://arxiv.org/pdf/2602.10090v1.pdf) | [GitHub](https://github.com/Snowflake-Labs/agent-world-model)

<details>
<summary>Abstract</summary>

Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (...

</details>

---

### [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856v1)

**Authors:** Yuhao Zheng, Li'an Zhong, Yi Wang, Rui Dai, Kaikui Liu et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2602.09856v1) | [PDF](https://arxiv.org/pdf/2602.09856v1.pdf) | [Project Page](https://amap-ml.github.io/Code2World/) | [GitHub](https://github.com/AMAP-ML/Code2World)

<details>
<summary>Abstract</summary>

Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generat...

</details>

---

### [WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022v1)

**Authors:** Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu et al. (12 authors)

**Published:** 2026-02-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.09022v1) | [PDF](https://arxiv.org/pdf/2602.09022v1.pdf) | [Project Page](\url{https://3d-models.hunyuan.tencent.com/world/})

<details>
<summary>Abstract</summary>

This work presents WorldCompass, a novel Reinforcement Learning (RL) post-training framework for the long-horizon, interactive video-based world models, enabling them to explore the world more accurately and consistently based on interaction signals. To effectively "steer" the world model's exploration, we introduce three core innovations tailored to the autoregressive video generation paradigm: 1) Clip-level rollout Strategy: We generate and evaluate multiple samples at a single target clip, wh...

</details>

---

### [When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning](https://arxiv.org/abs/2602.08236v1)

**Authors:** Shoubin Yu, Yue Zhang, Zun Wang, Jaehong Yoon, Huaxiu Yao et al. (7 authors)

**Published:** 2026-02-09 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2602.08236v1) | [PDF](https://arxiv.org/pdf/2602.08236v1.pdf) | [Project Page](https://adaptive-visual-tts.github.io/)

<details>
<summary>Abstract</summary>

Despite rapid progress in Multimodal Large Language Models (MLLMs), visual spatial reasoning remains unreliable when correct answers depend on how a scene would appear under unseen or alternative viewpoints. Recent work addresses this by augmenting reasoning with world models for visual imagination, but questions such as when imagination is actually necessary, how much of it is beneficial, and when it becomes harmful, remain poorly understood. In practice, indiscriminate imagination can increase...

</details>

---

## Other Recent Papers

### [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098v1)

**Authors:** Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10098v1) | [PDF](https://arxiv.org/pdf/2602.10098v1.pdf)

<details>
<summary>Abstract</summary>

Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a JEPA-style pretraining framework that sidesteps these pitfalls by design. The key idea is \emph{leakage-free state prediction}: a target encoder prod...

</details>

---

### [Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning](https://arxiv.org/abs/2602.10044v1)

**Authors:** Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, Dileep Kalathil, P. R. Kumar

**Published:** 2026-02-10 | **Categories:** cs.LG, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2602.10044v1) | [PDF](https://arxiv.org/pdf/2602.10044v1.pdf)

<details>
<summary>Abstract</summary>

Efficient exploration remains a central challenge in reinforcement learning (RL), particularly in sparse-reward environments. We introduce Optimistic World Models (OWMs), a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likelihood estimation (RBMLE) from adaptive control into deep RL. In contrast to upper confidence bound (UCB)-style exploration methods, OWMs incorporate optimism directly into model learning by augmentation with an optimi...

</details>

---

### [MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation](https://arxiv.org/abs/2602.09878v1)

**Authors:** Jiaxu Wang, Yicheng Jiang, Tianlun He, Jingkai Sun, Qiang Zhang et al. (11 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.09878v1) | [PDF](https://arxiv.org/pdf/2602.09878v1.pdf)

<details>
<summary>Abstract</summary>

World-model-based imagine-then-act becomes a promising paradigm for robotic manipulation, yet existing approaches typically support either purely image-based forecasting or reasoning over partial 3D geometry, limiting their ability to predict complete 4D scene dynamics. This work proposes a novel embodied 4D world model that enables geometrically consistent, arbitrary-view RGBD generation: given only a single-view RGBD observation as input, the model imagines the remaining viewpoints, which can ...

</details>

---

### [Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)

**Authors:** Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen et al. (6 authors)

**Published:** 2026-02-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.09600v1) | [PDF](https://arxiv.org/pdf/2602.09600v1.pdf)

<details>
<summary>Abstract</summary>

Egocentric interactive world models are essential for augmented reality and embodied AI, where visual generation must respond to user input with low latency, geometric consistency, and long-term stability. We study egocentric interaction generation from a single scene image under free-space hand gestures, aiming to synthesize photorealistic videos in which hands enter the scene, interact with objects, and induce plausible world dynamics under head motion. This setting introduces fundamental chal...

</details>

---

### [WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971v1)

**Authors:** Yu Shang, Zhuohang Li, Yiding Ma, Weikang Su, Xin Jin et al. (19 authors)

**Published:** 2026-02-09 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.08971v1) | [PDF](https://arxiv.org/pdf/2602.08971v1.pdf)

<details>
<summary>Abstract</summary>

While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility of these models in downstream decision-making tasks. In this work, we introduce WorldArena, a unified benchmark designed to systematical...

</details>

---

### [stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2602.08968v1)

**Authors:** Lucas Maes, Quentin Le Lidec, Dan Haramati, Nassim Massaudi, Damien Scieur et al. (7 authors)

**Published:** 2026-02-09 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.08968v1) | [PDF](https://arxiv.org/pdf/2602.08968v1.pdf)

<details>
<summary>Abstract</summary>

World Models have emerged as a powerful paradigm for learning compact, predictive representations of environment dynamics, enabling agents to reason, plan, and generalize beyond direct experience. Despite recent interest in World Models, most available implementations remain publication-specific, severely limiting their reusability, increasing the risk of bugs, and reducing evaluation standardization. To mitigate these issues, we introduce stable-worldmodel (SWM), a modular, tested, and document...

</details>

---
