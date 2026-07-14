# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-14 17:13 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models](https://arxiv.org/abs/2607.10655v1)

**Authors:** Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete, Matei-Victor Coldea, Chen Liang et al. (12 authors)

**Published:** 2026-07-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.10655v1) | [PDF](https://arxiv.org/pdf/2607.10655v1.pdf)

<details>
<summary>Abstract</summary>

Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We identify this failure mode as shortcut learning: the tendency to exploit predictive but non-causal correlations in the training distribution r...

</details>

---
