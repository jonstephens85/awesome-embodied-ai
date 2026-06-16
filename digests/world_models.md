# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-16 23:17 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046v1)

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An et al. (10 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17046v1) | [PDF](https://arxiv.org/pdf/2606.17046v1.pdf) | [Project Page](https://cvlab-kaist.github.io/Geometric-Action-Model/)

<details>
<summary>Abstract</summary>

Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action M...

</details>

---

### [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993v1)

**Authors:**  DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang et al. (23 authors)

**Published:** 2026-06-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.16993v1) | [PDF](https://arxiv.org/pdf/2606.16993v1.pdf) | [Project Page](https://amap-ml.github.io/DreamX_World) | [GitHub](https://github.com/AMAP-ML/DreamX-World)

<details>
<summary>Abstract</summary>

DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation. It supports camera navigation, revisits to previously observed regions, and promptable events across photorealistic, game-style, and stylized domains. Our data engine combines camera-accurate Unreal Engine rendering, action-rich gameplay recordings, and real-world videos with recovered camera geometry. For camera control, we introduce E-PRoPE, a lightweight variant of proje...

</details>

---

### [Medical world models: representing medical states, modelling clinical dynamics and guiding intervention policies](https://arxiv.org/abs/2606.16721v1)

**Authors:** Ke Liu, Mengxuan Li, Yanyi Bao, Tianyun Zhang, Chong Chu et al. (7 authors)

**Published:** 2026-06-15 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.16721v1) | [PDF](https://arxiv.org/pdf/2606.16721v1.pdf) | [GitHub](https://github.com/1999kevin/awesome_medical_world_models)

<details>
<summary>Abstract</summary>

Medical diagnosis and treatment are dynamic processes in which patient states evolve over time and clinical interventions alter future outcomes. Although current medical AI can detect disease, estimate risk and generate reports, many systems still return static labels or scores, offering limited insight into how illness may progress or how alternative interventions may reshape its trajectory. Medical world models adapt the world-model idea from artificial intelligence to healthcare by learning i...

</details>

---

### [ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control](https://arxiv.org/abs/2606.16605v1)

**Authors:** Junjian Zhang, Hao Tan, Ruonan Li, Dong Zhu, Aiping Li et al. (6 authors)

**Published:** 2026-06-15 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.16605v1) | [PDF](https://arxiv.org/pdf/2606.16605v1.pdf) | [GitHub](https://github.com/zaoanguai/ARB4WM)

<details>
<summary>Abstract</summary>

World models are widely used in robotic and agentic engineering control systems due to their ability to learn latent dynamics for planning and decision-making. As these systems are increasingly deployed in safety-critical settings, understanding their robustness under adversarial conditions has become essential. However, existing evaluations lack a unified benchmark for testing adversarial threats across the policy, value, and latent-dynamics levels of world-model agents. To fill this gap, we pr...

</details>

---

### [BadWorld: Adversarial Attacks on World Models](https://arxiv.org/abs/2606.16519v1)

**Authors:** Linghui Shen, Mingyue Cui, Xingyi Yang

**Published:** 2026-06-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.16519v1) | [PDF](https://arxiv.org/pdf/2606.16519v1.pdf) | [Project Page](https://linghuiishen.github.io/BadWorld/)

<details>
<summary>Abstract</summary>

Visual world models (VWMs) synthesize interactive, action-conditioned rollouts from a single context image. However, it remains an open question how robust these models are to adversarial perturbations. Standard adversarial attacks fail to assess this vulnerability because attackers lack ground-truth future videos and cannot predict subsequent user controls. We introduce BadWorld, a label-free adversarial framework tailored for autoregressive VWMs that systematically overcomes both constraints. ...

</details>

---

## Other Recent Papers

### [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030v1)

**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, Chenxu Lv, Deqing Li et al. (38 authors)

**Published:** 2026-06-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17030v1) | [PDF](https://arxiv.org/pdf/2606.17030v1.pdf)

<details>
<summary>Abstract</summary>

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for...

</details>

---

### [Kairos: A Native World Model Stack for Physical AI](https://arxiv.org/abs/2606.16533v1)

**Authors:**  Kairos Team, Fei Wang, Shan You, Qiming Zhang, Tao Huang et al. (23 authors)

**Published:** 2026-06-15 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.16533v1) | [PDF](https://arxiv.org/pdf/2606.16533v1.pdf)

<details>
<summary>Abstract</summary>

World models are transitioning from passive visual generators to foundational, operational infrastructure for Physical AI: they must natively acquire world knowledge from heterogeneous experience, maintain persistent states over long horizons, and execute efficiently within real deployment constraints. We introduce Kairos, a native world model stack designed around these requirements. (1) Kairos learns the world by pioneering a Native Pre-training Paradigm governed by a Cross-Embodiment Data Cur...

</details>

---

### [BRICKS-WM: Building Reusability via Interface Composition Kinetics for Structured World Models](https://arxiv.org/abs/2606.16489v1)

**Authors:** Shaowei Zhang, Jiahan Cao, Xunlan Zhou, Shenghua Wan, De-Chuan Zhan

**Published:** 2026-06-15 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.16489v1) | [PDF](https://arxiv.org/pdf/2606.16489v1.pdf)

<details>
<summary>Abstract</summary>

Model-based Reinforcement Learning (MBRL) has achieved remarkable success in continuous control by leveraging latent world models. However, prevailing approaches typically rely on monolithic latent dynamics, entangling environment dynamics into a coupled process. This coupling severely limits reusability: altering the agent necessitates retraining the entire world from scratch, even if the environment remains constant. To address this, we introduce BRICKS-WM (Building Reusability via Interface C...

</details>

---

### [HOLO-MPPI: Multi-Scenario Motion Planning via Hierarchical Policy Optimization](https://arxiv.org/abs/2606.16480v1)

**Authors:** Youngjae Min, Jovin D'sa, Faizan M. Tariq, David Isele, Navid Azizan et al. (6 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2606.16480v1) | [PDF](https://arxiv.org/pdf/2606.16480v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in the real world must plan motions across diverse scenarios without per-scenario retuning. End-to-end reinforcement learning (RL) can generalize across scenarios but often becomes brittle under distribution shift, reward misspecification, and stochastic interactions. Model predictive path integral (MPPI) control enables strong real-time refinement without gradients, but its performance depends on a well-shaped sampling prior, while manually designing the priors does not scale to...

</details>

---

### [FlowMPC: Improving Flow Matching policies with World Models](https://arxiv.org/abs/2606.16286v1)

**Authors:** Chandon Hamel

**Published:** 2026-06-15 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.16286v1) | [PDF](https://arxiv.org/pdf/2606.16286v1.pdf)

<details>
<summary>Abstract</summary>

Flow Matching (FM) is a powerful approach for behavior cloning in multimodal action spaces [Jiang et al., 2025], but because it is not trained to directly maximize expected return, there is still room to improve how FM policies act at test time. This work investigates whether a learned world model can improve FM policies by enabling Model Predictive Path Integral (MPPI) planning over candidate action sequences proposed by the policy. Building on TD-MPC2 [Hansen et al., 2024], I introduce FlowMPC...

</details>

---

### [GraphWorld: Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274v1)

**Authors:** Ziying Song, Caiyan Jia, Lin Liu, Lei Yang, Shengkai Zhang et al. (11 authors)

**Published:** 2026-06-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.16274v1) | [PDF](https://arxiv.org/pdf/2606.16274v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has made significant progress by unifying perception, prediction, and planning within a single learning framework, achieving strong performance in short-horizon decision making. However, most existing E2E-AD methods remain confined to short-horizon planning and lack the ability to model long-term temporal dependencies, which severely limits their generalization and security in complex and highly interactive driving scenarios. In this work, we propose GraphWorld, an ...

</details>

---

### [Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting](https://arxiv.org/abs/2606.16076v1)

**Authors:** Weizhi Nie, Weichao Liu, Honglin Guo, Yuting Su

**Published:** 2026-06-15 | **Categories:** cs.LG, cs.AI, cs.GT

**Links:** [arXiv](https://arxiv.org/abs/2606.16076v1) | [PDF](https://arxiv.org/pdf/2606.16076v1.pdf)

<details>
<summary>Abstract</summary>

Multivariate forecasting in physical systems requires models that predict coupled temporal variables while preserving meaningful state evolution. Deep forecasters can fit temporal correlations, and physics-informed models can regularize predictions with scientific constraints, but these directions are often connected only at the decoded-output level. As a result, the hidden predictive state that generates future trajectories may remain statistically useful but physically unstructured. We introdu...

</details>

---

### [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070v1)

**Authors:** Yifei Dong, Mingen Zheng, Linquan Wu, Jeff Z. Pan, Jiaxin Bai

**Published:** 2026-06-14 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.16070v1) | [PDF](https://arxiv.org/pdf/2606.16070v1.pdf)

<details>
<summary>Abstract</summary>

World-model synthesis aims to turn interaction experience into an internal model of environment dynamics. Existing symbolic approaches often fit observed transitions or mixtures of local rules, but they do not produce a complete executable program that can run independently of the real environment. We present Mind-Studio, a framework that synthesizes executable pygame-style world models from state-action-next-state trajectories using large language models. Mind-Studio combines entropy-selected t...

</details>

---

### [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768v1)

**Authors:** Jialei Chen, Kai Wang, Kang Chen, Shuaihang Chen, Feng Gao et al. (12 authors)

**Published:** 2026-06-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.15768v1) | [PDF](https://arxiv.org/pdf/2606.15768v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) leverage large-scale vision-language pretraining for semantic robot control, but often lack explicit foresight into how robot actions change the scene. World-Action Models (WAMs) address this limitation by conditioning policies on predicted futures, yet existing approaches typically rely on computationally expensive video generation with substantial pixel-level redundancy. We present LaWAM, a Latent World Action Model that exposes predictive dynamics to robot...

</details>

---

### [Pixels to Proofs: Probabilistically-Safe Latent World Model Control via Parallel Conformal Robust MPC](https://arxiv.org/abs/2606.15594v1)

**Authors:** Devesh Nath, Anutam Srinivasan, Haoran Yin, Ruitong Jiang, Jeffrey Fang et al. (6 authors)

**Published:** 2026-06-14 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.15594v1) | [PDF](https://arxiv.org/pdf/2606.15594v1.pdf)

<details>
<summary>Abstract</summary>

We present SLS^2, a framework for safe feedback motion planning from pixels using robust model predictive control (MPC) in learned latent world models. Our approach trains an action-conditioned joint-embedding world model with compact Markovian latent states, enabling efficient gradient-based trajectory optimization through learned latent dynamics. To enforce safety for the true system despite imperfect latent predictions, we inform a GPU-accelerated system level synthesis (SLS) robust MPC schem...

</details>

---
