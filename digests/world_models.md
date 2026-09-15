# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-09-15 19:31 UTC

**Papers shown:** 30 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence](https://arxiv.org/abs/2609.12036)

**Authors:** Shilong Zou, Shilin Zhang, Yingji Zhang, Yuhang Huang, Yi Zhang et al. (11 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.12036) | [PDF](https://arxiv.org/pdf/2609.12036) | [Project Page](https://zoushilong1024.github.io/Pelican-Sim1.0/)

<details>
<summary>Abstract</summary>

In this technical report, we propose Pelican-Sim 1.0, a general world model simulator for embodied intelligence that predicts future observations from visual context and robot actions to support downstream learning and decision making. The model incorporates four key design features: (1) Unified action representation: a 28-dimensional action value space covering most mainstream embodiments, keeping one model valid across heterogeneous devices. (2) Action-visual injection: URDF- and camera-rendered action videos bridge actions and pixels, giving markedly better controllability across embodiment...

</details>

<details>
<summary>Share</summary>

```
Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence

In this technical report, we propose Pelican-Sim 1.0, a general world model simulator for embodied intelligence that predicts future observations from visual context and robot actions to support downstream learning an...

arXiv: https://arxiv.org/abs/2609.12036
Project page: https://zoushilong1024.github.io/Pelican-Sim1.0/

#worldmodels #robotics
```

</details>

---

### [Programmable World Model](https://arxiv.org/abs/2609.10540)

**Authors:** Zheng-Hui Huang, Guixu Lin, Jiacheng Lin, Yi-Chuan Huang, Ruihan Yu et al. (11 authors)

**Published:** 2026-09-09 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

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

### [LPA-CWM: A Learned Physical Adjudicator for Motion Reasoning with Counterfactual World Models](https://arxiv.org/abs/2609.14073)

**Authors:** Kunwei Wu, Xiang Liu, Guocai Yao, Junming Chen, Zhikang Chen et al. (8 authors)

**Published:** 2026-09-12 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.14073) | [PDF](https://arxiv.org/pdf/2609.14073) | [Project Page](https://LPA-CWM.github.io)

<details>
<summary>Abstract</summary>

Counterfactual world models (CWM) extract motion from pretrained video predictors by comparing factual and intervened predictions. However, responses generated under different target-frame masks vary in reliability, while uniform aggregation weights them equally. We formulate response aggregation as candidate reliability learning and propose LPA-CWM with a lightweight Learned Physical Adjudicator (LPA). Trained on dense MOVi-F trajectories, the 3.0M-parameter LPA compares visual context and response structure across an unordered candidate set to predict relative weights, while the CWM predicto...

</details>

<details>
<summary>Share</summary>

```
LPA-CWM: A Learned Physical Adjudicator for Motion Reasoning with Counterfactual World Models

Counterfactual world models (CWM) extract motion from pretrained video predictors by comparing factual and intervened predictions.

arXiv: https://arxiv.org/abs/2609.14073
Project page: https://LPA-CWM.github.io

#worldmodels #robotics
```

</details>

---

### [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](https://arxiv.org/abs/2609.10506)

**Authors:** Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg et al. (8 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

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

**Published:** 2026-09-08 (updated 2026-09-14) | **Categories:** cs.AI | **Relevance:** ★★★☆☆

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

### [JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion](https://arxiv.org/abs/2609.15770)

**Authors:** Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.15770) | [PDF](https://arxiv.org/pdf/2609.15770) | [Code](https://github.com/ASIG-X/JEPLO)

<details>
<summary>Abstract</summary>

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots. We introduce a proprio-exteroceptive JEPA (PE-JEPA) world model to learn predictive egocentric terrain representations from onboard observations, including raw LiDAR scans. A concurrent JEPA-teacher-student (CJTS) pipeline is further prop...

</details>

<details>
<summary>Share</summary>

```
JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping.

arXiv: https://arxiv.org/abs/2609.15770
Code: https://github.com/ASIG-X/JEPLO

#worldmodels #robotics
```

</details>

---

### [Legislating World-Model-Based Planning with Legal Reasoning](https://arxiv.org/abs/2609.15113)

**Authors:** Dylan Waldner, Yiannis Kantaros, Guido Governatori, Risto Miikkulainen, Amir Banifatemi

**Published:** 2026-09-14 | **Categories:** cs.RO, cs.AI, cs.LO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15113) | [PDF](https://arxiv.org/pdf/2609.15113)

<details>
<summary>Abstract</summary>

As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The paper introduces a legal planning stack that employs Defeasible Deontic Logic (DDL) to constrain a mo...

</details>

<details>
<summary>Share</summary>

```
Legislating World-Model-Based Planning with Legal Reasoning

As robotic systems grow more general, legal norms are needed to integrate them into society.

arXiv: https://arxiv.org/abs/2609.15113

#worldmodels #robotics
```

</details>

---

### [GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation](https://arxiv.org/abs/2609.14561)

**Authors:** I-Tak Ieong, Ruizhi Feng, Zhaoyang Lu, Yifei Cao, Jiayao Zhao et al. (8 authors)

**Published:** 2026-09-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.14561) | [PDF](https://arxiv.org/pdf/2609.14561)

<details>
<summary>Abstract</summary>

Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that prediction into actionable plans. We present GLAM, a goal-conditioned latent world model trained over global spatiotemporal memory, and GLAM NAV, the complete navigation system built around it. Given historical map tokens, a navigation goal, and the current robot pose, GLAM jointly predicts future map representations and robot-centric waypoint latents, allowing future spatial context and...

</details>

<details>
<summary>Share</summary>

```
GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation

Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that predicti...

arXiv: https://arxiv.org/abs/2609.14561

#worldmodels #robotics
```

</details>

---

### [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464)

**Authors:** Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous

**Published:** 2026-09-09 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

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

### [From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation](https://arxiv.org/abs/2609.15382)

**Authors:** Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu et al. (6 authors)

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15382) | [PDF](https://arxiv.org/pdf/2609.15382)

<details>
<summary>Abstract</summary>

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions. A practical world model must predict action consequences accurately, rank candidates in real time, and operate inside the closed loop of a full-size machine. We present the World-Action Model (WAM), which proposes multiple scoops, rejects geometrically inadmissible candidates, jointly predicts signed terrain change and loaded volume, executes the candidate with the largest predicted load, and replans from the newly observed terrain. On 32 geometry-disjoint MinSlope...

</details>

<details>
<summary>Share</summary>

```
From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions.

arXiv: https://arxiv.org/abs/2609.15382

#worldmodels #robotics
```

</details>

---

### [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](https://arxiv.org/abs/2609.09941)

**Authors:** Zengjue Chen, Peidong Liu, Jiawei Li, Qi Wang

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

### [When Should a World Model Move? Loss-Conditioned State Execution](https://arxiv.org/abs/2609.15801)

**Authors:** Jintao Xu, Zhengyu Chen, Ben Zhang, Yongzhi Qi, Jianshen Zhang

**Published:** 2026-09-14 | **Categories:** cs.AI, cs.LG, math.OC | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15801) | [PDF](https://arxiv.org/pdf/2609.15801)

<details>
<summary>Abstract</summary>

We introduce loss-conditioned state execution, a model-agnostic method that decides whether to execute a world model's fixed feasible proposal or retain the current state. Predictive informativeness alone, however, does not establish whether an update will reduce downstream loss. Occurrence ranking can approach perfection while persistence remains the unique absolute-loss Bayes action. Two transition laws can also share occurrence information and conditional variance yet require opposite absolute-loss decisions. We formalize state movability as the existence of a loss-reducing feasible correct...

</details>

<details>
<summary>Share</summary>

```
When Should a World Model Move? Loss-Conditioned State Execution

We introduce loss-conditioned state execution, a model-agnostic method that decides whether to execute a world model's fixed feasible proposal or retain the current state.

arXiv: https://arxiv.org/abs/2609.15801

#worldmodels #robotics
```

</details>

---

### [When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control](https://arxiv.org/abs/2609.15781)

**Authors:** Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta

**Published:** 2026-09-14 | **Categories:** cs.CR, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15781) | [PDF](https://arxiv.org/pdf/2609.15781)

<details>
<summary>Abstract</summary>

Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees the trigger. The attack encodes no explicit trigger-to-action rule. Instead, the poisoned model rout...

</details>

<details>
<summary>Share</summary>

```
When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control

Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pre...

arXiv: https://arxiv.org/abs/2609.15781

#worldmodels #robotics
```

</details>

---

### [One Model, Two Physical Stories: Auditing Misalignment in Multi-Modal World Modeling](https://arxiv.org/abs/2609.14833)

**Authors:** Geigh Zollicoffer, Minh Vu, Rajiv Ranasinghe, Manish Bhattarai

**Published:** 2026-09-13 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.14833) | [PDF](https://arxiv.org/pdf/2609.14833)

<details>
<summary>Abstract</summary>

World models, systems that generate what happens next given current environmental conditions, are increasingly being implemented with multi-modal generation in mind. However, generating multiple modalities simultaneously, such as visual simulations alongside physical state predictions in the form of text, introduces the risk of cross-modal inconsistency. Tested separately, both outputs may look convincing while still disagreeing: a model can calculate that a ball should rebound in one modality, then generate no rebound in another modality, to say nothing of diverging from real-world dynamics e...

</details>

<details>
<summary>Share</summary>

```
One Model, Two Physical Stories: Auditing Misalignment in Multi-Modal World Modeling

World models, systems that generate what happens next given current environmental conditions, are increasingly being implemented with multi-modal generation in mind.

arXiv: https://arxiv.org/abs/2609.14833

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

### [LePlanner: An Iterative Amortized Controller For World Models](https://arxiv.org/abs/2609.13845)

**Authors:** Saksham Bansal, Om Naphade, Chayan Aggarwal, Vrishin M

**Published:** 2026-09-12 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.13845) | [PDF](https://arxiv.org/pdf/2609.13845)

<details>
<summary>Abstract</summary>

World models trained with joint-embedding predictive architectures learn compact, structured latent representations from physical interaction, yet planning in these latent spaces typically relies on one of two costly approaches. Search-based planners such as CEM, MPPI, and iCEM optimize action sequences through many predictor rollouts, achieving strong performance at the cost of high per-decision compute and latency. Policy-based methods amortize inference into a single forward pass but can degrade on contact-rich tasks where the demonstration distribution is multimodal. We propose LePlanner,...

</details>

<details>
<summary>Share</summary>

```
LePlanner: An Iterative Amortized Controller For World Models

World models trained with joint-embedding predictive architectures learn compact, structured latent representations from physical interaction, yet planning in these latent spaces typically relies on one of two costly...

arXiv: https://arxiv.org/abs/2609.13845

#worldmodels #robotics
```

</details>

---

### [IMPLY: Physically Anchored Consistency for World-Model Rollouts](https://arxiv.org/abs/2609.12441)

**Authors:** Aman Mehta, Riya Baviskar

**Published:** 2026-09-11 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12441) | [PDF](https://arxiv.org/pdf/2609.12441)

<details>
<summary>Abstract</summary>

A world model asked what happens if an object is pushed at several speeds produces several futures. If the model has the object in mind, those futures agree about it: each implies the same mass and friction. The consistency checks now used to vet world-action models ask whether a model's futures agree with each other, and none of them knows any physics. We show that this is not enough, and what to do instead. IMPLY reads the physics each rollout implies by inverting a simulator and scores a set of rollouts by how well one object explains all of them, anchored to two calibration pushes the mode...

</details>

<details>
<summary>Share</summary>

```
IMPLY: Physically Anchored Consistency for World-Model Rollouts

A world model asked what happens if an object is pushed at several speeds produces several futures.

arXiv: https://arxiv.org/abs/2609.12441

#worldmodels #robotics
```

</details>

---

### [DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal](https://arxiv.org/abs/2609.12347)

**Authors:** Rongjun Jin, Jianming Ma, Yue Gao

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12347) | [PDF](https://arxiv.org/pdf/2609.12347)

<details>
<summary>Abstract</summary>

Humanoid robots must traverse cluttered obstacle fields using onboard proprioceptive and visual observations, yet existing methods usually process multimodal observations without explicitly considering their different characteristics: proprioceptive observations are low-dimensional but governed by highly nonlinear robot dynamics, while egocentric visual observations are high-dimensional, noisy, and redundant. We propose DWMP (Dual World Model Policy), a framework that provides the actor with separate but complementary world-model representations for humanoid obstacle traversal. A Koopman-based...

</details>

<details>
<summary>Share</summary>

```
DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal

Humanoid robots must traverse cluttered obstacle fields using onboard proprioceptive and visual observations, yet existing methods usually process multimodal observations without explicitly considering their different...

arXiv: https://arxiv.org/abs/2609.12347

#worldmodels #robotics
```

</details>

---

### [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](https://arxiv.org/abs/2609.11445)

**Authors:** Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo et al. (7 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

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

### [RodForesight: A World Model Enhanced Diffusion Policy for Slender Rod Insertion](https://arxiv.org/abs/2609.12103)

**Authors:** Chuanbo Yu, Mingyu Yue, Yan Lyu, Chuhan Song, Peng Wang

**Published:** 2026-09-10 (updated 2026-09-14) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.12103) | [PDF](https://arxiv.org/pdf/2609.12103)

<details>
<summary>Abstract</summary>

Slender rod insertion arises in precision manufacturing, where millimetre scale diameter and tight clearances demand accurate perception and control. Conventional peg-in-hole methods assume a rigid object whose tip pose is fixed relative to the gripper. This assumption breaks down for a high aspect ratio rod, which can bend during manipulation, making its tip motion dependent on the rod configuration, grasp, material properties, and contact. We present RodForesight, a learning framework that factorises the task into two stages: 1) coarse approaching, which uses visual servoing to map diverse i...

</details>

<details>
<summary>Share</summary>

```
RodForesight: A World Model Enhanced Diffusion Policy for Slender Rod Insertion

Slender rod insertion arises in precision manufacturing, where millimetre scale diameter and tight clearances demand accurate perception and control.

arXiv: https://arxiv.org/abs/2609.12103

#worldmodels #robotics
```

</details>

---

### [Compact Visuotactile World Models for Lifting: Prediction, Reward Alignment, and Force Constraints](https://arxiv.org/abs/2609.09597)

**Authors:** Qinzhen Ma

**Published:** 2026-09-09 (updated 2026-09-10) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

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

### [Math for AI safety: an invitation for mathematicians](https://arxiv.org/abs/2609.15289)

**Authors:** Lionel Levine

**Published:** 2026-09-14 | **Categories:** math.HO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15289) | [PDF](https://arxiv.org/pdf/2609.15289)

<details>
<summary>Abstract</summary>

Artificial intelligence threatens to outrun human understanding and control. New mathematics is needed to design AI that is legible, steerable, and cooperative with humanity. I organize this invitation by mathematical field, so you can turn straight to your own: logic and game theory for cooperation; probability for agency and world-models; algebra and representation theory for learned features; analysis and geometry for generalization and training dynamics. Each section ends with an open problem that is accessible to a working mathematician with no prior experience in AI safety.

</details>

<details>
<summary>Share</summary>

```
Math for AI safety: an invitation for mathematicians

Artificial intelligence threatens to outrun human understanding and control.

arXiv: https://arxiv.org/abs/2609.15289

#worldmodels #robotics
```

</details>

---

### [Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation](https://arxiv.org/abs/2609.12422)

**Authors:** Kowei Shih, Lu Cheng, Zeyu Wang, Yeyun Xu, Kejian Tong

**Published:** 2026-09-11 | **Categories:** cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.12422) | [PDF](https://arxiv.org/pdf/2609.12422)

<details>
<summary>Abstract</summary>

Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation. We present HORIZON, a hierarchical agent that combines symmetry aware spatial perception, dual memory belief tracking, relic centric graph attention, information gain driven exploration, and an opponent conditioned policy mixture. HORIZON separates short horizon control from cross match meta reasoning, while auxiliary belief and world model objectives stabilize learning. Trained with PPO in a large sc...

</details>

<details>
<summary>Share</summary>

```
Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation

Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation.

arXiv: https://arxiv.org/abs/2609.12422

#worldmodels #robotics
```

</details>

---

### [Seven Sources of Physical AI Capability Formation](https://arxiv.org/abs/2609.09627)

**Authors:** Gang Chen

**Published:** 2026-09-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

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

### [Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.12278)

**Authors:** Fernando Palafox, David Fridovich-Keil

**Published:** 2026-09-10 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.12278) | [PDF](https://arxiv.org/pdf/2609.12278)

<details>
<summary>Abstract</summary>

World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate. We study the problem of adapting a world model to an unknown test-time environment, drawn from a known environment family, using only a few episodes of interaction. Existing approaches trade off computational cost against expressivity, i.e., the range of models a method can produce. For example, in-context learning is computationally cheap but limited in expressivity, and gradient-based adaptation is expressive but computationally expensive. We present CLAW (Co...

</details>

<details>
<summary>Share</summary>

```
Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning

World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate.

arXiv: https://arxiv.org/abs/2609.12278

#worldmodels #robotics
```

</details>

---

### [CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising](https://arxiv.org/abs/2609.11553)

**Authors:** Hongjin Chen, Zijun Xu, Shihao Ma, Yi Zhao, Xilai Liu et al. (11 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

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

### [Exploring napping paradigm for Recurrent Spiking Neural Networks](https://arxiv.org/abs/2609.13927)

**Authors:** Andreas Massey, Stefano Nichele, Aliaksandr Hubin

**Published:** 2026-09-12 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.13927) | [PDF](https://arxiv.org/pdf/2609.13927)

<details>
<summary>Abstract</summary>

Biological organisms minimize free energy by balancing two competing demands on their internal world model: it must be accurate enough to predict sensory input, yet simple enough to generalize beyond it. Two mechanisms regulate this balance offline: sleep reduces complexity through gradual synaptic downscaling, while stochastic noise attenuates precision, relaxing the constraint sensory input imposes on synaptic reorganization. Engineered Spiking Neural Networks (SNNs) leave this balance unaddressed, favoring instantaneous, noiseless weight normalization instead. This paper investigates the hy...

</details>

<details>
<summary>Share</summary>

```
Exploring napping paradigm for Recurrent Spiking Neural Networks

Biological organisms minimize free energy by balancing two competing demands on their internal world model: it must be accurate enough to predict sensory input, yet simple enough to generalize beyond it.

arXiv: https://arxiv.org/abs/2609.13927

#worldmodels #robotics
```

</details>

---

### [Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity](https://arxiv.org/abs/2609.12090)

**Authors:** Aditi Tiwari, Akshit Bhalla, Darshan Prasad, Heng Ji

**Published:** 2026-09-10 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.12090) | [PDF](https://arxiv.org/pdf/2609.12090)

<details>
<summary>Abstract</summary>

Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content. Standard memory ablations test whether memory helps, but not whether the retrieved content is responsible. We test this directly with read-time memory substitution, which replaces the consumed memory value while leaving the rest of the computation unchanged. This separates memory benefit from memory specificity, the extent to which the gain depends on retrieved content. Across frozen video world models, identity-free controls...

</details>

<details>
<summary>Share</summary>

```
Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity

Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content.

arXiv: https://arxiv.org/abs/2609.12090

#worldmodels #robotics
```

</details>

---
