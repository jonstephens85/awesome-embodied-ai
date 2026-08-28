# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-28 05:52 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578v1)

**Authors:** Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, Xu-Han Chen, Yinghao Li et al. (12 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.26578v1) | [PDF](https://arxiv.org/pdf/2608.26578v1.pdf) | [Project Page](https://john-liua.github.io/TrapVLA/)

<details>
<summary>Abstract</summary>

This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failure modes. Unlike prior backdoor attacks that treat any task failure as a successful attack, Configured Failure Trapping requires the attacker to control how the robot fails (e.g., causing the robot to grasp with a specified positional offset), making it substantially more challenging...

</details>

---

### [Decoupling Planning and Control for Instructable Agents](https://arxiv.org/abs/2608.26788v1)

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr

**Published:** 2026-08-27 | **Categories:** cs.AI, cs.CL, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2608.26788v1) | [PDF](https://arxiv.org/pdf/2608.26788v1.pdf) | [Project Page](https://zinengtang.github.io/instruct-to-act/)

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model c...

</details>

---

### [One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058v1)

**Authors:**  Xiaomi Embodied Intelligence Team, University of Macau,  :, Shaoqing Xu, Fang Li et al. (24 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.26058v1) | [PDF](https://arxiv.org/pdf/2608.26058v1.pdf) | [Project Page](https://public-bots.github.io/UCAG-P)

<details>
<summary>Abstract</summary>

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action ...

</details>

---

### [MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization](https://arxiv.org/abs/2608.25864v1)

**Authors:** Zaibin Zhang, Junlan Xiao, Zhongbo Zhang, Yifan Wang, Li Kang et al. (14 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25864v1) | [PDF](https://arxiv.org/pdf/2608.25864v1.pdf) | [GitHub](https://github.com/zhangzaibin/future-robots)

<details>
<summary>Abstract</summary>

Multi-arm collaboration is becoming a core capability in embodied manipulation. Recent vision-language-action (VLA) models integrate perception, language, and control, but most represent language as a single global instruction and do not provide an explicit mechanism for assigning and composing arm-specific behaviors. This design limits transfer to collaboration patterns that differ from those observed during training. We present MA-VLA, a unified framework for multi-arm collaboration via atomic...

</details>

---

### [A Taxonomy of Construction Task Activities for Robot Workers](https://arxiv.org/abs/2608.25395v1)

**Authors:** Sadman Sakib, Zhangyi None Peng, Yujie Pang, Yu Otsuki, Mohammad Abdullah Al Faruque

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25395v1) | [PDF](https://arxiv.org/pdf/2608.25395v1.pdf) | [GitHub](https://github.com/AICPS/TARCAT-Taxonomy)

<details>
<summary>Abstract</summary>

Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems. Construction deployment, however, requires a precise inventory of worker activities and the capabilities needed to execute them. We present TARCAT, an occupation-grounded taxonomy derived from 91 O*NET tasks across seven high-employment construction occupations and 30 instructional videos of physical work. TARCAT defines 41 action primitives in 12 groups and three cla...

</details>

---

## Other Recent Papers

### [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384v1)

**Authors:** Zekai Li, Jiaming Tang, Zhijian Liu

**Published:** 2026-08-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.27384v1) | [PDF](https://arxiv.org/pdf/2608.27384v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly promising for robotic manipulation, yet their real-world deployment remains bottlenecked by high inference latency and unstable asynchronous execution. This challenge is particularly pronounced in flow-matching-based VLA models, where action decoding requires multiple iterative steps conditioned on the VLM context. While efficient inference methods improve control frequency and asynchronous methods reduce execution idle time, existing approach...

</details>

---

### [GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.27079v1)

**Authors:** Yibo Qiu, Haoliang Ye, Shu'ang Sun, Zan Huang, Ronald X Xu et al. (6 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.27079v1) | [PDF](https://arxiv.org/pdf/2608.27079v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) policies provide strong priors for robot manipulation, yet adapting them online to fine-grained biomedical tasks remains challenging. Task success often hinges on subtle, view-dependent visual cues, while task-level rewards provide little guidance about which regions matter, making it difficult to learn task-relevant visual grounding from limited real-robot interaction. Online adaptation is further constrained by the computational cost of VLA inference and...

</details>

---

### [TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2608.26821v1)

**Authors:** Jiarui Yang, Yehao Lu, Yuning Su, Yu Zhong, Yufeng Xie et al. (12 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.26821v1) | [PDF](https://arxiv.org/pdf/2608.26821v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models leverage pretrained vision-language representations for robot control, yet simply adding historical frames does not reliably capture recent physical change. This is especially problematic in multi-stage manipulation, where visually similar states may require different actions depending on prior execution. To address this challenge, we present TemporalFlow-VLA, which learns compact execution history through physically grounded temporal supervision. Using record...

</details>

---

### [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645v1)

**Authors:** Ganlong Zhao, Zijia Tang, Xingping Chen, Zhanghui Kuang, Ye Tian et al. (6 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.26645v1) | [PDF](https://arxiv.org/pdf/2608.26645v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models~(VLAs) have demonstrated significant promise in generalizing to complex, long-horizon robotic manipulation tasks. However, their performance remains brittle, as they are typically trained on trajectory-monotonic, failure-free demonstrations. This reliance on ``perfect" data leaves them unable to recover from common execution errors, such as a missed grasp, a dropped object, or an unexpected collision. In this paper, we propose FLARE, a novel framework that endows VL...

</details>

---

### [PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation](https://arxiv.org/abs/2608.26673v1)

**Authors:** Hiroki Sawada, Shunichi Kasahara

**Published:** 2026-08-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.26673v1) | [PDF](https://arxiv.org/pdf/2608.26673v1.pdf)

<details>
<summary>Abstract</summary>

Large pretrained vision-language-action models dominate modern robot-manipulation benchmarks, but it remains unclear how much model scale is necessary for strong language-conditioned control, or whether fundamentally different control architectures can remain competitive at much smaller parameter budgets. We present PredVLA, a language-conditioned predictive-coding policy with only 0.68 million trainable network parameters and no robot-data pretraining, whose hierarchical generative recurrent dy...

</details>

---

### [StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.26067v1)

**Authors:** Zhe Liu, Jinghua Hou, Yuxiang Lu, Zhenya Yang, Xianzhe Fan et al. (10 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.26067v1) | [PDF](https://arxiv.org/pdf/2608.26067v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored...

</details>

---

### [LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation](https://arxiv.org/abs/2608.25757v2)

**Authors:** Jin Lou, Zhiyuan Jing, Andong Chen, Xupeng Wang, Yuan Xu et al. (23 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.25757v2) | [PDF](https://arxiv.org/pdf/2608.25757v2.pdf)

<details>
<summary>Abstract</summary>

Generalist vision--language--action (VLA) policies learn long-horizon behavior mainly through short-horizon action prediction and reveal little beyond sampled commands. This creates two coupled bottlenecks: a single action target must implicitly absorb task progress, intermediate intent, and local reliability, while these control states remain hidden during execution. Inspired by functional principles of biological sensorimotor control, we introduce LM-X , which organizes prediction across task,...

</details>

---

### [GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)

**Authors:** Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He et al. (11 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25659v1) | [PDF](https://arxiv.org/pdf/2608.25659v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have advanced language-conditioned robotic manipulation, yet action-imitation objectives provide only weak supervision for metric 3D structure and short-horizon physical evolution. Geometry-enhanced policies mainly improve current-scene grounding, whereas predictive policies often model future dynamics in RGB or latent spaces and may incur substantial deployment cost. GaussianDream demonstrates that training-time current Gaussian reconstruction and future Ga...

</details>

---

### [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](https://arxiv.org/abs/2608.25585v1)

**Authors:** Sanghwan Jang, Minjin Jeon, Minsoo Kim, Seongjin Choi, Dongha Kim et al. (6 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.25585v1) | [PDF](https://arxiv.org/pdf/2608.25585v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a versatile foundation for general robotic manipulation, yet they exhibit significant brittleness when confronted with novel task distributions. While In-Context Imitation Learning (ICIL) offers a training-free alternative, existing frameworks suffer from an adaptation bottleneck that hinders the effective translation of expert context to executable actions. This failure originates from superficial retrieval mechanisms and an inherent behavioral inerti...

</details>

---

### [V-Link: Recovering Lost Visual Representations in Action DiT for Vision-Language-Action Models](https://arxiv.org/abs/2608.25308v1)

**Authors:** Yehao Lu, Jiarui Yang, Yuning Su, Yufeng Xie, Yu Zhong et al. (13 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.25308v1) | [PDF](https://arxiv.org/pdf/2608.25308v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a scalable path toward generalist robotic manipulation by integrating visual perception, language understanding, and continuous action control. However, we reveal a critical limitation of VLA architectures: the action expert has limited access to the 3D geometric and 2D semantic information available in VLM features. This accessibility gap weakens perceptual grounding and limits performance on fine-grained robotic manipulation. To address this issue, w...

</details>

---

### [TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback](https://arxiv.org/abs/2608.25798v1)

**Authors:** Jianbo Zhou, Boyuan Zhao, Yuzheng Zhang, Yiyang Chen, Wenxin Chen et al. (11 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.25798v1) | [PDF](https://arxiv.org/pdf/2608.25798v1.pdf)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon. However, chunk-based vision-language-action models predict complete action chunks from observations collected before execution, leaving tactile conditioning stale during execution. Existing tactile-reactive approaches typically rely on separate high-frequency controllers, which increase both architectural and training complexity. In this paper, we introduce TacForcing, a streamin...

</details>

---
