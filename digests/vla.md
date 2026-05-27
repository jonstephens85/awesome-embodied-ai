# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-27 18:26 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies](https://arxiv.org/abs/2605.27284v1)

**Authors:** Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun et al. (14 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.27284v1) | [PDF](https://arxiv.org/pdf/2605.27284v1.pdf) | [Project Page](https://finevla.xlang.ai/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly expected to not only complete robot tasks, but also follow human instructions about how those tasks should be executed. However, existing robot datasets usually pair trajectories with coarse goal-level language, leaving execution-critical details such as active arm, approach direction, and contact region unspecified. This limits steerable policy learning and robotic video understanding. We introduce FineVLA, an open framework for action-aligne...

</details>

---

### [OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation](https://arxiv.org/abs/2605.25829v1)

**Authors:** Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li et al. (8 authors)

**Published:** 2026-05-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.25829v1) | [PDF](https://arxiv.org/pdf/2605.25829v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models and world action models (WAMs) advance robotic manipulation by enriching intermediate representations with auxiliary spatial features or future visual-state prediction. However, these representations largely remain within the observation space and do not share the rigid-body geometry of the action space, forcing the action decoder to implicitly recover this geometry. We propose OASIS, a visuomotor policy that aligns the intermediate representation with ...

</details>

---

## Other Recent Papers

### [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820v1)

**Authors:** Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Mingqi Yuan et al. (8 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.26820v1) | [PDF](https://arxiv.org/pdf/2605.26820v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a promising foundation for general-purpose robotics. However, their successful deployment in real-world scenarios requires the ability to continually acquire new skills while retaining previously learned behaviors. While pioneering research has studied the continual learning of VLA models in narrowly simulated environments, this challenge remains largely unexplored under realistic conditions. To address this limitation, we construct a real-world contin...

</details>

---

### [Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](https://arxiv.org/abs/2605.25889v2)

**Authors:** Jianwei Tai

**Published:** 2026-05-25 | **Categories:** cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.25889v2) | [PDF](https://arxiv.org/pdf/2605.25889v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly deployed on real robots, where each predicted action is executed and each failure carries a safety cost. They reach high success rates on clean inputs but collapse under small adversarial perturbations. A $16/255$ PGD attack on OpenVLA-7B drops LIBERO success from above $95\%$ to under $5\%$. Empirical defenses recover some robustness at a cost in clean accuracy, but the literature does not say whether the trade-off has a theoretical floor. We...

</details>

---

### [Rethinking VLM Representation for VLA Initialization](https://arxiv.org/abs/2605.25802v1)

**Authors:** Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An et al. (8 authors)

**Published:** 2026-05-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.25802v1) | [PDF](https://arxiv.org/pdf/2605.25802v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models widely adopt pretrained Vision-Language Models (VLMs) as policy backbones, yet it remains unclear what kind of pretrained VLM representation is useful as a VLA initialization. In this paper, we study VLA initialization as a controlled representation-design problem along three axes: capability-level embodied VQA supervision, parameter-update strategy, and robot-data pretraining. Our experiments show that the original pretrained VLM representation is a key sourc...

</details>

---

### [EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](https://arxiv.org/abs/2605.25477v1)

**Authors:** Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn

**Published:** 2026-05-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.25477v1) | [PDF](https://arxiv.org/pdf/2605.25477v1.pdf)

<details>
<summary>Abstract</summary>

The ability to efficiently and reliably learn new tasks has been a foundational challenge in robotics. Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse manipulation tasks, yet pretrained policies consistently fall short of the reliability required for real-world deployment. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches either train from scratch without fully leveraging pretrained priors, or fi...

</details>

---
