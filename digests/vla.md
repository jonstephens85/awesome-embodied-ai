# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-08 17:02 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing](https://arxiv.org/abs/2604.05014v1)

**Authors:** StarVLA Community

**Published:** 2026-04-06 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.05014v1) | [PDF](https://arxiv.org/pdf/2604.05014v1.pdf) | [GitHub](https://github.com/starVLA/starVLA)

<details>
<summary>Abstract</summary>

Building generalist embodied agents requires integrating perception, language understanding, and action, which are core capabilities addressed by Vision-Language-Action (VLA) approaches based on multimodal foundation models, including recent advances in vision-language models and world models. Despite rapid progress, VLA methods remain fragmented across incompatible architectures, codebases, and evaluation protocols, hindering principled comparison and reproducibility. We present StarVLA, an ope...

</details>

---

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

## Other Recent Papers

### [A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model](https://arxiv.org/abs/2604.05672v1)

**Authors:** Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue et al. (23 authors)

**Published:** 2026-04-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.05672v1) | [PDF](https://arxiv.org/pdf/2604.05672v1.pdf)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) models have emerged as a powerful paradigm for open-world robot manipulation, but their practical deployment is often constrained by \emph{cost}: billion-scale VLM backbones and iterative diffusion/flow-based action heads incur high latency and compute, making real-time control expensive on commodity hardware. We present A1, a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success; O...

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

### [Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?](https://arxiv.org/abs/2604.04502v1)

**Authors:** Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang et al. (7 authors)

**Published:** 2026-04-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.04502v1) | [PDF](https://arxiv.org/pdf/2604.04502v1.pdf)

<details>
<summary>Abstract</summary>

Video generation models have advanced rapidly and are beginning to show a strong understanding of physical dynamics. In this paper, we investigate how far an advanced video generation model such as Veo-3 can support generalizable robotic manipulation. We first study a zero-shot approach in which Veo-3 predicts future image sequences from current robot observations, while an inverse dynamics model IDM recovers the corresponding robot actions. The IDM is trained solely on random-play data, requiri...

</details>

---
