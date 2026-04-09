# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-09 22:32 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Other Recent Papers

### [A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model](https://arxiv.org/abs/2604.05672v2)

**Authors:** Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue et al. (23 authors)

**Published:** 2026-04-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.05672v2) | [PDF](https://arxiv.org/pdf/2604.05672v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for open-world robot manipulation, but their practical deployment is often constrained by cost: billion-scale VLM backbones and iterative diffusion/flow-based action heads incur high latency and compute, making real-time control expensive on commodity hardware. We present A1, a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success; Our approa...

</details>

---

### [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/abs/2604.05656v1)

**Authors:** Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu et al. (6 authors)

**Published:** 2026-04-07 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.05656v1) | [PDF](https://arxiv.org/pdf/2604.05656v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models based on flow matching -- such as pi0, pi0.5, and SmolVLA -- achieve state-of-the-art generalist robotic manipulation, yet their iterative denoising, typically 10 ODE steps, introduces substantial latency: on a modern GPU, denoising alone accounts for 80% of end-to-end inference time. Naively reducing the step count is unreliable, degrading success on most tasks due to the velocity field being uncalibrated for single-step jumps. We present SnapFlow, a plug-and...

</details>

---

### [Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment](https://arxiv.org/abs/2604.05614v1)

**Authors:** Theodor Wulff, Federico Tavella, Rahul Singh Maharjan, Manith Adikari, Angelo Cangelosi

**Published:** 2026-04-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.05614v1) | [PDF](https://arxiv.org/pdf/2604.05614v1.pdf)

<details>
<summary>Abstract</summary>

Achieving robot transparency is a critical step toward effective human-robot collaboration. To be transparent, a robot's natural language communication must be consistent with its actions and explicitly grounded in the task and environment. Existing hierarchical Vision-Language-Action (VLA) models can generate language (e.g., through chain-of-thought) and low-level actions. However, current work does not consider explicit alignment between these modalities during training. To address this crucia...

</details>

---

### [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/abs/2604.05595v1)

**Authors:** Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin

**Published:** 2026-04-07 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.05595v1) | [PDF](https://arxiv.org/pdf/2604.05595v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved remarkable success in robotic manipulation. However, their robustness to linguistic nuances remains a critical, under-explored safety concern, posing a significant safety risk to real-world deployment. Red teaming, or identifying environmental scenarios that elicit catastrophic behaviors, is an important step in ensuring the safe deployment of embodied AI agents. Reinforcement learning (RL) has emerged as a promising approach in automated red tea...

</details>

---

### [ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving](https://arxiv.org/abs/2604.05378v1)

**Authors:** Kaiser Hamid, Can Cui, Nade Liang

**Published:** 2026-04-07 | **Categories:** cs.CL, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.05378v1) | [PDF](https://arxiv.org/pdf/2604.05378v1.pdf)

<details>
<summary>Abstract</summary>

Recent progress in vision-language-action (VLA) models has enabled language-conditioned driving agents to execute natural-language navigation commands in closed-loop simulation, yet standard evaluations largely assume instructions are precise and well-formed. In deployment, instructions vary in phrasing and specificity, may omit critical qualifiers, and can occasionally include misleading, authority-framed text, leaving instruction-level robustness under-measured. We introduce ICR-Drive, a diagn...

</details>

---

### [VLA-InfoEntropy: A Training-Free Vision-Attention Information Entropy Approach for Vision-Language-Action Models Inference Acceleration and Success](https://arxiv.org/abs/2604.05323v1)

**Authors:** Chuhang Liu, Yayun He, Zuheng Kang, Xiaoyang Qu, Jianzong Wang

**Published:** 2026-04-07 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.05323v1) | [PDF](https://arxiv.org/pdf/2604.05323v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action decision-making for cross-modal semantic alignment, exhibiting broad application potential. However, the joint processing of high-dimensional visual features, complex linguistic inputs, and continuous action sequences incurs significant computational overhead and low inference efficiency, thereby hindering real-time deployment and reliability. To address this issue, we use image entropy to quantif...

</details>

---

### [ExpressMM: Expressive Mobile Manipulation Behaviors in Human-Robot Interactions](https://arxiv.org/abs/2604.05320v1)

**Authors:** Souren Pashangpour, Haitong Wang, Matthew Lisondra, Goldie Nejat

**Published:** 2026-04-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.05320v1) | [PDF](https://arxiv.org/pdf/2604.05320v1.pdf)

<details>
<summary>Abstract</summary>

Mobile manipulators are increasingly deployed in human-centered environments to perform tasks. While completing such tasks, they should also be able to communicate their intent to the people around them using expressive robot behaviors. Prior work on expressive robot behaviors has used preprogrammed or learning-from-demonstration- based expressive motions and large language model generated high-level interactions. The majority of these existing approaches have not considered human-robot interact...

</details>

---
