# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-30 17:53 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model](https://arxiv.org/abs/2606.30292v1)

**Authors:** Daniyel Ayupov, Artur Markov-Tsoy

**Published:** 2026-06-29 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30292v1) | [PDF](https://arxiv.org/pdf/2606.30292v1.pdf) | [Project Page](https://trydreamforge.com/)

<details>
<summary>Abstract</summary>

We present DreamForge-World 0.1 Preview, a preview foundational world model for real-time interactive world simulation. The system adapts the LongLive 1 autoregressive video stack, itself derived from Wan2.1-T2V-1.3B, with a residual action pathway inspired by the Matrix-Game family. DreamForge-World 0.1 Preview focuses on a complementary axis to frontier-scale world simulators: low-compute adaptation, consumer-GPU runtime, and broad interactive capability coverage. It supports live keyboard and...

</details>

---

### [Cognitive World Models for Process-Level Social Influence Evaluation](https://arxiv.org/abs/2606.29495v1)

**Authors:** Minghui Ma, Bin Guo, Han Wang, Mengqi Chen, Jingqi Liu et al. (7 authors)

**Published:** 2026-06-28 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29495v1) | [PDF](https://arxiv.org/pdf/2606.29495v1.pdf) | [GitHub](https://github.com/lucianma05-create/CogWM})

<details>
<summary>Abstract</summary>

Social influence dialogue changes user behavior by altering internal cognitive states. The central evaluation question is whether the user's beliefs, desires, intentions, and emotions measurably change over the course of conversation, a process-oriented criterion that neither surface-level text metrics (BLEU/ROUGE) nor single-score LLM judgments can capture. We propose the \textbf{Cog}nitive \textbf{W}orld \textbf{M}odel \textbf{(CogWM)}, an LLM-based user model that reframes multi-turn dialogue...

</details>

---

### [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286v1)

**Authors:** Dingyi Yao, Xinqi Zhang, Lihui Peng, Jianming Hu, Danya Yao et al. (6 authors)

**Published:** 2026-06-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.29286v1) | [PDF](https://arxiv.org/pdf/2606.29286v1.pdf) | [GitHub](https://github.com/Dingyi-Yao/ASTAD)

<details>
<summary>Abstract</summary>

Synthetic data mitigates the data scarcity problem in autonomous driving perception. However, the synthetic-to-real gap leads to performance degradation, hindering real-world model generalization. Although current methods leverage diffusion models for photorealistic style transfer to bridge this gap, they critically ignore a practical asymmetry: while synthetic data possesses perfect pixel-level annotations, real-world style reference images generally lack corresponding labels. Consequently, exi...

</details>

---

## Other Recent Papers

### [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)

**Authors:** Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng

**Published:** 2026-06-29 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.30639v1) | [PDF](https://arxiv.org/pdf/2606.30639v1.pdf)

<details>
<summary>Abstract</summary>

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits...

</details>

---

### [OWMDrive: Causality-Aware End-to-End Autonomous Driving via 4D Occupancy World Model](https://arxiv.org/abs/2606.30421v1)

**Authors:** Junjie Cheng, Ruiqi Song, Ye Wu, Nanxing Zeng, Ximiao Li et al. (6 authors)

**Published:** 2026-06-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30421v1) | [PDF](https://arxiv.org/pdf/2606.30421v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving systems are steadily moving toward end-to-end paradigms to mitigate the limited adaptability of rule-based pipelines in complex traffic environments. However, most existing learning-based methods still make decisions from static representations of the current scene, without explicit future rollouts or modeling of the temporal causal dynamics in traffic interactions. This limitation often results in unstable or overly conservative planning under high-uncertainty conditions, suc...

</details>

---

### [Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation](https://arxiv.org/abs/2606.29908v1)

**Authors:** Hong Chen, Daqi Liu, Zehan Zhang, Haiguang Wang, Tianhao Lu et al. (13 authors)

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29908v1) | [PDF](https://arxiv.org/pdf/2606.29908v1.pdf)

<details>
<summary>Abstract</summary>

Existing world model-based planners for visual navigation typically follow a verification-centric paradigm, decoupling goal intent from trajectory synthesis. This approach suffers from candidate dependence, heavy computational overhead, and inconsistencies between sampled actions and predicted visuals. To address these issues, we propose SWAM (Spatial-perceiving World Action Model), a task-centric joint observation-action generation framework. Given start and goal RGB observations, SWAM performs...

</details>

---

### [LWDrive: Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879v1)

**Authors:** Chen Yang, Yuhao Wei, Ze Xu, Ziheng Zou, Shuang Liang et al. (9 authors)

**Published:** 2026-06-29 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29879v1) | [PDF](https://arxiv.org/pdf/2606.29879v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) provide powerful semantic understanding and commonsense reasoning for End-to-End Autonomous Driving (E2E-AD) planning. However, trajectories directly generated by VLMs often encode only coarse driving intentions and remain insufficient for geometrically accurate, future-aware, and multi-view-grounded planning. To address these limitations, we develop the Layer-Wise World-Model-Guided Driving framework (LWDrive). LWDrive is a VLM planning framework that refines coars...

</details>

---

### [The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models](https://arxiv.org/abs/2606.29799v1)

**Authors:** Rafael Kaufmann, Felix Neubürger, Michael Walters, Thomas Kopinski, Dimitrije Marković

**Published:** 2026-06-29 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29799v1) | [PDF](https://arxiv.org/pdf/2606.29799v1.pdf)

<details>
<summary>Abstract</summary>

This project introduces the CRISTAL Method (Coherent Reliable Intentional Synthesis of Truthful Analysis Logic), a neurosymbolic framework for automating complex analysis workflows, with fundamental investment analysis as a primary use case. This domain poses major challenges: high structural uncertainty, noisy and subjective data, tight attention budgets, and the need for justified, reproducible decisions. Human analysts often struggle in this domain due to cognitive biases and limitations, sug...

</details>

---

### [HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data](https://arxiv.org/abs/2606.29784v1)

**Authors:** Xinrui Ruan, Zhenyu Zhao, Waverly Wei, Yueshan Zhang, Zeyu Zheng et al. (7 authors)

**Published:** 2026-06-29 | **Categories:** stat.ME, cs.AI, econ.EM

**Links:** [arXiv](https://arxiv.org/abs/2606.29784v1) | [PDF](https://arxiv.org/pdf/2606.29784v1.pdf)

<details>
<summary>Abstract</summary>

Reliable generative AI models critically rely on expert human annotations to evaluate output quality, yet these "gold" labels are expensive to collect and limited in quantity. Organizations thus often turn to collecting vast but noisy "silver" labels from crowdsourced workers or vendor annotators as proxies for gold labels. Because gold remains the evaluation target, naively aggregating noisy silver labels may introduce bias, and estimators built on sparsely observed gold labels may have high va...

</details>

---

### [Learning Transferable Dynamics Priors from Action to World Modeling](https://arxiv.org/abs/2606.29501v1)

**Authors:** Ze Huang, Jiahui Zhang, Hairuo Liu, Chenxi Zhang, Ran Cheng et al. (6 authors)

**Published:** 2026-06-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.29501v1) | [PDF](https://arxiv.org/pdf/2606.29501v1.pdf)

<details>
<summary>Abstract</summary>

We study action-conditioned world modeling as a scalable way to learn transferable dynamics priors for robot learning. By pretraining a model to predict how actions drive visual scene evolution, the resulting world model captures reusable interaction dynamics beyond appearance-level video generation. Concretely, we pretrain a multi-view interactive base diffusion world model, A2World, on large-scale robot manipulation data with real action annotations. We validate the learned dynamics priors fro...

</details>

---

### [Prototype Latent World Model Replay for Class-Incremental Learning](https://arxiv.org/abs/2606.29465v1)

**Authors:** Weizhi Nie, Hui Wang, Weijie Wang, Yuting Su

**Published:** 2026-06-28 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.29465v1) | [PDF](https://arxiv.org/pdf/2606.29465v1.pdf)

<details>
<summary>Abstract</summary>

Class-incremental learning requires a model to learn new classes while preserving decision regions for old ones. This is difficult when raw old samples are no longer available. We propose Prototype Latent World Model Replay, a memory-free framework that stores old classes as distributions over stable hidden states rather than as images. A frozen ImageNet-pretrained encoder maps each image into a latent state space. In this space, each class is summarized by several prototype-centered distributio...

</details>

---

### [L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction](https://arxiv.org/abs/2606.29374v1)

**Authors:** Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He et al. (9 authors)

**Published:** 2026-06-28 | **Categories:** cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2606.29374v1) | [PDF](https://arxiv.org/pdf/2606.29374v1.pdf)

<details>
<summary>Abstract</summary>

High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense m...

</details>

---
