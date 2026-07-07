# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-07 22:51 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396v1)

**Authors:** Wenhao Li, Xueying Jiang, Quanhao Qian, Deli Zhao, Shijian Lu et al. (7 authors)

**Published:** 2026-07-06 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.05396v1) | [PDF](https://arxiv.org/pdf/2607.05396v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/CamVLA/)

<details>
<summary>Abstract</summary>

Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...

</details>

---

### [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377v1)

**Authors:** Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai et al. (13 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.05377v1) | [PDF](https://arxiv.org/pdf/2607.05377v1.pdf) | [Project Page](https://steinate.github.io/cortex.github.io/)

<details>
<summary>Abstract</summary>

While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...

</details>

---

### [Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning](https://arxiv.org/abs/2607.04681v1)

**Authors:** Matthew Foutter, Matteo Cercola, Lena Wild, Yunshan Wang, Michelle Li et al. (7 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04681v1) | [PDF](https://arxiv.org/pdf/2607.04681v1.pdf) | [Project Page](https://mjf-su.github.io/pinocchio/)

<details>
<summary>Abstract</summary>

Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We arg...

</details>

---

### [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](https://arxiv.org/abs/2607.04517v1)

**Authors:** Damir Shodiev, Aleksei Staroverov, Nikita Kachaev, Alexey K. Kovalev, Aleksandr I. Panov

**Published:** 2026-07-05 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04517v1) | [PDF](https://arxiv.org/pdf/2607.04517v1.pdf) | [Project Page](https://tttonyalpha.github.io/vla_grounder)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies can be improved by optimizing language space rather than updating action weights. Our method introduces a language-conditioning space policy...

</details>

---

### [!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics](https://arxiv.org/abs/2607.04146v1)

**Authors:** Stefan Bühler, Mark Schutera

**Published:** 2026-07-05 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.04146v1) | [PDF](https://arxiv.org/pdf/2607.04146v1.pdf) | [GitHub](https://github.com/StefanBuhler/ImperioVLAPoisoning)

<details>
<summary>Abstract</summary>

This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes ...

</details>

---

## Other Recent Papers

### [Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies](https://arxiv.org/abs/2607.05122v1)

**Authors:** Adrian Szvoren, Dimitrios Kanoulas, Nilufer Tuptuk

**Published:** 2026-07-06 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.05122v1) | [PDF](https://arxiv.org/pdf/2607.05122v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and...

</details>

---

### [DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2607.04927v1)

**Authors:** Jian Zhu, Jianjun Zhang, Taiyi Su, Tianbin Liu, Zhangyuan Wang et al. (13 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04927v1) | [PDF](https://arxiv.org/pdf/2607.04927v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted i...

</details>

---

### [CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models](https://arxiv.org/abs/2607.04816v1)

**Authors:** Yifu Xiong, Wenhao Yu, Jiaxuan Lin, Bojun Zou, Jiahao Li et al. (8 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04816v1) | [PDF](https://arxiv.org/pdf/2607.04816v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reason...

</details>

---

### [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637v1)

**Authors:** Pin Tang, Guoqing Wang, Xiangxuan Ren, Zhongdao Wang, Guodongfang Zhao et al. (7 authors)

**Published:** 2026-07-06 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.04637v1) | [PDF](https://arxiv.org/pdf/2607.04637v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe converg...

</details>

---

### [SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies](https://arxiv.org/abs/2607.04609v1)

**Authors:** Dijia Zhan, Xuemiao Xu, Jinyi Li, Jie Tang

**Published:** 2026-07-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04609v1) | [PDF](https://arxiv.org/pdf/2607.04609v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task relia...

</details>

---

### [Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning](https://arxiv.org/abs/2607.04591v1)

**Authors:** Xinchuan Qiu, Yi Yu

**Published:** 2026-07-06 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.04591v1) | [PDF](https://arxiv.org/pdf/2607.04591v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing research has primarily focused on improving model architectures, training strategies, and dataset scale, while little attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a fundamental yet overlooked aspect of imitation learning, as it direct...

</details>

---

### [PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis](https://arxiv.org/abs/2607.04880v1)

**Authors:** Dogyu Ko, Haneul Kim, Chanyoung Yeo, Dowoon Lee, Taeho Park et al. (6 authors)

**Published:** 2026-07-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.04880v1) | [PDF](https://arxiv.org/pdf/2607.04880v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in large-scale pretrained vision-language-action models have improved robot policy learning, but directly deploying such policies in user-specific environments remains challenging due to limited generalization, which inevitably requires collecting a dataset tailored to the target environment. Teleoperation yields well-aligned data but is costly and difficult to scale, whereas simulation scales easily but struggles to resemble the target environment and generate task-specific traj...

</details>

---

### [XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control](https://arxiv.org/abs/2607.04171v1)

**Authors:** Lei Iok Tong, Qingchen Xie, Wei Huang, Ying Jie Yap, Yujie Zhang et al. (8 authors)

**Published:** 2026-07-05 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.04171v1) | [PDF](https://arxiv.org/pdf/2607.04171v1.pdf)

<details>
<summary>Abstract</summary>

Large Vision-Language Models (LVLMs) have shown strong multimodal understanding and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability. Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to highly diverse behaviors. To address these limitations, we pr...

</details>

---
