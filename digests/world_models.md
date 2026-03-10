# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-10 16:56 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.08572v1)

**Authors:** Yutong Shen, Hangxu Liu, Penghui Liu, Jiashuo Luo, Yongkang Zhang et al. (9 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.08572v1) | [PDF](https://arxiv.org/pdf/2603.08572v1.pdf) | [Project Page](https://syt2004.github.io/metaworldX/)

<details>
<summary>Abstract</summary>

Learning natural, stable, and compositionally generalizable whole-body control policies for humanoid robots performing simultaneous locomotion and manipulation (loco-manipulation) remains a fundamental challenge in robotics. Existing reinforcement learning approaches typically rely on a single monolithic policy to acquire multiple skills, which often leads to cross-skill gradient interference and motion pattern conflicts in high-degree-of-freedom systems. As a result, generated behaviors frequen...

</details>

---

### [Interactive World Simulator for Robot Policy Training and Evaluation](https://arxiv.org/abs/2603.08546v1)

**Authors:** Yixuan Wang, Rhythm Syed, Fangyu Wu, Mengchao Zhang, Aykut Onol et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08546v1) | [PDF](https://arxiv.org/pdf/2603.08546v1.pdf) | [Project Page](https://yixuanwang.me/interactive_world_sim)

<details>
<summary>Abstract</summary>

Action-conditioned video prediction models (often referred to as world models) have shown strong potential for robotics applications, but existing approaches are often slow and struggle to capture physically consistent interactions over long horizons, limiting their usefulness for scalable robot policy training and evaluation. We present Interactive World Simulator, a framework for building interactive world models from a moderate-sized robot interaction dataset. Our approach leverages consisten...

</details>

---

### [MWM: Mobile World Models for Action-Conditioned Consistent Prediction](https://arxiv.org/abs/2603.07799v1)

**Authors:** Han Yan, Zishang Xiang, Zeyu Zhang, Hao Tang

**Published:** 2026-03-08 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.07799v1) | [PDF](https://arxiv.org/pdf/2603.07799v1.pdf) | [Project Page](https://aigeeksgroup.github.io/MWM) | [GitHub](https://github.com/AIGeeksGroup/MWM)

<details>
<summary>Abstract</summary>

World models enable planning in imagined future predicted space, offering a promising framework for embodied navigation. However, existing navigation world models often lack action-conditioned consistency, so visually plausible predictions can still drift under multi-step rollout and degrade planning. Moreover, efficient deployment requires few-step diffusion inference, but existing distillation methods do not explicitly preserve rollout consistency, creating a training-inference mismatch. To ad...

</details>

---

### [Brain-WM: Brain Glioblastoma World Model](https://arxiv.org/abs/2603.07562v1)

**Authors:** Chenhui Wang, Boyun Zheng, Liuxin Bao, Zhihao Peng, Peter Y. M. Woo et al. (7 authors)

**Published:** 2026-03-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.07562v1) | [PDF](https://arxiv.org/pdf/2603.07562v1.pdf) | [GitHub](https://github.com/thibault-wch/Brain-GBM-world-model)

<details>
<summary>Abstract</summary>

Precise prognostic modeling of glioblastoma (GBM) under varying treatment interventions is essential for optimizing clinical outcomes. While generative AI has shown promise in simulating GBM evolution, existing methods typically treat interventions as static conditional inputs rather than dynamic decision variables. Consequently, they fail to capture the complex, reciprocal interplay between tumor evolution and treatment response. To bridge this gap, we present Brain-WM, a pioneering brain GBM w...

</details>

---

## Other Recent Papers

### [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519v1)

**Authors:** Xiaoquan Sun, Zetian Xu, Chen Cao, Zonghe Liu, Yihan Sun et al. (12 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.08519v1) | [PDF](https://arxiv.org/pdf/2603.08519v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate remarkable potential for generalizable robotic manipulation. The execution of complex multi-step behaviors in VLA models can be improved by robust instruction grounding, a critical component for effective control. However, current paradigms predominantly rely on coarse, high-level task instructions during supervised fine-tuning. This instruction grounding gap leaves models without explicit intermediate guidance, leading to severe compounding errors...

</details>

---

### [The Boiling Frog Threshold: Criticality and Blindness in World Model-Based Anomaly Detection Under Gradual Drift](https://arxiv.org/abs/2603.08455v1)

**Authors:** Zhe Hong

**Published:** 2026-03-09 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.08455v1) | [PDF](https://arxiv.org/pdf/2603.08455v1.pdf)

<details>
<summary>Abstract</summary>

When an RL agent's observations are gradually corrupted, at what drift rate does it "wake up" -- and what determines this boundary? We study world model-based self-monitoring under continuous observation drift across four MuJoCo environments, three detector families (z-score, variance, percentile), and three model capacities. We find that (1) a sharp detection threshold $\varepsilon^*$ exists universally: below it, drift is absorbed as normal variation; above it, detection occurs rapidly. The th...

</details>

---

### [SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v1)

**Authors:** Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang et al. (13 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08403v1) | [PDF](https://arxiv.org/pdf/2603.08403v1.pdf)

<details>
<summary>Abstract</summary>

We introduce SPIRAL, a self-improving planning and iterative reflective action world modeling closed-loop framework that enables controllable long-horizon video generation conditioned on high-level semantic actions. Existing one-shot video generation models operate in open-loop, often resulting in incomplete action execution, weak semantic grounding, and temporal drift. SPIRAL formulates ActWM as a closed-loop think-act-reflect process, where generation proceeds step by step under explicit plann...

</details>

---

### [SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving](https://arxiv.org/abs/2603.08113v1)

**Authors:** Zihan You, Hongwei Liu, Chenxu Dang, Zhe Wang, Sining Ang et al. (7 authors)

**Published:** 2026-03-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.08113v1) | [PDF](https://arxiv.org/pdf/2603.08113v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have shown promising capabilities in autonomous driving by leveraging the understanding and reasoning strengths of Large Language Models(LLMs).However, our empirical analysis reveals that directly applying existing token-level MoE mechanisms--which are inherited from LLM architectures--to VLA models results in unstable performance and safety degradation in autonomous driving, highlighting a misalignment between token-based expert specializat...

</details>

---

### [Long-Short Term Agents for Pure-Vision Bronchoscopy Robotic Autonomy](https://arxiv.org/abs/2603.07909v1)

**Authors:** Junyang Wu, Mingyi Luo, Fangfang Xie, Minghui Zhang, Hanxiao Zhang et al. (10 authors)

**Published:** 2026-03-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.07909v1) | [PDF](https://arxiv.org/pdf/2603.07909v1.pdf)

<details>
<summary>Abstract</summary>

Accurate intraoperative navigation is essential for robot-assisted endoluminal intervention, but remains difficult because of limited endoscopic field of view and dynamic artifacts. Existing navigation platforms often rely on external localization technologies, such as electromagnetic tracking or shape sensing, which increase hardware complexity and remain vulnerable to intraoperative anatomical mismatch. We present a vision-only autonomy framework that performs long-horizon bronchoscopic naviga...

</details>

---

### [DreamSAC: Learning Hamiltonian World Models via Symmetry Exploration](https://arxiv.org/abs/2603.07545v1)

**Authors:** Jinzhou Tang, Fan Feng, Minghao Fu, Wenjun Lin, Biwei Huang et al. (6 authors)

**Published:** 2026-03-08 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.07545v1) | [PDF](https://arxiv.org/pdf/2603.07545v1.pdf)

<details>
<summary>Abstract</summary>

Learned world models excel at interpolative generalization but fail at extrapolative generalization to novel physical properties. This limitation arises because they learn statistical correlations rather than the environment's underlying generative rules, such as physical invariances and conservation laws. We argue that learning these invariances is key to robust extrapolation. To achieve this, we first introduce \textbf{Symmetry Exploration}, an unsupervised exploration strategy where an agent ...

</details>

---

### [Underwater Embodied Intelligence for Autonomous Robots: A Constraint-Coupled Perspective on Planning, Control, and Deployment](https://arxiv.org/abs/2603.07393v1)

**Authors:** Jingzehua Xu, Guanwen Xie, Jiwei Tang, Shuai Zhang, Xiaofan Li

**Published:** 2026-03-08 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2603.07393v1) | [PDF](https://arxiv.org/pdf/2603.07393v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous underwater robots are increasingly deployed for environmental monitoring, infrastructure inspection, subsea resource exploration, and long-horizon exploration. Yet, despite rapid advances in learning-based planning and control, reliable autonomy in real ocean environments remains fundamentally constrained by tightly coupled physical limits. Hydrodynamic uncertainty, partial observability, bandwidth-limited communication, and energy scarcity are not independent challenges; they interac...

</details>

---
