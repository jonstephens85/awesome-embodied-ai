# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-04 18:16 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825v1)

**Authors:** Amirhosein Alian, Yongqiang Zhao, Shiyi Gu, Xuyang Zhang, Zhuo Chen et al. (8 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04825v1) | [PDF](https://arxiv.org/pdf/2606.04825v1.pdf) | [Project Page](haptile-dataset.github.io)

<details>
<summary>Abstract</summary>

Despite the importance of tactile sensing for reliable manipulation, most existing Vision-Language-Action (VLA) datasets remain vision-only, and those that do incorporate tactile information typically lack the joint combination of task diversity, language conditioning, and action trajectories. Furthermore, existing teleoperation pipelines rarely provide haptic feedback to the operator, despite its established role in demonstration quality and manipulation stability. In this work, we present HapT...

</details>

---

### [Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation](https://arxiv.org/abs/2606.04046v1)

**Authors:** Boyuan Xiao, Bohong Chen, Yumeng Li, Ji Feng, Yao-Xiang Ding et al. (6 authors)

**Published:** 2026-06-02 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.04046v1) | [PDF](https://arxiv.org/pdf/2606.04046v1.pdf) | [Project Page](https://future-item.github.io/SceneDiver)

<details>
<summary>Abstract</summary>

In embodied vision-language decision making tasks such as robotic manipulation and navigation, Vision-Language and Vision-Language-Action Models (VLMs & VLAs) are powerful tools with different benefits: VLMs are better at long-term planning, while VLAs are better at reactive control. However, their performance is limited by the same perceptual bottleneck: visual hallucinations arise due to the models' inability to distinguish task-relevant objects from distractors. In principle, accurate identif...

</details>

---

## Other Recent Papers

### [Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement](https://arxiv.org/abs/2606.04968v1)

**Authors:** Yunpeng Mei, Jiakai He, Hongjie Cao, Chenyu Wang, Xiaowen Zhu et al. (15 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04968v1) | [PDF](https://arxiv.org/pdf/2606.04968v1.pdf)

<details>
<summary>Abstract</summary>

Large vision-language-action (VLA) policies are increasingly trained as conditional generative models over action chunks. Yet deployment produces mixed-quality experience-successful demonstrations, partial completions, recoverable mistakes, and failures-that is difficult to use with standard imitation. Full behavior cloning (BC) imitates failures, filtered BC discards useful sub-trajectories, and offline reinforcement learning adds a large critic. We introduce ForesightFlow, a self-guided flow-m...

</details>

---

### [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708v1)

**Authors:** Siyuan Yang, Linzheng Guo, Ouyang Lu,  Zhaxizhuoma, Daoran Zhang et al. (13 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.04708v1) | [PDF](https://arxiv.org/pdf/2606.04708v1.pdf)

<details>
<summary>Abstract</summary>

Universal Manipulation Interface (UMI) enables scalable real-world robot data collection without hardware-specific teleoperation, yet leveraging UMI data to train large-scale Vision-Language-Action (VLA) models remains fundamentally challenging. We identify two critical mismatches: wrist-mounted fisheye views, with severe radial distortion and local gripper-centric perspectives, are out-of-distribution for pretrained VLMs; and human-collected trajectories frequently violate kinematic limits, inc...

</details>

---

### [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436v1)

**Authors:** Jiaxin Shi, Xidong Zhang, Fucai Zhu, Zhe Li, Siyu Zhu et al. (6 authors)

**Published:** 2026-06-03 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04436v1) | [PDF](https://arxiv.org/pdf/2606.04436v1.pdf)

<details>
<summary>Abstract</summary>

We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction. Our core insight is that 3D geometry perception and 3D spatial reasoning are distinct capabilities that can be disentangled and injected at different feature hierarchies. During training, three tightly coupled components work in concert primarily within the latent space: (1) To gain geometric priors, a latent 3D geometry perce...

</details>

---

### [Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation](https://arxiv.org/abs/2606.03784v2)

**Authors:** Nan Sun, Yuan Zhang, Yongkun Yang, Wentao Zhao, Peiyan Li et al. (13 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03784v2) | [PDF](https://arxiv.org/pdf/2606.03784v2.pdf)

<details>
<summary>Abstract</summary>

Embodied chain-of-thought (CoT) aims to bridge linguistic reasoning and robotic control, but its effective form and integration strategy remain underexplored. In this paper, we revisit embodied CoT for vision-language-action (VLA) models at large scale. We construct the largest embodied CoT corpus to date, comprising 978,743 trajectories, 226.3M samples, and 2592.5 hours of robot data. Through extensive experiments, we find that effective embodied CoT should ground high-level semantic understand...

</details>

---

### [PHASER: Phase-Aware and Semantic Experience Replay for Vision-Language-Action Models](https://arxiv.org/abs/2606.03598v2)

**Authors:** Ziyang Chen, Shaoguang Wang, Weiyu Guo, Qianyi Cai, He Zhang et al. (8 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.03598v2) | [PDF](https://arxiv.org/pdf/2606.03598v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved remarkable success in language-conditioned robotic manipulation. However, deploying these models in open-ended environments requires continuously acquiring novel skills, a process that inevitably triggers severe catastrophic forgetting of previously learned behaviors. While experience replay (ER) serves as a standard mitigating strategy, naive uniform sampling fundamentally misaligns with the temporal characteristics of manipulation trajectories....

</details>

---

### [Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2606.03556v1)

**Authors:** Xiaofei Wang, Mingliang Han, Tianyu Hao, Yi Yang, Yun-Bo Zhao et al. (6 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03556v1) | [PDF](https://arxiv.org/pdf/2606.03556v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are gaining attention in robotics, yet their robustness to adversarial attacks remains largely unexplored. Existing work shows that adversarial patches can mislead VLA-based robots but assumes full access to the entire execution trajectory, an unrealistic requirement in practice. We address this limitation by formulating a partially observable threat model, where the adversary can exploit only a short prefix of the trajectory to generate a fixed patch applied ...

</details>

---

### [OpenEAI-Platform: An Open-source Embodied Artificial Intelligence Hardware-Software Unified Platform](https://arxiv.org/abs/2606.03392v1)

**Authors:** Jinyuan Zhang, Luoyi Fan, Leiyu Wang, Yeqiang Wang, Yicheng Zhu et al. (7 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03392v1) | [PDF](https://arxiv.org/pdf/2606.03392v1.pdf)

<details>
<summary>Abstract</summary>

Embodied AI in the real world requires both accurate hardware and robust vision-language-action (VLA) policies. We present OpenEAI-Platform, a fully open-source platform that integrates a low-cost 6+1 degree-of-freedom (dof) robotic arm (OpenEAI-Arm) and a reproducible VLA model (OpenEAI-VLA). OpenEAI-Arm provides open-source mechanical designs for low manufacturing cost and compliant control methods for higher accuracy. OpenEAI-VLA builds on Qwen3-VL-4B and uses a Diffusion Transformer action h...

</details>

---

### [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240v1)

**Authors:** Yizhi Chen, Zhanxiang Cao, Xinyi Peng, Yixiao Zheng, Xiaxi Si et al. (17 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03240v1) | [PDF](https://arxiv.org/pdf/2606.03240v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision--Language--Action (VLA) models often optimize for semantic grounding, whereas executable manipulation requires geometry-aware spatial alignment and dynamic affordance selection. We introduce GeoAlign, a state-guided spatial alignment architecture for VLA policy learning. GeoAlign post-trains an RGB geometry branch with robot-domain RGB-D supervision, yielding RGB-derived Geometry-Enhanced Post-Trained (GEP) features for policy rollout. The robot's proprioceptive state queries the ...

</details>

---

### [TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127v1)

**Authors:** Wenbo Zhang, Jianxiong Li, Shuai Yang, Sijin Chen, Jiajun Liu et al. (7 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03127v1) | [PDF](https://arxiv.org/pdf/2606.03127v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models trained on large-scale data have made remarkable progress, but they remain vulnerable to distribution shifts at deployment time. Recent VLA models suggest that prompts can serve as an efficient interface for steering policy behavior, but existing prompt-based steering typically relies on external guidance. This raises a natural question: can test-time training (TTT) for VLA be achieved by optimizing a prompt, so that the steering interface itself can be learne...

</details>

---
