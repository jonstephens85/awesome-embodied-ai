# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-29 00:25 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406v1)

**Authors:** Kechen Liu, Ola Shorinwa

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.27406v1) | [PDF](https://arxiv.org/pdf/2608.27406v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical l...

</details>

---

### [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](https://arxiv.org/abs/2608.27328v1)

**Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li et al. (10 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.27328v1) | [PDF](https://arxiv.org/pdf/2608.27328v1.pdf) | [GitHub](https://github.com/AMAP-ML/R2MBench)

<details>
<summary>Abstract</summary>

High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambiguity makes absolute revisit scores sensitive to rendering stability, repetitive content, and failed motion. We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency. For every detected return, R2M-Bench compar...

</details>

---

### [SpatialCrafter: Single Image World Modeling with Generative 3D Proxies](https://arxiv.org/abs/2608.27073v1)

**Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo et al. (11 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.27073v1) | [PDF](https://arxiv.org/pdf/2608.27073v1.pdf) | [Project Page](https://fangchuan.github.io/SpatialCrafter/)

<details>
<summary>Abstract</summary>

Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generati...

</details>

---

### [Decoupling Planning and Control for Instructable Agents](https://arxiv.org/abs/2608.26788v1)

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr

**Published:** 2026-08-27 | **Categories:** cs.AI, cs.CL, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2608.26788v1) | [PDF](https://arxiv.org/pdf/2608.26788v1.pdf) | [Project Page](https://zinengtang.github.io/instruct-to-act/)

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model c...

</details>

---

## Other Recent Papers

### [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](https://arxiv.org/abs/2608.27367v1)

**Authors:** Frederik Berenz

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.27367v1) | [PDF](https://arxiv.org/pdf/2608.27367v1.pdf)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transform...

</details>

---

### [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345v1)

**Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević et al. (14 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.27345v1) | [PDF](https://arxiv.org/pdf/2608.27345v1.pdf)

<details>
<summary>Abstract</summary>

Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recove...

</details>

---
