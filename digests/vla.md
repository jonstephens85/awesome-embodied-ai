# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-13 22:20 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics](https://arxiv.org/abs/2603.12193v1)

**Authors:** Mengzhen Liu, Enshen Zhou, Cheng Chi, Yi Han, Shanyu Rong et al. (9 authors)

**Published:** 2026-03-12 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.12193v1) | [PDF](https://arxiv.org/pdf/2603.12193v1.pdf) | [Project Page](https://lmzpai.github.io/SaPaVe)

<details>
<summary>Abstract</summary>

Active perception and manipulation are crucial for robots to interact with complex scenes. Existing methods struggle to unify semantic-driven active perception with robust, viewpoint-invariant execution. We propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner. Our approach decouples camera and manipulation actions rather than placing them in a shared action space, and follows a bottom-up training strategy: we first train semantic camera contro...

</details>

---

### [DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control](https://arxiv.org/abs/2603.10448v1)

**Authors:** Teli Ma, Jia Zheng, Zifan Wang, Chuili Jiang, Andy Cui et al. (7 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10448v1) | [PDF](https://arxiv.org/pdf/2603.10448v1.pdf) | [Project Page](https://dit4dit.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively limited action data. Generative video models, by contrast, encode rich spatiotemporal structure and implicit physics, making them a compelling foundation for robotic manipulation. But their potentials are not fully explored in the literature. To bridge the g...

</details>

---

### [World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)

**Authors:** An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma et al. (9 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.10422v1) | [PDF](https://arxiv.org/pdf/2603.10422v1.pdf) | [Project Page](https://wm2act.github.io/)

<details>
<summary>Abstract</summary>

World Models (WMs) have emerged as a promising approach for post-training Vision-Language-Action (VLA) policies to improve robustness and generalization under environmental changes. However, most WM-based post-training methods rely on pixel-space supervision, making policies sensitive to pixel-level artifacts and hallucination from imperfect WM rollouts. We introduce World2Act, a post-training framework that aligns VLA actions directly with WM video-dynamics latents using a contrastive matching ...

</details>

---

## Other Recent Papers

### [Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning](https://arxiv.org/abs/2603.11653v1)

**Authors:** Jiaheng Hu, Jay Shim, Chen Tang, Yoonchang Sung, Bo Liu et al. (7 authors)

**Published:** 2026-03-12 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.11653v1) | [PDF](https://arxiv.org/pdf/2603.11653v1.pdf)

<details>
<summary>Abstract</summary>

Continual Reinforcement Learning (CRL) for Vision-Language-Action (VLA) models is a promising direction toward self-improving embodied agents that can adapt in openended, evolving environments. However, conventional wisdom from continual learning suggests that naive Sequential Fine-Tuning (Seq. FT) leads to catastrophic forgetting, necessitating complex CRL strategies. In this work, we take a step back and conduct a systematic study of CRL for large pretrained VLAs across three models and five c...

</details>

---

### [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558v1)

**Authors:** Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang et al. (18 authors)

**Published:** 2026-03-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.11558v1) | [PDF](https://arxiv.org/pdf/2603.11558v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) systems have shown strong potential for language-driven robotic manipulation. However, scaling them to long-horizon tasks remains challenging. Existing pipelines typically separate data collection, policy learning, and deployment, resulting in heavy reliance on manual environment resets and brittle multi-policy execution. We present RoboClaw, an agentic robotics framework that unifies data collection, policy learning, and task execution under a single VLM-driven cont...

</details>

---

### [DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](https://arxiv.org/abs/2603.11041v1)

**Authors:** Shuyao Shang, Bing Zhan, Yunfei Yan, Yuqi Wang, Yingyan Li et al. (12 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.11041v1) | [PDF](https://arxiv.org/pdf/2603.11041v1.pdf)

<details>
<summary>Abstract</summary>

We propose DynVLA, a driving VLA model that introduces a new CoT paradigm termed Dynamics CoT. DynVLA forecasts compact world dynamics before action generation, enabling more informed and physically grounded decision-making. To obtain compact dynamics representations, DynVLA introduces a Dynamics Tokenizer that compresses future evolution into a small set of dynamics tokens. Considering the rich environment dynamics in interaction-intensive driving scenarios, DynVLA decouples ego-centric and env...

</details>

---

### [FG-CLTP: Fine-Grained Contrastive Language Tactile Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.10871v1)

**Authors:** Wenxuan Ma, Chaofan Zhang, Yinghao Cai, Guocai Yao, Shaowei Cui et al. (6 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10871v1) | [PDF](https://arxiv.org/pdf/2603.10871v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in integrating tactile sensing into vision-language-action (VLA) models have demonstrated transformative potential for robotic perception. However, existing tactile representations predominantly rely on qualitative descriptors (e.g., texture), neglecting quantitative contact states such as force magnitude, contact geometry, and principal axis orientation, which are indispensable for fine-grained manipulation. To bridge this gap, we propose FG-CLTP, a fine-grained contrastive ...

</details>

---

### [FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model](https://arxiv.org/abs/2603.10712v1)

**Authors:** Xiaoxu Xu, Hao Li, Jinhui Ye, Yilun Chen, Jia Zeng et al. (10 authors)

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10712v1) | [PDF](https://arxiv.org/pdf/2603.10712v1.pdf)

<details>
<summary>Abstract</summary>

Predictive foresight is important to intelligent embodied agents. Since the motor execution of a robot is intrinsically constrained by its visual perception of environmental geometry, effectively anticipating the future requires capturing this tightly coupled visuomotor interplay. While recent vision-language-action models attempt to incorporate future guidance, they struggle with this joint modeling. Existing explicit methods divert capacity to task-irrelevant visual details, whereas implicit m...

</details>

---

### [RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation](https://arxiv.org/abs/2603.11106v1)

**Authors:** Shijie Zhou, Bin Zhu, Jiarui Yang, Xiangyu Zhao, Jingjing Chen et al. (6 authors)

**Published:** 2026-03-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.11106v1) | [PDF](https://arxiv.org/pdf/2603.11106v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have enabled robots to execute increasingly complex tasks. However, VLA models trained through imitation learning struggle to operate reliably in dynamic environments and often fail under Out-of-Distribution (OOD) conditions. To address this issue, we propose Robot-Conditioned Normalizing Flow (RC-NF), a real-time monitoring model for robotic anomaly detection and intervention that ensures the robot's state and the object's motion trajectory...

</details>

---

### [DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference](https://arxiv.org/abs/2603.10469v1)

**Authors:** Yuquan Li, Lianjie Ma, Han Ding, Lijun Zhu

**Published:** 2026-03-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10469v1) | [PDF](https://arxiv.org/pdf/2603.10469v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable generalist robotic manipulation but suffer from high inference latency. This bottleneck stems from the massive number of visual tokens processed by large language backbones. Existing methods either prune or merge tokens uniformly, degrading the spatial reasoning essential for robotic control. We present DepthCache, a training-free framework that leverages depth as a structural prior for visual token compression. It partitions observations into depth-bas...

</details>

---

### [Overcoming Visual Clutter in Vision Language Action Models via Concept-Gated Visual Distillation](https://arxiv.org/abs/2603.10340v1)

**Authors:** Sangmim Song, Sarath Kodagoda, Marc Carmichael, Karthick Thiyagarajan

**Published:** 2026-03-11 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.10340v1) | [PDF](https://arxiv.org/pdf/2603.10340v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate impressive zero-shot generalization but frequently suffer from a "Precision-Reasoning Gap" in cluttered environments. This failure is driven by background-induced feature dilution, where high-frequency semantic noise corrupts the geometric grounding required for precise manipulation. To bridge this gap, we propose Concept-Gated Visual Distillation (CGVD), a training-free, model-agnostic inference framework that stabilizes VLA policies. CGVD operate...

</details>

---

### [Vision-Based Hand Shadowing for Robotic Manipulation via Inverse Kinematics](https://arxiv.org/abs/2603.11383v1)

**Authors:** Hendrik Chiche, Antoine Jamme, Trevor Rigoberto Martinez

**Published:** 2026-03-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.11383v1) | [PDF](https://arxiv.org/pdf/2603.11383v1.pdf)

<details>
<summary>Abstract</summary>

Teleoperation of low-cost robotic manipulators remains challenging due to the complexity of mapping human hand articulations to robot joint commands. We present an offline hand-shadowing and retargeting pipeline from a single egocentric RGB-D camera mounted on 3D-printed glasses. The pipeline detects 21 hand landmarks per hand using MediaPipe Hands, deprojects them into 3D via depth sensing, transforms them into the robot coordinate frame, and solves a damped-least-squares inverse kinematics pro...

</details>

---
