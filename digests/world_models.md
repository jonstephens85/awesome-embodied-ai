# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-28 22:50 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](https://arxiv.org/abs/2607.23969v1)

**Authors:** Pei Liu, Nan Zheng, Lang Zhang, Daojie Peng, Yanan Zhang et al. (11 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.23969v1) | [PDF](https://arxiv.org/pdf/2607.23969v1.pdf) | [GitHub](https://github.com/LeapWM/leapbot-wa)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck. Forcing models to reconstruct task-irrelevant visual details dissipates representational capacity and renders policies vulnerable to visual distractors. In this paper, we propose LeapBot-WA, which establishes a novel Predictive-Latent paradigm for WAMs by operationalizing the Joint-Embedding Predictive Architecture...

</details>

---

## Other Recent Papers

### [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720v1)

**Authors:** Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao

**Published:** 2026-07-27 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.24720v1) | [PDF](https://arxiv.org/pdf/2607.24720v1.pdf)

<details>
<summary>Abstract</summary>

Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, making it difficult to identify how planning ability is acquired, shaped, and integrated. To address this challenge, we introduce a unified and controlled multi-turn environment that enables precise control. It allows systematically study long-horizon planning across three stages. (1) Planning abilit...

</details>

---

### [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](https://arxiv.org/abs/2607.24481v1)

**Authors:** Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24481v1) | [PDF](https://arxiv.org/pdf/2607.24481v1.pdf)

<details>
<summary>Abstract</summary>

Real-world evaluation is a bottleneck in developing generalist robot manipulation policies. Each rollout requires physical hardware and an operator to set up, reset, and score it. We introduce ArmnetBench v0.1, a benchmark run on a fleet of low-cost SO-101 cells under light on-site supervision. v0.1 validates this arm farm end to end and compares 7 policies across 12 tasks with both single-arm and bimanual configurations. Each policy is trained or fine-tuned on 50 demonstrations per task; the be...

</details>

---

### [Context Is King: How In-Context Specification Shapes the Geometry of Concepts](https://arxiv.org/abs/2607.24425v1)

**Authors:** Elad David, Max Fomin

**Published:** 2026-07-27 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.24425v1) | [PDF](https://arxiv.org/pdf/2607.24425v1.pdf)

<details>
<summary>Abstract</summary>

Large language models place structured concepts on geometrically faithful manifolds: weekdays lie on a circle, months on another, usually taken to be a fixed world-model the network stores and looks up. We show that context is king: the structure a model actually uses is set by the in-context specification. A declarative rule fixes not only which relations the geometry encodes but its topology type: the same tokens form a cycle or a branching tree on command, built even on arbitrary, meaning-fre...

</details>

---

### [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](https://arxiv.org/abs/2607.24267v1)

**Authors:** Wenxuan Ma, Chaofan Zhang, Chao Xue, Yinghao Cai, Guocai Yao et al. (7 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24267v1) | [PDF](https://arxiv.org/pdf/2607.24267v1.pdf)

<details>
<summary>Abstract</summary>

Humans plan physical interactions by imagining the possible outcomes of candidate actions. However, existing visual world models primarily capture appearance dynamics while overlooking the tactile states that govern contact-rich interactions, potentially producing imagined futures that appear visually plausible but violate physical dynamics. We introduce FeelWorld, a hierarchical visuo-tactile world model that jointly predicts future visual latents and three tactile states. FeelWorld organizes t...

</details>

---

### [Scaling GUI Agents with Visual State Transitions](https://arxiv.org/abs/2607.24112v1)

**Authors:** Xiangyan Liu, Kaixin Li, Haonan Wang, Biao Wu, Meng Fang et al. (9 authors)

**Published:** 2026-07-27 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.24112v1) | [PDF](https://arxiv.org/pdf/2607.24112v1.pdf)

<details>
<summary>Abstract</summary>

We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents. During the STP stage, we continually pretrain a unified multimodal model on visual state transitions by jointly optimizing inverse dynamics (predicting actions from state changes) and forward dynamics (predicting next states from current states and actions). This optimization equips the model with better action-grounded visual representations and an internal world model of GUI dynamics. When subsequently fine-t...

</details>

---

### [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909v1)

**Authors:** Sen Wang, R. Gnana Praveen, Bidhan Roy, Marcos Villagra

**Published:** 2026-07-27 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.23909v1) | [PDF](https://arxiv.org/pdf/2607.23909v1.pdf)

<details>
<summary>Abstract</summary>

Many recent robot policies pursue stronger control by using large pretrained vision-language models (VLMs) as the action backbone. We introduce WorldDiT, a unified diffusion transformer architecture that couples action generation with visual world modeling and achieves strong performance without a large pretrained VLM action backbone. During training, a single diffusion transformer generates continuous action chunks and predicts normalized RGB patch targets from future camera frames. Across four...

</details>

---

### [Embodied GPT-5.1: Evidence of a World Model?](https://arxiv.org/abs/2607.23899v1)

**Authors:** Roberto Spinelli, Thiago C. Martins

**Published:** 2026-07-27 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.23899v1) | [PDF](https://arxiv.org/pdf/2607.23899v1.pdf)

<details>
<summary>Abstract</summary>

This exploratory study examines whether a large multimodal language model, GPT-5.1, can serve as the high-level controller of a physical mobile robot despite having no prior embodiment, no training in simulated environments, and no exposure to sensorimotor experience. Using only low-resolution first-person images and a discrete action set, the model was tasked with navigation and object-directed behaviors such as locating and contacting a target toy. Across multiple trials, GPT-5.1 demonstrated ...

</details>

---

### [Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models](https://arxiv.org/abs/2607.23602v1)

**Authors:** Liangyu Li, Qingwen Liu, Mingqing Liu

**Published:** 2026-07-26 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.23602v1) | [PDF](https://arxiv.org/pdf/2607.23602v1.pdf)

<details>
<summary>Abstract</summary>

Controllers based on sampling and latent world models assign a predicted terminal cost to each candidate action sequence, choose the minimum, execute its first action block, and replan. This rule can fail even when the terminal cost perfectly and accurately reflects the true task objective in the physical world. Residual prediction error can give an infeasible sequence an anomalously low cost, and a larger proposal pool gives such errors more chances to outrank feasible alternatives. We call thi...

</details>

---

### [Real-Time Human-Centric World Modeling for Upper-Body Human-Object Interaction](https://arxiv.org/abs/2607.23517v1)

**Authors:** Chaonan Ji, Jinwei Qi, Peng Zhang, Bang Zhang

**Published:** 2026-07-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.23517v1) | [PDF](https://arxiv.org/pdf/2607.23517v1.pdf)

<details>
<summary>Abstract</summary>

We present a real-time human-centric world model for upper-body interactive generation, aiming to synthesize coherent local world dynamics centered on a person, where coordinated body, hand, and facial motions evolve jointly with controllable human-object discrete interaction. To this end, we adopt a continuous-discrete joint control scheme with two complementary components: a continuous human state and a discrete interaction state. For continuous human-state control, we introduce a unified impl...

</details>

---
