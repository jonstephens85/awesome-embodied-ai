# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-18 22:11 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885v1)

**Authors:** Xiaowei Cai, Yunuo Cai, Bingao Chen, Jingxiao Chen, Zhi Chen et al. (39 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16885v1) | [PDF](https://arxiv.org/pdf/2608.16885v1.pdf) | [Project Page](https://tau0-vla.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_0$-VLA, a hierarchical robot foundation model that formulates high-level subtask generation as a compute-scalable inference problem through w...

</details>

---

### [HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](https://arxiv.org/abs/2608.16837v1)

**Authors:** Langzhe Gu, Chengkai Hou, Meng Li, Xinhua Wang, Jiaming Liu et al. (17 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16837v1) | [PDF](https://arxiv.org/pdf/2608.16837v1.pdf) | [Project Page](https://grange007.github.io/HAF)

<details>
<summary>Abstract</summary>

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate locomotion, waist posture, and dual-arm manipulation effectively. Moreover, policies trained through offline behavior cloning can ...

</details>

---

### [US-VLA: An Ultrasound Vision-Language-Action Model for Embodied Abdomina](https://arxiv.org/abs/2608.16074v1)

**Authors:** Cheng Zhang, Xingzheng Wu, Guihao Yan, Xifeng Hu, Zhi Liu et al. (7 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16074v1) | [PDF](https://arxiv.org/pdf/2608.16074v1.pdf) | [GitHub](https://github.com/VMVLab/US-VLA)

<details>
<summary>Abstract</summary>

Artificial intelligence-assisted ultrasound scanning enhances diagnostic reliability and efficiency by providing real-time guidance for standardized image acquisition and reducing operator dependence. However, existing reinforcement learning and learning-assisted ultrasound scanning methods typically rely on carefully designed reward functions or extensive interaction data, which limits their generalization ability and stability across different devices, patient populations, and complex clinical...

</details>

---

## Other Recent Papers

### [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](https://arxiv.org/abs/2608.16889v1)

**Authors:** Bingxin Xu, Yuzhang Shang, Emilio Ferrara

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16889v1) | [PDF](https://arxiv.org/pdf/2608.16889v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation chains many contact-rich skills into one multi-stage task. Vision-language-action (VLA) models increasingly master the individual skills, yet the chain still fails: errors compound beyond the policy's ability to correct, and one subtask silently constrains the next. A promising recipe freezes the VLA and puts an LLM agent in charge: it plans in language, moves in free space with analytic primitives, invokes the VLA only for contact-rich segments, and writes adapta...

</details>

---

### [FabriMAE I Trust Myself? Self-Evaluating VLA Action Generation with Markov Attention Entropy](https://arxiv.org/abs/2608.16697v1)

**Authors:**  Aniri, Chen Yilin, Jinhe Bi, Junfei Guo, Donglai Ran et al. (13 authors)

**Published:** 2026-08-17 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16697v1) | [PDF](https://arxiv.org/pdf/2608.16697v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) integrate visual perception, language instruction, and action generation into end-to-end policies across heterogeneous architectures. However, enabling VLAs to self-evaluate their action generation reliability without external supervision remains a major challenge. Existing methods either rely on expert annotations or estimate uncertainty only from output statistics, largely ignoring internal signals. In this work, we observe that internal visual modality ent...

</details>

---

### [NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](https://arxiv.org/abs/2608.16503v1)

**Authors:** Cong Zhao, Shuai Tian, Xu Zhang, Baocheng Ni, Xinguo Song et al. (14 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16503v1) | [PDF](https://arxiv.org/pdf/2608.16503v1.pdf)

<details>
<summary>Abstract</summary>

Real-world deployment of Vision-Language-Action (VLA) models is often bottlenecked by efficiency-performance trade-offs, cross-embodiment generalization, and execution smoothness. We present NebulaVLA, an asynchronous dual-frequency architecture that decouples high-level semantic reasoning from low-level action control, optimizing computational resources and modularity. To bridge semantic gaps across heterogeneous robots, we introduce GESTURE-7, a unified language-grounded action representation....

</details>

---

### [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172v1)

**Authors:** Xunyao Lei, Renjun Wu, Tianlin Huo, Xuesong Li

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16172v1) | [PDF](https://arxiv.org/pdf/2608.16172v1.pdf)

<details>
<summary>Abstract</summary>

At every re-observation point in a hierarchical Vision-Language-Action (VLA) system, two interface decisions must be made: when to terminate the current subtask and how far to execute the proposed action chunk. These decisions are mutually dependent---the optimal stopping point depends on what the executor plans to do, while the optimal execution length depends on where the subtask boundary lies---yet existing architectures evaluate them in isolation, an asymmetry neither module can overcome alo...

</details>

---

### [When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents](https://arxiv.org/abs/2608.16806v1)

**Authors:** Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang et al. (10 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16806v1) | [PDF](https://arxiv.org/pdf/2608.16806v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated capabilities in in-context learning, task decomposition, step-by-step reasoning, and code generation, driving their gradual evolution from text generation models into the core of agents capable of perceiving environments, invoking tools, and executing tasks. Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this t...

</details>

---

### [Exposing the Long-tail in Embodied Urban Navigation via Scalable Learning from In-the-Wild Videos](https://arxiv.org/abs/2608.16476v1)

**Authors:** Bingyi Xia, Han Bao, Zhewei Chen, Hanjing Ye, Jingwen Yu et al. (8 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16476v1) | [PDF](https://arxiv.org/pdf/2608.16476v1.pdf)

<details>
<summary>Abstract</summary>

Learning embodied urban navigation policies from real-world data is constrained by the cost of task-specific data collection and the limited coverage of rare yet safety-critical scenarios. To address these challenges, we present a scalable framework for learning point-goal urban navigation from web-scale in-the-wild egocentric videos while systematically exposing its long tail. The framework automatically annotates uncurated web videos with metric trajectories and structured navigation semantics...

</details>

---

### [GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](https://arxiv.org/abs/2608.15875v1)

**Authors:**  GigaBrain Team, Angen Ye, Axiang Sun, Can Jin, Chenxi Cheng et al. (59 authors)

**Published:** 2026-08-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.15875v1) | [PDF](https://arxiv.org/pdf/2608.15875v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have become a dominant paradigm for generalist embodied agents, demonstrating strong complex and long-horizon task completion in structured settings. Yet it remains an open question whether current VLA systems can benefit from more effective architectural design, scale to substantially larger and more heterogeneous data regimes, and achieve broader generalization across tasks and embodiments. To this end, we present GigaBrain-0.7, an embodied foundation model ...

</details>

---

### [ViTaR: Visuo-Tactile Residual Adaptation for Foundation VLA Manipulation](https://arxiv.org/abs/2608.15816v1)

**Authors:** Yi Wang, Renjun Wu, Jinyan Liu, Xuesong Li

**Published:** 2026-08-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.15816v1) | [PDF](https://arxiv.org/pdf/2608.15816v1.pdf)

<details>
<summary>Abstract</summary>

As Vision-Language-Action (VLA) models scale toward real-world deployment, contact-rich manipulation exposes a critical blind spot: these policies encode broad visual-semantic priors yet remain unaware of local contact events, producing identical actions whether contact is established, lost, or destabilized. Existing remedies either modify VLA internals, risking catastrophic forgetting, or demand online reinforcement under near-failure contact conditions. Both grant tactile unbounded influence o...

</details>

---

### [Robo-Dopamine 2.0: History-Conditioned and OOD-Aware Process Reward Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.15680v1)

**Authors:** Yijie Xu, Haopeng Jin, Run Zhou, Shengbang Liu, Sixiang Chen et al. (11 authors)

**Published:** 2026-08-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.15680v1) | [PDF](https://arxiv.org/pdf/2608.15680v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models improve robotic manipulation but remain vulnerable to compounding errors, scene changes, and off-trajectory states. Reinforcement learning can refine pretrained VLA policies, yet sparse success signals hinder exploration, while engineered dense rewards are costly and task-specific. Existing learned visual reward models often rely on static before-after observations, causing temporal ambiguity and weak discrimination between robustness-preserving variations and...

</details>

---

### [Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification](https://arxiv.org/abs/2608.15636v1)

**Authors:** Chunyu Qi, Zhuoran Song, Jian Weng, Haozhe Jiang, Xueyuan Liu et al. (9 authors)

**Published:** 2026-08-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.15636v1) | [PDF](https://arxiv.org/pdf/2608.15636v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in the field of embodied AI, but their high computational cost and limited predicted action length hinder real-time deployment. Although Dadu-Corki, a dedicated accelerator for efficient embodied AI, has been introduced, it does not exploit the inherent interaction patterns between the robot and its environment, which results in a relatively short predicted action length. We observe that robotic environments naturally ...

</details>

---

### [EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints](https://arxiv.org/abs/2608.15502v1)

**Authors:** Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao et al. (8 authors)

**Published:** 2026-08-16 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.15502v1) | [PDF](https://arxiv.org/pdf/2608.15502v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems. In practice, on-device inference is constrained by limited compute capacity and energy budgets, struggling to simultaneously satisfy real-time control and energy efficiency requirements. Alternatively, offloading the inference workload to an edge server is susceptible to fluctuations in system conditions, introdu...

</details>

---

### [Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability](https://arxiv.org/abs/2608.15475v1)

**Authors:** Yudong Gao, Linghan Chen, Wenhan Wu, Mia Zhou, Jiyao Wang et al. (8 authors)

**Published:** 2026-08-16 | **Categories:** cs.CR, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.15475v1) | [PDF](https://arxiv.org/pdf/2608.15475v1.pdf)

<details>
<summary>Abstract</summary>

Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token po...

</details>

---
