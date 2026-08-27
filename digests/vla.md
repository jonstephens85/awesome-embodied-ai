# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-27 02:24 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control](https://arxiv.org/abs/2608.24115v1)

**Authors:** Suhwan Choi, Jaeyoon Jung, Sungkyung Kim, Yunsung Lee, Youngjae Yu

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.24115v1) | [PDF](https://arxiv.org/pdf/2608.24115v1.pdf) | [Project Page](https://worv-ai.github.io/ponderpounce/)

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) can integrate long visual histories, reason under partial observability, and infer behavior from a few examples. Yet vision-language-action (VLA) models generally inherit pretrained representations without using this contextual capacity as episode memory. Memory-dependent policies address this gap through purpose-built history mechanisms. PonderPounce instead reuses an MLLM's native causal context as robot memory. Ponder, a System2 MLLM, accumulates episo...

</details>

---

### [Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models](https://arxiv.org/abs/2608.24042v1)

**Authors:** Haoran Hao, Shahram Najam Syed, Jeff Schneider, Jeffrey Ichnowski

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.24042v1) | [PDF](https://arxiv.org/pdf/2608.24042v1.pdf) | [Project Page](https://hoar012.github.io/HSR-Project)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models pretrained on large-scale robot datasets provide a strong foundation for robot manipulation, their performance can degrade when adapted to new tasks with limited task-specific demonstrations. Retrieval offers a practical way to reuse existing demonstrations for data-efficient adaptation, but existing methods often rely on visual similarity, state-action representations, or task-level language matching. These approaches may overlook the hierarchical struc...

</details>

---

## Other Recent Papers

### [StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.26067v1)

**Authors:** Zhe Liu, Jinghua Hou, Yuxiang Lu, Zhenya Yang, Xianzhe Fan et al. (10 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.26067v1) | [PDF](https://arxiv.org/pdf/2608.26067v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored...

</details>

---

### [LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation](https://arxiv.org/abs/2608.25757v1)

**Authors:** Jin Lou, Jingxuan Zhu, Andong Chen, Xupeng Wang, Yuan Xu et al. (17 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.25757v1) | [PDF](https://arxiv.org/pdf/2608.25757v1.pdf)

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

### [Gripper-aware Vision Language Action Models](https://arxiv.org/abs/2608.24603v1)

**Authors:** Hanyi Zhang, Zihong Luo, Tianyu Li, Khang Nguyen, Basu Hela et al. (19 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24603v1) | [PDF](https://arxiv.org/pdf/2608.24603v1.pdf)

<details>
<summary>Abstract</summary>

Vision language action models (VLAs) have advanced general purpose robotic grasping and manipulation by enabling robots to interpret visual observations and natural language instructions to generate executable action sequences. However, existing VLAs often implicitly assume gripper invariance, despite grasping strategies being inherently embodiment-dependent. Different gripper types, such as parallel-jaw and suction, usually require distinct interaction strategies to achieve the same grasping ob...

</details>

---

### [GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1)

**Authors:** Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn

**Published:** 2026-08-25 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.24959v1) | [PDF](https://arxiv.org/pdf/2608.24959v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models encode visual observations as flat 2D patch tokens that carry no intrinsic geometric structure, and augmenting them with dense monocular depth injects per-pixel scalar values that encode neither surface orientation nor geometric confidence. This leaves the policy with limited structured spatial reasoning for action prediction. We propose GaussVLA, a Mamba-based VLA that incorporates two custom modules: Gaussian Spatial Tokenizer (GST) to lift frozen semantic a...

</details>

---

### [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](https://arxiv.org/abs/2608.24101v1)

**Authors:** Zhi Cao, Howard Ji, Kevin Zhang, Kuangzhi Ge, Li Fei-Fei et al. (7 authors)

**Published:** 2026-08-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.24101v1) | [PDF](https://arxiv.org/pdf/2608.24101v1.pdf)

<details>
<summary>Abstract</summary>

Robot actions are inherently embodiment-specific and only weakly aligned with image-space visual changes, limiting their effectiveness as conditioning signals for robot world models. In contrast, visual tracks provide an embodiment-agnostic representation of how task-relevant points move through a scene, offering dense image-space guidance for accurate and spatially precise future video prediction. Building on this observation, we propose TrAct, a world-model-based robot decision-making framewor...

</details>

---
