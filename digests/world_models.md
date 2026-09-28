# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-09-28 21:35 UTC

**Papers shown:** 36 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation](https://arxiv.org/abs/2609.28393)

**Authors:** Hantao Ye, Ross Worobel, Zhuoli Xie, Mingen Li, Houjian Yu et al. (7 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28393) | [PDF](https://arxiv.org/pdf/2609.28393) | [Project Page](https://pointcast-wm.github.io)

<details>
<summary>Abstract</summary>

World models are useful for robotic manipulation because robots can predict how actions change the states of objects before executing them. We present PointCast, a point-set world model that spans rigid, articulated, and deformable object manipulation. Its state is a set of 3D points on the object and the end-effector, mesh-free and topology-agnostic. Each point keeps its identity and is supervised on its own trajectory, which teaches the model where every point goes rather than only the shape the points form. Its backbone is a diffusion transformer that denoises a short window of future point...

</details>

<details>
<summary>Share</summary>

```
PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation

World models are useful for robotic manipulation because robots can predict how actions change the states of objects before executing them.

arXiv: https://arxiv.org/abs/2609.28393
Project page: https://pointcast-wm.github.io

#worldmodels #robotics
```

</details>

---

### [TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models](https://arxiv.org/abs/2609.26314)

**Authors:** Xuanyi Liu, Haofeng Wang, Ruiqi Li, Danni Yu, Rui Wan et al. (12 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.26314) | [PDF](https://arxiv.org/pdf/2609.26314) | [Code](https://github.com/TriWorldBench/TriWorldBench)

<details>
<summary>Abstract</summary>

Embodied world models predict the outcomes of robot actions to support learning and planning. For robots equipped with head and wrist cameras, this requires complementary views: the head view captures the overall task, while wrist views reveal local gripper-object interactions. However, evaluating these views independently cannot determine whether they describe the same action and object state. We introduce TRIWORLDBENCH, a benchmark for evaluating embodied world models through synchronized head, left-wrist, and right-wrist videos. It contains 500 episodes across 50 bimanual manipulation tasks...

</details>

<details>
<summary>Share</summary>

```
TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models

Embodied world models predict the outcomes of robot actions to support learning and planning.

arXiv: https://arxiv.org/abs/2609.26314
Code: https://github.com/TriWorldBench/TriWorldBench

#worldmodels #robotics
```

</details>

---

### [D-JEPA: A Decision-Aligned Latent World Model](https://arxiv.org/abs/2609.24749)

**Authors:** Shuaijun Liu, Chengyu Wu, Qifu Wen, Feiyang You, Chenglong Zhang et al. (8 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24749) | [PDF](https://arxiv.org/pdf/2609.24749) | [Project Page](https://nebulis-lab.com/D-JEPA)

<details>
<summary>Abstract</summary>

Latent world models predict the consequences of actions, but accurate prediction does not guarantee that latent distance reflects which candidate will execute successfully. We identify a decision-local prediction gap: among the few futures competing for execution, a candidate predicted closer to the goal can produce a worse realized outcome than an available alternative. We introduce D-JEPA, a decision-aligned latent world model that learns decision-relevant relations among candidate futures from executed outcomes. A bounded, permutation-equivariant operator jointly reasons over goal-relative...

</details>

<details>
<summary>Share</summary>

```
D-JEPA: A Decision-Aligned Latent World Model

Latent world models predict the consequences of actions, but accurate prediction does not guarantee that latent distance reflects which candidate will execute successfully.

arXiv: https://arxiv.org/abs/2609.24749
Project page: https://nebulis-lab.com/D-JEPA

#worldmodels #robotics
```

</details>

---

### [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652)

**Authors:** Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin

**Published:** 2026-09-22 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25652) | [PDF](https://arxiv.org/pdf/2609.25652) | [Project Page](https://jimntu.github.io/gamedirector/)

<details>
<summary>Abstract</summary>

Recent game world models support realistic visual simulation and interactive gameplay based on player inputs. However, they typically learn environment dynamics from pixel-level supervision, jointly modeling perception, memory, state transitions, and rendering within a single end-to-end framework. While this design enables open-ended, action-controllable generation, it still falls short of delivering a complete gameplay experience. Games are governed by explicit mechanics, such as health deduction, skill activation, combat rules, and termination conditions. These mechanics depend on precise an...

</details>

<details>
<summary>Share</summary>

```
GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models

Recent game world models support realistic visual simulation and interactive gameplay based on player inputs.

arXiv: https://arxiv.org/abs/2609.25652
Project page: https://jimntu.github.io/gamedirector/

#worldmodels #robotics
```

</details>

---

### [AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/abs/2609.30264)

**Authors:** Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo et al. (6 authors)

**Published:** 2026-09-24 (updated 2026-09-25) | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.30264) | [PDF](https://arxiv.org/pdf/2609.30264) | [Project Page](https://ad-wm.github.io/)

<details>
<summary>Abstract</summary>

Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized recovery objective motivated by conditional mutual information. Both objectives encourage planning tra...

</details>

<details>
<summary>Share</summary>

```
AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control

Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state.

arXiv: https://arxiv.org/abs/2609.30264
Project page: https://ad-wm.github.io/

#worldmodels #robotics
```

</details>

---

### [Representation World Model: Learning States, Transition and Executable Plans in Representation](https://arxiv.org/abs/2609.29171)

**Authors:** Yijun Yuan, Weicheng Zheng, Weibang Wang, Minghui Qin, Chang Sun et al. (10 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.29171) | [PDF](https://arxiv.org/pdf/2609.29171) | [Project Page](https://tsinghua-mars-lab.github.io/RepresentationWorldModel)

<details>
<summary>Abstract</summary>

We propose the Representation World Model (RWM), which learns states, transitions, and executable plans directly in representation space. Unlike existing world models that typically learn latent representations together with explicit dynamics models and perform planning through search, optimization, or policy-based prediction, RWM directly incorporates planning into the learned representation geometry. RWM learns the representation geometry by applying inverse-dynamics supervision locally along latent paths constructed from endpoint representations, requiring these paths to preserve task-relev...

</details>

<details>
<summary>Share</summary>

```
Representation World Model: Learning States, Transition and Executable Plans in Representation

We propose the Representation World Model (RWM), which learns states, transitions, and executable plans directly in representation space.

arXiv: https://arxiv.org/abs/2609.29171
Project page: https://tsinghua-mars-lab.github.io/RepresentationWorldModel

#worldmodels #robotics
```

</details>

---

### [Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007)

**Authors:** Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang et al. (9 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.26007) | [PDF](https://arxiv.org/pdf/2609.26007)

<details>
<summary>Abstract</summary>

Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in flight the executed action explains almost all of the change between observations, so prediction reduces...

</details>

<details>
<summary>Share</summary>

```
Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models

Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale.

arXiv: https://arxiv.org/abs/2609.26007

#worldmodels #robotics
```

</details>

---

### [DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976)

**Authors:** Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell et al. (7 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24976) | [PDF](https://arxiv.org/pdf/2609.24976) | [Project Page](https://dextacwam.github.io/)

<details>
<summary>Abstract</summary>

Dexterous manipulation depends on contact dynamics that are often only partially observable from vision. Recent World-Action Models (WAMs) couple predictive video world modeling with action generation, but remain largely vision-centric and therefore cannot directly model these contact dynamics. We present DexTacWAM, a visuo-tactile WAM that encodes each fingertip independently, aggregates the resulting features through a finger- and pose-aware tactile compressor, and injects the tactile latent into a video diffusion world model for joint visuo-tactile world modeling. Across six contact-rich de...

</details>

<details>
<summary>Share</summary>

```
DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation

Dexterous manipulation depends on contact dynamics that are often only partially observable from vision.

arXiv: https://arxiv.org/abs/2609.24976
Project page: https://dextacwam.github.io/

#worldmodels #robotics
```

</details>

---

### [MA-WAM: Multi-Agent World-Action Model for Test-Time Planning](https://arxiv.org/abs/2609.31281)

**Authors:** Guowei Zou, Haitao Wang, Guoxin Wang, Beiwen Zhang, Zhiquan Chen et al. (7 authors)

**Published:** 2026-09-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.31281) | [PDF](https://arxiv.org/pdf/2609.31281) | [Project Page](https://ma-wam.github.io/)

<details>
<summary>Abstract</summary>

Multi-agent cooperative tasks require different agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the other agents. Hence, a world model is needed to predict the team return resulting from the joint actions of all agents. A naive extension directly applies a single-agent world model to each agent's action when predicting the team return step by step. However, such an extension fails to capture the dependencies among the simultaneous actions of multiple agents. We propose Multi-Agent World-Action Model (MA-WAM), a test-time p...

</details>

<details>
<summary>Share</summary>

```
MA-WAM: Multi-Agent World-Action Model for Test-Time Planning

Multi-agent cooperative tasks require different agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the other agents.

arXiv: https://arxiv.org/abs/2609.31281
Project page: https://ma-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [HelloWorld: Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931)

**Authors:** Fan Lu, Hanshi Wang, Zijing Wang, Quan Feng, Zhi Wang et al. (23 authors)

**Published:** 2026-09-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28931) | [PDF](https://arxiv.org/pdf/2609.28931) | [Project Page](https://helloworld-4d.github.io)

<details>
<summary>Abstract</summary>

Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs. Realizing this potential requires a system that can generalize across diverse scenes, respond faithfully to prescribed controls, generate coherent multi-sensor observations, and operate efficiently under repeated inference. We present \textbf{HelloWorld}, a 2B driving world model system designed around these requirements. HelloWorld progressively specializes broad visual and motion priors from heterogeneous video data into controllable driving g...

</details>

<details>
<summary>Share</summary>

```
HelloWorld: Towards Practical Applications of Generative Driving World Models

Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs.

arXiv: https://arxiv.org/abs/2609.28931
Project page: https://helloworld-4d.github.io

#worldmodels #robotics
```

</details>

---

### [Training Object Permanence in World Models](https://arxiv.org/abs/2609.28654)

**Authors:** Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao et al. (31 authors)

**Published:** 2026-09-23 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28654) | [PDF](https://arxiv.org/pdf/2609.28654) | [Project Page](https://object-permanence.world)

<details>
<summary>Abstract</summary>

Object permanence and solidity are hallmarks of human cognitive priors. Recent studies show that video generation models, a paradigmatic class of current world models, have begun to show emerged reasoning abilities, making them ideal candidates for building human-like physical intelligence. Do video models have emerged object permanence in them? If not, could we train them with a core-cognition inspired dataset? We introduce WROP (World Reasoning with Object Permanence), a data infrastructure of 150 hand-designed cognitive science inspired tasks, divided into six cognitive categories. We build...

</details>

<details>
<summary>Share</summary>

```
Training Object Permanence in World Models

Object permanence and solidity are hallmarks of human cognitive priors.

arXiv: https://arxiv.org/abs/2609.28654
Project page: https://object-permanence.world

#worldmodels #robotics
```

</details>

---

### [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299)

**Authors:** Sinuo Wang, Zichong Gu, Yuhan Huang, Wenxin Wen, Xun Yang et al. (13 authors)

**Published:** 2026-09-22 (updated 2026-09-23) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.26299) | [PDF](https://arxiv.org/pdf/2609.26299)

<details>
<summary>Abstract</summary>

Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizon latent future representations learned with a JEPA-style world model; planning gradients update the...

</details>

<details>
<summary>Share</summary>

```
ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model

Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving.

arXiv: https://arxiv.org/abs/2609.26299

#worldmodels #robotics
```

</details>

---

### [NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models](https://arxiv.org/abs/2609.24313)

**Authors:** Jiajing Lin, Xin Zhang, Jianhua Sun

**Published:** 2026-09-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24313) | [PDF](https://arxiv.org/pdf/2609.24313) | [Code](https://github.com/JiajingLin/NeuIDO)

<details>
<summary>Abstract</summary>

World models aim to capture environmental dynamics and predict future trajectories, showing growing potential for embodied intelligence. Physics-informed 4D generation integrates physical simulation to predict 3D object interactions, offering a promising pathway toward world models. However, this paradigm relies on manually imposed dynamical assumptions rather than internalizing world dynamics, and thus still leaves a gap toward a true world model. To bridge this gap, we propose NeuIDO, a novel world dynamics modeling framework that learns a unified intrinsic dynamics representation from visua...

</details>

<details>
<summary>Share</summary>

```
NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models

World models aim to capture environmental dynamics and predict future trajectories, showing growing potential for embodied intelligence.

arXiv: https://arxiv.org/abs/2609.24313
Code: https://github.com/JiajingLin/NeuIDO

#worldmodels #robotics
```

</details>

---

### [WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436)

**Authors:** Mingkai Jia, Jiaxin Guo, Zhijian Shu, Jiawei Xu, Mingxiao Li et al. (8 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.30436) | [PDF](https://arxiv.org/pdf/2609.30436)

<details>
<summary>Abstract</summary>

Driving world models learn rich predictive representations of the surrounding environment from visual observations, yet accurate visual prediction does not necessarily translate into effective trajectory planning. We argue that a key bottleneck lies in the mismatch between visual world states and raw geometric trajectories, which may limit the planner's ability to exploit action-relevant semantics encoded by the world model. To address this issue, we propose World-Model Alignment for Latent Trajectories (WALT), which learns a compact generative trajectory latent space by transferring informati...

</details>

<details>
<summary>Share</summary>

```
WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving

Driving world models learn rich predictive representations of the surrounding environment from visual observations, yet accurate visual prediction does not necessarily translate into effective trajectory planning.

arXiv: https://arxiv.org/abs/2609.30436

#worldmodels #robotics
```

</details>

---

### [Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage](https://arxiv.org/abs/2609.30214)

**Authors:** Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang et al. (7 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.30214) | [PDF](https://arxiv.org/pdf/2609.30214)

<details>
<summary>Abstract</summary>

We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and context tokens, fuses cross-camera evidence through held-out-view attention, and directly predicts future...

</details>

<details>
<summary>Share</summary>

```
Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage

We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage.

arXiv: https://arxiv.org/abs/2609.30214

#worldmodels #robotics
```

</details>

---

### [InternW0: A Foundational Physical World Model for Efficient Real-World Interactions](https://arxiv.org/abs/2609.27656)

**Authors:** Jisong Cai, Yao Mu, Ganlin Yang, Zhe Cao, Zhangzheng Tu et al. (26 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2609.27656) | [PDF](https://arxiv.org/pdf/2609.27656)

<details>
<summary>Abstract</summary>

Physical intelligence requires more than predicting how the world may evolve: predictions must remain actionable as the world continues to change. We introduce InternW0, the first instantiation of the InternW physical world model series from Shanghai AI Laboratory, built around omnimodal interfaces, asynchronous multi-frequency processing, and local physical modeling under partial observations and external influences. InternW0 jointly learns future visual dynamics and continuous robot control through an asymmetric video--action architecture with flow matching. A high-capacity video expert prov...

</details>

<details>
<summary>Share</summary>

```
InternW0: A Foundational Physical World Model for Efficient Real-World Interactions

Physical intelligence requires more than predicting how the world may evolve: predictions must remain actionable as the world continues to change.

arXiv: https://arxiv.org/abs/2609.27656

#worldmodels #robotics
```

</details>

---

### [Relationally Grounded Latent World Models for Autonomous Driving](https://arxiv.org/abs/2609.24626)

**Authors:** Fabian Schmidt, Markus Enzweiler, Abhinav Valada

**Published:** 2026-09-21 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.24626) | [PDF](https://arxiv.org/pdf/2609.24626)

<details>
<summary>Abstract</summary>

Latent world models learn predictive representations for autonomous driving, but the relational semantics these states preserve often remain implicit. We investigate whether traffic scene graphs can serve as privileged semantic supervision for latent world representations. Building on LAW, we construct actor-centric scene graphs from nuScenes 3D annotations, encode their serialized relational structure using a frozen text embedding model, and align the visual latent representations with this semantic target during training. We remove the supervision branch at inference, so it requires neither...

</details>

<details>
<summary>Share</summary>

```
Relationally Grounded Latent World Models for Autonomous Driving

Latent world models learn predictive representations for autonomous driving, but the relational semantics these states preserve often remain implicit.

arXiv: https://arxiv.org/abs/2609.24626

#worldmodels #robotics
```

</details>

---

### [OneWorld: Learning Consistent Physics Across Actions in World Models](https://arxiv.org/abs/2609.30946)

**Authors:** Ke He, Yichen Ding, Bin Yang

**Published:** 2026-09-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30946) | [PDF](https://arxiv.org/pdf/2609.30946)

<details>
<summary>Abstract</summary>

Action-conditioned video world models aim to predict scene evolution under different actions, a capability that is essential for reliable planning, decision-making, and interaction in dynamic environments. However, futures generated independently from the same initial scene may each appear plausible while implying incompatible physical properties, such as friction or mass. This inconsistency can lead to contradictory predictions across interventions, making it difficult for the model to maintain a coherent understanding of the underlying world and limiting its reliability for planning and deci...

</details>

<details>
<summary>Share</summary>

```
OneWorld: Learning Consistent Physics Across Actions in World Models

Action-conditioned video world models aim to predict scene evolution under different actions, a capability that is essential for reliable planning, decision-making, and interaction in dynamic environments.

arXiv: https://arxiv.org/abs/2609.30946

#worldmodels #robotics
```

</details>

---

### [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](https://arxiv.org/abs/2609.26458)

**Authors:** Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen et al. (10 authors)

**Published:** 2026-09-22 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.26458) | [PDF](https://arxiv.org/pdf/2609.26458) | [Project Page](https://becauseimbatman0.github.io/CoDeR)

<details>
<summary>Abstract</summary>

We introduce \textbf{CoDeR}, a new paradigm for world modeling. Unlike existing video world models that implicitly represent world dynamics through visual observations, our system explicitly constructs an executable world with code and employs video generation models for visual realization. Specifically, we coordinate five complementary roles to translate high-level concepts into structured world rules, executable dynamics, and perceptual observations. This design enables \textit{long-term memory}, \textit{open-ended interactions}, \textit{autonomous world evolution}, and \textit{multi-agent s...

</details>

<details>
<summary>Share</summary>

```
Code Plans, Diffusion Renders: Open-Ended Generative World Modeling

We introduce \textbf{CoDeR}, a new paradigm for world modeling.

arXiv: https://arxiv.org/abs/2609.26458
Project page: https://becauseimbatman0.github.io/CoDeR

#worldmodels #robotics
```

</details>

---

### [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425)

**Authors:** Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang et al. (6 authors)

**Published:** 2026-09-22 (updated 2026-09-23) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.26425) | [PDF](https://arxiv.org/pdf/2609.26425)

<details>
<summary>Abstract</summary>

KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to much larger output degradation. We trace this discrepancy to attention: small Key perturbations can...

</details>

<details>
<summary>Share</summary>

```
QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation

KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency.

arXiv: https://arxiv.org/abs/2609.26425

#worldmodels #robotics
```

</details>

---

### [Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think](https://arxiv.org/abs/2609.30036)

**Authors:** Xvyuan Liu, Jianjie Fang, Chen Gao, Yong Li

**Published:** 2026-09-24 (updated 2026-09-25) | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.30036) | [PDF](https://arxiv.org/pdf/2609.30036)

<details>
<summary>Abstract</summary>

Planners built on visual world models commonly score each predicted outcome by its distance to the encoded goal image. We show that this target can limit control even with exact dynamics and globally optimal short-horizon search: reaching a goal may require actions that initially move away from it. With frozen LeWM models, intermediate targets substantially improve action synthesis and recorded-action ranking on Cube, PushT, Reacher, and TwoRoom. Learned targets and targets drawn from observed experience both produce these gains. We introduce Anchored Planning, which retrieves a recorded segme...

</details>

<details>
<summary>Share</summary>

```
Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think

Planners built on visual world models commonly score each predicted outcome by its distance to the encoded goal image.

arXiv: https://arxiv.org/abs/2609.30036

#worldmodels #robotics
```

</details>

---

### [Frozen Flows Forget: Diagnosing and Restoring Lost Motion in a Latent-flow World Model](https://arxiv.org/abs/2609.28414)

**Authors:** Xiwen Chen, Rigaudiere Z. Li, Zhiruo Zhou, Xiaojun Zhu, Houde Liu

**Published:** 2026-09-23 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.28414) | [PDF](https://arxiv.org/pdf/2609.28414)

<details>
<summary>Abstract</summary>

Latent world models that integrate a flow in a frozen self supervised latent space train stably and cheaply, yet silently lose the property manipulation depends on most: motion. The pretrained flow never moves the manipulated object; retraining it with latent-only losses only trades stillness for teleport-like motion. We trace the failure to the training signal, not the representation: anchor-sparse, latent-only supervision never says where along the horizon change belongs. Decode-augmented rollout training (DART) repairs this while keeping the representation frozen, retraining only the flow w...

</details>

<details>
<summary>Share</summary>

```
Frozen Flows Forget: Diagnosing and Restoring Lost Motion in a Latent-flow World Model

Latent world models that integrate a flow in a frozen self supervised latent space train stably and cheaply, yet silently lose the property manipulation depends on most: motion.

arXiv: https://arxiv.org/abs/2609.28414

#worldmodels #robotics
```

</details>

---

### [Generalizable Robotic Insertion with World Models](https://arxiv.org/abs/2609.28258)

**Authors:** Nicklas Hansen, Iretiayo Akinola, Yijie Guo, Jie Xu, Bingjie Tang et al. (10 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.28258) | [PDF](https://arxiv.org/pdf/2609.28258)

<details>
<summary>Abstract</summary>

Robotic assembly in high-mixture settings requires adaptable systems that can handle diverse parts, yet current approaches typically rely on policies specialized to each insertion task. Although this can reach high success rates, it makes the process of deploying systems for new problems tedious and time consuming. We present a framework for generalizable insertion using world models that combine robot proprioceptive information with raw visual observations captured by a wrist-mounted camera. Our model-based approach trains a single world model on up to 90 insertion tasks with geometrically di...

</details>

<details>
<summary>Share</summary>

```
Generalizable Robotic Insertion with World Models

Robotic assembly in high-mixture settings requires adaptable systems that can handle diverse parts, yet current approaches typically rely on policies specialized to each insertion task.

arXiv: https://arxiv.org/abs/2609.28258

#worldmodels #robotics
```

</details>

---

### [DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](https://arxiv.org/abs/2609.31349)

**Authors:** Haojun Xu, Jie Huang, Xin Lu, Mingchen Zhong, Zihao Fan et al. (7 authors)

**Published:** 2026-09-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.31349) | [PDF](https://arxiv.org/pdf/2609.31349)

<details>
<summary>Abstract</summary>

Large video diffusion models offer expressive priors for embodied prediction and learning, yet their many-step sampling remains costly for interactive downstream use. Distribution Matching Distillation (DMD) enables few-step video generation, but can suppress robot--object motion while preserving visual quality. Examining DMD's teacher and fake-score signals, we find that weak re-noising keeps the teacher posterior concentrated near motion-deficient rollouts, limiting motion-restoring guidance. Meanwhile, stronger-motion rollouts tend to incur larger fake-score fitting errors, which can hinder...

</details>

<details>
<summary>Share</summary>

```
DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models

Large video diffusion models offer expressive priors for embodied prediction and learning, yet their many-step sampling remains costly for interactive downstream use.

arXiv: https://arxiv.org/abs/2609.31349

#worldmodels #robotics
```

</details>

---

### [I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?](https://arxiv.org/abs/2609.31161)

**Authors:** Yuhang Liu, Zhuo Huang, Javen Qinfeng Shi

**Published:** 2026-09-25 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.31161) | [PDF](https://arxiv.org/pdf/2609.31161)

<details>
<summary>Abstract</summary>

Recent empirical and theoretical advances suggest that joint-embedding predictive architectures (JEPAs) may learn meaningful representations for action-conditioned prediction of future outcomes, thus becoming one of the foundational structures for world models. However, accurate prediction does not, in general, necessarily imply recovery of underlying causal states that give rise to the observed dynamics. This work investigates when and how JEPAs can recover the underlying causal states from observations. We first introduce a latent variable model, in which high-dimensional observations are ge...

</details>

<details>
<summary>Share</summary>

```
I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?

Recent empirical and theoretical advances suggest that joint-embedding predictive architectures (JEPAs) may learn meaningful representations for action-conditioned prediction of future outcomes, thus becoming one of t...

arXiv: https://arxiv.org/abs/2609.31161

#worldmodels #robotics
```

</details>

---

### [Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases](https://arxiv.org/abs/2609.30595)

**Authors:** Ashish Sundar, Tiankuo Hou, Zhong Fan, Chunbo Luo, Xiaoyang Wang

**Published:** 2026-09-24 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.30595) | [PDF](https://arxiv.org/pdf/2609.30595)

<details>
<summary>Abstract</summary>

Synchronised action annotations are needed to train controllable world models and these datasets remain elusive. Existing approaches make use of instrumented platforms with calibrated sensors, costly manual annotation, or latent-action models which lack grounding. We instead turn ordinary unlabelled video into action-supervised training data by recovering (without training) a data-derived egomotion basis. We track pixel displacements across frames and exploit the recurring coherent structure induced by egomotion to obtain grounded control signals directly. Using a method as simple as principal...

</details>

<details>
<summary>Share</summary>

```
Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases

Synchronised action annotations are needed to train controllable world models and these datasets remain elusive.

arXiv: https://arxiv.org/abs/2609.30595

#worldmodels #robotics
```

</details>

---

### [Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies](https://arxiv.org/abs/2609.28670)

**Authors:** Alex Schutz, Nick Hawes, Victor-Alexandru Darvariu

**Published:** 2026-09-23 | **Categories:** cs.LG, cs.AI, cs.SI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.28670) | [PDF](https://arxiv.org/pdf/2609.28670)

<details>
<summary>Abstract</summary>

Graph-based world models have recently emerged as a means of learning transitions over relational state representations. However, existing approaches are largely limited to fixed-topology graphs or deterministic, fully observable environments. We propose the Graph Dynamics Model (GDM), a world model for graph-structured observations that is designed to handle the more general setting of evolving topologies in stochastic and partially observable environments. The GDM uses a sparse recurrent adjacency matrix to model topology updates and perform message passing, together with a recurrent state-s...

</details>

<details>
<summary>Share</summary>

```
Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies

Graph-based world models have recently emerged as a means of learning transitions over relational state representations.

arXiv: https://arxiv.org/abs/2609.28670

#worldmodels #robotics
```

</details>

---

### [SHRAV: State-Hypothesis-Reason-Action-Verify Framework for Physical Modeling and Inverse Design](https://arxiv.org/abs/2609.27621)

**Authors:** Ziheng Guo, Yang Bu

**Published:** 2026-09-23 (updated 2026-09-24) | **Categories:** cs.AI, cs.CE, physics.comp-ph | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.27621) | [PDF](https://arxiv.org/pdf/2609.27621)

<details>
<summary>Abstract</summary>

Physical modeling and inverse design require computation that can continue from reusable state. We introduce SHRAV, an architecture-independent computational framework organized around State, Hypothesis, Reason, Action, and Verify. Its central mechanism is a state-continuation core with declared reuse boundaries and explicit roles for learned evolution and numerical quantities. Forward configurations evolve predictive state and read out physical responses; inverse-design configurations additionally generate target-directed modifications and consume evaluator feedback. Electromagnetic world-mod...

</details>

<details>
<summary>Share</summary>

```
SHRAV: State-Hypothesis-Reason-Action-Verify Framework for Physical Modeling and Inverse Design

Physical modeling and inverse design require computation that can continue from reusable state.

arXiv: https://arxiv.org/abs/2609.27621

#worldmodels #robotics
```

</details>

---

### [Dual-Frontier: When Can an Agent Trust Its World Model?](https://arxiv.org/abs/2609.26293)

**Authors:** Huatai Zhu, Qiang Chen, Ziqian Kou, Wenhao Li, Fei Wang et al. (8 authors)

**Published:** 2026-09-22 (updated 2026-09-24) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.26293) | [PDF](https://arxiv.org/pdf/2609.26293)

<details>
<summary>Abstract</summary>

Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove that its components are not identifiable from passive interaction, even for finite-horizon planners....

</details>

<details>
<summary>Share</summary>

```
Dual-Frontier: When Can an Agent Trust Its World Model?

Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error.

arXiv: https://arxiv.org/abs/2609.26293

#worldmodels #robotics
```

</details>

---

### [A JEPA Recipe for Tabular Foundation Models](https://arxiv.org/abs/2609.25541)

**Authors:** Mingyu Jeon, Suwan Cho, Jae Young Suh

**Published:** 2026-09-22 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.25541) | [PDF](https://arxiv.org/pdf/2609.25541)

<details>
<summary>Abstract</summary>

Tabular foundation models learn to predict cell values in context, whereas world-model self-supervision asks for prediction in representation space (LeCun, 2022; Assran et al., 2023). On a tabular foundation-model prior, the latent term of a joint-embedding predictive architecture (JEPA) collapsed in our earlier runs and took the encoder with it to a constant map. We report a recipe under which the latent term survives to convergence beside the value objective: the value head reads the encoder field rather than the predictor, and the target is an exponential moving average (EMA) difference. To...

</details>

<details>
<summary>Share</summary>

```
A JEPA Recipe for Tabular Foundation Models

Tabular foundation models learn to predict cell values in context, whereas world-model self-supervision asks for prediction in representation space (LeCun, 2022; Assran et al., 2023).

arXiv: https://arxiv.org/abs/2609.25541

#worldmodels #robotics
```

</details>

---

### [UniK: Universal Knowledge Perception for Digital and Physical AI](https://arxiv.org/abs/2609.23971)

**Authors:** Nirmit Desai, Kunal Sawarkar, Aditya Mahakali, Dongkon Lee, Kevin Park et al. (6 authors)

**Published:** 2026-09-21 | **Categories:** cs.AI, cs.CV, cs.IR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.23971) | [PDF](https://arxiv.org/pdf/2609.23971)

<details>
<summary>Abstract</summary>

Two transformative classes of AI systems are reshaping how organizations operate: \textit{digital AI}, which reasons over enterprise knowledge to power chatbots and agent workflows; and \textit{physical AI}, which learns to control robots and autonomous systems from video, gameplay, and sensor telemetry. Both face the same foundational bottleneck: raw knowledge at scale, spanning heterogeneous modalities, locked in private corpora that existing AI infrastructure cannot access reliably or efficiently. We propose \textit{Universal Knowledge Perception (UniK)} as a common platform for both classe...

</details>

<details>
<summary>Share</summary>

```
UniK: Universal Knowledge Perception for Digital and Physical AI

Two transformative classes of AI systems are reshaping how organizations operate: \textit{digital AI}, which reasons over enterprise knowledge to power chatbots and agent workflows; and \textit{physical AI}, which lea...

arXiv: https://arxiv.org/abs/2609.23971

#worldmodels #robotics
```

</details>

---

### [Sim-to-Real Aware End-to-End Learning Environment for Micromobility](https://arxiv.org/abs/2609.28969)

**Authors:** Shouma Amano, Takuya Azumi

**Published:** 2026-09-24 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.28969) | [PDF](https://arxiv.org/pdf/2609.28969)

<details>
<summary>Abstract</summary>

While end-to-end autonomous driving systems show promise, their application to micromobility vehicles is hindered by simulators failing to capture specific kinematics, such as differential drives and omni-wheels. This paper pro- poses a sim-to-real-aware, vehicle-specific end-to-end learning environment for the WHILL Model CR on AWSIM and ROS 2. To minimize the sim-to-real gap, physical parameters are optimized via Bayesian optimization using real-world data, reducing trajectory errors across various driving scenarios. Additionally, this study introduces a synchronized architecture tailored fo...

</details>

<details>
<summary>Share</summary>

```
Sim-to-Real Aware End-to-End Learning Environment for Micromobility

While end-to-end autonomous driving systems show promise, their application to micromobility vehicles is hindered by simulators failing to capture specific kinematics, such as differential drives and omni-wheels.

arXiv: https://arxiv.org/abs/2609.28969

#worldmodels #robotics
```

</details>

---

### [AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution](https://arxiv.org/abs/2609.31133)

**Authors:** Tian Luo, Ruge Zhang, Haozhi Han, Yifrng Chen, Yunquan Zhang et al. (8 authors)

**Published:** 2026-09-25 | **Categories:** cs.AI, cond-mat.mtrl-sci | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.31133) | [PDF](https://arxiv.org/pdf/2609.31133)

<details>
<summary>Abstract</summary>

High-fidelity atomistic evolution over long timescales requires more than observing the current crystal configuration. Instantaneous atomistic snapshots are often incomplete: locally similar configurations can correspond to different hidden dynamical contexts, future event preferences, and waiting-time scales. We argue that this snapshot ambiguity makes long-horizon atomistic evolution fundamentally a memory-based world-state restoration problem. To address this, we introduce AtomWorld-Mem, a memory-restored atomistic world model that recovers the latent world state missing from instantaneous...

</details>

<details>
<summary>Share</summary>

```
AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution

High-fidelity atomistic evolution over long timescales requires more than observing the current crystal configuration.

arXiv: https://arxiv.org/abs/2609.31133

#worldmodels #robotics
```

</details>

---

### [From S3Q Theory to Implementation: Towards an Architecture for Machine Qualia](https://arxiv.org/abs/2609.30743)

**Authors:** Tetiana Grinberg, Katrina Schleisman, Patryk Laurent, Bogdan Udrea, Minda Myers et al. (9 authors)

**Published:** 2026-09-25 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.30743) | [PDF](https://arxiv.org/pdf/2609.30743)

<details>
<summary>Abstract</summary>

A key challenge in machine consciousness research is translating theoretical models into computational-level implementations. In this paper, we address this challenge by proposing a five-layer implementation architecture for the S3Q (Simulated, Situated, Structurally Coherent) theory of consciousness. Rather than introducing novel formalisms, the architecture composes published computational primitives into a single pipeline. S3Q identifies three jointly necessary conditions for qualia: (1) grounded sensorimotor situatedness, (2) internal simulation via a world model, and (3) structural cohere...

</details>

<details>
<summary>Share</summary>

```
From S3Q Theory to Implementation: Towards an Architecture for Machine Qualia

A key challenge in machine consciousness research is translating theoretical models into computational-level implementations.

arXiv: https://arxiv.org/abs/2609.30743

#worldmodels #robotics
```

</details>

---

### [Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation](https://arxiv.org/abs/2609.30650)

**Authors:** Shengjun Zhang, Tingyi Liu, Dong Xie, Yunlong Dong, Xiang Wang et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.LG, cs.AI, stat.ML | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.30650) | [PDF](https://arxiv.org/pdf/2609.30650)

<details>
<summary>Abstract</summary>

Task performance need not determine which intervention mechanism an agent retains. We study causal retention: whether a frozen learned state answers a mechanism-probe map fixed independently of training, including action, context, direct target, value, and delay. For finite structural causal model classes, the optimal probe error is a Bayes decision risk. It vanishes exactly when every learning-interface fiber lies within one probe-answer fiber; any state obtained by post-processing that interface inherits the same lower bound. A posterior-coverage theorem characterizes budgeted retesting, whi...

</details>

<details>
<summary>Share</summary>

```
Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation

Task performance need not determine which intervention mechanism an agent retains.

arXiv: https://arxiv.org/abs/2609.30650

#worldmodels #robotics
```

</details>

---

### [HappyWorld-Bench](https://arxiv.org/abs/2609.24308)

**Authors:** Zhiqi Bai, Junai Cai, Yixin Chen, Jingrun Du, Tao Feng et al. (36 authors)

**Published:** 2026-09-21 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.24308) | [PDF](https://arxiv.org/pdf/2609.24308)

<details>
<summary>Abstract</summary>

Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification. We introduce HappyWorld-Bench, a comprehensive benchmark that evaluates whether generated worlds remain reliable as agents interact with them. Our design is built on a hierarchical capability framework of six world capabilities (W1-W6), from generative construction to unified world modeling, instantiated across three independent evaluation tracks: video world models, spatial world models, and embodied world models. Ha...

</details>

<details>
<summary>Share</summary>

```
HappyWorld-Bench

Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification.

arXiv: https://arxiv.org/abs/2609.24308

#worldmodels #robotics
```

</details>

---
