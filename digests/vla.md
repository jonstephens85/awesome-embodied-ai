# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-26 16:59 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010v1)

**Authors:** Yue Su, Sijin Chen, Haixin Shi, Mingyu Liu, Zhengshen Zhang et al. (10 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.22010v1) | [PDF](https://arxiv.org/pdf/2602.22010v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Leveraging future observation modeling to facilitate action generation presents a promising avenue for enhancing the capabilities of Vision-Language-Action (VLA) models. However, existing approaches struggle to strike a balance between maintaining efficient, predictable future representations and preserving sufficient fine-grained information to guide precise action generation. To address this limitation, we propose WoG (World Guidance), a framework that maps future observations into compact con...

</details>

---

### [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633v1)

**Authors:** Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li et al. (7 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.21633v1) | [PDF](https://arxiv.org/pdf/2602.21633v1.pdf) | [GitHub](https://github.com/Kisaragi0/SC-VLA)

<details>
<summary>Abstract</summary>

Standard vision-language-action (VLA) models rely on fitting statistical data priors, limiting their robust understanding of underlying physical dynamics. Reinforcement learning enhances physical grounding through exploration yet typically relies on external reward signals that remain isolated from the agent's internal states. World action models have emerged as a promising paradigm that integrates imagination and control to enable predictive planning. However, they rely on implicit context mode...

</details>

---

### [LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies](https://arxiv.org/abs/2602.21531v1)

**Authors:** Yue Yang, Shuo Cheng, Yu Fang, Homanga Bharadhwaj, Mingyu Ding et al. (7 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.21531v1) | [PDF](https://arxiv.org/pdf/2602.21531v1.pdf) | [Project Page](https://yy-gx.github.io/LiLo-VLA/)

<details>
<summary>Abstract</summary>

General-purpose robots must master long-horizon manipulation, defined as tasks involving multiple kinematic structure changes (e.g., attaching or detaching objects) in unstructured environments. While Vision-Language-Action (VLA) models offer the potential to master diverse atomic skills, they struggle with the combinatorial complexity of sequencing them and are prone to cascading failures due to environmental sensitivity. To address these challenges, we propose LiLo-VLA (Linked Local VLA), a mo...

</details>

---

### [VLA Knows Its Limits](https://arxiv.org/abs/2602.21445v1)

**Authors:** Haoxuan Wang, Gengyu Zhang, Yan Yan, Ramana Rao Kompella, Gaowen Liu

**Published:** 2026-02-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21445v1) | [PDF](https://arxiv.org/pdf/2602.21445v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Action chunking has recently emerged as a standard practice in flow-based Vision-Language-Action (VLA) models. However, the effect and choice of the execution horizon - the number of actions to be executed from each predicted chunk - remains underexplored. In this work, we first show that varying the execution horizon leads to substantial performance deviations, with performance initially improving and then declining as the horizon increases. To uncover the reasons, we analyze the cross- and sel...

</details>

---

## Other Recent Papers

### [Are Foundation Models the Route to Full-Stack Transfer in Robotics?](https://arxiv.org/abs/2602.22001v1)

**Authors:** Freek Stulp, Samuel Bustamante, João Silvério, Alin Albu-Schäffer, Jeannette Bohg et al. (6 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.22001v1) | [PDF](https://arxiv.org/pdf/2602.22001v1.pdf)

<details>
<summary>Abstract</summary>

In humans and robots alike, transfer learning occurs at different levels of abstraction, from high-level linguistic transfer to low-level transfer of motor skills. In this article, we provide an overview of the impact that foundation models and transformer networks have had on these different levels, bringing robots closer than ever to "full-stack transfer". Considering LLMs, VLMs and VLAs from a robotic transfer learning perspective allows us to highlight recurring concepts for transfer, beyond...

</details>

---

### [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](https://arxiv.org/abs/2602.21736v1)

**Authors:** Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng et al. (8 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21736v1) | [PDF](https://arxiv.org/pdf/2602.21736v1.pdf)

<details>
<summary>Abstract</summary>

Despite progress, Vision-Language-Action models (VLAs) are limited by a scarcity of large-scale, diverse robot data. While human manipulation videos offer a rich alternative, existing methods are forced to choose between small, precisely-labeled datasets and vast in-the-wild footage with unreliable hand tracking labels. We present JALA, a pretraining framework that learns Jointly-Aligned Latent Actions. JALA bypasses full visual dynamic reconstruction, instead learns a predictive action embeddin...

</details>

---

### [NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning](https://arxiv.org/abs/2602.21172v1)

**Authors:** Ishaan Rawal, Shubh Gupta, Yihan Hu, Wei Zhan

**Published:** 2026-02-24 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.21172v1) | [PDF](https://arxiv.org/pdf/2602.21172v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are advancing autonomous driving by replacing modular pipelines with unified end-to-end architectures. However, current VLAs face two expensive requirements: (1) massive dataset collection, and (2) dense reasoning annotations. In this work, we address both challenges with \modelname (\textbf{No} \textbf{R}easoning for \textbf{D}riving). Compared to existing VLAs, \modelname achieves competitive performance while being fine-tuned on $<$60\% of the data and no r...

</details>

---

### [ActionReasoning: Robot Action Reasoning in 3D Space with LLM for Robotic Brick Stacking](https://arxiv.org/abs/2602.21161v1)

**Authors:** Guangming Wang, Qizhen Ying, Yixiong Jing, Olaf Wysocki, Brian Sheil

**Published:** 2026-02-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21161v1) | [PDF](https://arxiv.org/pdf/2602.21161v1.pdf)

<details>
<summary>Abstract</summary>

Classical robotic systems typically rely on custom planners designed for constrained environments. While effective in restricted settings, these systems lack generalization capabilities, limiting the scalability of embodied AI and general-purpose robots. Recent data-driven Vision-Language-Action (VLA) approaches aim to learn policies from large-scale simulation and real-world data. However, the continuous action space of the physical world significantly exceeds the representational capacity of l...

</details>

---

### [HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.21157v1)

**Authors:** Quanxin Shou, Fangqi Zhu, Shawn Chen, Puxin Yan, Zhengyang Yan et al. (12 authors)

**Published:** 2026-02-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21157v1) | [PDF](https://arxiv.org/pdf/2602.21157v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but often struggle in long-horizon or out-of-distribution scenarios due to the lack of explicit mechanisms for multimodal reasoning and anticipating how the world will evolve under action. Recent works introduce textual chain-of-thought or visual subgoal prediction within VLA models to reason, but still fail to offer a unified human-like reasoning framework for joint textual reasoning, visual foresight, an...

</details>

---

### [Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks](https://arxiv.org/abs/2602.21013v1)

**Authors:** Sanjay Haresh, Daniel Dijkman, Apratim Bhattacharyya, Roland Memisevic

**Published:** 2026-02-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21013v1) | [PDF](https://arxiv.org/pdf/2602.21013v1.pdf)

<details>
<summary>Abstract</summary>

Many dexterous manipulation tasks are non-markovian in nature, yet little attention has been paid to this fact in the recent upsurge of the vision-language-action (VLA) paradigm. Although they are successful in bringing internet-scale semantic understanding to robotics, existing VLAs are primarily "stateless" and struggle with memory-dependent long horizon tasks. In this work, we explore a way to impart both spatial and temporal memory to a VLA by incorporating a language scratchpad. The scratch...

</details>

---

### [IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2602.20715v1)

**Authors:** Zhian Su, Weijie Kong, Haonan Dong, Huixu Dong

**Published:** 2026-02-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.20715v1) | [PDF](https://arxiv.org/pdf/2602.20715v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated significant potential for generalist robotic policies; however, they struggle to generalize to long-horizon complex tasks in novel real-world domains due to distribution shifts and the scarcity of high-quality demonstrations. Although reinforcement learning (RL) offers a promising avenue for policy improvement, applying it to real-world VLA fine-tuning faces challenges regarding exploration efficiency, training stability, and sample cost. To ...

</details>

---

### [Recursive Belief Vision Language Action Models](https://arxiv.org/abs/2602.20659v2)

**Authors:** Vaidehi Bagaria, Bijo Sebastian, Nirav Kumar Patel

**Published:** 2026-02-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.20659v2) | [PDF](https://arxiv.org/pdf/2602.20659v2.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models must enable agents to execute long-horizon tasks under partial observability. However, most existing approaches remain observation-driven, relying on short context windows or repeated queries to vision-language models (VLMs). This leads to loss of task progress, action repetition under perceptual aliasing, and high inference latency. While semantic grounding is important, long-horizon manipulation fundamentally requires persistent, action-conditioned state represent...

</details>

---

### [An interactive enhanced driving dataset for autonomous driving](https://arxiv.org/abs/2602.20575v1)

**Authors:** Haojie Feng, Peizhi Zhang, Mengjie Tian, Xinrui Zhang, Zhuoren Li et al. (11 authors)

**Published:** 2026-02-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.20575v1) | [PDF](https://arxiv.org/pdf/2602.20575v1.pdf)

<details>
<summary>Abstract</summary>

The evolution of autonomous driving towards full automation demands robust interactive capabilities; however, the development of Vision-Language-Action (VLA) models is constrained by the sparsity of interactive scenarios and inadequate multimodal alignment in existing data. To this end, this paper proposes the Interactive Enhanced Driving Dataset (IEDD). We develop a scalable pipeline to mine million-level interactive segments from naturalistic driving data based on interactive trajectories, and...

</details>

---

### [BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model](https://arxiv.org/abs/2602.20566v1)

**Authors:** Haosheng Li, Weixin Mao, Zihan Lan, Hongwei Xiong, Hongan Wang et al. (9 authors)

**Published:** 2026-02-24 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.20566v1) | [PDF](https://arxiv.org/pdf/2602.20566v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved significant breakthroughs by leveraging Large Vision Language Models (VLMs) to jointly interpret instructions and visual inputs. However, the substantial increase in visual tokens, particularly from multi-view inputs, poses serious challenges to real-time robotic manipulation. Existing acceleration techniques for VLMs, such as token pruning, often result in degraded performance when directly applied to VLA models, as they overlook the relationshi...

</details>

---

### [Efficient and Explainable End-to-End Autonomous Driving via Masked Vision-Language-Action Diffusion](https://arxiv.org/abs/2602.20577v1)

**Authors:** Jiaru Zhang, Manav Gagvani, Can Cui, Juntong Peng, Ruqi Zhang et al. (6 authors)

**Published:** 2026-02-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.20577v1) | [PDF](https://arxiv.org/pdf/2602.20577v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) and Vision-Language Models (VLMs) have emerged as promising candidates for end-to-end autonomous driving. However, these models typically face challenges in inference latency, action precision, and explainability. Existing autoregressive approaches struggle with slow token-by-token generation, while prior diffusion-based planners often rely on verbose, general-purpose language tokens that lack explicit geometric structure. In this work, we propose Masked Vision-Langu...

</details>

---
