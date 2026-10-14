# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-14 19:59 UTC

**Papers shown:** 99 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL](https://arxiv.org/abs/2610.17922)

**Authors:** Shangqing Zhou, Zhennan Jiang, Ning Ma, Xin Fu, Yupeng Zheng et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17922) | [PDF](https://arxiv.org/pdf/2610.17922) | [Project Page](https://youmo445.github.io/WoVR_Plus.github.io/)

<details>
<summary>Abstract</summary>

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization. Extending them to richer VLA interfaces and long-horizon tasks raises challenges in spatiotemporal and cross-modal consistency, exploration-reliability balance in RL, and compounding rollout errors. We present WoVR+, extending WoVR's hallucination-aware WM-RL framework by redesigning the learned environment and imagined interaction protocol: A VLA-interface-aligned world model provides multi-view predi...

</details>

<details>
<summary>Share</summary>

```
WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization.

arXiv: https://arxiv.org/abs/2610.17922
Project page: https://youmo445.github.io/WoVR_Plus.github.io/

#VLA #robotics
```

</details>

---

### [TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency](https://arxiv.org/abs/2610.17540)

**Authors:** Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17540) | [PDF](https://arxiv.org/pdf/2610.17540) | [Project Page](https://tacitvla.github.io)

<details>
<summary>Abstract</summary>

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate...

</details>

<details>
<summary>Share</summary>

```
TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding.

arXiv: https://arxiv.org/abs/2610.17540
Project page: https://tacitvla.github.io

#VLA #robotics
```

</details>

---

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869)

