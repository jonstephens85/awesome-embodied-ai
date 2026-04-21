# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-21 22:31 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486v1)

**Authors:** Jinghui Lu, Jiayi Guan, Zhijian Huang, Jinlong Li, Guang Li et al. (50 authors)

**Published:** 2026-04-20 | **Categories:** cs.CV, cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.18486v1) | [PDF](https://arxiv.org/pdf/2604.18486v1.pdf) | [Project Page](https://xiaomi-embodied-intelligence.github.io/OneVL)

<details>
<summary>Abstract</summary>

Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world,...

</details>

---

### [Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models](https://arxiv.org/abs/2604.18107v1)

**Authors:** Zehua Zang, Xi Wang, Fuchun Sun, Xiao Xu, Lixiang Lium et al. (7 authors)

**Published:** 2026-04-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.18107v1) | [PDF](https://arxiv.org/pdf/2604.18107v1.pdf) | [GitHub](https://github.com/zhoujiahuan1991/CVPR2026-PDF}{https://github.com/zhoujiahuan1991/CVPR2026-PDF})

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. We attribute this brittleness to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns. We propose Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision p...

</details>

---

### [ST-$π$: Structured SpatioTemporal VLA for Robotic Manipulation](https://arxiv.org/abs/2604.17880v1)

**Authors:** Chuanhao Ma, Hanyu Zhou, Shihan Peng, Yan Li, Tao Gu et al. (6 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.17880v1) | [PDF](https://arxiv.org/pdf/2604.17880v1.pdf) | [GitHub](https://github.com/chuanhaoma/ST-pi)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved great success on general robotic tasks, but still face challenges in fine-grained spatiotemporal manipulation. Typically, existing methods mainly embed spatiotemporal knowledge into visual and action representations, and directly perform a cross-modal mapping for step-level action prediction. However, such spatiotemporal reasoning remains largely implicit, making it difficult to handle multiple sequential behaviors with explicit spatiotemporal bo...

</details>

---

### [OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models](https://arxiv.org/abs/2604.17915v1)

**Authors:** Yiwei Zhang, Xuesong Chen, Jin Gao, Hanshi Wang, Fudong Ge et al. (8 authors)

**Published:** 2026-04-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.17915v1) | [PDF](https://arxiv.org/pdf/2604.17915v1.pdf) | [GitHub](https://github.com/Z1zyw/OneDrive)

<details>
<summary>Abstract</summary>

Vision-Language Models(VLMs) excel at autoregressive text generation, yet end-to-end autonomous driving requires multi-task learning with structured outputs and heterogeneous decoding behaviors, such as autoregressive language generation, parallel object detection and trajectory regression. To accommodate these differences, existing systems typically introduce separate or cascaded decoders, resulting in architectural fragmentation and limited backbone reuse. In this work, we present a unified au...

</details>

---

## Other Recent Papers

### [XEmbodied: A Foundation Model with Enhanced Geometric and Physical Cues for Large-Scale Embodied Environments](https://arxiv.org/abs/2604.18484v1)

**Authors:** Kangan Qian, ChuChu Xie, Yang Zhong, Jingrui Pang, Siwen Jiao et al. (16 authors)

**Published:** 2026-04-20 | **Categories:** cs.CV, cs.MM, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.18484v1) | [PDF](https://arxiv.org/pdf/2604.18484v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models drive next-generation autonomous systems, but training them requires scalable, high-quality annotations from complex environments. Current cloud pipelines rely on generic vision-language models (VLMs) that lack geometric reasoning and domain semantics due to their 2D image-text pretraining. To address this mismatch, we propose XEmbodied, a cloud-side foundation model that endows VLMs with intrinsic 3D geometric awareness and interaction with physical cues (e.g...

</details>

---

### [Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2604.18000v1)

**Authors:** Haiweng Xu, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Ziheng Xi et al. (6 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.18000v1) | [PDF](https://arxiv.org/pdf/2604.18000v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models report impressive success rates on standard robotic benchmarks, fueling optimism about general-purpose physical intelligence. However, recent evidence suggests a systematic misalignment between standard benchmark success and true embodied reasoning, raising the question of whether these high scores reflect genuine cognitive capability. To address this gap, we introduce BeTTER, a diagnostic Benchmark for Testing True Embodied Reasoning in robotic policie...

</details>

---

### [Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study](https://arxiv.org/abs/2604.17896v1)

**Authors:** Yubai Wei, Chen Wu, Hashem Haghbayan

**Published:** 2026-04-20 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.17896v1) | [PDF](https://arxiv.org/pdf/2604.17896v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map multimodal inputs directly to robot actions and are typically trained through large-scale imitation learning. While this paradigm has shown strong performance, prevailing VLA training procedures do not explicitly supervise hard physical constraints such as obstacle avoidance or kinematic feasibility. As a result, the geometric structure underlying physically feasible behavior must be inferred only implicitly from demonstrations. In this paper, we study whe...

</details>

---

### [StableIDM: Stabilizing Inverse Dynamics Model against Manipulator Truncation via Spatio-Temporal Refinement](https://arxiv.org/abs/2604.17887v1)

**Authors:** Kerui Li, Zhe Jing, Xiaofeng Wang, Zheng Zhu, Yukun Zhou et al. (9 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.17887v1) | [PDF](https://arxiv.org/pdf/2604.17887v1.pdf)

<details>
<summary>Abstract</summary>

Inverse Dynamics Models (IDMs) map visual observations to low-level action commands, serving as central components for data labeling and policy execution in embodied AI. However, their performance degrades severely under manipulator truncation, a common failure mode that makes state recovery ill-posed and leads to unstable control. We present StableIDM, a spatio-temporal framework that refines features from visual inputs to stabilize action predictions under such partial observability. StableIDM...

</details>

---

### [OFlow: Injecting Object-Aware Temporal Flow Matching for Robust Robotic Manipulation](https://arxiv.org/abs/2604.17876v1)

**Authors:** Kuanning Wang, Ke Fan, Chenhao Qiu, Zeyu Shangguan, Yuqian Fu et al. (8 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.17876v1) | [PDF](https://arxiv.org/pdf/2604.17876v1.pdf)

<details>
<summary>Abstract</summary>

Robust robotic manipulation requires not only predicting how the scene evolves over time, but also recognizing task-relevant objects in complex scenes. However, existing VLA models face two limitations. They typically act only on the current frame, while future prediction and object-aware reasoning are often learned in separate latent spaces. We propose OFlow (injecting Object-Aware Temporal Flow Matching into VLAs), a framework that addresses both limitations by unifying temporal foresight and ...

</details>

---

### [ReFineVLA: Multimodal Reasoning-Aware Generalist Robotic Policies via Teacher-Guided Fine-Tuning](https://arxiv.org/abs/2604.17800v1)

**Authors:** Tuan Van Vo, Tan Q. Nguyen, Khang Nguyen, Nhat Xuan Tran, Duy H. M. Nguyen et al. (8 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.17800v1) | [PDF](https://arxiv.org/pdf/2604.17800v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have gained much attention from the research community thanks to their strength in translating multimodal observations with linguistic instructions into desired robotic actions. Despite their advancements, VLAs often overlook explicit reasoning and learn the functional input-action mappings, omitting crucial logical steps, which are especially pronounced in interpretability and generalization for complex, long-horizon manipulation tasks. In this work, we propo...

</details>

---

### [AnchorRefine: Synergy-Manipulation Based on Trajectory Anchor and Residual Refinement for Vision-Language-Action Models](https://arxiv.org/abs/2604.17787v1)

**Authors:** Tingzheng Jia, Kan Guo, Lanping Qian, Yongli Hu, Daxin Tian et al. (9 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.17787v1) | [PDF](https://arxiv.org/pdf/2604.17787v1.pdf)

<details>
<summary>Abstract</summary>

Precision-critical manipulation requires both global trajectory organization and local execution correction, yet most vision-language-action (VLA) policies generate actions within a single unified space. This monolithic formulation forces macro-level transport and micro-level refinement to be optimized under the same objective, causing large motions to dominate learning while suppressing small but failure-critical corrective signals. In contrast, human manipulation is structured by global moveme...

</details>

---

### [OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL](https://arxiv.org/abs/2604.17706v1)

**Authors:** Haoxiang Jie, Yaoyuan Yan, Xiangyu Wei, Kailin Wang, Hongjie Yan et al. (7 authors)

**Published:** 2026-04-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.17706v1) | [PDF](https://arxiv.org/pdf/2604.17706v1.pdf)

<details>
<summary>Abstract</summary>

Visual-Language-Action (VLA) models represent a paradigm shift in embodied AI, yet existing frameworks often struggle with imprecise spatial perception, suboptimal multimodal fusion, and instability in reinforcement learning. To bridge these gaps, we propose OmniVLA-RL, a novel architecture that leverages a Mix-of-Transformers (MoT) design to synergistically integrate reasoning, spatial, and action experts. Furthermore, we introduce Flow-GSPO, which reformulates flow matching as a Stochastic Dif...

</details>

---

### [Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception](https://arxiv.org/abs/2604.17651v1)

**Authors:** Siyuan Meng, Chengbo Ai

**Published:** 2026-04-19 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.17651v1) | [PDF](https://arxiv.org/pdf/2604.17651v1.pdf)

<details>
<summary>Abstract</summary>

World models, generative AI systems that simulate how environments evolve, are transforming autonomous driving, yet all existing approaches adopt an ego-vehicle perspective, leaving the infrastructure viewpoint unexplored. We argue that infrastructure-centric world models offer a fundamentally complementary capability: the bird's-eye, multi-sensor, persistent viewpoint that roadside systems uniquely possess. Central to our thesis is a spatio-temporal complementarity: fixed roadside sensors excel...

</details>

---
