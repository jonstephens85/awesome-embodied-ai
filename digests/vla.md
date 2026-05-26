# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-26 18:25 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](https://arxiv.org/abs/2605.25889v1)

**Authors:** Jianwei Tai

**Published:** 2026-05-25 | **Categories:** cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.25889v1) | [PDF](https://arxiv.org/pdf/2605.25889v1.pdf)

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

### [X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models](https://arxiv.org/abs/2605.25044v1)

**Authors:** Boyu Li, Chaoyi Xu, Haoqi Yuan, Xinrun Xu, Börje F. Karlsson et al. (8 authors)

**Published:** 2026-05-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.25044v1) | [PDF](https://arxiv.org/pdf/2605.25044v1.pdf)

<details>
<summary>Abstract</summary>

Learning universal policies from cross-embodied data remains a fundamental challenge in robotics. Although Vision-Language-Action (VLA) models are pre-trained on large and diverse datasets, they typically rely on embodiment-specific fine-tuning to achieve strong performance in downstream tasks. This requirement severely limits their generalization capability and restricts knowledge transfer across embodiments performing similar tasks. To overcome these limitations, we focus on cross-embodied set...

</details>

---

### [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/abs/2605.24892v1)

**Authors:** Baolu Li, Jingyu Qian, Rui Guo, Yilun Chen, Hanpeng Liu et al. (17 authors)

**Published:** 2026-05-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.24892v1) | [PDF](https://arxiv.org/pdf/2605.24892v1.pdf)

<details>
<summary>Abstract</summary>

Physical world knowledge resides mainly in videos. Equipping Vision-Language-Action (VLA) models with such knowledge is fundamental for safe and generalizable planning. Predictive world modeling enables VLA to internalize physical dynamics and long-term causality by predicting future video from past observations. However, naive next-frame prediction faces two challenges: 1) unlike semantically distinct text tokens, video tokens are low-entropy and redundant, causing prediction to degenerate into...

</details>

---

### [QuoVLA: Quotient Space for Vision-Language-Action Models](https://arxiv.org/abs/2605.24890v1)

**Authors:** Xuan Wang, Yinan Wu, Haoran Duan, Jungong Han

**Published:** 2026-05-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.24890v1) | [PDF](https://arxiv.org/pdf/2605.24890v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models commonly adapt pretrained Vision-Language Models (VLMs) to robot control by mapping visual observations and language instructions to continuous actions. Existing approaches typically take an action-insufficiency view, assuming that pretrained VLM latents either lack directly usable action information or should be shielded from action-learning signals. Against this view, our \textit{Quotient Theory for VLA} shows that pretrained VLM latents are not action-insuf...

</details>

---