**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang et al. (22 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18869) | [PDF](https://arxiv.org/pdf/2610.18869) | [Project Page](https://axis-bench.github.io/)

<details>
<summary>Abstract</summary>

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain b...

</details>

<details>
<summary>Share</summary>

```
What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning?

arXiv: https://arxiv.org/abs/2610.18869
Project page: https://axis-bench.github.io/

#VLA #robotics
```

</details>

---

### [Interaction Latents as Actions for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18855)

**Authors:** Yuhang Zheng, Yujie Zang, Yuchen Liu, Yupeng Zheng, Zhennan Jiang et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18855) | [PDF](https://arxiv.org/pdf/2610.18855) | [Project Page](https://mrsecant.github.io/ILA/)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction. Yet most robot policies represent actions primarily as motion trajectories, using tactile signals as inputs or auxiliary prediction targets without explicitly encoding contact dynamics in the action representation. We propose ILA (Interaction Latents as Actions), which uses decodable interaction latents that jointly capture the evolution of motion, contact, and force application as policy action units, providing a shared representation for acti...

</details>

<details>
<summary>Share</summary>

```
Interaction Latents as Actions for Contact-Rich Manipulation

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction.

arXiv: https://arxiv.org/abs/2610.18855
Project page: https://mrsecant.github.io/ILA/

#VLA #robotics
```

</details>

---

### [Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation](https://arxiv.org/abs/2610.14415)

**Authors:** Shihan Zhao, Henry Chen, Ya-Chuan Hsu, Minjune Hwang, Siddharth Srikanth et al. (10 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14415) | [PDF](https://arxiv.org/pdf/2610.14415) | [Project Page](https://qd-env.github.io/qdeg/)

<details>
<summary>Abstract</summary>

A long-standing goal in robotics is to develop generalist robots that can perform tasks across a wide range of settings, flexibly specified with images and text. Vision-Language-Action (VLA) models offer a promising path toward this goal by training on large collections of robot demonstrations. However, while VLAs perform well in-distribution, they often fail under minor test-time shifts, such as changes in object positions, lighting, textures, and camera poses. To address this, we propose Quality Diversity for Diverse Environment Generation (Q-DEG), a method for improving VLA robustness by ge...

</details>

<details>
<summary>Share</summary>

```
Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation

A long-standing goal in robotics is to develop generalist robots that can perform tasks across a wide range of settings, flexibly specified with images and text.

arXiv: https://arxiv.org/abs/2610.14415
Project page: https://qd-env.github.io/qdeg/

#VLA #robotics
```

</details>

---

### [Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models](https://arxiv.org/abs/2610.13212)

**Authors:** Min Lin, Bokai Zhou, Jianqi Lin, Kaiyuan Yang, Yicheng Chang et al. (11 authors)

**Published:** 2026-10-09 (updated 2026-10-12) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13212) | [PDF](https://arxiv.org/pdf/2610.13212) | [Project Page](https://afceproject.github.io/AFCE-Web/)

<details>
<summary>Abstract</summary>

Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary prediction target. An offline tokenizer constructs temporally ordered Effect tokens from demonstrated actions, realized robot responses, and sparse visual transitions. Reconstruction objectives encourage the representation to retain executable d...

</details>

<details>
<summary>Share</summary>

```
Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models

Actions specify what a robot should execute, but do not describe what those commands will achieve.

arXiv: https://arxiv.org/abs/2610.13212
Project page: https://afceproject.github.io/AFCE-Web/

#VLA #robotics
```

</details>

---

### [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)

**Authors:** Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12696) | [PDF](https://arxiv.org/pdf/2610.12696) | [Project Page](https://justintiensmith.github.io/Spa-Bench/)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) offer a promising route toward general-purpose robotics by transferring semantic knowledge from large-scale vision-language pretraining into language-conditioned control. However, most VLA evaluations emphasize aggregate manipulation success under changes in objects, instructions, or environments, leaving unclear how reliably these policies ground spatial descriptions in the physical scenes where they act. We therefore ask a sharper question: how reliably can current VLAs translate spatial descriptions into appropriate real-robot behavior? To investigate th...

</details>

<details>
<summary>Share</summary>

```
Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

Vision-language-action models (VLAs) offer a promising route toward general-purpose robotics by transferring semantic knowledge from large-scale vision-language pretraining into language-conditioned control.

arXiv: https://arxiv.org/abs/2610.12696
Project page: https://justintiensmith.github.io/Spa-Bench/

#VLA #robotics
```

</details>

---

### [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526)

**Authors:** Mikey Watts, Yuchen Cui

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CL, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10526) | [PDF](https://arxiv.org/pdf/2610.10526) | [Project Page](https://sttawm.github.io/rephrase-before-you-act)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmentation still shows swings of up to 61 points. We characterize this sensitivity with statistically tested single-edit swings and an oracle phrase search, which shows that phrasing alone nearly closes the...

</details>

<details>
<summary>Share</summary>

```
Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on.

arXiv: https://arxiv.org/abs/2610.10526
Project page: https://sttawm.github.io/rephrase-before-you-act

#VLA #robotics
```

</details>

---

### [Juno: Taming Predictive Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.09940)

**Authors:** Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu

**Published:** 2026-10-07 (updated 2026-10-11) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09940) | [PDF](https://arxiv.org/pdf/2610.09940) | [Project Page](https://juno-policy.github.io/)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predict...

</details>

<details>
<summary>Share</summary>

```
Juno: Taming Predictive Latents for Vision-Language-Action Models

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2610.09940
Project page: https://juno-policy.github.io/

#VLA #robotics
```

</details>

---

### [AUGUstus: Autonomous Driving VLA Model with Unified Generation and Understanding](https://arxiv.org/abs/2610.16985)

**Authors:** Yuqi Ye, Caigao Jiang, Zhuonan Wang, Congyuan Pei, Chao Qu et al. (15 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16985) | [PDF](https://arxiv.org/pdf/2610.16985) | [Project Page](https://augustus-ad.github.io)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models show strong potential for end-to-end autonomous driving by leveraging world knowledge and understanding to excel in long-tail scenarios. However, current VLAs have two limitations: 1) Degeneration into vision-action (VA) models. For low latency, regression/flow-based methods directly generate actions but underuse VLM understanding, causing unsafe, unexplainable actions. 2) Autoregressive high latency. Autoregressive methods sequentially generate chain-of-thought (CoT) and action tokens, fully leveraging VLM understanding, but high latency hinders deployment....

</details>

<details>
<summary>Share</summary>

```
AUGUstus: Autonomous Driving VLA Model with Unified Generation and Understanding

Vision-language-action (VLA) models show strong potential for end-to-end autonomous driving by leveraging world knowledge and understanding to excel in long-tail scenarios.

arXiv: https://arxiv.org/abs/2610.16985
Project page: https://augustus-ad.github.io

#VLA #robotics
```

</details>

---

### [The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover](https://arxiv.org/abs/2610.17746)

**Authors:** Yiqing Xu, Jiajun Wu

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17746) | [PDF](https://arxiv.org/pdf/2610.17746) | [Project Page](https://commgap.github.io/)

<details>
<summary>Abstract</summary>

A robot may know how to perform a task yet fail when a human asks for it naturally. We study this human--VLA communication gap by separating an \emph{information gap}, where task semantics, grounding, or event structure remain unresolved, from a residual \emph{execution gap}, where even a fully specified task depends on how it is organized and invoked. To do this, we characterize how people naturally express demonstrated objectives and evaluate controlled variants of the same physical tasks, with detailed analysis on $π_{0.5}$ and consistent trends on $π_0$-FAST and Cosmos3-Edge. Our study rev...

</details>

<details>
<summary>Share</summary>

```
The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover

A robot may know how to perform a task yet fail when a human asks for it naturally.

arXiv: https://arxiv.org/abs/2610.17746
Project page: https://commgap.github.io/

#VLA #robotics
```

</details>

---

### [Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?](https://arxiv.org/abs/2610.16634)

**Authors:** Zihan You, Zehua Fan, Wenqi Lyu, Aoqi Wang, Ni Wang et al. (22 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16634) | [PDF](https://arxiv.org/pdf/2610.16634)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models increasingly use natural-language instructions to condition autonomous driving behavior. Yet existing closed-loop benchmarks primarily measure route completion, safety, and rule compliance, leaving a fundamental question unresolved: does language actually determine which feasible behavior the vehicle executes? A trajectory may be safe and successful while still violating or even ignoring the passenger's instruction. To address this, we introduce \ltd, a benchmark designed to directly test this capability. Its key evaluation unit, the paired counterfac...

</details>

<details>
<summary>Share</summary>

```
Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?

Recent Vision-Language-Action (VLA) models increasingly use natural-language instructions to condition autonomous driving behavior.

arXiv: https://arxiv.org/abs/2610.16634

#VLA #robotics
```

</details>

---

### [VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2610.16567)

**Authors:** Jun Xiao, Rui Ye, Dong Cao, Jinyu Gu, Ying Wang et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16567) | [PDF](https://arxiv.org/pdf/2610.16567)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable task representation. It combines (1) paired in-distribution and out-of-distribution tasks across six c...

</details>

<details>
<summary>Share</summary>

```
VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models

Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness.

arXiv: https://arxiv.org/abs/2610.16567

#VLA #robotics
```

</details>

---

### [$Δ$ Flow Matching for Robot Foundation Models](https://arxiv.org/abs/2610.15794)

**Authors:** Kuangji Zuo, Tuo An, Xinying Guo, Gen Li, Mengfei Zhao et al. (12 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15794) | [PDF](https://arxiv.org/pdf/2610.15794) | [Project Page](https://zuo-kuangji.github.io/delta-flow/)

<details>
<summary>Abstract</summary>

Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly training and iterative sampling, especially for WAMs with an additional visual branch. We introduce $Δ$-flow, which constructs the source from recent history with mild noise rather than from a fixed Gaussian prior. This moves the source closer t...

</details>

<details>
<summary>Share</summary>

```
$Δ$ Flow Matching for Robot Foundation Models

Flow matching is a common generative recipe for robot foundation models.

arXiv: https://arxiv.org/abs/2610.15794
Project page: https://zuo-kuangji.github.io/delta-flow/

#VLA #robotics
```

</details>

---

### [CoLA: Multi-VLA Coordination via Learned Adapters](https://arxiv.org/abs/2610.15337)

**Authors:** Ahaskar Kashyap, Jiawen Zong, Boyu Ma, Chuhao Zhou, Jingliang Li et al. (7 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.LG, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15337) | [PDF](https://arxiv.org/pdf/2610.15337) | [Code](https://github.com/Ahaskar04/CoLA.git)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies. When several such agents share a workspace, they can coordinate implicitly, by observing one another, or explicitly, by exchanging messages, but it remains unclear when explicit communication becomes necessary. We introduce CoLA (Coordination via Learned Adapters), which keeps each agent's VLA backbone frozen and trains a lightweight message channel and a per-arm diffusion action head on top, with fully decentralised execution. Across three tasks that differ in how much each agent can observe, the cha...

</details>

<details>
<summary>Share</summary>

```
CoLA: Multi-VLA Coordination via Learned Adapters

Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies.

arXiv: https://arxiv.org/abs/2610.15337
Code: https://github.com/Ahaskar04/CoLA.git

#VLA #robotics
```

</details>

---

### [Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945)

**Authors:** Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13945) | [PDF](https://arxiv.org/pdf/2610.13945) | [Project Page](https://splat2act.github.io)

<details>
<summary>Abstract</summary>

A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects...

</details>

<details>
<summary>Share</summary>

```
Splat2Act: From Captured Scenes to Personalized VLA Manipulation

A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables.

arXiv: https://arxiv.org/abs/2610.13945
Project page: https://splat2act.github.io

#VLA #robotics
```

</details>

---

### [JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation](https://arxiv.org/abs/2610.13628)

**Authors:** Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov, Dzmitry Tsetserukou

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.HC, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13628) | [PDF](https://arxiv.org/pdf/2610.13628) | [Project Page](https://faithogunwoye.github.io/JitterVLA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isolating the controller's effect. We apply it to synthetic reaches, hand trajectories from 20 people, three open VLA pipelines (838 episodes) and a physical UR3. Interpolation lowered modeled p99 jerk for every source, by 83% (615 to 106 m/s^3)...

</details>

<details>
<summary>Share</summary>

```
JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation

Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people.

arXiv: https://arxiv.org/abs/2610.13628
Project page: https://faithogunwoye.github.io/JitterVLA/

#VLA #robotics
```

</details>

---

### [VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation](https://arxiv.org/abs/2610.12451)

**Authors:** Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12451) | [PDF](https://arxiv.org/pdf/2610.12451) | [Project Page](https://boyaohan.github.io/VersaCamVLA.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-A...

</details>

<details>
<summary>Share</summary>

```
VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pos...

arXiv: https://arxiv.org/abs/2610.12451
Project page: https://boyaohan.github.io/VersaCamVLA.github.io/

#VLA #robotics
```

</details>

---

### [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models](https://arxiv.org/abs/2610.12007)

**Authors:** Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren et al. (11 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12007) | [PDF](https://arxiv.org/pdf/2610.12007) | [Project Page](https://react-vla.github.io)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon...

</details>

<details>
<summary>Share</summary>

```
REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, wherea...

arXiv: https://arxiv.org/abs/2610.12007
Project page: https://react-vla.github.io

#VLA #robotics
```

</details>

---

### [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](https://arxiv.org/abs/2610.09718)

**Authors:** Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu, Hanlong Li, Tatsuya Matsushima et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09718) | [PDF](https://arxiv.org/pdf/2610.09718) | [Project Page](https://yubi-stag.airoa.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grounding that automatically enriches manipulation demonstrations with interaction-rich semantics to ali...

</details>

<details>
<summary>Share</summary>

```
YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions.

arXiv: https://arxiv.org/abs/2610.09718
Project page: https://yubi-stag.airoa.io/

#VLA #robotics
```

</details>

---

### [TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks](https://arxiv.org/abs/2610.09462)

**Authors:** Zirun Zhou, Jingfeng Zhang, HaoChuan Xu, Xizhe Zhang, Elliott Wen et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09462) | [PDF](https://arxiv.org/pdf/2610.09462) | [Project Page](https://zzr42.github.io/tmt/)

<details>
<summary>Abstract</summary>

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears. Detecting such activation is difficult because malicious behavior can comprise individually plausible actions, while unfamiliar tasks introduce legitimate changes in observations and behavior. We introduce TMT, a runtime backdoor detector based on Token Manifold and latent Transition modeling. Trained on benign rollouts, its two branches assess input-token structure and prediction errors in adjacent-layer latent dynamics. A suspicious rollout identifie...

</details>

<details>
<summary>Share</summary>

```
TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears.

arXiv: https://arxiv.org/abs/2610.09462
Project page: https://zzr42.github.io/tmt/

#VLA #robotics
```

</details>

---

### [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09451)

**Authors:** Yeonseo Lee, Hyosup Shin, Guebin Hwang, Sungho Jo

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09451) | [PDF](https://arxiv.org/pdf/2610.09451) | [Project Page](https://lysees.github.io/tempobridge-page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextual VLM representations, aligns them with task progress through a causal phase router, and modulates n...

</details>

<details>
<summary>Share</summary>

```
TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly.

arXiv: https://arxiv.org/abs/2610.09451
Project page: https://lysees.github.io/tempobridge-page/

#VLA #robotics
```

</details>

---

### [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](https://arxiv.org/abs/2610.10390)

**Authors:** Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10390) | [PDF](https://arxiv.org/pdf/2610.10390) | [Code](https://github.com/TabGuigui/GeoCoTDrive)

<details>
<summary>Abstract</summary>

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critic...

</details>

<details>
<summary>Share</summary>

```
Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving.

arXiv: https://arxiv.org/abs/2610.10390
Code: https://github.com/TabGuigui/GeoCoTDrive

#VLA #robotics
```

</details>

---

### [ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures](https://arxiv.org/abs/2610.18650)

**Authors:** Chenru Wen, Huajian Zeng, Haokai Ding, Jian Kang, Anqing Duan et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18650) | [PDF](https://arxiv.org/pdf/2610.18650)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution. Recovery is typically learned during policy training or delegated to a monitor that triggers a scripted repair after detecting a failure. We introduce ForkCast, a predictive recovery framework that compares counterfactual futures to determine whether and how to intervene in a frozen VLA policy. At each decision point, ForkCast evaluates three candidates: executing the policy's nominal action chunk (Commit), adjusting the came...

</details>

<details>
<summary>Share</summary>

```
ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution.

arXiv: https://arxiv.org/abs/2610.18650

#VLA #robotics
```

</details>

---

### [ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models](https://arxiv.org/abs/2610.18596)

**Authors:** Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18596) | [PDF](https://arxiv.org/pdf/2610.18596) | [Project Page](https://accrue-rl.github.io)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency without addressing learner persistence across tasks. We propose ACCRUE, a continual off-policy RL framework that carries lightweight actor and critic networks across tasks, allowin...

</details>

<details>
<summary>Share</summary>

```
ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired...

arXiv: https://arxiv.org/abs/2610.18596
Project page: https://accrue-rl.github.io

#VLA #robotics
```

</details>

---

### [WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568)

**Authors:** Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18568) | [PDF](https://arxiv.org/pdf/2610.18568)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly large-scale video pretraining. We introduce WAVE-0 (World-model-Augmented VLA Execution), a framework that bridges VLAs and WAMs through a lightweight latent world model. By connectin...

</details>

<details>
<summary>Share</summary>

```
WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences.

arXiv: https://arxiv.org/abs/2610.18568

#VLA #robotics
```

</details>

---

### [YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation](https://arxiv.org/abs/2610.17521)

**Authors:** Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17521) | [PDF](https://arxiv.org/pdf/2610.17521) | [Project Page](https://yubi-real2sim.airoa.io)

<details>
<summary>Abstract</summary>

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation. While 3D Gaussian Splatting (3DGS) enables rapid real-to-sim scene generation, the reconstruction quality required for reliable policy evaluation remains unquantified. In particular, policies relying on wrist-mounted fisheye cameras (e.g., YUBI handheld gripper data) are heavily exposed to visual artifacts (holes, floaters) in wide-angle views, directly degrading task performance. To address this, we present YUBI-Real2Sim, a unified fram...

</details>

<details>
<summary>Share</summary>

```
YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation.

arXiv: https://arxiv.org/abs/2610.17521
Project page: https://yubi-real2sim.airoa.io

#VLA #robotics
```

</details>

---

### [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843)

**Authors:** Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang et al. (9 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18843) | [PDF](https://arxiv.org/pdf/2610.18843)

<details>
<summary>Abstract</summary>

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height, and gripper pads. Each axis has five severity lev...

</details>

<details>
<summary>Share</summary>

```
LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-eff...

arXiv: https://arxiv.org/abs/2610.18843

#VLA #robotics
```

</details>

---

### [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)

**Authors:** Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18774) | [PDF](https://arxiv.org/pdf/2610.18774) | [Project Page](https://greenvla.github.io/GreenWAM)

<details>
<summary>Abstract</summary>

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that describes 20 robot families, from bimanual arms to dexterous humanoids, in common joint coordinates; (...

</details>

<details>
<summary>Share</summary>

```
GreenWAM: A World Foundation Model for Robotics

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.

arXiv: https://arxiv.org/abs/2610.18774
Project page: https://greenvla.github.io/GreenWAM

#VLA #robotics
```

</details>

---

### [Trust-Calibrated VLA Policy Post-Training with Evolving Imagination](https://arxiv.org/abs/2610.16517)

**Authors:** Wenzhan Li, Yiran Qin, Heng Zhou, Huirui Wang, Yulan Guo et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.16517) | [PDF](https://arxiv.org/pdf/2610.16517)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage. Existing refinement paradigms expose a reliability--efficiency tension: model-free refinement avoids simulator bias but is interaction-intensive, whereas model-based refinement can exploit unreliable imagination even as its simulator adapts. We propose Model-Evolving Reinforcement Learning (MERL), a trust-calibrated framework that couples policy optimization with an online-updated simulator comprising a...

</details>

<details>
<summary>Share</summary>

```
Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage.

arXiv: https://arxiv.org/abs/2610.16517

#VLA #robotics
```

</details>

---

### [Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks](https://arxiv.org/abs/2610.16238)

**Authors:** Zhi Han, Zihan Guo, Chenxi Zeng, Zicai Cui, Yue Xin et al. (9 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16238) | [PDF](https://arxiv.org/pdf/2610.16238) | [Code](https://github.com/HanZhi306/EmbodiedSkill-Bench)

<details>
<summary>Abstract</summary>

LLM agents increasingly control robots using VLA policies, perception models, and procedural knowledge. These modules are difficult to reuse because their interfaces, embodiment assumptions, and conditions of use differ, and their benefits on physical tasks remain unclear. We package them as embodied skills that extend agent skills with explicit embodiment assumptions and conditions of use, building 250 action, perception, and experience skills from 1,052 resources. On this basis we introduce EmbodiedSkillBench, which runs an agent in a closed observation-action loop and records success, actio...

</details>

<details>
<summary>Share</summary>

```
Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks

LLM agents increasingly control robots using VLA policies, perception models, and procedural knowledge.

arXiv: https://arxiv.org/abs/2610.16238
Code: https://github.com/HanZhi306/EmbodiedSkill-Bench

#VLA #robotics
```

</details>

---

### [Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors](https://arxiv.org/abs/2610.15556)

**Authors:** Yeonseok Lee

**Published:** 2026-10-11 | **Categories:** cs.LO, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15556) | [PDF](https://arxiv.org/pdf/2610.15556) | [Code](https://github.com/ylee-sling/Vision-Predictor-Action)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency. We present Goal-Conditioned Vision-Predictor-Action (VPA), which replaces autoregressive decoders with a lightweight latent control loop. A shared vision encoder and a frozen text encoder embed observations, goal images, and instructions; a neuro-symbolic selector chooses a discrete skill; a Joint-Embedding Predictive Architecture (JEPA) predictor forecasts the ne...

</details>

<details>
<summary>Share</summary>

```
Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop co...

arXiv: https://arxiv.org/abs/2610.15556
Code: https://github.com/ylee-sling/Vision-Predictor-Action

#VLA #robotics
```

</details>

---

### [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425)

**Authors:** Xupeng Zhang, Yantai Yang, Chang Guo, Zhaokai Yin, Zhipeng Zhang

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15425) | [PDF](https://arxiv.org/pdf/2610.15425) | [Code](https://github.com/AutoLab-SAI-SJTU/RoboCombine)

<details>
<summary>Abstract</summary>

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination. The full instruction route treats skill chaining as long-horizon imitation. In a controlled study, full instruction training on limited skill combination sequences reaches 40.0% ordered success on covered combinations but only 7.7% on recombination, suggesting memorization of sequence templates rather than robust skill recombination. We introduce Hierarchical Subtask Execution (HSE), a diagno...

</details>

<details>
<summary>Share</summary>

```
Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination.

arXiv: https://arxiv.org/abs/2610.15425
Code: https://github.com/AutoLab-SAI-SJTU/RoboCombine

#VLA #robotics
```

</details>

---

### [Verify, Act, Distill: Turning Test-Time Compute into Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.14885)

**Authors:** Kaneyoshi Hiratsuka, Satoshi Yamamori, Jun Morimoto

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14885) | [PDF](https://arxiv.org/pdf/2610.14885)

<details>
<summary>Abstract</summary>

Test-time compute (TTC), which scores multiple candidate actions at inference time, is a powerful way to improve the execution performance of vision-language-action (VLA) models, but existing methods keep the policy frozen, so the gain must be recomputed at every execution. We propose Verify, Act, Distill, a framework that consolidates the gains of TTC into the VLA itself. A fixed verifier scores candidates generated by a flow-matching VLA, the weighted aggregate is executed, and the observations and aggregated chunks from successful adaptation episodes are distilled directly into LoRA paramet...

</details>

<details>
<summary>Share</summary>

```
Verify, Act, Distill: Turning Test-Time Compute into Test-Time Adaptation for Vision-Language-Action Models

Test-time compute (TTC), which scores multiple candidate actions at inference time, is a powerful way to improve the execution performance of vision-language-action (VLA) models, but existing methods keep the policy f...

arXiv: https://arxiv.org/abs/2610.14885

#VLA #robotics
```

</details>

---

### [Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies](https://arxiv.org/abs/2610.14588)

**Authors:** Chen Zhao, Zipeng Ye, Haitao Shen, Guanlin Li, Yuchen Xie et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14588) | [PDF](https://arxiv.org/pdf/2610.14588)

<details>
<summary>Abstract</summary>

Test-time sampling promises to turn one action prediction into a set of distinct executable candidates that a verifier can choose among. Downstream fine-tuning works against that promise. A vision-language-action model trained to solve one task distribution concentrates its flow-matching decoder around the dominant demonstrated action, so repeated samples differ only marginally and the verifier receives many copies of one decision. We call this proposal contraction and identify it as a key constraint on test-time scaling: repeated samples can remain highly redundant as the candidate budget gro...

</details>

<details>
<summary>Share</summary>

```
Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies

Test-time sampling promises to turn one action prediction into a set of distinct executable candidates that a verifier can choose among.

arXiv: https://arxiv.org/abs/2610.14588

#VLA #robotics
```

</details>

---

### [CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance](https://arxiv.org/abs/2610.14936)

**Authors:** Shutong Ding, Zhaoyang Liu, Yimiao Zhou, Jingya Wang, Jiayuan Gu et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14936) | [PDF](https://arxiv.org/pdf/2610.14936) | [Project Page](https://zhy-liu.github.io/cfg-policy-page)

<details>
<summary>Abstract</summary>

Diffusion policies are increasingly used in robotic control and manipulation, vision-language-action models, and world-model-based agents. Their ability to represent multimodal action distributions offers rich opportunities for exploration in reinforcement learning (RL). However, optimizing diffusion policies with RL can reduce the behavioral diversity and further limit their exploration capability. In RL post-training, directly fine-tuning a pretrained policy may also disrupt its acquired capabilities, while action-space residuals may lack the expressive power for multimodal exploration. Toge...

</details>

<details>
<summary>Share</summary>

```
CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance

Diffusion policies are increasingly used in robotic control and manipulation, vision-language-action models, and world-model-based agents.

arXiv: https://arxiv.org/abs/2610.14936
Project page: https://zhy-liu.github.io/cfg-policy-page

#VLA #robotics
```

</details>

---

### [Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies](https://arxiv.org/abs/2610.14406)

**Authors:** Yilin Wu, Rutav Shah, Shuaiyi Huang, Sumedh A. Sontakke, Homanga Bharadhwaj et al. (8 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14406) | [PDF](https://arxiv.org/pdf/2610.14406) | [Project Page](https://yilin-wu98.github.io/imprint_website/)

<details>
<summary>Abstract</summary>

It is widely appreciated that robotic policies require long-term memory to perform complex tasks. However, directly conditioning policies on all past observations leaves policy learning susceptible to learning spurious shortcuts, and introduces large latency at policy deployment. As such, today's memory-augmented policies curate what to remember, either by retaining only recent frames, selected keyframes, or textual summaries, or by learning latent representations of the visual stream alone. In this work, we propose an alternative approach IMPRINT, a policy-agnostic latent memory framework tha...

</details>

<details>
<summary>Share</summary>

```
Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies

It is widely appreciated that robotic policies require long-term memory to perform complex tasks.

arXiv: https://arxiv.org/abs/2610.14406
Project page: https://yilin-wu98.github.io/imprint_website/

#VLA #robotics
```

</details>

---

### [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation](https://arxiv.org/abs/2610.13578)

**Authors:** Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13578) | [PDF](https://arxiv.org/pdf/2610.13578) | [Project Page](https://shua-kang.github.io/RARA_robot/)

<details>
<summary>Abstract</summary>

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves...

</details>

<details>
<summary>Share</summary>

```
RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging.

arXiv: https://arxiv.org/abs/2610.13578
Project page: https://shua-kang.github.io/RARA_robot/

#VLA #robotics
```

</details>

---

### [Forward Dynamics Models](https://arxiv.org/abs/2610.13117)

**Authors:** Zipei Ma, Junzhe Jiang, Jiahui Zhang, Juntong Zhang, Chun Gu et al. (9 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13117) | [PDF](https://arxiv.org/pdf/2610.13117) | [Project Page](https://logosroboticsgroup.github.io/FDM/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively. Yet VLAs learn without explicit supervision from future world states, while WAMs that condition actions on predicted futures incur extra inference cost and let visual prediction errors propagate into actions. We present Forward Dynamics Models (FDM), a family of robotic action models that couples action and future world-state prediction through an action-to-future paradigm. Future predi...

</details>

<details>
<summary>Share</summary>

```
Forward Dynamics Models

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively.

arXiv: https://arxiv.org/abs/2610.13117
Project page: https://logosroboticsgroup.github.io/FDM/

#VLA #robotics
```

</details>

---

### [Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision](https://arxiv.org/abs/2610.12936)

**Authors:** Zile Zhong, Yuxin Du, Tao Lin, Haoxiao Wang, Wei Dai et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12936) | [PDF](https://arxiv.org/pdf/2610.12936)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide additional information for control. Action supervision alone does not explicitly encourage such anticipation, while future-image prediction entangles task-relevant motion with largely static appearance. To address these limitations, we introduce Evo-World, a lightweight VLA model that augments policy learning with future motion prediction through optical-flow supervision, thereby pr...

</details>

<details>
<summary>Share</summary>

```
Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision

Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide ad...

arXiv: https://arxiv.org/abs/2610.12936

#VLA #robotics
```

</details>

---

### [Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies](https://arxiv.org/abs/2610.12861)

**Authors:** Weiwei Chen, Chenghao Xu, Meiling Yu, Xu Yang, Cheng Deng

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12861) | [PDF](https://arxiv.org/pdf/2610.12861) | [Project Page](https://krlozhilderman287-creator.github.io/EVIDENCE-GUIDED-COUNTERFACTUAL-LEARNING-FOR-LONG-TAILED-ROBOTIC-POLICIES/)

<details>
<summary>Abstract</summary>

In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets. To investigate this issue, we study the head-task action bias in shared robot policies, particularly focusing on its relationship with task-specific visual evidence. Our experimental analysis shows that, when the visual evidence required by a tail task is insufficient, the policy increasingly falls back on action patterns reinforced by data-rich head tasks, resulting in degraded performance on u...

</details>

<details>
<summary>Share</summary>

```
Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies

In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets.

arXiv: https://arxiv.org/abs/2610.12861
Project page: https://krlozhilderman287-creator.github.io/EVIDENCE-GUIDED-COUNTERFACTUAL-LEARNING-FOR-LONG-TAILED-ROBOTIC-POLICIES/

#VLA #robotics
```

</details>

---

### [VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding](https://arxiv.org/abs/2610.12832)

**Authors:** Jingkun Yi, Shujie Zhang, Zirui Zhou, Haoxiao Wang, Haiyang Sun et al. (11 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12832) | [PDF](https://arxiv.org/pdf/2610.12832) | [Project Page](https://general-robo.github.io/EASG/)

<details>
<summary>Abstract</summary>

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation. The key challenge in turning pretrained VLMs into generalist manipulation policies is to expose these capabilities through an appropriate action interface. Vision-language-action (VLA) models provide a unified trainable policy, but typically introduce learned action tokens, action heads, or action experts whose semantics must be learned from robot data pretraining. In contrast, modular foundation-model-based manipulation methods can exploit pretrained VLM...

</details>

<details>
<summary>Share</summary>

```
VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation.

arXiv: https://arxiv.org/abs/2610.12832
Project page: https://general-robo.github.io/EASG/

#VLA #robotics
```

</details>

---

### [StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras](https://arxiv.org/abs/2610.12734)

**Authors:** Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12734) | [PDF](https://arxiv.org/pdf/2610.12734) | [Project Page](https://stereoengine.github.io)

<details>
<summary>Abstract</summary>

Stereo vision is increasingly used for robotic manipulation, with a growing body of work incorporating it into Vision-Language-Action (VLA) models. However, the scarcity of large-scale, real-world stereo datasets remains a fundamental bottleneck for scaling such policies. Recent generative monocular-to-stereo methods target settings such as VR content and autonomous driving. No prior work produces realistic synthetic stereo data for robotic manipulation, where stereo supervision has come predominantly from simulation. We propose StereoEngine, which introduces two complementary methods to synth...

</details>

<details>
<summary>Share</summary>

```
StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras

Stereo vision is increasingly used for robotic manipulation, with a growing body of work incorporating it into Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2610.12734
Project page: https://stereoengine.github.io

#VLA #robotics
```

</details>

---

### [CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding](https://arxiv.org/abs/2610.11971)

**Authors:** Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11971) | [PDF](https://arxiv.org/pdf/2610.11971) | [Project Page](https://capable-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that mot...

</details>

<details>
<summary>Share</summary>

```
CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed.

arXiv: https://arxiv.org/abs/2610.11971
Project page: https://capable-vla.github.io/

#VLA #robotics
```

</details>

---

### [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models](https://arxiv.org/abs/2610.11508)

**Authors:** Junmyeong Lee, Dongmin Shin, Min-Gyu Park, Wooseok Jeon, Inho Chang et al. (6 authors)

**Published:** 2026-10-08 (updated 2026-10-13) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.11508) | [PDF](https://arxiv.org/pdf/2610.11508)

<details>
<summary>Abstract</summary>

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration. The problem becomes more evident in cross-setup deployment, as reproducing the exact camera pose used for training is nearly impossible. Unlike fixed external views, wrist views are more challenging because the camera moves with the robot, causing even small mounting variations to alter fine-grained geometric cues. To address this, we propose WARP-VLA, a camera-view robust VLA for diverse wrist camera configurations. WARP-VLA adopts a...

</details>

<details>
<summary>Share</summary>

```
WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration.

arXiv: https://arxiv.org/abs/2610.11508

#VLA #robotics
```

</details>

---

### [SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation](https://arxiv.org/abs/2610.11248)

**Authors:** Kyoungin Baik, Youngwoon Lee

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11248) | [PDF](https://arxiv.org/pdf/2610.11248) | [Project Page](https://kyounginbaik.github.io/simvla/)

<details>
<summary>Abstract</summary>

Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework that trains VLAs entirely on synthetic simulation data without teleoperation for mobile manipulation. SimVLA is first pre-trained on two complementary simulation-derived datasets: SimAction, a large-scale robot action dataset spanning 35 diver...

</details>

<details>
<summary>Share</summary>

```
SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation

Large-scale, diverse datasets have driven the success of LLMs and VLMs.

arXiv: https://arxiv.org/abs/2610.11248
Project page: https://kyounginbaik.github.io/simvla/

#VLA #robotics
```

</details>

---

### [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](https://arxiv.org/abs/2610.10178)

**Authors:** Theodor Wulff, Angelo Cangelosi

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.10178) | [PDF](https://arxiv.org/pdf/2610.10178)

<details>
<summary>Abstract</summary>

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their Vision-Language model backbones. For this reason, we conduct a controlled mechanistic interpretabil...

</details>

<details>
<summary>Share</summary>

```
Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they...

arXiv: https://arxiv.org/abs/2610.10178

#VLA #robotics
```

</details>

---

### [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](https://arxiv.org/abs/2610.09496)

**Authors:** Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09496) | [PDF](https://arxiv.org/pdf/2610.09496)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened attention to task-relevant visual regions, and a mechanistic interpretation via sparse autoencoders...

</details>

<details>
<summary>Share</summary>

```
Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models.

arXiv: https://arxiv.org/abs/2610.09496

#VLA #robotics
```

</details>

---

### [OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models](https://arxiv.org/abs/2610.12914)

**Authors:** Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12914) | [PDF](https://arxiv.org/pdf/2610.12914)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optim...

</details>

<details>
<summary>Share</summary>

```
OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations.

arXiv: https://arxiv.org/abs/2610.12914

#VLA #robotics
```

</details>

---

### [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](https://arxiv.org/abs/2610.12090)

**Authors:** Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12090) | [PDF](https://arxiv.org/pdf/2610.12090)

<details>
<summary>Abstract</summary>

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and...

</details>

<details>
<summary>Share</summary>

```
Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions.

arXiv: https://arxiv.org/abs/2610.12090

#VLA #robotics
```

</details>

---

### [ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874)

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18874) | [PDF](https://arxiv.org/pdf/2610.18874)

<details>
<summary>Abstract</summary>

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present Chunk...

</details>

<details>
<summary>Share</summary>

```
ChunkAct: Action Chunking for Agentic Robotics

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes...

arXiv: https://arxiv.org/abs/2610.18874

#VLA #robotics
```

</details>

---

### [EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence](https://arxiv.org/abs/2610.18867)

**Authors:** Wenyi Li, Yizhe Chi, Youjie Zheng, Chunyu Liu, Xiaoqiu Wang et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18867) | [PDF](https://arxiv.org/pdf/2610.18867)

<details>
<summary>Abstract</summary>

Bringing general-purpose agents into the physical world calls for an executable representation of physical intelligence. Compared with vision-language-action (VLA) models, which map observations and language instructions directly to actions, code makes control logic explicit and reusable. Code can serve not only as a policy representation but also as the workspace in which the agent solves a task. Rather than following a prescribed workflow of planning, execution, and verification, the agent can autonomously inspect the state, revise and execute code, and use feedback to choose the next step....

</details>

<details>
<summary>Share</summary>

```
EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence

Bringing general-purpose agents into the physical world calls for an executable representation of physical intelligence.

arXiv: https://arxiv.org/abs/2610.18867

#VLA #robotics
```

</details>

---

### [EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning](https://arxiv.org/abs/2610.18790)

**Authors:** Haodong Yang, Runhan Huang, Bowen Zhang, Iofai Lei, Zunzhe Zhang et al. (10 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18790) | [PDF](https://arxiv.org/pdf/2610.18790)

<details>
<summary>Abstract</summary>

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve. We introduce Equilibrium Energy Control (EqC), a framework for introspective lifelong robot learning built around an explicit conditional energy landscape. EqC casts generative action refinement as equilibrium-seeking optimization, while the geometry of the refinement process reveals whether the generated behavior remains consistent with the learned landscape. This competence signal enables Energy-Gated DAgger, w...

</details>

<details>
<summary>Share</summary>

```
EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve.

arXiv: https://arxiv.org/abs/2610.18790

#VLA #robotics
```

</details>

---

### [Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments](https://arxiv.org/abs/2610.18381)

**Authors:** Zhibo Duan, Hanlin Kong, Tianran Ma, Yuze Wu, Yuxuan Xu et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18381) | [PDF](https://arxiv.org/pdf/2610.18381)

<details>
<summary>Abstract</summary>

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the same trajectories. Existing aerial benchmarks are typically confined to single-environment settings, limiting evaluation of agents across continuous environmental transitions. When interaction is evaluated, agents are often initialized near the target, leaving the transition from navigation to interaction largely unassessed. This work introduces CrossFly, a benchmark for long-horizon...

</details>

<details>
<summary>Share</summary>

```
Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the sam...

arXiv: https://arxiv.org/abs/2610.18381

#VLA #robotics
```

</details>

---

### [DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations](https://arxiv.org/abs/2610.18373)

**Authors:** Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18373) | [PDF](https://arxiv.org/pdf/2610.18373)

<details>
<summary>Abstract</summary>

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-invariant scene representation (DISR). The framework combines vision-language understanding and laten...

</details>

<details>
<summary>Share</summary>

```
DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways.

arXiv: https://arxiv.org/abs/2610.18373

#VLA #robotics
```

</details>

---

### [Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance](https://arxiv.org/abs/2610.17983)

**Authors:** Mohammed Daba, Waleed Abdulrahman Saleh AlAkwa

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17983) | [PDF](https://arxiv.org/pdf/2610.17983)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets. However, these models frequently suffer from distributional convergence, a phenomenon where the policy regresses to "safe" but suboptimal mean behaviors due to mode averaging in the training data. This often results in generic grasp strategies, Convergent Defaults, that fail in constrained or long-tail scenarios. In this work, we propose a novel framework to identify and correct these behaviors without parameter updates. We...

</details>

<details>
<summary>Share</summary>

```
Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets.

arXiv: https://arxiv.org/abs/2610.17983

#VLA #robotics
```

</details>

---

### [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792)

**Authors:** Xinyi Wang, Bangzheng Li, Hanyu Wang, Lin Zhang, Andrea Yaoyun Cui et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18792) | [PDF](https://arxiv.org/pdf/2610.18792)

<details>
<summary>Abstract</summary>

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fin...

</details>

<details>
<summary>Share</summary>

```
SEAR: Self-Evolving Agentic Robotics

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task.

arXiv: https://arxiv.org/abs/2610.18792

#VLA #robotics
```

</details>

---

### [UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation](https://arxiv.org/abs/2610.16969)

**Authors:** Lei Yao, Qiao Feng, Mutian Tong, Qihao Yun, Lap-Pui Chau et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16969) | [PDF](https://arxiv.org/pdf/2610.16969)

<details>
<summary>Abstract</summary>

Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action. Recent continuous alternatives mitigate this, but they are typically used as proxies for world modeling and require a further planning step to produce executable actions. We thus introduce UniLAP, a unified continuous latent-action policy that models the latent space via flow matching and bypasses reliance on future frames during inference. By distilling a LAM teacher with a flow-adaptive obje...

</details>

<details>
<summary>Share</summary>

```
UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation

Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action.

arXiv: https://arxiv.org/abs/2610.16969

#VLA #robotics
```

</details>

---

### [Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA](https://arxiv.org/abs/2610.16313)

**Authors:** Jiaqi Fan, Rui Xu, Jiakun Xia, Xuyu Fan, Shuailei Ma et al. (10 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16313) | [PDF](https://arxiv.org/pdf/2610.16313)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation. However, many manipulation tasks depend on auditory cues that cannot be reliably inferred from visual observations and may need to be elicited through physical interaction. To address this gap, we present ListenVLA, an audio-conditioned VLA policy built on GR00T N1.7 for sound-guided manipulation. ListenVLA combines semantic audio embeddings with waveform-derived acoustic cues over a causal audio history and conditions continuous action generati...

</details>

<details>
<summary>Share</summary>

```
Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA

Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation.

arXiv: https://arxiv.org/abs/2610.16313

#VLA #robotics
```

</details>

---

### [FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning](https://arxiv.org/abs/2610.16160)

**Authors:** Junhyeong Go, Mingyu Jung, Woobin Im, Jongbin Ryu

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16160) | [PDF](https://arxiv.org/pdf/2610.16160)

<details>
<summary>Abstract</summary>

Recent advances in 3D reconstruction enable the extraction of temporally consistent 3D motion from RGB observations; however, current Vision-Language-Action (VLA) models still predominantly rely on 2D image-text priors. Therefore, they do not accurately represent the fundamental dynamics of the 3D world associated with physical actions. This over-reliance on static 2D visual cues limits the capacity of VLA models in achieving robust robot manipulation. To address these limitations, we introduce FlowVLA, a reconstruction-guided, pluggable 3D flow learning framework aimed at empowering VLA model...

</details>

<details>
<summary>Share</summary>

```
FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning

Recent advances in 3D reconstruction enable the extraction of temporally consistent 3D motion from RGB observations; however, current Vision-Language-Action (VLA) models still predominantly rely on 2D image-text priors.

arXiv: https://arxiv.org/abs/2610.16160

#VLA #robotics
```

</details>

---

### [Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.15675)

**Authors:** Seongmin Park, Jaewon Lee, Yujun Heo, Yoonsik Kim, Seheon Choi et al. (7 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15675) | [PDF](https://arxiv.org/pdf/2610.15675)

<details>
<summary>Abstract</summary>

Quantization lowers deployment costs of vision-language-action (VLA) policies but can compromise task completion. Across five VLA models and 4,050 real-world trials, we systematically reveal that quantization-aware training (QAT) generally improves on post-training quantization (PTQ) but leaves substantial gaps to full precision (FP) on long-horizon tasks and under visual and semantic shifts, while its imitation-based objective does not explicitly use rollout success or partial completion. To exploit these outcome signals, we introduce Quantization-Conditioned Reinforcement Learning (QCRL), an...

</details>

<details>
<summary>Share</summary>

```
Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning

Quantization lowers deployment costs of vision-language-action (VLA) policies but can compromise task completion.

arXiv: https://arxiv.org/abs/2610.15675

#VLA #robotics
```

</details>

---

### [DEFT-VLA: Stage-Localized Force Specialization for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2610.14854)

**Authors:** Zan Huang, Yibo Qiu, Kan Ding, Xuanping Zhang, Ao Tian et al. (7 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14854) | [PDF](https://arxiv.org/pdf/2610.14854)

<details>
<summary>Abstract</summary>

Contact-rich manipulation poses a stage-dependent sensory conflict: vision and proprioception are essential for localization and approach, when force is largely uninformative and potentially distracting, whereas force becomes critical after contact, when irrelevant visual details and correlated robot states may become shortcuts. We propose DEFT-VLA (Dual-Expert Force-specialized Training for Vision-Language-Action Manipulation), which retains the task-adapted base expert for vision-dominated non-contact behavior and introduces a force-aware contact expert for critical contact stages, localizin...

</details>

<details>
<summary>Share</summary>

```
DEFT-VLA: Stage-Localized Force Specialization for Contact-Rich Robotic Manipulation

Contact-rich manipulation poses a stage-dependent sensory conflict: vision and proprioception are essential for localization and approach, when force is largely uninformative and potentially distracting, whereas force...

arXiv: https://arxiv.org/abs/2610.14854

#VLA #robotics
```

</details>

---

### [PRISM: Precision Forcing for Generalist Vision-Language-Action Policies](https://arxiv.org/abs/2610.14704)

**Authors:** Chenghao Yue, Peiyan Li, Hao Wang, Lei Lv, Jiahao Chen et al. (8 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14704) | [PDF](https://arxiv.org/pdf/2610.14704)

<details>
<summary>Abstract</summary>

Coupling a pretrained vision-language model (VLM) with a diffusion or flow-matching action expert has become the mainstream vision-language-action (VLA) paradigm for embodied policies, yet they remain unreliable once a task demands precise manipulation, e.g., submillimeter cable insertion. We attribute this weakness to a training objective that averages flow-matching errors across contexts and flow times, allocating little supervision to the few decisive moments determining task success. Along the generative path, inference integrates a locally supervised velocity field, so equally penalized e...

</details>

<details>
<summary>Share</summary>

```
PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

Coupling a pretrained vision-language model (VLM) with a diffusion or flow-matching action expert has become the mainstream vision-language-action (VLA) paradigm for embodied policies, yet they remain unreliable once...

arXiv: https://arxiv.org/abs/2610.14704

#VLA #robotics
```

</details>

---

### [Noise Space Learning for VLA Adaptation](https://arxiv.org/abs/2610.13943)

**Authors:** Junjie Lu, Chuheng Zhang, Yucen Wang, Yuhua Jiang, Xinyao Qin et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.13943) | [PDF](https://arxiv.org/pdf/2610.13943)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints. Noise space learning (NSL) adapts flow-matching-based VLAs by learning a context-conditioned distribution over noise while keeping the pretrained VLA fixed. Building on prior noise-steering methods, we formulate NSL as an interface for VLA adaptation that accommodates different learning algorithms and instantiate it with PPO, SAC, and AWR. Theoretically, we provide an information-theor...

</details>

<details>
<summary>Share</summary>

```
Noise Space Learning for VLA Adaptation

Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints.

arXiv: https://arxiv.org/abs/2610.13943

#VLA #robotics
```

</details>

---

### [Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies](https://arxiv.org/abs/2610.14155)

**Authors:** Renbin Shu, Jing Yang, Xiangyuan You, Guolin Qiu, Yufei Xia et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14155) | [PDF](https://arxiv.org/pdf/2610.14155)

<details>
<summary>Abstract</summary>

Reliable manipulation requires policies that generalize across tasks, layouts, and object interactions. Vision-language-action (VLA) models combine pretrained multimodal understanding with learned control, but their performance remains limited on unfamiliar task compositions. We present Axiom-0, a VLA policy that addresses both the quality of its representations and their use in action generation through hierarchical self-refinement. Intra-VLM Representation Refinement (IVRR) strengthens selected intermediate features through consistency supervision with learned feature projections during trai...

</details>

<details>
<summary>Share</summary>

```
Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies

Reliable manipulation requires policies that generalize across tasks, layouts, and object interactions.

arXiv: https://arxiv.org/abs/2610.14155

#VLA #robotics
```

</details>

---

### [Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving](https://arxiv.org/abs/2610.13453)

**Authors:** Yuechen Luo, He Chong, Fang Li, Shaoqing Xu, Hexin Zhang et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.13453) | [PDF](https://arxiv.org/pdf/2610.13453)

<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models. However, existing RL methods rely on scalar trajectory rewards that measure overall quality but fail to identify specific planning errors or provide actionable correction signals. In long-tail scenarios, errors in scene understanding, behavior selection, and trajectory execution are compressed into a single score. We observe that Reflective Guidance turns trajectory evaluation into explicit diagnoses and corrective instructions, substantially improving planning acc...

</details>

<details>
<summary>Share</summary>

```
Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving

Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2610.13453

#VLA #robotics
```

</details>

---

### [ARC: A Reasoning Recipe for Robot Foundation Models](https://arxiv.org/abs/2610.12386)

**Authors:** Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12386) | [PDF](https://arxiv.org/pdf/2610.12386) | [Project Page](https://arc-robot-reasoning.github.io/)

<details>
<summary>Abstract</summary>

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces s...

</details>

<details>
<summary>Share</summary>

```
ARC: A Reasoning Recipe for Robot Foundation Models

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale.

arXiv: https://arxiv.org/abs/2610.12386
Project page: https://arc-robot-reasoning.github.io/

#VLA #robotics
```

</details>

---

### [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.12285)

**Authors:** Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen et al. (14 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12285) | [PDF](https://arxiv.org/pdf/2610.12285)

<details>
<summary>Abstract</summary>

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented representation space, reducing the need to predict control-irrelevant visual details. Built on a Mixture-of-Transformers architecture, PLaW-VLA conditions action generation on observation history, current task semantics, and predicted future stat...

</details>

<details>
<summary>Share</summary>

```
PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and...

arXiv: https://arxiv.org/abs/2610.12285

#VLA #robotics
```

</details>

---

### [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](https://arxiv.org/abs/2610.12185)

**Authors:** Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12185) | [PDF](https://arxiv.org/pdf/2610.12185) | [Code](https://github.com/JIA-Lab-research/RESETTLE)

<details>
<summary>Abstract</summary>

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery w...

</details>

<details>
<summary>Share</summary>

```
RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors.

arXiv: https://arxiv.org/abs/2610.12185
Code: https://github.com/JIA-Lab-research/RESETTLE

#VLA #robotics
```

</details>

---

### [Tell Robot What Not to Do: A Negation Understanding Perspective](https://arxiv.org/abs/2610.11952)

**Authors:** Fazeng Li, Gan Sun, Hao Cheng, Weihong Ren, Yang Cong

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.11952) | [PDF](https://arxiv.org/pdf/2610.11952)

<details>
<summary>Abstract</summary>

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-play framework that extends pretrained VLAs to follow negated instructions through image-language super...

</details>

<details>
<summary>Share</summary>

```
Tell Robot What Not to Do: A Negation Understanding Perspective

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction.

arXiv: https://arxiv.org/abs/2610.11952

#VLA #robotics
```

</details>

---

### [PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies](https://arxiv.org/abs/2610.11771)

**Authors:** Qing Huang, Yifei Yang, Ziqing Zou, Anzhe Chen, Zhenjie Zhu et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.11771) | [PDF](https://arxiv.org/pdf/2610.11771)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace. This coupling complicates adaptation from teleoperation: useful geometric guidance comes with timing shaped by interface delays and operator behavior. Our key insight is to bring the path-time parameterization of classical motion planning into the learned action representation of a VLA. We introduce PathTime-VLA, which represents motion as a progress-indexed interaction path $X(s)$ and a positive interval-time profile. The latter defines a monoton...

</details>

<details>
<summary>Share</summary>

```
PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace.

arXiv: https://arxiv.org/abs/2610.11771

#VLA #robotics
```

</details>

---

### [REMM: Revisable Embodied Memory for Manipulation](https://arxiv.org/abs/2610.12710)

**Authors:** Revanth Krishna Senthilkumaran, Ruwan Wickramarachchi, Alessandro Oltramari, Jonathan Francis

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12710) | [PDF](https://arxiv.org/pdf/2610.12710) | [Project Page](https://revanthsenthil.github.io/remm/)

<details>
<summary>Abstract</summary>

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence. Retaining observations alone does not specify which completed conditions should be withdrawn after a disturbance or which obligations require repair. We introduce REMM, Revisable Embodied Memory for Manipulation, a supervisory memory layer for a frozen G0.5 vision-language-action executor. REMM separates an append-only evidence history from revisable task state and explicitly links derived relations and completed conditions to their supporting facts. Wh...

</details>

<details>
<summary>Share</summary>

```
REMM: Revisable Embodied Memory for Manipulation

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence.

arXiv: https://arxiv.org/abs/2610.12710
Project page: https://revanthsenthil.github.io/remm/

#VLA #robotics
```

</details>

---

### [Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning](https://arxiv.org/abs/2610.12231)

**Authors:** Yuchen Zhou, Jiacheng You, Weikang Wan, Weijun Dong, Yang Gao et al. (6 authors)

**Published:** 2026-10-08 (updated 2026-10-09) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12231) | [PDF](https://arxiv.org/pdf/2610.12231) | [Project Page](https://projects.thelabone.org/regression-policy/)

<details>
<summary>Abstract</summary>

Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective of statistical modeling: how action-prediction residuals shape policy optimization. Our analysis of real-world robot demonstration data reveals substantial state-dependent variation in residual scales and heavier-than-Gaussian tails. While bo...

</details>

<details>
<summary>Share</summary>

```
Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning

Learning from demonstration has enabled impressive robot behaviors.

arXiv: https://arxiv.org/abs/2610.12231
Project page: https://projects.thelabone.org/regression-policy/

#VLA #robotics
```

</details>

---

### [When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs](https://arxiv.org/abs/2610.10912)

**Authors:** Jasper Gerigk, Kenzo Aspuru-Takata, Chin-Hsuan Wu, Mohammad Mohammadi, Shuhong Zheng et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.10912) | [PDF](https://arxiv.org/pdf/2610.10912)

<details>
<summary>Abstract</summary>

Shortcut learning is a prevalent issue in robot learning. The limited diversity of robot demonstration datasets can mislead policies into exploiting spurious correlations between tasks and irrelevant features, such as viewpoint or background. Collecting sufficiently diverse robot demonstrations is costly and inefficient, motivating algorithmic alternatives. We focus on vision-language-action (VLA) models and discover that different vision-language model backbones exhibit substantially different levels of susceptibility to visual shortcut learning. We find that model behavior correlates with ou...

</details>

<details>
<summary>Share</summary>

```
When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs

Shortcut learning is a prevalent issue in robot learning.

arXiv: https://arxiv.org/abs/2610.10912

#VLA #robotics
```

</details>

---

### [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787)

**Authors:** Gengze Zhou, Yicong Hong, Jiazhao Zhang, Xunyi Zhao, Jian Zhou et al. (12 authors)

**Published:** 2026-10-07 (updated 2026-10-12) | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10787) | [PDF](https://arxiv.org/pdf/2610.10787) | [Project Page](https://metacognitionai.github.io/NavGPT3/)

<details>
<summary>Abstract</summary>

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control. We present NavGPT-3, a harness that connects the two models, with an OS-like runtime built above it: reasoning, acting, and monitoring run as threads with their own context, tools, and permissions, while the runtime schedules them and deci...

</details>

<details>
<summary>Share</summary>

```
NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied a...

arXiv: https://arxiv.org/abs/2610.10787
Project page: https://metacognitionai.github.io/NavGPT3/

#VLA #robotics
```

</details>

---

### [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework](https://arxiv.org/abs/2610.10384)

**Authors:** Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao et al. (17 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10384) | [PDF](https://arxiv.org/pdf/2610.10384) | [Project Page](https://fvl-repo.github.io/OpenViTac/)

<details>
<summary>Abstract</summary>

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulation and the real world. OpenViTac organizes contact-rich manipulation into four tactile-relevant capab...

</details>

<details>
<summary>Share</summary>

```
OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world.

arXiv: https://arxiv.org/abs/2610.10384
Project page: https://fvl-repo.github.io/OpenViTac/

#VLA #robotics
```

</details>

---

### [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](https://arxiv.org/abs/2610.09943)

**Authors:** Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun et al. (8 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09943) | [PDF](https://arxiv.org/pdf/2610.09943)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternative strategies under distribution shifts. Inspired by this, we introduce DRIVE (Diversity-driven RL fI...

</details>

<details>
<summary>Share</summary>

```
Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited.

arXiv: https://arxiv.org/abs/2610.09943

#VLA #robotics
```

</details>

---

### [LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](https://arxiv.org/abs/2610.16782)

**Authors:** Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang, Boning Tan, Liangna Fu et al. (12 authors)

**Published:** 2026-10-12 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.16782) | [PDF](https://arxiv.org/pdf/2610.16782)

<details>
<summary>Abstract</summary>

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap, we introduce LIBERO-Industry, a novel benchmark built on the widely used robot learning benchmark L...

</details>

<details>
<summary>Share</summary>

```
LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions.

arXiv: https://arxiv.org/abs/2610.16782

#VLA #robotics
```

</details>

---

### [TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments](https://arxiv.org/abs/2610.17999)

**Authors:** Qingyu Lan, Zhihao Tian, Zifan Wang, Junwei Liang

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17999) | [PDF](https://arxiv.org/pdf/2610.17999)

<details>
<summary>Abstract</summary>

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to the target robot.TRACE first injects kinematic priors into input and output projection layers and aligns nominal joint dynamics to reduce embodiment mismatch and support stable fine-tuning. It then combines encoder distillation with low-rank...

</details>

<details>
<summary>Share</summary>

```
TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch.

arXiv: https://arxiv.org/abs/2610.17999

#VLA #robotics
```

</details>

---

### [SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation](https://arxiv.org/abs/2610.15766)

**Authors:** Angen Ye, junjie xie, Yujia Song, Junkai Huang, Dapeng Zhang

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15766) | [PDF](https://arxiv.org/pdf/2610.15766)

<details>
<summary>Abstract</summary>

Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficient precision, opaque decisions, and scarce data. This paper presents SurgiCLAW, a hierarchical skill-based framework for precision surgical manipulation. SurgiCLAW confines an MLLM to intraoperative visual understanding, structured explanation, and atomic surgical-skill selection, while delegating physical execution to...

</details>

<details>
<summary>Share</summary>

```
SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation

Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning.

arXiv: https://arxiv.org/abs/2610.15766

#VLA #robotics
```

</details>

---

### [Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution](https://arxiv.org/abs/2610.14997)

**Authors:** Wenbo Yu, Jifan Li, Wenke Xia, Yuchen Li, Yizhuo Zhang et al. (8 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.14997) | [PDF](https://arxiv.org/pdf/2610.14997)

<details>
<summary>Abstract</summary>

While asynchronous execution enables VLA models to operate in real-time environments by predicting the next chunk during execution, it inevitably introduces boundary misalignment with the committed action stream. Existing delay-aware solutions address this at the prohibitive cost of extensive retraining, architectural modifications, or fixed-prefix inpainting that inflates computation when low latency is vital. To address these problems, we propose FreeBar, a training-free real-time inference plugin that enables robust asynchronous execution with only marginal additional inference cost by cast...

</details>

<details>
<summary>Share</summary>

```
Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution

While asynchronous execution enables VLA models to operate in real-time environments by predicting the next chunk during execution, it inevitably introduces boundary misalignment with the committed action stream.

arXiv: https://arxiv.org/abs/2610.14997

#VLA #robotics
```

</details>

---

### [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/abs/2610.13516)

**Authors:** David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.13516) | [PDF](https://arxiv.org/pdf/2610.13516)

<details>
<summary>Abstract</summary>

Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions. Yet an accurate alarm may arrive too late for recovery, while an unnecessary intervention may disrupt an execution that would otherwise succeed. We introduce RESCUE, a counterfactual framework for evaluating whether a monitor's alarms enable useful interventions. By restoring simulator and policy states at execution checkpoints, RESCUE compares alternative actions, identifies the latest checkpoint satisfying a specified recovery criterion, and evaluates whet...

</details>

<details>
<summary>Share</summary>

```
RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions.

arXiv: https://arxiv.org/abs/2610.13516

#VLA #robotics
```

</details>

---

### [Dual-Stream Memory for Vision-Language-Action Policies](https://arxiv.org/abs/2610.13262)

**Authors:** Yang Wang, Ping Liu, Ruiyu Wang, Xuhua Chen, Lingfeng Zhang et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.13262) | [PDF](https://arxiv.org/pdf/2610.13262)

<details>
<summary>Abstract</summary>

Memory-dependent manipulation requires a policy to track execution state and recover visual evidence that is no longer observable. We propose dual-stream memory for vision-language-action policies, assigning these requirements to complementary representations. A task-agnostic Gated DeltaNet compresses history into one temporal token, supervised by progress prediction and action-conditioned feature reconstruction. A task-conditioned retriever retains frames above a fixed relevance threshold; linear multi-scale fusion encodes each frame into sixteen spatial tokens. We then freeze the temporal co...

</details>

<details>
<summary>Share</summary>

```
Dual-Stream Memory for Vision-Language-Action Policies

Memory-dependent manipulation requires a policy to track execution state and recover visual evidence that is no longer observable.

arXiv: https://arxiv.org/abs/2610.13262

#VLA #robotics
```

</details>

---

### [Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation](https://arxiv.org/abs/2610.12793)

**Authors:** Yudong Liu, Yueqian Lin, Zijia Tang, Yuxi Zheng, Yuan Li et al. (14 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12793) | [PDF](https://arxiv.org/pdf/2610.12793)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key id...

</details>

<details>
<summary>Share</summary>

```
Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation

Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic...

arXiv: https://arxiv.org/abs/2610.12793

#VLA #robotics
```

</details>

---

### [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](https://arxiv.org/abs/2610.12089)

**Authors:** Guoting Wei, Dawei Yan, Xia Yuan, Gengming Zhang, Yelin He et al. (13 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12089) | [PDF](https://arxiv.org/pdf/2610.12089)

<details>
<summary>Abstract</summary>

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction. Learning and evaluating these skills present three challenges: similar observations under a fixed task instruction may make skill selection ambiguous; even when a preceding skill succeeds, the robot state inherited by the next skill may deviate from its demonstrated starting states and affect execution; and task-level metrics hinder skill-specific diagnosis, while early failures leave later skills untested. We therefore...

</details>

<details>
<summary>Share</summary>

```
ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction.

arXiv: https://arxiv.org/abs/2610.12089

#VLA #robotics
```

</details>

---

### [HWAM: Humanoid World Action Model With Joint State--Action Generation](https://arxiv.org/abs/2610.12026)

**Authors:** Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu et al. (10 authors)

**Published:** 2026-10-08 (updated 2026-10-12) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12026) | [PDF](https://arxiv.org/pdf/2610.12026)

<details>
<summary>Abstract</summary>

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robo...

</details>

<details>
<summary>Share</summary>

```
HWAM: Humanoid World Action Model With Joint State--Action Generation

Humanoid robots are a promising platform for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2610.12026

#VLA #robotics
```

</details>

---

### [Experience-Guided Initiation Search for Learned Skills in Skill Composition](https://arxiv.org/abs/2610.11418)

**Authors:** Qixuan Li, Yanhong Zhao, Jincheng Yu

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.11418) | [PDF](https://arxiv.org/pdf/2610.11418)

<details>
<summary>Abstract</summary>

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution. In skill composition, an initiation configuration affects not only the current skill but also the physical state passed to subsequent skills, so successful execution of an individual skill does not necessarily imply successful completion of the composed task. Estimating target-specific capability through extensive rollouts is costly in real-world deployment, while directly reusing historical experience can be unrelia...

</details>

<details>
<summary>Share</summary>

```
Experience-Guided Initiation Search for Learned Skills in Skill Composition

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution.

arXiv: https://arxiv.org/abs/2610.11418

#VLA #robotics
```

</details>

---

### [Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer](https://arxiv.org/abs/2610.11416)

**Authors:** Shuang Luo, Yilun Kong, Yunpeng Qing, Yihang Jiao, Zhi Hou et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.11416) | [PDF](https://arxiv.org/pdf/2610.11416)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs). However, such VLM backbones offer insufficient physical dynamics priors, which limits the generalization capabilities of robot policies. Recent efforts therefore integrate video-generation World Models (WMs) into robot policies through various strategies, using predictive dynamics to facilitate action generation. Despite these advances, harnessing semantic understanding and dynamics prediction as c...

</details>

<details>
<summary>Share</summary>

```
Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer

Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs).

arXiv: https://arxiv.org/abs/2610.11416

#VLA #robotics
```

</details>

---

### [VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving](https://arxiv.org/abs/2610.11161)

**Authors:** Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.11161) | [PDF](https://arxiv.org/pdf/2610.11161)

<details>
<summary>Abstract</summary>

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations. Although recent extensions enable temporal 3D prediction, their future evolution remains weakly conditioned on driving intentions and actions, limiting their ability to model alternative action-dependent futures. We propose VGGTWorld-VLA, an intention-conditioned extension of VGGT-World for controllable 3D world evolution in autonomous driving. First, we introduce an action--semantic conditioning mechanism that injects complementary driving semantics and ego-mot...

</details>

<details>
<summary>Share</summary>

```
VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations.

arXiv: https://arxiv.org/abs/2610.11161

#VLA #robotics
```

</details>

---

### [RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies](https://arxiv.org/abs/2610.09696)

**Authors:** Mimo Shirasaka, Takehiko Ohkawa, Takuya Okubo, Nicola Scianca, Tatsuya Matsushima et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09696) | [PDF](https://arxiv.org/pdf/2610.09696)

<details>
<summary>Abstract</summary>

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands. Vision-Language-Action (VLA) policies trained on such data inherit the demonstrator's timing. Yet human timing does not directly transfer to robots: compliant hands tolerate fast contact, whereas robots may overshoot due to actuator and tracking limitations; conversely, robots can move faster in free space. This motivates a unified approach that reconciles execution speed with contact safety...

</details>

<details>
<summary>Share</summary>

```
RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands.

arXiv: https://arxiv.org/abs/2610.09696

#VLA #robotics
```

</details>

---

### [ADAPT: Audio-Depth Action Planning with Transition-Aware Rewards for Lights-Out Industrial Navigation](https://arxiv.org/abs/2610.15956)

**Authors:** Wenjun Huang, Shenghao Fu, Yian Jin, Yang Ni, Yifan Li et al. (15 authors)

**Published:** 2026-10-11 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15956) | [PDF](https://arxiv.org/pdf/2610.15956)

<details>
<summary>Abstract</summary>

Vision-language-action models for embodied navigation typically rely on RGB observations, limiting their applicability in lights-out industrial environments where visible illumination may be unavailable. We study illumination-independent navigation using spatial audio for target localization and depth for obstacle-aware geometry. To support this setting, we introduce DarkNav-Bench, a benchmark with 24 industrial scenes and four progressively challenging acoustic conditions. We further propose ADAPT, an audio-depth action-planning framework equipped with spatial-audio perception and optimized f...

</details>

<details>
<summary>Share</summary>

```
ADAPT: Audio-Depth Action Planning with Transition-Aware Rewards for Lights-Out Industrial Navigation

Vision-language-action models for embodied navigation typically rely on RGB observations, limiting their applicability in lights-out industrial environments where visible illumination may be unavailable.

arXiv: https://arxiv.org/abs/2610.15956

#VLA #robotics
```

</details>

---

### [A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding](https://arxiv.org/abs/2610.15666)

**Authors:** Abdollah Pourasghari, Saeedeh Sadat Sadidpour, Mohammad Roustaei

**Published:** 2026-10-11 | **Categories:** cs.CV, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.15666) | [PDF](https://arxiv.org/pdf/2610.15666)

<details>
<summary>Abstract</summary>

Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-grounded environments, and largely assume instructions are clear and executable. We introduce the first Persian vision-language-action dataset for this task: 258 instances over 230 real household/office photographs, annotated with reference plans, deliberate ambiguity and infeasibility labels, disambiguating question-answer pairs, and an auto-generated chain-of-thought rationale f...

</details>

<details>
<summary>Share</summary>

```
A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding

Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-...

arXiv: https://arxiv.org/abs/2610.15666

#VLA #robotics
```

</details>

---

### [YOUDrive: Driving Style as a Composable Direction for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.14802)

**Authors:** Guantian Zheng, Lidong Yu, Tianyu Gao, Jiaxing Chen, Jiashu Li et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14802) | [PDF](https://arxiv.org/pdf/2610.14802)

<details>
<summary>Abstract</summary>

End-to-end driving policies can achieve strong task performance while offering limited control over their driving style. Driving style describes how a vehicle accelerates, brakes, and maintains distance. Policies trained without explicit preference conditioning lack a direct mechanism for adjusting these behaviors at inference. We propose YOUDrive, a vision--language--action planner for continuous and composable driving-style control. Each teacher's behavior is distilled into a task vector, a learned parameter update that induces a style direction in the planner's representation. These directi...

</details>

<details>
<summary>Share</summary>

```
YOUDrive: Driving Style as a Composable Direction for End-to-End Autonomous Driving

End-to-end driving policies can achieve strong task performance while offering limited control over their driving style.

arXiv: https://arxiv.org/abs/2610.14802

#VLA #robotics
```

</details>

---

### [Successful but Unsafe: An Analytical Benchmark for Revealing Collisions in Vision-and-Language Navigation](https://arxiv.org/abs/2610.14682)

**Authors:** Hieu D. Pham, Quoc-An Luong, Dung D. Le

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14682) | [PDF](https://arxiv.org/pdf/2610.14682)

<details>
<summary>Abstract</summary>

Vision-and-language navigation (VLN) agents are typically evaluated by whether they reach a target and how efficiently they follow an instructed route, yet these metrics provide little information about collision behavior. Moreover, continuous VLN evaluation commonly uses a sliding regime, where an agent can slide along obstacles after a collision, potentially masking the effect of unsafe actions on navigation performance. We introduce VLN-Safe, a benchmark for analyzing collision safety under two complementary evaluation regimes: sliding, reflecting common VLN evaluation practice, and blockin...

</details>

<details>
<summary>Share</summary>

```
Successful but Unsafe: An Analytical Benchmark for Revealing Collisions in Vision-and-Language Navigation

Vision-and-language navigation (VLN) agents are typically evaluated by whether they reach a target and how efficiently they follow an instructed route, yet these metrics provide little information about collision beha...

arXiv: https://arxiv.org/abs/2610.14682

#VLA #robotics
```

</details>

---

### [VioLA: Learning Generalist Humanoid Control Policies from Human Data](https://arxiv.org/abs/2610.12435)

**Authors:** Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12435) | [PDF](https://arxiv.org/pdf/2610.12435)

<details>
<summary>Abstract</summary>

Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing...

</details>

<details>
<summary>Share</summary>

```
VioLA: Learning Generalist Humanoid Control Policies from Human Data

Teaching a humanoid to follow instructions with its whole body runs into two obstacles.

arXiv: https://arxiv.org/abs/2610.12435

#VLA #robotics
```

</details>

---

### [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](https://arxiv.org/abs/2610.12369)

**Authors:** Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12369) | [PDF](https://arxiv.org/pdf/2610.12369)

<details>
<summary>Abstract</summary>

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code measures and tracks the robot, environment, and task state from camera images and proprioception, a...

</details>

<details>
<summary>Share</summary>

```
Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time.

arXiv: https://arxiv.org/abs/2610.12369

#VLA #robotics
```

</details>

---

### [RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes](https://arxiv.org/abs/2610.11480)

**Authors:** Bohan Zhou, Xingbei Chen, Emily Huang, Weilin Ruan, Haojian Huang et al. (20 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.11480) | [PDF](https://arxiv.org/pdf/2610.11480)

<details>
<summary>Abstract</summary>

Embodied coding agents can combine modular robot skills with frozen end-to-end policies, yet effective composition requires anticipating which policy family will succeed in the current physical state. We present RoboAware, which builds on coding agents' skill orchestration by learning only a state-conditioned responsibility coordinator from counterfactual outcomes. Inspired by the success of REPL, we propose the $P^5$ schema and formulate a hierarchical MDP based on it. $P^5$ organizes skills uniformly into five semantic stages, defining where responsibility can be compared. To address the lac...

</details>

<details>
<summary>Share</summary>

```
RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes

Embodied coding agents can combine modular robot skills with frozen end-to-end policies, yet effective composition requires anticipating which policy family will succeed in the current physical state.

arXiv: https://arxiv.org/abs/2610.11480

#VLA #robotics
```

</details>

---

### [Q-Learning with Scalar Adjoint Matching](https://arxiv.org/abs/2610.10437)

**Authors:** Yonghoon Dong, Minsung Yoon, Jaehyuk Kim, Jungwoo Park, Changyeon Kim et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.10437) | [PDF](https://arxiv.org/pdf/2610.10437)

<details>
<summary>Abstract</summary>

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to update the flow model itself by propagating value information from the final action back to each flow step, but it requires a vector--Jacobian product through the policy at every step, a cost that grows with the number of flow steps and the pol...

</details>

<details>
<summary>Share</summary>

```
Q-Learning with Scalar Adjoint Matching

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest.

arXiv: https://arxiv.org/abs/2610.10437

#VLA #robotics
```

</details>

---

### [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](https://arxiv.org/abs/2610.12107)

**Authors:** Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou, Shuhan Yang, Junchao Huang et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12107) | [PDF](https://arxiv.org/pdf/2610.12107)

<details>
<summary>Abstract</summary>

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise boundary delineation. This requirement challenges existing cascaded vision-language architectures, which typically rely on static feature interfaces and single-pass mask prediction, limiting adaptive perception and geometric correction. We introduce ContourVLA, a vision-language-action policy that recasts GRES as a closed-loop visuomotor process, in which editable contours serve a...

</details>

<details>
<summary>Share</summary>

```
ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise...

arXiv: https://arxiv.org/abs/2610.12107

#VLA #robotics
```

</details>

---
