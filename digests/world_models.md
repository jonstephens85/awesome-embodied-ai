# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-25 17:02 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG](https://arxiv.org/abs/2603.23497v1)

**Authors:** Zhen Li, Zian Meng, Shuwei Shi, Wenshuo Peng, Yuwei Wu et al. (8 authors)

**Published:** 2026-03-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.23497v1) | [PDF](https://arxiv.org/pdf/2603.23497v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Dynamical systems theory and reinforcement learning view world evolution as latent-state dynamics driven by actions, with visual observations providing partial information about the state. Recent video world models attempt to learn this action-conditioned dynamics from data. However, existing datasets rarely match the requirement: they typically lack diverse and semantically meaningful action spaces, and actions are directly tied to visual observations rather than mediated by underlying states. ...

</details>

---

### [VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs](https://arxiv.org/abs/2603.23481v1)

**Authors:** Haoran Yuan, Weigang Yi, Zhenyu Zhang, Wendi Chen, Yuchen Mo et al. (12 authors)

**Published:** 2026-03-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.23481v1) | [PDF](https://arxiv.org/pdf/2603.23481v1.pdf) | [Project Page](https://plan-lab.github.io/projects/vtam/)

<details>
<summary>Abstract</summary>

Video-Action Models (VAMs) have emerged as a promising framework for embodied intelligence, learning implicit world dynamics from raw video streams to produce temporally consistent action predictions. Although such models demonstrate strong performance on long-horizon tasks through visual reasoning, they remain limited in contact-rich scenarios where critical interaction states are only partially observable from vision alone. In particular, fine-grained force modulation and contact transitions a...

</details>

---

### [WorldCache: Content-Aware Caching for Accelerated Video World Models](https://arxiv.org/abs/2603.22286v1)

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, Abdelrahman Shaker, Salman Khan et al. (6 authors)

**Published:** 2026-03-23 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2603.22286v1) | [PDF](https://arxiv.org/pdf/2603.22286v1.pdf) | [Project Page](https://umair1221.github.io/World-Cache/}{World-Cache})

<details>
<summary>Abstract</summary>

Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsiste...

</details>

---

## Other Recent Papers

### [ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376v1)

**Authors:** Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi et al. (14 authors)

**Published:** 2026-03-24 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.23376v1) | [PDF](https://arxiv.org/pdf/2603.23376v1.pdf)

<details>
<summary>Abstract</summary>

Video-based world models offer a powerful paradigm for embodied simulation and planning, yet state-of-the-art models often generate physically implausible manipulations - such as object penetration and anti-gravity motion - due to training on generic visual data and likelihood-based objectives that ignore physical laws. We present ABot-PhysWorld, a 14B Diffusion Transformer model that generates visually realistic, physically plausible, and action-controllable videos. Built on a curated dataset o...

</details>

---

### [Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models](https://arxiv.org/abs/2603.23149v1)

**Authors:** Massimiliano Pappa, Luca Romani, Valentino Sacco, Alessio Palma, Stéphane Lathuilière et al. (8 authors)

**Published:** 2026-03-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.23149v1) | [PDF](https://arxiv.org/pdf/2603.23149v1.pdf)

<details>
<summary>Abstract</summary>

Deploying safety-critical agents requires anticipating the consequences of actions before they are executed. While world models offer a paradigm for this proactive foresight, current approaches relying on visual simulation incur prohibitive latencies, often exceeding several seconds per step. In this work, we challenge the assumption that visual processing is necessary for failure prevention. We show that a trained policy's latent state, combined with its planned actions, already encodes suffici...

</details>

---

### [PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)

**Authors:** Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang

**Published:** 2026-03-24 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22796v1) | [PDF](https://arxiv.org/pdf/2603.22796v1.pdf)

<details>
<summary>Abstract</summary>

Embodied agents for creative tasks like photography must bridge the semantic gap between high-level language commands and geometric control. We introduce PhotoAgent, an agent that achieves this by integrating Large Multimodal Models (LMMs) reasoning with a novel control paradigm. PhotoAgent first translates subjective aesthetic goals into solvable geometric constraints via LMM-driven, chain-of-thought (CoT) reasoning, allowing an analytical solver to compute a high-quality initial viewpoint. Thi...

</details>

---

### [AI Mental Models: Learned Intuition and Deliberation in a Bounded Neural Architecture](https://arxiv.org/abs/2603.22561v1)

**Authors:** Laurence Anthony

**Published:** 2026-03-23 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.22561v1) | [PDF](https://arxiv.org/pdf/2603.22561v1.pdf)

<details>
<summary>Abstract</summary>

This paper asks whether a bounded neural architecture can exhibit a meaningful division of labor between intuition and deliberation on a classic 64-item syllogistic reasoning benchmark. More broadly, the benchmark is relevant to ongoing debates about world models and multi-stage reasoning in AI. It provides a controlled setting for testing whether a learned system can develop structured internal computation rather than only one-shot associative prediction. Experiment 1 evaluates a direct neural ...

</details>

---

### [Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning](https://arxiv.org/abs/2603.22430v1)

**Authors:** Rohan Deb, Stephen J. Wright, Arindam Banerjee

**Published:** 2026-03-23 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.22430v1) | [PDF](https://arxiv.org/pdf/2603.22430v1.pdf)

<details>
<summary>Abstract</summary>

Offline Reinforcement Learning (RL) aims to learn optimal policies from fixed offline datasets, without further interactions with the environment. Such methods train an offline policy (or value function), and apply it at inference time without further refinement. We introduce an inference time adaptation framework inspired by model predictive control (MPC) that utilizes a pretrained policy along with a learned world model of state transitions and rewards. While existing world model and diffusion...

</details>

---

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
