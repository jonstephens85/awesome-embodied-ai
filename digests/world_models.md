# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-07 17:47 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Other Recent Papers

### [LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/abs/2605.05187v1)

**Authors:** Wei Luo, Yiting Lu, Xin Li, Haoran Li, Fengbin Guan et al. (35 authors)

**Published:** 2026-05-06 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.05187v1) | [PDF](https://arxiv.org/pdf/2605.05187v1.pdf)

<details>
<summary>Abstract</summary>

This paper reports on the LoViF 2026 PhyScore challenge, a competition on holistic quality assessment of world-model-generated videos across both 2D and 4D generation settings. The challenge is motivated by a central gap in current evaluation practice: perceptual quality alone is insufficient to judge whether generated dynamics are physically plausible, temporally coherent, and consistent with input conditions. Participants are required to build a metric that jointly predicts four dimensions, i....

</details>

---

### [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/abs/2605.05138v1)

**Authors:** Sergey Rodionov

**Published:** 2026-05-06 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.05138v1) | [PDF](https://arxiv.org/pdf/2605.05138v1.pdf)

<details>
<summary>Abstract</summary>

We evaluate an initial coding-agent system for ARC-AGI-3 in which the agent maintains an executable Python world model, verifies it against previous observations, refactors it toward simpler abstractions as a practical proxy for an MDL-like simplicity bias, and plans through the model before acting. The system is intentionally direct: it uses a scripted controller, predefined world-model interfaces, verifier programs, and a plan executor, but no hand-coded game-specific logic. We report results ...

</details>

---

### [Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior](https://arxiv.org/abs/2605.05115v1)

**Authors:** Daniel Wurgaft, Can Rager, Matthew Kowal, Vasudev Shyam, Sheridan Feucht et al. (16 authors)

**Published:** 2026-05-06 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.05115v1) | [PDF](https://arxiv.org/pdf/2605.05115v1.pdf)

<details>
<summary>Abstract</summary>

Neural representations carry rich geometric structure; but does that structure causally shape behavior? To address this question, we intervene along paths through activation space defined by different geometries, and measure the behavioral trajectories they induce. In particular, we test whether interventions that respect the geometry of activation space will yield behaviors close to those the model exhibits naturally. Concretely, we first fit an activation manifold $M_h$ to representations and ...

</details>

---

### [Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout](https://arxiv.org/abs/2605.05092v1)

**Authors:** Haozhuang Chi, Daosheng Qiu, Hao Su, Haochen Liu, Zirui Li et al. (7 authors)

**Published:** 2026-05-06 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.05092v1) | [PDF](https://arxiv.org/pdf/2605.05092v1.pdf)

<details>
<summary>Abstract</summary>

Safe L2/L3 driving automation requires anticipating human-in-the-loop reactions during shared-control transitions. While most driving world models forecast the external environment, in-cabin intelligence remains strictly recognition-oriented and lacks multi-step rollout capabilities for driver dynamics. We introduce Driver-WM, a driver-centric latent world model that rolls out in-cabin dynamics causally conditioned on out-cabin traffic context. This formulation unifies physical kinematics foreca...

</details>

---

### [The Predictive-Causal Gap: An Impossibility Theorem and Large-Scale Neural Evidence](https://arxiv.org/abs/2605.05029v1)

**Authors:** Kejun Liu

**Published:** 2026-05-06 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.05029v1) | [PDF](https://arxiv.org/pdf/2605.05029v1.pdf)

<details>
<summary>Abstract</summary>

We report a systematic failure mode in predictive representation learning. Across 2695 neural network configurations trained to predict linear-Gaussian dynamics, the optimal encoder tracks the environment rather than the system it is meant to model. The mean causal fidelity -- the fraction of encoder sensitivity allocated to system degrees of freedom -- is 0.49, and only 2.5% of configurations exceed 0.70. The failure intensifies with dimension: at N=100, the optimal encoder becomes causally bli...

</details>

---

### [A geometric relation of the error introduced by sampling a language model's output distribution to its internal state](https://arxiv.org/abs/2605.04899v1)

**Authors:** Albert F. Modenbach

**Published:** 2026-05-06 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.04899v1) | [PDF](https://arxiv.org/pdf/2605.04899v1.pdf)

<details>
<summary>Abstract</summary>

GPT-style language models are sensitive to single-token changes at generation points where the predicted probability distribution is spread across multiple tokens. Viewing this sensitivity as a geometric property, we derive an $\mathfrak{so}(n)$-valued 1-form that depends only on the geometry of the token embeddings. Despite this purely geometric origin, we show that its curvature is semantically meaningful: On chess reasoning tasks, the curvature couples to the world model of an off-the-shelf i...

</details>

---

### [Gyan: An Explainable Neuro-Symbolic Language Model](https://arxiv.org/abs/2605.04759v1)

**Authors:** Venkat Srinivasan, Vishaal Jatav, Anushka Chandrababu, Geetika Sharma

**Published:** 2026-05-06 | **Categories:** cs.CL, cs.AI, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2605.04759v1) | [PDF](https://arxiv.org/pdf/2605.04759v1.pdf)

<details>
<summary>Abstract</summary>

Transformer based pre-trained large language models have become ubiquitous. There is increasing evidence to suggest that even with large scale pre-training, these models do not capture complete compositional context and certainly not, the full human analogous context. Besides, by the very nature of the architecture, these models hallucinate, are difficult to maintain, are not easily interpretable and require enormous compute resources for training and inference. Here, we describe Gyan, an explai...

</details>

---

### [Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination](https://arxiv.org/abs/2605.04568v1)

**Authors:** Jonathan Spieler, Sven Behnke

**Published:** 2026-05-06 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.04568v1) | [PDF](https://arxiv.org/pdf/2605.04568v1.pdf)

<details>
<summary>Abstract</summary>

State-of-the-art model-based Reinforcement Learning (RL) approaches either use gradient-free, population-based methods for planning, learned policy networks, or a combination of policy networks and planning. Hybrid approaches that combine Model Predictive Control (MPC) with a learned model and a policy prior to leverage the advantages of both paradigms have shown promising results. However, these approaches typically rely on gradient-free optimization methods, which can be computationally expens...

</details>

---

### [Counterfactual identifiability beyond global monotonicity: non-monotone triangular structural causal models](https://arxiv.org/abs/2605.04413v1)

**Authors:** Pengcheng Tan, Jiang Chen, Dehui Du

**Published:** 2026-05-06 | **Categories:** cs.LG, stat.ME

**Links:** [arXiv](https://arxiv.org/abs/2605.04413v1) | [PDF](https://arxiv.org/pdf/2605.04413v1.pdf)

<details>
<summary>Abstract</summary>

Structural causal models provide a unified semantics for interventions and counterfactuals, but most identifiability results rely on restrictive assumptions like global monotonicity, which are often violated in embodied interaction, where the same exogenous perturbation can induce opposite responses under different contact contexts. We ask what structure still suffices once global monotonicity is dropped. We introduce non-monotone triangular structural causal models (NM-TM-SCM), which retain tri...

</details>

---

### [iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework](https://arxiv.org/abs/2605.03941v2)

**Authors:** Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang et al. (11 authors)

**Published:** 2026-05-05 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.03941v2) | [PDF](https://arxiv.org/pdf/2605.03941v2.pdf)

<details>
<summary>Abstract</summary>

Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception an...

</details>

---

### [Awaking Spatial Intelligence in Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2605.04128v1)

**Authors:** Lin Song, Wenbo Li, Guoqing Ma, Wei Tang, Bo Wang et al. (19 authors)

**Published:** 2026-05-05 | **Categories:** cs.GR, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.04128v1) | [PDF](https://arxiv.org/pdf/2605.04128v1.pdf)

<details>
<summary>Abstract</summary>

We present JoyAI-Image, a unified multimodal foundation model for visual understanding, text-to-image generation, and instruction-guided image editing. JoyAI-Image couples a spatially enhanced Multimodal Large Language Model (MLLM) with a Multimodal Diffusion Transformer (MMDiT), allowing perception and generation to interact through a shared multimodal interface. Around this architecture, we build a scalable training recipe that combines unified instruction tuning, long-text rendering supervisi...

</details>

---

### [RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models](https://arxiv.org/abs/2605.03821v1)

**Authors:** Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang et al. (13 authors)

**Published:** 2026-05-05 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.03821v1) | [PDF](https://arxiv.org/pdf/2605.03821v1.pdf)

<details>
<summary>Abstract</summary>

Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon in...

</details>

---

### [What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity](https://arxiv.org/abs/2605.03782v1)

**Authors:** Haoxi Li, Qinglin Hou, Jianfei Ma, Jinxiang Lai, Tao Han et al. (9 authors)

**Published:** 2026-05-05 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.03782v1) | [PDF](https://arxiv.org/pdf/2605.03782v1.pdf)

<details>
<summary>Abstract</summary>

To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities into their policies via explicit CoT reasoning, enabling them to mentally simulate futures before acting. However, relying solely on passive reasoning over visited states is insufficient for sparse-reward tasks, as it lacks the epistemic drive to actively uncover the ``known unknown'' required for robust generalization. We ask: Can VLM agents actively find signals that cha...

</details>

---

### [Learning to Theorize the World from Observation](https://arxiv.org/abs/2605.03413v1)

**Authors:** Doojin Baek, Gyubin Lee, Junyeob Baek, Hosung Lee, Sungjin Ahn

**Published:** 2026-05-05 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.03413v1) | [PDF](https://arxiv.org/pdf/2605.03413v1.pdf)

<details>
<summary>Abstract</summary>

What does it mean to understand the world? Contemporary world models often operationalize understanding as accurate future prediction in latent or observation space. Developmental cognitive science, however, suggests a different view: human understanding emerges through the construction of internal theories of how the world works, even before mature language is acquired. Inspired by this theory-building view of cognition, we introduce Learning-to-Theorize, a learning paradigm for inferring expli...

</details>

---
