# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-25 23:07 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning](https://arxiv.org/abs/2606.25880v1)

**Authors:** Yuchen Xie, Xinyu Zhou, Kuangji Zuo, Yanshuo Lu, Fengrui Huang et al. (7 authors)

**Published:** 2026-06-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.25880v1) | [PDF](https://arxiv.org/pdf/2606.25880v1.pdf) | [Project Page](https://arescheah.github.io/uss-project-page/)

<details>
<summary>Abstract</summary>

Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only sp...

</details>

---

### [When Do Conservation Laws Survive Learned Representations? Certified Horizons for Latent World Models](https://arxiv.org/abs/2606.24945v1)

**Authors:** Hongbo Wang

**Published:** 2026-06-23 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.24945v1) | [PDF](https://arxiv.org/pdf/2606.24945v1.pdf) | [GitHub](https://github.com/TimothyWang418/se3-ejepa)

<details>
<summary>Abstract</summary>

We ask a representation-learning question about physical world models: when does a conservation law remain certifiable after a model learns a latent representation? A certified horizon bounds -- in advance, from measurable model defects -- how many steps a rollout provably stays on a physical invariant's level set. The key design choice is what is certified: not a learned latent Hamiltonian or a learned scalar witness (a model can conserve either while drifting in true energy), but the decoded p...

</details>

---

## Other Recent Papers

### [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1)

**Authors:** Seth Dobrin, Łukasz Chmiel

**Published:** 2026-06-24 | **Categories:** cs.AI, cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.26057v1) | [PDF](https://arxiv.org/pdf/2606.26057v1.pdf)

<details>
<summary>Abstract</summary>

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mecha...

</details>

---

### [In-Context World Modeling for Robotic Control](https://arxiv.org/abs/2606.26025v1)

**Authors:** Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji et al. (7 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26025v1) | [PDF](https://arxiv.org/pdf/2606.26025v1.pdf)

<details>
<summary>Abstract</summary>

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Mode...

</details>

---

### [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](https://arxiv.org/abs/2606.25527v1)

**Authors:** Guozheng Ma, Lu Li, Zilin Wang, Pierre-Luc Bacon, Dacheng Tao

**Published:** 2026-06-24 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.25527v1) | [PDF](https://arxiv.org/pdf/2606.25527v1.pdf)

<details>
<summary>Abstract</summary>

Online reinforcement learning (RL) agents increasingly depend on knowledge acquired offline to achieve practical efficiency. Originally studied in offline-to-online RL, this paradigm now spans foundation model post-training and embodied intelligence, with prior types expanding from offline datasets and pre-trained policies to increasingly diverse knowledge sources such as multimodal foundation models and generative world models. Offline priors have become central to how deep RL is developed and ...

</details>

---

### [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473v1)

**Authors:** Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen et al. (10 authors)

**Published:** 2026-06-24 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.25473v1) | [PDF](https://arxiv.org/pdf/2606.25473v1.pdf)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in dif...

</details>

---

### [Hypergraph Normal World Models for Logical Visual Anomaly Detection](https://arxiv.org/abs/2606.25368v1)

**Authors:** Weizhi Nie, Zibo Xu, Weijie Wang, Yuting Su

**Published:** 2026-06-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.25368v1) | [PDF](https://arxiv.org/pdf/2606.25368v1.pdf)

<details>
<summary>Abstract</summary>

Visual anomaly detection is often deployed with only normal training images. Most one-class detectors map test patches or features to a normal reference distribution. This works well for local structural defects. Logical anomalies are different. Each visible part may look normal, while the whole image violates a normal count, co-occurrence, or spatial relation. This paper studies whether a model can learn such a category-specific normal world from nominal images alone. We propose the Hypergraph ...

</details>

---

### [World Models in Pieces: Structural Certification for General Agents](https://arxiv.org/abs/2606.24842v1)

**Authors:** Yikai Lu, Yifei Wu, Xinyu Lu, Tongxin Li

**Published:** 2026-06-23 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.24842v1) | [PDF](https://arxiv.org/pdf/2606.24842v1.pdf)

<details>
<summary>Abstract</summary>

In the big-world regime, agents cannot be universally capable and their ability is inevitably specialized across a world model in pieces. Consequently, standard uniform guarantees fail to distinguish between the understanding of critical bottlenecks and irrelevant failures. We first formalize this limitation by proving that general agents are not universal, rendering standard worst-case analysis uninformative. To overcome this, we introduce structural certification, a transition-local framework ...

</details>

---

### [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742v1)

**Authors:** Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan et al. (7 authors)

**Published:** 2026-06-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.24742v1) | [PDF](https://arxiv.org/pdf/2606.24742v1.pdf)

<details>
<summary>Abstract</summary>

Generalist value models play a pivotal role in scaling robotic policy learning from large-scale, mixed-quality data. Mathematically, accurate value estimation demands deep temporal understanding, requiring models to both ground the current belief using historical context and plan over future outcomes. However, most existing robotic value models are built on Vision-Language Model (VLM) backbones that are pretrained primarily on static or temporally sparse visual observations, lacking the requisit...

</details>

---

### [Trimming the Long-Tail of Visual World Modeling Evaluation](https://arxiv.org/abs/2606.24256v1)

**Authors:** Bingxuan Li, Yining Hong, Cheng Qian, Hyeonjeong Ha, Jiateng Liu et al. (9 authors)

**Published:** 2026-06-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.24256v1) | [PDF](https://arxiv.org/pdf/2606.24256v1.pdf)

<details>
<summary>Abstract</summary>

Physical interactions follow a long-tailed distribution: a set of common and regular interactions dominates human experience and visual data, while a broad spectrum of rare and irregular interactions remains underrepresented. Although recent visual world models, including image and video generation models, achieve impressive realism on existing benchmarks, they primarily focus on simulating common physical interactions. This raises a central question: Do current visual world models internalize a...

</details>

---

### [Conformal Orbit-Valid Trust Horizons for Equivariant World Models](https://arxiv.org/abs/2606.24946v1)

**Authors:** Hongbo Wang

**Published:** 2026-06-23 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.24946v1) | [PDF](https://arxiv.org/pdf/2606.24946v1.pdf)

<details>
<summary>Abstract</summary>

Learned world models are useful only over horizons on which their rollout error remains controlled. We study trust-horizon certification for latent world models with known group symmetries. Given a one-step latent residual and a finite-time expansion estimate, we form a raw horizon curve and calibrate it with a split-conformal multiplicative factor. On the reproducible audit set, the conformal factor is $γ_α=1.0$: the raw certificate is already conservative under the audit protocol. Across 50 st...

</details>

---

### [Autonomous Video Generation with Counterfactual Controllability for Self-Evolving World Models](https://arxiv.org/abs/2606.24152v1)

**Authors:** Xin Wang, Wenxuan Liu, Tongtong Feng, Wenwu Zhu

**Published:** 2026-06-23 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.24152v1) | [PDF](https://arxiv.org/pdf/2606.24152v1.pdf)

<details>
<summary>Abstract</summary>

Existing literature claims that video generation essentially is world modelling. On the one hand, the claim is productive because it pushes generative AI beyond static images and toward temporally extended physical scenes. On the other hand, this claim dangerously relies on the belief that scaling visual prediction alone will automatically yield physical agents. We prefer a more accurate statement: video generation models learn a partial, implicit spatiotemporal world model, but not a fully grou...

</details>

---

### [NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101v1)

**Authors:** Yanghong Mei, Longteng Guo, Ming-Ming Yu, Guiyu Zhao, Xingjian He et al. (6 authors)

**Published:** 2026-06-23 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.24101v1) | [PDF](https://arxiv.org/pdf/2606.24101v1.pdf)

<details>
<summary>Abstract</summary>

Conventional visual navigation policies often struggle with myopic decision-making and mode collapse in complex environments. While world models offer a promising alternative, existing paradigms typically isolate perception, generation, and control, failing to capture their shared spatio-temporal dynamics. In this paper, we propose NavWM, a unified navigation world model that seamlessly integrates latent world reasoning, multimodal action prediction, and controllable visual generation. At its co...

</details>

---

### [DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089v1)

**Authors:** Haidong Hou, Zhangguo Yu, Hengbo Qi, Jianlin Zhang

**Published:** 2026-06-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.24089v1) | [PDF](https://arxiv.org/pdf/2606.24089v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in control have enabled bipedal-wheeled robots to traverse slopes and single-step obstacles, yet long staircase traversal remains challenging as current teacher-student frameworks suffer from weakened dynamics-aware representations and incomplete terrain geometry encoding. To bridge this gap, we propose DynaWM, a dynamics-aware representation learning framework. To enhance terrain encoding capability and enable transparent assessment, we introduce a world model as a regularizer t...

</details>

---
