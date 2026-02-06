# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-06 16:44 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Benchmarking Affordance Generalization with BusyBox](https://arxiv.org/abs/2602.05441v1)

**Authors:** Dean Fortier, Timothy Adamson, Tess Hellebrekers, Teresa LaScala, Kofi Ennin et al. (8 authors)

**Published:** 2026-02-05 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.05441v1) | [PDF](https://arxiv.org/pdf/2602.05441v1.pdf) | [Project Page](https://microsoft.github.io/BusyBox)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have been attracting the attention of researchers and practitioners thanks to their promise of generalization. Although single-task policies still offer competitive performance, VLAs are increasingly able to handle commands and environments unseen in their training set. While generalization in vision and language space is undoubtedly important for robust versatile behaviors, a key meta-skill VLAs need to possess is affordance generalization -- the ability to m...

</details>

---

### [VISTA: Enhancing Visual Conditioning via Track-Following Preference Optimization in Vision-Language-Action Models](https://arxiv.org/abs/2602.05049v1)

**Authors:** Yiye Chen, Yanan Jian, Xiaoyi Dong, Shuxin Cao, Jing Wu et al. (8 authors)

**Published:** 2026-02-04 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.05049v1) | [PDF](https://arxiv.org/pdf/2602.05049v1.pdf) | [Project Page](https://vista-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong performance across a wide range of robotic manipulation tasks. Despite the success, extending large pretrained Vision-Language Models (VLMs) to the action space can induce vision-action misalignment, where action predictions exhibit weak dependence on the current visual state, leading to unreliable action outputs. In this work, we study VLA models through the lens of visual conditioning and empirically show that successful rollouts con...

</details>

---

### [GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning](https://arxiv.org/abs/2602.04315v1)

**Authors:** Guoqing Ma, Siheng Wang, Zeyu Zhang, Shan Yu, Hao Tang

**Published:** 2026-02-04 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.04315v1) | [PDF](https://arxiv.org/pdf/2602.04315v1.pdf) | [Project Page](https://aigeeksgroup.github.io/GeneralVLA) | [GitHub](https://github.com/AIGeeksGroup/GeneralVLA)

<details>
<summary>Abstract</summary>

Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is that the models exhibit limited zero-shot capability, which hampers their ability to generalize effectively to unseen scenarios. In this work, we propose GeneralVLA (Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning), a hierarchical vision-language-...

</details>

---

### [Reshaping Action Error Distributions for Reliable Vision-Language-Action Models](https://arxiv.org/abs/2602.04228v1)

**Authors:** Shuanghao Bai, Dakai Wang, Cheng Chi, Wanqi Zhou, Jing Lyu et al. (11 authors)

**Published:** 2026-02-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.04228v1) | [PDF](https://arxiv.org/pdf/2602.04228v1.pdf) | [Project Page](https://cognition2actionlab.github.io/VLA-TMEE.github.io/)

<details>
<summary>Abstract</summary>

In robotic manipulation, vision-language-action (VLA) models have emerged as a promising paradigm for learning generalizable and scalable robot policies. Most existing VLA frameworks rely on standard supervised objectives, typically cross-entropy for discrete actions and mean squared error (MSE) for continuous action regression, which impose strong pointwise constraints on individual predictions. In this work, we focus on continuous-action VLA models and move beyond conventional MSE-based regres...

</details>

---

### [Natural Language Instructions for Scene-Responsive Human-in-the-Loop Motion Planning in Autonomous Driving using Vision-Language-Action Models](https://arxiv.org/abs/2602.04184v1)

**Authors:** Angel Martinez-Sanchez, Parthib Roy, Ross Greer

**Published:** 2026-02-04 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.04184v1) | [PDF](https://arxiv.org/pdf/2602.04184v1.pdf) | [GitHub](https://github.com/Mi3-Lab/doScenes-VLM-Planning)

<details>
<summary>Abstract</summary>

Instruction-grounded driving, where passenger language guides trajectory planning, requires vehicles to understand intent before motion. However, most prior instruction-following planners rely on simulation or fixed command vocabularies, limiting real-world generalization. doScenes, the first real-world dataset linking free-form instructions (with referentiality) to nuScenes ground-truth motion, enables instruction-conditioned planning. In this work, we adapt OpenEMMA, an open-source MLLM-based ...

</details>

---

## Other Recent Papers

### [RL-VLA$^3$: Reinforcement Learning VLA Accelerating via Full Asynchronism](https://arxiv.org/abs/2602.05765v1)

**Authors:** Zhong Guan, Haoran Sun, Yongjian Guo, Shuai Di, Xiaodong Bai et al. (21 authors)

**Published:** 2026-02-05 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.05765v1) | [PDF](https://arxiv.org/pdf/2602.05765v1.pdf)

<details>
<summary>Abstract</summary>

In recent years, Vision-Language-Action (VLA) models have emerged as a crucial pathway towards general embodied intelligence, yet their training efficiency has become a key bottleneck. Although existing reinforcement learning (RL)-based training frameworks like RLinf can enhance model generalization, they still rely on synchronous execution, leading to severe resource underutilization and throughput limitations during environment interaction, policy generation (rollout), and model update phases ...

</details>

---

### [RoboPaint: From Human Demonstration to Any Robot and Any View](https://arxiv.org/abs/2602.05325v1)

**Authors:** Jiacheng Fan, Zhiyue Zhao, Yiqian Zhang, Chao Chen, Peide Wang et al. (7 authors)

**Published:** 2026-02-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.05325v1) | [PDF](https://arxiv.org/pdf/2602.05325v1.pdf)

<details>
<summary>Abstract</summary>

Acquiring large-scale, high-fidelity robot demonstration data remains a critical bottleneck for scaling Vision-Language-Action (VLA) models in dexterous manipulation. We propose a Real-Sim-Real data collection and data editing pipeline that transforms human demonstrations into robot-executable, environment-specific training data without direct robot teleoperation. Standardized data collection rooms are built to capture multimodal human demonstrations (synchronized 3 RGB-D videos, 11 RGB videos, ...

</details>

---

### [MobileManiBench: Simplifying Model Verification for Mobile Manipulation](https://arxiv.org/abs/2602.05233v1)

**Authors:** Wenbo Wang, Fangyun Wei, QiXiu Li, Xi Chen, Yaobo Liang et al. (8 authors)

**Published:** 2026-02-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.05233v1) | [PDF](https://arxiv.org/pdf/2602.05233v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models have advanced robotic manipulation but remain constrained by reliance on the large, teleoperation-collected datasets dominated by the static, tabletop scenes. We propose a simulation-first framework to verify VLA architectures before real-world deployment and introduce MobileManiBench, a large-scale benchmark for mobile-based robotic manipulation. Built on NVIDIA Isaac Sim and powered by reinforcement learning, our pipeline autonomously generates diverse manipulatio...

</details>

---

### [Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data](https://arxiv.org/abs/2602.04600v1)

**Authors:** Jialiang Li, Yi Qiao, Yunhan Guo, Changwen Chen, Wenzhao Lian

**Published:** 2026-02-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.04600v1) | [PDF](https://arxiv.org/pdf/2602.04600v1.pdf)

<details>
<summary>Abstract</summary>

Achieving generalizable manipulation in unconstrained environments requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However, existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex environments. In this work, we formalize active perception as a non-Markovian process driven by information gain and decision branching, providing a structured categorization of visual active perc...

</details>

---

### [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://arxiv.org/abs/2602.04208v1)

**Authors:** Hyeonbeom Choi, Daechul Ahn, Youhan Lee, Taewook Kang, Seongwon Cho et al. (6 authors)

**Published:** 2026-02-04 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.04208v1) | [PDF](https://arxiv.org/pdf/2602.04208v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic control, with test-time scaling (TTS) gaining attention to enhance robustness beyond training. However, existing TTS methods for VLAs require additional training, verifiers, and multiple forward passes, making them impractical for deployment. Moreover, they intervene only at action decoding while keeping visual representations fixed-insufficient under perceptual ambiguity, where reconsidering how...

</details>

---
