# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-29 19:13 UTC

**Papers found:** 7

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
