# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-25 16:36 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models](https://arxiv.org/abs/2608.23478v1)

**Authors:** Sangoh Lee, Sangwoo Mo, Wook-Shin Han

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23478v1) | [PDF](https://arxiv.org/pdf/2608.23478v1.pdf) | [Project Page](https://leesangoh.github.io/indi-project-page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can turn multimodal context into robot actions, but their action decoders are still trained largely by behavior cloning. This supervises which motor command was demonstrated while leaving implicit the local objective served by the behavior under the instruction. Future-based supervision enriches action learning with frames, latent observations, trajectories, or motion representations, but these signals capture particular realizations of what may happen rather ...

</details>

---

### [InstructMove: A Text-Indispensable Benchmark for Instruction-Following Manipulation](https://arxiv.org/abs/2608.22990v1)

**Authors:** Mengao Zhao, Ziang Li, Chaodong Huang, Mengchen Ma, Haoyi Jiang et al. (18 authors)

**Published:** 2026-08-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.22990v1) | [PDF](https://arxiv.org/pdf/2608.22990v1.pdf) | [GitHub](https://github.com/HorizonRobotics/RoboOrchardSim)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have made general-purpose robot manipulation increasingly plausible by conditioning robot actions on natural-language instructions. A key test of such generality is whether policies actually follow language instructions. Yet many manipulation benchmarks leave this ability underdetermined: the intended object or destination is often visually salient or uniquely feasible, allowing policies to succeed without grounding the instruction. We argue that instruction-f...

</details>

---

### [UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models](https://arxiv.org/abs/2608.22869v1)

**Authors:** Lars Osterberg, Maggie Wang, Mac Schwager

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.22869v1) | [PDF](https://arxiv.org/pdf/2608.22869v1.pdf) | [Project Page](https://losterberg3.github.io/unimem-vla/)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have leveraged internet-scale pretraining and task-focused finetuning to achieve strong performance on long-horizon tasks, they often struggle with non-Markovian tasks that require memory. Existing approaches to memory typically involve additional Vision-Language-Models (VLMs) for long-term memory management, introducing a memory bottleneck and a fractured training pipeline. Conditioning on multiple historical frames can provide the VLA with access to mo...

</details>

---

## Other Recent Papers

### [ROS2SmolVLA: Enabling Small Vision-Language-Action Models for Integration into Industrial-Grade Lightweight Robots](https://arxiv.org/abs/2608.23320v1)

**Authors:** Nils Mandischer, Noah Böckmann, Ludwig Holl, Lars Mikelsons

**Published:** 2026-08-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.23320v1) | [PDF](https://arxiv.org/pdf/2608.23320v1.pdf)

<details>
<summary>Abstract</summary>

Industrial demand changes the paradigms of production. Due to smaller batch sizes and more variations in products, companies face a growing challenge to adopt more adaptive production systems. In particular, robot-based automation is usually static and fails to respond to constantly changing processes. Vision-Language-Action (VLA) Models are a promising opportunity to mitigate this challenge by generating robot actions based on the observed system state. However, current research either focuses ...

</details>

---

### [Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23224v1)

**Authors:** Zhiruo Zhou, Zelin Li, Xiwen Chen, Jiazhuo Li, Chenwei Wang et al. (7 authors)

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23224v1) | [PDF](https://arxiv.org/pdf/2608.23224v1.pdf)

<details>
<summary>Abstract</summary>

Retrieval can efficiently and effectively augment a frozen vision--language--action (VLA) policy without retraining, yet retrieved text becomes a control intervention once it enters the executed prompt. In a matched audit, raw appended text reduces mean success from 92.47\% to 3.00\%, while meaningful and length-matched meaningless appends both fail on all 500 states. This result identifies \emph{prompt-form collapse}: changing the instruction form, rather than adding useful semantics, can domin...

</details>

---

### [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23138v1)

**Authors:** Xiwen Chen, Zelin Li, Zhiruo Zhou, Huiming Chen, Chenwei Wang et al. (6 authors)

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.23138v1) | [PDF](https://arxiv.org/pdf/2608.23138v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models often expose spatial grounding through autoregressive text coordinates or opaque action tokens, creating brittle interfaces between multimodal reasoning and robot execution. We present Pointing-VLA, a typed hidden-state spatial readout built on Embodied-R1. Geometry-specific heads predict normalized points, object-functional grounding (OFG) heatmaps, and visual trajectories without serializing geometry as text. For the evaluated Bridge/WidowX and physical pick...

</details>

---

### [Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation](https://arxiv.org/abs/2608.22800v1)

**Authors:** Jianxiang Liu, Gaojing Zhang, Chuan Wen, Qipeng Liu, Yuxuan Zhao et al. (7 authors)

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.22800v1) | [PDF](https://arxiv.org/pdf/2608.22800v1.pdf)

<details>
<summary>Abstract</summary>

Ensuring reliability in uncertain environments remains difficult for long-horizon robotic manipulation. End-to-end VLA models are data-heavy and opaque, making diagnosis and verification difficult. Hierarchical pipelines are more interpretable, but their plans are often weakly grounded in observations, weakly aligned with low-level actions, and computed without online feedback, leading to open-loop behavior and hallucinations. To address these issues, we introduce the Triplet-to-Track System (TT...

</details>

---

### [Robust Bimanual Vision-Language-Action Models via Embarrassingly Simple Modality Masking](https://arxiv.org/abs/2608.22419v1)

**Authors:** Dongzhou Cheng, Ziang Li, Yixiao Zhou, Haojuan Li, Jinghao Zhang et al. (9 authors)

**Published:** 2026-08-23 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.22419v1) | [PDF](https://arxiv.org/pdf/2608.22419v1.pdf)

<details>
<summary>Abstract</summary>

Query-based Vision-Language-Action (VLA) models offer low-latency inference that is attractive for bimanual robotic manipulation, but we observe that they can still exhibit discontinuous actions and execution failures in complex dual-arm tasks. We hypothesize that unstable multi-view and language fusion is one contributing factor in these failures, often coinciding with attention spreading to distracting regions. To improve robustness, we introduce the Modality Masking Mechanism (M3), an embarra...

</details>

---
