# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-16 22:48 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429v1)

**Authors:** Dwip Dalal, Shivansh Patel, Chahit Jain, Jeonghwan Kim, Utkarsh Mishra et al. (10 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13429v1) | [PDF](https://arxiv.org/pdf/2607.13429v1.pdf) | [Project Page](anchoralignvla.github.io) | [GitHub](https://github.com/dwipddalal/Anchor-Align)

<details>
<summary>Abstract</summary>

Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that stan...

</details>

---

### [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017v1)

**Authors:** Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang et al. (16 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13017v1) | [PDF](https://arxiv.org/pdf/2607.13017v1.pdf) | [Project Page](https://flow-wam.github.io)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy the former, and prior visual action representations overlook the temporal motion structure across fram...

</details>

---

### [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](https://arxiv.org/abs/2607.12992v1)

**Authors:** Zhao Yang, Yinan Shi, Mingyuan Yao, Wenyao Xue, Yawei Jueluo et al. (6 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12992v1) | [PDF](https://arxiv.org/pdf/2607.12992v1.pdf) | [Project Page](https://cytoderm-ai.github.io/chunkflow)

<details>
<summary>Abstract</summary>

Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. We propose Chun...

</details>

---

### [Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/abs/2607.12659v1)

**Authors:** Zebin Yang, Qi Wang, Yunhe Wang, Xiurui Guo, Bo Yu et al. (9 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12659v1) | [PDF](https://arxiv.org/pdf/2607.12659v1.pdf) | [GitHub](https://github.com/PKU-SEC-Lab/Jetson-PI)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially mask this latency by parallelizing action execution and subsequent inference, but it introduces two critical issues: perception-execution misa...

</details>

---

## Other Recent Papers

### [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2607.13926v1)

**Authors:** Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng et al. (6 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13926v1) | [PDF](https://arxiv.org/pdf/2607.13926v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglemen...

</details>

---

### [Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning](https://arxiv.org/abs/2607.13818v1)

**Authors:** Xiaopeng Zhang, Yueyang Weng, Qi Liu, Yongjin Mu, Yanjie Li

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13818v1) | [PDF](https://arxiv.org/pdf/2607.13818v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution deviates from its nominal behavior. In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, a...

</details>

---

### [UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following](https://arxiv.org/abs/2607.13621v1)

**Authors:** Kun Yu, Jianhua Yang, Yixiang Chen, Changwei Wang, Hongyuan Yu et al. (10 authors)

**Published:** 2026-07-15 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.13621v1) | [PDF](https://arxiv.org/pdf/2607.13621v1.pdf)

<details>
<summary>Abstract</summary>

Language-guided human following is an important capability for embodied agents, but existing benchmarks typically assume that the target person is visible at the start of an episode. This setting simplifies the problem and overlooks a more realistic requirement: an agent often needs to first find a language-described target and then persistently follow that target in a dynamic environment. While recent work has started to study human search, existing settings are typically evaluated in task-spec...

</details>

---

### [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](https://arxiv.org/abs/2607.13605v1)

**Authors:** Yingwei Ji

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13605v1) | [PDF](https://arxiv.org/pdf/2607.13605v1.pdf)

<details>
<summary>Abstract</summary>

One high-level instruction in long-horizon manipulation can cover several action stages. We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks. A progress module tracks the active stage, while the action policy receives stage information either as current-stage text or as a normalized ordinal stage index in robot state. We compare these interfaces with GR00T N1.6 on LIBERO-10 under direct fine-tuning and continuation fine-tu...

</details>

---

### [Semantic Anchoring for Robotic Action Representations](https://arxiv.org/abs/2607.13597v1)

**Authors:** Yuan Xu, Youheng Shi, Chengyang Li, Wentao Zhu, Yizhou Wang

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13597v1) | [PDF](https://arxiv.org/pdf/2607.13597v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit rich semantic representations from pretrained Vision-Language Models, yet fine-tuning on limited robot demonstrations degrades this structure and undermines generalization. A fundamental question therefore arises: what constitutes a good action representation? Inspired by the mirror neuron theory's insight that observation and execution share an intention-level encoding, we examine whether a robot's action representations preserve the semantic structur...

</details>

---

### [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](https://arxiv.org/abs/2607.12931v1)

**Authors:** Yilun Kong, Yunpeng Qing, Guozheng Ma, Haoyu Wang, Li Shen et al. (7 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12931v1) | [PDF](https://arxiv.org/pdf/2607.12931v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts...

</details>

---

### [UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies](https://arxiv.org/abs/2607.12892v1)

**Authors:** Lirui Zhao, Modi Shi, Li Chen, Qi Liu, Ping Luo et al. (6 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12892v1) | [PDF](https://arxiv.org/pdf/2607.12892v1.pdf)

<details>
<summary>Abstract</summary>

Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states, guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames are treated as higher progress. However, this time-derived label is only a noisy proxy for physical task progress. In contact-rich manipulat...

</details>

---

### [TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/abs/2607.12571v1)

**Authors:** Pinhan Fu, Xianda Guo, Xuetao Li, Wenke Huang, Ruilin Wang et al. (8 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12571v1) | [PDF](https://arxiv.org/pdf/2607.12571v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. We study this gap through two independently proposed VLA attacks from groups with distinct ...

</details>

---

### [VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v1)

**Authors:** Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao et al. (8 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12356v1) | [PDF](https://arxiv.org/pdf/2607.12356v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures an...

</details>

---

### [Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2607.12287v1)

**Authors:** Yuzhou Wu, Yuxin Zheng, Muchun Niu, Yishan Yang, Tianhao Liu et al. (9 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12287v1) | [PDF](https://arxiv.org/pdf/2607.12287v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies. To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation. On the ...

</details>

---
