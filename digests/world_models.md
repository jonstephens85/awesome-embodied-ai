# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-14 17:07 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [ComSim: Building Scalable Real-World Robot Data Generation via Compositional Simulation](https://arxiv.org/abs/2604.11386v1)

**Authors:** Yiran Qin, Jiahua Ma, Li Kang, Wenzhan Li, Yihang Jiao et al. (14 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.11386v1) | [PDF](https://arxiv.org/pdf/2604.11386v1.pdf) | [Project Page](https://faceong.github.io/ComSim/)

<details>
<summary>Abstract</summary>

Recent advancements in foundational models, such as large language models and world models, have greatly enhanced the capabilities of robotics, enabling robots to autonomously perform complex tasks. However, acquiring large-scale, high-quality training data for robotics remains a challenge, as it often requires substantial manual effort and is limited in its coverage of diverse real-world environments. To address this, we propose a novel hybrid approach called Compositional Simulation, which com...

</details>

---

### [WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models](https://arxiv.org/abs/2604.11351v1)

**Authors:** Anlan Yu, Zaishu Chen, Peili Song, Zhiqing Hong, Haotian Wang et al. (9 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.11351v1) | [PDF](https://arxiv.org/pdf/2604.11351v1.pdf) | [GitHub](https://github.com/czs12354-xxdbd/WM-Dagger)

<details>
<summary>Abstract</summary>

Imitation learning is a powerful paradigm for training robotic policies, yet its performance is limited by compounding errors: minor policy inaccuracies could drive robots into unseen out-of-distribution (OOD) states in the training set, where the policy could generate even bigger errors, leading to eventual failures. While the Data Aggregation (DAgger) framework tries to address this issue, its reliance on continuous human involvement severely limits scalability. In this paper, we propose WM-DA...

</details>

---

## Other Recent Papers

### [Grounded World Model for Semantically Generalizable Planning](https://arxiv.org/abs/2604.11751v1)

**Authors:** Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang et al. (7 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.11751v1) | [PDF](https://arxiv.org/pdf/2604.11751v1.pdf)

<details>
<summary>Abstract</summary>

In Model Predictive Control (MPC), world models predict the future outcomes of various action proposals, which are then scored to guide the selection of the optimal action. For visuomotor MPC, the score function is a distance metric between a predicted image and a goal image, measured in the latent space of a pretrained vision encoder like DINO and JEPA. However, it is challenging to obtain the goal image in advance of the task execution, particularly in new environments. Additionally, conveying...

</details>

---

### [Dyadic Partnership(DP): A Missing Link Towards Full Autonomy in Medical Robotics](https://arxiv.org/abs/2604.11423v1)

**Authors:** Nassir Navab, Zhongliang Jiang

**Published:** 2026-04-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.11423v1) | [PDF](https://arxiv.org/pdf/2604.11423v1.pdf)

<details>
<summary>Abstract</summary>

For the past decades medical robotic solutions were mostly based on the concept of tele-manipulation. While their design was extremely intelligent, allowing for better access, improved dexterity, reduced tremor, and improved imaging, their intelligence was limited. They therefore left cognition and decision making to the surgeon. As medical robotics advances towards high-level autonomy, the scientific community needs to explore the required pathway towards partial and full autonomy. Here, we int...

</details>

---

### [3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS](https://arxiv.org/abs/2604.11302v1)

**Authors:** Bronislav Sidik, Dror Mizrahi

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.11302v1) | [PDF](https://arxiv.org/pdf/2604.11302v1.pdf)

<details>
<summary>Abstract</summary>

We present 3D-Anchored Lookahead Planning (3D-ALP), a System 2 reasoning engine for robotic manipulation that combines Monte Carlo Tree Search (MCTS) with a 3D-consistent world model as the rollout oracle. Unlike reactive policies that evaluate actions from the current camera frame only, 3D-ALP maintains a persistent camera-to-world (c2w) anchor that survives occlusion, enabling accurate replanning to object positions that are no longer directly observable. On a 5-step sequential reach task requ...

</details>

---

### [AIM: Intent-Aware Unified world action Modeling with Spatial Value Maps](https://arxiv.org/abs/2604.11135v1)

**Authors:** Liaoyuan Fan, Zetian Xu, Chen Cao, Wenyao Zhang, Mingqi Yuan et al. (6 authors)

**Published:** 2026-04-13 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.11135v1) | [PDF](https://arxiv.org/pdf/2604.11135v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained video generation models provide strong priors for robot control, but existing unified world action models still struggle to decode reliable actions without substantial robot-specific training. We attribute this limitation to a structural mismatch: while video models capture how scenes evolve, action generation requires explicit reasoning about where to interact and the underlying manipulation intent. We introduce AIM, an intent-aware unified world action model that bridges this gap vi...

</details>

---

### [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041v1)

**Authors:** Jia Luo

**Published:** 2026-04-13 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.11041v1) | [PDF](https://arxiv.org/pdf/2604.11041v1.pdf)

<details>
<summary>Abstract</summary>

Semiconductor supply chains face unprecedented resilience challenges amidst global geopolitical turbulence. Conventional Large Language Model (LLM) planners, when confronting such non-stationary "Policy Black Swan" events, frequently suffer from Decision Paralysis or a severe Grounding Gap due to the absence of physical environmental modeling. This paper introduces ReflectiChain, a cognitive agentic framework tailored for resilient macroeconomic supply chain planning. The core innovation lies in...

</details>

---

### [Do LLMs Build Spatial World Models? Evidence from Grid-World Maze Tasks](https://arxiv.org/abs/2604.10690v1)

**Authors:** Weijiang Li, Yilin Zhu, Rajarshi Das, Parijat Dube

**Published:** 2026-04-12 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.10690v1) | [PDF](https://arxiv.org/pdf/2604.10690v1.pdf)

<details>
<summary>Abstract</summary>

Foundation models have shown remarkable performance across diverse tasks, yet their ability to construct internal spatial world models for reasoning and planning remains unclear. We systematically evaluate the spatial understanding of large language models through maze tasks, a controlled testing context requiring multi-step planning and spatial abstraction. Across comprehensive experiments with Gemini-2.5-Flash, GPT-5-mini, Claude-Haiku-4.5, and DeepSeek-Chat, we uncover significant discrepanci...

</details>

---
