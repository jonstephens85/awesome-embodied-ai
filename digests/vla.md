# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-15 22:48 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017v1)

**Authors:** Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang et al. (16 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13017v1) | [PDF](https://arxiv.org/pdf/2607.13017v1.pdf) | [Project Page](https://flow-wam.github.io)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy the former, and prior visual action representations overlook the temporal motion structure across fram...

</details>

---

### [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](https://arxiv.org/abs/2607.12992v1)

**Authors:** Zhao Yang, Yinan Shi, Mingyuan Yao, Wenyao Xue, Yawei Jueluo et al. (6 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12992v1) | [PDF](https://arxiv.org/pdf/2607.12992v1.pdf) | [Project Page](https://cytoderm-ai.github.io/chunkflow)

<details>
<summary>Abstract</summary>

Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. We propose Chun...

</details>

---

### [Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/abs/2607.12659v1)

**Authors:** Zebin Yang, Qi Wang, Yunhe Wang, Xiurui Guo, Bo Yu et al. (9 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12659v1) | [PDF](https://arxiv.org/pdf/2607.12659v1.pdf) | [GitHub](https://github.com/PKU-SEC-Lab/Jetson-PI)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially mask this latency by parallelizing action execution and subsequent inference, but it introduces two critical issues: perception-execution misa...

</details>

---

### [See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models](https://arxiv.org/abs/2607.11498v1)

**Authors:** Byungkun Lee, Dongyoon Hwang, Dongjin Kim, Hojoon Lee, Minho Park et al. (6 authors)

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11498v1) | [PDF](https://arxiv.org/pdf/2607.11498v1.pdf) | [Project Page](https://davian-robotics.github.io/pointmap/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating a frame mismatch between where the scene is observed and where actions are defined. The mismatch is benign under a fixed viewpoint, where the policy can memorize a single observation-to-action mapping, but grows harder as large-scale datasets aggregate demonstra...

</details>

---

## Other Recent Papers

### [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](https://arxiv.org/abs/2607.12931v1)

**Authors:** Yilun Kong, Yunpeng Qing, Guozheng Ma, Haoyu Wang, Li Shen et al. (7 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12931v1) | [PDF](https://arxiv.org/pdf/2607.12931v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts...

</details>

---

### [UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies](https://arxiv.org/abs/2607.12892v1)

**Authors:** Lirui Zhao, Modi Shi, Li Chen, Qi Liu, Ping Luo et al. (6 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12892v1) | [PDF](https://arxiv.org/pdf/2607.12892v1.pdf)

<details>
<summary>Abstract</summary>

Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states, guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames are treated as higher progress. However, this time-derived label is only a noisy proxy for physical task progress. In contact-rich manipulat...

</details>

---

### [TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/abs/2607.12571v1)

**Authors:** Pinhan Fu, Xianda Guo, Xuetao Li, Wenke Huang, Ruilin Wang et al. (8 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12571v1) | [PDF](https://arxiv.org/pdf/2607.12571v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. We study this gap through two independently proposed VLA attacks from groups with distinct ...

</details>

---

### [VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v1)

**Authors:** Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao et al. (8 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12356v1) | [PDF](https://arxiv.org/pdf/2607.12356v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures an...

</details>

---

### [Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2607.12287v1)

**Authors:** Yuzhou Wu, Yuxin Zheng, Muchun Niu, Yishan Yang, Tianhao Liu et al. (9 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.12287v1) | [PDF](https://arxiv.org/pdf/2607.12287v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies. To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation. On the ...

</details>

---

### [Technical Report on the CVPR 2026@AdvML Workshop Challenge](https://arxiv.org/abs/2607.11560v1)

**Authors:** Tianyuan Zhang, Zonglei Jing, Jiangfan Liu, Ligong Zhang, Ke Ma et al. (50 authors)

**Published:** 2026-07-13 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11560v1) | [PDF](https://arxiv.org/pdf/2607.11560v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language agents (VLAs) are increasingly used to interpret complex driving scenes and support safety-critical reasoning. This report presents the CVPR 2026@AdvML Workshop Challenge on adversarial multimodal attacks against autonomous-driving VLAs. Built on DriveLM-style multi-view visual question answering, the challenge represents each scene with six synchronized camera images and a structured collection of driving-related question-answer pairs. Participants generate adversarial images an...

</details>

---

### [Towards Predictive, Aligned, and Scalable Robot Learning](https://arxiv.org/abs/2607.11270v1)

**Authors:** Peijun Tang, Shangjin Xie, Baifu Huang, Binyan Sun, Haotian Yang et al. (9 authors)

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11270v1) | [PDF](https://arxiv.org/pdf/2607.11270v1.pdf)

<details>
<summary>Abstract</summary>

Learning, at its core, extends beyond memorization to the ability to reason and solve novel problems by navigating a space of possibilities. We introduce Lumo-2, a latent world-action model that generates actions by reasoning over world dynamics in latent space. The learned latent world dynamics capture physically grounded visual transitions, naturally encoding future possibilities and providing a unified substrate for cross-modal alignment. This formulation enables predictive reasoning akin to ...

</details>

---

### [VIA: Visual Interface Agent for Robot Control](https://arxiv.org/abs/2607.11119v1)

**Authors:** Hengyuan Hu, Priya Sundaresan, Jensen Gao, Dorsa Sadigh

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11119v1) | [PDF](https://arxiv.org/pdf/2607.11119v1.pdf)

<details>
<summary>Abstract</summary>

Robot manipulation is a complex task that requires visual understanding, physical reasoning, planning, and closed-loop control. General-purpose foundation models (FMs) have grown remarkably capable of some of these, especially vision and reasoning. To leverage this for generalist robot policies, current methods typically involve converting existing FMs into vision-language-action (VLA) models by fine-tuning on robot data to output low-level actions. However, VLAs are often orders of magnitude sm...

</details>

---

### [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](https://arxiv.org/abs/2607.11689v1)

**Authors:** Yuanzhi Liang, Xufeng Zhan, Haibin Huang, Chi Zhang, Xuelong Li

**Published:** 2026-07-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.11689v1) | [PDF](https://arxiv.org/pdf/2607.11689v1.pdf)

<details>
<summary>Abstract</summary>

Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets and tasks follow different conventions, and runtime systems e...

</details>

---
