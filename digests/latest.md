# What's New

Papers discovered in the run at **2026-11-18 22:50 UTC**.

**New this run:** 9

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (4)

### [RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models](https://arxiv.org/abs/2611.22736)

**Authors:** Shaozhen Liu, Zhiwei Li, Jiayang Sun, Shuangjun Du, Yi Zhong et al. (9 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22736) | [PDF](https://arxiv.org/pdf/2611.22736)

<details>
<summary>Abstract</summary>

Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retraining when manipulation objects change. We introduce RefCloth, a framework that optimizes one persistent adversarial tablecloth on a frozen source policy and deploys it zero-shot across unseen tasks and target models without modifying task objects or cameras. Throughout manipulation, static third-person and moving wrist views observe this shared world-bound texture under evolving oc...

</details>

<details>
<summary>Share</summary>

```
RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models

Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retrain...

arXiv: https://arxiv.org/abs/2611.22736

#VLA #robotics
```

</details>

---

### [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2611.22880)

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.22880) | [PDF](https://arxiv.org/pdf/2611.22880)

<details>
<summary>Abstract</summary>

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portion of the tokens directly encode critical planning-relevant factors, such as agent geometry, motion d...

</details>

<details>
<summary>Share</summary>

```
Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely re...

arXiv: https://arxiv.org/abs/2611.22880

#VLA #robotics
```

</details>

---

### [Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies](https://arxiv.org/abs/2611.22878)

**Authors:** Yuhan Wang, Ruiyang Wang, Jiaguan Zhu

**Published:** 2026-11-17 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22878) | [PDF](https://arxiv.org/pdf/2611.22878)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction. However, this optimization raises two challenges: policy updates can alter the velocity-field geometry underlying the score approximation used for stochastic transitions, and sparse multi-task rollouts can yield uneven learning signals across tasks and advantage signs. We introduce an RL framework that combines Outcome-Balanced Proximal Policy Optimization (PPO) with policy-induced flow rectification. Outcome-Balanced PPO rewe...

</details>

<details>
<summary>Share</summary>

```
Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies

Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction.

arXiv: https://arxiv.org/abs/2611.22878

#VLA #robotics
```

</details>

---

### [PAIR: Bringing Household Robots into the Smart Home](https://arxiv.org/abs/2611.23070)

**Authors:** Junseong Pyo, Hyeongjin Kim, Jongwook Han, Seungwon Kook, Sungjib Lim et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23070) | [PDF](https://arxiv.org/pdf/2611.23070)

<details>
<summary>Abstract</summary>

Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs. Existing embodied AI simulation environments, however, model appliances solely as physical objects. We introduce PAIR, a smart-home simulation environment grounded in the Matter protocol~\footnote{https://csa-iot.org/all-solutions/matter/}, the industry standard for smart-home devices. PAIR provides 84 smart-device assets whose functional control panels and APIs act on a shared device state, with ambient conditions that evolve in response to both. From a survey of 1,443 requests,...

</details>

<details>
<summary>Share</summary>

```
PAIR: Bringing Household Robots into the Smart Home

Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs.

arXiv: https://arxiv.org/abs/2611.23070

#VLA #robotics
```

</details>

---

## World Models (5)

### [Auditing a Learned Simulator for Legged Robots: The Robotic World Model on ANYmal D](https://arxiv.org/abs/2611.23118)

**Authors:** Joyjeet Singh

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.23118) | [PDF](https://arxiv.org/pdf/2611.23118) | [Code](https://github.com/joyjeet-singh/rwm-robot-level)

<details>
<summary>Abstract</summary>

A legged robot can learn to walk inside a learned simulator: a neural network that predicts the robot's next state and is run forward on its own predictions. They are usually trained and checked one step ahead, although a policy uses them for a hundred steps or more. We audit one published system end to end, without a GPU: the dynamics model of the Robotic World Model (RWM) for the ANYmal D quadruped, and the uncertainty estimate of its follow-up, RWM-U. We rebuilt the model to match the released code's outputs, losses and gradients exactly, measured 101 trained simulators, 200 compressed copi...

</details>

<details>
<summary>Share</summary>

```
Auditing a Learned Simulator for Legged Robots: The Robotic World Model on ANYmal D

A legged robot can learn to walk inside a learned simulator: a neural network that predicts the robot's next state and is run forward on its own predictions.

arXiv: https://arxiv.org/abs/2611.23118
Code: https://github.com/joyjeet-singh/rwm-robot-level

#worldmodels #robotics
```

</details>

---

### [Code World Model 2.0: Towards Infinite Controllable Video Generation](https://arxiv.org/abs/2611.22925)

**Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu et al. (11 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.22925) | [PDF](https://arxiv.org/pdf/2611.22925) | [Project Page](https://www.inclusion-ai.org/CodeWorldModel/)

<details>
<summary>Abstract</summary>

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without accumulating drift across self-generated history. We present Invoker-Render, pairing a bidirectional creation model with a causal four-step streaming model under a shared conditioning...

</details>

<details>
<summary>Share</summary>

```
Code World Model 2.0: Towards Infinite Controllable Video Generation

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming.

arXiv: https://arxiv.org/abs/2611.22925
Project page: https://www.inclusion-ai.org/CodeWorldModel/

#worldmodels #robotics
```

</details>

---

### [SpikWM: Efficient End-to-End Spiking World Modeling for Visual Planning](https://arxiv.org/abs/2611.22981)

**Authors:** Shuhan Ye, Hongbin Yu, Chong Wang, Hui Lu, Jiaming He et al. (8 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.22981) | [PDF](https://arxiv.org/pdf/2611.22981) | [Code](https://github.com/ShawnYE618/SpikWM)

<details>
<summary>Abstract</summary>

Goal-conditioned planning with image observations and goals requires predictions that distinguish visual states and action consequences. Spiking neural networks offer sparse computation, but single-step spikes can obscure motion cues and merge actions with different physical outcomes. We propose the Spiking Latent World Model (SpikWM), an end-to-end joint-embedding predictive architecture (JEPA) with one simulation step per image and one neural update per latent position. Spiking Regional Encoding retains spatial cues through regional pooling. Bi-Spike Action Encoding combines positive and neg...

</details>

<details>
<summary>Share</summary>

```
SpikWM: Efficient End-to-End Spiking World Modeling for Visual Planning

Goal-conditioned planning with image observations and goals requires predictions that distinguish visual states and action consequences.

arXiv: https://arxiv.org/abs/2611.22981
Code: https://github.com/ShawnYE618/SpikWM

#worldmodels #robotics
```

</details>

---

### [Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model](https://arxiv.org/abs/2611.22998)

**Authors:** Jiaqi Wu, Yongqi Dong, Yijie Zhong, Maple Shao, Yide Tao et al. (9 authors)

**Published:** 2026-11-17 | **Categories:** cs.AI, cs.ET, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22998) | [PDF](https://arxiv.org/pdf/2611.22998)

<details>
<summary>Abstract</summary>

In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs. We propose a residual-guided reinforcement learning (RL) framework for lightweight trajectory selection with a frozen world model and a fixed candidate bank. The framework uses proximal policy optimization (PPO) to fine-tune a joint policy over candidate selection and bounded trajectory residuals. A context-conditioned ranking network learns candidate preferences from feedback obtained by evaluating local perturbations...

</details>

<details>
<summary>Share</summary>

```
Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model

In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs.

arXiv: https://arxiv.org/abs/2611.22998

#worldmodels #robotics
```

</details>

---

### [Sim2CBF: From Forward Simulations to Implicit Control Barrier Function Safety Filtering without Model Derivatives](https://arxiv.org/abs/2611.22954)

**Authors:** Luzia Knoedler, Yihan Liu, Shaohang Han, Yifei Dong, Jana Tumova

**Published:** 2026-11-17 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22954) | [PDF](https://arxiv.org/pdf/2611.22954)

<details>
<summary>Abstract</summary>

Failure avoidance in complex robot-environment interactions is challenging because the underlying dynamics are difficult to model accurately, and available predictive models may not provide reliable derivatives. We present Sim2CBF, a failure-avoidance framework that solves the Control Barrier Function (CBF)-Safety Filter (SF) optimization problem using only forward-model evaluations, thereby avoiding differentiation of the predictive model. Specifically, we approximate the CBF constraint using finite differences and local linear interpolation over sampled control inputs while preserving failur...

</details>

<details>
<summary>Share</summary>

```
Sim2CBF: From Forward Simulations to Implicit Control Barrier Function Safety Filtering without Model Derivatives

Failure avoidance in complex robot-environment interactions is challenging because the underlying dynamics are difficult to model accurately, and available predictive models may not provide reliable derivatives.

arXiv: https://arxiv.org/abs/2611.22954

#worldmodels #robotics
```

</details>

---
