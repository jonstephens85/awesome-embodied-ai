# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-15 16:22 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Other Recent Papers

### [Decoding Task Progress from VLA Representations](https://arxiv.org/abs/2608.13474v1)

**Authors:** Atiksh Bhardwaj, Edward Weiyi Duan, Prithwish Dan, Wei-Chiu Ma, Preston Culbertson

**Published:** 2026-08-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.13474v1) | [PDF](https://arxiv.org/pdf/2608.13474v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are moving rapidly towards deployment as general-purpose manipulation policies, but we currently lack basic tools for understanding what these models represent internally or for monitoring them at runtime. Leveraging ideas from mechanistic interpretability, we probe the residual stream of $π_{0.5}$ and find that task progress, the normalized time remaining in a trajectory, is linearly readable from the activations. We find that this signal is present in the p...

</details>

---

### [UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](https://arxiv.org/abs/2608.13453v1)

**Authors:** Yukun Dai, Mingzhe Dai, Tianshi Wang, Fengling Li, Jingjing Li et al. (6 authors)

**Published:** 2026-08-13 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.13453v1) | [PDF](https://arxiv.org/pdf/2608.13453v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We intr...

</details>

---

### [FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2608.13395v1)

**Authors:** Hao Dou

**Published:** 2026-08-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.13395v1) | [PDF](https://arxiv.org/pdf/2608.13395v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy. Group relative policy optimization (GRPO) learns from reward differences within each rollout group. When all sampled trajectories are poor, this relative signal can rank failures without identifying behavior outside the failed region. We introduce FIRE-VLA, a failure-informed self-evolution framework that converts such unresolved failures into privile...

</details>

---

### [Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2608.13026v1)

**Authors:** Yao Zhou, Hang Gao, Fengge Wu, Changwen Zheng, Wenwen Qiang

**Published:** 2026-08-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.13026v1) | [PDF](https://arxiv.org/pdf/2608.13026v1.pdf)

<details>
<summary>Abstract</summary>

Outcome-driven reinforcement learning offers a scalable way to post-train vision-language-action (VLA) policies from sparse task-success feedback. In common GRPO-based VLA post-training, one rollout-level advantage is applied to every action in the trajectory. A rollout that completes several valid stages but fails later can therefore penalize the actions that produced its earlier progress. We call this trajectory-level credit aliasing. Temporal GRPO addresses this problem by constructing detect...

</details>

---

### [FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving](https://arxiv.org/abs/2608.12932v1)

**Authors:** Zekai Li, Yihao Liang, Hongfei Zhang, Jian Chen, Yesheng Liang et al. (6 authors)

**Published:** 2026-08-13 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.12932v1) | [PDF](https://arxiv.org/pdf/2608.12932v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-match...

</details>

---

### [BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving](https://arxiv.org/abs/2608.12854v1)

**Authors:** Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu et al. (11 authors)

**Published:** 2026-08-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.12854v1) | [PDF](https://arxiv.org/pdf/2608.12854v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving requires planning under both semantic constraints and predictive dynamics. Existing end-to-end driving approaches, however, typically emphasize only one side of this requirement: Vision-Language-Action (VLA) models exploit VLM priors for semantic reasoning, while World Action Models (WAMs) provide future-aware prediction through generative world modeling. This naturally motivates a unified planner that can leverage both semantic priors and predictive dynamics. However, we find...

</details>

---
