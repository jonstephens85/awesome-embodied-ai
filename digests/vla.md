# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-20 16:43 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FASTER: Rethinking Real-Time Flow VLAs](https://arxiv.org/abs/2603.19199v1)

**Authors:** Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou et al. (8 authors)

**Published:** 2026-03-19 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.19199v1) | [PDF](https://arxiv.org/pdf/2603.19199v1.pdf) | [Project Page](https://innovator-zero.github.io/FASTER)

<details>
<summary>Abstract</summary>

Real-time execution is crucial for deploying Vision-Language-Action (VLA) models in the physical world. Existing asynchronous inference methods primarily optimize trajectory smoothness, but neglect the critical latency in reacting to environmental changes. By rethinking the notion of reaction in action chunking policies, this paper presents a systematic analysis of the factors governing reaction time. We show that reaction time follows a uniform distribution determined jointly by the Time to Fir...

</details>

---

### [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183v1)

**Authors:** Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy, Mac Schwager

**Published:** 2026-03-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.19183v1) | [PDF](https://arxiv.org/pdf/2603.19183v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation. However, their generalization is inconsistent: while these models can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. We apply mechanistic interpretability techniques to better understand the inner workings of VLA models. To probe internal representations, we train Sparse Autoencoders (SAEs) on hidden layer activations ...

</details>

---

### [MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model](https://arxiv.org/abs/2603.18892v1)

**Authors:** Youngwan Lee, Soojin Jang, Yoorhim Cho, Seunghwan Lee, Yong-Ju Lee et al. (6 authors)

**Published:** 2026-03-19 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.18892v1) | [PDF](https://arxiv.org/pdf/2603.18892v1.pdf) | [Project Page](https://youngwanlee.github.io/multihopspatial)

<details>
<summary>Abstract</summary>

Spatial reasoning is foundational for Vision-Language Models (VLMs), particularly when deployed as Vision-Language-Action (VLA) agents in physical environments. However, existing benchmarks predominantly focus on elementary, single-hop relations, neglecting the multi-hop compositional reasoning and precise visual grounding essential for real-world scenarios. To address this, we introduce MultihopSpatial, offering three key contributions: (1) A comprehensive benchmark designed for multi-hop and c...

</details>

---

### [DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding](https://arxiv.org/abs/2603.19219v1)

**Authors:** Dong Zhuo, Wenzhao Zheng, Sicheng Zuo, Siming Yan, Lu Hou et al. (7 authors)

**Published:** 2026-03-19 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.19219v1) | [PDF](https://arxiv.org/pdf/2603.19219v1.pdf) | [Project Page](https://paryi555.github.io/DriveTok/) | [GitHub](https://github.com/paryi555/DriveTok)

<details>
<summary>Abstract</summary>

With the growing adoption of vision-language-action models and world models in autonomous driving systems, scalable image tokenization becomes crucial as the interface for the visual modality. However, most existing tokenizers are designed for monocular and 2D scenes, leading to inefficiency and inter-view inconsistency when applied to high-resolution multi-view driving scenes. To address this, we propose DriveTok, an efficient 3D driving scene tokenizer for unified multi-view reconstruction and...

</details>

---

### [Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control](https://arxiv.org/abs/2603.17834v1)

**Authors:** Zunzhe Zhang, Runhan Huang, Yicheng Liu, Shaoting Zhu, Linzhan Mou et al. (6 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17834v1) | [PDF](https://arxiv.org/pdf/2603.17834v1.pdf) | [Project Page](https://hrh6666.github.io/GeCO/)

<details>
<summary>Abstract</summary>

Diffusion models and flow matching have become a cornerstone of robotic imitation learning, yet they suffer from a structural inefficiency where inference is often bound to a fixed integration schedule that is agnostic to state complexity. This paradigm forces the policy to expend the same computational budget on trivial motions as it does on complex tasks. We introduce Generative Control as Optimization (GeCO), a time-unconditional framework that transforms action synthesis from trajectory inte...

</details>

---

## Other Recent Papers

### [Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models](https://arxiv.org/abs/2603.19233v1)

**Authors:** Bryce Grant, Xijia Zhao, Peng Wang

**Published:** 2026-03-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.19233v1) | [PDF](https://arxiv.org/pdf/2603.19233v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models combine perception, language, and motor control in a single architecture, yet how they translate multimodal inputs into actions remains poorly understood. We apply activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M--7B parameters across 394,000+ rollout episodes on four benchmarks. The visual pathway dominates action generation across all architectures: injecting baseline activations into null-prompt episodes recover...

</details>

---

### [From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models](https://arxiv.org/abs/2603.19131v1)

**Authors:** Zhuofan Li, Hongkun Yang, Zhenyang Chen, Yangxuan Chen,  Yingyan et al. (7 authors)

**Published:** 2026-03-19 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.19131v1) | [PDF](https://arxiv.org/pdf/2603.19131v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently enabled embodied agents to perform increasingly complex tasks by jointly reasoning over visual, linguistic, and motor modalities. However, we find that the prevailing notion of ``efficiency'' in current VLA research, characterized by parameters, FLOPs, or token decoding throughput, does not reflect actual performance on robotic platforms. In real-world execution, efficiency is determined by system-level embodied behaviors such as task completion ...

</details>

---

### [Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds](https://arxiv.org/abs/2603.18532v1)

**Authors:** Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu

**Published:** 2026-03-19 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.18532v1) | [PDF](https://arxiv.org/pdf/2603.18532v1.pdf)

<details>
<summary>Abstract</summary>

The strong performance of large vision-language models (VLMs) trained with reinforcement learning (RL) has motivated similar approaches for fine-tuning vision-language-action (VLA) models in robotics. Many recent works fine-tune VLAs directly in the real world to avoid addressing the sim-to-real gap. While real-world RL circumvents sim-to-real issues, it inherently limits the generality of the resulting VLA, as scaling scene and object diversity in the physical world is prohibitively difficult. ...

</details>

---

### [AcceRL: A Distributed Asynchronous Reinforcement Learning and World Model Framework for Vision-Language-Action Models](https://arxiv.org/abs/2603.18464v1)

**Authors:** Chengxuan Lu, Shukuan Wang, Yanjie Li, Wei Liu, Shiji Jin et al. (9 authors)

**Published:** 2026-03-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.18464v1) | [PDF](https://arxiv.org/pdf/2603.18464v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) for large-scale Vision-Language-Action (VLA) models faces significant challenges in computational efficiency and data acquisition. We propose AcceRL, a fully asynchronous and decoupled RL framework designed to eliminate synchronization barriers by physically isolating training, inference, and rollouts. Crucially, AcceRL is the first to integrate a plug-and-play, trainable world model into a distributed asynchronous RL pipeline to generate virtual experiences. Experime...

</details>

---

### [Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model](https://arxiv.org/abs/2603.18342v1)

**Authors:** Yanchuan Tang, Taowen Wang, Yuefei Chen, Boxuan Zhang, Qiang Guan et al. (6 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.18342v1) | [PDF](https://arxiv.org/pdf/2603.18342v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable general-purpose robotic policies by mapping visual observations and language instructions to low-level actions, but they often lack reliable introspection. A common practice is to compute a token-level uncertainty signal and take its mean over a rollout. However, mean aggregation can dilute short-lived but safety-critical uncertainty spikes in continuous control. In particular, successful rollouts may contain localized high-entropy segments due to benig...

</details>

---

### [ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2603.17850v1)

**Authors:** Zhou Fang, Jiaqi Wang, Yi Zhou, Qiongfeng Shi

**Published:** 2026-03-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.17850v1) | [PDF](https://arxiv.org/pdf/2603.17850v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models equipped with Flow Matching (FM) action heads achieve state-of-the-art performance in complex robot manipulation. However, the multi-step iterative ODE solving required by FM introduces inference latency that precludes responsive physical control. While current acceleration efforts optimize the Vision-Language Model (VLM) backbone, the action head bottleneck remains overlooked. To address this, we propose ProbeFlow, a training-free adaptive inference fr...

</details>

---

### [HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness](https://arxiv.org/abs/2603.17573v1)

**Authors:** Zihao Zheng, Zhihao Mao, Sicheng Tian, Maoliang Li, Jiayu Chen et al. (11 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.DB, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.17573v1) | [PDF](https://arxiv.org/pdf/2603.17573v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) Models have become the mainstream solution for robot control, but suffer from slow inference speeds. Speculative Decoding (SD) is a promising acceleration method which can be divided into two categories: drafter-based SD and retrieval-based SD. Existing methods fail to analyze the advantages and disadvantages of these two types of SD in VLA models, leading to their sole application or optimization. In this paper, we analyze the trajectory patterns of robots controlle...

</details>

---

### [KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition](https://arxiv.org/abs/2603.17524v1)

**Authors:** Gaoge Han, Zhengqing Gao, Ziwen Li, Jiaxin Huang, Shaoli Huang et al. (8 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17524v1) | [PDF](https://arxiv.org/pdf/2603.17524v1.pdf)

<details>
<summary>Abstract</summary>

In this paper, we introduce a novel kinematics-rich vision-language-action (VLA) task, in which language commands densely encode diverse kinematic attributes (such as direction, trajectory, orientation, and relative displacement) from initiation through completion, at key moments, unlike existing action instructions that capture kinematics only coarsely or partially, thereby supporting fine-grained and personalized manipulation. In this setting, where task goals remain invariant while execution ...

</details>

---

### [Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model](https://arxiv.org/abs/2603.18091v1)

**Authors:** Chen Zhao, Zhuoran Wang, Haoyang Li, Shifeng Bao, Guanlin Li et al. (9 authors)

**Published:** 2026-03-18 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.18091v1) | [PDF](https://arxiv.org/pdf/2603.18091v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently demonstrated strong performance across embodied tasks. Modern VLAs commonly employ diffusion action experts to efficiently generate high-precision continuous action chunks, while auto-regressive generation can be slower and less accurate at low-level control. Yet auto-regressive paradigms still provide complementary priors that can improve robustness and generalization in out-of-distribution environments. To leverage both paradigms, we propose Ac...

</details>

---
