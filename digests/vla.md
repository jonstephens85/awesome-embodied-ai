# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-24 22:52 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation](https://arxiv.org/abs/2607.21588v1)

**Authors:** Mengfei Zhao, Dihong Huang, Yikai Tang, Peihao Li, Mingxuan Yan et al. (15 authors)

**Published:** 2026-07-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.21588v1) | [PDF](https://arxiv.org/pdf/2607.21588v1.pdf) | [Project Page](https://axisaiorg.github.io/AXIS-V1/)

<details>
<summary>Abstract</summary>

Learning effective robot manipulation policies requires diverse, high-quality demonstrations, yet existing data pipelines are often difficult to scale because they rely on specialized hardware, centralized operators, or fixed task suites. We present AXIS, a growable community-driven data engine and benchmark for scalable robot learning, which enables browser-based teleoperation for large-scale demonstration collection, automatically generates and validates new manipulation tasks, and transforms ...

</details>

---

### [ReferTrack: Referring Then Tracking for Embodied Visual Tracking](https://arxiv.org/abs/2607.20061v1)

**Authors:** Hanjing Ye, Tianle Zeng, Jiazhao Zhang, Shaoan Wang, Zibo Zhang et al. (9 authors)

**Published:** 2026-07-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.20061v1) | [PDF](https://arxiv.org/pdf/2607.20061v1.pdf) | [GitHub](https://github.com/MedlarTea/referTrack)

<details>
<summary>Abstract</summary>

Embodied visual tracking (EVT) requires a mobile agent to continuously follow a specific target described in natural language using only onboard vision. While recent vision-language-action (VLA) policies unify target identification and trajectory planning, their chain-of-thought (CoT) reasoning often operates in abstract spatial latents that are difficult to supervise and weakly aligned with explicit image-space detections. To address this, we introduce ReferTrack, a referring-then-tracking para...

</details>

---

### [LENS: LLM-guided Environment Simplification for Planning and Control in Clutter](https://arxiv.org/abs/2607.19633v1)

**Authors:** Aileen Liao, Rachel Holladay, Dinesh Jayaraman, Michael Posa

**Published:** 2026-07-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.19633v1) | [PDF](https://arxiv.org/pdf/2607.19633v1.pdf) | [Project Page](https://lens-2026.github.io/)

<details>
<summary>Abstract</summary>

Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging to handle for today's prevalent approaches. The problem scales in complexity due to more objects and collisions, more unpredictable contact physics, distractors, and task ambiguity. Bridging this gap to real-world deployment requires effective scene abstractions; yet today, producing such abstractions requires extensive task-specific manual engineering, which does not scale. These...

</details>

---

## Other Recent Papers

### [HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](https://arxiv.org/abs/2607.20988v1)

**Authors:** Quanfu Yu, Xian Wu, Hao Xu, Liulong Ma

**Published:** 2026-07-23 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.20988v1) | [PDF](https://arxiv.org/pdf/2607.20988v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models augmented with world modeling represent a promising paradigm for end-to-end autonomous driving. While pixel-level future prediction enables fine-grained spatiotemporal reasoning, it compromises robustness in noisy driving scenarios. Conversely, latent-based world models alleviate this sensitivity but often incur limited interpretability and representational degradation due to absent pixel-level grounding. To reconcile this trade-off, we propose HyWorldVLA, a h...

</details>

---

### [Emergent Compositional Skills in Mixture-of-Experts VLAs](https://arxiv.org/abs/2607.20771v1)

**Authors:** Shlok Shah, Rhiaan Jhaveri, Tharun Kumar Tiruppali Kalidoss, Chirayu Nimonkar, Ishaan Javali

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.20771v1) | [PDF](https://arxiv.org/pdf/2607.20771v1.pdf)

<details>
<summary>Abstract</summary>

We consider the problem of learning compositional robot policies end-to-end from expert demonstrations, without any pre-specified notion of task decomposition or hierarchy. We ask whether a VLA trained with a simplified Mixture-of-Experts (MoE) action head can emergently learn to decompose tasks into reusable, interpretable primitives. We find that learned experts are heavily reused across tasks and consistently correspond to qualitatively distinct low-level behaviors, suggesting that the router...

</details>

---

### [Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids](https://arxiv.org/abs/2607.20345v1)

**Authors:** Roger Sala Sisó, Tiago Silvério, Jakob Sand, Tran Nguyen Le

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.20345v1) | [PDF](https://arxiv.org/pdf/2607.20345v1.pdf)

<details>
<summary>Abstract</summary>

Closing the gap between benchmark performance and reliable real-world operation remains a central challenge for Vision-Language-Action (VLA) humanoid robots, which must handle execution errors, distribution shifts, and environmental variability. This paper presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems-level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu humanoid robot and the GR00T N1.6 foundation model. DEED comprises thr...

</details>

---

### [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/abs/2607.19695v1)

**Authors:** Junzhe Wu, Yue Hu, Zeyu Han, Po-Hsun Chang, Yinan Dong et al. (7 authors)

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.19695v1) | [PDF](https://arxiv.org/pdf/2607.19695v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in delivery, campus, and emergency-response settings often need to navigate from buildings to streets within a single continuous episode. Existing benchmarks usually evaluate indoor and outdoor navigation separately, and many abstract away robot execution, leaving exit finding, boundary traversal, adaptation, and kinodynamic failures underexplored. We introduce NavVerse, a physics-enabled benchmark for indoor-to-outdoor embodied navigation. NavVerse contains 100 indoor scenes, 50...

</details>

---
