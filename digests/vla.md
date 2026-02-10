# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-10 22:30 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](https://arxiv.org/abs/2602.09017v1)

**Authors:** Zichen Jeff Cui, Omar Rayyan, Haritheja Etukuru, Bowen Tan, Zavier Andrianarivo et al. (19 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.09017v1) | [PDF](https://arxiv.org/pdf/2602.09017v1.pdf) | [Project Page](https://cap-policy.github.io/)

<details>
<summary>Abstract</summary>

The prevalent paradigm in robot learning attempts to generalize across environments, embodiments, and tasks with language prompts at runtime. A fundamental tension limits this approach: language is often too abstract to guide the concrete physical understanding required for robust manipulation. In this work, we introduce Contact-Anchored Policies (CAP), which replace language conditioning with points of physical contact in space. Simultaneously, we structure CAP as a library of modular utility m...

</details>

---

### [SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios](https://arxiv.org/abs/2602.08440v1)

**Authors:** Tian Gao, Celine Tan, Catherine Glossop, Timothy Gao, Jiankai Sun et al. (11 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.08440v1) | [PDF](https://arxiv.org/pdf/2602.08440v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

A fundamental challenge in autonomous driving is the integration of high-level, semantic reasoning for long-tail events with low-level, reactive control for robust driving. While large vision-language models (VLMs) trained on web-scale data offer powerful common-sense reasoning, they lack the grounded experience necessary for safe vehicle control. We posit that an effective autonomous agent should leverage the world knowledge of VLMs to guide a steerable driving policy toward robust control in d...

</details>

---

### [Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning](https://arxiv.org/abs/2602.07845v1)

**Authors:** Yalcin Tur, Jalal Naghiyev, Haoquan Fang, Wei-Chuan Tsai, Jiafei Duan et al. (7 authors)

**Published:** 2026-02-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.07845v1) | [PDF](https://arxiv.org/pdf/2602.07845v1.pdf) | [Project Page](https://rd-vla.github.io/)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models rely on fixed computational depth, expending the same amount of compute on simple adjustments and complex multi-step manipulation. While Chain-of-Thought (CoT) prompting enables variable computation, it scales memory linearly and is ill-suited for continuous action spaces. We introduce Recurrent-Depth VLA (RD-VLA), an architecture that achieves computational adaptivity via latent iterative refinement rather than explicit token generation. RD-VLA employ...

</details>

---

## Other Recent Papers

### [TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation](https://arxiv.org/abs/2602.09023v1)

**Authors:** Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han et al. (14 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09023v1) | [PDF](https://arxiv.org/pdf/2602.09023v1.pdf)

<details>
<summary>Abstract</summary>

Despite strong generalization capabilities, Vision-Language-Action (VLA) models remain constrained by the high cost of expert demonstrations and insufficient real-world interaction. While online reinforcement learning (RL) has shown promise in improving general foundation models, applying RL to VLA manipulation in real-world settings is still hindered by low exploration efficiency and a restricted exploration space. Through systematic real-world experiments, we observe that the effective explora...

</details>

---

### [Any-to-All MRI Synthesis: A Unified Foundation Model for Nasopharyngeal Carcinoma and Its Downstream Applications](https://arxiv.org/abs/2602.08822v1)

**Authors:** Yao Pu, Yiming Shi, Zhenxi Zhang, Peixin Yu, Yitao Zhuang et al. (9 authors)

**Published:** 2026-02-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.08822v1) | [PDF](https://arxiv.org/pdf/2602.08822v1.pdf)

<details>
<summary>Abstract</summary>

Magnetic resonance imaging (MRI) is essential for nasopharyngeal carcinoma (NPC) radiotherapy (RT), but practical constraints, such as patient discomfort, long scan times, and high costs often lead to incomplete modalities in clinical practice, compromising RT planning accuracy. Traditional MRI synthesis methods are modality-specific, limited in anatomical adaptability, and lack clinical interpretability-failing to meet NPC's RT needs. Here, we developed a unified foundation model integrating co...

</details>

---

### [Mimic Intent, Not Just Trajectories](https://arxiv.org/abs/2602.08602v1)

**Authors:** Renming Huang, Chendong Zeng, Wenjing Tang, Jingtian Cai, Cewu Lu et al. (6 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.08602v1) | [PDF](https://arxiv.org/pdf/2602.08602v1.pdf)

<details>
<summary>Abstract</summary>

While imitation learning (IL) has achieved impressive success in dexterous manipulation through generative modeling and pretraining, state-of-the-art approaches like Vision-Language-Action (VLA) models still struggle with adaptation to environmental changes and skill transfer. We argue this stems from mimicking raw trajectories without understanding the underlying intent. To address this, we propose explicitly disentangling behavior intent from execution details in end-2-end IL: \textit{``Mimic ...

</details>

---

### [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167v1)

**Authors:** Milan Ganai, Katie Luo, Jonas Frey, Clark Barrett, Marco Pavone

**Published:** 2026-02-09 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.08167v1) | [PDF](https://arxiv.org/pdf/2602.08167v1.pdf)

<details>
<summary>Abstract</summary>

Embodied Chain-of-Thought (CoT) reasoning has significantly enhanced Vision-Language-Action (VLA) models, yet current methods rely on rigid templates to specify reasoning primitives (e.g., objects in the scene, high-level plans, structural affordances). These templates can force policies to process irrelevant information that distracts from critical action-prediction signals. This creates a bottleneck: without successful policies, we cannot verify reasoning quality; without quality reasoning, we...

</details>

---

### [RLinf-USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI](https://arxiv.org/abs/2602.07837v1)

**Authors:** Hongzhi Zang, Shu'ang Yu, Hao Lin, Tianxing Zhou, Zefang Huang et al. (17 authors)

**Published:** 2026-02-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.07837v1) | [PDF](https://arxiv.org/pdf/2602.07837v1.pdf)

<details>
<summary>Abstract</summary>

Online policy learning directly in the physical world is a promising yet challenging direction for embodied intelligence. Unlike simulation, real-world systems cannot be arbitrarily accelerated, cheaply reset, or massively replicated, which makes scalable data collection, heterogeneous deployment, and long-horizon effective training difficult. These challenges suggest that real-world policy learning is not only an algorithmic issue but fundamentally a systems problem. We present USER, a Unified ...

</details>

---
