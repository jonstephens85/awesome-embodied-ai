# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-05 22:21 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](https://arxiv.org/abs/2603.03818v1)

**Authors:** Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu

**Published:** 2026-03-04 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03818v1) | [PDF](https://arxiv.org/pdf/2603.03818v1.pdf) | [Project Page](https://ut-austin-rpl.github.io/continual-vla)

<details>
<summary>Abstract</summary>

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we found that pretrained VLAs are remarkably resistant to f...

</details>

---

### [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596v1)

**Authors:** Marcel Torne, Karl Pertsch, Homer Walke, Kyle Vedder, Suraj Nair et al. (17 authors)

**Published:** 2026-03-04 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.03596v1) | [PDF](https://arxiv.org/pdf/2603.03596v1.pdf) | [Project Page](https://pi.website/research/memory)

<details>
<summary>Abstract</summary>

Conventionally, memory in end-to-end robotic learning involves inputting a sequence of past observations into the learned policy. However, in complex multi-stage real-world tasks, the robot's memory must represent past events at multiple levels of granularity: from long-term memory that captures abstracted semantic concepts (e.g., a robot cooking dinner should remember which stages of the recipe are already done) to short-term memory that captures recent events and compensates for occlusions (e....

</details>

---

### [Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195v1)

**Authors:** Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan et al. (9 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03195v1) | [PDF](https://arxiv.org/pdf/2603.03195v1.pdf) | [Project Page](https://fx-hit.github.io/cowvla-io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are a promising path toward embodied intelligence, yet they often overlook the predictive and temporal-causal structure underlying visual dynamics. World-model VLAs address this by predicting future frames, but waste capacity reconstructing redundant backgrounds. Latent-action VLAs encode frame-to-frame transitions compactly, but lack temporally continuous dynamic modeling and world knowledge. To overcome these limitations, we introduce CoWVLA (Chain-of-World ...

</details>

---

### [Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283v1)

**Authors:** Yujia Zhang, Xiaoyang Wu, Yunhan Yang, Xianzhe Fan, Han Li et al. (9 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.03283v1) | [PDF](https://arxiv.org/pdf/2603.03283v1.pdf) | [Project Page](https://pointcept.github.io/Utonia)

<details>
<summary>Abstract</summary>

We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across diverse domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent repres...

</details>

---

## Other Recent Papers

### [SkillVLA: Tackling Combinatorial Diversity in Dual-Arm Manipulation via Skill Reuse](https://arxiv.org/abs/2603.03836v1)

**Authors:** Xuanran Zhai, Zekai Huang, Longyan Wu, Qianyou Zhao, Qiaojun Yu et al. (8 authors)

**Published:** 2026-03-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03836v1) | [PDF](https://arxiv.org/pdf/2603.03836v1.pdf)

<details>
<summary>Abstract</summary>

Recent progress in vision-language-action (VLA) models has demonstrated strong potential for dual-arm manipulation, enabling complex behaviors and generalization to unseen environments. However, mainstream bimanual VLA formulations largely overlook the critical challenge of combinatorial diversity. Different pairings of single-arm behaviors can induce qualitatively distinct task behaviors, yet existing models do not explicitly account for this structure. We argue that effective bimanual VLAs sho...

</details>

---

### [Cognition to Control - Multi-Agent Learning for Human-Humanoid Collaborative Transport](https://arxiv.org/abs/2603.03768v1)

**Authors:** Hao Zhang, Ding Zhao, H. Eric Tseng

**Published:** 2026-03-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.03768v1) | [PDF](https://arxiv.org/pdf/2603.03768v1.pdf)

<details>
<summary>Abstract</summary>

Effective human-robot collaboration (HRC) requires translating high-level intent into contact-stable whole-body motion while continuously adapting to a human partner. Many vision-language-action (VLA) systems learn end-to-end mappings from observations and instructions to actions, but they often emphasize reactive (System 1-like) behavior and leave under-specified how sustained System 2-style deliberation can be integrated with reliable, low-latency continuous control. This gap is acute in multi...

</details>

---

### [PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation](https://arxiv.org/abs/2603.03739v1)

**Authors:** Zehua Fan, Wenqi Lyu, Wenxuan Song, Linge Zhao, Yifei Yang et al. (15 authors)

**Published:** 2026-03-04 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.03739v1) | [PDF](https://arxiv.org/pdf/2603.03739v1.pdf)

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) have advanced zero-shot end-to-end Vision-Language Navigation (VLN), yet robust navigation requires not only semantic understanding but also predictive modeling of environment dynamics and spatial structure. We propose PROSPECT, a unified streaming navigation agent that couples a streaming Vision-Language-Action (VLA) policy with latent predictive representation learning. PROSPECT uses CUT3R as a streaming 3D foundation spatial encoder to produce long-con...

</details>

---

### [LiteVLA-Edge: Quantized On-Device Multimodal Control for Embedded Robotics](https://arxiv.org/abs/2603.03380v1)

**Authors:** Justin Williams, Kishor Datta Gupta, Roy George, Mrinmoy Sarkar

**Published:** 2026-03-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.03380v1) | [PDF](https://arxiv.org/pdf/2603.03380v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a unified framework for perception, language conditioning, and action generation, but many existing systems remain difficult to deploy in embedded robotic settings because of their computational requirements and inference latency. In this paper, we present LiteVLA-Edge, a deployment-oriented VLA pipeline for fully on-device inference on Jetson Orin-class hardware. Our approach combines supervised image-to-action fine-tuning in FP32 with post-training 4...

</details>

---
