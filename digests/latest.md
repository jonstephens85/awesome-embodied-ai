# What's New

Papers discovered in the run at **2026-09-10 18:57 UTC**.

**New this run:** 16

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (8)

### [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2609.10405)

**Authors:** Haochen Niu, Shengye Dong, Hao Liu, Peiwen Lin, Wang Chuang

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10405) | [PDF](https://arxiv.org/pdf/2609.10405)

<details>
<summary>Abstract</summary>

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions. Yet Flow Matching--based vision-language-action (VLA) models typically generate actions in temporal coordinates, without explicitly modeling or systematically leveraging this frequency heterogeneity. We introduce \emph{FreqFM}, a frequency-conditioned Flow Matching framework for VLA models. It raises action frequency from an implicit trajectory property to an explicit conditioning dimension that spans the entire generation pipeline. Con...

</details>

<details>
<summary>Share</summary>

```
Frequency-Conditioned Flow Matching for Vision-Language-Action Models

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions.

arXiv: https://arxiv.org/abs/2609.10405

#VLA #robotics
```

</details>

---

### [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925)

**Authors:** Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang et al. (6 authors)

**Published:** 2026-09-09 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09925) | [PDF](https://arxiv.org/pdf/2609.09925)

<details>
<summary>Abstract</summary>

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entangles them. Second, cross-phase geometry: motions of different phases (reach, contact, grasp adjustme...

</details>

<details>
<summary>Share</summary>

```
Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass.

arXiv: https://arxiv.org/abs/2609.09925

#VLA #robotics
```

</details>

---

### [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)

**Authors:** Yanzhe Chen, Zechen Bai, Zhijun Cao, Wenzheng Zeng, Kevin Qinghong Lin et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10522) | [PDF](https://arxiv.org/pdf/2609.10522) | [Project Page](https://showlab.github.io/Show-Harness)

<details>
<summary>Abstract</summary>

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging. We present Show-Harness, an Embodied Harness that enables VLMs to "play" robots through a compact semantic interface linking intent to action. Show-Harness exposes discrete semantic action units that VLMs can naturally reason over, while embodiment-specific interpreters deterministically ground them into local robot actions, keeping the VLM directly responsible for fine-grained physical decisions. Through the same interface, Show-Harness...

</details>

<details>
<summary>Share</summary>

```
Show-Harness: Just a VLM Agent Can Play Robots

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging.

arXiv: https://arxiv.org/abs/2609.10522
Project page: https://showlab.github.io/Show-Harness

#VLA #robotics
```

</details>

---

### [RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility](https://arxiv.org/abs/2609.10021)

**Authors:** Runze Xu, Yuanfan Xu, Cuijie Xu, Shuang Dai, Yining Li et al. (7 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10021) | [PDF](https://arxiv.org/pdf/2609.10021)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data. Unlike pretraining, post-training targets task- and embodiment-specific adaptation, making it particularly sensitive to data quality. In practice, collected robot datasets often contain heterogeneous errors, including execution mistakes, sensor drift, and timestamp misalignment, which can impair post-training and policy performance. Manual inspection is costly, while existing data-cleaning...

</details>

<details>
<summary>Share</summary>

```
RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data.

arXiv: https://arxiv.org/abs/2609.10021

#VLA #robotics
```

</details>

---

### [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808)

**Authors:** M. Yunus Seker, Shobhit Aggarwal, Ruwan Wickramarachchi, Jonathan Francis, Oliver Kroemer

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.09808) | [PDF](https://arxiv.org/pdf/2609.09808) | [Project Page](https://gta2-project.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation tasks are often decomposed into behaviors or skills. However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills. As a result, these behaviors can remain too coarse to expose the geometric, control, and scene-dependent decisions required for execution. We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable object-centric task-axis components. Rather than predicting actions end-to-end or composing fixed task-le...

</details>

<details>
<summary>Share</summary>

```
GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes

Robotic manipulation tasks are often decomposed into behaviors or skills.

arXiv: https://arxiv.org/abs/2609.09808
Project page: https://gta2-project.github.io/

#VLA #robotics
```

</details>

---

### [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](https://arxiv.org/abs/2609.09591)

**Authors:** Zhuodong Liu, Xiangyu Li, Chunhong Yuan, Hongyang Du, Bodong Shang et al. (8 authors)

**Published:** 2026-09-09 | **Categories:** eess.SP, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09591) | [PDF](https://arxiv.org/pdf/2609.09591)

<details>
<summary>Abstract</summary>

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing. Vision-language-action (VLA) models offer a foundation by integrating visual perception, language understanding, and action generation into a unified closed-loop policy. However, training and adapting VLA models to distributed robotic agents introduce challenges in privacy protection, communication efficiency, and model heterogeneity. Existing federated lea...

</details>

<details>
<summary>Share</summary>

```
Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, a...

arXiv: https://arxiv.org/abs/2609.09591

#VLA #robotics
```

</details>

---

### [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](https://arxiv.org/abs/2609.10243)

**Authors:** Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10243) | [PDF](https://arxiv.org/pdf/2609.10243)

<details>
<summary>Abstract</summary>

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world. Yet methods that perform well in simulation can degrade substantially on real robots, especially in long-horizon deformable-object manipulation, where policies must track changing states and execute reliable multi-stage bimanual interactions. Existing real-robot benchmarks mainly focus on short-horizon rigid-object tasks and offer limited coverage of long-horizon deformable manipulation. We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with gar...

</details>

<details>
<summary>Share</summary>

```
FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world.

arXiv: https://arxiv.org/abs/2609.10243

#VLA #robotics
```

</details>

---

### [No Free Checker: A Survey of Verifiers for Robot Policies](https://arxiv.org/abs/2609.09250)

**Authors:** Yang Wan, Xihang Yue, Zhirui Liu, Ziyuan Chu, Shuxun Wang et al. (10 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09250) | [PDF](https://arxiv.org/pdf/2609.09250)

<details>
<summary>Abstract</summary>

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two properties. Availability is how much a verdict costs, how early in a rollout the verdict arrives, and how often a verdict can be asked for. Availability rises as verdicts get cheaper, earlier, and denser. Credibility is how much a high score...

</details>

<details>
<summary>Share</summary>

```
No Free Checker: A Survey of Verifiers for Robot Policies

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them.

arXiv: https://arxiv.org/abs/2609.09250

#VLA #robotics
```

</details>

---

## World Models (8)

### [Programmable World Model](https://arxiv.org/abs/2609.10540)

**Authors:** Zheng-Hui Huang, Guixu Lin, Jiacheng Lin, Yi-Chuan Huang, Ruihan Yu et al. (11 authors)

**Published:** 2026-09-09 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10540) | [PDF](https://arxiv.org/pdf/2609.10540) | [Project Page](https://alaya-lab.github.io/pwm) | [Code](https://github.com/AlayaLab/pwm)

<details>
<summary>Abstract</summary>

Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions. We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation. An agent translates natural-language instructions into executable programs that specify entity states and state-transition rules, enabling direct control over individual entities and their interactions. A lightweight engine executes these programs to up...

</details>

<details>
<summary>Share</summary>

```
Programmable World Model

Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interact...

arXiv: https://arxiv.org/abs/2609.10540
Project page: https://alaya-lab.github.io/pwm
Code: https://github.com/AlayaLab/pwm

#worldmodels #robotics
```

</details>

---

### [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](https://arxiv.org/abs/2609.10506)

**Authors:** Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg et al. (8 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10506) | [PDF](https://arxiv.org/pdf/2609.10506) | [Project Page](https://utn-air.github.io/DUET-DINO)

<details>
<summary>Abstract</summary>

Action-conditioned latent world models predict future visual representations, enabling zero-shot goal-conditioned robot planning and control. However, their predictions for fine-grained spatial and rotational actions are unreliable for full 7-DoF end-effector control. To address this gap, we introduce DUET-DINO, a simultaneous cross-view latent world model that jointly learns action-conditioned predictions from static side- and wrist-camera observations through cross-view conditioning. By exploiting complementary global scene and gripper-centric information, DUET-DINO enables latent planning o...

</details>

<details>
<summary>Share</summary>

```
DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation

Action-conditioned latent world models predict future visual representations, enabling zero-shot goal-conditioned robot planning and control.

arXiv: https://arxiv.org/abs/2609.10506
Project page: https://utn-air.github.io/DUET-DINO

#worldmodels #robotics
```

</details>

---

### [Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration](https://arxiv.org/abs/2609.09418)

**Authors:** Yiran Qiao, Feng Wang, Jing Ma

**Published:** 2026-09-08 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09418) | [PDF](https://arxiv.org/pdf/2609.09418)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior. Although WAMs are rapidly advancing embodied AI, general-purpose counterparts remain largely unexplored in games. Existing game-oriented approaches often combine action-conditioned world models with external policies and reward functions to realize WAM-like decision-making, yet they operate mainly in 2D visual observation space and do not instantiate persistent 3D geometry. Extending this paradigm to 3D games introduces a distinct challenge. In autonom...

</details>

<details>
<summary>Share</summary>

```
Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration

World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior.

arXiv: https://arxiv.org/abs/2609.09418

#worldmodels #robotics
```

</details>

---

### [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464)

**Authors:** Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous

**Published:** 2026-09-09 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10464) | [PDF](https://arxiv.org/pdf/2609.10464) | [Project Page](https://sg-jepa.github.io)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested. In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout. To evaluate the model's ability to generalize out of distribution...

</details>

<details>
<summary>Share</summary>

```
Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically reali...

arXiv: https://arxiv.org/abs/2609.10464
Project page: https://sg-jepa.github.io

#worldmodels #robotics
```

</details>

---

### [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](https://arxiv.org/abs/2609.09941)

**Authors:** Zengjue Chen, Peidong Liu, Jiawei Li, Qi Wang

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2609.09941) | [PDF](https://arxiv.org/pdf/2609.09941)

<details>
<summary>Abstract</summary>

Generalist robot policies have demonstrated strong generalization across robotic manipulation tasks, yet their success rates remain limited in com- plex long-horizon scenarios. Recent methods improve Visual-Language-Action (VLA) policies through online reinforcement learning on real robots, but such training relies on costly physical interactions, suffers from low sample efficiency, and may introduce hardware and safety risks. World models offer a promising alternative by enabling policy optimization with imagined rollouts. However, long-horizon rollouts generated by world models often suffer...

</details>

<details>
<summary>Share</summary>

```
HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy

Generalist robot policies have demonstrated strong generalization across robotic manipulation tasks, yet their success rates remain limited in com- plex long-horizon scenarios.

arXiv: https://arxiv.org/abs/2609.09941

#worldmodels #robotics
```

</details>

---

### [Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints](https://arxiv.org/abs/2609.09597)

**Authors:** Qinzhen Ma, Sida Peng

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09597) | [PDF](https://arxiv.org/pdf/2609.09597)

<details>
<summary>Abstract</summary>

Accurate contact prediction is useful for robotic manipulation only if it supports effective decisions. We investigate this connection using a compact, randomly initialized visuotactile world model, trajectory-level uncertainty calibration, and behavior-initialized actor-critic learning in imagination. On 160 MuJoCo Lift episodes, adding touch reduces endpoint-force prediction error from 1.058 to 0.228 N and interval-peak error from 2.724 to 0.523 N across three training seeds. However, tactile persistence achieves lower errors of 0.095 and 0.498 N, respectively. Two exploratory control rounds...

</details>

<details>
<summary>Share</summary>

```
Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints

Accurate contact prediction is useful for robotic manipulation only if it supports effective decisions.

arXiv: https://arxiv.org/abs/2609.09597

#worldmodels #robotics
```

</details>

---

### [Identifying Habit, Physics, and Nuisance in Robot World Models](https://arxiv.org/abs/2609.09210)

**Authors:** Jinting Hang, Zhenhui Cai

**Published:** 2026-09-06 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.09210) | [PDF](https://arxiv.org/pdf/2609.09210)

<details>
<summary>Abstract</summary>

Teleoperated demonstrations are often multimodal even when the underlying dynamics are nearly deterministic given the executed action. We argue that this multimodality typically mixes three factors--operator habit in action selection, shared physics, and observation nuisance--and that entangled next-observation predictors absorb all three. We formalize the split with a structural causal model a=g(h,z,u), z'=f(z,a), o=r(z,c), and test it with complementary interventions: replacing or shuffling actions at fixed state sharply increases next-state error, whereas appearance and camera changes shoul...

</details>

<details>
<summary>Share</summary>

```
Identifying Habit, Physics, and Nuisance in Robot World Models

Teleoperated demonstrations are often multimodal even when the underlying dynamics are nearly deterministic given the executed action.

arXiv: https://arxiv.org/abs/2609.09210

#worldmodels #robotics
```

</details>

---

### [Seven Sources of Physical AI Capability Formation](https://arxiv.org/abs/2609.09627)

**Authors:** Gang Chen

**Published:** 2026-09-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09627) | [PDF](https://arxiv.org/pdf/2609.09627)

<details>
<summary>Abstract</summary>

Capabilities relevant to Physical AI can arise from materially different formation histories, yet existing taxonomies organized by morphology, architecture, learning algorithm, task, or domain do not directly answer what gives rise to a capability. We define a capability-formation source as a factor materially contributing to capability formation, distinct from components or construction steps. We identify seven non-exclusive sources: Recorded-Experience (RE), Predictive-Modeling (PM), Evaluative-Interaction (EI), Surrogate-Environment (SE), Mechanism-Grounded (MG), Embodied-Coupling (EC), and...

</details>

<details>
<summary>Share</summary>

```
Seven Sources of Physical AI Capability Formation

Capabilities relevant to Physical AI can arise from materially different formation histories, yet existing taxonomies organized by morphology, architecture, learning algorithm, task, or domain do not directly answer w...

arXiv: https://arxiv.org/abs/2609.09627

#worldmodels #robotics
```

</details>

---
