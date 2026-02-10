# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-10 22:30 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Horizon Imagination: Efficient On-Policy Training in Diffusion World Models](https://arxiv.org/abs/2602.08032v1)

**Authors:** Lior Cohen, Ofir Nabati, Kaixin Wang, Navdeep Kumar, Shie Mannor

**Published:** 2026-02-08 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.08032v1) | [PDF](https://arxiv.org/pdf/2602.08032v1.pdf) | [GitHub](https://github.com/leor-c/horizon-imagination)

<details>
<summary>Abstract</summary>

We study diffusion-based world models for reinforcement learning, which offer high generative fidelity but face critical efficiency challenges in control. Current methods either require heavyweight models at inference or rely on highly sequential imagination, both of which impose prohibitive computational costs. We propose Horizon Imagination (HI), an on-policy imagination process for discrete stochastic policies that denoises multiple future observations in parallel. HI incorporates a stabiliza...

</details>

---

### [MIND: Benchmarking Memory Consistency and Action Control in World Models](https://arxiv.org/abs/2602.08025v1)

**Authors:** Yixuan Ye, Xuanyu Lu, Yuxin Jiang, Yuchao Gu, Rui Zhao et al. (10 authors)

**Published:** 2026-02-08 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.08025v1) | [PDF](https://arxiv.org/pdf/2602.08025v1.pdf) | [Project Page](https://csu-jpg.github.io/MIND.github.io/)

<details>
<summary>Abstract</summary>

World models aim to understand, remember, and predict dynamic visual environments, yet a unified benchmark for evaluating their fundamental abilities remains lacking. To address this gap, we introduce MIND, the first open-domain closed-loop revisited benchmark for evaluating Memory consIstency and action coNtrol in worlD models. MIND contains 250 high-quality videos at 1080p and 24 FPS, including 100 (first-person) + 100 (third-person) video clips under a shared action space and 25 + 25 clips ac...

</details>

---

## Other Recent Papers

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

### [Geometry-Aware Rotary Position Embedding for Consistent Video World Model](https://arxiv.org/abs/2602.07854v1)

**Authors:** Chendong Xiang, Jiajun Liu, Jintao Zhang, Xiao Yang, Zhengwei Fang et al. (10 authors)

**Published:** 2026-02-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.07854v1) | [PDF](https://arxiv.org/pdf/2602.07854v1.pdf)

<details>
<summary>Abstract</summary>

Predictive world models that simulate future observations under explicit camera control are fundamental to interactive AI. Despite rapid advances, current systems lack spatial persistence: they fail to maintain stable scene structures over long trajectories, frequently hallucinating details when cameras revisit previously observed locations. We identify that this geometric drift stems from reliance on screen-space positional embeddings, which conflict with the projective geometry required for 3D...

</details>

---
