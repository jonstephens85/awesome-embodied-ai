# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-25 17:02 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs](https://arxiv.org/abs/2603.23481v1)

**Authors:** Haoran Yuan, Weigang Yi, Zhenyu Zhang, Wendi Chen, Yuchen Mo et al. (12 authors)

**Published:** 2026-03-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.23481v1) | [PDF](https://arxiv.org/pdf/2603.23481v1.pdf) | [Project Page](https://plan-lab.github.io/projects/vtam/)

<details>
<summary>Abstract</summary>

Video-Action Models (VAMs) have emerged as a promising framework for embodied intelligence, learning implicit world dynamics from raw video streams to produce temporally consistent action predictions. Although such models demonstrate strong performance on long-horizon tasks through visual reasoning, they remain limited in contact-rich scenarios where critical interaction states are only partially observable from vision alone. In particular, fine-grained force modulation and contact transitions a...

</details>

---

### [VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2603.22991v1)

**Authors:** Jintao Cheng, Haozhe Wang, Weibin Li, Gang Wang, Yipu Zhang et al. (10 authors)

**Published:** 2026-03-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.22991v1) | [PDF](https://arxiv.org/pdf/2603.22991v1.pdf) | [Project Page](is:)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have rapidly advanced embodied intelligence, enabling robots to execute complex, instruction-driven tasks. However, as model capacity and visual context length grow, the inference cost of VLA systems becomes a major bottleneck for real-world deployment on resource-constrained platforms. Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA t...

</details>

---

### [CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models](https://arxiv.org/abs/2603.22846v1)

**Authors:** Youzhi Liu, Li Gao, Liu Liu, Mingyang Lv, Yang Cai

**Published:** 2026-03-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.22846v1) | [PDF](https://arxiv.org/pdf/2603.22846v1.pdf) | [GitHub](https://github.com/wlqcode/CoMaTrack-Bench)

<details>
<summary>Abstract</summary>

Embodied Visual Tracking (EVT), a core dynamic task in embodied intelligence, requires an agent to precisely follow a language-specified target. Yet most existing methods rely on single-agent imitation learning, suffering from costly expert data and limited generalization due to static training environments. Inspired by competition-driven capability evolution, we propose CoMaTrack, a competitive game-theoretic multi-agent reinforcement learning framework that trains agents in a dynamic adversari...

</details>

---

### [ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling](https://arxiv.org/abs/2603.22126v1)

**Authors:** Byungjin Kim

**Published:** 2026-03-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22126v1) | [PDF](https://arxiv.org/pdf/2603.22126v1.pdf) | [GitHub](https://github.com/liveplex-cpu/robogate)

<details>
<summary>Abstract</summary>

Deploying learned robot manipulation policies in industrial settings requires rigorous pre-deployment validation, yet exhaustive testing across high-dimensional parameter spaces is intractable. We present ROBOGATE, a deployment risk management framework that combines physics-based simulation with a two-stage adaptive sampling strategy to efficiently discover failure boundaries in the operational parameter space. Stage 1 employs Latin Hypercube Sampling (LHS) across an 8-dimensional parameter spa...

</details>

---

### [VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models](https://arxiv.org/abs/2603.22003v1)

**Authors:** Zixuan Wang, Yuxin Chen, Yuqi Liu, Jinhui Ye, Pengguang Chen et al. (8 authors)

**Published:** 2026-03-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22003v1) | [PDF](https://arxiv.org/pdf/2603.22003v1.pdf) | [Project Page](https://visualprompt-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models typically map visual observations and linguistic instructions directly to robotic control signals. This "black-box" mapping forces a single forward pass to simultaneously handle instruction interpretation, spatial grounding, and low-level control, often leading to poor spatial precision and limited robustness in out-of-distribution scenarios. To address these limitations, we propose VP-VLA, a dual-system framework that decouples high-level reasoning and low-le...

</details>

---

## Other Recent Papers

### [Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2603.23202v1)

**Authors:** Anupam Pani, Yanchao Yang

**Published:** 2026-03-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.23202v1) | [PDF](https://arxiv.org/pdf/2603.23202v1.pdf)

<details>
<summary>Abstract</summary>

Despite advances in Vision-Language-Action (VLA) models, robotic manipulation struggles with fine-grained tasks because current models lack mechanisms for active visual attention allocation. Human gaze naturally encodes intent, planning, and execution patterns -- offering a powerful supervisory signal for guiding robot perception. We introduce a gaze-regularized training framework that aligns VLA models' internal attention with human visual patterns without architectural modifications or inferen...

</details>

---

### [Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring](https://arxiv.org/abs/2603.22899v1)

**Authors:** Teng Yan, Zhengyang Pei, Chengyu Shi, Yue Yu, Yikun Chen et al. (11 authors)

**Published:** 2026-03-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22899v1) | [PDF](https://arxiv.org/pdf/2603.22899v1.pdf)

<details>
<summary>Abstract</summary>

Deploying Vision-Language-Action (VLA) models on resource-constrained edge platforms encounters a fundamental conflict between high-latency semantic inference and the high-frequency control required for dynamic manipulation. To address the challenge, this paper presents Agile-VLA, a hierarchical framework designed for industrial pose reorientation tasks on edge devices such as the NVIDIA Jetson Orin Nano. The core innovation is an Implicit Affordance Anchoring mechanism that directly maps geomet...

</details>

---

### [Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models](https://arxiv.org/abs/2603.22876v1)

**Authors:** Ruixing Jin, Zicheng Zhu, Ruixiang Ouyang, Sheng Xu, Bo Yue et al. (7 authors)

**Published:** 2026-03-24 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.22876v1) | [PDF](https://arxiv.org/pdf/2603.22876v1.pdf)

<details>
<summary>Abstract</summary>

Learning a generalist control policy for dexterous manipulation typically relies on large-scale datasets. Given the high cost of real-world data collection, a practical alternative is to generate synthetic data through simulation. However, the resulting synthetic data often exhibits a significant gap from real-world distributions. While many prior studies have proposed algorithms to bridge the Sim-to-Real discrepancy, there remains a lack of principled research that grounds these methods in real...

</details>

---

### [SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation](https://arxiv.org/abs/2603.22760v1)

**Authors:** Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li et al. (8 authors)

**Published:** 2026-03-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22760v1) | [PDF](https://arxiv.org/pdf/2603.22760v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show promise for robotic control, yet performance in complex household environments remains sub-optimal. Mobile manipulation requires reasoning about global scene layout, fine-grained geometry, and high-dimensional continuous actions, making standard imitation learning insufficient. We introduce a framework for learning spatially-grounded VLA models that strengthens perception and representation through auxiliary task co-training and multi-modal input enhancem...

</details>

---

### [CATNAV: Cached Vision-Language Traversability for Efficient Zero-Shot Robot Navigation](https://arxiv.org/abs/2603.22800v1)

**Authors:** Aditya Potnis, Francisco Affonso, Shreya Gummadi, Naveen Kumar Uppalapati, Girish Chowdhary

**Published:** 2026-03-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22800v1) | [PDF](https://arxiv.org/pdf/2603.22800v1.pdf)

<details>
<summary>Abstract</summary>

Navigating unstructured environments requires assessing traversal risk relative to a robot's physical capabilities, a challenge that varies across embodiments. We present CATNAV, a cost-aware traversability navigation framework that leverages multimodal LLMs for zero-shot, embodiment-aware costmap generation without task-specific training. We introduce a visuosemantic caching mechanism that detects scene novelty and reuses prior risk assessments for semantically similar frames, reducing online V...

</details>

---

### [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435v1)

**Authors:** Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue et al. (15 authors)

**Published:** 2026-03-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.22435v1) | [PDF](https://arxiv.org/pdf/2603.22435v1.pdf)

<details>
<summary>Abstract</summary>

"Code-as-Policy" considers how executable code can complement data-intensive Vision-Language-Action (VLA) methods, yet their effectiveness as autonomous controllers for embodied manipulation remains underexplored. We present CaP-X, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation. At its core is CaP-Gym, an interactive environment in which agents control robots by synthesizing and executing programs that compose perception and control primitives. B...

</details>

---

### [DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2603.22280v1)

**Authors:** Zhide Zhong, Junfeng Li, Junjie He, Haodong Yan, Xin Gong et al. (13 authors)

**Published:** 2026-03-23 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22280v1) | [PDF](https://arxiv.org/pdf/2603.22280v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map visual observations and language instructions directly to robotic actions. While effective for simple tasks, standard VLA models often struggle with complex, multi-step tasks requiring logical planning, as well as precise manipulations demanding fine-grained spatial perception. Recent efforts have incorporated Chain-of-Thought (CoT) reasoning to endow VLA models with a ``thinking before acting'' capability. However, current CoT-based VLA models face two cr...

</details>

---

### [UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos](https://arxiv.org/abs/2603.22264v1)

**Authors:** Gu Zhang, Qicheng Xu, Haozhe Zhang, Jianhan Ma, Long He et al. (19 authors)

**Published:** 2026-03-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22264v1) | [PDF](https://arxiv.org/pdf/2603.22264v1.pdf)

<details>
<summary>Abstract</summary>

Dexterous manipulation remains challenging due to the cost of collecting real-robot teleoperation data, the heterogeneity of hand embodiments, and the high dimensionality of control. We present UniDex, a robot foundation suite that couples a large-scale robot-centric dataset with a unified vision-language-action (VLA) policy and a practical human-data capture setup for universal dexterous hand control. First, we construct UniDex-Dataset, a robot-centric dataset over 50K trajectories across eight...

</details>

---

### [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078v1)

**Authors:** Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma et al. (13 authors)

**Published:** 2026-03-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.22078v1) | [PDF](https://arxiv.org/pdf/2603.22078v1.pdf)

<details>
<summary>Abstract</summary>

Robot action planning in the real world is challenging as it requires not only understanding the current state of the environment but also predicting how it will evolve in response to actions. Vision-language-action (VLA), which repurpose large-scale vision-language models for robot action generation using action experts, have achieved notable success across a variety of robotic tasks. Nevertheless, their performance remains constrained by the scope of their training data, exhibiting limited gen...

</details>

---

### [AI Token Futures Market: Commoditization of Compute and Derivatives Contract Design](https://arxiv.org/abs/2603.21690v1)

**Authors:** Yicai Xing

**Published:** 2026-03-23 | **Categories:** cs.AI, econ.GN

**Links:** [arXiv](https://arxiv.org/abs/2603.21690v1) | [PDF](https://arxiv.org/pdf/2603.21690v1.pdf)

<details>
<summary>Abstract</summary>

As large language models (LLMs) and vision-language-action models (VLAs) become widely deployed, the tokens consumed by AI inference are evolving into a new type of commodity. This paper systematically analyzes the commodity attributes of tokens, arguing for their transition from intelligent service outputs to compute infrastructure raw materials, and draws comparisons with established commodities such as electricity, carbon emission allowances, and bandwidth. Building on the historical experien...

</details>

---
