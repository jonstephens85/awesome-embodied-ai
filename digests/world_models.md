# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-28 18:36 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players](https://arxiv.org/abs/2605.28816v1)

**Authors:** Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler et al. (10 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28816v1) | [PDF](https://arxiv.org/pdf/2605.28816v1.pdf) | [Project Page](https://research.nvidia.com/labs/sil/projects/gamma-world)

<details>
<summary>Abstract</summary>

World models for interactive video generation have largely focused on single-agent settings, where future observations are generated from a single control signal. However, many generated environments require multi-agent interaction: multiple players, robots, or embodied agents act simultaneously within a shared space. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient infere...

</details>

---

### [Turning Video Models into Generalist Robot Policies](https://arxiv.org/abs/2605.27817v1)

**Authors:** Sizhe Lester Li, Evan Kim, Xingjian Bai, Tong Zhao, Tao Pang et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.27817v1) | [PDF](https://arxiv.org/pdf/2605.27817v1.pdf) | [Project Page](https://vera.csail.mit.edu)

<details>
<summary>Abstract</summary>

Video generative models have emerged as a promising robotics backbone, capable of generating videos that depict the completion of complex tasks across embodiments and environments. Recent work proposes robot foundation models that jointly predict future observations and actions by finetuning video models with action-labeled data. In this paper, we test the limits of an alternative approach: leave the video planner as-is while training an embodiment-specific inverse dynamics model (IDM). This dec...

</details>

---

## Other Recent Papers

### [Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization](https://arxiv.org/abs/2605.28810v1)

**Authors:** Audrey Chan, Aaron Labbé, Jacob Lavoie, Jordan Bannister, Arsène Fansi Tchango et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.LG, cs.IR, cs.SD

**Links:** [arXiv](https://arxiv.org/abs/2605.28810v1) | [PDF](https://arxiv.org/pdf/2605.28810v1.pdf)

<details>
<summary>Abstract</summary>

Functional music applications, from consumer focus and sleep aids to clinical interventions, share a distinctive recommendation problem: success is defined by the listener's affective state, but online experimentation on emotion is ethically constrained, particularly for clinical populations who cannot reliably skip a song or report distress. We describe AMRS, the Affective Music Recommendation System deployed on LUCID's health-and-wellness platforms, which serve clinical users (primarily older ...

</details>

---

### [LEIA: Learned Environment for Interactive Architected Materials](https://arxiv.org/abs/2605.28368v1)

**Authors:** Haiqian Yang, Yuan Cao, Markus J. Buehler

**Published:** 2026-05-27 | **Categories:** cs.LG, cond-mat.mtrl-sci, physics.app-ph

**Links:** [arXiv](https://arxiv.org/abs/2605.28368v1) | [PDF](https://arxiv.org/pdf/2605.28368v1.pdf)

<details>
<summary>Abstract</summary>

World models have enabled interactive exploration of game environments and robotic manipulation, but physical engineering remains beyond their reach: real materials exhibit nonlinear constitutive laws, carry history-dependent internal state, undergo inertial dynamics, and may possess hierarchical structures spanning multiple length scales. We present LEIA (Learned Environment for Interactive Architected materials), a world model that lets engineers apply boundary conditions step by step and obse...

</details>

---

### [Hybrid Neural World Models](https://arxiv.org/abs/2605.28317v1)

**Authors:** Pranav Lakshmanan, Paras Chopra

**Published:** 2026-05-27 | **Categories:** cs.LG, cs.AI, math.NA

**Links:** [arXiv](https://arxiv.org/abs/2605.28317v1) | [PDF](https://arxiv.org/pdf/2605.28317v1.pdf)

<details>
<summary>Abstract</summary>

Neural surrogates promise large speedups over classical solvers for physical dynamics but fail silently at sharp dynamical events such as shocks, fronts, and contact. We present hybrid neural world models for physical dynamics: a recipe for training and deploying multi-horizon surrogates in physical state space, where a single network with continuous horizon conditioning is trained with direct supervision against textbook reference solvers to predict any future state at horizon T in one forward ...

</details>

---

### [Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning](https://arxiv.org/abs/2605.28277v1)

**Authors:** Zhikai Pan, Chih-Ting Liao, Chunrui Liu, Xi Xiao, Yitong Qiao et al. (8 authors)

**Published:** 2026-05-27 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.28277v1) | [PDF](https://arxiv.org/pdf/2605.28277v1.pdf)

<details>
<summary>Abstract</summary>

Whether large language models (LLMs) construct internal spatial world models from pure-text descriptions remains contested, and whether such capabilities transfer across languages has not been systematically studied. We introduce MentalMap, a multilingual diagnostic benchmark with a six-level capability hierarchy (L0-L5) spanning atomic spatial facts to generative world-graph construction, together with four diagnostic axes probing frame of reference, reading-direction bias, reasoning-effort all...

</details>

---

### [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230v1)

**Authors:** Mariam Hassan, Kaouther Messaoud, Wuyang Li, Alexandre Alahi

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28230v1) | [PDF](https://arxiv.org/pdf/2605.28230v1.pdf)

<details>
<summary>Abstract</summary>

Modern video generative models produce visually impressive results, yet frequently violate basic physical principles. We propose Proprio, a training-free framework that enables a frozen video generator to assess and improve the physical plausibility of its own outputs. Inspired by proprioception, the biological sense of one's own movement, Proprio treats the model's flow residual under controlled latent perturbations as a self-scoring signal. Samples that are better explained by the generator's ...

</details>

---

### [Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction](https://arxiv.org/abs/2605.28111v1)

**Authors:** Mufan Qiu, Genhui Zheng, Yinuo Xu, Ruichen Zhang, Ying Ding et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28111v1) | [PDF](https://arxiv.org/pdf/2605.28111v1.pdf)

<details>
<summary>Abstract</summary>

Predicting how a cell will change its transcriptional state under a developmental signal or a genetic perturbation is the computational core of in-silico biology and the AI Virtual Cell program. Existing approaches either fit static control-to-treated maps that discard time, or solve multi-step ODE / Schrödinger-bridge problems on each dataset independently. We introduce Chreode, a one-step cell world model that predicts action-conditioned cell-state transitions through a structured residual tra...

</details>

---

### [What-If World: A Causal Benchmark for General World Models in Embodied Scenarios](https://arxiv.org/abs/2605.27589v1)

**Authors:** Kunlin Cai, Rui Song, Jinghuai Zhang, Kaiyuan Zhang, Pranav Bodapati et al. (10 authors)

**Published:** 2026-05-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.27589v1) | [PDF](https://arxiv.org/pdf/2605.27589v1.pdf)

<details>
<summary>Abstract</summary>

Video generation models are increasingly used as world simulators for tasks like driving and robotic manipulation. What matters in these settings is not whether a single video looks right, but whether the model's output changes when its input changes. We test this by giving a model two prompts describing the same scene with one physical detail varied, and checking whether the two videos diverge the way physics predicts. The wording difference between the prompts is small by design, since only on...

</details>

---

### [Riding the Shifting Potential: When Reactive Control Suffices for Multi-Goal Behavior](https://arxiv.org/abs/2605.27314v1)

**Authors:** Vito Mengers, Oliver Brock

**Published:** 2026-05-26 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2605.27314v1) | [PDF](https://arxiv.org/pdf/2605.27314v1.pdf)

<details>
<summary>Abstract</summary>

Reactive control is often considered insufficient for multi-objective tasks because conflicting objectives give rise to local minima. We argue this limitation is not inherent but arises from static encodings that fail to reflect how objectives currently interact. We exploit the interaction structure encoded in a graph-based world model by extending it with nullspace projections: conflicts are resolved where they arise by projecting lower-priority gradients into the nullspace of higher-priority o...

</details>

---

### [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](https://arxiv.org/abs/2605.27491v1)

**Authors:** Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang, Lintao Wang et al. (15 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.27491v1) | [PDF](https://arxiv.org/pdf/2605.27491v1.pdf)

<details>
<summary>Abstract</summary>

We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation. Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially improving action-following fidelity and trajectory coverage. On top of this foundation, three new modules close the loop fr...

</details>

---
