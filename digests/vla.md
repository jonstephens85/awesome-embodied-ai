# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-13 16:55 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824v1)

**Authors:** Zhijie Wu, Kento Kawaharazuka, Kei Okada

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10824v1) | [PDF](https://arxiv.org/pdf/2608.10824v1.pdf) | [Project Page](https://zjw4321.github.io/neural-introspection-gating-page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action(VLA) models map camera images and language instructions directly to motor commands through a single autoregressive transformer. In real-time control, they still spend substantial compute recomputing key-value(KV) representations for visual tokens that barely change across neighboring frames. Recent work such as VLA-Cache reduces that cost by reusing KV states for visually static patches, but its policy relies only on observation-space heuristics and does not account for th...

</details>

---

### [DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving](https://arxiv.org/abs/2608.10413v1)

**Authors:** Zebin Xing, Yupeng Zheng, Qiang Chen, Linbo Wang, Yichen Zhang et al. (13 authors)

**Published:** 2026-08-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10413v1) | [PDF](https://arxiv.org/pdf/2608.10413v1.pdf) | [GitHub](https://github.com/ZebinX/DriveVLA-M0)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for end-to-end autonomous driving by enabling unified reasoning across perception, language, and planning. However, existing approaches lack mechanisms to exploit past failures or adapt to distribution shifts, causing the model to persistently underperform on similar scenarios where it has previously failed. In this paper, we propose DriveVLA-M0, a retrieval-augmented VLA with failure-aware latent memory. We constr...

</details>

---

## Other Recent Papers

### [DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.12308v1)

**Authors:** Yan Deng, Fei Xu

**Published:** 2026-08-12 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.12308v1) | [PDF](https://arxiv.org/pdf/2608.12308v1.pdf)

<details>
<summary>Abstract</summary>

Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-b...

</details>

---

### [Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation: Diagnosing and Mitigating Initial-Pose Dependence](https://arxiv.org/abs/2608.11769v1)

**Authors:** Chaeyeon Jung, Juyoun Park

**Published:** 2026-08-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11769v1) | [PDF](https://arxiv.org/pdf/2608.11769v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are expected to operate robustly across variations in the robot's initial configuration, yet aggregate task success can conceal pose-specific failures and inappropriate hand selection. This work investigates initial-pose dependence in VLA-based humanoid dual-arm manipulation. We characterize the initial-condition-dependent early hand preference as a policy-induced hand prior and quantify it using HandPriorScore, residual hand bias, and target responsiveness....

</details>

---

### [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739v1)

**Authors:** Yicheng Liu, Zibin Dong, Baijun Ye, Tianyuan Yuan, Tao Jiang et al. (27 authors)

**Published:** 2026-08-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.11739v1) | [PDF](https://arxiv.org/pdf/2608.11739v1.pdf)

<details>
<summary>Abstract</summary>

The prevailing recipe for Vision-Language-Action (VLA) models couples a pretrained VLM with a separately trained flow-matching action expert. This makes the VLM a context encoder rather than a decision-maker. We introduce G0.5, a pretrained autoregressive VLA in which a single transformer decoder emits reasoning and action tokens under a single objective. Three components make this tractable at foundation-model scale: a learnable cross-embodiment action tokenizer that maps heterogeneous robot ac...

</details>

---

### [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671v1)

**Authors:** Siyu Xu, Yunke Wang, Zijian Wang, Dihao Zhu, Chenghao Xia et al. (9 authors)

**Published:** 2026-08-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11671v1) | [PDF](https://arxiv.org/pdf/2608.11671v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can follow instructions and manipulate objects, but their performance often collapses out of distribution (OOD), when the scene, viewpoint, or object differs from training. Adapting to each new situation typically requires collecting more data and fine-tuning. We present StellaVLA, a framework that instead adapts at test time by conditioning on a single retrieved demonstration. The key idea is to move beyond imitating what an expert did and instead convey why:...

</details>

---

### [Adaptation of Generalist Robot Policies with Minimal Data](https://arxiv.org/abs/2608.11363v1)

**Authors:** Shreyas Kowshik, Sreyas Venkataraman, Leo Wang, Niharika Pant, Max Simchowitz et al. (6 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.11363v1) | [PDF](https://arxiv.org/pdf/2608.11363v1.pdf)

<details>
<summary>Abstract</summary>

A central goal in robot learning is to move beyond task-specific human data collection toward robots that improve through autonomous interaction. Yet fully autonomous learning remains difficult with current policies: sparse rewards and weak zero-shot exploration make it unlikely that a robot will discover successful behavior from scratch. We study minimal-data adaptation, a regime in which a pre-trained robot policy must learn a new task from as little as one demonstration followed by autonomous...

</details>

---

### [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](https://arxiv.org/abs/2608.10976v1)

**Authors:**  Foundation Model Team, XPeng Inc

**Published:** 2026-08-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.10976v1) | [PDF](https://arxiv.org/pdf/2608.10976v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can connect scene understanding, semantic reasoning, and trajectory generation for autonomous driving. However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optimize as an action-facing representation. We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision. ...

</details>

---

### [Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)

**Authors:** Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10756v1) | [PDF](https://arxiv.org/pdf/2608.10756v1.pdf)

<details>
<summary>Abstract</summary>

Embodied mobile manipulation requires language, visual observations, three-dimensional scene structure, and action feasibility to be aligned before execution. We study open-vocabulary target grounding with few-shot manipulation in local household workspaces and present an embodied multimodal grounding framework that integrates active multi-view Semantic 3D Gaussian Splatting (Semantic-3DGS), reachability-aware base positioning, and a diffusion-based vision-language-action policy. A task-driven l...

</details>

---

### [TCAM for Autonomous Deformable Manipulation: The RMC2 Champion System for WBCD 2026 Track 4](https://arxiv.org/abs/2608.10718v1)

**Authors:** Guangrui Shen, Zhili He, Shigang Wang, Yuanjun Sun, Qing Yu

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10718v1) | [PDF](https://arxiv.org/pdf/2608.10718v1.pdf)

<details>
<summary>Abstract</summary>

This technical report describes the RMC2 Team's champion solution for the WBCD 2026 Track 4: Deformable Manipulation Challenge. The task requires a robot to pick a single T-shirt from a stack, load it onto a printing pallet, align the collar with a target area, and smooth the printing region, a sequence that involves single-layer separation, deformable transport, precise placement, and contact-rich surface adjustment. The competition strongly incentivizes fully autonomous execution, motivating t...

</details>

---

### [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484v1)

**Authors:** Li Wenjie, Yash Jangir, Ignacy Stepka, Yash Agarwal, Marion Kipsang et al. (6 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2608.10484v1) | [PDF](https://arxiv.org/pdf/2608.10484v1.pdf)

<details>
<summary>Abstract</summary>

Action verbs describe not only the physical outcomes of actions, but also how those actions are performed. Yet action representations in vision-language-action models (VLAs) are typically optimized for reconstruction under L1/L2 losses in raw action space, where numerical proximity need not reflect linguistically meaningful distinctions. On BridgeV2, we show that action trajectories contain verb-grounding information beyond visual state changes, and that reconstruction-only discrete tokenization...

</details>

---

### [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393v1)

**Authors:** Jiahui Han, Yuhui Yao, Xin Wang, Jiafei Cao, Mingxuan Zhang et al. (9 authors)

**Published:** 2026-08-11 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10393v1) | [PDF](https://arxiv.org/pdf/2608.10393v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on pixel-space perturbations or white-box access, resulting in noticeable artifacts and limited deployability in real-world robotic systems. In this work, we propose DURA, a diffusion-based unrestricted ...

</details>

---
