# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-22 17:01 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)

**Authors:** Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge et al. (6 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19734v1) | [PDF](https://arxiv.org/pdf/2604.19734v1.pdf) | [Project Page](https://xpeng-robotics.github.io/unit/)

<details>
<summary>Abstract</summary>

Scaling humanoid foundation models is bottlenecked by the scarcity of robotic data. While massive egocentric human data offers a scalable alternative, bridging the cross-embodiment chasm remains a fundamental challenge due to kinematic mismatches. We introduce UniT (Unified Latent Action Tokenizer via Visual Anchoring), a framework that establishes a unified physical language for human-to-humanoid transfer. Grounded in the philosophy that heterogeneous kinematics share universal visual consequen...

</details>

---

### [MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)

**Authors:** Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu

**Published:** 2026-04-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.18564v2) | [PDF](https://arxiv.org/pdf/2604.18564v2.pdf) | [Project Page](https://multi-world.github.io/)

<details>
<summary>Abstract</summary>

Video world models have achieved remarkable success in simulating environmental dynamics in response to actions by users or agents. They are modeled as action-conditioned video generation models that take historical frames and current actions as input to predict future frames. Yet, most existing approaches are limited to single-agent scenarios and fail to capture the complex interactions inherent in real-world multi-agent systems. We present \textbf{MultiWorld}, a unified framework for multi-age...

</details>

---

### [OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486v1)

**Authors:** Jinghui Lu, Jiayi Guan, Zhijian Huang, Jinlong Li, Guang Li et al. (50 authors)

**Published:** 2026-04-20 | **Categories:** cs.CV, cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.18486v1) | [PDF](https://arxiv.org/pdf/2604.18486v1.pdf) | [Project Page](https://xiaomi-embodied-intelligence.github.io/OneVL)

<details>
<summary>Abstract</summary>

Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world,...

</details>

---

## Other Recent Papers

### [Mask World Model: Predicting What Matters for Robust Robot Policy Learning](https://arxiv.org/abs/2604.19683v1)

**Authors:** Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li et al. (12 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.19683v1) | [PDF](https://arxiv.org/pdf/2604.19683v1.pdf)

<details>
<summary>Abstract</summary>

World models derived from large-scale video generative pre-training have emerged as a promising paradigm for generalist robot policy learning. However, standard approaches often focus on high-fidelity RGB video prediction, this can result in overfitting to irrelevant factors, such as dynamic backgrounds and illumination changes. These distractions reduce the model's ability to generalize, ultimately leading to unreliable and fragile control policies. To address this, we introduce the Mask World ...

</details>

---

### [Safety-Critical Contextual Control via Online Riemannian Optimization with World Models](https://arxiv.org/abs/2604.19639v1)

**Authors:** Tongxin Li

**Published:** 2026-04-21 | **Categories:** eess.SY, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19639v1) | [PDF](https://arxiv.org/pdf/2604.19639v1.pdf)

<details>
<summary>Abstract</summary>

Modern world models are becoming too complex to admit explicit dynamical descriptions. We study safety-critical contextual control, where a Planner must optimize a task objective using only feasibility samples from a black-box Simulator, conditioned on a context signal $ξ_t$. We develop a sample-based Penalized Predictive Control (PPC) framework grounded in online Riemannian optimization, in which the Simulator compresses the feasibility manifold into a score-based density $\hat{p}(u \mid ξ_t)$ ...

</details>

---

### [LASER: Learning Active Sensing for Continuum Field Reconstruction](https://arxiv.org/abs/2604.19355v1)

**Authors:** Huayu Deng, Jinghui Zhong, Xiangming Zhu, Yunbo Wang, Xiaokang Yang

**Published:** 2026-04-21 | **Categories:** cs.LG, cs.AI, cs.CE

**Links:** [arXiv](https://arxiv.org/abs/2604.19355v1) | [PDF](https://arxiv.org/pdf/2604.19355v1.pdf)

<details>
<summary>Abstract</summary>

High-fidelity measurements of continuum physical fields are essential for scientific discovery and engineering design but remain challenging under sparse and constrained sensing. Conventional reconstruction methods typically rely on fixed sensor layouts, which cannot adapt to evolving physical states. We propose LASER, a unified, closed-loop framework that formulates active sensing as a Partially Observable Markov Decision Process (POMDP). At its core, LASER employs a continuum field latent worl...

</details>

---

### [RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)

**Authors:** Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang et al. (11 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19092v1) | [PDF](https://arxiv.org/pdf/2604.19092v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in large-scale video world models have enabled increasingly realistic future prediction, raising the prospect of leveraging imagined videos for robot learning. However, visual realism does not imply physical plausibility, and behaviors inferred from generated videos may violate dynamics and fail when executed by embodied agents. Existing benchmarks begin to incorporate notions of physical plausibility, but they largely remain perception- or diagnostic-oriented and do not systemat...

</details>

---

### [Curiosity-Critic: Cumulative Prediction Error Improvement as a Tractable Intrinsic Reward for World Model Training](https://arxiv.org/abs/2604.18701v1)

**Authors:** Vin Bhaskara, Haicheng Wang

**Published:** 2026-04-20 | **Categories:** cs.LG, cs.AI, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2604.18701v1) | [PDF](https://arxiv.org/pdf/2604.18701v1.pdf)

<details>
<summary>Abstract</summary>

Local prediction-error-based curiosity rewards focus on the current transition without considering the world model's cumulative prediction error across all visited transitions. We introduce Curiosity-Critic, which grounds its intrinsic reward in the improvement of this cumulative objective, and show that it reduces to a tractable per-step form: the difference between the current prediction error and the asymptotic error baseline of the current state transition. We estimate this baseline online w...

</details>

---

### [Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity](https://arxiv.org/abs/2604.18058v1)

**Authors:** Blaise Delaney, Salil Patel, Yuji Xing, Dominic Dootson, Karin Sevegnani

**Published:** 2026-04-20 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.18058v1) | [PDF](https://arxiv.org/pdf/2604.18058v1.pdf)

<details>
<summary>Abstract</summary>

We introduce Sonata, a compact latent world model for six-axis trunk IMU representation learning under clinical data scarcity. Clinical cohorts typically comprise tens to hundreds of patients, making web-scale masked-reconstruction objectives poorly matched to the problem. Sonata is a 3.77 M-parameter hybrid model, pre-trained on a harmonised corpus of nine public datasets (739 subjects, 190k windows) with a latent world-model objective that predicts future state rather than reconstructing raw s...

</details>

---

### [The Umwelt Representation Hypothesis: Rethinking Universality](https://arxiv.org/abs/2604.17960v1)

**Authors:** Victoria Bosch, Rowan Sommers, Adrien Doerig, Tim C Kietzmann

**Published:** 2026-04-20 | **Categories:** q-bio.NC, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.17960v1) | [PDF](https://arxiv.org/pdf/2604.17960v1.pdf)

<details>
<summary>Abstract</summary>

Recent studies reveal striking representational alignment between artificial neural networks (ANNs) and biological brains, leading to proposals that all sufficiently capable systems converge on universal representations of reality. Here, we argue that this claim of Universality is premature. We introduce the Umwelt Representation Hypothesis (URH), proposing that alignment arises not from convergence toward a single global optimum, but from overlap in ecological constraints under which systems de...

</details>

---

### [Scaling Human-AI Coding Collaboration Requires a Governable Consensus Layer](https://arxiv.org/abs/2604.17883v1)

**Authors:** Tianfu Wang, Zhezheng Hao, Yin Wu, Wei Wu, Qiang Lin et al. (8 authors)

**Published:** 2026-04-20 | **Categories:** cs.SE, cs.HC, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.17883v1) | [PDF](https://arxiv.org/pdf/2604.17883v1.pdf)

<details>
<summary>Abstract</summary>

Vibe coding produces correct, executable code at speed, but leaves no record of the structural commitments, dependencies, or evidence behind it. Reviewers cannot determine what invariants were assumed, what changed, or why a regression occurred. This is not a generation failure but a control failure: the dominant artifact of AI-assisted development (code plus chat history) performs dimension collapse, flattening complex system topology into low-dimensional text and making systems opaque and frag...

</details>

---
