# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-24 16:59 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WorldCache: Content-Aware Caching for Accelerated Video World Models](https://arxiv.org/abs/2603.22286v1)

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, Abdelrahman Shaker, Salman Khan et al. (6 authors)

**Published:** 2026-03-23 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2603.22286v1) | [PDF](https://arxiv.org/pdf/2603.22286v1.pdf) | [Project Page](https://umair1221.github.io/World-Cache/}{World-Cache})

<details>
<summary>Abstract</summary>

Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

</details>

---

### [FluidWorld: Reaction-Diffusion Dynamics as a Predictive Substrate for World Models](https://arxiv.org/abs/2603.21315v1)

**Authors:** Fabien Polly

**Published:** 2026-03-22 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.21315v1) | [PDF](https://arxiv.org/pdf/2603.21315v1.pdf) | [GitHub](https://github.com/infinition/FluidWorld/)

<details>
<summary>Abstract</summary>

World models learn to predict future states of an environment, enabling planning and mental simulation. Current approaches default to Transformer-based predictors operating in learned latent spaces. This comes at a cost: O(N^2) computation and no explicit spatial inductive bias. This paper asks a foundational question: is self-attention necessary for predictive world modeling, or can alternative computational substrates achieve comparable or superior results? I introduce FluidWorld, a proof-of-c...

</details>

---

## Other Recent Papers

### [ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model](https://arxiv.org/abs/2603.22281v1)

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, Tushar Nagarajan, Mingfei Chen et al. (8 authors)

**Published:** 2026-03-23 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2603.22281v1) | [PDF](https://arxiv.org/pdf/2603.22281v1.pdf)

<details>
<summary>Abstract</summary>

Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning ove...

</details>

---

### [Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)

**Authors:** Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang et al. (16 authors)

**Published:** 2026-03-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.22212v1) | [PDF](https://arxiv.org/pdf/2603.22212v1.pdf)

<details>
<summary>Abstract</summary>

Video--based world models have emerged along two dominant paradigms: video generation and 3D reconstruction. However, existing evaluation benchmarks either focus narrowly on visual fidelity and text--video alignment for generative models, or rely on static 3D reconstruction metrics that fundamentally neglect temporal dynamics. We argue that the future of world modeling lies in 4D generation, which jointly models spatial structure and temporal evolution. In this paradigm, the core capability is i...

</details>

---

### [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078v1)

**Authors:** Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma et al. (13 authors)

**Published:** 2026-03-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22078v1) | [PDF](https://arxiv.org/pdf/2603.22078v1.pdf)

<details>
<summary>Abstract</summary>

Robot action planning in the real world is challenging as it requires not only understanding the current state of the environment but also predicting how it will evolve in response to actions. Vision-language-action (VLA), which repurpose large-scale vision-language models for robot action generation using action experts, have achieved notable success across a variety of robotic tasks. Nevertheless, their performance remains constrained by the scope of their training data, exhibiting limited gen...

</details>

---

### [From Part to Whole: 3D Generative World Model with an Adaptive Structural Hierarchy](https://arxiv.org/abs/2603.21557v1)

**Authors:** Bi'an Du, Daizong Liu, Pufan Li, Wei Hu

**Published:** 2026-03-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.21557v1) | [PDF](https://arxiv.org/pdf/2603.21557v1.pdf)

<details>
<summary>Abstract</summary>

Single-image 3D generation lies at the core of vision-to-graphics models in the real world. However, it remains a fundamental challenge to achieve reliable generalization across diverse semantic categories and highly variable structural complexity under sparse supervision. Existing approaches typically model objects in a monolithic manner or rely on a fixed number of parts, including recent part-aware models such as PartCrafter, which still require a labor-intensive user-specified part count. Su...

</details>

---

### [What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators](https://arxiv.org/abs/2603.21546v1)

**Authors:** Xinyu Zhang

**Published:** 2026-03-23 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.21546v1) | [PDF](https://arxiv.org/pdf/2603.21546v1.pdf)

<details>
<summary>Abstract</summary>

World models learn to simulate environment dynamics from experience, enabling sample-efficient reinforcement learning. But what do these models actually represent internally? We apply interpretability techniques--including linear and nonlinear probing, causal interventions, and attention analysis--to two architecturally distinct world models: IRIS (discrete token transformer) and DIAMOND (continuous diffusion UNet), trained on Atari Breakout and Pong. Using linear probes, we find that both model...

</details>

---

### [ARYA: A Physics-Constrained Composable & Deterministic World Model Architecture](https://arxiv.org/abs/2603.21340v1)

**Authors:** Seth Dobrin, Lukasz Chmiel

**Published:** 2026-03-22 | **Categories:** cs.AI, cs.DC

**Links:** [arXiv](https://arxiv.org/abs/2603.21340v1) | [PDF](https://arxiv.org/pdf/2603.21340v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents ARYA, a composable, physics-constrained, deterministic world model architecture built on five foundational principles: nano models, composability, causal reasoning, determinism, and architectural AI safety. We demonstrate that ARYA satisfies all canonical world model requirements, including state representation, dynamic prediction, causal and physical awareness, temporal consistency, generalization, learnability, and planning and control. Unlike monolithic foundation models, ...

</details>

---

### [CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation](https://arxiv.org/abs/2603.21104v1)

**Authors:** Bowen Jing, Ruiyang Hao, Weitao Zhou, Haibao Yu

**Published:** 2026-03-22 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.21104v1) | [PDF](https://arxiv.org/pdf/2603.21104v1.pdf)

<details>
<summary>Abstract</summary>

Generating safety-critical driving scenarios requires understanding why dangerous interactions arise, rather than merely forcing collisions. However, existing methods rely on heuristic adversarial agent selection and unstructured perturbations, lacking explicit modeling of interaction dependencies and thus exhibiting a realism--adversarial trade-off. We present CounterScene, a framework that endows closed-loop generative BEV world models with structured counterfactual reasoning for safety-critic...

</details>

---

### [Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness](https://arxiv.org/abs/2603.21017v1)

**Authors:** Ziou Hu, Xiangtong Yao, Yuan Meng, Zhenshan Bing, Alois Knoll

**Published:** 2026-03-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.21017v1) | [PDF](https://arxiv.org/pdf/2603.21017v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion policies excel at visuomotor control but often fail catastrophically under severe out-of-distribution (OOD) disturbances, such as unexpected object displacements or visual corruptions. To address this vulnerability, we introduce the Dream Diffusion Policy (DDP), a framework that deeply integrates a diffusion world model into the policy's training objective via a shared 3D visual encoder. This co-optimization endows the policy with robust state-prediction capabilities. When encountering...

</details>

---
