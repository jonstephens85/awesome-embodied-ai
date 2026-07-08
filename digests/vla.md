# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-08 22:55 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](https://arxiv.org/abs/2607.06564v1)

**Authors:** Jiaming Liu, Qingpo Wuwu, Nuowei Han, Hao Chen, Zhuoyang Liu et al. (11 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.06564v1) | [PDF](https://arxiv.org/pdf/2607.06564v1.pdf) | [Project Page](https://lift3dvla.github.io/)

<details>
<summary>Abstract</summary>

Recently, Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse tasks. However, effective robotic manipulation in physical environments fundamentally requires geometric understanding and spatial reasoning. While some VLA approaches attempt to incorporate 3D information, they are constrained by limited data availability and geometric information loss in current 3D encoding pipelines, and fail to jointly capture 3D geometry and temporally structured actions in ...

</details>

---

### [SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models](https://arxiv.org/abs/2607.06442v1)

**Authors:** Changti Wu, Bin Yu, Zhaolong Shen, Shijie Lian, Xiaopeng Lin et al. (9 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06442v1) | [PDF](https://arxiv.org/pdf/2607.06442v1.pdf) | [GitHub](https://github.com/ChangtiWu/SIEVE}{SIEVE})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are typically trained by imitation learning on large-scale robot demonstration datasets, but more data does not necessarily yield better policies due to redundancy, noise, and uneven coverage. Existing data selection methods often assess demonstrations at either the trajectory or state-action level, missing the reusable structures that compose long-horizon behaviors. In this paper, we propose SIEVE, a structure-aware data selection method for VLA imitation lea...

</details>

---

### [From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403v1)

**Authors:** Wei Wu, Fangjing Wang, Fan Lu, He Sun, Shi Liu et al. (24 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06403v1) | [PDF](https://arxiv.org/pdf/2607.06403v1.pdf) | [Project Page](https://technology.robbyant.com/lingbot-vla-v2) | [GitHub](https://github.com/robbyant/lingbot-vla-v2)

<details>
<summary>Abstract</summary>

Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to the previous version, we revamp the data processing pipeline and curate around 60,000 hours of data for pretraining, including 50,000 hours ...

</details>

---

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

## Other Recent Papers

### [Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement](https://arxiv.org/abs/2607.06370v1)

**Authors:** Ryuji Oi, Hikari Otsuka, Kosuke Matsushima, Yuki Ichikawa, Masato Motomura et al. (7 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.06370v1) | [PDF](https://arxiv.org/pdf/2607.06370v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for generalizable robotic manipulations. In particular, flow matching-based VLA models have shown remarkable success due to their capability to generate precise and smooth action sequences and capture multimodal distributions. However, the iterative denoising process in the action head acts as a major computational bottleneck, posing a critical challenge for real-time deployment. To address this challenge, we propose Action...

</details>

---

### [Optimal Transport Q-Learning for Flow Policy Steering and Acceleration](https://arxiv.org/abs/2607.06262v1)

**Authors:** Andreas Sochopoulos, Esmeralda S. Whitammer, Nikolaos Tsagkas, João Moura, Michael Gienger et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06262v1) | [PDF](https://arxiv.org/pdf/2607.06262v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion and flow policies have recently demonstrated remarkable performance in robotic applications by accurately capturing multimodal robot trajectory distributions, especially in the context of vision language action (VLA) models. However, high quality policy performance also requires fast inference and high quality demonstrations, which are often hard to get. Lack of these leads to suboptimal policy behaviors and failure under distribution shifts. In this work we address the problem of fine...

</details>

---

### [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256v1)

**Authors:** Ke Rui, Yushen Zuo, Jiawei Wang, Haoran Jia, Jinming Ma et al. (7 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06256v1) | [PDF](https://arxiv.org/pdf/2607.06256v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon household tasks require robots to compose many language-conditioned skills, yet the boundary between consecutive skills is rarely explicit. A skill may satisfy its own postcondition while leaving the robot, objects, or camera views in a state from which the next skill cannot reliably start. We study this semantic handoff problem in BEHAVIOR-1K through an agent-orchestrated vision-language-action execution harness. The harness invokes $π_{0.5}$-based skill checkpoints trained from cl...

</details>

---

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
