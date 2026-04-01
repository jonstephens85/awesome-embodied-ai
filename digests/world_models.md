# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-01 16:55 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA](https://arxiv.org/abs/2603.29844v1)

**Authors:** Yi Chen, Yuying Ge, Hui Zhou, Mingyu Ding, Yixiao Ge et al. (6 authors)

**Published:** 2026-03-31 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.29844v1) | [PDF](https://arxiv.org/pdf/2603.29844v1.pdf) | [Project Page](https://xpeng-robotics.github.io/dial)

<details>
<summary>Abstract</summary>

The development of Vision-Language-Action (VLA) models has been significantly accelerated by pre-trained Vision-Language Models (VLMs). However, most existing end-to-end VLAs treat the VLM primarily as a multimodal encoder, directly mapping vision-language features to low-level actions. This paradigm underutilizes the VLM's potential in high-level decision making and introduces training instability, frequently degrading its rich semantic representations. To address these limitations, we introduc...

</details>

---

### [HCLSM: Hierarchical Causal Latent State Machines for Object-Centric World Modeling](https://arxiv.org/abs/2603.29090v1)

**Authors:** Jaber Jaber, Osama Jaber

**Published:** 2026-03-31 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.29090v1) | [PDF](https://arxiv.org/pdf/2603.29090v1.pdf) | [GitHub](https://github.com/rightnow-ai/hclsm)

<details>
<summary>Abstract</summary>

World models that predict future states from video remain limited by flat latent representations that entangle objects, ignore causal structure, and collapse temporal dynamics into a single scale. We present HCLSM, a world model architecture that operates on three interconnected principles: object-centric decomposition via slot attention with spatial broadcast decoding, hierarchical temporal dynamics through a three-level engine combining selective state space models for continuous physics, spar...

</details>

---

### [Stepper: Stepwise Immersive Scene Generation with Multiview Panoramas](https://arxiv.org/abs/2603.28980v1)

**Authors:** Felix Wimbauer, Fabian Manhardt, Michael Oechsle, Nikolai Kalischek, Christian Rupprecht et al. (7 authors)

**Published:** 2026-03-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.28980v1) | [PDF](https://arxiv.org/pdf/2603.28980v1.pdf) | [Project Page](under)

<details>
<summary>Abstract</summary>

The synthesis of immersive 3D scenes from text is rapidly maturing, driven by novel video generative models and feed-forward 3D reconstruction, with vast potential in AR/VR and world modeling. While panoramic images have proven effective for scene initialization, existing approaches suffer from a trade-off between visual fidelity and explorability: autoregressive expansion suffers from context drift, while panoramic video generation is limited to low resolution. We present Stepper, a unified fra...

</details>

---

### [AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models](https://arxiv.org/abs/2603.28963v1)

**Authors:** Mozhgan Pourkeshavatz, Tianran Liu, Nicholas Rhinehart

**Published:** 2026-03-30 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.28963v1) | [PDF](https://arxiv.org/pdf/2603.28963v1.pdf) | [Project Page](contains)

<details>
<summary>Abstract</summary>

Multi-agent traffic simulation is central to developing and testing autonomous driving systems. Recent data-driven simulators have achieved promising results, but rely heavily on supervised learning from labeled trajectories or semantic annotations, making it costly to scale their performance. Meanwhile, large amounts of unlabeled sensor data can be collected at scale but remain largely unused by existing traffic simulation frameworks. This raises a key question: How can a method harness unlabel...

</details>

---

## Other Recent Papers

### [Enhancing Policy Learning with World-Action Model](https://arxiv.org/abs/2603.28955v1)

**Authors:** Yuci Han, Alper Yilmaz

**Published:** 2026-03-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.28955v1) | [PDF](https://arxiv.org/pdf/2603.28955v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents the World-Action Model (WAM), an action-regularized world model that jointly reasons over future visual observations and the actions that drive state transitions. Unlike conventional world models trained solely via image prediction, WAM incorporates an inverse dynamics objective into DreamerV2 that predicts actions from latent state transitions, encouraging the learned representations to capture action-relevant structure critical for downstream control. We evaluate WAM on enh...

</details>

---

### [OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models](https://arxiv.org/abs/2603.28887v1)

**Authors:** Tianran Liu, Shengwen Zhao, Mozhgan Pourkeshavarz, Weican Li, Nicholas Rhinehart

**Published:** 2026-03-30 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.28887v1) | [PDF](https://arxiv.org/pdf/2603.28887v1.pdf)

<details>
<summary>Abstract</summary>

Data-driven autonomous driving simulation has long been constrained by its heavy reliance on pre-recorded driving logs or spatial priors, such as HD maps. This fundamental dependency severely limits scalability, restricting open-ended generation capabilities to the finite scale of existing collected datasets. To break this bottleneck, we present OccSim, the first occupancy world model-driven 3D simulator. OccSim obviates the requirement for continuous logs or HD maps; conditioned only on a singl...

</details>

---

### [ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation](https://arxiv.org/abs/2603.28545v1)

**Authors:** Yu Sun, Meng Cao, Ping Yang, Rongtao Xu, Yunxiao Yan et al. (18 authors)

**Published:** 2026-03-30 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.28545v1) | [PDF](https://arxiv.org/pdf/2603.28545v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models and world models have recently emerged as promising paradigms for general-purpose robotic intelligence, yet their progress is hindered by the lack of reliable evaluation protocols that reflect real-world deployment. Existing benchmarks are largely simulator-centric, which provide controllability but fail to capture the reality gap caused by perception noise, complex contact dynamics, hardware constraints, and system latency. Moreover, fragmented real-world eva...

</details>

---
