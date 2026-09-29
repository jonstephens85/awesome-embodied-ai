# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-09-29 01:20 UTC

**Papers shown:** 41 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [HapticWorld: an Interactive World Simulator with Real-time Torque Feedback](https://arxiv.org/abs/2609.31924)

**Authors:** Shaoting Peng, Litian Liang, Yixuan Wang, Ming Yang, Katherine Driggs-Campbell et al. (7 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world simulator" in title; 2 distinct keyword hits; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.31924) | [PDF](https://arxiv.org/pdf/2609.31924) | [Project Page](https://haptic-world.github.io/)

<details>
<summary>Abstract</summary>

Contact-rich manipulation depends on force sensing that is hard to infer from visual signals alone, both for collecting demonstrations and for training policies. Force-annotated data, however, remains hard to obtain at scale: real-robot collection ties every demonstration to physical hardware, physics simulators report contact forces that deviate systematically from real measurements, and learned world simulators, though scalable and realistic, are vision-only, so operators feel nothing during data collection and the data carries no force/torque (F/T) labels. We present HapticWorld, an interac...

</details>

<details>
<summary>Share</summary>

```
HapticWorld: an Interactive World Simulator with Real-time Torque Feedback

Contact-rich manipulation depends on force sensing that is hard to infer from visual signals alone, both for collecting demonstrations and for training policies.

arXiv: https://arxiv.org/abs/2609.31924
Project page: https://haptic-world.github.io/

#worldmodels #robotics
```

</details>

---

### [Scanning While Imagining: A Scene-Graph World Model for Robotic Ultrasound Navigation](https://arxiv.org/abs/2609.32837)

**Authors:** Xuesong Li, Shuai Chen, Feng Li, Zhongliang Jiang, Nassir Navab et al. (6 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.32837) | [PDF](https://arxiv.org/pdf/2609.32837) | [Project Page](https://noseefood.github.io/us-sonograph-wm/)

<details>
<summary>Abstract</summary>

Ultrasound (US) acquisition depends on the operator's ability to interpret anatomy and anticipate how the view will change with probe motion. Many robotic US navigation methods select actions without explicitly predicting these anatomical changes. We propose SonoGraph-WM, an action- and goal-conditioned world model for anticipatory probe navigation. The model represents anatomy as scene graphs (SGs), capturing visible structures, their geometry, and spatial relationships without synthesizing US images. Given a history of SGs and probe poses, a unified Transformer jointly predicts future SGs an...

</details>

<details>
<summary>Share</summary>

```
Scanning While Imagining: A Scene-Graph World Model for Robotic Ultrasound Navigation

Ultrasound (US) acquisition depends on the operator's ability to interpret anatomy and anticipate how the view will change with probe motion.

arXiv: https://arxiv.org/abs/2609.32837
Project page: https://noseefood.github.io/us-sonograph-wm/

#worldmodels #robotics
```

</details>

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

### [TriO: Tri-Modal Unsupervised Occupancy World Model for Anything Perception](https://arxiv.org/abs/2609.32013)

**Authors:** Quinlan Sykora, Sourav Biswas, Christopher Diehl, Andrew Cunningham, Thomas Gilles et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.32013) | [PDF](https://arxiv.org/pdf/2609.32013)

<details>
<summary>Abstract</summary>

We present TriO, a multi-modal unsupervised world model that predicts 4D occupancy, obstacle segmentation, flow and LiDAR. In contrast to prior work, TriO utilizes three distinct sensor modalities (camera, LiDAR, and RADAR) as both inputs and sources of self-supervision, eliminating the need for additional human annotations. Thanks to its novel supervision, the model is able to segment any occupancy from the drivable surface, overcoming the limitations of existing open-set methods in handling long-tail objects. TriO achieves state-of-the-art results in multiple 3D and 4D tasks, including occup...

</details>

<details>
<summary>Share</summary>

```
TriO: Tri-Modal Unsupervised Occupancy World Model for Anything Perception

We present TriO, a multi-modal unsupervised world model that predicts 4D occupancy, obstacle segmentation, flow and LiDAR.

arXiv: https://arxiv.org/abs/2609.32013

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

### [The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models](https://arxiv.org/abs/2609.32679)

**Authors:** Dongsheng Liu, Chao Jin, Wenkui Yang, Hejin Wang, Junwei Yang et al. (10 authors)

**Published:** 2026-09-26 | **Categories:** cs.LG, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.32679) | [PDF](https://arxiv.org/pdf/2609.32679)

<details>
<summary>Abstract</summary>

GUI World Models (GUI-WMs) are increasingly used to predict future states for agent planning and simulation, yet most existing formulations condition only on the current GUI observation and action. We identify state aliasing, where the vis- ible interface omits transition-relevant environment state, so identical observable conditions can correspond to different valid futures. To diagnose this failure mode, we introduce StateAliasBench, a diagnostic benchmark that explicitly isolates such ambiguities via strict pairing. We further propose lightweight predictive- state recovery that infers struc...

</details>

<details>
<summary>Share</summary>

```
The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models

GUI World Models (GUI-WMs) are increasingly used to predict future states for agent planning and simulation, yet most existing formulations condition only on the current GUI observation and action.

arXiv: https://arxiv.org/abs/2609.32679

#worldmodels #robotics
```

</details>

---

### [World Models with Predictable Long-Horizon Marginals](https://arxiv.org/abs/2609.32657)

**Authors:** Yuhao Du, Shunian Chen

**Published:** 2026-09-26 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.32657) | [PDF](https://arxiv.org/pdf/2609.32657)

<details>
<summary>Abstract</summary>

Accurate one-step predictions do not ensure that a world model's rollouts retain the data distribution. We make the model's decoded stationary law explicit by learning a decoder of a fixed Gaussian reference and constraining the behaviour-averaged transition to preserve that reference. For controlled systems, a joint transition uses a conditional action chart to preserve behaviour occupancy without requiring invariance at each fixed action. Joint state--action rotations and parallel Gaussian noise give an exactly preserving transition with a tractable conditional density. We derive an absolute...

</details>

<details>
<summary>Share</summary>

```
World Models with Predictable Long-Horizon Marginals

Accurate one-step predictions do not ensure that a world model's rollouts retain the data distribution.

arXiv: https://arxiv.org/abs/2609.32657

#worldmodels #robotics
```

</details>

---

### [Not All Errors Matter: Decision-Relevant Prediction Error Predicts Planning Quality](https://arxiv.org/abs/2609.32322)

**Authors:** Linhao Wang, Yiyan Fan, Dongjin Huang

**Published:** 2026-09-26 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.32322) | [PDF](https://arxiv.org/pdf/2609.32322)

<details>
<summary>Abstract</summary>

World models are typically trained and evaluated by prediction error, assuming that more accurate predictions lead to better decisions. We show that this assumption can fail because models with similar total error can differ substantially in planning performance when their errors occur on different state dimensions. We introduce Decision-Relevant Prediction Error (DRPE), which measures prediction error on the state dimensions that affect decisions. We also develop an iso-error evaluation protocol that varies error allocation while keeping total error fixed. In a factored gridworld with known s...

</details>

<details>
<summary>Share</summary>

```
Not All Errors Matter: Decision-Relevant Prediction Error Predicts Planning Quality

World models are typically trained and evaluated by prediction error, assuming that more accurate predictions lead to better decisions.

arXiv: https://arxiv.org/abs/2609.32322

#worldmodels #robotics
```

</details>

---

### [Cache-Aware Conv3D Lowering Across Embedded World-Model Decoders](https://arxiv.org/abs/2609.31938)

**Authors:** Jiaming Zhang, Wu Yang, Shuai Tao, Wulong Liu

**Published:** 2026-09-25 | **Categories:** cs.LG, cs.PF | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.31938) | [PDF](https://arxiv.org/pdf/2609.31938)

<details>
<summary>Abstract</summary>

Generative world models can provide visual rollouts for embodied planning, yet their feasibility on edge devices depends not only on the learned model but also on how the execution runtime represents its operations. We introduce a cache-aware lowering that expresses supported causal Conv3D calls as batched spatial Conv2D operations while preserving pretrained weights, temporal-cache semantics, convolution parameters, bias placement, and output layout. Across the complete Cosmos3-Edge image-to-video pipeline on a 64-GB NVIDIA Jetson AGX Orin, the proposed route accelerates VAE decoding by appro...

</details>

<details>
<summary>Share</summary>

```
Cache-Aware Conv3D Lowering Across Embedded World-Model Decoders

Generative world models can provide visual rollouts for embodied planning, yet their feasibility on edge devices depends not only on the learned model but also on how the execution runtime represents its operations.

arXiv: https://arxiv.org/abs/2609.31938

#worldmodels #robotics
```

</details>

---

### [CyberWorld: World Models for Sample-Efficient Autonomous Cyber Defense](https://arxiv.org/abs/2609.31893)

**Authors:** Ryozo Masukawa, Sanggeon Yun, Raheeb Hassan, Hyunwoo Oh, SungHeon Jeong et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.LG, cs.AI, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.31893) | [PDF](https://arxiv.org/pdf/2609.31893)

<details>
<summary>Abstract</summary>

Deep reinforcement learning has become a prominent approach to autonomous cyber defense. Existing methods are predominantly model-free and consequently require extensive environment interaction. World models provide an alternative by learning predictive dynamics and optimizing policies through imagined trajectories, yielding substantial gains in sample efficiency in robotics and embodied control. Extending this paradigm to cybersecurity raises a fundamental question: what should constitute the "world" in a cyber world model? We introduce CyberWorld, a Dreamer-style world modeling framework tha...

</details>

<details>
<summary>Share</summary>

```
CyberWorld: World Models for Sample-Efficient Autonomous Cyber Defense

Deep reinforcement learning has become a prominent approach to autonomous cyber defense.

arXiv: https://arxiv.org/abs/2609.31893

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

### [Think Fast, Plan Selectively: Adaptive Deliberation for Efficient Data-Driven MPC](https://arxiv.org/abs/2609.32591)

**Authors:** Yi Xian Goh, Sze Jue Yang, Hao Luan

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.32591) | [PDF](https://arxiv.org/pdf/2609.32591)

<details>
<summary>Abstract</summary>

Data-driven model predictive control (MPC) combines learned world models with online trajectory optimization, achieving strong performance in continuous control. However, the per-step cost of sampling and evaluating hundreds of candidate trajectories restricts deployment to control frequencies well below what real-time robotics demands. Motivated by the dual-process theory of human cognition, which distinguishes between fast, intuitive processing (System 1) and slower, deliberative reasoning (System 2), we ask whether every decision requires the same degree of computational deliberation. We pr...

</details>

<details>
<summary>Share</summary>

```
Think Fast, Plan Selectively: Adaptive Deliberation for Efficient Data-Driven MPC

Data-driven model predictive control (MPC) combines learned world models with online trajectory optimization, achieving strong performance in continuous control.

arXiv: https://arxiv.org/abs/2609.32591

#worldmodels #robotics
```

</details>

---

### [WSM-Aware HRI: An IoT-Enhanced Framework for Early Detection and Norm-Guided Repair of Failures with LLM Guidance](https://arxiv.org/abs/2609.32336)

**Authors:** Hanlin Zhang, Yuquan Wang, Tianwei Zhang, Zhenglong Sun

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.HC | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.32336) | [PDF](https://arxiv.org/pdf/2609.32336)

<details>
<summary>Abstract</summary>

Human-robot interaction (HRI) failures remain a major barrier to deploying robots in real-world environments. Prior work often treats failures as isolated technical faults or focuses on post-hoc recovery behaviors. In practice, many breakdowns arise because humans and robots operate under inconsistent assumptions about the current world state. We propose WSM-Aware HRI, an IoT-enhanced modular framework that unifies diverse HRI breakdowns as World-State Mismatches (WSMs) between a human's instruction-implied assumptions and a robot's grounded world model built from multimodal perception and dig...

</details>

<details>
<summary>Share</summary>

```
WSM-Aware HRI: An IoT-Enhanced Framework for Early Detection and Norm-Guided Repair of Failures with LLM Guidance

Human-robot interaction (HRI) failures remain a major barrier to deploying robots in real-world environments.

arXiv: https://arxiv.org/abs/2609.32336

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

### [What Do Latent Predictive Vehicle Representations Retain? Measuring State, Geometry, and Local Response](https://arxiv.org/abs/2609.32512)

**Authors:** Enzo Nicolás Spotorno, Josafat Leal Filho, Antônio Augusto Fröhlich

**Published:** 2026-09-26 | **Categories:** cs.LG, eess.SY | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.32512) | [PDF](https://arxiv.org/pdf/2609.32512)

<details>
<summary>Abstract</summary>

Models of vehicle dynamics learned from logged states and commands complement physics-based models, and latent world models, which predict in a learned representation, are used to plan and train controllers in other domains. Vehicle controllers are usually specified in physical terms: costs, limits, and references depend on position, yaw angle, speed, and yaw rate, and the optimizer compares or differentiates predicted outcomes across nearby commands. A latent model placed in such a controller must therefore let these quantities be recovered and must change its predictions with commands as the...

</details>

<details>
<summary>Share</summary>

```
What Do Latent Predictive Vehicle Representations Retain? Measuring State, Geometry, and Local Response

Models of vehicle dynamics learned from logged states and commands complement physics-based models, and latent world models, which predict in a learned representation, are used to plan and train controllers in other d...

arXiv: https://arxiv.org/abs/2609.32512

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
