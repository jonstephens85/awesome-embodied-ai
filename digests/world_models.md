# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-09 23:10 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828v1)

**Authors:** Weijie Wang, Haoyu Zhao, Yifan Yang, Feng Chen, Zeyu Zhang et al. (10 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09828v1) | [PDF](https://arxiv.org/pdf/2606.09828v1.pdf) | [Project Page](https://aka.ms/latent-spatial-memory) | [GitHub](https://github.com/microsoft/LatentSpatialMemory)

<details>
<summary>Abstract</summary>

Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space. This design is both computationally expensive, requiring repeated rendering and VAE encoding, and inherently lossy, as the round trip through pixel space discards rich features of the learned latent representation. In this paper, we introduce \emph{latent spatial memory} for video world models, a persistent 3D cache that stores scene information ...

</details>

---

### [MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](https://arxiv.org/abs/2606.09827v1)

**Authors:** Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou et al. (9 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09827v1) | [PDF](https://arxiv.org/pdf/2606.09827v1.pdf) | [Project Page](https://shihao1895.github.io/MemoryVLA-PP-Web)

<details>
<summary>Abstract</summary>

Temporal modeling is essential for robotic manipulation, as effective control requires both memory of past interactions and imagination of future states. However, most VLA models rely primarily on the current observation and therefore struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived context, the hippocampal system to preserve episodic memory of past experience, and internal models to imagine possible futur...

</details>

---

### [iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](https://arxiv.org/abs/2606.09813v1)

**Authors:** Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng et al. (11 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09813v1) | [PDF](https://arxiv.org/pdf/2606.09813v1.pdf) | [Project Page](https://imac-wm.github.io/)

<details>
<summary>Abstract</summary>

Embodied world models have emerged as a pivotal paradigm for visual robotic decision-making and interactive environment simulation. However, conventional embodied frameworks rely on low-dimensional structured action vectors (e.g., joint angles and end-effector poses), which suffer from limited expressive capacity, poor generalization across diverse embodiments, and unnatural dynamic modeling for complex physical interactions. To address these limitations, this paper proposesiMac (Image as Action...

</details>

---

### [Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/abs/2606.09803v1)

**Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li et al. (16 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV, cs.GR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.09803v1) | [PDF](https://arxiv.org/pdf/2606.09803v1.pdf) | [GitHub](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Memory}{this)

<details>
<summary>Abstract</summary>

We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-action sequence, but their central failure is often memory rather than local image synthesis: after the camera leaves and returns, the scene or salient object may silently change. Existing memory designs are hard to compare because gains are entangled with backbone, training, retrieval, and evaluation d...

</details>

---

### [Prisma-World: Camera-Controllable Multi-Agent Video World Model](https://arxiv.org/abs/2606.09507v1)

**Authors:** Huiqiang Sun, Zhan Peng, Size Wu, Kun Wang, Kang Liao et al. (12 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09507v1) | [PDF](https://arxiv.org/pdf/2606.09507v1.pdf) | [Project Page](https://huiqiang-sun.github.io/prisma-world/)

<details>
<summary>Abstract</summary>

Video world models have made rapid progress in generating controllable visual experiences, but most of them still simulate the world from a single observer. Extending such models to multiple agents raises a central challenge: if each agent's future state is generated independently, overlapping views may instantiate different versions of the same scene, leading to inconsistent objects, layouts, and appearances across agents. Conventional camera conditioning controls individual trajectories, but i...

</details>

---

### [Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2606.08737v1)

**Authors:** Yunfan Lou, Yifan Ye, Yankai Fu, Jun Cen, Xiaowei Chi et al. (10 authors)

**Published:** 2026-06-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.08737v1) | [PDF](https://arxiv.org/pdf/2606.08737v1.pdf) | [GitHub](https://github.com/LYFCLOUDFAN/Dream-Tac)

<details>
<summary>Abstract</summary>

World action models inherit the predictive capability of world models, enabling action generation to be guided by anticipated future observations. However, they rely primarily on vision and often fail in contact-rich manipulation, where critical cues arise from physical interaction. In this paper, we propose Dream-Tac, a unified Tactile-World Action Model that jointly models actions, future visual observations, and tactile dynamics. Specifically, Dream-Tac introduces (i) contact-gated visuotacti...

</details>

---

## Other Recent Papers

### [Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics](https://arxiv.org/abs/2606.09640v1)

**Authors:** Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09640v1) | [PDF](https://arxiv.org/pdf/2606.09640v1.pdf)

<details>
<summary>Abstract</summary>

Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, p...

</details>

---

### [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499v1)

**Authors:** Ethan Rathbun, Ahmed Agha, Saaduddin Mahmud, Christopher Amato, Alina Oprea et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2606.09499v1) | [PDF](https://arxiv.org/pdf/2606.09499v1.pdf)

<details>
<summary>Abstract</summary>

World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing their integration into the robot learning pipeline. While highly practical, in this work we demonstrate that world models introduce a uniquely stealthy and effective data poisoning entry point into the robot learning supply chain that can result in the deployment of unsafe or otherwi...

</details>

---

### [$ω$-EVA: Envision, Verify, and Act with Latent Interactive World Models](https://arxiv.org/abs/2606.09457v1)

**Authors:** Zhenguo Sun, Yu Sun, Hande Huang, Alois Knoll

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09457v1) | [PDF](https://arxiv.org/pdf/2606.09457v1.pdf)

<details>
<summary>Abstract</summary>

Embodied policies typically map current observations directly to actions, leaving candidate-action consequences implicit. World models provide predictive supervision, representations, or external simulation, but rarely let a policy inspect the imagined consequence of its own proposal before acting. We introduce $ω$-EVA, a latent interactive world model that realizes an Envision--Verify--Act loop for embodied action generation. Its three-stage framework learns action-conditioned latent dynamics, ...

</details>

---

### [Toward Compiler World Models: Learning Latent Dynamics for Efficient Tensor Program Search](https://arxiv.org/abs/2606.09312v1)

**Authors:** Haolin Pan, Lianghong Huang, Xvlin Zhou, Mingjie Xing, Yanjun Wu

**Published:** 2026-06-08 | **Categories:** cs.LG, cs.PL

**Links:** [arXiv](https://arxiv.org/abs/2606.09312v1) | [PDF](https://arxiv.org/pdf/2606.09312v1.pdf)

<details>
<summary>Abstract</summary>

Tensor program optimization is essential for modern machine learning systems, but its search space is enormous. Existing auto-schedulers reduce measurement cost with learned cost models, yet they usually evaluate each candidate as a static code snapshot, ignoring the schedule trajectory that produced it. This makes them insensitive to action dependencies and vulnerable to superficial code variations. We propose a \emph{world-model-inspired} evaluator that models schedule evaluation as action-con...

</details>

---

### [FF-JEPA: Long-Horizon Planning in World Models with Latent Planners](https://arxiv.org/abs/2606.09311v1)

**Authors:** Sergi Masip, Jonathan Swinnen, Yutong Hu, Renaud Detry, Tinne Tuytelaars

**Published:** 2026-06-08 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.09311v1) | [PDF](https://arxiv.org/pdf/2606.09311v1.pdf)

<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) have shown promising world modeling capabilities, enabling planning in latent space by optimizing action trajectories using methods like the Cross-Entropy Method (CEM). These methods are, however, too computationally expensive and ineffective for long-horizon planning. Furthermore, these methods typically require an explicit image of the goal state, which is not always possible in real-world tasks. In this work, we tackle these limitations by prop...

</details>

---

### [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215v1)

**Authors:** Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09215v1) | [PDF](https://arxiv.org/pdf/2606.09215v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple a video dynamics prior to the policy and have shown encouraging results on tabletop manipulation, but iterative denoising over high-dimensional video-action latents leaves them too slow for real-time humanoid loco-manipulation. The problem is compounded by the dominant hierarchical paradigm, in which a high-level manipulation policy controls only the upper body while a low-level controller tracks coarse base commands -- placing upper and lower body in inconsiste...

</details>

---

### [ATM: Action-Consistency Transfer Matrix for Diagnosing and Improving Latent World Models](https://arxiv.org/abs/2606.09028v1)

**Authors:** Jiaheng Chen

**Published:** 2026-06-08 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09028v1) | [PDF](https://arxiv.org/pdf/2606.09028v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models are increasingly used for control and goal-conditioned planning, yet assessing whether their learned representations are useful for planning usually requires slow, planner-coupled simulator evaluation with CEM or similar planners. Such evaluation is black-box and model-complexity-dependent: under the same protocol, different world models may require minutes to hours per checkpoint. In this work, we propose ATM, an Action-Consistency Transfer Matrix for diagnosing whether late...

</details>

---

### [Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks](https://arxiv.org/abs/2606.08775v1)

**Authors:** Raktim Gautam Goswami, Prashanth Krishnamurthy, Yann LeCun, Farshad Khorrami

**Published:** 2026-06-07 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.08775v1) | [PDF](https://arxiv.org/pdf/2606.08775v1.pdf)

<details>
<summary>Abstract</summary>

Visual world models have shown great potential in learning complex system dynamics. Recent advancements leverage these models as transition functions within Model Predictive Control (MPC) frameworks to solve various control tasks. When applied to robotics, however, they are limited to single-stage tasks such as reaching or grasping, and struggle with multi-stage ones that demand complex sequential planning. In this work, we introduce WorldDP, a world model framework designed for multi-stage robo...

</details>

---
