# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-03 16:53 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454v1)

**Authors:** Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, Yunzhe Zhang, Jiarao Liu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02454v1) | [PDF](https://arxiv.org/pdf/2602.02454v1.pdf) | [Project Page](https://world-gymnast.github.io/)

<details>
<summary>Abstract</summary>

Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world...

</details>

---

### [An Empirical Study of World Model Quantization](https://arxiv.org/abs/2602.02110v1)

**Authors:** Zhongqian Fu, Tianyi Zhao, Kai Han, Hang Zhou, Xinghao Chen et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02110v1) | [PDF](https://arxiv.org/pdf/2602.02110v1.pdf) | [GitHub](https://github.com/huawei-noah/noah-research/tree/master/QuantWM)

<details>
<summary>Abstract</summary>

World models learn an internal representation of environment dynamics, enabling agents to simulate and reason about future states within a compact latent space for tasks such as planning, prediction, and inference. However, running world models rely on hevay computational cost and memory footprint, making model quantization essential for efficient deployment. To date, the effects of post-training quantization (PTQ) on world models remain largely unexamined. In this work, we present a systematic ...

</details>

---

### [Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://arxiv.org/abs/2602.01801v1)

**Authors:** Dvir Samuel, Issar Tzachor, Matan Levy, Micahel Green, Gal Chechik et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.01801v1) | [PDF](https://arxiv.org/pdf/2602.01801v1.pdf) | [Project Page](https://dvirsamuel.github.io/fast-auto-regressive-video/)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models enable streaming generation, opening the door to long-form synthesis, video world models, and interactive neural game engines. However, their core attention layers become a major bottleneck at inference time: as generation progresses, the KV cache grows, causing both increasing latency and escalating GPU memory, which in turn restricts usable temporal context and harms long-range consistency. In this work, we study redundancy in autoregressive video diffusio...

</details>

---

### [DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](https://arxiv.org/abs/2602.01780v1)

**Authors:** Shicheng Yin, Kaixuan Yin, Weixing Chen, Yang Liu, Guanbin Li et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01780v1) | [PDF](https://arxiv.org/pdf/2602.01780v1.pdf) | [GitHub](https://github.com/HCPLabSYSU/DDP-WM)

<details>
<summary>Abstract</summary>

World models are essential for autonomous robotic planning. However, the substantial computational overhead of existing dense Transformerbased models significantly hinders real-time deployment. To address this efficiency-performance bottleneck, we introduce DDP-WM, a novel world model centered on the principle of Disentangled Dynamics Prediction (DDP). We hypothesize that latent state evolution in observed scenes is heterogeneous and can be decomposed into sparse primary dynamics driven by physi...

</details>

---

### [UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning](https://arxiv.org/abs/2602.01536v1)

**Authors:** Shuai Liu, Siheng Ren, Xiaoyao Zhu, Quanmin Liang, Zefeng Li et al. (8 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.01536v1) | [PDF](https://arxiv.org/pdf/2602.01536v1.pdf) | [GitHub](https://github.com/Say2L/UniDWM)

<details>
<summary>Abstract</summary>

Achieving reliable and efficient planning in complex driving environments requires a model that can reason over the scene's geometry, appearance, and dynamics. We present UniDWM, a unified driving world model that advances autonomous driving through multifaceted representation learning. UniDWM constructs a structure- and dynamic-aware latent world representation that serves as a physically grounded state space, enabling consistent reasoning across perception, prediction, and planning. Specifical...

</details>

---

## Other Recent Papers

### [Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory](https://arxiv.org/abs/2602.02393v1)

**Authors:** Ruiqi Wu, Xuanhua He, Meng Cheng, Tianyu Yang, Yong Zhang et al. (11 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02393v1) | [PDF](https://arxiv.org/pdf/2602.02393v1.pdf)

<details>
<summary>Abstract</summary>

We propose Infinite-World, a robust interactive world model capable of maintaining coherent visual memory over 1000+ frames in complex real-world environments. While existing world models can be efficiently optimized on synthetic data with perfect ground-truth, they lack an effective training paradigm for real-world videos due to noisy pose estimations and the scarcity of viewpoint revisits. To bridge this gap, we first introduce a Hierarchical Pose-free Memory Compressor (HPMC) that recursively...

</details>

---

### [Self-Supervised Learning from Structural Invariance](https://arxiv.org/abs/2602.02381v1)

**Authors:** Yipeng Zhang, Hafez Ghaemi, Jungyoon Lee, Shahab Bakhtiari, Eilif B. Muller et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.02381v1) | [PDF](https://arxiv.org/pdf/2602.02381v1.pdf)

<details>
<summary>Abstract</summary>

Joint-embedding self-supervised learning (SSL), the key paradigm for unsupervised representation learning from visual data, learns from invariances between semantically-related data pairs. We study the one-to-many mapping problem in SSL, where each datum may be mapped to multiple valid targets. This arises when data pairs come from naturally occurring generative processes, e.g., successive video frames. We show that existing methods struggle to flexibly capture this conditional uncertainty. As a...

</details>

---

### [Choice-Model-Assisted Q-learning for Delayed-Feedback Revenue Management](https://arxiv.org/abs/2602.02283v1)

**Authors:** Owen Shen, Patrick Jaillet

**Published:** 2026-02-02 | **Categories:** cs.LG, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2602.02283v1) | [PDF](https://arxiv.org/pdf/2602.02283v1.pdf)

<details>
<summary>Abstract</summary>

We study reinforcement learning for revenue management with delayed feedback, where a substantial fraction of value is determined by customer cancellations and modifications observed days after booking. We propose \emph{choice-model-assisted RL}: a calibrated discrete choice model is used as a fixed partial world model to impute the delayed component of the learning target at decision time. In the fixed-model deployment regime, we prove that tabular Q-learning with model-imputed targets converge...

</details>

---

### [UniDriveDreamer: A Single-Stage Multimodal World Model for Autonomous Driving](https://arxiv.org/abs/2602.02002v1)

**Authors:** Guosheng Zhao, Yaozeng Wang, Xiaofeng Wang, Zheng Zhu, Tingdong Yu et al. (13 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02002v1) | [PDF](https://arxiv.org/pdf/2602.02002v1.pdf)

<details>
<summary>Abstract</summary>

World models have demonstrated significant promise for data synthesis in autonomous driving. However, existing methods predominantly concentrate on single-modality generation, typically focusing on either multi-camera video or LiDAR sequence synthesis. In this paper, we propose UniDriveDreamer, a single-stage unified multimodal world model for autonomous driving, which directly generates multimodal future observations without relying on intermediate representations or cascaded modules. Our frame...

</details>

---

### [Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)

**Authors:** Christos Ziakas, Amir Bar, Alessandra Russo

**Published:** 2026-02-02 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.01960v1) | [PDF](https://arxiv.org/pdf/2602.01960v1.pdf)

<details>
<summary>Abstract</summary>

Large-scale video generative models have shown emerging capabilities as zero-shot visual planners, yet video-generated plans often violate temporal consistency and physical constraints, leading to failures when mapped to executable actions. To address this, we propose Grounding Video Plans with World Models (GVP-WM), a planning method that grounds video-generated plans into feasible action sequences using a learned action-conditioned world model. At test-time, GVP-WM first generates a video plan...

</details>

---

### [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725v1)

**Authors:** Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.01725v1) | [PDF](https://arxiv.org/pdf/2602.01725v1.pdf)

<details>
<summary>Abstract</summary>

With the widespread deployment of Computer-using Agents (CUAs) in complex real-world environments, prevalent long-term risks often lead to severe and irreversible consequences. Most existing guardrails for CUAs adopt a reactive approach, constraining agent behavior only within the current observation space. While these guardrails can prevent immediate short-term risks (e.g., clicking on a phishing link), they cannot proactively avoid long-term risks: seemingly reasonable actions can lead to high...

</details>

---

### [From Perception to Action: Spatial AI Agents and World Models](https://arxiv.org/abs/2602.01644v1)

**Authors:** Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.01644v1) | [PDF](https://arxiv.org/pdf/2602.01644v1.pdf)

<details>
<summary>Abstract</summary>

While large language models have become the prevailing approach for agentic reasoning and planning, their success in symbolic domains does not readily translate to the physical world. Spatial intelligence, the ability to perceive 3D structure, reason about object relationships, and act under physical constraints, is an orthogonal capability that proves important for embodied agents. Existing surveys address either agentic architectures or spatial domains in isolation. None provide a unified fram...

</details>

---

### [Research on World Models Is Not Merely Injecting World Knowledge into Specific Tasks](https://arxiv.org/abs/2602.01630v1)

**Authors:** Bohan Zeng, Kaixin Zhu, Daili Hua, Bozhou Li, Chengzhuo Tong et al. (27 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.01630v1) | [PDF](https://arxiv.org/pdf/2602.01630v1.pdf)

<details>
<summary>Abstract</summary>

World models have emerged as a critical frontier in AI research, aiming to enhance large models by infusing them with physical dynamics and world knowledge. The core objective is to enable agents to understand, predict, and interact with complex environments. However, current research landscape remains fragmented, with approaches predominantly focused on injecting world knowledge into isolated tasks, such as visual prediction, 3D estimation, or symbol grounding, rather than establishing a unifie...

</details>

---

### [Generative Visual Code Mobile World Models](https://arxiv.org/abs/2602.01576v1)

**Authors:** Woosung Koh, Sungjun Han, Segyu Lee, Se-Young Yun, Jamin Shin

**Published:** 2026-02-02 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.01576v1) | [PDF](https://arxiv.org/pdf/2602.01576v1.pdf)

<details>
<summary>Abstract</summary>

Mobile Graphical User Interface (GUI) World Models (WMs) offer a promising path for improving mobile GUI agent performance at train- and inference-time. However, current approaches face a critical trade-off: text-based WMs sacrifice visual fidelity, while the inability of visual WMs in precise text rendering led to their reliance on slow, complex pipelines dependent on numerous external models. We propose a novel paradigm: visual world modeling via renderable code generation, where a single Visi...

</details>

---

### [Mixture-of-World Models: Scaling Multi-Task Reinforcement Learning with Modular Latent Dynamics](https://arxiv.org/abs/2602.01270v1)

**Authors:** Boxuan Zhang, Weipu Zhang, Zhaohan Feng, Wei Xiao, Jian Sun et al. (7 authors)

**Published:** 2026-02-01 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.01270v1) | [PDF](https://arxiv.org/pdf/2602.01270v1.pdf)

<details>
<summary>Abstract</summary>

A fundamental challenge in multi-task reinforcement learning (MTRL) is achieving sample efficiency in visual domains where tasks exhibit substantial heterogeneity in both observations and dynamics. Model-based reinforcement learning offers a promising path to improved sample efficiency through world models, but standard monolithic architectures struggle to capture diverse task dynamics, resulting in poor reconstruction and prediction accuracy. We introduce Mixture-of-World Models (MoW), a scalab...

</details>

---
