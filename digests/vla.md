# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-19 16:58 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control](https://arxiv.org/abs/2603.17834v1)

**Authors:** Zunzhe Zhang, Runhan Huang, Yicheng Liu, Shaoting Zhu, Linzhan Mou et al. (6 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17834v1) | [PDF](https://arxiv.org/pdf/2603.17834v1.pdf) | [Project Page](https://hrh6666.github.io/GeCO/)

<details>
<summary>Abstract</summary>

Diffusion models and flow matching have become a cornerstone of robotic imitation learning, yet they suffer from a structural inefficiency where inference is often bound to a fixed integration schedule that is agnostic to state complexity. This paradigm forces the policy to expend the same computational budget on trivial motions as it does on complex tasks. We introduce Generative Control as Optimization (GeCO), a time-unconditional framework that transforms action synthesis from trajectory inte...

</details>

---

### [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666v1)

**Authors:** Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao

**Published:** 2026-03-17 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.16666v1) | [PDF](https://arxiv.org/pdf/2603.16666v1.pdf) | [Project Page](https://yuantianyuan01.github.io/FastWAM/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance. In this paper, we ask whether WAMs need explicit f...

</details>

---

### [Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation](https://arxiv.org/abs/2603.16086v1)

**Authors:** Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu, Hesheng Wang

**Published:** 2026-03-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16086v1) | [PDF](https://arxiv.org/pdf/2603.16086v1.pdf) | [Project Page](are)

<details>
<summary>Abstract</summary>

While recent Vision-Language-Action (VLA) models have begun to incorporate audio, they typically treat sound as static pre-execution prompts or focus exclusively on human speech. This leaves a significant gap in real-time, sound-centric manipulation where fleeting environmental acoustics provide critical state verification during task execution. Consequently, key sounds are easily missed due to low-frequency updates or system latency. This problem is exacerbated by action chunking with open-loop...

</details>

---

## Other Recent Papers

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

### [Enabling Dynamic Tracking in Vision-Language-Action Models via Time-Discrete and Time-Continuous Velocity Feedforward](https://arxiv.org/abs/2603.16218v1)

**Authors:** Johannes Hechtl, Philipp Schmitt, Georg von Wichert, Wolfram Burgard

**Published:** 2026-03-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.16218v1) | [PDF](https://arxiv.org/pdf/2603.16218v1.pdf)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models have shown great promise for robot manipulation, their deployment on rigid industrial robots remains challenging due to the inherent trade-off between compliance and responsiveness. Standard Behavior Cloning (BC) approaches predict discrete poses at low frequencies, omitting the velocity and acceleration feedforward terms typically used by low-level compliant controllers. This requires to rely on high stiffness for accurate tracking, thereby sacrificing ...

</details>

---

### [Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation](https://arxiv.org/abs/2603.16044v1)

**Authors:** Dongik Shin

**Published:** 2026-03-17 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.16044v1) | [PDF](https://arxiv.org/pdf/2603.16044v1.pdf)

<details>
<summary>Abstract</summary>

Generalization remains a core challenge in embodied AI, as robots must adapt to diverse environments. While OpenVLA represents the State-of-the-Art (SOTA) in Vision-Language-Action models by leveraging large-scale pre-training, its zero-shot performance can be limited when encountering completely new environments. This paper proposes a parameter-efficient fine-tuning strategy to enhance the linguistic generalization of OpenVLA by synthesizing a general instruction set for the Bridge Dataset V2. ...

</details>

---
