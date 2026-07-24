# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-24 17:37 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers](https://arxiv.org/abs/2607.21594v1)

**Authors:** Sicheng Mo, Yuheng Li, Ziyang Leng, Krishna Kumar Singh, Bolei Zhou

**Published:** 2026-07-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.21594v1) | [PDF](https://arxiv.org/pdf/2607.21594v1.pdf) | [Project Page](https://vail-ucla.github.io/worldweaver/)

<details>
<summary>Abstract</summary>

Multi-agent interactive world models should not only generate consistent observations, but also maintain world states that persist across agents and evolve across views. Existing autoregressive video diffusion pipelines carry forward observation history as conditioning context, which makes shared state difficult to maintain in multi-agent and multi-view settings. We present WorldWeaver (W^2), a streaming multi-agent video diffusion model that augments rollout with cross-agent world state registe...

</details>

---

### [The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL](https://arxiv.org/abs/2607.19749v1)

**Authors:** Gurp Nijjer

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19749v1) | [PDF](https://arxiv.org/pdf/2607.19749v1.pdf) | [GitHub](https://github.com/gurpnijjer/dream-rehearsal)

<details>
<summary>Abstract</summary>

Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? Under never-clear replay, pre-registered component-level probes (n=3 seeds throughout) show that the world model retains essentially everything measurable about old tasks -- reward discrimi...

</details>

---

## Other Recent Papers

### [HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](https://arxiv.org/abs/2607.20988v1)

**Authors:** Quanfu Yu, Xian Wu, Hao Xu, Liulong Ma

**Published:** 2026-07-23 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.20988v1) | [PDF](https://arxiv.org/pdf/2607.20988v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models augmented with world modeling represent a promising paradigm for end-to-end autonomous driving. While pixel-level future prediction enables fine-grained spatiotemporal reasoning, it compromises robustness in noisy driving scenarios. Conversely, latent-based world models alleviate this sensitivity but often incur limited interpretability and representational degradation due to absent pixel-level grounding. To reconcile this trade-off, we propose HyWorldVLA, a h...

</details>

---

### [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](https://arxiv.org/abs/2607.20653v1)

**Authors:** Haocheng Yin, Shuohan Tao, Yongsheng Chen, Lu Gan

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.20653v1) | [PDF](https://arxiv.org/pdf/2607.20653v1.pdf)

<details>
<summary>Abstract</summary>

Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge. Existing approaches typically rely on per-object optimization to fit material parameters, which can be slow and cannot generalize, while end-to-end learned alternatives extrapolate poorly and often violate basic physical structure. We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks. A ...

</details>

---

### [Active Inference as a Convex Markov Decision Process](https://arxiv.org/abs/2607.20152v1)

**Authors:** Nikola Milosevic, Nicolás Hinrichs, Nico Scherf

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.AI, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2607.20152v1) | [PDF](https://arxiv.org/pdf/2607.20152v1.pdf)

<details>
<summary>Abstract</summary>

Active Inference (AIF) frames adaptive behavior as the minimization of expected free energy (EFE), combining epistemic and pragmatic objectives within a single variational principle. We frame AIF as policy optimization and show that, for closed-loop control policies, EFE minimization can be formulated as a convex Markov decision process (MDP). In this formulation, the pragmatic terms are linear in the predictive state marginals and therefore equivalent to reward maximization in a latent MDP, whi...

</details>

---

### [LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition](https://arxiv.org/abs/2607.19889v1)

**Authors:** Jiajun Cheng, Subarna Tripathi, Sainan Liu, Xiaofan Yu, Shan Lin

**Published:** 2026-07-22 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.19889v1) | [PDF](https://arxiv.org/pdf/2607.19889v1.pdf)

<details>
<summary>Abstract</summary>

Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery. Pretrained vision-language models (VLMs) and vision encoders offer an alternative to conventional interaction classifiers by transferring broad visual and semantic knowledge. However, adapting them to fine-grained surgical interactions remains challenging: (1) freezing the vision encoder depends entirely on pretrained representations that may retain noise and provide weak spati...

</details>

---

### [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876v1)

**Authors:** Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai et al. (6 authors)

**Published:** 2026-07-22 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.19876v1) | [PDF](https://arxiv.org/pdf/2607.19876v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge. While closed-loop evaluation via simulator rollouts offers a more faithful assessment of physical plausibility than open-loop alternatives, existing frameworks almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be brittle to data outside their training distribution, resulting in u...

</details>

---

### [Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning](https://arxiv.org/abs/2607.19809v1)

**Authors:** Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi

**Published:** 2026-07-22 | **Categories:** cs.MA, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.19809v1) | [PDF](https://arxiv.org/pdf/2607.19809v1.pdf)

<details>
<summary>Abstract</summary>

In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) ...

</details>

---

### [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/abs/2607.19719v1)

**Authors:** Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan et al. (6 authors)

**Published:** 2026-07-22 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.19719v1) | [PDF](https://arxiv.org/pdf/2607.19719v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. Its Koopman-inspired backbone uses two-dimensional rotation--scaling blocks with bounded radii to represent damping, rotation, an...

</details>

---
