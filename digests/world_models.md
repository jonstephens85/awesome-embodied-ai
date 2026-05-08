# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-08 17:17 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [HaM-World: Soft-Hamiltonian World Models with Selective Memory for Planning](https://arxiv.org/abs/2605.05951v1)

**Authors:** Haoyun Tang, Haodong Cui, Keyao Xu, Kun Wang, Zhandong Mei

**Published:** 2026-05-07 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.05951v1) | [PDF](https://arxiv.org/pdf/2605.05951v1.pdf) | [GitHub](https://github.com/HaoyunT/HaM_World)

<details>
<summary>Abstract</summary>

World models enable model-based planning through learned latent dynamics, but imagined rollouts become unstable as the planning horizon grows or the dynamics distribution shifts. We argue that this instability reflects two missing structures in planner-facing latents: history-conditioned memory for approximate Markov completeness, and geometric organization that separates configuration, momentum, and task semantics. We propose HaM-World (HMW), a structured world model that decomposes the latent ...

</details>

---

## Other Recent Papers

### [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](https://arxiv.org/abs/2605.06388v1)

**Authors:**  Nilaksh, Saurav Jha, Artem Zholus, Sarath Chandar

**Published:** 2026-05-07 | **Categories:** cs.CV, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.06388v1) | [PDF](https://arxiv.org/pdf/2605.06388v1.pdf)

<details>
<summary>Abstract</summary>

World model-based policy evaluation is a practical proxy for testing real-world robot control by rolling out candidate actions in action-conditioned video diffusion models. As these models increasingly adopt latent diffusion modeling (LDM), choosing the right latent space becomes critical. While the status quo uses autoencoding latent spaces like VAEs that are primarily trained for pixel reconstruction, recent work suggests benefits from pretrained encoders with representation-aligned semantic l...

</details>

---

### [Earth-o1: A Grid-free Observation-native Atmospheric World Model](https://arxiv.org/abs/2605.06337v1)

**Authors:** Junchao Gong, Kaiyi Xu, Wangxu Wei, Siwei Tu, Jingyi Xu et al. (25 authors)

**Published:** 2026-05-07 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.06337v1) | [PDF](https://arxiv.org/pdf/2605.06337v1.pdf)

<details>
<summary>Abstract</summary>

Despite the unprecedented volume of multimodal data provided by modern Earth observation systems, our ability to model atmospheric dynamics remains constrained. Traditional modeling frameworks force heterogeneous measurements into predefined spatial grids, inherently limiting the full exploitation of raw sensor data and creating severe computational bottlenecks. Here we present Earth-o1, an observation-native atmospheric world model that overcomes these structural limitations. Rather than relyin...

</details>

---

### [MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents](https://arxiv.org/abs/2605.06334v1)

**Authors:** Ashwani Anand, Ivi Chatzi, Ritam Raha, Anne-Kathrin Schmuck

**Published:** 2026-05-07 | **Categories:** cs.CL, cs.LG, cs.LO

**Links:** [arXiv](https://arxiv.org/abs/2605.06334v1) | [PDF](https://arxiv.org/pdf/2605.06334v1.pdf)

<details>
<summary>Abstract</summary>

Tool-using large language model (LLM) agents are increasingly deployed in settings where their reliable behavior is governed by strict procedural manuals. Ensuring that such agents comply with the rules from these manuals is challenging, as they are typically written for humans in natural language while agent behavior manifests as an execution trace of tool calls. Existing evaluations of LLM agents rely on manually constructed benchmarks or LLM-based judges, which either do not scale or lack rel...

</details>

---

### [Render, Don't Decode: Weight-Space World Models with Latent Structural Disentanglement](https://arxiv.org/abs/2605.06298v1)

**Authors:** Roussel Desmond Nzoyem, Mauro Comi

**Published:** 2026-05-07 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.06298v1) | [PDF](https://arxiv.org/pdf/2605.06298v1.pdf)

<details>
<summary>Abstract</summary>

Training world models on vast quantities of unlabelled videos is a critical step toward fully autonomous intelligence. However, the prevailing paradigm of encoding raw pixels into opaque latent spaces and relying on heavy decoders for reconstruction leaves these models computationally expensive and uninterpretable. We address this problem by introducing NOVA, a world modelling framework that represents the system state as the weights and biases of an auxiliary coordinate-based implicit neural re...

</details>

---

### [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/abs/2605.06192v1)

**Authors:** Zhaoyang Yang, Yurun Jin, Lizhe Qi, Cong Huang, Kai Chen

**Published:** 2026-05-07 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.06192v1) | [PDF](https://arxiv.org/pdf/2605.06192v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained video diffusion models provide powerful spatiotemporal generative priors, making them a natural foundation for robotic world models. While recent world-action models jointly optimize future videos and actions, they predominantly treat video generation as an auxiliary representation for policy learning. Consequently, they insufficiently explore the inverse problem: leveraging action signals to guide video synthesis, thereby often failing to preserve precise robot spatial geometry and f...

</details>

---

### [Causal Reinforcement Learning for Complex Card Games: A Magic The Gathering Benchmark](https://arxiv.org/abs/2605.06066v1)

**Authors:** Cristiano da Costa Cunha, Ajmal Mian, Tim French, Wei Liu

**Published:** 2026-05-07 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.06066v1) | [PDF](https://arxiv.org/pdf/2605.06066v1.pdf)

<details>
<summary>Abstract</summary>

Causal reinforcement learning (RL) lacks benchmarks for complex systems that combine sequential decision making, hidden information, large masked action spaces, and explicit causal structure. We introduce MTG-Causal-RL, a Gymnasium benchmark built on Magic: The Gathering with a 3,077-dimensional partial observation, a 478-action masked discrete action space, five competitive Standard archetypes, three reward schemes, and a hand-specified Structural Causal Model (SCM) over strategic variables. Ev...

</details>

---

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
