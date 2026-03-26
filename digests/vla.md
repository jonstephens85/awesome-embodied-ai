# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-26 22:18 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Unleashing Vision-Language Semantics for Deepfake Video Detection](https://arxiv.org/abs/2603.24454v1)

**Authors:** Jiawen Zhu, Yunqi Miao, Xueyi Zhang, Jiankang Deng, Guansong Pang

**Published:** 2026-03-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.24454v1) | [PDF](https://arxiv.org/pdf/2603.24454v1.pdf) | [GitHub](https://github.com/mala-lab/VLAForge)

<details>
<summary>Abstract</summary>

Recent Deepfake Video Detection (DFD) studies have demonstrated that pre-trained Vision-Language Models (VLMs) such as CLIP exhibit strong generalization capabilities in detecting artifacts across different identities. However, existing approaches focus on leveraging visual features only, overlooking their most distinctive strength -- the rich vision-language semantics embedded in the latent space. We propose VLAForge, a novel DFD framework that unleashes the potential of such cross-modal semant...

</details>

---

### [SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060v1)

**Authors:** Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu

**Published:** 2026-03-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24060v1) | [PDF](https://arxiv.org/pdf/2603.24060v1.pdf) | [Project Page](and) | [GitHub](https://github.com/LZY-1021/SOMA)

<details>
<summary>Abstract</summary>

Despite the promise of Vision-Language-Action (VLA) models as generalist robotic controllers, their robustness against perceptual noise and environmental variations in out-of-distribution (OOD) tasks remains fundamentally limited by the absence of long-term memory, causal failure attribution, and dynamic intervention capability. To address this, we propose SOMA, a Strategic Orchestration and Memory-Augmented System that upgrades frozen VLA policies for robust in-context adaptation without parame...

</details>

---

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

## Other Recent Papers

### [TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models](https://arxiv.org/abs/2603.24584v1)

**Authors:** Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu et al. (8 authors)

**Published:** 2026-03-25 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24584v1) | [PDF](https://arxiv.org/pdf/2603.24584v1.pdf)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) policies have shown strong progress in mapping language instructions and visual observations to robotic actions, yet their reliability degrades in cluttered scenes with distractors. By analyzing failure cases, we find that many errors do not arise from infeasible motions, but from instance-level grounding failures: the policy often produces a plausible grasp trajectory that lands slightly off-target or even on the wrong object instance. To address this issue, we pr...

</details>

---

### [3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models](https://arxiv.org/abs/2603.24393v1)

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei et al. (11 authors)

**Published:** 2026-03-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24393v1) | [PDF](https://arxiv.org/pdf/2603.24393v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models leverage Multimodal Large Language Models (MLLMs) for robotic control, but recent studies reveal that MLLMs exhibit limited spatial intelligence due to training predominantly on 2D data, resulting in inadequate 3D perception for manipulation tasks. While recent approaches incorporate specialized 3D vision models such as VGGT to enhance spatial understanding, they employ diverse integration mechanisms without systematic investigation, leaving the optimal fusion...

</details>

---

### [LongTail Driving Scenarios with Reasoning Traces: The KITScenes LongTail Dataset](https://arxiv.org/abs/2603.23607v1)

**Authors:** Royden Wagner, Omer Sahin Tas, Jaime Villa, Felix Hauser, Yinzhe Shen et al. (21 authors)

**Published:** 2026-03-24 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.23607v1) | [PDF](https://arxiv.org/pdf/2603.23607v1.pdf)

<details>
<summary>Abstract</summary>

In real-world domains such as self-driving, generalization to rare scenarios remains a fundamental challenge. To address this, we introduce a new dataset designed for end-to-end driving that focuses on long-tail driving events. We provide multi-view video data, trajectories, high-level instructions, and detailed reasoning traces, facilitating in-context learning and few-shot generalization. The resulting benchmark for multimodal models, such as VLMs and VLAs, goes beyond safety and comfort metri...

</details>

---

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
