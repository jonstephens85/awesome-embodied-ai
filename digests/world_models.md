# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-20 00:48 UTC

**Papers shown:** 49 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)

**Authors:** Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20609) | [PDF](https://arxiv.org/pdf/2610.20609) | [Project Page](https://safedrive-vla.github.io/SafeDriveVLA/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose. We present the first benchmark suite that evaluates navigation following and conflict awareness together, along with adversarial rob...

</details>

<details>
<summary>Share</summary>

```
SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-f...

arXiv: https://arxiv.org/abs/2610.20609
Project page: https://safedrive-vla.github.io/SafeDriveVLA/

#worldmodels #robotics
```

</details>

---

### [Orbia: Do Generated Videos Form a Consistent 3D World?](https://arxiv.org/abs/2610.20693)

**Authors:** Dongyue Lu, Guian Fang, Hur Lim, Yonggang Wu, Yanrong Wang et al. (23 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20693) | [PDF](https://arxiv.org/pdf/2610.20693) | [Project Page](https://orbia-bench.github.io/) | [Code](https://github.com/worldbench/Orbia)

<details>
<summary>Abstract</summary>

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world. Existing benchmarks assess selected geometric properties or use vision-language models to judge memory and consistency, leaving systematic 3D evaluation underexplored. We introduce Orbia, the first benchmark dedicated to a systematic and comprehensive evaluation of 3D consistency in interactive world models. Through controlled exploration and revisit, we organize the evaluation into three dimensions: input preservation, genera...

</details>

<details>
<summary>Share</summary>

```
Orbia: Do Generated Videos Form a Consistent 3D World?

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world.

arXiv: https://arxiv.org/abs/2610.20693
Project page: https://orbia-bench.github.io/
Code: https://github.com/worldbench/Orbia

#worldmodels #robotics
```

</details>

---

### [Back on Track: Deployment-time Policy Improvement via World Model Planning](https://arxiv.org/abs/2610.19579)

**Authors:** Colton Crosby, Hao Wang, Mac Schwager, Somil Bansal

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19579) | [PDF](https://arxiv.org/pdf/2610.19579) | [Project Page](https://policy-improvement-wm.pages.dev/)

<details>
<summary>Abstract</summary>

State-of-the-art visuomotor policies are increasingly capable of executing complex tasks, yet can fail during deployment in ways they cannot predict or recover from on their own. Improving their performance and robustness typically requires collecting more data, retraining, or modifying the policy architecture, all of which are time- and resource-intensive in practice. We instead propose an offline-trained monitoring-and-intervention framework that improves a policy during deployment using only black-box query access. From a limited set of labeled on-policy rollouts, we learn a policy-conditio...

</details>

<details>
<summary>Share</summary>

```
Back on Track: Deployment-time Policy Improvement via World Model Planning

State-of-the-art visuomotor policies are increasingly capable of executing complex tasks, yet can fail during deployment in ways they cannot predict or recover from on their own.

arXiv: https://arxiv.org/abs/2610.19579
Project page: https://policy-improvement-wm.pages.dev/

#worldmodels #robotics
```

</details>

---

### [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](https://arxiv.org/abs/2610.18447)

**Authors:** Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo et al. (11 authors)

**Published:** 2026-10-13 (updated 2026-10-14) | **Categories:** cs.AI, cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18447) | [PDF](https://arxiv.org/pdf/2610.18447) | [Project Page](https://thinkercosmos.ubtrobot.com/thinker-wm)

<details>
<summary>Abstract</summary>

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and generates RGB, metric depth, and robot action through a shared intermediate Unified Dynamics Transformer...

</details>

<details>
<summary>Share</summary>

```
Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support.

arXiv: https://arxiv.org/abs/2610.18447
Project page: https://thinkercosmos.ubtrobot.com/thinker-wm

#worldmodels #robotics
```

</details>

---

### [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826)

**Authors:** Haoyi Duan, Liliang Chen, Nan Wang, Yang Zhang, Yuhang Lu et al. (16 authors)

**Published:** 2026-10-13 (updated 2026-10-16) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18826) | [PDF](https://arxiv.org/pdf/2610.18826) | [Project Page](https://worldoracle-benchmark.github.io/)

<details>
<summary>Abstract</summary>

We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions. Given the same initial observation and low-level action sequence, WorldOracle asks whether a predicted rollout reproduces what happens in the real world, including physical consequences and task-state transitions. We evaluate models along four complementary dimensions: physical state correctness, interaction spatial alignment, key interaction area fidelity, and multi-view action coherence. To support this evaluation, we curate real-world training...

</details>

<details>
<summary>Share</summary>

```
WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions

We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions.

arXiv: https://arxiv.org/abs/2610.18826
Project page: https://worldoracle-benchmark.github.io/

#worldmodels #robotics
```

</details>

---

### [GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations](https://arxiv.org/abs/2610.22708)

**Authors:** Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande

**Published:** 2026-10-15 | **Categories:** cs.AI, cs.CL | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22708) | [PDF](https://arxiv.org/pdf/2610.22708) | [Code](https://github.com/patronus-ai/globebench)

<details>
<summary>Abstract</summary>

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check whether models can predict the environment's response to a specific action given the full agent trajectory by understanding earlier state changes, following environment rules, and predic...

</details>

<details>
<summary>Share</summary>

```
GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases.

arXiv: https://arxiv.org/abs/2610.22708
Code: https://github.com/patronus-ai/globebench

#worldmodels #robotics
```

</details>

---

### [Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction](https://arxiv.org/abs/2610.19212)

**Authors:** Anton Arapin, Aditya Singh, Yixin Wang, Jun Gao, Bernadette Bucher

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19212) | [PDF](https://arxiv.org/pdf/2610.19212) | [Project Page](https://anton-arapin.github.io/d3wm-site)

<details>
<summary>Abstract</summary>

World models of visual information predict future image frames conditioned on given action sequences. This predicted scene evolution is driven by deterministic changes such as controlled motion on a robot platform, as well as stochastic changes such as rendering of manipulated objects or previously occluded regions. Our key insight is that the spatial location of these stochastic changes is itself learnable. We leverage this insight by jointly regressing both the deterministic next-state prediction and the spatial uncertainty map, then using the uncertainty map to guide a conditional diffusion...

</details>

<details>
<summary>Share</summary>

```
Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction

World models of visual information predict future image frames conditioned on given action sequences.

arXiv: https://arxiv.org/abs/2610.19212
Project page: https://anton-arapin.github.io/d3wm-site

#worldmodels #robotics
```

</details>

---

### [BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL](https://arxiv.org/abs/2610.23127)

**Authors:** Liyun Yan, Haoyang Li, Yang Zhang, Jialing Zhu, Zhanxiang Cao et al. (14 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.23127) | [PDF](https://arxiv.org/pdf/2610.23127) | [Project Page](https://ylyem9x.github.io/BeJEPA-project)

<details>
<summary>Abstract</summary>

Humanoid control requires coordinating whole-body posture with position and heading in the world frame. Mainstream controllers imitate trajectories in the root frame, but struggle to regain the target world pose after displacement. We introduce BeJEPA, a goal-conditioned Behavior World Model learned through unsupervised reinforcement learning from human motion priors and robot interaction. BeJEPA learns a shared representation of body configuration and world placement through a joint-embedding predictive architecture (JEPA). A Dynamic Predictor predicts the next state embedding under an action...

</details>

<details>
<summary>Share</summary>

```
BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL

Humanoid control requires coordinating whole-body posture with position and heading in the world frame.

arXiv: https://arxiv.org/abs/2610.23127
Project page: https://ylyem9x.github.io/BeJEPA-project

#worldmodels #robotics
```

</details>

---

### [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363)

**Authors:** Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li et al. (14 authors)

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "action-conditioned video" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22363) | [PDF](https://arxiv.org/pdf/2610.22363) | [Project Page](https://p3-wam.pages.dev/)

<details>
<summary>Abstract</summary>

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D acti...

</details>

<details>
<summary>Share</summary>

```
Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perc...

arXiv: https://arxiv.org/abs/2610.22363
Project page: https://p3-wam.pages.dev/

#worldmodels #robotics
```

</details>

---

### [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](https://arxiv.org/abs/2610.19201)

**Authors:** Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19201) | [PDF](https://arxiv.org/pdf/2610.19201) | [Project Page](https://research.nvidia.com/labs/sil/projects/lidarverse)

<details>
<summary>Abstract</summary>

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors. Existing LiDAR simulators largely follow one of two complementary paradigms: reconstruction-based methods preserve the geometry of a captured scene but require lengthy per-scene optimization, whereas generative methods amortize learning across data but lack the consistency needed for long-horizon rollouts. LidarVerse brings both paradigms into a single, unified conditional generative framework. A universal tokenizer maps LiDAR range sequences into a shared latent space, where a bidirect...

</details>

<details>
<summary>Share</summary>

```
Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.

arXiv: https://arxiv.org/abs/2610.19201
Project page: https://research.nvidia.com/labs/sil/projects/lidarverse

#worldmodels #robotics
```

</details>

---

### [Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](https://arxiv.org/abs/2610.18991)

**Authors:** Nolan Fey, Khai Nguyen, Yash Prabhu, Gabriel B. Margolis, Pulkit Agrawal

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18991) | [PDF](https://arxiv.org/pdf/2610.18991) | [Project Page](https://contact-uan.csail.mit.edu/)

<details>
<summary>Abstract</summary>

Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness to impacts. This failure can arise from actuator sim-to-real gaps because forces depend on actuator torques. We introduce Contact-UAN, a residual world model that preserves a simulator's physics priors while correcting actuator dynamics to align simulated rollouts with recorded hardware rollouts. For humanoid motion with contact, this requires contact-consistent replay: if hardwar...

</details>

<details>
<summary>Share</summary>

```
Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control

Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness...

arXiv: https://arxiv.org/abs/2610.18991
Project page: https://contact-uan.csail.mit.edu/

#worldmodels #robotics
```

</details>

---

### [ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18852)

**Authors:** Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen et al. (19 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18852) | [PDF](https://arxiv.org/pdf/2610.18852) | [Project Page](https://force-wam.github.io/)

<details>
<summary>Abstract</summary>

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions. Task-agnostic play provides broader experience of contact dynamics without specifying task goals. To fully leverage these two types of data, we introduce ForceWAM, a force world action model that decouples knowledge of task-compatible interaction outcomes from knowledge of how local actions change contact. A world model learns from successful demonstrations to jointly predict future video and six-axis force/torque trajectories. Together, these futu...

</details>

<details>
<summary>Share</summary>

```
ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions.

arXiv: https://arxiv.org/abs/2610.18852
Project page: https://force-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation](https://arxiv.org/abs/2610.18135)

**Authors:** Yifei Yang, Zehua Fan, Zike Yan, Zhongyu Li, Yan Wang

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.18135) | [PDF](https://arxiv.org/pdf/2610.18135)

<details>
<summary>Abstract</summary>

World-model-based visual navigation enables action planning by predicting future states under candidate trajectories. However, long-horizon rollout remains challenging: models are often trained with ground-truth visual histories but deployed in closed-loop prediction, and evaluating many candidates with step-by-step rollout is computationally expensive. We propose SkipWorld, a latent skip planning framework for efficient visual navigation. SkipWorld introduces three components: (i) Latent AutoRoll, which trains a world model to recursively roll out future states in latent space, reducing the m...

</details>

<details>
<summary>Share</summary>

```
SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation

World-model-based visual navigation enables action planning by predicting future states under candidate trajectories.

arXiv: https://arxiv.org/abs/2610.18135

#worldmodels #robotics
```

</details>

---

### [PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents](https://arxiv.org/abs/2610.20240)

**Authors:** Siqi Yang, Yimu Wang, Ziqi Cai, Chengxuan Zhu, Shuchen Weng et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20240) | [PDF](https://arxiv.org/pdf/2610.20240) | [Project Page](https://pawa.siki.moe)

<details>
<summary>Abstract</summary>

A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view. A point-of-view (POV) video captures such changes only after they enter its field of view, whereas panoramic video records the surroundings in every viewing direction and has served as an intermediate representation of the world state in recent world models. Learning this task therefore requires synchronized POV and panoramic videos of interacting players together with their actions, yet no existing dataset provides this...

</details>

<details>
<summary>Share</summary>

```
PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents

A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view.

arXiv: https://arxiv.org/abs/2610.20240
Project page: https://pawa.siki.moe

#worldmodels #robotics
```

</details>

---

### [One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models](https://arxiv.org/abs/2610.19375)

**Authors:** Joshua Cheung, Zhang He

**Published:** 2026-10-14 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.19375) | [PDF](https://arxiv.org/pdf/2610.19375)

<details>
<summary>Abstract</summary>

Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model. In model-based RL this assumption is known to be unreliable; we ask whether it also fails for latent world models, where the training target is the model's own embedding and the loss is not expressed in interpretable units. We introduce a frozen-decoder protocol reporting one-step error in physical units, decomposed into the part already present in the encoder's representation and the part the predictor adds. A...

</details>

<details>
<summary>Share</summary>

```
One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models

Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model.

arXiv: https://arxiv.org/abs/2610.19375

#worldmodels #robotics
```

</details>

---

### [Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold](https://arxiv.org/abs/2610.19007)

**Authors:** Anton Arapin, Chahyon Ku, Bernadette Bucher

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19007) | [PDF](https://arxiv.org/pdf/2610.19007) | [Project Page](https://anton-arapin.github.io/action-jets-site)

<details>
<summary>Abstract</summary>

World models are a powerful means of reasoning and planning, but many of these action-conditioned predictive models are high dimensional and computationally expensive. These challenges limit the number of action candidates that can be evaluated by a planner. We show that this cost is avoidable for planners over short horizons, which only require local information with respect to the current state. For a fixed state, the frames reachable by varying a low-dimensional action (a camera movement or an end-effector command) lie on a low-dimensional manifold. We estimate the local shape of that manif...

</details>

<details>
<summary>Share</summary>

```
Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold

World models are a powerful means of reasoning and planning, but many of these action-conditioned predictive models are high dimensional and computationally expensive.

arXiv: https://arxiv.org/abs/2610.19007
Project page: https://anton-arapin.github.io/action-jets-site

#worldmodels #robotics
```

</details>

---

### [RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control](https://arxiv.org/abs/2610.17584)

**Authors:** Binghan Wu, Kai Zeng, Kai Yang, Ya-Qin Zhang, Joseph Sifakis et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.17584) | [PDF](https://arxiv.org/pdf/2610.17584)

<details>
<summary>Abstract</summary>

Operational mobile networks are rich in observations but poor in interventions: they continuously generate large volumes of passive telemetry, while controlled action--response trajectories remain comparatively scarce and costly to collect. This observation--intervention asymmetry is a central obstacle to building practical world models for RAN control. We address this problem with RAN-JEPA, an action-conditioned world model that separates representation learning from intervention learning. The model first learns a predictive latent representation from observation-only network data, adapts tha...

</details>

<details>
<summary>Share</summary>

```
RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control

Operational mobile networks are rich in observations but poor in interventions: they continuously generate large volumes of passive telemetry, while controlled action--response trajectories remain comparatively scarce...

arXiv: https://arxiv.org/abs/2610.17584

#worldmodels #robotics
```

</details>

---

### [AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation](https://arxiv.org/abs/2610.23396)

**Authors:** Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yanwei Fu

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23396) | [PDF](https://arxiv.org/pdf/2610.23396)

<details>
<summary>Abstract</summary>

Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects. However, strong results in structured environments do not automatically transfer to open-world conditions, where clutter, occlusion, and changing viewpoints can obscure the spatial relationships required for action. To address this perceptual gap, a virtual active-perception paradigm is introduced. AWAM, an Active World-Action Model actively plans where to observe and imagines what will be seen along the planned trajectory before acting. Task-related v...

</details>

<details>
<summary>Share</summary>

```
AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation

Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects.

arXiv: https://arxiv.org/abs/2610.23396

#worldmodels #robotics
```

</details>

---

### [DriveWorld3D Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving](https://arxiv.org/abs/2610.22450)

**Authors:** Wei Wang, Yiru Veronika Wang, Yihan Wang, Zihao Li, Xiaohui Liang

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.22450) | [PDF](https://arxiv.org/pdf/2610.22450)

<details>
<summary>Abstract</summary>

Three dimensional modeling for autonomous driving must continuously estimate road geometry, obstacle occupancy, traffic participant behavior, and observational uncertainty under limited computational resources. Existing reconstruction methods can synthesize realistic novel views, but visual fidelity does not sufficiently characterize the geometric reliability required for driving. Generative world models can expand scenarios and predict future observations, yet may introduce content unsupported by measurements. We propose DriveWorld3D, a framework combining temporal video learning, measurement...

</details>

<details>
<summary>Share</summary>

```
DriveWorld3D Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving

Three dimensional modeling for autonomous driving must continuously estimate road geometry, obstacle occupancy, traffic participant behavior, and observational uncertainty under limited computational resources.

arXiv: https://arxiv.org/abs/2610.22450

#worldmodels #robotics
```

</details>

---

### [MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models](https://arxiv.org/abs/2610.21686)

**Authors:** Yi Qiao, Maolin Zheng, Haoran Sun, Lujia Dong, Wenzhao Lian

**Published:** 2026-10-15 (updated 2026-10-16) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.21686) | [PDF](https://arxiv.org/pdf/2610.21686)

<details>
<summary>Abstract</summary>

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action. Yet most monitoring methods are reactive, identifying anomalies only after they become observable. Anticipating such anomalies is challenging because visual observations only partially reveal physical interaction, while planned actions describe intended motion rather than their actual physical consequences. We address this problem with MAIA, a multimodal framework for anomaly anticipation. Its vision-action-force world model learns nominal interaction dynamics and predicts the visual...

</details>

<details>
<summary>Share</summary>

```
MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action.

arXiv: https://arxiv.org/abs/2610.21686

#worldmodels #robotics
```

</details>

---

### [LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction](https://arxiv.org/abs/2610.18093)

**Authors:** Jun Tian, Hao Wu, Ruo Chen, Yili Liao, Hongyi Lin et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.18093) | [PDF](https://arxiv.org/pdf/2610.18093)

<details>
<summary>Abstract</summary>

Wheel-legged robots operating in outdoor spaces shared with humans require accurate perception, socially compliant navigation, future-scene reasoning, and scene reconstruction. However, existing datasets typically support these capabilities in isolation and rarely provide dense spatial and behavior-level supervision on real wheel-legged platforms. We introduce LynxScenes, a large-scale real-world dataset and benchmark collected with a LYNX M20 wheel-legged robot. It contains approximately 100K 30-s navigation clips spanning 833.6 h and 3,294.7 km, with 3.0M annotated frames. The synchronized r...

</details>

<details>
<summary>Share</summary>

```
LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction

Wheel-legged robots operating in outdoor spaces shared with humans require accurate perception, socially compliant navigation, future-scene reasoning, and scene reconstruction.

arXiv: https://arxiv.org/abs/2610.18093

#worldmodels #robotics
```

</details>

---

### [From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction](https://arxiv.org/abs/2610.17630)

**Authors:** Ruo Chen, Jiahua Pang, Yingjie Niu, Hongyi Lin, Jun Tian et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.17630) | [PDF](https://arxiv.org/pdf/2610.17630)

<details>
<summary>Abstract</summary>

In outdoor environments, varying terrain and contact conditions can cause identical action commands to produce different motion outcomes for quadruped robots. Predicting these outcomes is essential for reliable navigation and informed path selection. Existing video world models can generate visually plausible futures, yet often struggle to capture robot dynamics and terrain interactions, leading to overly optimistic predictions of action outcomes. We present DR-WM, a physically consistent world model that incorporates robot-terrain contact dynamics to predict the consequences of quadruped acti...

</details>

<details>
<summary>Share</summary>

```
From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction

In outdoor environments, varying terrain and contact conditions can cause identical action commands to produce different motion outcomes for quadruped robots.

arXiv: https://arxiv.org/abs/2610.17630

#worldmodels #robotics
```

</details>

---

### [Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability](https://arxiv.org/abs/2610.23722)

**Authors:** Qingshi Wang

**Published:** 2026-10-16 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23722) | [PDF](https://arxiv.org/pdf/2610.23722)

<details>
<summary>Abstract</summary>

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This paper introduces the Mental World Model (MWM) and its implementation, the Multi-Branch Mental Evolutio...

</details>

<details>
<summary>Share</summary>

```
Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence.

arXiv: https://arxiv.org/abs/2610.23722

#worldmodels #robotics
```

</details>

---

### [Order-Consistent Latent Geometry for Reliable Short-Horizon Planning in World Models](https://arxiv.org/abs/2610.18570)

**Authors:** Junlin Wu, Wen Fan, Dandan Zhang

**Published:** 2026-10-13 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.18570) | [PDF](https://arxiv.org/pdf/2610.18570)

<details>
<summary>Abstract</summary>

Latent planners often rank candidate action sequences by terminal Euclidean distance to a goal latent. Exact agreement with transition distance would make this score ideal, but is stronger than planning requires: along a transition-shortest rollout, the essential requirement is that latent distance does not reverse true transition progress. We show that this pathwise no-reversal requirement is precisely the classical self-approaching condition. To the best of our knowledge, we are the first to identify self-approachingness as a planner-facing compatibility condition for terminal Euclidean late...

</details>

<details>
<summary>Share</summary>

```
Order-Consistent Latent Geometry for Reliable Short-Horizon Planning in World Models

Latent planners often rank candidate action sequences by terminal Euclidean distance to a goal latent.

arXiv: https://arxiv.org/abs/2610.18570

#worldmodels #robotics
```

</details>

---

### [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](https://arxiv.org/abs/2610.18289)

**Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18289) | [PDF](https://arxiv.org/pdf/2610.18289) | [Code](https://github.com/Fantasy-AMAP/LongForcing)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models have emerged as a foundation for long-horizon world rollout. However, when extended far beyond their training windows, these models suffer from progressive drift: visual quality deteriorates, motion becomes inconsistent, and object identity gradually collapses as generated frames are recursively reused as context. We study a supervision-horizon gap: short-horizon distillation leaves later rollout states without direct supervision. We show that matching short-window marginals need not determine long-horizon behavior, while longer on-policy trajectories expo...

</details>

<details>
<summary>Share</summary>

```
LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout

Autoregressive video diffusion models have emerged as a foundation for long-horizon world rollout.

arXiv: https://arxiv.org/abs/2610.18289
Code: https://github.com/Fantasy-AMAP/LongForcing

#worldmodels #robotics
```

</details>

---

### [Beyond Action Prediction: Learning Search-Free Planning in Latent Space](https://arxiv.org/abs/2610.23615)

**Authors:** Guanchen Du, Jinhao Du, Yanpeng Sun, Shan Zhang, Na Zhao et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23615) | [PDF](https://arxiv.org/pdf/2610.23615)

<details>
<summary>Abstract</summary>

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representations encode action-relevant information nor that predicted actions are consistent with the learned la...

</details>

<details>
<summary>Share</summary>

```
Beyond Action Prediction: Learning Search-Free Planning in Latent Space

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control.

arXiv: https://arxiv.org/abs/2610.23615

#worldmodels #robotics
```

</details>

---

### [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](https://arxiv.org/abs/2610.23156)

**Authors:** Yueyang Weng, Xiaopeng Zhang, Yuxi Ou, Yongjin Mu, Chengzhi Zhao et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23156) | [PDF](https://arxiv.org/pdf/2610.23156)

<details>
<summary>Abstract</summary>

World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks. However, existing image-based and dense 3D world models do not explicitly impose object-level rigid motion, leaving rigid-object geometry preservation to be learned implicitly and making multi-step rollouts susceptible to shape drift or object-level motion inconsistency. To address this, we propose ORD-WM, a 3D world model that learns object-centric rigid dynamics for robotic manipulation. ORD-WM learns a vector-neuron variational autoencoder supervised by signed...

</details>

<details>
<summary>Share</summary>

```
ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation

World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks.

arXiv: https://arxiv.org/abs/2610.23156

#worldmodels #robotics
```

</details>

---

### [TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control](https://arxiv.org/abs/2610.21922)

**Authors:** Menghao Yin, Jiaju Yin, Xiyue Dong, Lixin Xu, Zhenhui Zhang et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21922) | [PDF](https://arxiv.org/pdf/2610.21922)

<details>
<summary>Abstract</summary>

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states. These limitations hinder learning from action-free videos and can encourage overfitting to demonstration conditions, weakening generalization and robustness. We present TS-WAM, a lightweight Teacher-Student World-Action Model that addresses these challenges through self-supervised temporal learning and explicit future prediction. Its vlm-jepa framework learns from heterogeneous data, including robot demonstrations and action-free human videos, usi...

</details>

<details>
<summary>Share</summary>

```
TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states.

arXiv: https://arxiv.org/abs/2610.21922

#worldmodels #robotics
```

</details>

---

### [T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](https://arxiv.org/abs/2610.22364)

**Authors:** Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang et al. (12 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22364) | [PDF](https://arxiv.org/pdf/2610.22364)

<details>
<summary>Abstract</summary>

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z for test-time optimization of environment latents, which augments a robotic world model with a learnable environment latent to condition world predictions. This compact latent captures underlying environmental variation without supervision of what environmental factors exist or what values they take...

</details>

<details>
<summary>Share</summary>

```
T2-z: Test-Time Optimization of Environment Latents for Robotic World Models

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties...

arXiv: https://arxiv.org/abs/2610.22364

#worldmodels #robotics
```

</details>

---

### [Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift](https://arxiv.org/abs/2610.22041)

**Authors:** Danqi Zhao, Keyu Chen, Wenchao Sun, Minglei Huang, Jianhe Zhang et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22041) | [PDF](https://arxiv.org/pdf/2610.22041)

<details>
<summary>Abstract</summary>

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training. At deployment, a different downstream controller may execute the same planned trajectory differently, creating a planning-execution gap between the frozen model's imagined future and actual execution. A natural remedy is to replace the planned trajectory with its predicted or observed execution. However, we find that better execution fidelity does not necessarily yield better decisions: directly substituting predicted execu...

</details>

<details>
<summary>Share</summary>

```
Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training.

arXiv: https://arxiv.org/abs/2610.22041

#worldmodels #robotics
```

</details>

---

### [Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](https://arxiv.org/abs/2610.20134)

**Authors:** Kiyanoush Nazari, Luchen Li, Haoshu Fang, Nima Fazeli, Zhibin Li et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.20134) | [PDF](https://arxiv.org/pdf/2610.20134)

<details>
<summary>Abstract</summary>

Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation. Beyond its traditional role in contact detection and reactive control, touch is increasingly used to learn transferable representations, condition manipulation policies, and support embodied physical reasoning. Yet existing surveys largely emphasize tactile hardware and perception, leaving the rapid shift toward learning-based tactile manipulation insufficiently synthesized. This paper reviews tactile-guided skill learning from a learning-centric perspective, organized by the functional role of touch a...

</details>

<details>
<summary>Share</summary>

```
Tactile-Guided Robot Learning: From Representation Learning to Foundation Models

Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation.

arXiv: https://arxiv.org/abs/2610.20134

#worldmodels #robotics
```

</details>

---

### [RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories](https://arxiv.org/abs/2610.18699)

**Authors:** Yunfu Deng, Sangwoo Shin, Brahma S. Pavse, Josiah P. Hanna

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.18699) | [PDF](https://arxiv.org/pdf/2610.18699)

<details>
<summary>Abstract</summary>

Evaluating robot policies before deployment typically requires producing new trajectories through real-world execution, simulators, or learned world models. These rollout-based approaches impose infrastructure requirements; simulator and world-model evaluators additionally face prediction errors that can compound over the evaluation horizon. In this paper, we study off-policy evaluation as an alternative to rollout-based robot-policy evaluation methods. Specifically, we introduce RoboFQE, an evaluator that estimates the discounted expected return of a target policy from offline robot trajector...

</details>

<details>
<summary>Share</summary>

```
RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories

Evaluating robot policies before deployment typically requires producing new trajectories through real-world execution, simulators, or learned world models.

arXiv: https://arxiv.org/abs/2610.18699

#worldmodels #robotics
```

</details>

---

### [Grid or Nodes? Probing Object Memory in World Models Under Partial Observability](https://arxiv.org/abs/2610.18637)

**Authors:** Justin McMillen, Yasin Yilmaz

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.18637) | [PDF](https://arxiv.org/pdf/2610.18637)

<details>
<summary>Abstract</summary>

A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also scores 8 points higher in view although no frame is shown, which we attribute to its write-back of its...

</details>

<details>
<summary>Share</summary>

```
Grid or Nodes? Probing Object Memory in World Models Under Partial Observability

A robot's world model must remember objects that leave the camera's view.

arXiv: https://arxiv.org/abs/2610.18637

#worldmodels #robotics
```

</details>

---

### [DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2610.17903)

**Authors:** Shuzheng Wang, Haoxuan Li, Shengzhen Li, Chenxi Wu, Yajing Sun et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.17903) | [PDF](https://arxiv.org/pdf/2610.17903)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving. However, effectively integrating both capabilities for trajectory generation remains challenging. In this work, we propose DriveWLA, a unified World-Language-Action model based on Mixture-of-Transformers (MoT) that jointly models semantic understanding, future scene dynamics, and trajectory generation. DriveWLA consists of three experts: a World Expert for future prediction, a Language Expert for semantic understanding, and an Action...

</details>

<details>
<summary>Share</summary>

```
DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving

Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving.

arXiv: https://arxiv.org/abs/2610.17903

#worldmodels #robotics
```

</details>

---

### [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](https://arxiv.org/abs/2610.17688)

**Authors:** Qihang Huang, Wenhui Huang, Collister Chua, Shiyu Fang, Zhan Chen et al. (9 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.17688) | [PDF](https://arxiv.org/pdf/2610.17688)

<details>
<summary>Abstract</summary>

Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving. However, existing occupancy-aware planners typically couple occupancy prediction and action generation through either hierarchical coupling or parallel multi-task learning. Hierarchical methods use occupancy either as a fully predicted future preceding action generation or as an action-conditioned rollout for trajectory evaluation, whereas parallel multi-task methods predict occupancy alongside planning through a separate branch or auxili...

</details>

<details>
<summary>Share</summary>

```
OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching

Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving.

arXiv: https://arxiv.org/abs/2610.17688

#worldmodels #robotics
```

</details>

---

### [Momentum: Persistent Dynamics for Video World Models](https://arxiv.org/abs/2610.23423)

**Authors:** Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel, Yilun Du, Xi Wang et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.23423) | [PDF](https://arxiv.org/pdf/2610.23423)

<details>
<summary>Abstract</summary>

Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears. Existing approaches rely on observation history, static point clouds, or image caches constructed from past frames. These representations are often expensive and, more importantly, cannot update dynamic scene content outside the field of view: generated vehicles and pedestrians may be forgotten after leaving the field of view or reappear in physically inaccurate states. We represent an evolving scene through synchronized videos from reference-camera...

</details>

<details>
<summary>Share</summary>

```
Momentum: Persistent Dynamics for Video World Models

Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears.

arXiv: https://arxiv.org/abs/2610.23423

#worldmodels #robotics
```

</details>

---

### [Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311)

**Authors:** Qiuhong Shen, Shizun Wang, Xinchao Wang

**Published:** 2026-10-15 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22311) | [PDF](https://arxiv.org/pdf/2610.22311)

<details>
<summary>Abstract</summary>

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using frustum slab correspondences from streaming geometry. Velox represents historical b...

</details>

<details>
<summary>Share</summary>

```
Velox: Spatial Memory Makes World Models Efficient

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation.

arXiv: https://arxiv.org/abs/2610.22311

#worldmodels #robotics
```

</details>

---

### [Learning Intrinsic Dynamics in Latent World Models](https://arxiv.org/abs/2610.21612)

**Authors:** Jiamin Shi, Yuanhong Zhang, Zhiyang Liu, Jiawei Sun, Jingwen Fu

**Published:** 2026-10-15 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.21612) | [PDF](https://arxiv.org/pdf/2610.21612)

<details>
<summary>Abstract</summary>

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models. However, visual variations unrelated to the underlying control process can obscure this relationship in learned representations. We investigate the connection between action predictability, defined as the ability to reconstruct an action from consecutive latent states, and the preservation of intrinsic dynamics. Our central hypothesis is that encouraging action predictability discourages representations from discarding the distinctions between different actions and their conse...

</details>

<details>
<summary>Share</summary>

```
Learning Intrinsic Dynamics in Latent World Models

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models.

arXiv: https://arxiv.org/abs/2610.21612

#worldmodels #robotics
```

</details>

---

### [Neurosymbolic Learning of Interpretable World Models](https://arxiv.org/abs/2610.19955)

**Authors:** Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini, Alessandro Daniele, Emile van Krieken

**Published:** 2026-10-14 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.19955) | [PDF](https://arxiv.org/pdf/2610.19955)

<details>
<summary>Abstract</summary>

World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about the world. We introduce Concept-Grounded World Models (CGWMs), a neurosymbolic world model design that instead learns interpretable concept representations. We learn these concepts from observations using explicit and complete knowledge, expressed in temporal logic, that specifies the valid world states and the temporal...

</details>

<details>
<summary>Share</summary>

```
Neurosymbolic Learning of Interpretable World Models

World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour.

arXiv: https://arxiv.org/abs/2610.19955

#worldmodels #robotics
```

</details>

---

### [Enhancing Latent World Models with Associative Memory](https://arxiv.org/abs/2610.19683)

**Authors:** Yuwei Sun, Siyu Zhu

**Published:** 2026-10-14 | **Categories:** cs.LG, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.19683) | [PDF](https://arxiv.org/pdf/2610.19683)

<details>
<summary>Abstract</summary>

World models trained via latent dynamics offer a scalable path for embodied planning, yet existing methods suffer from representational collapse, computational overhead, and limited long-horizon capability. We introduce a memory-enhanced latent world model that augments JEPA-style prediction with a content-addressable memory bank. Our approach learns high-level representations directly from observations, operating at multiple temporal scales within a shared latent space, and conditions predictions via adaptive layer normalization. To prevent collapse and ensure effective memory usage, we desig...

</details>

<details>
<summary>Share</summary>

```
Enhancing Latent World Models with Associative Memory

World models trained via latent dynamics offer a scalable path for embodied planning, yet existing methods suffer from representational collapse, computational overhead, and limited long-horizon capability.

arXiv: https://arxiv.org/abs/2610.19683

#worldmodels #robotics
```

</details>

---

### [Dexterity from Supervised Play](https://arxiv.org/abs/2610.22340)

**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma et al. (6 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22340) | [PDF](https://arxiv.org/pdf/2610.22340)

<details>
<summary>Abstract</summary>

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-...

</details>

<details>
<summary>Share</summary>

```
Dexterity from Supervised Play

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation?

arXiv: https://arxiv.org/abs/2610.22340

#worldmodels #robotics
```

</details>

---

### [From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion](https://arxiv.org/abs/2610.21374)

**Authors:** Bazeela Banday, Jishnu Keshavan

**Published:** 2026-10-15 | **Categories:** cs.RO, eess.SY | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.21374) | [PDF](https://arxiv.org/pdf/2610.21374)

<details>
<summary>Abstract</summary>

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable. This letter introduces a visual safety-certification paradigm that uses scale-free, depth-normalized relative motion encoded by monocular optical flow as the representation for collision-risk certification, without reconstructing obstacle position, velocity, geometry, or a metric world model. Unlike conventional optical-flow-based navigation approaches that rely on image motion to shape avoidance behavior, the proposed framework directly encodes collision-cone geo...

</details>

<details>
<summary>Share</summary>

```
From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable.

arXiv: https://arxiv.org/abs/2610.21374

#worldmodels #robotics
```

</details>

---

### [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](https://arxiv.org/abs/2610.18697)

**Authors:** Jingbo Xu, Jianjie Fang, Zhuohang Li, Zihao Song, Zhaolu Wang et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.18697) | [PDF](https://arxiv.org/pdf/2610.18697)

<details>
<summary>Abstract</summary>

World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities required by each paradigm. We propose UniW(A)M, a mixture-of-experts world-(action) model built upon di...

</details>

<details>
<summary>Share</summary>

```
UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively.

arXiv: https://arxiv.org/abs/2610.18697

#worldmodels #robotics
```

</details>

---

### [Acting Through Registers](https://arxiv.org/abs/2610.17638)

**Authors:** Yiwei Zhang, Yantai Yang, Jin Gao, Jin Lou, Andong Chen et al. (10 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.17638) | [PDF](https://arxiv.org/pdf/2610.17638)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood. We identify persistent high-norm spatial outliers in WAM representations and find that their action relevance persists even after normalization and K/V projection attenuate their extreme magnitude. Motivated by this observation, we introduce RegisterWAM, which adds learnable non-spatial registers to the world model and uses them directly for action conditioning. Registers alone do not fully eliminate spatial o...

</details>

<details>
<summary>Share</summary>

```
Acting Through Registers

World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood.

arXiv: https://arxiv.org/abs/2610.17638

#worldmodels #robotics
```

</details>

---

### [World Action Critic (WAC) Model: Joint Foresight and Criticism for Policy Learning](https://arxiv.org/abs/2610.22825)

**Authors:** Xiangteng Zhang, Haoyuan Liu, Yang Guan, Jingliang Duan, Yao Lyu et al. (10 authors)

**Published:** 2026-10-16 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22825) | [PDF](https://arxiv.org/pdf/2610.22825)

<details>
<summary>Abstract</summary>

World models have shown considerable promise in sequential decision-making by anticipating the consequences of actions and providing predictive foresight for policy learning. However, learning to reason about counterfactual actions remains challenging, since predictive objectives may underemphasize information critical for action evaluation, while unexecuted actions lack observed futures for direct supervision. To address these challenges, we propose the World Action Critic (WAC) Model, which proposes multimodal action candidates and jointly learns candidate-conditioned future prediction and c...

</details>

<details>
<summary>Share</summary>

```
World Action Critic (WAC) Model: Joint Foresight and Criticism for Policy Learning

World models have shown considerable promise in sequential decision-making by anticipating the consequences of actions and providing predictive foresight for policy learning.

arXiv: https://arxiv.org/abs/2610.22825

#worldmodels #robotics
```

</details>

---

### [Is a Linear Probe Evidence of a Linear Representation?](https://arxiv.org/abs/2610.22655)

**Authors:** Nadir Kutluozen, Christian Internò, David Klindt

**Published:** 2026-10-15 | **Categories:** stat.ML, cs.CV, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22655) | [PDF](https://arxiv.org/pdf/2610.22655)

<details>
<summary>Abstract</summary>

The linear representation hypothesis holds that pretrained vision models encode generative factors as linearly decodable directions in feature space, and comes with a standard methodology: train a linear probe, declare a factor represented if accuracy is high. We show this test is too permissive. Asymptotically, any sufficiently rich feature map, including a random one, admits a linear readout, so high probe accuracy is consistent with two very different geometries: a true linear world model, where the latent-aligned subspace dominates the representation, or a kernel machine, where the latents...

</details>

<details>
<summary>Share</summary>

```
Is a Linear Probe Evidence of a Linear Representation?

The linear representation hypothesis holds that pretrained vision models encode generative factors as linearly decodable directions in feature space, and comes with a standard methodology: train a linear probe, declar...

arXiv: https://arxiv.org/abs/2610.22655

#worldmodels #robotics
```

</details>

---

### [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220)

**Authors:** Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.20220) | [PDF](https://arxiv.org/pdf/2610.20220)

<details>
<summary>Abstract</summary>

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show it can be made dramatically more efficient. Pushing this efficiency to its extreme, we reduce trajectory supervision to a single sample, the strictest setting possible, and find that...

</details>

<details>
<summary>Share</summary>

```
Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models.

arXiv: https://arxiv.org/abs/2610.20220

#worldmodels #robotics
```

</details>

---

### [SceneAE: Scene Generation and Reconstruction in Queryable 3D-Anchored Latent Space](https://arxiv.org/abs/2610.19708)

**Authors:** Shuofeng Sun, Wenzhao Zheng, Yunpeng Zhang, Yi Wu, Linqing Zhao et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.19708) | [PDF](https://arxiv.org/pdf/2610.19708)

<details>
<summary>Abstract</summary>

Recent video world models have increasingly adopted 3D memory mechanisms to integrate historical observations into a lightweight and persistent scene representation. This naturally raises a complementary question: if 3D representations can serve as an effective mechanism for memorizing observed scenes, can they also be directly used as the latent space for reconstructing and generating scenes? Motivated by this idea, we represent a scene as a compact and unstructured 3D-anchored latent space (\textbf{SceneAE}). Each latent combines an explicit 3D position with an implicit content feature and i...

</details>

<details>
<summary>Share</summary>

```
SceneAE: Scene Generation and Reconstruction in Queryable 3D-Anchored Latent Space

Recent video world models have increasingly adopted 3D memory mechanisms to integrate historical observations into a lightweight and persistent scene representation.

arXiv: https://arxiv.org/abs/2610.19708

#worldmodels #robotics
```

</details>

---

### [AffectWorld: Benchmarking Emotion-Driven Future World Prediction](https://arxiv.org/abs/2610.18305)

**Authors:** Changhao Song, Yacong Chen, Hui Gao, Yazhou Zhang, Peng Zhang

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.18305) | [PDF](https://arxiv.org/pdf/2610.18305)

<details>
<summary>Abstract</summary>

The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotions shape human actions. However, existing world model benchmarks primarily assess physical plausibility and perceptual quality, leaving emotion-driven world evolution largely untested.We introduce AffectWorld, a benchmark that evaluates the chain Emotion-Action-World State through three tasks: World-State Consistency, Emotion-Action Consistency, and Causal Consistency. It comprises 1,498 everyday video samples annotated with plausible emotions, act...

</details>

<details>
<summary>Share</summary>

```
AffectWorld: Benchmarking Emotion-Driven Future World Prediction

The world encompasses both physical environments and human actors.

arXiv: https://arxiv.org/abs/2610.18305

#worldmodels #robotics
```

</details>

---
