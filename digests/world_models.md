# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-02-04 16:50 UTC

**Papers found:** 24

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)

**Authors:** Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu et al. (11 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03793v1) | [PDF](https://arxiv.org/pdf/2602.03793v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Embodied world models have emerged as a promising paradigm in robotics, most of which leverage large-scale Internet videos or pretrained video generation models to enrich visual and motion priors. However, they still face key challenges: a misalignment between coordinate-space actions and pixel-space videos, sensitivity to camera viewpoint, and non-unified architectures across embodiments. To this end, we present BridgeV2W, which converts coordinate-space actions into pixel-aligned embodiment ma...

</details>

---

### [A Lightweight Library for Energy-Based Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2602.03604v1)

**Authors:** Basile Terver, Randall Balestriero, Megi Dervishi, David Fan, Quentin Garrido et al. (11 authors)

**Published:** 2026-02-03 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.03604v1) | [PDF](https://arxiv.org/pdf/2602.03604v1.pdf) | [GitHub](https://github.com/facebookresearch/eb_jepa)

<details>
<summary>Abstract</summary>

We present EB-JEPA, an open-source library for learning representations and world models using Joint-Embedding Predictive Architectures (JEPAs). JEPAs learn to predict in representation space rather than pixel space, avoiding the pitfalls of generative modeling while capturing semantically meaningful features suitable for downstream tasks. Our library provides modular, self-contained implementations that illustrate how representation learning techniques developed for image-level self-supervised ...

</details>

---

### [InstaDrive: Instance-Aware Driving World Models for Realistic and Consistent Video Generation](https://arxiv.org/abs/2602.03242v1)

**Authors:** Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu et al. (6 authors)

**Published:** 2026-02-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03242v1) | [PDF](https://arxiv.org/pdf/2602.03242v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Autonomous driving relies on robust models trained on high-quality, large-scale multi-view driving videos. While world models offer a cost-effective solution for generating realistic driving videos, they struggle to maintain instance-level temporal consistency and spatial geometric fidelity. To address these challenges, we propose InstaDrive, a novel framework that enhances driving video realism through two key advancements: (1) Instance Flow Guider, which extracts and propagates instance featur...

</details>

---

### [ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask](https://arxiv.org/abs/2602.03213v1)

**Authors:** Zhuoran Yang, Yanyong Zhang

**Published:** 2026-02-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03213v1) | [PDF](https://arxiv.org/pdf/2602.03213v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Autonomous driving relies on robust models trained on large-scale, high-quality multi-view driving videos. Although world models provide a cost-effective solution for generating realistic driving data, they often suffer from identity drift, where the same object changes its appearance or category across frames due to the absence of instance-level temporal constraints. We introduce ConsisDrive, an identity-preserving driving world model designed to enforce temporal consistency at the instance lev...

</details>

---

### [World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454v1)

**Authors:** Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, Yunzhe Zhang, Jiarao Liu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02454v1) | [PDF](https://arxiv.org/pdf/2602.02454v1.pdf) | [Project Page](https://world-gymnast.github.io/)

<details>
<summary>Abstract</summary>

Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world...

</details>

---

### [Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory](https://arxiv.org/abs/2602.02393v2)

**Authors:** Ruiqi Wu, Xuanhua He, Meng Cheng, Tianyu Yang, Yong Zhang et al. (11 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02393v2) | [PDF](https://arxiv.org/pdf/2602.02393v2.pdf) | [Project Page](https://rq-wu.github.io/projects/infinite-world/index.html)

<details>
<summary>Abstract</summary>

We propose Infinite-World, a robust interactive world model capable of maintaining coherent visual memory over 1000+ frames in complex real-world environments. While existing world models can be efficiently optimized on synthetic data with perfect ground-truth, they lack an effective training paradigm for real-world videos due to noisy pose estimations and the scarcity of viewpoint revisits. To bridge this gap, we first introduce a Hierarchical Pose-free Memory Compressor (HPMC) that recursively...

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

### [DDP-WM: Disentangled Dynamics Prediction for Efficient World Models](https://arxiv.org/abs/2602.01780v2)

**Authors:** Shicheng Yin, Kaixuan Yin, Weixing Chen, Yang Liu, Guanbin Li et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01780v2) | [PDF](https://arxiv.org/pdf/2602.01780v2.pdf) | [GitHub](https://github.com/HCPLab-SYSU/DDP-WM)

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

### [LIVE: Long-horizon Interactive Video World Modeling](https://arxiv.org/abs/2602.03747v1)

**Authors:** Junchao Huang, Ziyang Ye, Xinting Hu, Tianyu He, Guiyu Zhang et al. (8 authors)

**Published:** 2026-02-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03747v1) | [PDF](https://arxiv.org/pdf/2602.03747v1.pdf)

<details>
<summary>Abstract</summary>

Autoregressive video world models predict future visual observations conditioned on actions. While effective over short horizons, these models often struggle with long-horizon generation, as small prediction errors accumulate over time. Prior methods alleviate this by introducing pre-trained teacher models and sequence-level distribution matching, which incur additional computational cost and fail to prevent error propagation beyond the training horizon. In this work, we propose LIVE, a Long-hor...

</details>

---

### [EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories](https://arxiv.org/abs/2602.03569v1)

**Authors:** Linjie Mu, Zhongzhen Huang, Yannian Gu, Shengqian Qin, Shaoting Zhang et al. (6 authors)

**Published:** 2026-02-03 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.03569v1) | [PDF](https://arxiv.org/pdf/2602.03569v1.pdf)

<details>
<summary>Abstract</summary>

World models offer a principled framework for simulating future states under interventions, but realizing such models in complex, high-stakes domains like medicine remains challenging. Recent large language models (LLMs) have achieved strong performance on static medical reasoning tasks, raising the question of whether they can function as dynamic medical world models capable of simulating disease progression and treatment outcomes over time. In this work, we show that LLMs only incorporating me...

</details>

---

### [A Minimal Task Reveals Emergent Path Integration and Object-Location Binding in a Predictive Sequence Model](https://arxiv.org/abs/2602.03490v1)

**Authors:** Linda Ariel Ventura, Victoria Bosch, Tim C Kietzmann, Sushrut Thorat

**Published:** 2026-02-03 | **Categories:** cs.LG, q-bio.NC

**Links:** [arXiv](https://arxiv.org/abs/2602.03490v1) | [PDF](https://arxiv.org/pdf/2602.03490v1.pdf)

<details>
<summary>Abstract</summary>

Adaptive cognition requires structured internal models representing objects and their relations. Predictive neural networks are often proposed to form such "world models", yet their underlying mechanisms remain unclear. One hypothesis is that action-conditioned sequential prediction suffices for learning such world models. In this work, we investigate this possibility in a minimal in-silico setting. Sequentially sampling tokens from 2D continuous token scenes, a recurrent neural network is train...

</details>

---

### [General Agents Contain World Models, even under Partial Observability and Stochasticity](https://arxiv.org/abs/2602.03146v1)

**Authors:** Santiago Cifuentes

**Published:** 2026-02-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.03146v1) | [PDF](https://arxiv.org/pdf/2602.03146v1.pdf)

<details>
<summary>Abstract</summary>

Deciding whether an agent possesses a model of its surrounding world is a fundamental step toward understanding its capabilities and limitations. In [10], it was shown that, within a particular framework, every almost optimal and general agent necessarily contains sufficient knowledge of its environment to allow an approximate reconstruction of it by querying the agent as a black box. This result relied on the assumptions that the agent is deterministic and that the environment is fully observab...

</details>

---

### [Latent Perspective-Taking via a Schrödinger Bridge in Influence-Augmented Local Models](https://arxiv.org/abs/2602.02857v1)

**Authors:** Kevin Alcedo, Pedro U. Lima, Rachid Alami

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.02857v1) | [PDF](https://arxiv.org/pdf/2602.02857v1.pdf)

<details>
<summary>Abstract</summary>

Operating in environments alongside humans requires robots to make decisions under uncertainty. In addition to exogenous dynamics, they must reason over others' hidden mental-models and mental-states. While Interactive POMDPs and Bayesian Theory of Mind formulations are principled, exact nested-belief inference is intractable, and hand-specified models are brittle in open-world settings. We address both by learning structured mental-models and an estimator of others' mental-states. Building on t...

</details>

---

### [Joint Learning of Hierarchical Neural Options and Abstract World Model](https://arxiv.org/abs/2602.02799v1)

**Authors:** Wasu Top Piriyakulkij, Wolfgang Lehrach, Kevin Ellis, Kevin Murphy

**Published:** 2026-02-02 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02799v1) | [PDF](https://arxiv.org/pdf/2602.02799v1.pdf)

<details>
<summary>Abstract</summary>

Building agents that can perform new skills by composing existing skills is a long-standing goal of AI agent research. Towards this end, we investigate how to efficiently acquire a sequence of skills, formalized as hierarchical neural options. However, existing model-free hierarchical reinforcement algorithms need a lot of data. We propose a novel method, which we call AgentOWL (Option and World model Learning Agent), that jointly learns -- in a sample efficient way -- an abstract world model (a...

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
