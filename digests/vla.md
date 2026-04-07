# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-07 16:59 UTC

**Papers found:** 5

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes](https://arxiv.org/abs/2604.04834v1)

**Authors:** Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang

**Published:** 2026-04-06 | **Categories:** cs.CV, cs.MM, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.04834v1) | [PDF](https://arxiv.org/pdf/2604.04834v1.pdf) | [GitHub](https://github.com/JJayzee/E-VLA)

<details>
<summary>Abstract</summary>

Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perc...

</details>

---

### [ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration](https://arxiv.org/abs/2604.04664v1)

**Authors:** Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu et al. (7 authors)

**Published:** 2026-04-06 | **Categories:** cs.RO, cs.AI, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2604.04664v1) | [PDF](https://arxiv.org/pdf/2604.04664v1.pdf) | [Project Page](https://www.rosclaw.io/)

<details>
<summary>Abstract</summary>

The integration of large language models (LLMs) with embodied agents has improved high-level reasoning capabilities; however, a critical gap remains between semantic understanding and physical execution. While vision-language-action (VLA) and vision-language-navigation (VLN) systems enable robots to perform manipulation and navigation tasks from natural language instructions, they still struggle with long-horizon sequential and temporally structured tasks. Existing frameworks typically adopt mod...

</details>

---

### [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/abs/2604.04161v1)

**Authors:** Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng et al. (8 authors)

**Published:** 2026-04-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.04161v1) | [PDF](https://arxiv.org/pdf/2604.04161v1.pdf) | [Project Page](https://lance-lot.github.io/adaptive-chunking.github.io/)

<details>
<summary>Abstract</summary>

In Vision-Language-Action (VLA) models, action chunking (i.e., executing a sequence of actions without intermediate replanning) is a key technique to improve robotic manipulation abilities. However, a large chunk size reduces the model's responsiveness to new information, while a small one increases the likelihood of mode-jumping, jerky behavior resulting from discontinuities between chunks. Therefore, selecting the optimal chunk size is an urgent demand to balance the model's reactivity and con...

</details>

---

## Other Recent Papers

### [Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?](https://arxiv.org/abs/2604.04502v1)

**Authors:** Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang et al. (7 authors)

**Published:** 2026-04-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.04502v1) | [PDF](https://arxiv.org/pdf/2604.04502v1.pdf)

<details>
<summary>Abstract</summary>

Video generation models have advanced rapidly and are beginning to show a strong understanding of physical dynamics. In this paper, we investigate how far an advanced video generation model such as Veo-3 can support generalizable robotic manipulation. We first study a zero-shot approach in which Veo-3 predicts future image sequences from current robot observations, while an inverse dynamics model IDM recovers the corresponding robot actions. The IDM is trained solely on random-play data, requiri...

</details>

---

### [VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/abs/2604.03956v1)

**Authors:** Ravi Ranjan, Agoritsa Polyzou

**Published:** 2026-04-05 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.03956v1) | [PDF](https://arxiv.org/pdf/2604.03956v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are emerging as embodied foundation models for robotic manipulation, but their deployment introduces a new unlearning challenge: removing unsafe, spurious, or privacy-sensitive behaviors without degrading perception, language grounding, and action control. In OpenVLA-style policies, behavior is produced through a fused visual encoder, a cross-modal projector, and a language backbone that predicts tokenized robot actions, so undesirable knowledge can be distrib...

</details>

---
