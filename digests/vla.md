# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-26 16:47 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control](https://arxiv.org/abs/2608.24115v1)

**Authors:** Suhwan Choi, Jaeyoon Jung, Sungkyung Kim, Yunsung Lee, Youngjae Yu

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.24115v1) | [PDF](https://arxiv.org/pdf/2608.24115v1.pdf) | [Project Page](https://worv-ai.github.io/ponderpounce/)

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) can integrate long visual histories, reason under partial observability, and infer behavior from a few examples. Yet vision-language-action (VLA) models generally inherit pretrained representations without using this contextual capacity as episode memory. Memory-dependent policies address this gap through purpose-built history mechanisms. PonderPounce instead reuses an MLLM's native causal context as robot memory. Ponder, a System2 MLLM, accumulates episo...

</details>

---

### [Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models](https://arxiv.org/abs/2608.24042v1)

**Authors:** Haoran Hao, Shahram Najam Syed, Jeff Schneider, Jeffrey Ichnowski

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.24042v1) | [PDF](https://arxiv.org/pdf/2608.24042v1.pdf) | [Project Page](https://hoar012.github.io/HSR-Project)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models pretrained on large-scale robot datasets provide a strong foundation for robot manipulation, their performance can degrade when adapted to new tasks with limited task-specific demonstrations. Retrieval offers a practical way to reuse existing demonstrations for data-efficient adaptation, but existing methods often rely on visual similarity, state-action representations, or task-level language matching. These approaches may overlook the hierarchical struc...

</details>

---

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

### [Gripper-aware Vision Language Action Models](https://arxiv.org/abs/2608.24603v1)

**Authors:** Hanyi Zhang, Zihong Luo, Tianyu Li, Khang Nguyen, Basu Hela et al. (19 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24603v1) | [PDF](https://arxiv.org/pdf/2608.24603v1.pdf)

<details>
<summary>Abstract</summary>

Vision language action models (VLAs) have advanced general purpose robotic grasping and manipulation by enabling robots to interpret visual observations and natural language instructions to generate executable action sequences. However, existing VLAs often implicitly assume gripper invariance, despite grasping strategies being inherently embodiment-dependent. Different gripper types, such as parallel-jaw and suction, usually require distinct interaction strategies to achieve the same grasping ob...

</details>

---

### [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](https://arxiv.org/abs/2608.24101v1)

**Authors:** Zhi Cao, Howard Ji, Kevin Zhang, Kuangzhi Ge, Li Fei-Fei et al. (7 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24101v1) | [PDF](https://arxiv.org/pdf/2608.24101v1.pdf)

<details>
<summary>Abstract</summary>

Robot actions are inherently embodiment-specific and only weakly aligned with image-space visual changes, limiting their effectiveness as conditioning signals for robot world models. In contrast, visual tracks provide an embodiment-agnostic representation of how task-relevant points move through a scene, offering dense image-space guidance for accurate and spatially precise future video prediction. Building on this observation, we propose TrAct, a world-model-based robot decision-making framewor...

</details>

---

### [Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency](https://arxiv.org/abs/2608.23831v1)

**Authors:** Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt et al. (20 authors)

**Published:** 2026-08-24 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.23831v1) | [PDF](https://arxiv.org/pdf/2608.23831v1.pdf)

<details>
<summary>Abstract</summary>

While reinforcement learning (RL) allows generalist robot policies to continually improve during deployment, the large model size of modern generalist policies, such as VLAs, poses a fundamental obstacle to effective RL improvement. In particular, their severe inference latency---which can lead to pauses or jerky movements---can alter the effective environment dynamics and, if not correctly accounted for, break the Markov assumption that RL relies on, causing standard RL algorithms to fail compl...

</details>

---

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
