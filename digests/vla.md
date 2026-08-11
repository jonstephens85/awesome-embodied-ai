# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-11 16:57 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability](https://arxiv.org/abs/2608.08904v1)

**Authors:** Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou

**Published:** 2026-08-09 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.08904v1) | [PDF](https://arxiv.org/pdf/2608.08904v1.pdf)

<details>
<summary>Abstract</summary>

How much of a vision-language model's (VLM) spatial understanding remains after the action post-training process of building a vision-language-action model (VLA)? We probe depth perception, a primitive of spatiogeometric understanding, from every decoder layer of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO. First, the VLA decodes depth worse at every layer, a persistent gap we call the floor. Second, the degradation is not uniform: while the base VLM's depth de...

</details>

---

### [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749v1)

**Authors:** Zhongxi Chen, Shenqi Zong

**Published:** 2026-08-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.08749v1) | [PDF](https://arxiv.org/pdf/2608.08749v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires policies to track completed subtasks and critical interaction events. However, existing memory mechanisms heavily rely on external models or predefined update rules. To address this, we propose OnEvoMemory, a value-guided memory module for pretrained robot policies. It maintains recent context, high-value experiences, and salient transitions, while learning which experiences should be retained from trajectory outcomes. Offline demonstrations initialize th...

</details>

---

### [WA-SpecDec: World-Aware Speculative Decoding for Vision-Language-Action Models](https://arxiv.org/abs/2608.08725v1)

**Authors:** Zikang Wen, Yuning Zhang, Dong Yuan

**Published:** 2026-08-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.08725v1) | [PDF](https://arxiv.org/pdf/2608.08725v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies generate robot controls autoregressively, making closed-loop latency dominated by repeated target-model forward passes. Speculative decoding reduces this cost by verifying blocks of draft action tokens in parallel, and recent VLA methods further relax token-level acceptance because small differences in action-token space often map to similar continuous controls. However, this relaxation remains scene-agnostic. A fixed token-distance tolerance treats the same...

</details>

---
