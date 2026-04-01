# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-01 22:27 UTC

**Papers found:** 8

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

### [CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics](https://arxiv.org/abs/2603.29409v1)

**Authors:** Andrew Jeong, Jaemin Kim, Sebin Lee, Sung-Eui Yoon

**Published:** 2026-03-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.29409v1) | [PDF](https://arxiv.org/pdf/2603.29409v1.pdf) | [Project Page](https://andrewwwj.github.io/clad)

<details>
<summary>Abstract</summary>

Robotic manipulation involves kinematic and semantic transitions that are inherently coupled via underlying actions. However, existing approaches plan within either semantic or latent space without explicitly aligning these cross-modal transitions. To address this, we propose CLaD, a framework that models how proprioceptive and semantic states jointly evolve under actions through asymmetric cross-attention that allows kinematic transitions to query semantic ones. CLaD predicts grounded latent fo...

</details>

---

### [LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301v1)

**Authors:** Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, Dahuin Jung

**Published:** 2026-03-30 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.28301v1) | [PDF](https://arxiv.org/pdf/2603.28301v1.pdf) | [GitHub](https://github.com/cau-hai-lab/LIBERO-Para)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong performance in robotic manipulation by leveraging pre-trained vision-language backbones. However, in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. To study this gap, we introduce LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-...

</details>

---

### [CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence](https://arxiv.org/abs/2603.28032v1)

**Authors:** Tianle Zeng, Hanxuan Chen, Yanci Wen, Hong Zhang

**Published:** 2026-03-30 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.28032v1) | [PDF](https://arxiv.org/pdf/2603.28032v1.pdf) | [GitHub](https://github.com/louiszengCN/CarlaAir)

<details>
<summary>Abstract</summary>

The convergence of low-altitude economies, embodied intelligence, and air-ground cooperative systems creates growing demand for simulation infrastructure capable of jointly modeling aerial and ground agents within a single physically coherent environment. Existing open-source platforms remain domain-segregated: driving simulators lack aerial dynamics, while multirotor simulators lack realistic ground scenes. Bridge-based co-simulation introduces synchronization overhead and cannot guarantee stri...

</details>

---

## Other Recent Papers

### [FocusVLA: Focused Visual Utilization for Vision-Language-Action Models](https://arxiv.org/abs/2603.28740v1)

**Authors:** Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan

**Published:** 2026-03-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.28740v1) | [PDF](https://arxiv.org/pdf/2603.28740v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models improve action generation by conditioning policies on rich vision-language information. However, current auto-regressive policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise - together severely impairing the quality of action. In thi...

</details>

---

### [StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation](https://arxiv.org/abs/2603.28565v1)

**Authors:** Yiran Shi, Dongqi Guo, Tianchen Zhao, Feng Gao, Liangzhi Shi et al. (11 authors)

**Published:** 2026-03-30 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.28565v1) | [PDF](https://arxiv.org/pdf/2603.28565v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have demonstrated exceptional performance in natural language-driven perception and control. However, the high computational cost of VLA models poses significant efficiency challenges, particularly for resource-constrained edge platforms in real-world deployments. However, since different stages of VLA (observation, action generation and execution) must proceed sequentially, and wait for the completion of the preceding stage, the system suffers from frequent h...

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

### [Learning Multi-View Spatial Reasoning from Cross-View Relations](https://arxiv.org/abs/2603.27967v1)

**Authors:** Suchae Jeong, Jaehwi Song, Haeone Lee, Hanna Kim, Jian Kim et al. (12 authors)

**Published:** 2026-03-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.27967v1) | [PDF](https://arxiv.org/pdf/2603.27967v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have achieved impressive results on single-view vision tasks, but lack the multi-view spatial reasoning capabilities essential for embodied AI systems to understand 3D environments and manipulate objects across different viewpoints. In this work, we introduce Cross-View Relations (XVR), a large-scale dataset designed to teach VLMs spatial reasoning across multiple views. XVR comprises 100K vision-question-answer samples derived from 18K diverse 3D scenes and 70K rob...

</details>

---
