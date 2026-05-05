# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-05 17:23 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881v1)

**Authors:** Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu et al. (29 authors)

**Published:** 2026-05-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02881v1) | [PDF](https://arxiv.org/pdf/2605.02881v1.pdf) | [Project Page](https://allenai.org/blog/molmoact2)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deploym...

</details>

---

### [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](https://arxiv.org/abs/2605.02757v1)

**Authors:** Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You et al. (8 authors)

**Published:** 2026-05-04 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02757v1) | [PDF](https://arxiv.org/pdf/2605.02757v1.pdf) | [GitHub](https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically rely on large-scale real-world videos, whereas simulated data, despite being inexpensive and highly parallelizable to collect, often suffers from a substantial visual domain gap and limited environmental diversity, resulting in weak real-world generalization. We present an efficient video augmentation framework that converts simulated VLA videos into realistic training videos while preserving task semantics and action trajectories. Our pipeline extra...

</details>

---

## Other Recent Papers

### [Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference](https://arxiv.org/abs/2605.02739v1)

**Authors:** Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin et al. (15 authors)

**Published:** 2026-05-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02739v1) | [PDF](https://arxiv.org/pdf/2605.02739v1.pdf)

<details>
<summary>Abstract</summary>

Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We instantiate Latent Bridge on two architecturally distinct...

</details>

---

### [CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation](https://arxiv.org/abs/2605.02600v1)

**Authors:** Berk Çiçek, Mert K. Er, Özgür S. Öğüz

**Published:** 2026-05-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.02600v1) | [PDF](https://arxiv.org/pdf/2605.02600v1.pdf)

<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) and Vision-Language Models (VLMs) demonstrate remarkable capabilities in high-level reasoning and semantic understanding, applying them directly to contact-rich manipulation remains a challenge due to their lack of explicit physical grounding and inability to perform adaptive control. To bridge this gap, we propose CoRAL (Contact-Rich Adaptive LLM-based control), a modular framework that enables zero-shot planning by decoupling high-level reasoning from low-lev...

</details>

---

### [VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation](https://arxiv.org/abs/2605.02037v1)

**Authors:** Zijian An, Hadi Khezam, Bill Cai, Ran Yang, Shijie Geng et al. (9 authors)

**Published:** 2026-05-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.02037v1) | [PDF](https://arxiv.org/pdf/2605.02037v1.pdf)

<details>
<summary>Abstract</summary>

We present VILAS, a fully low-cost, modular robotic manipulation platform designed to support end-to-end vision-language-action (VLA) policy learning and deployment on accessible hardware. The system integrates a Fairino FR5 collaborative arm, a Jodell RG52-50 electric gripper, and a dual-camera perception module, unified through a ZMQ-based communication architecture that seamlessly coordinates teleoperation, data collection, and policy deployment within a single framework. To enable safe manip...

</details>

---

### [Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection](https://arxiv.org/abs/2605.01948v1)

**Authors:** Om Mandhane, Bipin Yadav, Sangeetha Prasanna Ram, Gopalakrishnan Narayanan

**Published:** 2026-05-03 | **Categories:** cs.RO, cs.AI, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2605.01948v1) | [PDF](https://arxiv.org/pdf/2605.01948v1.pdf)

<details>
<summary>Abstract</summary>

Collecting diverse, high-quality manipulation data for Vision-Language-Action (VLA) model training remains prohibitively expensive for many research groups, as existing teleoperation frameworks rely on specialized hardware or are tightly coupled to specific robot platforms. We present Phone2Act, a low-cost, hardware-agnostic teleoperation framework that transforms a commodity smartphone into a 6-DoF robot controller via Google ARCore. Built on a modular ROS 2 architecture, Phone2Act decouples co...

</details>

---

### [Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation](https://arxiv.org/abs/2605.01772v1)

**Authors:** Zhilong Zhang, Wenyu Luo, Haonan Wang, Yifei Sheng, Yidi Wang et al. (12 authors)

**Published:** 2026-05-03 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.01772v1) | [PDF](https://arxiv.org/pdf/2605.01772v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied intelligence, enabling robots to perform tasks based on natural language instructions and current visual input. However, existing VLA models struggle with long-horizon tasks due to compounding errors. Prior methods decompose tasks into subtasks of fixed granularity, which cannot adapt to the varying complexity of execution states, limiting their robustness in long-horizon tasks. To overcome this, we introduce An...

</details>

---
