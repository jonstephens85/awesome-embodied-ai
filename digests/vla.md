# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-14 22:14 UTC

**Papers found:** 8

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
