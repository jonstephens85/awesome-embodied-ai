# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-13 22:23 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning](https://arxiv.org/abs/2602.12099v1)

**Authors:**  GigaBrain Team, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao et al. (25 authors)

**Published:** 2026-02-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.12099v1) | [PDF](https://arxiv.org/pdf/2602.12099v1.pdf) | [Project Page](https://gigabrain05m.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models that directly predict multi-step action chunks from current observations face inherent limitations due to constrained scene understanding and weak future anticipation capabilities. In contrast, video world models pre-trained on web-scale video corpora exhibit robust spatiotemporal reasoning and accurate future prediction, making them a natural foundation for enhancing VLA learning. Therefore, we propose \textit{GigaBrain-0.5M*}, a VLA model trained via world m...

</details>

---

### [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063v1)

**Authors:** Yanjiang Guo, Tony Lee, Lucy Xiaoyang Shi, Jianyu Chen, Percy Liang et al. (6 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.12063v1) | [PDF](https://arxiv.org/pdf/2602.12063v1.pdf) | [Project Page](https://sites.google.com/view/vla-w)

<details>
<summary>Abstract</summary>

The goal of this paper is to improve the performance and reliability of vision-language-action (VLA) models through iterative online interaction. Since collecting policy rollouts in the real world is expensive, we investigate whether a learned simulator-specifically, an action-conditioned video generation model-can be used to generate additional rollout data. Unfortunately, existing world models lack the physical fidelity necessary for policy improvement: they are predominantly trained on demons...

</details>

---

### [ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation](https://arxiv.org/abs/2602.11598v1)

**Authors:** Zedong Chu, Shichao Xie, Xiaolong Wu, Yanfen Shen, Minghua Luo et al. (44 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.11598v1) | [PDF](https://arxiv.org/pdf/2602.11598v1.pdf) | [Project Page](https://amap-cvlab.github.io/ABot-Navigation/ABot-N0/)

<details>
<summary>Abstract</summary>

Embodied navigation has long been fragmented by task-specific architectures. We introduce ABot-N0, a unified Vision-Language-Action (VLA) foundation model that achieves a ``Grand Unification'' across 5 core tasks: Point-Goal, Object-Goal, Instruction-Following, POI-Goal, and Person-Following. ABot-N0 utilizes a hierarchical ``Brain-Action'' architecture, pairing an LLM-based Cognitive Brain for semantic reasoning with a Flow Matching-based Action Expert for precise, continuous trajectory generat...

</details>

---

### [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075v1)

**Authors:** Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin et al. (13 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11075v1) | [PDF](https://arxiv.org/pdf/2602.11075v1.pdf) | [Project Page](https://opendrivelab.com/kai0-rl/)

<details>
<summary>Abstract</summary>

Despite the sustained scaling on model capacity and data acquisition, Vision-Language-Action (VLA) models remain brittle in contact-rich and dynamic manipulation tasks, where minor execution deviations can compound into failures. While reinforcement learning (RL) offers a principled path to robustness, on-policy RL in the physical world is constrained by safety risk, hardware cost, and environment reset. To bridge this gap, we present RISE, a scalable framework of robotic reinforcement learning ...

</details>

---

### [ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning](https://arxiv.org/abs/2602.11236v1)

**Authors:** Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Dekang Qi et al. (14 authors)

**Published:** 2026-02-11 | **Categories:** cs.CV, cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11236v1) | [PDF](https://arxiv.org/pdf/2602.11236v1.pdf) | [Project Page](https://amap-cvlab.github.io/ABot-Manipulation/) | [GitHub](https://github.com/amap-cvlab/ABot-Manipulation)

<details>
<summary>Abstract</summary>

Building general-purpose embodied agents across diverse hardware remains a central challenge in robotics, often framed as the ''one-brain, many-forms'' paradigm. Progress is hindered by fragmented data, inconsistent representations, and misaligned training objectives. We present ABot-M0, a framework that builds a systematic data curation pipeline while jointly optimizing model architecture and training strategies, enabling end-to-end transformation of heterogeneous raw data into unified, efficie...

</details>

---

### [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983v2)

**Authors:** Qian Long, Yueze Wang, Jiaxi Song, Junbo Zhang, Peiyan Li et al. (16 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10983v2) | [PDF](https://arxiv.org/pdf/2602.10983v2.pdf) | [Project Page](\href{https://vista-wm.github.io/}{https://vista-wm.github.io})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are promising for generalist robot manipulation but remain brittle in out-of-distribution (OOD) settings, especially with limited real-robot data. To resolve the generalization bottleneck, we introduce a hierarchical Vision-Language-Action framework \our{} that leverages the generalization of large-scale pre-trained world model for robust and generalizable VIsual Subgoal TAsk decomposition VISTA. Our hierarchical framework \our{} consists of a world model as t...

</details>

---

### [LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer](https://arxiv.org/abs/2602.10556v1)

**Authors:** Lihan Zha, Asher J. Hancock, Mingtong Zhang, Tenny Yin, Yixuan Huang et al. (8 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.10556v1) | [PDF](https://arxiv.org/pdf/2602.10556v1.pdf) | [Project Page](https://lap-vla.github.io)

<details>
<summary>Abstract</summary>

A long-standing goal in robotics is a generalist policy that can be deployed zero-shot on new robot embodiments without per-embodiment adaptation. Despite large-scale multi-embodiment pre-training, existing Vision-Language-Action models (VLAs) remain tightly coupled to their training embodiments and typically require costly fine-tuning. We introduce Language-Action Pre-training (LAP), a simple recipe that represents low-level robot actions directly in natural language, aligning action supervisio...

</details>

---

## Other Recent Papers

### [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281v1)

**Authors:** Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini et al. (7 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2602.12281v1) | [PDF](https://arxiv.org/pdf/2602.12281v1.pdf)

<details>
<summary>Abstract</summary>

The long-standing vision of general-purpose robots hinges on their ability to understand and act upon natural language instructions. Vision-Language-Action (VLA) models have made remarkable progress toward this goal, yet their generated actions can still misalign with the given instructions. In this paper, we investigate test-time verification as a means to shrink the "intention-action gap.'' We first characterize the test-time scaling law for embodied instruction following and demonstrate that ...

</details>

---

### [HoloBrain-0 Technical Report](https://arxiv.org/abs/2602.12062v1)

**Authors:** Xuewu Lin, Tianwei Lin, Yun Du, Hongyu Xie, Yiwei Jin et al. (15 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.12062v1) | [PDF](https://arxiv.org/pdf/2602.12062v1.pdf)

<details>
<summary>Abstract</summary>

In this work, we introduce HoloBrain-0, a comprehensive Vision-Language-Action (VLA) framework that bridges the gap between foundation model research and reliable real-world robot deployment. The core of our system is a novel VLA architecture that explicitly incorporates robot embodiment priors, including multi-view camera parameters and kinematic descriptions (URDF), to enhance 3D spatial reasoning and support diverse embodiments. We validate this design through a scalable ``pre-train then post...

</details>

---

### [Robot-DIFT: Distilling Diffusion Features for Geometrically Consistent Visuomotor Control](https://arxiv.org/abs/2602.11934v1)

**Authors:** Yu Deng, Yufeng Jin, Xiaogang Jia, Jiahong Xue, Gerhard Neumann et al. (6 authors)

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11934v1) | [PDF](https://arxiv.org/pdf/2602.11934v1.pdf)

<details>
<summary>Abstract</summary>

We hypothesize that a key bottleneck in generalizable robot manipulation is not solely data scale or policy capacity, but a structural mismatch between current visual backbones and the physical requirements of closed-loop control. While state-of-the-art vision encoders (including those used in VLAs) optimize for semantic invariance to stabilize classification, manipulation typically demands geometric sensitivity the ability to map millimeter-level pose shifts to predictable feature changes. Thei...

</details>

---

### [JEPA-VLA: Video Predictive Embedding is Needed for VLA Models](https://arxiv.org/abs/2602.11832v1)

**Authors:** Shangchen Miao, Ningya Feng, Jialong Wu, Ye Lin, Xu He et al. (7 authors)

**Published:** 2026-02-12 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11832v1) | [PDF](https://arxiv.org/pdf/2602.11832v1.pdf)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models built upon pretrained vision-language models (VLMs) have achieved significant improvements in robotic manipulation. However, current VLAs still suffer from low sample efficiency and limited generalization. This paper argues that these limitations are closely tied to an overlooked component, pretrained visual representation, which offers insufficient knowledge on both aspects of environment understanding and policy prior. Through an in-depth analysis, we...

</details>

---

### [When would Vision-Proprioception Policies Fail in Robotic Manipulation?](https://arxiv.org/abs/2602.12032v1)

**Authors:** Jingxian Lu, Wenke Xia, Yuxuan Wu, Zhiwu Lu, Di Hu

**Published:** 2026-02-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.12032v1) | [PDF](https://arxiv.org/pdf/2602.12032v1.pdf)

<details>
<summary>Abstract</summary>

Proprioceptive information is critical for precise servo control by providing real-time robotic states. Its collaboration with vision is highly expected to enhance performances of the manipulation policy in complex tasks. However, recent studies have reported inconsistent observations on the generalization of vision-proprioception policies. In this work, we investigate this by conducting temporally controlled experiments. We found that during task sub-phases that robot's motion transitions, whic...

</details>

---

### [H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model](https://arxiv.org/abs/2602.11291v1)

**Authors:** Wenyuan Chen, Jinbang Huang, Oscar Pang, Zhiyuan Li, Xiao Hu et al. (11 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11291v1) | [PDF](https://arxiv.org/pdf/2602.11291v1.pdf)

<details>
<summary>Abstract</summary>

World models are becoming central to robotic planning and control, as they enable prediction of future state transitions. Existing approaches often emphasize video generation or natural language prediction, which are difficult to directly ground in robot actions and suffer from compounding errors over long horizons. Traditional task and motion planning relies on symbolic logic world models, such as planning domains, that are robot-executable and robust for long-horizon reasoning. However, these ...

</details>

---

### [RADAR: Benchmarking Vision-Language-Action Generalization via Real-World Dynamics, Spatial-Physical Intelligence, and Autonomous Evaluation](https://arxiv.org/abs/2602.10980v1)

**Authors:** Yuhao Chen, Zhihao Zhan, Xiaoxin Lin, Zijian Song, Hao Liu et al. (14 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10980v1) | [PDF](https://arxiv.org/pdf/2602.10980v1.pdf)

<details>
<summary>Abstract</summary>

VLA models have achieved remarkable progress in embodied intelligence; however, their evaluation remains largely confined to simulations or highly constrained real-world settings. This mismatch creates a substantial reality gap, where strong benchmark performance often masks poor generalization in diverse physical environments. We identify three systemic shortcomings in current benchmarking practices that hinder fair and reliable model comparison. (1) Existing benchmarks fail to model real-world...

</details>

---

### [From Representational Complementarity to Dual Systems: Synergizing VLM and Vision-Only Backbones for End-to-End Driving](https://arxiv.org/abs/2602.10719v1)

**Authors:** Sining Ang, Yuguang Yang, Chenxu Dang, Canyu Chen, Cheng Chi et al. (11 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10719v1) | [PDF](https://arxiv.org/pdf/2602.10719v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) driving augments end-to-end (E2E) planning with language-enabled backbones, yet it remains unclear what changes beyond the usual accuracy--cost trade-off. We revisit this question with 3--RQ analysis in RecogDrive by instantiating the system with a full VLM and vision-only backbones, all under an identical diffusion Transformer planner. RQ1: At the backbone level, the VLM can introduce additional subspaces upon the vision-only backbones. RQ2: This unique subspace lea...

</details>

---

### [AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models](https://arxiv.org/abs/2602.10698v1)

**Authors:** Zhifeng Rao, Wenlong Chen, Lei Xie, Xia Hua, Dongfu Yin et al. (7 authors)

**Published:** 2026-02-11 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.10698v1) | [PDF](https://arxiv.org/pdf/2602.10698v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic perception and control, yet most existing approaches primarily rely on VLM trained using 2D images, which limits their spatial understanding and action grounding in complex 3D environments. To address this limitation, we propose a novel framework that integrates depth estimation into VLA models to enrich 3D feature representations. Specifically, we employ a depth estimation baseline called VGGT to extract g...

</details>

---

### [Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning](https://arxiv.org/abs/2602.10503v1)

**Authors:** Yuan Liu, Haoran Li, Shuai Tian, Yuxing Qin, Yuhui Chen et al. (8 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10503v1) | [PDF](https://arxiv.org/pdf/2602.10503v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained on large-scale and diverse datasets, VLA models demonstrate strong generalization and adaptability as general-purpose robotic policies. However, Supervised Fine-Tuning (SFT), which serves as the primary mechanism for adapting VLAs to downstream domains, requires substantial amounts of task-specific data and is prone to catastrophic forgetting. To address these limitations, we propose LifeLong-RFT, a simple yet effective Reinforcement Fine-Tuning (RFT) strategy for VLA models independe...

</details>

---
