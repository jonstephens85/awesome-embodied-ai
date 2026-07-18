# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-18 22:38 UTC

**Papers found:** 3

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278v1)

**Authors:** Zezhong Qian, Xiaowei Chi, Chak-Wing Mak, Tianze Zhou, Ruibin Yuan et al. (12 authors)

**Published:** 2026-07-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.15278v1) | [PDF](https://arxiv.org/pdf/2607.15278v1.pdf) | [Project Page](https://hierarchical-diffusion-reasoning.github.io/)

<details>
<summary>Abstract</summary>

Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework ...

</details>

---

### [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065v1)

**Authors:** Susie Lu, Haonan Chen, Weirui Ye, Yilun Du

**Published:** 2026-07-16 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.15065v1) | [PDF](https://arxiv.org/pdf/2607.15065v1.pdf) | [Project Page](https://susie-lu.github.io/driftworld/)

<details>
<summary>Abstract</summary>

Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. We introduce DriftWorld, an action-conditioned world model based on drifting generative models. Rather than denoising iteratively at inference, DriftWorld learns an action-con...

</details>

---

## Other Recent Papers

### [Concept-Guided Spatial Regularization for World Models in Atari Pong](https://arxiv.org/abs/2607.15142v1)

**Authors:** Yukuan Lu, Zaishuo Xia, Weyl Lu, Yubei Chen

**Published:** 2026-07-16 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.15142v1) | [PDF](https://arxiv.org/pdf/2607.15142v1.pdf)

<details>
<summary>Abstract</summary>

World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation. We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and evaluate them with a closed-loop rollout diagnostic: a policy trained separately f...

</details>

---
