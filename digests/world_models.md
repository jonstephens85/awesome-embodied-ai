# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-30 17:20 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning](https://arxiv.org/abs/2604.26934v1)

**Authors:** Wanyue Zhang, Wenxiang Wu, Wang Xu, Jiaxin Luo, Helu Zhi et al. (9 authors)

**Published:** 2026-04-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.26934v1) | [PDF](https://arxiv.org/pdf/2604.26934v1.pdf) | [GitHub](https://github.com/WanyueZhang-ai/World2VLM)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial compu...

</details>

---

### [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)

**Authors:** Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun et al. (10 authors)

**Published:** 2026-04-29 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.26694v1) | [PDF](https://arxiv.org/pdf/2604.26694v1.pdf) | [Project Page](https://sharinka0715.github.io/X-WAM/)

<details>
<summary>Abstract</summary>

We propose X-WAM, a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing the critical limitations of prior unified world models (e.g., UWM) that only model 2D pixel-space and fail to balance action efficiency and world modeling quality. To leverage the strong visual priors of pretrained video diffusion models, X-WAM imagines the future world by predicting multi-view RGB-D videos, ...

</details>

---

## Other Recent Papers

### [STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation](https://arxiv.org/abs/2604.26848v1)

**Authors:** Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu et al. (8 authors)

**Published:** 2026-04-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.26848v1) | [PDF](https://arxiv.org/pdf/2604.26848v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation critically requires reasoning about future spatial-temporal interactions, yet existing VLA policies and world-model-enhanced policies do not fully model action-relevant spatial-temporal interaction structure. We propose STARRY, a world-model-enhanced action-generation policy that aligns spatial-temporal prediction with action generation. STARRY jointly denoises future spatial-temporal latents and action sequences, and introduces Geometry-Aware Selective Attention Modulation ...

</details>

---

### [AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents](https://arxiv.org/abs/2604.26522v1)

**Authors:** Mahnoor Shahid, Hannes Rothe

**Published:** 2026-04-29 | **Categories:** cs.AI, cs.LG, cs.LO

**Links:** [arXiv](https://arxiv.org/abs/2604.26522v1) | [PDF](https://arxiv.org/pdf/2604.26522v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based agents exhibit systemic failures in compositional generalization, limiting their robustness in interactive environments. This work introduces AGEL-Comp, a neuro-symbolic AI agent architecture designed to address this challenge by grounding actions of the agent. AGEL-Comp integrates three core innovations: (1) a dynamic Causal Program Graph (CPG) as a world model, representing procedural and causal knowledge as a directed hypergraph; (2) an Inductive Logic Program...

</details>

---

### [DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)

**Authors:** Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu et al. (12 authors)

**Published:** 2026-04-29 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.26232v1) | [PDF](https://arxiv.org/pdf/2604.26232v1.pdf)

<details>
<summary>Abstract</summary>

Controllable medical video generation has achieved remarkable progress, but it still lacks interpretability, which requires the alignment of generated contents with physical priors and faithful clinical manifestations. To push the boundaries from mere controllability to interpretability, we propose DepthPilot, the first interpretable framework for colonoscopy video generation. This work takes a step toward trustworthy generation through two synergistic paradigms. To achieve explicit geometric gr...

</details>

---

### [Lifting Embodied World Models for Planning and Control](https://arxiv.org/abs/2604.26182v1)

**Authors:** Alex N. Wang, Trevor Darrell, Pavel Izmailov, Yutong Bai, Amir Bar

**Published:** 2026-04-28 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.26182v1) | [PDF](https://arxiv.org/pdf/2604.26182v1.pdf)

<details>
<summary>Abstract</summary>

World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. To address this issue, we train a lightweight policy that maps high-le...

</details>

---

### [ProDrive: Proactive Planning for Autonomous Driving via Ego-Environment Co-Evolution](https://arxiv.org/abs/2604.25329v1)

**Authors:** Chuyao Fu, Shengzhe Gan, Zhuoli Ouyang, Yuhan Rui, Xiaowei Chi et al. (8 authors)

**Published:** 2026-04-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.25329v1) | [PDF](https://arxiv.org/pdf/2604.25329v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving planners typically generate trajectories from current observations alone. However, real-world driving is highly dynamic, and such reactive planning cannot anticipate future scene evolution, often leading to myopic decisions and safety-critical failures. We propose ProDrive, a world-model-based proactive planning framework that enables ego-environment co-evolution for autonomous driving. ProDrive jointly trains a query-centric trajectory planner and a bird's-eye-view...

</details>

---
