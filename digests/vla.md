# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-12 16:55 UTC

**Papers found:** 14

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

### [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771v1)

**Authors:** Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen et al. (10 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09771v1) | [PDF](https://arxiv.org/pdf/2608.09771v1.pdf) | [Project Page](https://kzz1031.github.io/slim-project-page/)

<details>
<summary>Abstract</summary>

Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step. Much of this capacity supports open-domain semantics, whereas continuous robot manipulation primarily requires compact representations of observations, actions, and the transitions induced by actions. Pixel-level world models provide another route, but predicting visual details irrelevant to control can be unnecessarily expensive. W...

</details>

---

### [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](https://arxiv.org/abs/2608.09381v1)

**Authors:** Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li et al. (9 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09381v1) | [PDF](https://arxiv.org/pdf/2608.09381v1.pdf) | [Project Page](https://spritewithoutice.github.io/JEPA_WAM/)

<details>
<summary>Abstract</summary>

Robust robot control benefits from explicitly modeling state transitions, but video-generation world action models (WAMs) introduce substantial deployment cost. Existing latent WAMs avoid explicit future generation, but often compress predictive representations or separate predictive modeling from the representations used for action generation. We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space, which couples latent transition prediction with continuous action generation thro...

</details>

---

## Other Recent Papers

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

### [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730v1)

**Authors:** Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo et al. (6 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.09730v1) | [PDF](https://arxiv.org/pdf/2608.09730v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation or a large video backbone in the control loop substantially increases inference cost. We introduce World Tokens, an embodied policy architec...

</details>

---

### [RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.09467v1)

**Authors:** Boxiong Wang, Hui Kang, Geng Sun, Jiahui Li, Chao Yu et al. (6 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.09467v1) | [PDF](https://arxiv.org/pdf/2608.09467v1.pdf)

<details>
<summary>Abstract</summary>

Unmanned aerial vehicle vision-language navigation (UAV-VLN) requires agents to translate visual observations and language instructions into reliable flight actions in complex environments. Although recent end-to-end UAV vision-language-action (UAV-VLA) policies reduce reliance on separately designed perception, planning, and control modules, their behavior-cloning objectives provide limited corrective supervision for interactive closed-loop execution. Reinforcement learning (RL) offers a promis...

</details>

---

### [VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction](https://arxiv.org/abs/2608.09448v1)

**Authors:** Hongjin Ji, Guoyang Xia, Luoyang Sun, Fangxiang Feng, Lei Ren

**Published:** 2026-08-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.09448v1) | [PDF](https://arxiv.org/pdf/2608.09448v1.pdf)

<details>
<summary>Abstract</summary>

Test-time training (TTT) offers a lightweight way to adapt vision--language--action (VLA) policies from unlabeled deployment streams, but it remains difficult to use reliably in closed-loop manipulation. A shared adaptation space can mix incompatible task corrections, while an online update can alter subsequent actions before its consequences are known. We introduce a reliable TTT framework for VLA policies (VANE). VANE conditions prompt adaptation on the current vision--language context and lea...

</details>

---

### [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](https://arxiv.org/abs/2608.09410v1)

**Authors:** Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09410v1) | [PDF](https://arxiv.org/pdf/2608.09410v1.pdf)

<details>
<summary>Abstract</summary>

Modern vision-language-action (VLA) policies have acquired broad manipulation skills, but typically generate each action chunk from the current observation or a short fixed-length history. However, real-world manipulation is often non-Markovian, requiring robots to retain and reason over task-relevant information from long-horizon interaction histories to determine the next action. To address this challenge, we propose HyMeS, a hybrid learning framework that leverages the reasoning and memory-ma...

</details>

---

### [Trajectory Divergence Horizon Decision for Reliable Dual-Arm Surgical Subtask Manipulation](https://arxiv.org/abs/2608.09125v1)

**Authors:** Mingwu Su, Guankun Wang, Jinsong Lin, Rulin Zhou, Ziyi Hao et al. (11 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09125v1) | [PDF](https://arxiv.org/pdf/2608.09125v1.pdf)

<details>
<summary>Abstract</summary>

Surgical robotic systems are increasingly being adopted as clinical workload rises, motivating autonomous solutions for repetitive manipulation subtasks. Learning-based controllers improve generalization compared with rule-based and analytic approaches, but most are trained for individual tasks and remain difficult to reuse across procedures. Vision-Language-Action (VLA) models provide a unified framework that integrates visual perception, language grounding, and action generation, offering a pr...

</details>

---
