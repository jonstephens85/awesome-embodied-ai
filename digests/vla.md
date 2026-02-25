# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-25 22:22 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [UniLACT: Depth-Aware RGB Latent Action Learning for Vision-Language-Action Models](https://arxiv.org/abs/2602.20231v1)

**Authors:** Manish Kumar Govind, Dominick Reilly, Pu Wang, Srijan Das

**Published:** 2026-02-23 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.20231v1) | [PDF](https://arxiv.org/pdf/2602.20231v1.pdf) | [Project Page](https://manishgovind.github.io/unilact-vla/)

<details>
<summary>Abstract</summary>

Latent action representations learned from unlabeled videos have recently emerged as a promising paradigm for pretraining vision-language-action (VLA) models without explicit robot action supervision. However, latent actions derived solely from RGB observations primarily encode appearance-driven dynamics and lack explicit 3D geometric structure, which is essential for precise and contact-rich manipulation. To address this limitation, we introduce UniLACT, a transformer-based VLA model that incor...

</details>

---

## Other Recent Papers

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

### [Recursive Belief Vision Language Model](https://arxiv.org/abs/2602.20659v1)

**Authors:** Vaidehi Bagaria, Bijo Sebastian, Nirav Patel

**Published:** 2026-02-24 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.20659v1) | [PDF](https://arxiv.org/pdf/2602.20659v1.pdf)

<details>
<summary>Abstract</summary>

Current vision-language-action (VLA) models struggle with long-horizon manipulation under partial observability. Most existing approaches remain observation-driven, relying on short context windows or repeated queries to vision-language models (VLMs). This leads to loss of task progress, action repetition under perceptual aliasing, and high inference latency. Semantic reasoning alone is not the primary bottleneck in long-horizon manipulation. Instead, VLAs lack persistent, action-conditioned sta...

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

### [QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2602.20309v1)

**Authors:** Jingxuan Zhang, Yunta Hsieh, Zhongwei Wang, Haokun Lin, Xin Wang et al. (8 authors)

**Published:** 2026-02-23 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.20309v1) | [PDF](https://arxiv.org/pdf/2602.20309v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models unify perception, language, and control for embodied agents but face significant challenges in practical deployment due to rapidly increasing compute and memory demands, especially as models scale to longer horizons and larger backbones. To address these bottlenecks, we introduce QuantVLA, a training-free post-training quantization (PTQ) framework that, to our knowledge, is the first PTQ approach for VLA systems and the first to successfully quantize a diffusi...

</details>

---

### [Universal Pose Pretraining for Generalizable Vision-Language-Action Policies](https://arxiv.org/abs/2602.19710v1)

**Authors:** Haitao Lin, Hanyang Yu, Jingshun Huang, He Zhang, Yonggen Ling et al. (8 authors)

**Published:** 2026-02-23 | **Categories:** cs.CV, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.19710v1) | [PDF](https://arxiv.org/pdf/2602.19710v1.pdf)

<details>
<summary>Abstract</summary>

Existing Vision-Language-Action (VLA) models often suffer from feature collapse and low training efficiency because they entangle high-level perception with sparse, embodiment-specific action supervision. Since these models typically rely on VLM backbones optimized for Visual Question Answering (VQA), they excel at semantic identification but often overlook subtle 3D state variations that dictate distinct action patterns. To resolve these misalignments, we propose Pose-VLA, a decoupled paradigm ...

</details>

---
