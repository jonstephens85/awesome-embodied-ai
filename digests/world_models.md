# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-29 18:32 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [NeuROK: Generative 4D Neural Object Kinematics](https://arxiv.org/abs/2605.30347v1)

**Authors:** Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu et al. (6 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2605.30347v1) | [PDF](https://arxiv.org/pdf/2605.30347v1.pdf) | [Project Page](https://chen-geng.com/neurok)

<details>
<summary>Abstract</summary>

Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these...

</details>

---

### [YoCausal: How Far is Video Generation from World Model? A Causality Perspective](https://arxiv.org/abs/2605.30346v1)

**Authors:** You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu et al. (6 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.30346v1) | [PDF](https://arxiv.org/pdf/2605.30346v1.pdf) | [Project Page](https://www.youzhexie.me/papers/YoCausal/index.html)

<details>
<summary>Abstract</summary>

As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, ...

</details>

---

### [minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://arxiv.org/abs/2605.30263v1)

**Authors:** Min Zhao, Hongzhou Zhu, Bokai Yan, Zihan Zhou, Yimin Chen et al. (12 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.30263v1) | [PDF](https://arxiv.org/pdf/2605.30263v1.pdf) | [GitHub](https://github.com/shengshu-ai/minWM)

<details>
<summary>Abstract</summary>

Recent video diffusion foundation models have achieved remarkable progress in high-quality video generation, yet turning them into real-time interactive video world models remains challenging. Interactive world models require controllable, causal, and low-latency rollout, which in practice demands a full pipeline spanning data construction, controllable fine-tuning, autoregressive training, few-step distillation, and streaming inference. In this work, we present minWM, a full-stack open-source f...

</details>

---

### [PassNet: Scaling Large Language Models for Graph Compiler Pass Generation](https://arxiv.org/abs/2605.29357v1)

**Authors:** Yiqun Liu, Yingsheng Wu, Ruqi Yang, Enrong Zheng, Honglei Qiu et al. (14 authors)

**Published:** 2026-05-28 | **Categories:** cs.AI, cs.LG, cs.PL

**Links:** [arXiv](https://arxiv.org/abs/2605.29357v1) | [PDF](https://arxiv.org/pdf/2605.29357v1.pdf) | [GitHub](https://github.com/PaddlePaddle/PassNet)

<details>
<summary>Abstract</summary>

Modern tensor compilers such as TorchInductor deliver substantial speedups on mainstream models, yet face a systematic performance ceiling on long-tail workloads -- our profiling shows that 43% of real-world subgraphs experience end-to-end slowdowns under default compilation. While LLMs offer a path toward automated optimization, existing efforts focus on standalone kernel generation. We argue that pass generation -- where LLMs author structured graph transformations that integrate directly into...

</details>

---

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

### [Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences](https://arxiv.org/abs/2605.30100v1)

**Authors:** Benjamin Walker, Terry Lyons

**Published:** 2026-05-28 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.30100v1) | [PDF](https://arxiv.org/pdf/2605.30100v1.pdf)

<details>
<summary>Abstract</summary>

World models require state tracking, which is the ability to maintain a correct latent state across action sequences. Existing benchmarks are often synthetic or language-based, limiting their value as tests of structured state updates in realistic domains. We introduce Chess-World-Model, a large-scale state-tracking benchmark built from 10 million real chess games, where models predict the exact board state reached after a sequence of legal moves. Alongside a held-out real-game split, we include...

</details>

---

### [Toward AI Systems That Understand Self and Others: A Multi-Phase Inference Framework for Human Cognitive Diversity and World-Model Alignment](https://arxiv.org/abs/2605.29930v1)

**Authors:** Toru Takahashi

**Published:** 2026-05-28 | **Categories:** cs.AI, cs.CY, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2605.29930v1) | [PDF](https://arxiv.org/pdf/2605.29930v1.pdf)

<details>
<summary>Abstract</summary>

Mutual misunderstanding in contemporary society does not arise merely because people hold different opinions or values. Even under the same observations, different subjects may form different inferential targets, state representations, prediction errors, and update priorities. This paper proposes a multi-phase inference framework and defines its core internal mechanism as the Multi-Phase Inference Mechanism (MIM). MIM formalizes how heterogeneous world models arise through a phase-formation spac...

</details>

---

### [MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models](https://arxiv.org/abs/2605.29360v1)

**Authors:** Tianzhuo Yang, Zihan Shen, Zirui Mi, Zhaoyi Zhang, Jiayi Zhou et al. (10 authors)

**Published:** 2026-05-28 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.29360v1) | [PDF](https://arxiv.org/pdf/2605.29360v1.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models are increasingly used as scalable simulators for robot learning, yet current evaluations provide limited evidence that their predictions are reliable under the actions they condition on. Existing benchmarks largely emphasize visual fidelity, leaving unclear whether predicted futures are physically plausible, faithful to commanded actions, and calibrated to failure when actions should not succeed. We introduce \textsc{MiraBench}, a hierarchical benchmark that defin...

</details>

---

### [Theoretical Foundations and Effective Algorithms for Policy-Aware Simulator Learning](https://arxiv.org/abs/2605.29032v1)

**Authors:** Christoph Dann, Yishay Mansour, Mehryar Mohri

**Published:** 2026-05-27 | **Categories:** cs.LG, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2605.29032v1) | [PDF](https://arxiv.org/pdf/2605.29032v1.pdf)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (MBRL) agents typically learn world models by minimizing predictive loss. However, powerful RL optimizers inevitably exploit minor model inaccuracies, leading to simulator exploitation and a reality gap where policies succeed in simulation but fail in the real world. We propose that the objective for learning simulators should be strategic robustness rather than predictive accuracy, and formulate this as a zero-sum minimax game between a model player and an adv...

</details>

---

### [Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization](https://arxiv.org/abs/2605.28810v1)

**Authors:** Audrey Chan, Aaron Labbé, Jacob Lavoie, Jordan Bannister, Arsène Fansi Tchango et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.LG, cs.IR, cs.SD

**Links:** [arXiv](https://arxiv.org/abs/2605.28810v1) | [PDF](https://arxiv.org/pdf/2605.28810v1.pdf)

<details>
<summary>Abstract</summary>

Functional music applications, from consumer focus and sleep aids to clinical interventions, share a distinctive recommendation problem: success is defined by the listener's affective state, but online experimentation on emotion is ethically constrained, particularly for clinical populations who cannot reliably skip a song or report distress. We describe AMRS, the Affective Music Recommendation System deployed on LUCID's health-and-wellness platforms, which serve clinical users (primarily older ...

</details>

---

### [LEIA: Learned Environment for Interactive Architected Materials](https://arxiv.org/abs/2605.28368v2)

**Authors:** Haiqian Yang, Yuan Cao, Markus J. Buehler

**Published:** 2026-05-27 | **Categories:** cs.LG, cond-mat.mtrl-sci, physics.app-ph

**Links:** [arXiv](https://arxiv.org/abs/2605.28368v2) | [PDF](https://arxiv.org/pdf/2605.28368v2.pdf)

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
