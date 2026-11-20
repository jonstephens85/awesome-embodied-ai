# What's New

Papers discovered in the run at **2026-11-20 02:44 UTC**.

**New this run:** 14

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (1)

### [EgoPass-Bench: Identifying Objects That May Affect the Wearer's Passage in Egocentric Video](https://arxiv.org/abs/2611.24995)

**Authors:** Hongyu Wang, Chuhan Li, Congjin Xu, Xuandong Zhao, Hua Shen

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24995) | [PDF](https://arxiv.org/pdf/2611.24995)

<details>
<summary>Abstract</summary>

Understanding an egocentric environment requires reasoning about how surrounding entities affect the observer's actions. Existing evaluations of multimodal foundation models (MFMs) examine observer localization, motion trajectories, and action feasibility, but leave the discovery and interpretation of evolving observer-entity interactions insufficiently assessed. We introduce EgoPass-Bench, a benchmark for observer-relative interaction understanding in real-world egocentric video. EgoPass-Bench comprises 284 manually reviewed evaluation clips recorded using Ray-Ban Meta (Gen 2) smart glasses a...

</details>

<details>
<summary>Share</summary>

```
EgoPass-Bench: Identifying Objects That May Affect the Wearer's Passage in Egocentric Video

Understanding an egocentric environment requires reasoning about how surrounding entities affect the observer's actions.

arXiv: https://arxiv.org/abs/2611.24995

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (6)

### [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](https://arxiv.org/abs/2611.25461)

**Authors:** Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25461) | [PDF](https://arxiv.org/pdf/2611.25461) | [Code](https://github.com/LigphiDonk/ActMem)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual...

</details>

<details>
<summary>Share</summary>

```
ActMem: From Latent Memory Reasoning to Grounded Robotic Action

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.

arXiv: https://arxiv.org/abs/2611.25461
Code: https://github.com/LigphiDonk/ActMem

#VLA #robotics
```

</details>

---

### [Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation](https://arxiv.org/abs/2611.25400)

**Authors:** Chengyang Dong, Ze Chen, Kai Ye, Chutian Wang, Heng Xu et al. (14 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25400) | [PDF](https://arxiv.org/pdf/2611.25400)

<details>
<summary>Abstract</summary>

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining. However, backpropagation-based adaptation incurs heavy memory overhead on resource-constrained robots, whereas zeroth-order (ZO) methods suffer from high estimation variance under limited perturbation budgets. We observe that while ZO estimation enables low-memory adaptation with rapid initial gains, it often stalls or degrades over long-horizon updates due to noisy gradient estimates. To address these limitations, we propose Dune, a zeroth-or...

</details>

<details>
<summary>Share</summary>

```
Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining.

arXiv: https://arxiv.org/abs/2611.25400

#VLA #robotics
```

</details>

---

### [RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning](https://arxiv.org/abs/2611.25398)

**Authors:** Dijia Zhan, Jinyi Li, Xuemiao Xu, Yan Zhou, Yu Liu et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25398) | [PDF](https://arxiv.org/pdf/2611.25398)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training. However, we find that demonstration data vary sharply in supervision value across temporal windows, and that each window's value to the policy evolves substantially during training rather than being fixed or captured by raw loss alone. Motivated by this finding, we propose RefreshGrad, an online adaptive data-sampling framework that periodically scores temporal windows from the evolving policy using five policy-native sign...

</details>

<details>
<summary>Share</summary>

```
RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training.

arXiv: https://arxiv.org/abs/2611.25398

#VLA #robotics
```

</details>

---

### [LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models](https://arxiv.org/abs/2611.25460)

**Authors:** LoongForge Team

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.25460) | [PDF](https://arxiv.org/pdf/2611.25460)

<details>
<summary>Abstract</summary>

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraini...

</details>

<details>
<summary>Share</summary>

```
LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to r...

arXiv: https://arxiv.org/abs/2611.25460

#VLA #robotics
```

</details>

---

### [TuringPAI: A Foundation for On-Device Physical AI](https://arxiv.org/abs/2611.25474)

**Authors:** Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang et al. (28 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25474) | [PDF](https://arxiv.org/pdf/2611.25474)

<details>
<summary>Abstract</summary>

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation histo...

</details>

<details>
<summary>Share</summary>

```
TuringPAI: A Foundation for On-Device Physical AI

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute.

arXiv: https://arxiv.org/abs/2611.25474

#VLA #robotics
```

</details>

---

### [MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation](https://arxiv.org/abs/2611.25105)

**Authors:** Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu et al. (13 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25105) | [PDF](https://arxiv.org/pdf/2611.25105)

<details>
<summary>Abstract</summary>

Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the high...

</details>

<details>
<summary>Share</summary>

```
MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

Every move in a robot team changes the world in which its teammates must act.

arXiv: https://arxiv.org/abs/2611.25105

#VLA #robotics
```

</details>

---

## World Models (7)

### [WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation](https://arxiv.org/abs/2611.25251)

**Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25251) | [PDF](https://arxiv.org/pdf/2611.25251) | [Project Page](https://qianzhong-chen.github.io/wevo.github.io/)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and locomotion play data improve contact-dynamics and viewpoint-change prediction. A VLA trained on synthetic demonstrations collects 20 autonomous real robot rollouts per task to align the WM with deployment observations. The VLA, whole-body contro...

</details>

<details>
<summary>Share</summary>

```
WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation

Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps.

arXiv: https://arxiv.org/abs/2611.25251
Project page: https://qianzhong-chen.github.io/wevo.github.io/

#worldmodels #robotics
```

</details>

---

### [Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners](https://arxiv.org/abs/2611.25415)

**Authors:** Junhyeok Lee, Dongheon Lee, Kyu Sung Choi

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25415) | [PDF](https://arxiv.org/pdf/2611.25415) | [Code](https://github.com/jhlee0619/unstick)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architecture (JEPA) world models plan from pixels with model predictive control, yet often fail on tasks their model should handle. Test-time adaptation attributes such failures to model error under distribution shift and updates the weights on the current episode, without checking this attribution against the planning loop itself. We follow the executed planning loop on pushing tasks. In most settings, with and without distribution shift, nearly all failures (at least 96%) are stalls, where the object stays in place while the model predicts progress. The warm-starte...

</details>

<details>
<summary>Share</summary>

```
Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners

Joint-embedding predictive architecture (JEPA) world models plan from pixels with model predictive control, yet often fail on tasks their model should handle.

arXiv: https://arxiv.org/abs/2611.25415
Code: https://github.com/jhlee0619/unstick

#worldmodels #robotics
```

</details>

---

### [MoRE: Mixture-of-Experts for Multi-Physics Robotic World Models](https://arxiv.org/abs/2611.25336)

**Authors:** Ziyu Zhu, Shaowei Liu, Albert J. Zhai, Henry Che, Wei-Chiu Ma et al. (6 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25336) | [PDF](https://arxiv.org/pdf/2611.25336) | [Project Page](https://alwaysleepy.github.io/MoRE-WM-site/)

<details>
<summary>Abstract</summary>

A robotic world model should predict how objects evolve under robot actions and physical dynamics. While recent 3D world models have shown strong predictive capabilities, they still struggle with the heterogeneous dynamics arising from diverse object interactions. To address this in a unified framework, we decompose robotic interactions into distinct physical regimes and assign each to a specialized motion expert. We introduce MoRE, a 3D world model with a mixture of motion experts organized around rigid, deformable, and prehensile dynamics. This design enables a single model to capture divers...

</details>

<details>
<summary>Share</summary>

```
MoRE: Mixture-of-Experts for Multi-Physics Robotic World Models

A robotic world model should predict how objects evolve under robot actions and physical dynamics.

arXiv: https://arxiv.org/abs/2611.25336
Project page: https://alwaysleepy.github.io/MoRE-WM-site/

#worldmodels #robotics
```

</details>

---

### [Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans](https://arxiv.org/abs/2611.25243)

**Authors:** Chrisantus Eze, Christopher Crick

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25243) | [PDF](https://arxiv.org/pdf/2611.25243)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) can propose multi-step manipulation plans, but they have no grounded model of how a scene will change, and the pixel-level world models that could check those plans are slow and drift over long horizons. We present Verify2Act, a modular verification framework that separates semantic action proposal from latent physical verification. A VLM proposes candidate plans, a latent world model (V2A-WM) imagines each of them in the DINOv2 feature space, and a dual-head critic checks the imagined rollouts for temporal consistency and goal satisfaction before anything is exec...

</details>

<details>
<summary>Share</summary>

```
Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans

Vision-Language Models (VLMs) can propose multi-step manipulation plans, but they have no grounded model of how a scene will change, and the pixel-level world models that could check those plans are slow and drift ove...

arXiv: https://arxiv.org/abs/2611.25243

#worldmodels #robotics
```

</details>

---

### [GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning](https://arxiv.org/abs/2611.25134)

**Authors:** Yangchen Zhao, Ali Payani, Caiwen Ding

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25134) | [PDF](https://arxiv.org/pdf/2611.25134)

<details>
<summary>Abstract</summary>

Visual world models enable effective short-horizon goal-conditioned planning, such as reaching nearby targets and pushing objects over short distances, by predicting candidate action outcomes and comparing their representations with a goal representation. However, extending this approach to long-horizon tasks is challenging: prediction errors accumulate over extended rollouts, while latent-space similarity to distant goals provides limited guidance for ranking candidate outcomes. Existing methods address these limitations by introducing intermediate subgoals, either generated by learned models...

</details>

<details>
<summary>Share</summary>

```
GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning

Visual world models enable effective short-horizon goal-conditioned planning, such as reaching nearby targets and pushing objects over short distances, by predicting candidate action outcomes and comparing their repre...

arXiv: https://arxiv.org/abs/2611.25134

#worldmodels #robotics
```

</details>

---

### [Search or Scoring? Diagnosing Why Visual World-Model Planners Fail](https://arxiv.org/abs/2611.25347)

**Authors:** Haoxuan Jia, Yang Liu, Shang Luo, Chenhao Wu, Zixiang Ni et al. (13 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25347) | [PDF](https://arxiv.org/pdf/2611.25347)

<details>
<summary>Abstract</summary>

Visual world models such as DINO-WM and JEPA-WM plan with an optimizer that searches for actions whose predicted outcome has the lowest cost, its distance to a goal image. A plan can thus fail in two ways: the optimizer never tries a good action that the cost would prefer (a search failure), or the cost, computed on predictions, ranks a bad action first (a scoring failure). The two need different remedies, more search or a better model, but a planner does not record which one occurred. We tell them apart by executing the optimizer's candidates, scoring a known solution with the planner's own c...

</details>

<details>
<summary>Share</summary>

```
Search or Scoring? Diagnosing Why Visual World-Model Planners Fail

Visual world models such as DINO-WM and JEPA-WM plan with an optimizer that searches for actions whose predicted outcome has the lowest cost, its distance to a goal image.

arXiv: https://arxiv.org/abs/2611.25347

#worldmodels #robotics
```

</details>

---

### [PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction](https://arxiv.org/abs/2611.24999)

**Authors:** Ziyuan Qin, Yang Qiao, Summer B. Frandsen, Michael T. Treadway, Liang Zhao

**Published:** 2026-11-18 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24999) | [PDF](https://arxiv.org/pdf/2611.24999)

<details>
<summary>Abstract</summary>

Understanding how stable psychometric traits and time-varying states jointly inform behavior is an important problem in computational behavioral science. Existing personalized agents commonly condition actions directly on a static profile, leaving realized state transitions unused as an explicit source of supervision. We introduce a profile-conditioned state world model that uses observed environment--behavior state transitions to learn transition-informed representations for behavioral prediction. During training, a posterior encoder quantizes realized transitions, while a prior predicts the...

</details>

<details>
<summary>Share</summary>

```
PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction

Understanding how stable psychometric traits and time-varying states jointly inform behavior is an important problem in computational behavioral science.

arXiv: https://arxiv.org/abs/2611.24999

#worldmodels #robotics
```

</details>

---
