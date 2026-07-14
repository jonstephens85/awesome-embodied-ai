# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-14 17:13 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WALA Learning Executable Latent Actions from Action-Labeled Demonstrations and Action-Free Videos](https://arxiv.org/abs/2607.11397v1)

**Authors:** Jiahao Liu, Zhongpu Xia, Shuai Tian, Huangrui Li, Yuhang Zheng et al. (16 authors)

**Published:** 2026-07-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.11397v1) | [PDF](https://arxiv.org/pdf/2607.11397v1.pdf) | [Project Page](https://liujiahao2077.github.io/WALA.github.io)

<details>
<summary>Abstract</summary>

Generalizable robot policies typically rely on action-labeled robot demonstrations, which are expensive to collect and difficult to scale. In contrast, large-scale human and robot videos contain rich physical interactions but often lack executable robot action labels. We present WALA, a framework for learning executable latent actions from both action-labeled demonstrations and action-free videos. WALA first pretrains a semantic-geometric latent action model from videos by modeling the evolution...

</details>

---

## Other Recent Papers

### [Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/abs/2607.11836v1)

**Authors:** Zihan Su, Teng Hu, Jiangning Zhang, Ruiyan Wang, Ran Yi et al. (7 authors)

**Published:** 2026-07-13 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.11836v1) | [PDF](https://arxiv.org/pdf/2607.11836v1.pdf)

<details>
<summary>Abstract</summary>

Autoregressive diffusion models have enabled high-quality video generation, yet their sequential nature inherently suffers from error accumulation. In long-horizon video synthesis, minor prediction deviations compound over time, inevitably leading to unconstrained generative drift, structural collapse, and severe visual degradation. To address this, we propose Cycle-World, a novel framework designed for stable and temporally consistent long-video generation. Our approach tackles error drift by e...

</details>

---

### [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](https://arxiv.org/abs/2607.11689v1)

**Authors:** Yuanzhi Liang, Xufeng Zhan, Haibin Huang, Chi Zhang, Xuelong Li

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11689v1) | [PDF](https://arxiv.org/pdf/2607.11689v1.pdf)

<details>
<summary>Abstract</summary>

Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets and tasks follow different conventions, and runtime systems e...

</details>

---

### [ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v1)

**Authors:** Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li et al. (37 authors)

**Published:** 2026-07-13 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.11673v1) | [PDF](https://arxiv.org/pdf/2607.11673v1.pdf)

<details>
<summary>Abstract</summary>

We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajec...

</details>

---

### [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)

**Authors:** Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai et al. (24 authors)

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11643v1) | [PDF](https://arxiv.org/pdf/2607.11643v1.pdf)

<details>
<summary>Abstract</summary>

Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model...

</details>

---

### [Towards Predictive, Aligned, and Scalable Robot Learning](https://arxiv.org/abs/2607.11270v1)

**Authors:** Peijun Tang, Shangjin Xie, Baifu Huang, Binyan Sun, Haotian Yang et al. (9 authors)

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11270v1) | [PDF](https://arxiv.org/pdf/2607.11270v1.pdf)

<details>
<summary>Abstract</summary>

Learning, at its core, extends beyond memorization to the ability to reason and solve novel problems by navigating a space of possibilities. We introduce Lumo-2, a latent world-action model that generates actions by reasoning over world dynamics in latent space. The learned latent world dynamics capture physically grounded visual transitions, naturally encoding future possibilities and providing a unified substrate for cross-modal alignment. This formulation enables predictive reasoning akin to ...

</details>

---

### [Is Energy Guidance All You Need? Training-Free Norm Injection for Driving World Models](https://arxiv.org/abs/2607.10781v1)

**Authors:** Xiyan Su, Frank Diermeyer, Markus Lienkamp

**Published:** 2026-07-12 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.10781v1) | [PDF](https://arxiv.org/pdf/2607.10781v1.pdf)

<details>
<summary>Abstract</summary>

Driving world models built on large video-diffusion backbones generate realistic scenes but are hard to control: enforcing a traffic norm typically means retraining the backbone or conditioning it on hand-built layouts. We ask whether controllability requires training at all. Our experiment shows that a rectified-flow driving world model, which jointly generates future video and a planned ego trajectory, can have its planned trajectory steered entirely at sampling time by differentiable energy f...

</details>

---

### [World Models as Adversaries: Multi-Agent Self-Play Fine-Tuning for Robust Motion Planning](https://arxiv.org/abs/2607.10630v1)

**Authors:** Tong Nie, Yuewen Mei, Junlin He, Yihong Tang, Jian Sun et al. (6 authors)

**Published:** 2026-07-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.10630v1) | [PDF](https://arxiv.org/pdf/2607.10630v1.pdf)

<details>
<summary>Abstract</summary>

Robust motion planning in dense traffic requires autonomous vehicles to interact in rare and safety-critical scenarios that are underrepresented in naturalistic driving data. Although adversarial training offers a feasible solution, existing methods often rely on external scenario generators, heuristic perturbations, or simulator-heavy rollouts, which makes them difficult to integrate with modern autoregressive planners. Here, we cast adversarially robust planner learning as a constrained min-ma...

</details>

---
