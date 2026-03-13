# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-13 22:20 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [O3N: Omnidirectional Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2603.12144v1)

**Authors:** Mengfei Duan, Hao Shi, Fei Teng, Guoqiang Zhao, Yuheng Zhang et al. (7 authors)

**Published:** 2026-03-12 | **Categories:** cs.CV, cs.RO, eess.IV

**Links:** [arXiv](https://arxiv.org/abs/2603.12144v1) | [PDF](https://arxiv.org/pdf/2603.12144v1.pdf) | [GitHub](https://github.com/MengfeiD/O3N)

<details>
<summary>Abstract</summary>

Understanding and reconstructing the 3D world through omnidirectional perception is an inevitable trend in the development of autonomous agents and embodied intelligence. However, existing 3D occupancy prediction methods are constrained by limited perspective inputs and predefined training distribution, making them difficult to apply to embodied agents that require comprehensive and safe perception of scenes in open world exploration. To address this, we present O3N, the first purely visual, end...

</details>

---

### [InSpatio-WorldFM: An Open-Source Real-Time Generative Frame Model](https://arxiv.org/abs/2603.11911v1)

**Authors:**  InSpatio Team, Xiaoyu Zhang, Weihong Pan, Zhichao Ye, Jialin Liu et al. (19 authors)

**Published:** 2026-03-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.11911v1) | [PDF](https://arxiv.org/pdf/2603.11911v1.pdf) | [Project Page](https://inspatio.github.io/worldfm/) | [GitHub](https://github.com/inspatio/worldfm)

<details>
<summary>Abstract</summary>

We present InSpatio-WorldFM, an open-source real-time frame model for spatial intelligence. Unlike video-based world models that rely on sequential frame generation and incur substantial latency due to window-level processing, InSpatio-WorldFM adopts a frame-based paradigm that generates each frame independently, enabling low-latency real-time spatial inference. By enforcing multi-view spatial consistency through explicit 3D anchors and implicit spatial memory, the model preserves global scene g...

</details>

---

### [World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)

**Authors:** An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma et al. (9 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.10422v1) | [PDF](https://arxiv.org/pdf/2603.10422v1.pdf) | [Project Page](https://wm2act.github.io/)

<details>
<summary>Abstract</summary>

World Models (WMs) have emerged as a promising approach for post-training Vision-Language-Action (VLA) policies to improve robustness and generalization under environmental changes. However, most WM-based post-training methods rely on pixel-space supervision, making policies sensitive to pixel-level artifacts and hallucination from imperfect WM rollouts. We introduce World2Act, a post-training framework that aligns VLA actions directly with WM video-dynamics latents using a contrastive matching ...

</details>

---

## Other Recent Papers

### [Temporal Straightening for Latent Planning](https://arxiv.org/abs/2603.12231v1)

**Authors:** Ying Wang, Oumayma Bounou, Gaoyue Zhou, Randall Balestriero, Tim G. J. Rudner et al. (7 authors)

**Published:** 2026-03-12 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.12231v1) | [PDF](https://arxiv.org/pdf/2603.12231v1.pdf)

<details>
<summary>Abstract</summary>

Learning good representations is essential for latent planning with world models. While pretrained visual encoders produce strong semantic visual features, they are not tailored to planning and contain information irrelevant -- or even detrimental -- to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening to improve representation learning for latent planning. Using a curvature regularizer that encourages locally straighten...

</details>

---

### [Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)

**Authors:** Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang et al. (8 authors)

**Published:** 2026-03-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.11534v1) | [PDF](https://arxiv.org/pdf/2603.11534v1.pdf)

<details>
<summary>Abstract</summary>

Generating safety-critical driving scenarios is crucial for evaluating and improving autonomous driving systems, but long-tail risky situations are rarely observed in real-world data and difficult to specify through manual scenario design. Existing generative approaches typically treat risk as an after-the-fact label and struggle to maintain geometric consistency in multi-view driving scenes. We present RiskMV-DPO, a general and systematic pipeline for physically-informed, risk-controllable mult...

</details>

---

### [ARROW: Augmented Replay for RObust World models](https://arxiv.org/abs/2603.11395v1)

**Authors:** Abdulaziz Alyahya, Abdallah Al Siyabi, Markus R. Ernst, Luke Yang, Levin Kuhlmann et al. (6 authors)

**Published:** 2026-03-12 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.11395v1) | [PDF](https://arxiv.org/pdf/2603.11395v1.pdf)

<details>
<summary>Abstract</summary>

Continual reinforcement learning challenges agents to acquire new skills while retaining previously learned ones with the goal of improving performance in both past and future tasks. Most existing approaches rely on model-free methods with replay buffers to mitigate catastrophic forgetting; however, these solutions often face significant scalability challenges due to large memory demands. Drawing inspiration from neuroscience, where the brain replays experiences to a predictive World Model rathe...

</details>

---

### [PPGuide: Steering Diffusion Policies with Performance Predictive Guidance](https://arxiv.org/abs/2603.10980v1)

**Authors:** Zixing Wang, Devesh K. Jha, Ahmed H. Qureshi, Diego Romeres

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10980v1) | [PDF](https://arxiv.org/pdf/2603.10980v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion policies have shown to be very efficient at learning complex, multi-modal behaviors for robotic manipulation. However, errors in generated action sequences can compound over time which can potentially lead to failure. Some approaches mitigate this by augmenting datasets with expert demonstrations or learning predictive world models which might be computationally expensive. We introduce Performance Predictive Guidance (PPGuide), a lightweight, classifier-based framework that steers a pr...

</details>

---

### [ResWM: Residual-Action World Model for Visual RL](https://arxiv.org/abs/2603.11110v1)

**Authors:** Jseen Zhang, Gabriel Adineera, Jinzhou Tan, Jinoh Kim

**Published:** 2026-03-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.11110v1) | [PDF](https://arxiv.org/pdf/2603.11110v1.pdf)

<details>
<summary>Abstract</summary>

Learning predictive world models from raw visual observations is a central challenge in reinforcement learning (RL), especially for robotics and continuous control. Conventional model-based RL frameworks directly condition future predictions on absolute actions, which makes optimization unstable: the optimal action distributions are task-dependent, unknown a priori, and often lead to oscillatory or inefficient control. To address this, we introduce the Residual-Action World Model (ResWM), a new ...

</details>

---

### [World Model for Battery Degradation Prediction Under Non-Stationary Aging](https://arxiv.org/abs/2603.10527v1)

**Authors:** Kai Chin Lim, Khay Wai See

**Published:** 2026-03-11 | **Categories:** cs.LG, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2603.10527v1) | [PDF](https://arxiv.org/pdf/2603.10527v1.pdf)

<details>
<summary>Abstract</summary>

Degradation prognosis for lithium-ion cells requires forecasting the state-of-health (SOH) trajectory over future cycles. Existing data-driven approaches can produce trajectory outputs through direct regression, but lack a mechanism to propagate degradation dynamics forward in time. This paper formulates battery degradation prognosis as a world model problem, encoding raw voltage, current, and temperature time-series from each cycle into a latent state and propagating it forward via a learned dy...

</details>

---
