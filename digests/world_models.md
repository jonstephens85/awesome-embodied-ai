# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-09-11 18:59 UTC

**Papers shown:** 29 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

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

### [How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation](https://arxiv.org/abs/2609.06009)

**Authors:** Jiaju Yin, Zhenhui Zhang, Lixin Xu, Heng Zhang, Jun Shao et al. (8 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06009) | [PDF](https://arxiv.org/pdf/2609.06009) | [Project Page](https://whirl-dexterous.github.io/)

<details>
<summary>Abstract</summary>

Multi-fingered dexterous manipulation remains a frontier for real-world reinforcement learning (RL) due to the high-dimensional action space and the prohibitive cost of hardware failures. While human-in-the-loop (HIL) RL allows operators to intervene before failures occur, current pipelines often treat these interventions as reactive corrections, discarding the rich safety signal inherent in the operator's decision to take control. In this paper, we ask: How can we learn from what a human would avoid? We present WHIRL, a safety-aware RL framework that transforms binary human interventions into...

</details>

<details>
<summary>Share</summary>

```
How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation

Multi-fingered dexterous manipulation remains a frontier for real-world reinforcement learning (RL) due to the high-dimensional action space and the prohibitive cost of hardware failures.

arXiv: https://arxiv.org/abs/2609.06009
Project page: https://whirl-dexterous.github.io/

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

### [Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration](https://arxiv.org/abs/2609.09418)

**Authors:** Yiran Qiao, Feng Wang, Jing Ma

**Published:** 2026-09-08 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus

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

### [PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling](https://arxiv.org/abs/2609.07532)

**Authors:** Yinan Deng, Jianqiao Song, Yisi Zhang, Yuhan Wang, Jiahui Wang et al. (6 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.07532) | [PDF](https://arxiv.org/pdf/2609.07532) | [Project Page](https://physreal.github.io/anonymous_web)

<details>
<summary>Abstract</summary>

Learning physically plausible dynamics from visual observations is essential for interactive world models and embodied agents. However, modeling real-world deformable objects remains challenging because their dynamics often arise from complex, spatially heterogeneous material responses. To address this challenge, we propose PhysReal, a video-driven framework for learning and simulating the underlying physics of real deformable objects. PhysReal integrates a spatially varying hybrid expert-neural constitutive model with a differentiable MPM simulator and 3DGS renderer. Analytical expert models...

</details>

<details>
<summary>Share</summary>

```
PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling

Learning physically plausible dynamics from visual observations is essential for interactive world models and embodied agents.

arXiv: https://arxiv.org/abs/2609.07532
Project page: https://physreal.github.io/anonymous_web

#worldmodels #robotics
```

</details>

---

### [WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation](https://arxiv.org/abs/2609.07002)

**Authors:** Jie Yin, Zeyuan Zhao, Xiaojing Tan, Yang Liu, Chiyu Wang et al. (6 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.07002) | [PDF](https://arxiv.org/pdf/2609.07002) | [Project Page](https://wmcraftnet.github.io/)

<details>
<summary>Abstract</summary>

Generalizable and robust dexterous in-hand manipulation requires a policy to infer object pose, geometry, contact, and potential slip from partial and noisy observations. Although recent tactile and visuotactile RL methods achieve strong in-hand rotation in controlled settings, their robustness often degrades under pose shifts, force disturbances, and object variation. We propose WM-Craftnet, a world-model-conditioned framework that learns compact action-conditioned latent dynamics from proprioception, depth, tactile sensing, and actions, supervised by multimodal reconstruction and reward pred...

</details>

<details>
<summary>Share</summary>

```
WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation

Generalizable and robust dexterous in-hand manipulation requires a policy to infer object pose, geometry, contact, and potential slip from partial and noisy observations.

arXiv: https://arxiv.org/abs/2609.07002
Project page: https://wmcraftnet.github.io/

#worldmodels #robotics
```

</details>

---

### [BinauralVAE: Spatial Audio Reconstruction For World Models](https://arxiv.org/abs/2609.06837)

**Authors:** Luis Vitor Zerkowski, Luiz Velho

**Published:** 2026-09-06 | **Categories:** cs.SD, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06837) | [PDF](https://arxiv.org/pdf/2609.06837) | [Code](https://github.com/Luizerko/BinauralVAE)

<details>
<summary>Abstract</summary>

Embodied artificial intelligence has historically very much relied on visual perception, leading to a proliferation of multiple vision-centric world models. However, this reliance fails to capture spatial understanding in its entirety and can even present vulnerabilities in environments with visual occlusions, low-light conditions, or blackouts-scenarios, where acoustic information becomes a critical alternative for spatial awareness and navigation. Despite its potential, research into realistic spatial audio and particularly the development of audio-centric world models remains sparse. In thi...

</details>

<details>
<summary>Share</summary>

```
BinauralVAE: Spatial Audio Reconstruction For World Models

Embodied artificial intelligence has historically very much relied on visual perception, leading to a proliferation of multiple vision-centric world models.

arXiv: https://arxiv.org/abs/2609.06837
Code: https://github.com/Luizerko/BinauralVAE

#worldmodels #robotics
```

</details>

---

### [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](https://arxiv.org/abs/2609.11445)

**Authors:** Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo et al. (7 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2609.11445) | [PDF](https://arxiv.org/pdf/2609.11445)

<details>
<summary>Abstract</summary>

Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components. We ask whether the internal predictive states of a frozen pretrained robotic world model already contain directly decodable failure information. Failure-Aware Readout from World Models (FARM) trains only a 33,985-parameter supervised readout over frozen VLA-JEPA predictive states, producing step-wise failure scores and causal trajectory risk. Five-fold out-of-fold evaluation across seven source tasks reaches 85.68/88.59 pooled AUROC...

</details>

<details>
<summary>Share</summary>

```
FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model

Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components.

arXiv: https://arxiv.org/abs/2609.11445

#worldmodels #robotics
```

</details>

---

### [Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints](https://arxiv.org/abs/2609.09597)

**Authors:** Qinzhen Ma

**Published:** 2026-09-09 (updated 2026-09-10) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09597) | [PDF](https://arxiv.org/pdf/2609.09597)

<details>
<summary>Abstract</summary>

Accurate tactile forecasts need not improve force-constrained control. We study a 652,157-parameter action-conditioned visuotactile world model with matched behavior cloning, policy learning in imagination, independent reactive implicit Q-learning, and model-assisted force feedback. A fixed protocol executes 34 policies on 120 fresh MuJoCo environments spanning geometry and physical-parameter shifts, plus 324 independently replayed action branches on 12 additional ID environments. Visuotactile dynamics reduce force action-effect MAE from 0.413 N for persistence to 0.338 N. Model-assisted feedb...

</details>

<details>
<summary>Share</summary>

```
Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints

Accurate tactile forecasts need not improve force-constrained control.

arXiv: https://arxiv.org/abs/2609.09597

#worldmodels #robotics
```

</details>

---

### [Beyond Task Success: Stage-Wise Reliability of World Model Planning under Sensing Degradation](https://arxiv.org/abs/2609.07126)

**Authors:** Geonmyeong Lee, Byoung-Tak Zhang

**Published:** 2026-09-07 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.07126) | [PDF](https://arxiv.org/pdf/2609.07126)

<details>
<summary>Abstract</summary>

In world model planning, sensing inputs pass through an encoder and predictor before affecting planner decisions, so final task success alone cannot reveal where sensing disturbances attenuate or persist in the pipeline. We apply 10 visual and temporal sensing degradations to a world model planner and track their effects across representation, future prediction, planner preference, and physical outcome using paired evaluation on the same 50 tasks. The relative impact of degradations was not preserved across stages: large representation shifts could attenuate downstream, while smaller initial s...

</details>

<details>
<summary>Share</summary>

```
Beyond Task Success: Stage-Wise Reliability of World Model Planning under Sensing Degradation

In world model planning, sensing inputs pass through an encoder and predictor before affecting planner decisions, so final task success alone cannot reveal where sensing disturbances attenuate or persist in the pipeline.

arXiv: https://arxiv.org/abs/2609.07126

#worldmodels #robotics
```

</details>

---

### [Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping](https://arxiv.org/abs/2609.06820)

**Authors:** Jiahui Zhang, Gongbo Liang, Yu Zhang

**Published:** 2026-09-06 (updated 2026-09-10) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.06820) | [PDF](https://arxiv.org/pdf/2609.06820)

<details>
<summary>Abstract</summary>

Active mapping requires a robot to select camera viewpoints that efficiently reconstruct an unknown 3D scene. To reason about unobserved regions, recent systems use pretrained occupancy networks as world models that complete missing geometry. The predicted structure contributes to expected coverage gain and constrains feasible robot motion. Consequently, occupancy errors can change both what the robot chooses to explore and where it is able to move. We diagnose these effects by holding the planner fixed and varying only the occupancy representation provided to it. We consider planning without...

</details>

<details>
<summary>Share</summary>

```
Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping

Active mapping requires a robot to select camera viewpoints that efficiently reconstruct an unknown 3D scene.

arXiv: https://arxiv.org/abs/2609.06820

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

### [CST-WM: A Causally Structured World Model for Embodied Visual Tracking](https://arxiv.org/abs/2609.06302)

**Authors:** Junyi Hu, Shuaihang Yuan, Yi Fang

**Published:** 2026-09-05 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.06302) | [PDF](https://arxiv.org/pdf/2609.06302)

<details>
<summary>Abstract</summary>

Embodied visual tracking requires a robot not only to react to the current view, but to choose actions that preserve or recover future evidence of a moving target under ego-motion, occlusion, and distractors. It is therefore a predictive decision problem over future target observability and apparent scale. A central difficulty is a task-specific form of causal hallucination: in action-conditioned prediction, a model can exploit the strong correlation between robot control and target-related observations by hallucinating a direct causal effect from the current action to target evidence, rather...

</details>

<details>
<summary>Share</summary>

```
CST-WM: A Causally Structured World Model for Embodied Visual Tracking

Embodied visual tracking requires a robot not only to react to the current view, but to choose actions that preserve or recover future evidence of a moving target under ego-motion, occlusion, and distractors.

arXiv: https://arxiv.org/abs/2609.06302

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

### [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://arxiv.org/abs/2609.09155)

**Authors:** Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang et al. (9 authors)

**Published:** 2026-09-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.09155) | [PDF](https://arxiv.org/pdf/2609.09155)

<details>
<summary>Abstract</summary>

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a...

</details>

<details>
<summary>Share</summary>

```
SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions.

arXiv: https://arxiv.org/abs/2609.09155

#worldmodels #robotics
```

</details>

---

### [Earth System World Model for What-If Simulations: A Case Study for Terrestrial Ecosystems](https://arxiv.org/abs/2609.08855)

**Authors:** Zhihao Wang, Ruichen Wang, Ruohan Li, Lei Ma, George Hurtt et al. (9 authors)

**Published:** 2026-09-08 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.08855) | [PDF](https://arxiv.org/pdf/2609.08855)

<details>
<summary>Abstract</summary>

Machine learning emulators have become essential for accelerating expensive Earth-system simulations, but most existing approaches remain passive forecasters: they reproduce simulator trajectories under prescribed forcings without an explicit interaction mechanism for user-specified interventions. This limits their use in interactive scientific workflows and Earth-system digital twins, where users often need to explore how a system would respond if selected state components were changed. We propose an action-conditioned world-modeling framework for Earth-system emulation that reformulates simu...

</details>

<details>
<summary>Share</summary>

```
Earth System World Model for What-If Simulations: A Case Study for Terrestrial Ecosystems

Machine learning emulators have become essential for accelerating expensive Earth-system simulations, but most existing approaches remain passive forecasters: they reproduce simulator trajectories under prescribed for...

arXiv: https://arxiv.org/abs/2609.08855

#worldmodels #robotics
```

</details>

---

### [TrojanWorld: Backdooring World-Model Agents via Imagination Steering](https://arxiv.org/abs/2609.07051)

**Authors:** Wenkai Huang, Siyuan Liang, Gaolei Li, Yiming Li, Tianhao Peng et al. (7 authors)

**Published:** 2026-09-07 | **Categories:** cs.LG, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.07051) | [PDF](https://arxiv.org/pdf/2609.07051)

<details>
<summary>Abstract</summary>

World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting. Their substantial training demands make pretrained world models attractive for distribution and reuse, exposing downstream systems to model supply chain threats. Backdoor attacks offer a targeted and stealthy means of exploiting such supply chains, yet their threat to interactive world-model agents remains largely unexplored. To fill this gap, we present TrojanWorld, a backdoor framework for world-mod...

</details>

<details>
<summary>Share</summary>

```
TrojanWorld: Backdooring World-Model Agents via Imagination Steering

World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting.

arXiv: https://arxiv.org/abs/2609.07051

#worldmodels #robotics
```

</details>

---

### [Learning Counterfactual World Models for Embodied Reasoning under Partial Observability](https://arxiv.org/abs/2609.05834)

**Authors:** Todd Y. Zhou, Daniel Zhang

**Published:** 2026-09-05 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.05834) | [PDF](https://arxiv.org/pdf/2609.05834)

<details>
<summary>Abstract</summary>

World models promise a general route to embodied intelligence: learn predictive dynamics once, then reason, plan, and act with them. Increasingly, the representations beneath such models are pretrained on large-scale video, interaction, and multimodal corpora, which raises a question prediction quality alone cannot answer: when is a learned representation actually actionable? We identify a failure mode we call counterfactual collapse: a model predicts visually plausible futures while failing to distinguish interventions with different behavioral consequences. This arises whenever a representat...

</details>

<details>
<summary>Share</summary>

```
Learning Counterfactual World Models for Embodied Reasoning under Partial Observability

World models promise a general route to embodied intelligence: learn predictive dynamics once, then reason, plan, and act with them.

arXiv: https://arxiv.org/abs/2609.05834

#worldmodels #robotics
```

</details>

---

### [TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911)

**Authors:** Xin Zhang, Yabo Chen, Zixuan Duan, Haibin Huang, Chi Zhang et al. (7 authors)

**Published:** 2026-09-04 (updated 2026-09-07) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.04911) | [PDF](https://arxiv.org/pdf/2609.04911)

<details>
<summary>Abstract</summary>

Interactive visual world models must distinguish observation from physical intervention. Camera motion reveals new surfaces, whereas intervention changes object motion, contact, and deformation. Current video world models are largely driven by appearance priors and often lose physical or spatial consistency over long horizons. We present TourPhysics, an online framework initialized from a single image and a declarative physical configuration. TourPhysics extends PhysOmni, our ACM Multimedia 2026 work, from finite physics-grounded video synthesis to persistent exploration and manipulation. Tour...

</details>

<details>
<summary>Share</summary>

```
TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image

Interactive visual world models must distinguish observation from physical intervention.

arXiv: https://arxiv.org/abs/2609.04911

#worldmodels #robotics
```

</details>

---

### [CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising](https://arxiv.org/abs/2609.11553)

**Authors:** Hongjin Chen, Zijun Xu, Shihao Ma, Yi Zhao, Xilai Liu et al. (11 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.11553) | [PDF](https://arxiv.org/pdf/2609.11553)

<details>
<summary>Abstract</summary>

Humanoid locomotion across complex terrain demands forward-looking exteroception to anticipate obstacles, yet this signal is unreliable in real-world deployment, failing partially and intermittently. Existing perceptive policies often assume that depth observations remain clean and in-distribution, while recent attempts to unify perceptive and blind control typically route or switch between separate sub-policies, leaving recoverable information in partially corrupted depth unexploited. We instead propose CAP, a single-stage humanoid locomotion policy that recovers this signal with a perceptive...

</details>

<details>
<summary>Share</summary>

```
CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising

Humanoid locomotion across complex terrain demands forward-looking exteroception to anticipate obstacles, yet this signal is unreliable in real-world deployment, failing partially and intermittently.

arXiv: https://arxiv.org/abs/2609.11553

#worldmodels #robotics
```

</details>

---

### [CALIPER: Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Representations](https://arxiv.org/abs/2609.08250)

**Authors:** Aman Mehta, Riya Baviskar

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.08250) | [PDF](https://arxiv.org/pdf/2609.08250)

<details>
<summary>Abstract</summary>

How far a pushed object slides depends on its mass and friction, which no single image reveals. Pretrained visual encoders are increasingly used as the perception front end of world models for manipulation, and their physical competence is assessed with perturbation benchmarks and linear probes, almost always in a clean, fixed-camera scene. We show that these assessments cannot distinguish an encoder that infers physics from one that does not. CALIPER (calibrate, then predict) is a direct test: an object of unknown mass and friction is struck twice at known speeds, a third strike is shown only...

</details>

<details>
<summary>Share</summary>

```
CALIPER: Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Representations

How far a pushed object slides depends on its mass and friction, which no single image reveals.

arXiv: https://arxiv.org/abs/2609.08250

#worldmodels #robotics
```

</details>

---

### [PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout](https://arxiv.org/abs/2609.07328)

**Authors:** Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li et al. (7 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO, cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.07328) | [PDF](https://arxiv.org/pdf/2609.07328)

<details>
<summary>Abstract</summary>

Local pedestrian-vehicle forecasting spans heterogeneous physical scales: pedestrians combine root locomotion with articulated motion, whereas vehicles are rigid bodies described by kinematic state and oriented extent. Existing road-agent forecasters typically omit pedestrian articulation, while pose forecasters leave vehicle futures outside the learned rollout. We introduce PV-WM, a history-only world model over structured post-perception tracks. It recurrently advances pedestrian root motion, 15-joint articulation, and learned vehicle states within a synchronized heterogeneous state. The gen...

</details>

<details>
<summary>Share</summary>

```
PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout

Local pedestrian-vehicle forecasting spans heterogeneous physical scales: pedestrians combine root locomotion with articulated motion, whereas vehicles are rigid bodies described by kinematic state and oriented extent.

arXiv: https://arxiv.org/abs/2609.07328

#worldmodels #robotics
```

</details>

---

### [Coupled Control and Wireless World Models for Resilient Remote Robotic Control](https://arxiv.org/abs/2609.04851)

**Authors:** H. P. Madushanka, Sumudu Samarakoon, Mehdi Bennis

**Published:** 2026-09-04 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.04851) | [PDF](https://arxiv.org/pdf/2609.04851)

<details>
<summary>Abstract</summary>

Remote robotic systems operating over wireless networks must maintain reliable control despite limited communication resources, changing channel conditions, and environmental disturbances.However, continuously transmitting high-dimensional sensory observations, such as camera images, increases communication overhead and energy consumption while reducing robustness under unreliable connectivity.To address these challenges, this paper proposes a resilient communication-aware remote robotic control framework based on coupled control and wireless Joint Embedding Predictive Architecture (JEPA) worl...

</details>

<details>
<summary>Share</summary>

```
Coupled Control and Wireless World Models for Resilient Remote Robotic Control

Remote robotic systems operating over wireless networks must maintain reliable control despite limited communication resources, changing channel conditions, and environmental disturbances.However, continuously transmi...

arXiv: https://arxiv.org/abs/2609.04851

#worldmodels #robotics
```

</details>

---

### [World Models Under Asynchronous Sensor Observations](https://arxiv.org/abs/2609.07299)

**Authors:** Akash Anand, Abhay Anand, Yash Vishe

**Published:** 2026-09-07 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.07299) | [PDF](https://arxiv.org/pdf/2609.07299)

<details>
<summary>Abstract</summary>

Learned world models typically assume that observations arrive synchronously, an abstraction inherited from simulators that return a complete state vector at each environment step. Physical sensing instead operates at heterogeneous rates, leaving most observation channels stale at any given instant. Interpolating stale channels introduces measurements that were never observed, while downsampling to the slowest sensor discards valid measurements. A natural alternative is to zero-order-hold the most recent reading and provide the known sampling schedule to the model through two features, stalene...

</details>

<details>
<summary>Share</summary>

```
World Models Under Asynchronous Sensor Observations

Learned world models typically assume that observations arrive synchronously, an abstraction inherited from simulators that return a complete state vector at each environment step.

arXiv: https://arxiv.org/abs/2609.07299

#worldmodels #robotics
```

</details>

---

### [From Language Models to World-Acting Systems: Progress and Limits of Agentic AI across Digital, Social, Virtual, and Physical Environments](https://arxiv.org/abs/2609.04894)

**Authors:** Linsen Zhu, Mengqing Cai

**Published:** 2026-09-04 | **Categories:** cs.AI, cs.LG, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.04894) | [PDF](https://arxiv.org/pdf/2609.04894)

<details>
<summary>Abstract</summary>

Large language models become consequential agents when surrounding systems let outputs change external state. Models now call tools, operate interfaces, delegate work, retain state, inhabit generated worlds, and control robots or laboratory equipment. Such advances are often narrated as one march toward autonomy, conflating model competence, system integration, persistence, and safe authority. This critical review synthesizes primary research and official technical specifications available by 31 August 2026. We organize the evidence along delegated authority, temporal persistence, and environm...

</details>

<details>
<summary>Share</summary>

```
From Language Models to World-Acting Systems: Progress and Limits of Agentic AI across Digital, Social, Virtual, and Physical Environments

Large language models become consequential agents when surrounding systems let outputs change external state.

arXiv: https://arxiv.org/abs/2609.04894

#worldmodels #robotics
```

</details>

---

### [Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823)

**Authors:** Cristian Sminchisescu

**Published:** 2026-09-06 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.06823) | [PDF](https://arxiv.org/pdf/2609.06823)

<details>
<summary>Abstract</summary>

The next generation of artificial intelligence systems will likely be natively temporal and multimodal in both inputs and outputs: able to converse, perceive, predict, reason, and synthesize through a shared world representation. Realizing this requires a temporal perceptual substrate integrating sensory streams, language, and structured outputs within a multimodal world model. We seek a generalist open-world perceptual system that represents biological forms, natural physical structures, and artifacts, and their interactions, as a coherent, temporally persistent process. The model should infe...

</details>

<details>
<summary>Share</summary>

```
Generalist Open-World Temporal Perception

The next generation of artificial intelligence systems will likely be natively temporal and multimodal in both inputs and outputs: able to converse, perceive, predict, reason, and synthesize through a shared world rep...

arXiv: https://arxiv.org/abs/2609.06823

#worldmodels #robotics
```

</details>

---

### [PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207)

**Authors:** Rasul Khanbayov, Hasan Kurban

**Published:** 2026-09-05 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.06207) | [PDF](https://arxiv.org/pdf/2609.06207)

<details>
<summary>Abstract</summary>

Image-to-video generators are often credited with absorbing physical dynamics as implicit world models, a claim the community currently checks with plausibility scores that ask whether a clip looks consistent with real-world motion. Plausibility is the wrong test on its own, because a clip can look natural while encoding the wrong value of the governing physical parameter, and no existing benchmark measures this gap directly. PhysWeep closes it with a fixed, label-free audit, treating a frozen generator as a black box, recovering the realized parameter from generated pixels, and reporting how...

</details>

<details>
<summary>Share</summary>

```
PhysWeep: Does a Video Generator Realize the Physics You Ask For?

Image-to-video generators are often credited with absorbing physical dynamics as implicit world models, a claim the community currently checks with plausibility scores that ask whether a clip looks consistent with rea...

arXiv: https://arxiv.org/abs/2609.06207

#worldmodels #robotics
```

</details>

---
