# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-09 16:55 UTC

**Papers found:** 7

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
