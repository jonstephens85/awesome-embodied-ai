# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-06 16:41 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)

**Authors:** Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo

**Published:** 2026-03-05 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.04910v1) | [PDF](https://arxiv.org/pdf/2603.04910v1.pdf) | [GitHub](https://github.com/HarryLui98/code_vpwem)

<details>
<summary>Abstract</summary>

Imitation learning from human demonstrations has achieved significant success in robotic control, yet most visuomotor policies still condition on single-step observations or short-context histories, making them struggle with non-Markovian tasks that require long-term memory. Simply enlarging the context window incurs substantial computational and memory costs and encourages overfitting to spurious correlations, leading to catastrophic failures under distribution shift and violating real-time con...

</details>

---

### [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)

**Authors:** Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan et al. (7 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05117v1) | [PDF](https://arxiv.org/pdf/2603.05117v1.pdf) | [GitHub](https://github.com/Youqiang-Gui/SeedPolicy)

<details>
<summary>Abstract</summary>

Imitation Learning (IL) enables robots to acquire manipulation skills from expert demonstrations. Diffusion Policy (DP) models multi-modal expert behaviors but suffers performance degradation as observation horizons increase, limiting long-horizon manipulation. We propose Self-Evolving Gated Attention (SEGA), a temporal module that maintains a time-evolving latent state via gated attention, enabling efficient recurrent updates that compress long-horizon observations into a fixed-size representat...

</details>

---

### [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://arxiv.org/abs/2603.04639v1)

**Authors:** Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang et al. (9 authors)

**Published:** 2026-03-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.04639v1) | [PDF](https://arxiv.org/pdf/2603.04639v1.pdf) | [Project Page](https://robomme.github.io)

<details>
<summary>Abstract</summary>

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits their systematic understanding, comparison, and progress measurement. To address these challenges, we introduce RoboMME: a large-s...

</details>

---

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

## Other Recent Papers

### [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)

**Authors:** Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05487v1) | [PDF](https://arxiv.org/pdf/2603.05487v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) have shown remarkable progress towards embodied intelligence. While their architecture partially resembles that of Large Language Models (LLMs), VLAs exhibit higher complexity due to their multi-modal inputs/outputs and often hybrid nature of transformer and diffusion heads. This is part of the reason why insights from mechanistic interpretability in LLMs, which explain how the internal model representations relate to their output behavior, do not trivially t...

</details>

---

### [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410v1)

**Authors:** Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng et al. (8 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05410v1) | [PDF](https://arxiv.org/pdf/2603.05410v1.pdf)

<details>
<summary>Abstract</summary>

In the domain of humanoid robot control, the fusion of Vision-Language-Action (VLA) with whole-body control is essential for semantically guided execution of real-world tasks. However, existing methods encounter challenges in terms of low VLA inference efficiency or an absence of effective semantic guidance for whole-body control, resulting in instability in dynamic limb-coordinated tasks. To bridge this gap, we present a semantic-motion intent guided, physics-aware multi-brain VLA framework for...

</details>

---

### [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377v1)

**Authors:** Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum

**Published:** 2026-03-05 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.05377v1) | [PDF](https://arxiv.org/pdf/2603.05377v1.pdf)

<details>
<summary>Abstract</summary>

Open-world navigation requires robots to make decisions in complex everyday environments while adapting to flexible task requirements. Conventional navigation approaches often rely on dense 3D reconstruction and hand-crafted goal metrics, which limits their generalization across tasks and environments. Recent advances in vision--language navigation (VLN) and vision--language--action (VLA) models enable end-to-end policies conditioned on natural language, but typically require interactive trainin...

</details>

---

### [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)

**Authors:** Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan et al. (7 authors)

**Published:** 2026-03-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05185v1) | [PDF](https://arxiv.org/pdf/2603.05185v1.pdf)

<details>
<summary>Abstract</summary>

Balancing high-level semantic reasoning with low-level reactive control remains a core challenge in visual robotic manipulation. While Vision-Language Models (VLMs) excel at cognitive planning, their inference latency precludes real-time execution. Conversely, fast Vision-Language-Action (VLA) models often lack the semantic depth required for complex, long-horizon tasks. To bridge this gap, we introduce Critic in the Loop, an adaptive hierarchical framework driven by dynamic VLM-Expert schedulin...

</details>

---

### [Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models](https://arxiv.org/abs/2603.05147v1)

**Authors:** Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci

**Published:** 2026-03-05 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.05147v1) | [PDF](https://arxiv.org/pdf/2603.05147v1.pdf)

<details>
<summary>Abstract</summary>

Current research on Vision-Language-Action (VLA) models predominantly focuses on enhancing generalization through established reasoning techniques. While effective, these improvements invariably increase computational complexity and inference latency. Furthermore, these mechanisms are typically applied indiscriminately, resulting in the inefficient allocation of resources for trivial tasks while simultaneously failing to provide the uncertainty estimation necessary to prevent catastrophic failur...

</details>

---

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
