# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-04 16:50 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization](https://arxiv.org/abs/2602.03310v1)

**Authors:** Songming Liu, Bangguo Li, Kai Ma, Lingxuan Wu, Hengkai Tan et al. (8 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03310v1) | [PDF](https://arxiv.org/pdf/2602.03310v1.pdf) | [Project Page](https://rdt-robotics.github.io/rdt2/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models hold promise for generalist robotics but currently struggle with data scarcity, architectural inefficiencies, and the inability to generalize across different hardware platforms. We introduce RDT2, a robotic foundation model built upon a 7B parameter VLM designed to enable zero-shot deployment on novel embodiments for open-vocabulary tasks. To achieve this, we collected one of the largest open-source robotic datasets--over 10,000 hours of demonstrations in div...

</details>

---

### [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://arxiv.org/abs/2602.02459v1)

**Authors:** Zhiyu Huang, Yun Zhang, Johnson Liu, Rui Song, Chen Tang et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.02459v1) | [PDF](https://arxiv.org/pdf/2602.02459v1.pdf) | [Project Page](https://ucla-mobility.github.io/TIC-VLA/)

<details>
<summary>Abstract</summary>

Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control. Vision-language-action (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action. We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation. TIC-VLA defines a delayed ...

</details>

---

### [World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454v1)

**Authors:** Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, Yunzhe Zhang, Jiarao Liu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02454v1) | [PDF](https://arxiv.org/pdf/2602.02454v1.pdf) | [Project Page](https://world-gymnast.github.io/)

<details>
<summary>Abstract</summary>

Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world...

</details>

---

## Other Recent Papers

### [QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization](https://arxiv.org/abs/2602.03782v1)

**Authors:** Yuhao Xu, Yantai Yang, Zhenyang Fan, Yufan Liu, Yuming Li et al. (7 authors)

**Published:** 2026-02-03 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03782v1) | [PDF](https://arxiv.org/pdf/2602.03782v1.pdf)

<details>
<summary>Abstract</summary>

The advent of Vision-Language-Action (VLA) models represents a significant leap for embodied intelligence, yet their immense computational demands critically hinder deployment on resource-constrained robotic platforms. Intuitively, low-bit quantization is a prevalent and preferred technique for large-scale model compression. However, we find that a systematic analysis of VLA model's quantization is fundamentally lacking. We argue that naively applying uniform-bit quantization from Large Language...

</details>

---

### [MVP-LAM: Learning Action-Centric Latent Action via Cross-Viewpoint Reconstruction](https://arxiv.org/abs/2602.03668v1)

**Authors:** Jung Min Lee, Dohyeok Lee, Seokhun Ju, Taehyun Cho, Jin Woo Koo et al. (8 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03668v1) | [PDF](https://arxiv.org/pdf/2602.03668v1.pdf)

<details>
<summary>Abstract</summary>

Learning \emph{latent actions} from diverse human videos enables scaling robot learning beyond embodiment-specific robot datasets, and these latent actions have recently been used as pseudo-action labels for vision-language-action (VLA) model pretraining. To make VLA pretraining effective, latent actions should contain information about the underlying agent's actions despite the absence of ground-truth labels. We propose \textbf{M}ulti-\textbf{V}iew\textbf{P}oint \textbf{L}atent \textbf{A}ction ...

</details>

---

### [CRL-VLA: Continual Vision-Language-Action Learning](https://arxiv.org/abs/2602.03445v1)

**Authors:** Qixin Zeng, Shuo Zhang, Hongyin Zhang, Renjie Wang, Han Zhao et al. (9 authors)

**Published:** 2026-02-03 | **Categories:** cs.AI, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03445v1) | [PDF](https://arxiv.org/pdf/2602.03445v1.pdf)

<details>
<summary>Abstract</summary>

Lifelong learning is critical for embodied agents in open-world environments, where reinforcement learning fine-tuning has emerged as an important paradigm to enable Vision-Language-Action (VLA) models to master dexterous manipulation through environmental interaction. Thus, Continual Reinforcement Learning (CRL) is a promising pathway for deploying VLA models in lifelong robotic scenarios, yet balancing stability (retaining old skills) and plasticity (learning new ones) remains a formidable cha...

</details>

---

### [When Attention Betrays: Erasing Backdoor Attacks in Robotic Policies by Reconstructing Visual Tokens](https://arxiv.org/abs/2602.03153v1)

**Authors:** Xuetao Li, Pinhan Fu, Wenke Huang, Nengyuan Pan, Songhua Yang et al. (10 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03153v1) | [PDF](https://arxiv.org/pdf/2602.03153v1.pdf)

<details>
<summary>Abstract</summary>

Downstream fine-tuning of vision-language-action (VLA) models enhances robotics, yet exposes the pipeline to backdoor risks. Attackers can pretrain VLAs on poisoned data to implant backdoors that remain stealthy but can trigger harmful behavior during inference. However, existing defenses either lack mechanistic insight into multimodal backdoors or impose prohibitive computational costs via full-model retraining. To this end, we uncover a deep-layer attention grabbing mechanism: backdoors redire...

</details>

---

### [MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models](https://arxiv.org/abs/2602.02212v1)

**Authors:** Zheyuan Zhou, Liang Du, Zixun Sun, Xiaoyu Zhou, Ruimin Ye et al. (8 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02212v1) | [PDF](https://arxiv.org/pdf/2602.02212v1.pdf)

<details>
<summary>Abstract</summary>

Despite significant progress in Visual-Language-Action (VLA), in highly complex and dynamic environments that involve real-time unpredictable interactions (such as 3D open worlds and large-scale PvP games), existing approaches remain inefficient at extracting action-critical signals from redundant sensor streams. To tackle this, we introduce MAIN-VLA, a framework that explicitly Models the Abstraction of Intention and eNvironment to ground decision-making in deep semantic alignment rather than s...

</details>

---

### [FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2602.02142v1)

**Authors:** Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay et al. (7 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02142v1) | [PDF](https://arxiv.org/pdf/2602.02142v1.pdf)

<details>
<summary>Abstract</summary>

Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot s...

</details>

---

### [Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models](https://arxiv.org/abs/2602.01834v1)

**Authors:** Siqi Wen, Shu Yang, Shaopeng Fu, Jingfeng Zhang, Lijie Hu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01834v1) | [PDF](https://arxiv.org/pdf/2602.01834v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models close the perception action loop by translating multimodal instructions into executable behaviors, but this very capability magnifies safety risks: jailbreaks that merely yield toxic text in LLMs can trigger unsafe physical actions in embodied systems. Existing defenses alignment, filtering, or prompt hardening intervene too late or at the wrong modality, leaving fused representations exploitable. We introduce a concept-based dictionary learning framework for ...

</details>

---

### [From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models](https://arxiv.org/abs/2602.01811v1)

**Authors:** Wentao Zhang, Aolan Sun, Wentao Mo, Xiaoyang Qu, Yuxin Zheng et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01811v1) | [PDF](https://arxiv.org/pdf/2602.01811v1.pdf)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models for embodied agents integrate perception, reasoning, and control, they remain constrained by two critical weaknesses: first, during grasping tasks, the action tokens generated by the language model often exhibit subtle spatial deviations from the target object, resulting in grasp failures; second, they lack the ability to reliably recognize task completion, which leads to redundant actions and frequent timeout errors. To address these challenges and enha...

</details>

---

### [Accelerating Structured Chain-of-Thought in Autonomous Vehicles](https://arxiv.org/abs/2602.02864v1)

**Authors:** Yi Gu, Yan Wang, Yuxiao Chen, Yurong You, Wenjie Luo et al. (11 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.02864v1) | [PDF](https://arxiv.org/pdf/2602.02864v1.pdf)

<details>
<summary>Abstract</summary>

Chain-of-Thought (CoT) reasoning enhances the decision-making capabilities of vision-language-action models in autonomous driving, but its autoregressive nature introduces significant inference latency, making it impractical for real-time applications. To address this, we introduce FastDriveCoT, a novel parallel decoding method that accelerates template-structured CoT. Our approach decomposes the reasoning process into a dependency graph of distinct sub-tasks, such as identifying critical object...

</details>

---
