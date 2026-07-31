# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-31 17:28 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models](https://arxiv.org/abs/2607.27599v1)

**Authors:** Xiangcheng Zhang, Yilun Du

**Published:** 2026-07-30 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27599v1) | [PDF](https://arxiv.org/pdf/2607.27599v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Building generalizable agents for diverse applications remains a fundamental challenge. While imitation learning-based policies succeed in specific training environments, they often fail to generalize to novel scenes and tasks. In this work, we propose World Action Planner, a robot planning system that leverages the reasoning capabilities of Vision-Language Models (VLMs) and the physical grounding of a multi-task pose-image conditioned world model. Our system enables an agent to propose initial ...

</details>

---

### [Cross-Embodiment Transfer via Behavior-Aligned Representations](https://arxiv.org/abs/2607.27549v1)

**Authors:** Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale et al. (6 authors)

**Published:** 2026-07-30 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.27549v1) | [PDF](https://arxiv.org/pdf/2607.27549v1.pdf) | [Project Page](https://ajaysridhar.com/barx/)

<details>
<summary>Abstract</summary>

Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions, end-effector traces of robot motion) in vision-language-action (VLA) models to promote cross-embodiment transfer. We hypothesize that by po...

</details>

---

### [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](https://arxiv.org/abs/2607.28625v1)

**Authors:** Yukang Cao, Haozhe Xie, Beichen Wen, Runmao Yao, Yinghao Liu et al. (16 authors)

**Published:** 2026-07-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.28625v1) | [PDF](https://arxiv.org/pdf/2607.28625v1.pdf) | [Project Page](https://ace-data-engine.github.io/ACE-Data-0/)

<details>
<summary>Abstract</summary>

Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environme...

</details>

---

### [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205v1)

**Authors:** Hengyi Xie, Chenfei Yao, Xianjin Wu, Xuanyang Xi, Yiping Tang et al. (10 authors)

**Published:** 2026-07-29 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27205v1) | [PDF](https://arxiv.org/pdf/2607.27205v1.pdf) | [GitHub](https://github.com/H-EmbodVis/TurboVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional $V \to L \to A$ pathway as a direct $V + L \to A$ mapping. Instead of ...

</details>

---

## Other Recent Papers

### [RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents](https://arxiv.org/abs/2607.27881v1)

**Authors:** Sihyung Yoon, Minjong Yoo, Sanghyun Ahn, Seojeong Choi, Honguk Woo

**Published:** 2026-07-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.27881v1) | [PDF](https://arxiv.org/pdf/2607.27881v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have attracted growing interest as a scalable approach to robotic manipulation. While these models are effective action predictors, deploying them as robotic agents exposes critical gaps: no mechanism for failure recovery, inconsistent execution over long horizons, and limited robustness to shifts in observations, tasks, or embodiments. Existing solutions address these limitations individually through model retraining or environment-specific modules, yet what ...

</details>

---

### [RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy](https://arxiv.org/abs/2607.27782v1)

**Authors:** Zhengyang Yan, Junhao Li, Fangqi Zhu, Zijun Wang, Quanxin Shou et al. (9 authors)

**Published:** 2026-07-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.27782v1) | [PDF](https://arxiv.org/pdf/2607.27782v1.pdf)

<details>
<summary>Abstract</summary>

Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment. While offline reinforcement learning (RL) provides a practical way to improve deployed policies using rollout data, existing methods either ignore failure data or exploit it only at the trajectory level, resulting in low learning efficiency and persistent errors. We propose **RedFlow**, a fine-grained of...

</details>

---

### [DLAM: Distributional Latent Actions with Temporal Constraints](https://arxiv.org/abs/2607.27138v1)

**Authors:** Zuojin Tang, Feifan Luo, Haoyun Liu, Botai Yuan, Dekang Qi et al. (13 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.27138v1) | [PDF](https://arxiv.org/pdf/2607.27138v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained codes may predict future observations without the structure required for joint generation with robot actions. Existing structured methods add temporal constraints but retain deterministic transition points, so residual errors in locally inferred transitions ma...

</details>

---

### [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991v2)

**Authors:** Derek Ming Siang Tan, Shailesh Shailesh, Srikrishna Iyer, William Wei Jie Teo, Yuanliang Ju et al. (7 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26991v2) | [PDF](https://arxiv.org/pdf/2607.26991v2.pdf)

<details>
<summary>Abstract</summary>

Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore inherit correlated failure modes. Moreover, existing methods apply the same intervention strategy at every timestep, regardless of w...

</details>

---

### [Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA](https://arxiv.org/abs/2607.26807v1)

**Authors:** Tianhang Yang, Yanze Zheng, Junjie Wang, Wei-Bin Kou, Ruotong Li et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26807v1) | [PDF](https://arxiv.org/pdf/2607.26807v1.pdf)

<details>
<summary>Abstract</summary>

While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions across manipulation tasks and, even worse, the unavailability of the kinematic signals at inference time. In this work, we first observe that most semantically distinct manipulation tasks reduce to multiple kinematic archetypes. Motivated by this finding, we propose Kinematics-supervised explicit routing (KinRT), a new paradigm that shifts from implicit...

</details>

---

### [CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2607.26789v1)

**Authors:** Yushan Liu, Peibo Sun, Xintao Chao, Zhenyang Yang, Yifan Xie et al. (11 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26789v1) | [PDF](https://arxiv.org/pdf/2607.26789v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores l...

</details>

---

### [Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models](https://arxiv.org/abs/2607.26513v1)

**Authors:** Mingyang Sun, Jiude Wei, Xiujian Liang, Qichen He, Donglin Wang et al. (7 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26513v1) | [PDF](https://arxiv.org/pdf/2607.26513v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. To bridge this crucial gap, we construct a Concept Expert module for VLA to build executable Analytic Concepts that represent objects as explicit, programmatic blueprints. Our mechanism operates in two synergis...

</details>

---

### [CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/abs/2607.26452v1)

**Authors:** Yiming Cai, Fangjie Yu, Meiqing Yu, Ziyue Shi, Pengfei Yuan et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.AI, cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2607.26452v1) | [PDF](https://arxiv.org/pdf/2607.26452v1.pdf)

<details>
<summary>Abstract</summary>

World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure. We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines. CG-World explicitly records intermediate states, including multimodal semantics, spatial structure, skeletal and controller states, motion curves, camera and lighting parameters,...

</details>

---
