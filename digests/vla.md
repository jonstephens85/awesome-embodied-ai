# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-04-28 22:46 UTC

**Papers found:** 7

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2604.24622v1)

**Authors:** Fan Du, Feng Yan, Jianxiong Wu, Xinrun Xu, Weiye Zhang et al. (9 authors)

**Published:** 2026-04-27 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.24622v1) | [PDF](https://arxiv.org/pdf/2604.24622v1.pdf) | [GitHub](https://github.com/EmbodiedAI-RoboTron/CF-VLA)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structure from uninformative Gaussian noise, leading to a poor efficiency-quality trade-off under real-time constraints. We address this issue by rethinking the role of the starting point in generative action modeling. Instead of shortening the sampling trajectory, we propose CF-VLA, a coarse-to-fine two-s...

</details>

---

### [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://arxiv.org/abs/2604.24447v1)

**Authors:** Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li et al. (6 authors)

**Published:** 2026-04-27 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.24447v1) | [PDF](https://arxiv.org/pdf/2604.24447v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are promising for generalist robot control, but on-robot deployment is bottlenecked by real-time inference under tight cost and energy budgets. Most prior evaluations rely on desktop-grade GPUs, obscuring the trade-offs and opportunities offered by heterogeneous edge accelerators (GPUs/XPUs/NPUs). We present a systematic analysis for low-cost VLA deployment via model-hardware co-characterization. First, we build a cross-accelerator leaderboard and evaluate mod...

</details>

---

## Other Recent Papers

### [$M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills](https://arxiv.org/abs/2604.24182v1)

**Authors:** Siyao Xiao, Yuhong Zhang, Zhifang Liu, Zihan Gao, Jingye Zhang et al. (12 authors)

**Published:** 2026-04-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.24182v1) | [PDF](https://arxiv.org/pdf/2604.24182v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models predominantly rely on end-to-end fine-tuning. While effective, this paradigm compromises the inherent generalization capabilities of Vision-Language Models (VLMs) and incurs catastrophic forgetting. To address these limitations, we propose $M^2$-VLA, which demonstrates that a generalized VLM is able to serve as a powerful backbone for robotic manipulation directly. However, it remains a key challenge to bridge the gap between the high-level semantic un...

</details>

---

### [AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation](https://arxiv.org/abs/2604.24086v1)

**Authors:** Kai Yang, Zedong Chu, Yingnan Guo, Zhengbo Wang, Shichao Xie et al. (9 authors)

**Published:** 2026-04-27 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.24086v1) | [PDF](https://arxiv.org/pdf/2604.24086v1.pdf)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have been demonstrated possessing strong zero-shot generalization for robot control, their massive parameter sizes typically necessitate cloud-based deployment. However, cloud deployment introduces network jitter and inference latency, which can induce severe spatiotemporal misalignment in mobile navigation under continuous displacement, so that the stale intents expressed in past ego frames may become spatially incorrect in the current frame and lead to...

</details>

---

### [Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2604.24681v1)

**Authors:** Yifan Xie, YuAn Wang, Guangyu Chen, Jinkun Liu, Yu Sun et al. (6 authors)

**Published:** 2026-04-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.24681v1) | [PDF](https://arxiv.org/pdf/2604.24681v1.pdf)

<details>
<summary>Abstract</summary>

Human videos contain rich manipulation priors, but using them for robot learning remains difficult because raw observations entangle scene understanding, human motion, and embodiment-specific action. We introduce MoT-HRA, a hierarchical vision-language-action framework that learns human-intention priors from large-scale human demonstrations. We first curate HA-2.2M, a 2.2M-episode action-language dataset reconstructed from heterogeneous human videos through hand-centric filtering, spatial recons...

</details>

---

### [Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775v1)

**Authors:** Qi Li, Bo Yin, Weiqi Huang, Ruhao Liu, Bojun Zou et al. (9 authors)

**Published:** 2026-04-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.23775v1) | [PDF](https://arxiv.org/pdf/2604.23775v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence. This shift raises a new class of safety challenges, stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajectories, and vulnerabilities in the data supply chain. Yet the literature remains fragmented across roboti...

</details>

---

### [Move-Then-Operate: Behavioral Phasing for Human-Like Robotic Manipulation](https://arxiv.org/abs/2604.23620v1)

**Authors:** Haoming Xu, Lei Lei, Jie Gu, Chu Tang, Jingmin Chen et al. (6 authors)

**Published:** 2026-04-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.23620v1) | [PDF](https://arxiv.org/pdf/2604.23620v1.pdf)

<details>
<summary>Abstract</summary>

We present Move-Then-Operate, a Vision language action framework that explicitly decouples robotic manipulation into two distinct behavioral phases: coarse relocation (move) and contact-critical interaction (operate). Unlike monolithic policies that conflate these heterogeneous regimes, our architecture employs a dual-expert policy routed by a learnable phase selector, introducing a structural inductive bias that isolates phase-specific dynamics. Phase labels are automatically generated via an M...

</details>

---
