# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-17 18:15 UTC

**Papers found:** 21

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/abs/2606.18250v1)

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab et al. (7 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18250v1) | [PDF](https://arxiv.org/pdf/2606.18250v1.pdf) | [Project Page](https://fr3d-wm.github.io)

<details>
<summary>Abstract</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. U...

</details>

---

### [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/abs/2606.17730v1)

**Authors:** Zhexiao Xiong, Yizhi Song, Hao Kang, Qing Yan, Liming Jiang et al. (14 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17730v1) | [PDF](https://arxiv.org/pdf/2606.17730v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable...

</details>

---

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

### [Looped World Models](https://arxiv.org/abs/2606.18208v1)

**Authors:** Hongyuan Adam Lu, Z. L. Victor Wei, Qun Zhang, Jinrui Zeng, Bowen Cao et al. (31 authors)

**Published:** 2026-06-16 | **Categories:** cs.LG, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.18208v1) | [PDF](https://arxiv.org/pdf/2606.18208v1.pdf)

<details>
<summary>Abstract</summary>

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive compu...

</details>

---

### [EgoCS-400K: An Egocentric Gameplay Dataset for World Models](https://arxiv.org/abs/2606.18180v1)

**Authors:** Rongjin Guo, Dong Liang, Yuhao Liu, Fang Liu, Tianyu Huang et al. (7 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18180v1) | [PDF](https://arxiv.org/pdf/2606.18180v1.pdf)

<details>
<summary>Abstract</summary>

The shift from video generation to interactive world modeling places new demands on data: beyond captioned videos, world models require temporally aligned video-action-language trajectories grounded in the actions, camera motion, states, and events that drive future scene changes. However, such data is difficult to obtain at scale. Web video datasets offer broad visual coverage but lack executable actions and reliable states; robotic datasets provide action and state supervision but are costly a...

</details>

---

### [PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space](https://arxiv.org/abs/2606.17924v1)

**Authors:** Bochen Yang, Lianlei Shan

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17924v1) | [PDF](https://arxiv.org/pdf/2606.17924v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model...

</details>

---

### [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906v1)

**Authors:** Zezhong Qian, Xiaowei Chi, Yu Qi, Haozhan Li, Zhi Yang Chen et al. (6 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17906v1) | [PDF](https://arxiv.org/pdf/2606.17906v1.pdf)

<details>
<summary>Abstract</summary>

Recent World-Action (WA) models demonstrate strong generalization ability and data efficiency, but they typically rely on expert trajectories for training. This reliance limits their ability to acquire fine-grained manipulation skills beyond the demonstration distribution and prevents them from continuously improving through real-world interaction. To address these limitations, we propose WAM-RL, a reinforcement learning framework that enables joint optimization of the world model and the action...

</details>

---

### [MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model](https://arxiv.org/abs/2606.17800v1)

**Authors:** Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong et al. (17 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17800v1) | [PDF](https://arxiv.org/pdf/2606.17800v1.pdf)

<details>
<summary>Abstract</summary>

As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies. In this work, we define the position of social world models and build a prototype model as the first step towards this goal. While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric...

</details>

---

### [OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation](https://arxiv.org/abs/2606.17536v1)

**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu et al. (11 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17536v1) | [PDF](https://arxiv.org/pdf/2606.17536v1.pdf)

<details>
<summary>Abstract</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-c...

</details>

---

### [NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama](https://arxiv.org/abs/2606.17391v1)

**Authors:** Logan Mann, Abdur Rahman, Mohammad Saifullah, Taaha Kazi, Vasu Sharma

**Published:** 2026-06-16 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17391v1) | [PDF](https://arxiv.org/pdf/2606.17391v1.pdf)

<details>
<summary>Abstract</summary>

Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open b...

</details>

---

### [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030v2)

**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, Deqing Li, Gengze Zhou et al. (38 authors)

**Published:** 2026-06-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17030v2) | [PDF](https://arxiv.org/pdf/2606.17030v2.pdf)

<details>
<summary>Abstract</summary>

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for...

</details>

---

### [Kairos: A Native World Model Stack for Physical AI](https://arxiv.org/abs/2606.16533v2)

**Authors:**  Kairos Team, Fei Wang, Shan You, Qiming Zhang, Tao Huang et al. (24 authors)

**Published:** 2026-06-15 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.16533v2) | [PDF](https://arxiv.org/pdf/2606.16533v2.pdf)

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
