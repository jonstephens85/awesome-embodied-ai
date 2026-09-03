# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-09-03 19:07 UTC

**Papers shown:** 31 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406)

**Authors:** Kechen Liu, Ola Shorinwa

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.27406) | [PDF](https://arxiv.org/pdf/2608.27406) | [Project Page](https://omni-clap.github.io)

<details>
<summary>Abstract</summary>

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. However, cross-embodiment learning is no...

</details>

<details>
<summary>Share</summary>

```
CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learni...

arXiv: https://arxiv.org/abs/2608.27406
Project page: https://omni-clap.github.io

#worldmodels #robotics
```

</details>

---

### [Do Better Imagined Rollouts Mean Better Robot Control? A Controlled Study of World-Model Evaluation Under Feedback](https://arxiv.org/abs/2609.02811)

**Authors:** Dharini Raghavan, Amritpal Singh

**Published:** 2026-09-02 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.02811) | [PDF](https://arxiv.org/pdf/2609.02811) | [Code](https://github.com/rdharini2001/Robot_World_Model)

<details>
<summary>Abstract</summary>

Predictive models are increasingly used in robotics for state estimation, planning, control, and policy evaluation, yet they are often judged by open-loop prediction accuracy over a fixed horizon. In closed-loop operation, a robot repeatedly acts, receives new measurements, updates its state estimate, and recomputes control. We study this difference in a differential-drive path-tracking task with biased odometry and intermittent landmark sensing. Six state estimators are evaluated across 24 sensing conditions using trajectory replay, a 20-step measurement-free rollout, and closed-loop tracking...

</details>

<details>
<summary>Share</summary>

```
Do Better Imagined Rollouts Mean Better Robot Control? A Controlled Study of World-Model Evaluation Under Feedback

Predictive models are increasingly used in robotics for state estimation, planning, control, and policy evaluation, yet they are often judged by open-loop prediction accuracy over a fixed horizon.

arXiv: https://arxiv.org/abs/2609.02811
Code: https://github.com/rdharini2001/Robot_World_Model

#worldmodels #robotics
```

</details>

---

### [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910)

**Authors:** Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu et al. (17 authors)

**Published:** 2026-08-30 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.29910) | [PDF](https://arxiv.org/pdf/2608.29910) | [Project Page](https://matrix-game-v3-5.github.io/)

<details>
<summary>Abstract</summary>

Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consistency, and camera control while supporting real-time autoregressive generation. Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and...

</details>

<details>
<summary>Share</summary>

```
Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR.

arXiv: https://arxiv.org/abs/2608.29910
Project page: https://matrix-game-v3-5.github.io/

#worldmodels #robotics
```

</details>

---

### [Hydra: A Navigation World Action Model with Discrete Latent Planning and Continuous Flow-Matching Execution](https://arxiv.org/abs/2608.28995)

**Authors:** Mohammad Nazeri, Alexandyr Card, Samira Huber, Anuj Pokhrel, Yujun Wang et al. (9 authors)

**Published:** 2026-08-29 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.28995) | [PDF](https://arxiv.org/pdf/2608.28995) | [Project Page](https://robotixx.github.io/hydra)

<details>
<summary>Abstract</summary>

World models let robots imagine possible futures, but exploiting this capability for real-time control is bottlenecked by a representation misalignment: the generative model and the planner operate on decoupled manifolds, so the planner has no shared structure to search over and must instead decode every candidate back into high-dimensional pixel space to evaluate it. This decoding step is a major obstacle to real-time control on physical hardware. In this paper, we present Hydra, a discrete World Action Model that closes this gap by moving the planner, both the sampler and the evaluator, insi...

</details>

<details>
<summary>Share</summary>

```
Hydra: A Navigation World Action Model with Discrete Latent Planning and Continuous Flow-Matching Execution

World models let robots imagine possible futures, but exploiting this capability for real-time control is bottlenecked by a representation misalignment: the generative model and the planner operate on decoupled manifo...

arXiv: https://arxiv.org/abs/2608.28995
Project page: https://robotixx.github.io/hydra

#worldmodels #robotics
```

</details>

---

### [CAER: Causal Action Effect Reweighting for World Model Training](https://arxiv.org/abs/2608.30897)

**Authors:** Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang et al. (12 authors)

**Published:** 2026-08-31 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.30897) | [PDF](https://arxiv.org/pdf/2608.30897) | [Project Page](https://manifoldai-research.github.io/CAER/)

<details>
<summary>Abstract</summary>

World models are becoming core infrastructure for embodied intelligence, with action-conditioned video generation providing controllable predictions of how scenes evolve after agent interventions. Yet existing models are commonly trained with space-time-uniform mean squared error, allowing abundant background tokens to dominate the gradient while sparse interaction dynamics remain under-optimized; such uniform fitting rewards reconstructing appearance rather than learning how actions change the world. We introduce Causal Action Effect Reweighting (CAER), a general training paradigm that redist...

</details>

<details>
<summary>Share</summary>

```
CAER: Causal Action Effect Reweighting for World Model Training

World models are becoming core infrastructure for embodied intelligence, with action-conditioned video generation providing controllable predictions of how scenes evolve after agent interventions.

arXiv: https://arxiv.org/abs/2608.30897
Project page: https://manifoldai-research.github.io/CAER/

#worldmodels #robotics
```

</details>

---

### [Can Video World Models Track Unobserved World States?](https://arxiv.org/abs/2608.30692)

**Authors:** Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang

**Published:** 2026-08-31 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.30692) | [PDF](https://arxiv.org/pdf/2608.30692) | [Project Page](https://joonghyuk.com/stateful-vwm-web/)

<details>
<summary>Abstract</summary>

Video world models are increasingly used as simulators, yet visual fidelity alone does not show that a model maintains the hidden state of the world. We examine this gap with an action-conditioned video Shell Game, a visual analog of $S_5$ state tracking that decouples visual rendering from compositing the hidden state underneath. Bidirectional and autoregressive Transformers, Mamba, and linear attention restricted to nonnegative transition eigenvalues all fit the training horizon of 5 swaps and then fall toward chance on longer swap chains (extrapolation) while still rendering plausible video...

</details>

<details>
<summary>Share</summary>

```
Can Video World Models Track Unobserved World States?

Video world models are increasingly used as simulators, yet visual fidelity alone does not show that a model maintains the hidden state of the world.

arXiv: https://arxiv.org/abs/2608.30692
Project page: https://joonghyuk.com/stateful-vwm-web/

#worldmodels #robotics
```

</details>

---

### [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](https://arxiv.org/abs/2608.27328)

**Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li et al. (10 authors)

**Published:** 2026-08-27 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.27328) | [PDF](https://arxiv.org/pdf/2608.27328) | [Code](https://github.com/AMAP-ML/R2MBench)

<details>
<summary>Abstract</summary>

High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambiguity makes absolute revisit scores sensitive to rendering stability, repetitive content, and failed motion. We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency. For every detected return, R2M-Bench compares the revisit pair with two controls from the same rollout: a gap-matched non-revisit pair that mea...

</details>

<details>
<summary>Share</summary>

```
R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models

High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little.

arXiv: https://arxiv.org/abs/2608.27328
Code: https://github.com/AMAP-ML/R2MBench

#worldmodels #robotics
```

</details>

---

### [Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation](https://arxiv.org/abs/2609.02046)

**Authors:** Param Thakkar, Parsika Paresh Shah, Manisha Sushant Gote

**Published:** 2026-09-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.02046) | [PDF](https://arxiv.org/pdf/2609.02046)

<details>
<summary>Abstract</summary>

Monolithic world models predict the entire next state at every step, spending capacity re-predicting the static majority of a scene and injecting error into it. We ask whether explicitly modeling change (a per-object change gate plus a residual delta head that perturbs only the objects the gate flags) is a more effective and interpretable bias for physical prediction and control. On a MuJoCo tabletop pushing benchmark scaling from 3 to 8 objects, the sparse/residual model predicts next-state poses 2.5 to 4.6 times more accurately than a dense multilayer perceptron at 8.6 to 11.1 times fewer pa...

</details>

<details>
<summary>Share</summary>

```
Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation

Monolithic world models predict the entire next state at every step, spending capacity re-predicting the static majority of a scene and injecting error into it.

arXiv: https://arxiv.org/abs/2609.02046

#worldmodels #robotics
```

</details>

---

### [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](https://arxiv.org/abs/2608.30237)

**Authors:** Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang et al. (19 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2608.30237) | [PDF](https://arxiv.org/pdf/2608.30237)

<details>
<summary>Abstract</summary>

General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-evolving general world model for dexterous manipulation. Motus2 advances world modeling through model scaling and data scaling. For model scaling, a single model with shared weights exposes three control interfaces: a policy (world-action mo...

</details>

<details>
<summary>Share</summary>

```
Motus2: A Self-Evolving General World Model for Dexterous Manipulation

General embodied agents should perceive, predict, act, evaluate, and improve within a unified system.

arXiv: https://arxiv.org/abs/2608.30237

#worldmodels #robotics
```

</details>

---

### [AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization](https://arxiv.org/abs/2608.29242)

**Authors:** Cheng Chen, Jerry Bai, Jiacheng Wei, Boyu Chen, Xiaoji Zheng et al. (14 authors)

**Published:** 2026-08-29 (updated 2026-09-01) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.29242) | [PDF](https://arxiv.org/pdf/2608.29242) | [Project Page](https://xpeng-robotics.github.io/anyworld/)

<details>
<summary>Abstract</summary>

Collecting contact-rich robot experiences at scale remains a major bottleneck for generalizable manipulation. Beyond data quantity, robot learning also requires diverse experiences across embodiments, viewpoints, and scenes. Human egocentric videos provide abundant physical interactions, but each video captures only a narrow slice of experience under a single body, camera trajectory, and environment. We propose AnyWorld, a cross-embodiment world modeling framework that expands a single human interaction into diverse robot-native rollouts without paired human-robot demonstrations. Our model fac...

</details>

<details>
<summary>Share</summary>

```
AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization

Collecting contact-rich robot experiences at scale remains a major bottleneck for generalizable manipulation.

arXiv: https://arxiv.org/abs/2608.29242
Project page: https://xpeng-robotics.github.io/anyworld/

#worldmodels #robotics
```

</details>

---

### [Decoupling Planning and Control for Instructable Agents](https://arxiv.org/abs/2608.26788)

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr

**Published:** 2026-08-27 | **Categories:** cs.AI, cs.CL, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.26788) | [PDF](https://arxiv.org/pdf/2608.26788) | [Project Page](https://zinengtang.github.io/instruct-to-act/)

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high...

</details>

<details>
<summary>Share</summary>

```
Decoupling Planning and Control for Instructable Agents

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-la...

arXiv: https://arxiv.org/abs/2608.26788
Project page: https://zinengtang.github.io/instruct-to-act/

#worldmodels #robotics
```

</details>

---

### [Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](https://arxiv.org/abs/2609.00610)

**Authors:** Xiaoyan Liu, Jiaxin Liu, Kangrui Li, Sifan Zhou

**Published:** 2026-09-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.00610) | [PDF](https://arxiv.org/pdf/2609.00610)

<details>
<summary>Abstract</summary>

Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency. This limits applications in interactive real-time scenarios. To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction. Unlike traditional frame-by-frame emission and delayed geometry recovery, Streaming4D generates temporal video blocks and immediately triggers reconstruction for each complete...

</details>

<details>
<summary>Share</summary>

```
Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction

Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency.

arXiv: https://arxiv.org/abs/2609.00610

#worldmodels #robotics
```

</details>

---

### [Towards a Belief-Based World Model for LLM Agents](https://arxiv.org/abs/2609.00455)

**Authors:** Shubham Kumar, Harshit Kumar, Narendra Ahuja, Saurabh Jha

**Published:** 2026-08-31 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.00455) | [PDF](https://arxiv.org/pdf/2609.00455) | [Code](https://github.com/skumar-ml/belief-world-models)

<details>
<summary>Abstract</summary>

Large language models (LLMs) are being used as policies for autonomous decision-making and planning in many domains. Despite their strong reasoning capabilities, LLMs struggle with long-horizon tasks, especially under partial observability. World models are a promising way to enhance policy performance, both during training and inference. During inference, agents currently use world models to simulate the consequences of candidate actions before committing to an action, which can improve decision-making. However, we argue that simulation alone is an incomplete interface for decision-making und...

</details>

<details>
<summary>Share</summary>

```
Towards a Belief-Based World Model for LLM Agents

Large language models (LLMs) are being used as policies for autonomous decision-making and planning in many domains.

arXiv: https://arxiv.org/abs/2609.00455
Code: https://github.com/skumar-ml/belief-world-models

#worldmodels #robotics
```

</details>

---

### [Off-Manifold Refinement: Guiding Video Generators with a Frozen World Model](https://arxiv.org/abs/2608.29904)

**Authors:** Hai Nguyen-Truong, Tuan-Anh Vu, Dang Huynh

**Published:** 2026-08-30 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.29904) | [PDF](https://arxiv.org/pdf/2608.29904) | [Project Page](https://itruonghai.github.io/omr)

<details>
<summary>Abstract</summary>

Modern video generators routinely fail at physical dynamics: objects float, trajectories violate gravity, contacts vanish. Standard denoising and flow-matching objectives fit visual data distributions but do not explicitly penalize such physical violations. Existing remedies can improve physical consistency, but typically add substantial inference or training cost. Candidate-selection methods generate and score multiple videos, while gradient-based world-model guidance repeatedly decodes and re-encodes intermediate estimates. Generator-internal refinement adds perturbation and re-denoising loo...

</details>

<details>
<summary>Share</summary>

```
Off-Manifold Refinement: Guiding Video Generators with a Frozen World Model

Modern video generators routinely fail at physical dynamics: objects float, trajectories violate gravity, contacts vanish.

arXiv: https://arxiv.org/abs/2608.29904
Project page: https://itruonghai.github.io/omr

#worldmodels #robotics
```

</details>

---

### [Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations](https://arxiv.org/abs/2608.29434)

**Authors:** Fabio F. Oberweger, Michael Schwingshackl

**Published:** 2026-08-29 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.29434) | [PDF](https://arxiv.org/pdf/2608.29434)

<details>
<summary>Abstract</summary>

JEPA world models make latent-space planning a practical route to control, but they are built almost exclusively on images. Whether latent prediction survives geometric observations is unclear: point clouds are sparse, unordered, and self-occluded, and with 0.3-15% of scene points moving, the slow-feature optimum of latent prediction compounds with the geometric shortcut of 3D self-supervision. We lift three canonical JEPA designs to point clouds, frozen-encoder, distribution-prior, and action-sensitive, and re-sense the stable-worldmodel benchmark so that only the observation differs from the...

</details>

<details>
<summary>Share</summary>

```
Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations

JEPA world models make latent-space planning a practical route to control, but they are built almost exclusively on images.

arXiv: https://arxiv.org/abs/2608.29434

#worldmodels #robotics
```

</details>

---

### [WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning](https://arxiv.org/abs/2608.27508)

**Authors:** Yu Han, Tianwen Qian

**Published:** 2026-08-27 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.27508) | [PDF](https://arxiv.org/pdf/2608.27508) | [Code](https://github.com/genalyu/WM-R1)

<details>
<summary>Abstract</summary>

GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also e...

</details>

<details>
<summary>Share</summary>

```
WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning

GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms.

arXiv: https://arxiv.org/abs/2608.27508
Code: https://github.com/genalyu/WM-R1

#worldmodels #robotics
```

</details>

---

### [From Proxy Learning to Driving Decisions: A Transfer-Based Framework for Evaluating Future-Aware Autonomous Driving Planners](https://arxiv.org/abs/2609.02688)

**Authors:** Yikai Wu

**Published:** 2026-09-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.02688) | [PDF](https://arxiv.org/pdf/2609.02688)

<details>
<summary>Abstract</summary>

Future-aware representations and world models are increasingly used in proposal-based autonomous-driving planners to improve trajectory selection. However, improvements in proxy objectives or restricted subsets are often interpreted as planning gains without verifying proposal ordering, selected trajectories, full-scale utility, and critical driving components. We propose the Proxy-to-Decision Transfer (PDT) Framework, an analysis framework that evaluates when learned future information supports a reliable driving-performance improvement claim. Its Decision-Transfer Decomposition Module locali...

</details>

<details>
<summary>Share</summary>

```
From Proxy Learning to Driving Decisions: A Transfer-Based Framework for Evaluating Future-Aware Autonomous Driving Planners

Future-aware representations and world models are increasingly used in proposal-based autonomous-driving planners to improve trajectory selection.

arXiv: https://arxiv.org/abs/2609.02688

#worldmodels #robotics
```

</details>

---

### [World-Model-Augmented Visual Locomotion for Humanoids on Foothold-Constrained Terrain](https://arxiv.org/abs/2609.02542)

**Authors:** Yuxi Liu, Lijun Han, Ziming Wang, Ao Zhang, Cong Yang et al. (6 authors)

**Published:** 2026-09-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.02542) | [PDF](https://arxiv.org/pdf/2609.02542)

<details>
<summary>Abstract</summary>

Foothold-constrained terrain is characterized by sparse, discontinuous, or geometrically restricted feasible foot contacts, as encountered on stepping stones, across gaps, and on narrow stair treads. On such terrain, a single misstep often leaves little room to recover, so policies that base foot-placement decisions primarily on the immediately visible terrain are prone to failure. We ask whether a learned predictive summary of near-future observations and rewards can provide the anticipatory information required in such settings. We present World-Model-Augmented Visual Locomotion (WM-LOCO), w...

</details>

<details>
<summary>Share</summary>

```
World-Model-Augmented Visual Locomotion for Humanoids on Foothold-Constrained Terrain

Foothold-constrained terrain is characterized by sparse, discontinuous, or geometrically restricted feasible foot contacts, as encountered on stepping stones, across gaps, and on narrow stair treads.

arXiv: https://arxiv.org/abs/2609.02542

#worldmodels #robotics
```

</details>

---

### [RoboPhys-3D: A Comprehensive Embodied World Model Evaluation via 3D Reconstruction](https://arxiv.org/abs/2608.28718)

**Authors:** Tianyi Wang, Jiazhou Chen, Yiming Xu, Xiangyu Li, Tianyi Zeng et al. (10 authors)

**Published:** 2026-08-28 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.28718) | [PDF](https://arxiv.org/pdf/2608.28718)

<details>
<summary>Abstract</summary>

Video world models increasingly serve as data engines, action planners, and simulators for embodied AI, but conventional embodied world model (EWM) benchmarks lack a unified 3D-grounded protocol for establishing whether generated rollouts preserve the underlying 3D scene state or translate into executable actions. We introduce RoboPhys-3D, a 3D-grounded EWM benchmark built on RoboTwin 2.0, covering 50 manipulation tasks across four regimes, with 5,000 episodes and 25,000 multi-view ground-truth videos. A defining feature of RoboPhys-3D is that generated and ground-truth videos are processed th...

</details>

<details>
<summary>Share</summary>

```
RoboPhys-3D: A Comprehensive Embodied World Model Evaluation via 3D Reconstruction

Video world models increasingly serve as data engines, action planners, and simulators for embodied AI, but conventional embodied world model (EWM) benchmarks lack a unified 3D-grounded protocol for establishing wheth...

arXiv: https://arxiv.org/abs/2608.28718

#worldmodels #robotics
```

</details>

---

### [Riemann-1.0: An Embodied World Action Model for Physical AI](https://arxiv.org/abs/2608.27033)

**Authors:** Haofeng Sun, Jiangbo Pei, Fei Kang, Zexiang Liu, Yaokun Li et al. (16 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2608.27033) | [PDF](https://arxiv.org/pdf/2608.27033)

<details>
<summary>Abstract</summary>

We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence. Riemann-1.0 jointly models multi-view visual observations, robot states, and embodiment-specific actions within a unified causal autoregressive sequence, representing robot actions and world evolution as causal state transitions. Unlike existing WAMs based on joint generation, video-first prediction, or decoupled modeling paradigms, Riemann-1.0 unifies online robot policy execution and action-conditioned world simulation within a single model, enabling it to function as both an executable robo...

</details>

<details>
<summary>Share</summary>

```
Riemann-1.0: An Embodied World Action Model for Physical AI

We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence.

arXiv: https://arxiv.org/abs/2608.27033

#worldmodels #robotics
```

</details>

---

### [Flow-JEPA: Flow Matching for Robust Latent Dynamics in JEPA World Models](https://arxiv.org/abs/2608.29029)

**Authors:** Yanchen Huo, Ziying Song, Yadan Luo

**Published:** 2026-08-29 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.29029) | [PDF](https://arxiv.org/pdf/2608.29029)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) have shown strong potential for learning compact predictive representations, and LeWorldModel (LeWM) extends this paradigm to reconstruction-free latent world modeling from pixels. However, its deterministic autoregressive predictor generates future states through repeated one-step transitions, which can accumulate errors and remain sensitive to task-irrelevant visual perturbations. In this work, we propose Flow-JEPA (F-JEPA), a conditional flow matching dynamics model that jointly generates a sequence of future latent states conditioned on the...

</details>

<details>
<summary>Share</summary>

```
Flow-JEPA: Flow Matching for Robust Latent Dynamics in JEPA World Models

Joint-Embedding Predictive Architectures (JEPAs) have shown strong potential for learning compact predictive representations, and LeWorldModel (LeWM) extends this paradigm to reconstruction-free latent world modeling...

arXiv: https://arxiv.org/abs/2608.29029

#worldmodels #robotics
```

</details>

---

### [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](https://arxiv.org/abs/2608.27367)

**Authors:** Frederik Berenz

**Published:** 2026-08-27 (updated 2026-09-01) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.27367) | [PDF](https://arxiv.org/pdf/2608.27367)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transformer blocks for higher-order semantic abstraction), driven by a task-agnostic test-and-verify mechanis...

</details>

<details>
<summary>Share</summary>

```
Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models

Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with signi...

arXiv: https://arxiv.org/abs/2608.27367

#worldmodels #robotics
```

</details>

---

### [Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531)

**Authors:** Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid

**Published:** 2026-09-02 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.02531) | [PDF](https://arxiv.org/pdf/2609.02531)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale video. This has made them a promising paradigm for robot policy learning, yet the prevailing models operate exclusively on RGB observations and do not leverage 3D information. To bridge this gap, we introduce a Spatially Aware World Action Model (SA-WAM), which repurposes a pretrained video model for joint action, RGB, and depth prediction, enabling 3D-aware world modeling and act...

</details>

<details>
<summary>Share</summary>

```
Spatially Aware World Action Model via Geometric Latent Diffusion

World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale...

arXiv: https://arxiv.org/abs/2609.02531

#worldmodels #robotics
```

</details>

---

### [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](https://arxiv.org/abs/2609.00161)

**Authors:** Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu et al. (11 authors)

**Published:** 2026-08-31 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.00161) | [PDF](https://arxiv.org/pdf/2609.00161)

<details>
<summary>Abstract</summary>

World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions. Existing approaches address this limitation by constraining the generation process with external representations encoding motion, geometry, or semantics. Obtaining these spatiotemporally dense representations typically requires auxiliary estimators or manual annotations, limiting training scalability. We instead revisit the training objective and identify a supervision-allocation mismatch under the globally averaged mean squared...

</details>

<details>
<summary>Share</summary>

```
IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training

World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions.

arXiv: https://arxiv.org/abs/2609.00161

#worldmodels #robotics
```

</details>

---

### [Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving](https://arxiv.org/abs/2608.29772)

**Authors:** Dong Hu, Chao Huang, Carman K. M. Lee, Dimitrios Kanoulas

**Published:** 2026-08-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.29772) | [PDF](https://arxiv.org/pdf/2608.29772)

<details>
<summary>Abstract</summary>

Learning-based autonomous driving (AD) systems can perform reliably in familiar conditions, yet rare distribution shifts and long-tail events remain a major source of abrupt failure. A central limitation is that most agents learn primarily from passive experience and lack mechanisms to estimate when their competence is insufficient, seek timely assistance, and convert safety-critical encounters into targeted improvement. Here we present self-aware guided exploration (SAGE), an active learning framework for post-training adaptation in AD. SAGE learns a predictive world model that generates two...

</details>

<details>
<summary>Share</summary>

```
Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving

Learning-based autonomous driving (AD) systems can perform reliably in familiar conditions, yet rare distribution shifts and long-tail events remain a major source of abrupt failure.

arXiv: https://arxiv.org/abs/2608.29772

#worldmodels #robotics
```

</details>

---

### [Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](https://arxiv.org/abs/2609.02864)

**Authors:** Yutong Liu, Nan Huang, Xu Cao, James M. Rehg

**Published:** 2026-09-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.02864) | [PDF](https://arxiv.org/pdf/2609.02864)

<details>
<summary>Abstract</summary>

Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introduce RIG-BENCH, a novel comprehensive benchmark that systematically evaluates Reasoning-driven Image G...

</details>

<details>
<summary>Share</summary>

```
Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation

Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis.

arXiv: https://arxiv.org/abs/2609.02864

#worldmodels #robotics
```

</details>

---

### [The Intervention Gap in Latent World Models](https://arxiv.org/abs/2608.29998)

**Authors:** Donna Vakalis

**Published:** 2026-08-30 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2608.29998) | [PDF](https://arxiv.org/pdf/2608.29998)

<details>
<summary>Abstract</summary>

Planning-time intervention fidelity is a distinct, measurable property of a learned world model: whether the model's own open-loop transitions move task variables the way matched environment interventions do. In the settings we test, it is neither revealed by reward fit nor ensured by task-anchored training. Across released TD-MPC2 checkpoint sizes, episode return falls as an operator-error diagnostic on task observables grows, while reward-prediction error stays small and nearly flat, and a self-supervised world model trained without task signal preserves the same operator substantially bette...

</details>

<details>
<summary>Share</summary>

```
The Intervention Gap in Latent World Models

Planning-time intervention fidelity is a distinct, measurable property of a learned world model: whether the model's own open-loop transitions move task variables the way matched environment interventions do.

arXiv: https://arxiv.org/abs/2608.29998

#worldmodels #robotics
```

</details>

---

### [AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies](https://arxiv.org/abs/2608.29937)

**Authors:** Yafei Zhang, Nan Wu

**Published:** 2026-08-30 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2608.29937) | [PDF](https://arxiv.org/pdf/2608.29937)

<details>
<summary>Abstract</summary>

Latent world-action models avoid rendering future pixels by predicting an action-relevant visual subgoal in feature space. LaWAM established this formulation, but its original presentation left the world model, multimodal backbone, and deployment checkpoint tightly coupled. We introduce AcrossWAM1.0, a modularization and scaling study of this latent world-action stack. Rather than presenting latent subgoals as a new algorithm, we make the module boundary explicit: a policy adapter produces latent-action and action-generation contexts; a retained latent world decoder grounds the predicted trans...

</details>

<details>
<summary>Share</summary>

```
AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies

Latent world-action models avoid rendering future pixels by predicting an action-relevant visual subgoal in feature space.

arXiv: https://arxiv.org/abs/2608.29937

#worldmodels #robotics
```

</details>

---

### [GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments](https://arxiv.org/abs/2609.00048)

**Authors:** Lin Fu, Zheyuan Yang, Tianhui Zhang, Jinbiao Wei, Guo Gan et al. (8 authors)

**Published:** 2026-08-30 | **Categories:** cs.CL, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.00048) | [PDF](https://arxiv.org/pdf/2609.00048)

<details>
<summary>Abstract</summary>

GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents. This mismatch leaves a key requirement under-tested: generated states must remain contextually consistent when they are repeatedly reused for future interaction. We introduce GUI-CC, a benchmark that evaluates contextual consistency of GUI world models as agent environments rather than isolated next-screen predictors. GUI-CC contains two complementary tracks: an offline reference-action track that rolls models along real mobile GUI trajector...

</details>

<details>
<summary>Share</summary>

```
GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments

GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents.

arXiv: https://arxiv.org/abs/2609.00048

#worldmodels #robotics
```

</details>

---

### [Should I Use This Synthetic Dataset for Training? How to Test with Minimal Real Data](https://arxiv.org/abs/2608.27996)

**Authors:** Zhenyu Tao, Wei Xu, Xiaohu You, Petar Popovski, Osvaldo Simeone

**Published:** 2026-08-28 | **Categories:** cs.AI, cs.IT, math.ST | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2608.27996) | [PDF](https://arxiv.org/pdf/2608.27996)

<details>
<summary>Abstract</summary>

Digital twins (DTs) and learned world models are increasingly used to generate synthetic data that augment the scarce real datasets available for training artificial intelligence (AI) models in engineering systems. Owing to the inevitable simulation-to-reality (sim-to-real) gap, however, augmentation may fail to improve the performance of the trained model on the real data distribution. This paper addresses the resulting decision problem: Given a real dataset, a candidate synthetic dataset, and a fixed learning algorithm, decide whether training on the augmented dataset improves the true, popu...

</details>

<details>
<summary>Share</summary>

```
Should I Use This Synthetic Dataset for Training? How to Test with Minimal Real Data

Digital twins (DTs) and learned world models are increasingly used to generate synthetic data that augment the scarce real datasets available for training artificial intelligence (AI) models in engineering systems.

arXiv: https://arxiv.org/abs/2608.27996

#worldmodels #robotics
```

</details>

---

### [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345)

**Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević et al. (14 authors)

**Published:** 2026-08-27 (updated 2026-08-28) | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2608.27345) | [PDF](https://arxiv.org/pdf/2608.27345)

<details>
<summary>Abstract</summary>

Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recover the correct distribution. This raises a central question: how far are current video generators fro...

</details>

<details>
<summary>Share</summary>

```
PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

Recent video generation models are increasingly framed as world models.

arXiv: https://arxiv.org/abs/2608.27345

#worldmodels #robotics
```

</details>

---
