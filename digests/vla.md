# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-14 22:12 UTC

**Papers found:** 12

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

### [Scaling Automatic Research Agents via World Models](https://arxiv.org/abs/2608.12564v1)

**Authors:** Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li et al. (10 authors)

**Published:** 2026-08-12 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.12564v1) | [PDF](https://arxiv.org/pdf/2608.12564v1.pdf)

<details>
<summary>Abstract</summary>

Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment exec...

</details>

---

### [DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.12308v1)

**Authors:** Yan Deng, Fei Xu

**Published:** 2026-08-12 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.12308v1) | [PDF](https://arxiv.org/pdf/2608.12308v1.pdf)

<details>
<summary>Abstract</summary>

Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-b...

</details>

---

### [Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation: Diagnosing and Mitigating Initial-Pose Dependence](https://arxiv.org/abs/2608.11769v1)

**Authors:** Chaeyeon Jung, Juyoun Park

**Published:** 2026-08-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11769v1) | [PDF](https://arxiv.org/pdf/2608.11769v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are expected to operate robustly across variations in the robot's initial configuration, yet aggregate task success can conceal pose-specific failures and inappropriate hand selection. This work investigates initial-pose dependence in VLA-based humanoid dual-arm manipulation. We characterize the initial-condition-dependent early hand preference as a policy-induced hand prior and quantify it using HandPriorScore, residual hand bias, and target responsiveness....

</details>

---

### [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739v1)

**Authors:** Yicheng Liu, Zibin Dong, Baijun Ye, Tianyuan Yuan, Tao Jiang et al. (27 authors)

**Published:** 2026-08-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.11739v1) | [PDF](https://arxiv.org/pdf/2608.11739v1.pdf)

<details>
<summary>Abstract</summary>

The prevailing recipe for Vision-Language-Action (VLA) models couples a pretrained VLM with a separately trained flow-matching action expert. This makes the VLM a context encoder rather than a decision-maker. We introduce G0.5, a pretrained autoregressive VLA in which a single transformer decoder emits reasoning and action tokens under a single objective. Three components make this tractable at foundation-model scale: a learnable cross-embodiment action tokenizer that maps heterogeneous robot ac...

</details>

---

### [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671v1)

**Authors:** Siyu Xu, Yunke Wang, Zijian Wang, Dihao Zhu, Chenghao Xia et al. (9 authors)

**Published:** 2026-08-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11671v1) | [PDF](https://arxiv.org/pdf/2608.11671v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can follow instructions and manipulate objects, but their performance often collapses out of distribution (OOD), when the scene, viewpoint, or object differs from training. Adapting to each new situation typically requires collecting more data and fine-tuning. We present StellaVLA, a framework that instead adapts at test time by conditioning on a single retrieved demonstration. The key idea is to move beyond imitating what an expert did and instead convey why:...

</details>

---

### [RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills](https://arxiv.org/abs/2608.12416v1)

**Authors:** Runyi Zhao, Ruixin Wu, Chengkun Li, Hongrui Zhang, Ang Li et al. (18 authors)

**Published:** 2026-08-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.12416v1) | [PDF](https://arxiv.org/pdf/2608.12416v1.pdf)

<details>
<summary>Abstract</summary>

Achieving generalizable robotic manipulation remains a central challenge in embodied intelligence. Despite rapid advances in model architectures and learning algorithms, progress is often limited by the scarcity and narrow diversity of real-world data. The RoboSynChallenge competition introduces a unified benchmark to evaluate and advance the generalizability of manipulation policies across a spectrum of tasks, environments, and difficulty levels. To alleviate the shortage of realistic data, the...

</details>

---
