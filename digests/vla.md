# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-11 16:57 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action](https://arxiv.org/abs/2607.08182v1)

**Authors:** Qi Lyu, Baicheng Liu, Xudong Wang, Jiahua Dong, Lianqing Liu et al. (6 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.08182v1) | [PDF](https://arxiv.org/pdf/2607.08182v1.pdf) | [GitHub](https://github.com/LyuQi127/LEEVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models aim to map multimodal inputs to robot actions. However, most existing approaches struggle to cover complex dynamic scenarios due to treating all visual tokens uniformly and reasoning with human-selected factors, which lack mechanisms to emphasize task-critical evidence and ignore underlying factors. To address this issue, we propose LEEVLA, a VLA architecture for seeing what matters in Latent Environment Evolution that explicitly guides the model toward inform...

</details>

---

## Other Recent Papers

### [FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation](https://arxiv.org/abs/2607.08575v1)

**Authors:** Shiyuan Yang, Borong Zhang, Jizheng Zhang, Zhijia Tao, Junfei Guo et al. (8 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08575v1) | [PDF](https://arxiv.org/pdf/2607.08575v1.pdf)

<details>
<summary>Abstract</summary>

We present FabriVLA, a lightweight Vision-Language-Action model for Precise Multi-Task Manipulation. FabriVLA combines an InternVL3.5 vision-language backbone with a flow-matching action head featuring gated self-attention across action tokens and shallow VLM layer fusion for enriched spatial context. The model is trained via single stage joint optimization from a pretrained VLM and randomly initialized action head. On the Meta-World MT50 benchmark spanning 50 diverse manipulation tasks, FabriVL...

</details>

---

### [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448v1)

**Authors:** Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu et al. (16 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08448v1) | [PDF](https://arxiv.org/pdf/2607.08448v1.pdf)

<details>
<summary>Abstract</summary>

Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional rea...

</details>

---

### [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375v1)

**Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang et al. (8 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.08375v1) | [PDF](https://arxiv.org/pdf/2607.08375v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-V...

</details>

---

### [TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning](https://arxiv.org/abs/2607.08283v1)

**Authors:** Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang et al. (9 authors)

**Published:** 2026-07-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08283v1) | [PDF](https://arxiv.org/pdf/2607.08283v1.pdf)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) policies such as $π_{0.5}$ and OpenVLA perform well on many manipulation tasks, but they are often reactive: the next action is predicted from the current observation, instruction, and proprioceptive state. This assumption breaks down in stage-dependent manipulation, where visually similar states may require different actions depending on latent task progress and previous interaction outcomes. We argue that such tasks require not only memory, but dynamics-aware bel...

</details>

---

### [Post-Training in End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08072v1)

**Authors:** Ruining Yang, Muxing Wang, Yixiao Chen, Tongfei Guo, Yi Xu et al. (11 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.08072v1) | [PDF](https://arxiv.org/pdf/2607.08072v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end models that map multimodal inputs directly to future trajectories/maneuvers have emerged as an increasingly prominent research paradigm in autonomous driving. This class of models includes both Vision-Language-Action models and trajectory-generative planners. Unlike classic machine learning applications, autonomous vehicles operate in safety-critical and interaction-intensive environments where traditional open-loop imitation of expert demonstrations is not sufficient to ensure reliab...

</details>

---
