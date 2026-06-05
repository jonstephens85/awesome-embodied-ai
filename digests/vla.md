# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-05 22:58 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155v1)

**Authors:** Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping et al. (13 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.CV, cs.MM

**Links:** [arXiv](https://arxiv.org/abs/2606.06155v1) | [PDF](https://arxiv.org/pdf/2606.06155v1.pdf) | [Project Page](are) | [GitHub](https://github.com/Skywalker-yqz/AffordanceVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models leverage the rich world knowledge of pretrained vision-language models (VLMs) to enable instruction-following robotic manipulation. However, the structural mismatch between VLM semantic spaces and embodied control policies often hinders the learning of precise perception--action mappings. To address this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces structured affordance forecasting as a task-oriented intermediate representa...

</details>

---

### [HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825v1)

**Authors:** Amirhosein Alian, Yongqiang Zhao, Shiyi Gu, Xuyang Zhang, Zhuo Chen et al. (8 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04825v1) | [PDF](https://arxiv.org/pdf/2606.04825v1.pdf) | [Project Page](haptile-dataset.github.io)

<details>
<summary>Abstract</summary>

Despite the importance of tactile sensing for reliable manipulation, most existing Vision-Language-Action (VLA) datasets remain vision-only, and those that do incorporate tactile information typically lack the joint combination of task diversity, language conditioning, and action trajectories. Furthermore, existing teleoperation pipelines rarely provide haptic feedback to the operator, despite its established role in demonstration quality and manipulation stability. In this work, we present HapT...

</details>

---

## Other Recent Papers

### [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491v1)

**Authors:** Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao et al. (7 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.06491v1) | [PDF](https://arxiv.org/pdf/2606.06491v1.pdf)

<details>
<summary>Abstract</summary>

Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion. Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache reuse, or reinforcement learning only shift the policy from one fixed speed to another, and leave deceleration almost unexplored. We observe that the magnitude of ...

</details>

---

### [MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action](https://arxiv.org/abs/2606.06245v1)

**Authors:** Boyang Zhang, Lianlei Shan

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.06245v1) | [PDF](https://arxiv.org/pdf/2606.06245v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies remain brittle in long-horizon and high-uncertainty control, where one-pass action decoding provides limited inference-time deliberation. Explicit chain-of-thought can increase reasoning depth, but introduces token latency and an indirect text-to-action interface. We propose MPCoT, a reward-guided multi-path latent reasoning framework that initializes $M$ hypotheses, refines them for K weight-tied steps, and softly aggregates them before action decoding. A t...

</details>

---

### [WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation](https://arxiv.org/abs/2606.06147v1)

**Authors:** Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao et al. (8 authors)

**Published:** 2026-06-04 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.06147v1) | [PDF](https://arxiv.org/pdf/2606.06147v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation. However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions. We argue that the ability to "imagine" future states -- inherent in World Models -- is critical for robust decision-making under such partial observability. To address this, we construct a ...

</details>

---

### [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979v1)

**Authors:** Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu et al. (12 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.05979v1) | [PDF](https://arxiv.org/pdf/2606.05979v1.pdf)

<details>
<summary>Abstract</summary>

We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions, conjoining the \emph{world modeling interface} to learn from extensive egocentric videos as in the world-action model (WAM) and the \emph{language reasoning} capacities to solve complex long-horizon tasks as in vision-language-action (VLA) models. At the core of WLA li...

</details>

---

### [PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773v1)

**Authors:** Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang et al. (7 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05773v1) | [PDF](https://arxiv.org/pdf/2606.05773v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies operate in a closed loop in real-world robot tasks: a robot observes the scene, executes an action chunk, and conditions its next decision on the resulting observation. However, most existing world models for robot action evaluation are limited to open-loop prediction along pre-collected action trajectories. This prevents them from supporting closed-loop VLA evaluation, where each action chunk must be conditioned on the observation generated by the previous ...

</details>

---

### [DRIFT: A Residual Flow Adapter for Decoding Continuous Outputs in Vision-Language Models](https://arxiv.org/abs/2606.05758v1)

**Authors:** Zhuoming Liu, Jinhong Lin, Kwan Man Cheng, Lin Zhang, Shayok Bagchi et al. (6 authors)

**Published:** 2026-06-04 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.05758v1) | [PDF](https://arxiv.org/pdf/2606.05758v1.pdf)

<details>
<summary>Abstract</summary>

Many modern vision-language models (VLMs) build on autoregressive decoding of discrete tokens. While text-based output interfaces enable scalable pretraining and strong zero-shot generalization across diverse tasks, they are poorly suited for problems that require precise continuous outputs, such as localizing temporal boundaries of events or generating robotic control actions. To address this challenge, we propose DRIFT, a general framework for adapting pretrained VLMs to continuous decoding ta...

</details>

---

### [Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models](https://arxiv.org/abs/2606.05737v1)

**Authors:** Yitong Chen, Shiduo Zhang, Jingjing Gong, Xipeng Qiu

**Published:** 2026-06-04 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.05737v1) | [PDF](https://arxiv.org/pdf/2606.05737v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) models often inherit the image-generation view: actions are generated by iterative denoising. We argue that VLA action generation has a different condition-target structure: the policy is conditioned on rich observations, language, and state, but predicts only a compact, low-dimensional action chunk. Under this asymmetry, strong one-step action generation should not necessarily require the advanced one-step methods developed for image synthesis. We ke...

</details>

---

### [FlowPRO: Reward-Free Reinforced Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization](https://arxiv.org/abs/2606.05468v1)

**Authors:** Yihao Wu, He Zhang, Junbo Tan, Xueqian Wang, Zhengyou Zhang

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05468v1) | [PDF](https://arxiv.org/pdf/2606.05468v1.pdf)

<details>
<summary>Abstract</summary>

Post-training Vision-Language-Action (VLA) models into policies that can be reliably deployed on real robots remains a major bottleneck. SFT and DAgger exploit failure signals only indirectly, and reward-based RL is bottlenecked by the difficulty of real-world reward design and of training reliable critics. We present FlowPRO, a reward-free offline reinforced fine-tuning framework for flow-matching VLAs. Algorithmically, we propose RPRO (Robotic Flow-matching Proximalized Preference Optimization...

</details>

---

### [Output Type Before Quality: A Standards-Derived XAI Admissibility Rubric for Autonomous-Driving Safety](https://arxiv.org/abs/2606.05461v1)

**Authors:** Abhinaw Priyadershi, Mandar Pitale, Jelena Frtunikj, Maria Spence

**Published:** 2026-06-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.05461v1) | [PDF](https://arxiv.org/pdf/2606.05461v1.pdf)

<details>
<summary>Abstract</summary>

Safety standards for ML-based autonomous driving specify the kind of evidence an assurance case must contain (directed cause-and-effect chains, quantified interventional effects, named root-cause variables), yet the XAI literature is organised by output type and technique family (saliency maps, feature attribution, counterfactuals, causal graphs, language traces). SHAP, the most-recommended ADS XAI method, returns a ranked feature list that no implementation effort can convert into a directed ch...

</details>

---

### [Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement](https://arxiv.org/abs/2606.04968v1)

**Authors:** Yunpeng Mei, Jiakai He, Hongjie Cao, Chenyu Wang, Xiaowen Zhu et al. (15 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04968v1) | [PDF](https://arxiv.org/pdf/2606.04968v1.pdf)

<details>
<summary>Abstract</summary>

Large vision-language-action (VLA) policies are increasingly trained as conditional generative models over action chunks. Yet deployment produces mixed-quality experience-successful demonstrations, partial completions, recoverable mistakes, and failures-that is difficult to use with standard imitation. Full behavior cloning (BC) imitates failures, filtered BC discards useful sub-trajectories, and offline reinforcement learning adds a large critic. We introduce ForesightFlow, a self-guided flow-m...

</details>

---

### [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708v2)

**Authors:** Siyuan Yang, Linzheng Guo, Ouyang Lu,  Zhaxizhuoma, Daoran Zhang et al. (13 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.04708v2) | [PDF](https://arxiv.org/pdf/2606.04708v2.pdf)

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
