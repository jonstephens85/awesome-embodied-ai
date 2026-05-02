# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-02 22:30 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196v1)

**Authors:** Xin Zhou, Dingkang Liang, Xiwu Chen, Feiyang Tan, Dingyuan Zhang et al. (7 authors)

**Published:** 2026-04-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.28196v1) | [PDF](https://arxiv.org/pdf/2604.28196v1.pdf) | [Project Page](https://h-embodvis.github.io/HERMESV2/) | [GitHub](https://github.com/H-EmbodVis/HERMESV2)

<details>
<summary>Abstract</summary>

Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics. However, existing approaches predominantly focus on future scene generation, often overlooking comprehensive 3D scene understanding. Conversely, while Large Language Models (LLMs) demonstrate impressive reasoning capabilities, they lack the capacity to predict future geometric evolution, creating a significant disparity between semantic interpretation and physical simulation. To bridge...

</details>

---

### [Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling](https://arxiv.org/abs/2604.28185v1)

**Authors:** Keming Wu, Zuhao Yang, Kaichen Zhang, Shizun Wang, Haowei Zhu et al. (27 authors)

**Published:** 2026-04-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.28185v1) | [PDF](https://arxiv.org/pdf/2604.28185v1.pdf) | [GitHub](https://github.com/EvolvingLMMs-Lab/Evolving-Visual-Generation)

<details>
<summary>Abstract</summary>

Recent visual generation models have made major progress in photorealism, typography, instruction following, and interactive editing, yet they still struggle with spatial reasoning, persistent state, long-horizon consistency, and causal understanding. We argue that the field should move beyond appearance synthesis toward intelligent visual generation: plausible visuals grounded in structure, dynamics, domain knowledge, and causal relations. To frame this shift, we introduce a five-level taxonomy...

</details>

---

### [GUI Agents with Reinforcement Learning: Toward Digital Inhabitants](https://arxiv.org/abs/2604.27955v1)

**Authors:** Junan Hu, Jian Liu, Jingxiang Lai, Jiarui Hu, Yiwei Sheng et al. (9 authors)

**Published:** 2026-04-30 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.27955v1) | [PDF](https://arxiv.org/pdf/2604.27955v1.pdf) | [GitHub](https://github.com/Steve2457/Awesome-RL-GUI-Agents)

<details>
<summary>Abstract</summary>

Graphical User Interface (GUI) agents have emerged as a promising paradigm for intelligent systems that perceive and interact with graphical interfaces visually. Yet supervised fine-tuning alone cannot handle long-horizon credit assignment, distribution shifts, and safe exploration in irreversible environments, making Reinforcement Learning (RL) a central methodology for advancing automation. In this work, we present the first comprehensive overview of the intersection between RL and GUI agents,...

</details>

---

### [LA-Pose: Latent Action Pretraining Meets Pose Estimation](https://arxiv.org/abs/2604.27448v1)

**Authors:** Zhengqing Wang, Saurabh Nair, Prajwal Chidananda, Pujith Kachana, Samuel Li et al. (7 authors)

**Published:** 2026-04-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.27448v1) | [PDF](https://arxiv.org/pdf/2604.27448v1.pdf) | [Project Page](https://la-pose.github.io/)

<details>
<summary>Abstract</summary>

This paper revisits camera pose estimation through the lens of self-supervised pretraining, focusing on inverse-dynamics pretraining as a scalable alternative to the current trend of fully supervised training with 3D annotations. Concretely, we employ inverse- and forward-dynamics models to learn latent action representations, similar to Genie from large-scale driving videos. Our idea is simple yet effective. Existing methods use latent actions in their original capacity, that is, as action cond...

</details>

---

## Other Recent Papers

### [LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models](https://arxiv.org/abs/2604.28192v1)

**Authors:** Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang et al. (14 authors)

**Published:** 2026-04-30 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.28192v1) | [PDF](https://arxiv.org/pdf/2604.28192v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have increasingly incorporated reasoning mechanisms for complex robotic manipulation. However, existing approaches share a critical limitation: whether employing explicit linguistic reasoning that suffers from latency and discretization, or utilizing more expressive continuous latent reasoning, they are predominantly confined to static imitation learning that limits adaptability and generalization. While online reinforcement learning (RL) has been introduced t...

</details>

---

### [Beyond Gaussian Bottlenecks: Topologically Aligned Encoding of Vision-Transformer Feature Spaces](https://arxiv.org/abs/2604.28122v1)

**Authors:** Andrew Bond, Ilkin Umut Melanlioglu, Erkut Erdem, Aykut Erdem

**Published:** 2026-04-30 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.28122v1) | [PDF](https://arxiv.org/pdf/2604.28122v1.pdf)

<details>
<summary>Abstract</summary>

Modern visual world modeling systems increasingly rely on high-capacity architectures and large-scale data to produce plausible motion, yet they often fail to preserve underlying 3D geometry or physically consistent camera dynamics. A key limitation lies not only in model capacity, but in the latent representations used to encode geometric structure. We propose S$^2$VAE, a geometry-first latent learning framework that focuses on compressing and representing the latent 3D state of a scene, includ...

</details>

---

### [Dreaming Across Towns: Semantic Rollout and Town-Adversarial Regularization for Zero-Shot Held-Out-Town Fixed-Route Driving in CARLA](https://arxiv.org/abs/2604.27994v1)

**Authors:** Feeza Khan Khanzada, Jaerock Kwon

**Published:** 2026-04-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.27994v1) | [PDF](https://arxiv.org/pdf/2604.27994v1.pdf)

<details>
<summary>Abstract</summary>

Learned driving agents often degrade when deployed in unseen environments. This paper studies a deliberately bounded instance of that problem in the CARLA simulator: zero-shot transfer of a closed-loop fixed-route driving agent from Town05 and Town06 to unseen Town03 and Town04. The study isolates structural town shift by keeping weather fixed to ClearNoon and removing traffic and pedestrians. We build on a Dreamer-style latent world-model agent and add two training-only auxiliary losses: multi-...

</details>

---

### [Flying by Inference: Active Inference World Models for Adaptive UAV Swarms](https://arxiv.org/abs/2604.27935v1)

**Authors:** Kaleem Arshid, Ali Krayani, Lucio Marcenaro, David Martin Gomez, Carlo Regazzoni

**Published:** 2026-04-30 | **Categories:** cs.RO, eess.SP, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2604.27935v1) | [PDF](https://arxiv.org/pdf/2604.27935v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents an expert-guided active-inference-inspired framework for adaptive UAV swarm trajectory planning. The proposed method converts multi-UAV trajectory design from a repeated combinatorial optimization problem into a hierarchical probabilistic inference problem. In the offline phase, a genetic-algorithm planner with repulsive-force collision avoidance (GA--RF) generates expert demonstrations, which are abstracted into Mission, Route, and Motion dictionaries. These dictionaries are...

</details>

---

### [Simulating clinical interventions with a generative multimodal model of human physiology](https://arxiv.org/abs/2604.27899v1)

**Authors:** Guy Lutsker, Gal Sapir, Jordi Merino, Smadar Shilo, Anastasia Godneva et al. (10 authors)

**Published:** 2026-04-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.27899v1) | [PDF](https://arxiv.org/pdf/2604.27899v1.pdf)

<details>
<summary>Abstract</summary>

Understanding how human health changes over time, and why responses to interventions vary between individuals, remains a central challenge in medicine. Here we present HealthFormer, a decoder-only transformer that models the human physiological trajectory generatively, by training on data from the Human Phenotype Project, a multi-visit cohort of over 15,000 deeply phenotyped individuals. We tokenise each participant's health trajectory across 667 measurements spanning seven domains: blood biomar...

</details>

---

### [Graph World Models: Concepts, Taxonomy, and Future Directions](https://arxiv.org/abs/2604.27895v1)

**Authors:** Jiawei Liu, Senqiao Yang, Mingjun Wang, Yu Wang, Bei Yu

**Published:** 2026-04-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.27895v1) | [PDF](https://arxiv.org/pdf/2604.27895v1.pdf)

<details>
<summary>Abstract</summary>

As one of the mainstream models of artificial intelligence, world models allow agents to learn the representation of the environment for efficient prediction and planning. However, classical world models based on flat tensors face several key problems, including noise sensitivity, error accumulation and weak reasoning. To address these limitations, many recent studies use graph structure to decompose the environment into entity nodes and interactive edges, and model virtual environments in a str...

</details>

---

### [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792v1)

**Authors:**  MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan et al. (20 authors)

**Published:** 2026-04-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.27792v1) | [PDF](https://arxiv.org/pdf/2604.27792v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong semantic generalization but often lack fine-grained modeling of world dynamics. Recent work explores video generation models as a foundation for world modeling, leading to unified World Action Models (WAMs) that jointly model visual dynamics and actions. We present MotuBrain, a unified multimodal generative model that jointly models video and action under a UniDiffuser formulation with a three-stream Mixture-of-Transformers architecture. A singl...

</details>

---

### [BAss: Symbolic Reasoning in Abstract Dialectical Frameworks](https://arxiv.org/abs/2604.27576v1)

**Authors:** Samuel Pastva, Van-Giang Trinh

**Published:** 2026-04-30 | **Categories:** cs.LO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.27576v1) | [PDF](https://arxiv.org/pdf/2604.27576v1.pdf)

<details>
<summary>Abstract</summary>

We present BAss (BDD-based ADF symbolic solver), a novel analysis tool for Abstract Dialectical Frameworks (ADFs) based on Binary Decision Diagrams (BDDs). It supports the fully symbolic computation of all admissible, complete, and preferred interpretations, as well as two-valued and stable models of an ADFs. Our approach is inspired by the recently discovered equivalence between Boolean Networks (BNs) and ADFs by Heyninck et al. (2024) and Azpeitia et al. (2024), significantly extending current...

</details>

---
