# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-23 17:20 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance](https://arxiv.org/abs/2604.20834v1)

**Authors:** Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian et al. (15 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20834v1) | [PDF](https://arxiv.org/pdf/2604.20834v1.pdf) | [Project Page](https://getterupper.github.io/PokeVLA)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-la...

</details>

---

### [UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)

**Authors:** Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge et al. (6 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19734v1) | [PDF](https://arxiv.org/pdf/2604.19734v1.pdf) | [Project Page](https://xpeng-robotics.github.io/unit/)

<details>
<summary>Abstract</summary>

Scaling humanoid foundation models is bottlenecked by the scarcity of robotic data. While massive egocentric human data offers a scalable alternative, bridging the cross-embodiment chasm remains a fundamental challenge due to kinematic mismatches. We introduce UniT (Unified Latent Action Tokenizer via Visual Anchoring), a framework that establishes a unified physical language for human-to-humanoid transfer. Grounded in the philosophy that heterogeneous kinematics share universal visual consequen...

</details>

---

### [FASTER: Value-Guided Sampling for Fast RL](https://arxiv.org/abs/2604.19730v1)

**Authors:** Perry Dong, Alexander Swerdlow, Dorsa Sadigh, Chelsea Finn

**Published:** 2026-04-21 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19730v1) | [PDF](https://arxiv.org/pdf/2604.19730v1.pdf) | [GitHub](https://github.com/alexanderswerdlow/faster)

<details>
<summary>Abstract</summary>

Some of the most performant reinforcement learning algorithms today can be prohibitively expensive as they use test-time scaling methods such as sampling multiple action candidates and selecting the best one. In this work, we propose FASTER, a method for getting the benefits of sampling-based test-time scaling of diffusion-based policies without the computational cost by tracing the performance gain of action samples back to earlier in the denoising process. Our key insight is that we can model ...

</details>

---

### [VLA Foundry: A Unified Framework for Training Vision-Language-Action Models](https://arxiv.org/abs/2604.19728v1)

**Authors:** Jean Mercat, Sedrick Keh, Kushal Arora, Isabella Huang, Paarth Shah et al. (8 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.19728v1) | [PDF](https://arxiv.org/pdf/2604.19728v1.pdf) | [Project Page](https://tri-ml.github.io/vla_foundry) | [GitHub](https://github.com/TRI-ML/vla_foundry)

<details>
<summary>Abstract</summary>

We present VLA Foundry, an open-source framework that unifies LLM, VLM, and VLA training in a single codebase. Most open-source VLA efforts specialize on the action training stage, often stitching together incompatible pretraining pipelines. VLA Foundry instead provides a shared training stack with end-to-end control, from language pretraining to action-expert fine-tuning. VLA Foundry supports both from-scratch training and pretrained backbones from Hugging Face. To demonstrate the utility of ou...

</details>

---

### [SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model](https://arxiv.org/abs/2604.19710v1)

**Authors:** Zewei Zhou, Ruining Yang,  Xuewei,  Qi, Yiluan Guo et al. (11 authors)

**Published:** 2026-04-21 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.19710v1) | [PDF](https://arxiv.org/pdf/2604.19710v1.pdf) | [Project Page](https://spanvla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising autonomous driving paradigm for leveraging world knowledge and reasoning capabilities, especially in long-tail scenarios. However, existing VLA models often struggle with the high latency in action generation using an autoregressive generation framework and exhibit limited robustness. In this paper, we propose SpanVLA, a novel end-to-end autonomous driving framework, integrating an autoregressive reasoning and a flow-matching action expert. F...

</details>

---

## Other Recent Papers

### [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](https://arxiv.org/abs/2604.20472v1)

**Authors:** Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.20472v1) | [PDF](https://arxiv.org/pdf/2604.20472v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in vision-language-action (VLA) models for robotics have highlighted the importance of reliable uncertainty quantification in sequential tasks. However, assessing and improving calibration in such settings remains mostly unexplored, especially when only partial trajectories are observed. In this work, we formulate sequential calibration for episodic tasks, where task-success confidence is produced along an episode, while success is determined at the end of it. We introduce a sequ...

</details>

---

### [A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking](https://arxiv.org/abs/2604.20347v1)

**Authors:** Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.20347v1) | [PDF](https://arxiv.org/pdf/2604.20347v1.pdf)

<details>
<summary>Abstract</summary>

Ultrasound (US)-guided needle insertion is a critical yet challenging procedure due to dynamic imaging conditions and difficulties in needle visualization. Many methods have been proposed for automated needle insertion, but they often rely on hand-crafted pipelines with modular controllers, whose performance degrades in challenging cases. In this paper, a Vision-Language-Action (VLA) model is proposed for adaptive and automated US-guided needle insertion and tracking on a robotic ultrasound (RUS...

</details>

---

### [JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy](https://arxiv.org/abs/2604.20100v1)

**Authors:** Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li et al. (62 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20100v1) | [PDF](https://arxiv.org/pdf/2604.20100v1.pdf)

<details>
<summary>Abstract</summary>

Robotic autonomy in open-world environments is fundamentally limited by insufficient data diversity and poor cross-embodiment generalization. Existing robotic datasets are often limited in scale and task coverage, while relatively large differences across robot embodiments impede effective behavior knowledge transfer. To address these challenges, we propose JoyAI-RA, a vision-language-action (VLA) embodied foundation model tailored for generalizable robotic manipulation. JoyAI-RA presents a mult...

</details>

---

### [Cortex 2.0: Grounding World Models in Real-World Industrial Deployment](https://arxiv.org/abs/2604.20246v1)

**Authors:** Adriana Aida, Walida Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch et al. (28 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.20246v1) | [PDF](https://arxiv.org/pdf/2604.20246v1.pdf)

<details>
<summary>Abstract</summary>

Industrial robotic manipulation demands reliable long-horizon execution across embodiments, tasks, and changing object distributions. While Vision-Language-Action models have demonstrated strong generalization, they remain fundamentally reactive. By optimizing the next action given the current observation without evaluating potential futures, they are brittle to the compounding failure modes of long-horizon tasks. Cortex 2.0 shifts from reactive control to plan-and-act by generating candidate fu...

</details>

---

### [EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training](https://arxiv.org/abs/2604.20012v1)

**Authors:** Yiyang Du, Zhanqiu Guo, Xin Ye, Liu Ren, Chenyan Xiong

**Published:** 2026-04-21 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2604.20012v1) | [PDF](https://arxiv.org/pdf/2604.20012v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) inherit their visual and linguistic capabilities from Vision-Language Models (VLMs), yet most VLAs are built from off-the-shelf VLMs that are not adapted to the embodied domain, limiting their downstream performance. In this work, we propose EmbodiedMidtrain to bridge the gap between VLMs and VLAs. We first characterize the data distribution gap between them, showing that VLA data occupy compact regions that are largely separated from the broader VLM distribu...

</details>

---

### [If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844v1)

**Authors:** Jiamin Chang, Minhui Xue, Ruoxi Sun, Shuchao Pang, Salil S. Kanhere et al. (6 authors)

**Published:** 2026-04-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19844v1) | [PDF](https://arxiv.org/pdf/2604.19844v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in embodied Vision-Language Agentic Systems (VLAS), powered by large vision-language models (LVLMs), enable AI systems to perceive and reason over real-world scenes. Within this context, environmental signals such as traffic lights are essential in-band signals that can and should influence agent behavior. However, similar signals could also be crafted to operate as misleading visual injections, overriding user intent and posing security risks. This duality creates a fundamental ...

</details>

---
