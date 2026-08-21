# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-21 16:33 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation](https://arxiv.org/abs/2608.19490v1)

**Authors:** Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.19490v1) | [PDF](https://arxiv.org/pdf/2608.19490v1.pdf) | [Project Page](https://self-supervised-control.pages.dev/)

<details>
<summary>Abstract</summary>

State-of-the-art vision-language-action (VLA) models such as $π_{0.5}$ exhibit strong semantic understanding, instruction following and task behavior. However, when deployed on new robots, even minor mismatches in hardware configuration relative to pretraining can cause severe performance drops. Finetuning the VLA on in-domain expert data from the new embodiment improves performance on the expert task but leads to a loss in its original instruction following and behavioral priors. In this paper,...

</details>

---

## Other Recent Papers

### [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891v1)

**Authors:** Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch et al. (8 authors)

**Published:** 2026-08-20 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19891v1) | [PDF](https://arxiv.org/pdf/2608.19891v1.pdf)

<details>
<summary>Abstract</summary>

How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours ...

</details>

---

### [OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation](https://arxiv.org/abs/2608.19589v1)

**Authors:** Jiaqi Wang, Zhou Fang, Qiongfeng Shi, Yi Zhou

**Published:** 2026-08-20 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.19589v1) | [PDF](https://arxiv.org/pdf/2608.19589v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained Vision-Language-Action models provide a strong foundation for robot learning, but sequentially adapting them to diverse skills can perturb the representations and velocity mappings used by previous skills, leading to catastrophic forgetting. Architecture-based approaches improve retention by isolating skills but lead to increased inference footprint. Recent subspace-constrained methods restrict parameter updates in an orthogonal subspace to minimize interference but impose a unified c...

</details>

---

### [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111v1)

**Authors:** Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li et al. (10 authors)

**Published:** 2026-08-20 | **Categories:** cs.RO, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2608.20111v1) | [PDF](https://arxiv.org/pdf/2608.20111v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols. This survey reviews this transition across behavior cloning, conditional imitation learning, privileged distillation, BEV and vectorized planning, unified perception-prediction-planning architectures, world-model-based planners, and vision-language-action systems. We argue that ...

</details>

---

### [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](https://arxiv.org/abs/2608.19161v1)

**Authors:** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, Jugad Singh, Sumit Kumar Jha et al. (6 authors)

**Published:** 2026-08-19 | **Categories:** cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2608.19161v1) | [PDF](https://arxiv.org/pdf/2608.19161v1.pdf)

<details>
<summary>Abstract</summary>

Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysi...

</details>

---

### [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066v1)

**Authors:** Yechan Park, HyunJin Kim

**Published:** 2026-08-19 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19066v1) | [PDF](https://arxiv.org/pdf/2608.19066v1.pdf)

<details>
<summary>Abstract</summary>

This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displaceme...

</details>

---

### [The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433v1)

**Authors:** Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda et al. (10 authors)

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18433v1) | [PDF](https://arxiv.org/pdf/2608.18433v1.pdf)

<details>
<summary>Abstract</summary>

Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs across methods and target robots, and those differences affect practical deployment. We call the gap between reusable models, representations, or ...

</details>

---

### [Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies](https://arxiv.org/abs/2608.18410v1)

**Authors:** Wei Jiang, Wei Wang

**Published:** 2026-08-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18410v1) | [PDF](https://arxiv.org/pdf/2608.18410v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. Sub-token compression provides a complementary alternative by retaining more tokens while reducing their value width. However, directly applying sub-token compression to VLA policies is less effective ...

</details>

---
