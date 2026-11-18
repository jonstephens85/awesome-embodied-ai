# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-18 22:50 UTC

**Papers shown:** 56 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [JEPA4R: Embodied JEPA World Models with 4D Point Planning](https://arxiv.org/abs/2611.19771)

**Authors:** Jiarui Dong, Zhiheng Liang, Yanjun Li, Zeyu Zhang, Heejeong Nam et al. (7 authors)

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★★

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19771) | [PDF](https://arxiv.org/pdf/2611.19771) | [Project Page](https://aigeeksgroup.github.io/JEPA4R) | [Code](https://github.com/AIGeeksGroup/JEPA4R)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that observes single-depth-camera point clouds, predicts and plans in their latent space, and acts through a policy head on its frozen latents; we call this 4D point planning. A decoder on...

</details>

<details>
<summary>Share</summary>

```
JEPA4R: Embodied JEPA World Models with 4D Point Planning

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space.

arXiv: https://arxiv.org/abs/2611.19771
Project page: https://aigeeksgroup.github.io/JEPA4R
Code: https://github.com/AIGeeksGroup/JEPA4R

#worldmodels #robotics
```

</details>

---

### [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.16579)

**Authors:** Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu et al. (13 authors)

**Published:** 2026-11-12 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16579) | [PDF](https://arxiv.org/pdf/2611.16579) | [Project Page](https://adept-thu.github.io/ActWorld-JEPA/) | [Code](https://github.com/adept-thu/ActWorld-JEPA)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction. However, latent predictive consistency alone does not establish the relative driving quality of candidate plans. We present ActWorld-JEPA, a joint-embedding formulation for candidate-based driving. Where Plan-Conditioned JEPA (PC-JEPA) uses global and step-wise trajectory intentions to guide recurrent latent prediction, then combines the predicted future with the current scene through gated cross-attention; Relational Residual Reranking ($R^3$) models agreement and discrepanc...

</details>

<details>
<summary>Share</summary>

```
ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving

Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction.

arXiv: https://arxiv.org/abs/2611.16579
Project page: https://adept-thu.github.io/ActWorld-JEPA/
Code: https://github.com/adept-thu/ActWorld-JEPA

#worldmodels #robotics
```

</details>

---

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

### [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](https://arxiv.org/abs/2611.20107)

**Authors:** Yansong Qu, Zilin Huang, Zihao Sheng, Sikai Chen, Samuel Labi

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.20107) | [PDF](https://arxiv.org/pdf/2611.20107) | [Project Page](https://ys-qu.github.io/safer-website)

<details>
<summary>Abstract</summary>

An autonomous vehicle must foresee the consequences of its actions, especially in the rare, time-critical situations where crashes happen. A world model offers this foresight, but only within the coverage of its training data, which poses an exploration-exploitation dilemma. Within this coverage a planner can hardly improve on the data, and beyond it the model's errors mislead it. Logs of competent driving rarely contain the failures that would widen the coverage, and agents that learn from interaction gain them only by failing themselves, without being shown what to do instead. We propose SAF...

</details>

<details>
<summary>Share</summary>

```
SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving

An autonomous vehicle must foresee the consequences of its actions, especially in the rare, time-critical situations where crashes happen.

arXiv: https://arxiv.org/abs/2611.20107
Project page: https://ys-qu.github.io/safer-website

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

### [Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](https://arxiv.org/abs/2611.22691)

**Authors:** Jia Hu, Yang Chang, Panqu Wang, Zhijun Fu, Chang Liu et al. (7 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22691) | [PDF](https://arxiv.org/pdf/2611.22691)

<details>
<summary>Abstract</summary>

World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and the ego visual observations. We propose a closed-loop interactive WM that couples behavior modeling and visual rendering. First, imitation-learned background-vehicle (BV) policies are fine-tuned with multi-agent reinforcement learning in the closed loop against an end-to-end ego plann...

</details>

<details>
<summary>Share</summary>

```
Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving

World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions.

arXiv: https://arxiv.org/abs/2611.22691

#worldmodels #robotics
```

</details>

---

### [Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models](https://arxiv.org/abs/2611.21517)

**Authors:** Itamar Mishani, Mukund Krishnakumar, Oren Salzman, Maxim Likhachev

**Published:** 2026-11-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.21517) | [PDF](https://arxiv.org/pdf/2611.21517)

<details>
<summary>Abstract</summary>

Long-horizon manipulation tasks require a robot to perform a sequence of physical interactions with its environment, typically combining several different skills. Planning such behaviors efficiently is challenging: given a library of parameterized skills, solutions lie in a vast hybrid space of skill sequences and their parameters, and evaluating each candidate skill's feasibility and effect with a high-fidelity world model such as a physics simulator is computationally expensive. MOSAIC, a recent skill-centric approach, lets the skills guide a non-sequential search toward the regions of this...

</details>

<details>
<summary>Share</summary>

```
Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models

Long-horizon manipulation tasks require a robot to perform a sequence of physical interactions with its environment, typically combining several different skills.

arXiv: https://arxiv.org/abs/2611.21517

#worldmodels #robotics
```

</details>

---

### [Successive Convexification in Learned World Models for Safe Offline Planning](https://arxiv.org/abs/2611.19466)

**Authors:** Samuel Younger

**Published:** 2026-11-14 | **Categories:** cs.LG, cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19466) | [PDF](https://arxiv.org/pdf/2611.19466) | [Code](https://github.com/youngers2006/scwm)

<details>
<summary>Abstract</summary>

World models learned from offline data allow an agent to plan without further interaction with the environment, but the sampling-based planners used with them handle safety constraints only by scoring or rejecting sampled action sequences. We instead pose safe planning in the latent space of a learned world model as a successive convex program (SCP), in which a learned discrete-time control barrier function is imposed as a constraint at every step of the horizon. SCP requires smooth dynamics, so we build the networks from smoothed MaxMin activations and spectrally normalised layers, and bound...

</details>

<details>
<summary>Share</summary>

```
Successive Convexification in Learned World Models for Safe Offline Planning

World models learned from offline data allow an agent to plan without further interaction with the environment, but the sampling-based planners used with them handle safety constraints only by scoring or rejecting sam...

arXiv: https://arxiv.org/abs/2611.19466
Code: https://github.com/youngers2006/scwm

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

### [Inertial Video World Models](https://arxiv.org/abs/2611.22314)

**Authors:** Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang et al. (7 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.22314) | [PDF](https://arxiv.org/pdf/2611.22314) | [Code](https://github.com/YuanGao-YG/InertialWorld)

<details>
<summary>Abstract</summary>

The physical world has inertia: it evolves from what already exists rather than being recreated at every instant. However, many existing video world models lack an explicit mechanism for inertial state evolution, leaving the continuity of motion and structure implicit in video prediction. During autoregressive rollouts, repeated reconstruction can accumulate errors and destabilize the predicted dynamics. To address this limitation, we introduce InertialWorld, an Inertial Video World Model that makes inertia a structural prior for autoregressive prediction: existing scene evidence is carried ac...

</details>

<details>
<summary>Share</summary>

```
Inertial Video World Models

The physical world has inertia: it evolves from what already exists rather than being recreated at every instant.

arXiv: https://arxiv.org/abs/2611.22314
Code: https://github.com/YuanGao-YG/InertialWorld

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

### [Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning](https://arxiv.org/abs/2611.22483)

**Authors:** Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li, Zishen Wan, Christopher Torng

**Published:** 2026-11-17 | **Categories:** cs.AR, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22483) | [PDF](https://arxiv.org/pdf/2611.22483)

<details>
<summary>Abstract</summary>

JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one planning step can take tens of seconds. We observe substantial latent locality in this repeated-inference workload: the predictor maps close actions to close latents, and inside a quantized predictor this closeness takes a form that hardware can exploit, differential bit-level sparsity. Unlike an input stream, whose temp...

</details>

<details>
<summary>Share</summary>

```
Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning

JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens o...

arXiv: https://arxiv.org/abs/2611.22483

#worldmodels #robotics
```

</details>

---

### [FailureGen: Scalable Robot Failure Data Generation with World Models](https://arxiv.org/abs/2611.22367)

**Authors:** Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22367) | [PDF](https://arxiv.org/pdf/2611.22367)

<details>
<summary>Abstract</summary>

Robot failures are difficult to collect at scale, limiting the range of failure scenarios represented in robot learning datasets. We present FailureGen, a method for generating synthetic videos with temporal event annotations by reusing action trajectories from recorded failures. The method comprises four stages: (1) fine-tuning an action-conditioned Cosmos world model on successful and failed real executions; (2) annotating source recordings to identify failure-associated donor segments and compatible successful hosts; (3) transferring donor motion into host contexts, with optional spatial of...

</details>

<details>
<summary>Share</summary>

```
FailureGen: Scalable Robot Failure Data Generation with World Models

Robot failures are difficult to collect at scale, limiting the range of failure scenarios represented in robot learning datasets.

arXiv: https://arxiv.org/abs/2611.22367

#worldmodels #robotics
```

</details>

---

### [ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space](https://arxiv.org/abs/2611.22077)

**Authors:** R. Gnana Praveen, Ali Rouzbayani, Zhiying Jiang, Bidhan Roy

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22077) | [PDF](https://arxiv.org/pdf/2611.22077)

<details>
<summary>Abstract</summary>

Videos provide a rich source of physical interaction for learning robot behavior without action annotations, yet effective latent actions must capture not only local transitions but also how those transitions evolve over time. We introduce ReLAP, a latent-action pretraining framework that couples local transition learning with recurrent multi-step prediction in a frozen JEPA representation space. A shared inverse dynamics model infers compact continuous latent actions from adjacent observations, while a latent world model recurrently predicts the future JEPA features. Because each predicted fe...

</details>

<details>
<summary>Share</summary>

```
ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space

Videos provide a rich source of physical interaction for learning robot behavior without action annotations, yet effective latent actions must capture not only local transitions but also how those transitions evolve o...

arXiv: https://arxiv.org/abs/2611.22077

#worldmodels #robotics
```

</details>

---

### [DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects](https://arxiv.org/abs/2611.22001)

**Authors:** Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik et al. (7 authors)

**Published:** 2026-11-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.22001) | [PDF](https://arxiv.org/pdf/2611.22001) | [Project Page](https://www.yimingdou.com/DreamFAR/)

<details>
<summary>Abstract</summary>

World models have shown great potential in serving as a simulator for robot manipulation. However, existing models are either fit to a single environment or lack ability to simulate long-horizon contact-rich events. We present DreamFAR, a world model whose dynamics model is trained from scratch on a large robot-native teleoperation dataset, with no internet-video pretraining. We present an architecture and learning recipe designed for training on robot-native data. DreamFAR is significantly smaller than the high-performance video generation models, yet shows better understanding of contact and...

</details>

<details>
<summary>Share</summary>

```
DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects

World models have shown great potential in serving as a simulator for robot manipulation.

arXiv: https://arxiv.org/abs/2611.22001
Project page: https://www.yimingdou.com/DreamFAR/

#worldmodels #robotics
```

</details>

---

### [The Flip Test: Video World Models Fail to Learn the World State](https://arxiv.org/abs/2611.19822)

**Authors:** Mi Luo, Lijun Yu, Adams Wei Yu, Ang Cao, Baochen Sun et al. (13 authors)

**Published:** 2026-11-15 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19822) | [PDF](https://arxiv.org/pdf/2611.19822) | [Project Page](https://flip-test.github.io/)

<details>
<summary>Abstract</summary>

Video world models promise to predict the future of a scene from its present. Do current models keep this promise? We probe this question counterfactually. When a small change to the present flips the future, such as a box resting a few millimeters before or past a table edge, a model that tracks the state of the world must flip its prediction too. We build FlipTest, a three-level hierarchy of increasingly strict tests over 1,680 initial frames from 10 simulated and 15 real-world tasks. At the base, visual minimal pairs, two nearly identical frames whose true futures differ, test whether predi...

</details>

<details>
<summary>Share</summary>

```
The Flip Test: Video World Models Fail to Learn the World State

Video world models promise to predict the future of a scene from its present.

arXiv: https://arxiv.org/abs/2611.19822
Project page: https://flip-test.github.io/

#worldmodels #robotics
```

</details>

---

### [What World Model Does Active Object Search Need? A Study under Imperfect Detection](https://arxiv.org/abs/2611.15689)

**Authors:** Kyeongryeol Go

**Published:** 2026-11-11 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15689) | [PDF](https://arxiv.org/pdf/2611.15689) | [Code](https://github.com/gokyeongryeol/BAMOS)

<details>
<summary>Abstract</summary>

In active object search, a robot must decide where to look and when to stop. Imperfect detection complicates both decisions: a non-detection may indicate occlusion, an out-of-view target, or a false negative, while a detection may be a false positive. This raises the question of which representations a world model needs to support reliable search under imperfect detection. We introduce Bayesian Active Miss-aware Object Search (BAMOS) to investigate how target belief, occupancy belief, and detector errors affect search decisions. Through comprehensive ablations in Isaac Sim and HSSD houses, we...

</details>

<details>
<summary>Share</summary>

```
What World Model Does Active Object Search Need? A Study under Imperfect Detection

In active object search, a robot must decide where to look and when to stop.

arXiv: https://arxiv.org/abs/2611.15689
Code: https://github.com/gokyeongryeol/BAMOS

#worldmodels #robotics
```

</details>

---

### [Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning](https://arxiv.org/abs/2611.22561)

**Authors:** Raphael C. Kim, Michele Santacatterina, Jingsen Zhu, Ramin Zabih

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22561) | [PDF](https://arxiv.org/pdf/2611.22561)

<details>
<summary>Abstract</summary>

Action-conditioned world models are increasingly used as world models for planning, yet a world model that makes plausible, realistic-looking videos that are consistent with the training data can produce poor decisions. We address two key questions: (1) when can we trust a world model for planning, and (2) what should we do when we cannot? We introduce CURE (Certify, Upweight, Rollout, Explore), a certificate-guided technique that assesses whether a world model can be trusted for planning and determines what to do next: whether to upweight the training data to debias the model; roll out more s...

</details>

<details>
<summary>Share</summary>

```
Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning

Action-conditioned world models are increasingly used as world models for planning, yet a world model that makes plausible, realistic-looking videos that are consistent with the training data can produce poor decisions.

arXiv: https://arxiv.org/abs/2611.22561

#worldmodels #robotics
```

</details>

---

### [Escaping Latent Traps by Remembering: Training-Free Episodic Kernel Repulsion for World-Model Planning](https://arxiv.org/abs/2611.22470)

**Authors:** Yican Zhao, Bolin Yang, Ruizhe Wang, Haiyang Guo, Fuji Yang et al. (7 authors)

**Published:** 2026-11-17 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22470) | [PDF](https://arxiv.org/pdf/2611.22470)

<details>
<summary>Abstract</summary>

Latent world models plan towards a goal image by minimising the distance between predicted and goal latents. This distance is not geodesic: it has local minima, latent traps, behind walls, at corners and in dead ends, and memoryless receding-horizon replanning keeps the agent in them, revisiting states far from the goal. We propose Episodic Kernel Repulsion (EKR), a training-free cost term that penalises candidate plans by a top-$k$ Gaussian kernel to a novelty-gated memory of the latents the agent has actually visited, rescaled by the current base cost so that its strength is comparable acros...

</details>

<details>
<summary>Share</summary>

```
Escaping Latent Traps by Remembering: Training-Free Episodic Kernel Repulsion for World-Model Planning

Latent world models plan towards a goal image by minimising the distance between predicted and goal latents.

arXiv: https://arxiv.org/abs/2611.22470

#worldmodels #robotics
```

</details>

---

### [WM-Quant: Rollout-Aware Post-Training Quantization for JEPA-Style World Models](https://arxiv.org/abs/2611.21882)

**Authors:** William Hammer, Andrew Heuer, Nikhil Krishna, Matthew Grenier, Ramtin Zand

**Published:** 2026-11-16 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.21882) | [PDF](https://arxiv.org/pdf/2611.21882)

<details>
<summary>Abstract</summary>

We present WM-Quant, to our knowledge, the first post-training quantization (PTQ) framework designed specifically for JEPA-style world models. Although world models typically feature relatively few parameters, action planning algorithms often require thousands of inferences, which can quickly become computationally expensive. PTQ is a natural way to reduce this cost. However, we show that in world models using autoregressive model predictive control (MPC) rollouts, quantization error can compound with each predictor step, resulting in action rankings from the quantized model becoming near-rand...

</details>

<details>
<summary>Share</summary>

```
WM-Quant: Rollout-Aware Post-Training Quantization for JEPA-Style World Models

We present WM-Quant, to our knowledge, the first post-training quantization (PTQ) framework designed specifically for JEPA-style world models.

arXiv: https://arxiv.org/abs/2611.21882

#worldmodels #robotics
```

</details>

---

### [WA-JEPA: Goal-Aware Predictive Feedback Action Refinement for a World-Action Model](https://arxiv.org/abs/2611.19183)

**Authors:** Tao An, Weihang Liang, Tianqi Wang, Chuqing Cao, Wenming Tan et al. (10 authors)

**Published:** 2026-11-14 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19183) | [PDF](https://arxiv.org/pdf/2611.19183) | [Code](https://github.com/Dovisya/WA-JEPA)

<details>
<summary>Abstract</summary>

JEPA-based world models predict action consequences in latent space, but representative planning approaches rely on candidate-action search, requiring repeated evaluation of action sequences and incurring substantial online computational cost. Direct action generation avoids this search, yet how to leverage latent predictions to guide action generation given task goals remains a key challenge in translating learned physical dynamics into effective decisions. We introduce WA-JEPA, a world-action model that couples action generation, action-conditioned latent prediction, and goal-aware feedback....

</details>

<details>
<summary>Share</summary>

```
WA-JEPA: Goal-Aware Predictive Feedback Action Refinement for a World-Action Model

JEPA-based world models predict action consequences in latent space, but representative planning approaches rely on candidate-action search, requiring repeated evaluation of action sequences and incurring substantial...

arXiv: https://arxiv.org/abs/2611.19183
Code: https://github.com/Dovisya/WA-JEPA

#worldmodels #robotics
```

</details>

---

### [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](https://arxiv.org/abs/2611.17831)

**Authors:** Keuntae Kim, Dongjun Kim, Yong Suk Choi

**Published:** 2026-11-13 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.17831) | [PDF](https://arxiv.org/pdf/2611.17831) | [Code](https://github.com/kkt94/Llama-V-JEPA-LM)

<details>
<summary>Abstract</summary>

World-model video encoders such as V-JEPA learn how scenes change (direction, speed, order, state) from video alone. To answer questions, they are joined to a language model trained on captions and question-answer pairs. But each caption or question names only a few attributes of a clip, so the model learns to retrieve those attributes rather than to read the clip, and the dynamics the encoder carries go unused: on the same items, a linear probe reads speed from frozen V-JEPA features at 87% while the VLM answers at chance. We show where dynamics lives in a frozen encoder: in a subspace shared...

</details>

<details>
<summary>Share</summary>

```
V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations

World-model video encoders such as V-JEPA learn how scenes change (direction, speed, order, state) from video alone.

arXiv: https://arxiv.org/abs/2611.17831
Code: https://github.com/kkt94/Llama-V-JEPA-LM

#worldmodels #robotics
```

</details>

---

### [CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models](https://arxiv.org/abs/2611.15602)

**Authors:** Qirui Li, Xin Zhang, Yabo Chen, Jinkun Hao, Paul L Rosin et al. (10 authors)

**Published:** 2026-11-11 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15602) | [PDF](https://arxiv.org/pdf/2611.15602) | [Project Page](https://iapple233.github.io/CCW/)

<details>
<summary>Abstract</summary>

Multiplayer generative world models must produce observations that agree on shared entities despite different camera motions and occlusions. Explicit world representations provide spatial control, but precise modeling of individual game maps limits scene diversity, while shared geometry alone cannot ensure consistent appearance across views. We present CoCode-World, a shared 3D proxy framework that separates structural control from visual synthesis for two-player video generation. Programmable proxies specify scene layout, motion, and occlusion, while RGB references guide character and scene a...

</details>

<details>
<summary>Share</summary>

```
CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models

Multiplayer generative world models must produce observations that agree on shared entities despite different camera motions and occlusions.

arXiv: https://arxiv.org/abs/2611.15602
Project page: https://iapple233.github.io/CCW/

#worldmodels #robotics
```

</details>

---

### [Driving World Models Move the Camera, Not the Scene](https://arxiv.org/abs/2611.15260)

**Authors:** Yuqiao Feng, Xiaoyu Ao

**Published:** 2026-11-11 (updated 2026-11-15) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15260) | [PDF](https://arxiv.org/pdf/2611.15260) | [Project Page](https://joefeng0571.github.io/retime-compose/)

<details>
<summary>Abstract</summary>

Plan-conditioned driving world models are used to compare candidate plans, so their forecast should change with the plan as the real scene would, yet widely used control metrics check only whether the camera follows the command. Recorded drives already contain real outcomes of plans that were never driven: retiming a log gives pose-matched images and LiDAR for other speeds, and a stereo rig records a laterally shifted view. Against these references, released world models move their camera but barely move the scene: their scene response, the share of the real change in distance that the forecas...

</details>

<details>
<summary>Share</summary>

```
Driving World Models Move the Camera, Not the Scene

Plan-conditioned driving world models are used to compare candidate plans, so their forecast should change with the plan as the real scene would, yet widely used control metrics check only whether the camera follows t...

arXiv: https://arxiv.org/abs/2611.15260
Project page: https://joefeng0571.github.io/retime-compose/

#worldmodels #robotics
```

</details>

---

### [Duo: A Reciprocal World Model for Full-Duplex Interaction](https://arxiv.org/abs/2611.15131)

**Authors:** Hengyuan Cao, Biao Gong, Guoshan Lu, Qiyuan Zhang, Lin Liu et al. (20 authors)

**Published:** 2026-11-11 | **Categories:** cs.CV, cs.SD | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15131) | [PDF](https://arxiv.org/pdf/2611.15131) | [Project Page](https://duo-v1.github.io/)

<details>
<summary>Abstract</summary>

In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time. The RWM treats intelligence and physical reality as equally fundamental to what constitutes a world. Existing world models largely focus on simulating the latter, leaving reasoning and decision-making as external controls rather than intrinsic parts of the world itself. In RWM, we identify two equally fundamental capabilities: Intent, which provides the cognition underlying world interactions, and Real...

</details>

<details>
<summary>Share</summary>

```
Duo: A Reciprocal World Model for Full-Duplex Interaction

In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time.

arXiv: https://arxiv.org/abs/2611.15131
Project page: https://duo-v1.github.io/

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

### [JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling](https://arxiv.org/abs/2611.22543)

**Authors:** Tian Lyu, Yichen Jiang, Ziyuan Cheng, Yunda Yan, Xiangyu Pan et al. (10 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22543) | [PDF](https://arxiv.org/pdf/2611.22543)

<details>
<summary>Abstract</summary>

Visual world models predict future visual states conditioned on actions, but recursive errors in entity poses and spatial relations limit their long-horizon prediction for robot planning and control. We ask whether a separately predicted relational state can correct this drift without restructuring the visual model. This is challenging because graph nodes and visual states share neither elements nor a feature space. We propose Joint Graph--Visual Dynamics Correction (JointGV), a plug-in based on a cross-granularity dynamics hypothesis: despite their different representations, graph-node and vi...

</details>

<details>
<summary>Share</summary>

```
JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling

Visual world models predict future visual states conditioned on actions, but recursive errors in entity poses and spatial relations limit their long-horizon prediction for robot planning and control.

arXiv: https://arxiv.org/abs/2611.22543

#worldmodels #robotics
```

</details>

---

### [Perception into Imagination: Executable Memory for World Models](https://arxiv.org/abs/2611.22294)

**Authors:** Xianyao Li, Ruitong Tian, Rui Min, Fang Xu, Jing Du

**Published:** 2026-11-17 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22294) | [PDF](https://arxiv.org/pdf/2611.22294)

<details>
<summary>Abstract</summary>

Physical agents must use what they previously saw or touched after visibility or contact is lost. Their actions change the implications of these remembered facts. We introduce executable perceptual memory (EPM), a world-model framework that advances explicit perceptual state alongside neural latent dynamics during imagination. Its evolving read-out informs reward prediction, value estimation and policy learning. We align reward inputs with the transitions that produced them and supervise the reward head on open-loop rollouts of recorded actions. On Memory Maze $13\times13$, EPM reaches 30.37 r...

</details>

<details>
<summary>Share</summary>

```
Perception into Imagination: Executable Memory for World Models

Physical agents must use what they previously saw or touched after visibility or contact is lost.

arXiv: https://arxiv.org/abs/2611.22294

#worldmodels #robotics
```

</details>

---

### [Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum](https://arxiv.org/abs/2611.17529)

**Authors:** Konstantinos Mylonas, Thrasyvoulos Spyropoulos

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.17529) | [PDF](https://arxiv.org/pdf/2611.17529)

<details>
<summary>Abstract</summary>

Image-goal planning with a frozen visual world model depends on how predicted observations are scored against the goal. Mean-squared error (MSE) between embeddings from a pretrained visual encoder can provide a useful signal near a goal, yet favor states across an obstacle that are visually similar to the goal and difficult to reach. We fit a small residual adapter on top of frozen I-JEPA embeddings to improve this latent goal cost. Starting near each goal, a planner collects trajectories from progressively wider regions of initial states. The adapter learns from the order of observations alon...

</details>

<details>
<summary>Share</summary>

```
Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum

Image-goal planning with a frozen visual world model depends on how predicted observations are scored against the goal.

arXiv: https://arxiv.org/abs/2611.17529

#worldmodels #robotics
```

</details>

---

### [Rethinking Actions: Continuity-Aware Priors for World-Model Planning](https://arxiv.org/abs/2611.16645)

**Authors:** Shaobo Yang, Zichen Ai, Ziyang Ma, Qian Yang, Bin Fang

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.16645) | [PDF](https://arxiv.org/pdf/2611.16645)

<details>
<summary>Abstract</summary>

Actions in expert demonstrations exhibit temporal structure. An ordered-versus-shuffled analysis across five environments confirms this dependence. We ask whether action proposals that better reflect expert continuity can improve visual world-model planning. Rather than imposing generic smoothness, we learn continuations from the temporal structure of demonstrated actions. Our locality-gated deep-kernel Gaussian-process prior, LG-DKGP, combines recent and longer-range executed action history, predicts a neural continuation, and learns a temporal Gaussian-process (GP) residual. A training-deriv...

</details>

<details>
<summary>Share</summary>

```
Rethinking Actions: Continuity-Aware Priors for World-Model Planning

Actions in expert demonstrations exhibit temporal structure.

arXiv: https://arxiv.org/abs/2611.16645

#worldmodels #robotics
```

</details>

---

### [BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU](https://arxiv.org/abs/2611.16422)

**Authors:** Fuyi Chen

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16422) | [PDF](https://arxiv.org/pdf/2611.16422) | [Code](https://github.com/fuyichen0725/blinkmimic)

<details>
<summary>Abstract</summary>

Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library of motions has usually taken hours of GPU time. SuperMimic showed that the policy can instead be trained by backpropagating through a world model learned from parallel simulation, and InstantTrack added Muon updates, a residual policy around the reference and an averaged deployed policy. We build on both and present BlinkMimic, a recipe that makes this training faster. On a simulated Unitree G1, BlinkMimic trains one policy for all 40 LAFAN1 clips in 3.4 minutes on a single R...

</details>

<details>
<summary>Share</summary>

```
BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU

Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library of motions has usually taken hours of GPU time.

arXiv: https://arxiv.org/abs/2611.16422
Code: https://github.com/fuyichen0725/blinkmimic

#worldmodels #robotics
```

</details>

---

### [Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail](https://arxiv.org/abs/2611.22537)

**Authors:** Karthik Iyer

**Published:** 2026-11-17 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22537) | [PDF](https://arxiv.org/pdf/2611.22537)

<details>
<summary>Abstract</summary>

A world model is trusted to answer "what if": how its world responds to an action it has never seen. We give a test of that trust for any action-conditioned world model: actions held out of training by design and scored against a known answer; whether forecast accuracy predicts accuracy on those actions; and the same structure given to simpler models. We run it in retail, where the action is a price and promotion plan, across 2,853 fitted models. First, forecast accuracy is a fair guide between kinds of model (rank correlation with error on new plans 0.32 to 0.66) and a poor guide between vers...

</details>

<details>
<summary>Share</summary>

```
Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail

A world model is trusted to answer "what if": how its world responds to an action it has never seen.

arXiv: https://arxiv.org/abs/2611.22537

#worldmodels #robotics
```

</details>

---

### [Can a World Model Predict a Deepfake Video? A Consistency Margin Prior for Deepfake Detection](https://arxiv.org/abs/2611.21846)

**Authors:** Pradip Gupta, Shubham Mandloi, Ravi Kumar Satzoda, Sujeeth Bharadwaj, Yassine Benajiba et al. (6 authors)

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.21846) | [PDF](https://arxiv.org/pdf/2611.21846)

<details>
<summary>Abstract</summary>

Deepfake detectors often perform well on the dataset they are trained on, but their performance drops when tested on videos from different datasets. In this paper, we study whether a predictive video model can provide a signal that generalizes better across datasets. Instead of relying only on generator-specific artifacts, as many existing detectors do, we use a model trained to predict natural video and measure the difference between what it predicts and what it observes in a video. Using V-JEPA 2.1, we keep the encoder frozen and adapt the predictor using rank-16 LoRA. We define the differen...

</details>

<details>
<summary>Share</summary>

```
Can a World Model Predict a Deepfake Video? A Consistency Margin Prior for Deepfake Detection

Deepfake detectors often perform well on the dataset they are trained on, but their performance drops when tested on videos from different datasets.

arXiv: https://arxiv.org/abs/2611.21846

#worldmodels #robotics
```

</details>

---

### [Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models](https://arxiv.org/abs/2611.21782)

**Authors:** Sheng Lu, Guangpin Tao, Tong Lu, Ying Tai

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.21782) | [PDF](https://arxiv.org/pdf/2611.21782)

<details>
<summary>Abstract</summary>

Interactive video world models serve as simulators for embodied agents: from a starting image and an action trajectory, they generate the views the agent would see. The starting image fixes how high the camera is, for example 0.15 m for a floor robot or 2.2 m for an overhead camera, and a faithful simulator must keep this height as the camera moves. We show that six recent open-weight models fail to do so: as motion replaces the starting view with generated content, they move the camera toward human eye level, a failure we call camera-height regression. Our benchmark, EyeHeight, pairs six rend...

</details>

<details>
<summary>Share</summary>

```
Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models

Interactive video world models serve as simulators for embodied agents: from a starting image and an action trajectory, they generate the views the agent would see.

arXiv: https://arxiv.org/abs/2611.21782

#worldmodels #robotics
```

</details>

---

### [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](https://arxiv.org/abs/2611.20899)

**Authors:** Xue Yang, Haonan Cai, Xinyu Hang, Zhimeng Huang, Xuanyi Liu et al. (7 authors)

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.20899) | [PDF](https://arxiv.org/pdf/2611.20899)

<details>
<summary>Abstract</summary>

While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the underlying principles remains a critical challenge. Existing benchmarks typically evaluate video samples in isolation, making it difficult to expose models that simply fit superficial visual priors. In scientific experiments, a small change in one condition produces a markedly different outcome even when the rest of the setup remains fixed. Capitalizing on this sensitivity, we introduce SciWorldBench, a benchmark compri...

</details>

<details>
<summary>Share</summary>

```
SciWorldBench: Do Video World Models Really Understand Scientific Experiments?

While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the underlying principles remains a critical...

arXiv: https://arxiv.org/abs/2611.20899

#worldmodels #robotics
```

</details>

---

### [Latent World Modeling for Point-Cloud Video Pretraining](https://arxiv.org/abs/2611.20090)

**Authors:** Zhuoyue Zhang, Jian Liu, Jihua Zhu, Ajmal Saeed Mian

**Published:** 2026-11-15 (updated 2026-11-17) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.20090) | [PDF](https://arxiv.org/pdf/2611.20090) | [Code](https://github.com/InitalZ/PointWM)

<details>
<summary>Abstract</summary>

Masked modeling is the dominant self-supervised paradigm for point-cloud videos. However, it leaks the information it is meant to predict, whether it reconstructs masked points as in MAE-style methods or predicts their latent features. Because point-cloud tokens are anchored at points sampled from each frame, querying a target at its own position reveals where its geometry has moved, in reconstruction and latent prediction alike. For latent predictors, random spatio-temporal masks introduce a further shortcut, as visible frames on both sides of each target allow interpolation rather than forec...

</details>

<details>
<summary>Share</summary>

```
Latent World Modeling for Point-Cloud Video Pretraining

Masked modeling is the dominant self-supervised paradigm for point-cloud videos.

arXiv: https://arxiv.org/abs/2611.20090
Code: https://github.com/InitalZ/PointWM

#worldmodels #robotics
```

</details>

---

### [GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models](https://arxiv.org/abs/2611.19247)

**Authors:** Bing He, Runze Wang, Fei Zha, Zhongyuan Wu, Ke Xu et al. (8 authors)

**Published:** 2026-11-14 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.19247) | [PDF](https://arxiv.org/pdf/2611.19247)

<details>
<summary>Abstract</summary>

For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay. Generative video models (VMs) now bear on all three. Neural networks already draw most of the pixels in shipped games, and recent world models let a lightweight game engine keep the world state while a VM turns the engine's coarse proxy video into final frames. These systems, however, treat the VM as a renderer that only restyles motion the engine has already authored, which leaves most of its generative capacity unused and limits the diversity a game can offer. We pres...

</details>

<details>
<summary>Share</summary>

```
GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models

For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay.

arXiv: https://arxiv.org/abs/2611.19247

#worldmodels #robotics
```

</details>

---

### [Progress Predicts Policy](https://arxiv.org/abs/2611.22491)

**Authors:** Licheng Zhong, Gim Hee Lee

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22491) | [PDF](https://arxiv.org/pdf/2611.22491)

<details>
<summary>Abstract</summary>

A task specifies how the world should change, while a policy specifies what the robot should do. We introduce Progress Predicts Policy (PPP), which learns a language-conditioned scalar field through the commands induced by its differential. We obtain action conditioning by composing a latent progress field with a shared world model and read its action gradient at a fixed reference command. Continuous commands scale this gradient by a learned positive gain, while discrete commands use finite differences of the same scalar. This yields a hybrid policy without a separate action head or iterative...

</details>

<details>
<summary>Share</summary>

```
Progress Predicts Policy

A task specifies how the world should change, while a policy specifies what the robot should do.

arXiv: https://arxiv.org/abs/2611.22491

#worldmodels #robotics
```

</details>

---

### [XMimic and XSoma: Learning Humanoid Motion Tracking and Locomotion in Under a Minute](https://arxiv.org/abs/2611.20452)

**Authors:** Nico Bohlinger, Jan Peters

**Published:** 2026-11-16 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.20452) | [PDF](https://arxiv.org/pdf/2611.20452)

<details>
<summary>Abstract</summary>

We present XMimic and XSoma, which learn humanoid motion tracking and locomotion on rough terrain in under a minute of training. Both follow SuperMimic, which learns a world model of the robot and optimizes the policy with analytic gradients through short rollouts imagined in this model. Existing implementations of this method do not make use of larger GPUs, as every training iteration is a long chain of small GPU operations that run one after another. XMimic and XSoma therefore shorten this chain and run the steps of every iteration at the same time on up to four GPUs. We compile the complete...

</details>

<details>
<summary>Share</summary>

```
XMimic and XSoma: Learning Humanoid Motion Tracking and Locomotion in Under a Minute

We present XMimic and XSoma, which learn humanoid motion tracking and locomotion on rough terrain in under a minute of training.

arXiv: https://arxiv.org/abs/2611.20452

#worldmodels #robotics
```

</details>

---

### [Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models](https://arxiv.org/abs/2611.17775)

**Authors:** Yu Zhou, Changsong Lei, Yixiang Wei, Kairui Wen, Huankun Sheng et al. (9 authors)

**Published:** 2026-11-13 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.17775) | [PDF](https://arxiv.org/pdf/2611.17775)

<details>
<summary>Abstract</summary>

World models that support planning, control, and interpretable reasoning require latent representations that genuinely encode action. Yet the large-scale video data from which such models are learned overwhelmingly lack action annotations. Latent-action models infer action-like variables from observation sequences, enabling action-aware learning from unlabeled videos or trajectories. A fundamental concern, however, remains: a latent that improves future prediction may simply encode the current state, episode progress, task identity, or other predictive shortcuts. Existing evaluation practices-...

</details>

<details>
<summary>Share</summary>

```
Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models

World models that support planning, control, and interpretable reasoning require latent representations that genuinely encode action.

arXiv: https://arxiv.org/abs/2611.17775

#worldmodels #robotics
```

</details>

---

### [Prediction or Persistence? What Future-Prediction Scores Miss About World Models](https://arxiv.org/abs/2611.15082)

**Authors:** Animesh Maheshwari

**Published:** 2026-11-11 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.15082) | [PDF](https://arxiv.org/pdf/2611.15082)

<details>
<summary>Abstract</summary>

Pretrained video world models are compared and chosen as components for robot learning largely by future-prediction scores. On its own, such a score cannot be read as evidence of prediction, because it mixes encoder quality, the near future's resemblance to the recent past, and the predictor's own contribution. We separate the three with a matched control. On 27,000 future-retrieval trials from household egocentric video, a model must pick the true continuation of a clip among eleven candidates from the same video (chance 0.091), ranked zero-shot by its own training criterion. Each model is pa...

</details>

<details>
<summary>Share</summary>

```
Prediction or Persistence? What Future-Prediction Scores Miss About World Models

Pretrained video world models are compared and chosen as components for robot learning largely by future-prediction scores.

arXiv: https://arxiv.org/abs/2611.15082

#worldmodels #robotics
```

</details>

---

### [Frame First, Decode Once: Object-Centric Coordinates and Single-Pass Decoding for System-1 World Models](https://arxiv.org/abs/2611.18761)

**Authors:** Abu Anas Ibn Samad

**Published:** 2026-11-11 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.18761) | [PDF](https://arxiv.org/pdf/2611.18761)

<details>
<summary>Abstract</summary>

Single-pass primitive decoders such as LocateAnything and VFlash predict all quantized coordinate tokens of a geometric primitive in one forward pass, enabling fast, System-1 visual planning. We study what matters when such a decoder serves as a System-1 world model: a fast action-conditioned predictor that ranks candidate pushes by their predicted outcome. On ManiSkill3 PushT-v1 (512 held-out test families, 8,192 rollouts) and on human demonstrations from lerobot/pusht (2,384 test windows), we compare decoders, training losses, rigid-body projections and coordinate frames, using matched check...

</details>

<details>
<summary>Share</summary>

```
Frame First, Decode Once: Object-Centric Coordinates and Single-Pass Decoding for System-1 World Models

Single-pass primitive decoders such as LocateAnything and VFlash predict all quantized coordinate tokens of a geometric primitive in one forward pass, enabling fast, System-1 visual planning.

arXiv: https://arxiv.org/abs/2611.18761

#worldmodels #robotics
```

</details>

---

### [AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention](https://arxiv.org/abs/2611.15215)

**Authors:** Haoyi Zhang, Qi Zhang, Yunfan Ren, Yi Bin, Lei Zhu et al. (6 authors)

**Published:** 2026-11-11 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.15215) | [PDF](https://arxiv.org/pdf/2611.15215)

<details>
<summary>Abstract</summary>

In robotics and embodied AI, a core challenge for world models is adapting to sudden, persistent, yet initially unknown changes in robot dynamics during interaction. For instance, when a robotic arm grasps an object with an unknown payload, the robot dynamics change suddenly. If the world model fails to adapt, its prediction errors accumulate over the open-loop rollout and ultimately mislead the robot's actions. Existing world models, however, struggle to simultaneously satisfy three critical requirements for dynamics adaptation: responsiveness, reacting promptly to sudden changes to curb pred...

</details>

<details>
<summary>Share</summary>

```
AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention

In robotics and embodied AI, a core challenge for world models is adapting to sudden, persistent, yet initially unknown changes in robot dynamics during interaction.

arXiv: https://arxiv.org/abs/2611.15215

#worldmodels #robotics
```

</details>

---

### [Does Your World Model Know Actions Have Consequences?](https://arxiv.org/abs/2611.15048)

**Authors:** Ayush Gaggar, Jared Berry, Todd D. Murphey

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.15048) | [PDF](https://arxiv.org/pdf/2611.15048)

<details>
<summary>Abstract</summary>

Embodied world models (WMs) are implicit learning systems that predict the next future latent state directly from observations and actions. Unique from other end-to-end learning systems, the dynamics predictor of WMs can simulate the environment's response to alternative actions without physical deployment nor pre-specifying states of the dynamical system. Current metrics focus on the quality of model outputs, e.g., clarity of reconstructions or task success, but fail to assess the fidelity of modeling consequences of counterfactual actions. Inspecting the forced response to action perturbatio...

</details>

<details>
<summary>Share</summary>

```
Does Your World Model Know Actions Have Consequences?

Embodied world models (WMs) are implicit learning systems that predict the next future latent state directly from observations and actions.

arXiv: https://arxiv.org/abs/2611.15048

#worldmodels #robotics
```

</details>

---

### [Fast Inference-Time Policy Refinement via Action-Affine World Models](https://arxiv.org/abs/2611.15011)

**Authors:** Run Wang, Yilin Mo, Liang Wu

**Published:** 2026-11-11 (updated 2026-11-17) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.15011) | [PDF](https://arxiv.org/pdf/2611.15011)

<details>
<summary>Abstract</summary>

Imitation policies can fail through compounding errors, while existing refinement methods often require additional on-policy learning or expensive online planning. Our key insight is to model the response to small corrections around a policy proposal in an affine form that enables fast optimization. We refine a frozen imitation policy using an \textit{action-affine world model} (A\textsuperscript{2}WM), trained offline from perturbed policy rollouts. Conditioned on history and the proposal, the model directly predicts a nominal trajectory and a linear action response over the full horizon. Wit...

</details>

<details>
<summary>Share</summary>

```
Fast Inference-Time Policy Refinement via Action-Affine World Models

Imitation policies can fail through compounding errors, while existing refinement methods often require additional on-policy learning or expensive online planning.

arXiv: https://arxiv.org/abs/2611.15011

#worldmodels #robotics
```

</details>

---

### [The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals](https://arxiv.org/abs/2611.14955)

**Authors:** Jaerock Kwon, Elahe Delavari, Donghyun Kim, Haewoon Nam

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.14955) | [PDF](https://arxiv.org/pdf/2611.14955)

<details>
<summary>Abstract</summary>

Model-based planners that roll out imagined futures assume the transition model faithfully propagates task-relevant signals---a property rarely measured directly. In a single-seed case study of a Recurrent State Space Model world model with active-inference planning in the CARLA driving simulator, we identify a \textbf{posterior-prior gap}---posterior (observation-filtered) states retain obstacle information that imagined rollout states progressively lose: a supervised obstacle probe achieves AUC 0.85 on posterior states, but the same probe applied to imagined prior states shows monotonic deca...

</details>

<details>
<summary>Share</summary>

```
The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals

Model-based planners that roll out imagined futures assume the transition model faithfully propagates task-relevant signals---a property rarely measured directly.

arXiv: https://arxiv.org/abs/2611.14955

#worldmodels #robotics
```

</details>

---

### [CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction](https://arxiv.org/abs/2611.22686)

**Authors:** Kailai Zhou, Ziqi Chen, Xiaoning Xu, Yuefeng Wu, Zixuan Fu et al. (11 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.22686) | [PDF](https://arxiv.org/pdf/2611.22686)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) have emerged as a promising paradigm for predictive visual representation learning. However, our analysis of I-JEPA reveals a growing discrepancy between semantic and geometric learning: improved semantic recognition during pretraining is accompanied by degraded 3D geometric representations. We hypothesize that this partly stems from predicting highly abstract latent representations with incomplete spatial context, favoring semantic regularities over fine-grained geometric information. To address this issue, we introduce CascadeJEPA, a spatially...

</details>

<details>
<summary>Share</summary>

```
CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction

Joint-Embedding Predictive Architectures (JEPAs) have emerged as a promising paradigm for predictive visual representation learning.

arXiv: https://arxiv.org/abs/2611.22686

#worldmodels #robotics
```

</details>

---

### [The Sense Paradigm for World Models](https://arxiv.org/abs/2611.19796)

**Authors:** Haidong Hu

**Published:** 2026-11-15 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.19796) | [PDF](https://arxiv.org/pdf/2611.19796)

<details>
<summary>Abstract</summary>

Latent world models predict the future in an embedding space rather than in pixels. An encoder trained only to predict collapses and maps every observation to the same point, so existing models add a mechanism against collapse, such as a target network, a variance penalty or a distribution penalty. These mechanisms keep the embedding from collapsing, but they leave its distances without meaning, and the model cannot tell a reversible transition from an irreversible one. We propose Sense, a single cross-entropy loss over the directed distance $d(x\to y)=\sum_i \mathrm{ReLU}(y_i-x_i)$ that repla...

</details>

<details>
<summary>Share</summary>

```
The Sense Paradigm for World Models

Latent world models predict the future in an embedding space rather than in pixels.

arXiv: https://arxiv.org/abs/2611.19796

#worldmodels #robotics
```

</details>

---

### [Macro Control and Capability Evaluation of Black-Box World Models: A Two-Regime Framework for LLM-Agent Markets](https://arxiv.org/abs/2611.19311)

**Authors:** Zhiyang Niu, Chuanjie Li, Huayuan Shen, Mengmeng Zhao, Jiajia Zhang

**Published:** 2026-11-14 | **Categories:** cs.AI, cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.19311) | [PDF](https://arxiv.org/pdf/2611.19311)

<details>
<summary>Abstract</summary>

Large language model (LLM) agents can be organized into multi-agent markets that act as world models, mapping macro information to emergent macro dynamics while the evaluator observes only macro inputs and outputs. This paper separates a model's capability into two stages that a single aggregate score cannot separate: information simulation, from macro information to micro behavior, and macro emergence, from micro behavior to the macro outcome. We introduce a soft macro-control method that announces a public reference path day by day without touching individual decisions, orders, or matching,...

</details>

<details>
<summary>Share</summary>

```
Macro Control and Capability Evaluation of Black-Box World Models: A Two-Regime Framework for LLM-Agent Markets

Large language model (LLM) agents can be organized into multi-agent markets that act as world models, mapping macro information to emergent macro dynamics while the evaluator observes only macro inputs and outputs.

arXiv: https://arxiv.org/abs/2611.19311

#worldmodels #robotics
```

</details>

---

### [Probing Where Surprise Happens: Localized Violation-of-Expectation Evaluation of Video World Models](https://arxiv.org/abs/2611.18979)

**Authors:** Yanbin Xu, Ming bo Cai

**Published:** 2026-11-13 | **Categories:** cs.CV, cs.AI, eess.IV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.18979) | [PDF](https://arxiv.org/pdf/2611.18979)

<details>
<summary>Abstract</summary>

Violation-of-expectation (VOE) benchmarks evaluate intuitive physics in video world models by testing whether physically impossible events produce greater prediction errors than matched possible events. However, conventional VOE evaluations aggregate prediction errors across space and time, making it unclear whether successful discrimination reflects model's understanding of physical violations at the locations and time where they occur. To address this limitation, we introduce localized VOE evaluation, a framework that measures prediction error differences between possible and impossible even...

</details>

<details>
<summary>Share</summary>

```
Probing Where Surprise Happens: Localized Violation-of-Expectation Evaluation of Video World Models

Violation-of-expectation (VOE) benchmarks evaluate intuitive physics in video world models by testing whether physically impossible events produce greater prediction errors than matched possible events.

arXiv: https://arxiv.org/abs/2611.18979

#worldmodels #robotics
```

</details>

---

### [Recovered or Memorized? Investigating Dynamical Consistency and Faithfulness in World Model Latents](https://arxiv.org/abs/2611.18807)

**Authors:** Jerome Francisco, Kyle Deng, George Flint, Kevin Zhu

**Published:** 2026-11-13 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.18807) | [PDF](https://arxiv.org/pdf/2611.18807)

<details>
<summary>Abstract</summary>

World models develop internal simulators that can learn the structure and dynamics of an environment. It has been demonstrated that their internal representations are both meaningful and causal, but are these representations faithful to the governing dynamics of the environment they are learning? We introduce Anchored Recovery Certification (ARC), a procedure that utilizes a discrete Fréchet distance calculation with ground truth to evaluate dynamical consistency on candidate world models up to an affine gauge. We use the procedure on TD-MPC2 (decoder-free world model) that has learned the pen...

</details>

<details>
<summary>Share</summary>

```
Recovered or Memorized? Investigating Dynamical Consistency and Faithfulness in World Model Latents

World models develop internal simulators that can learn the structure and dynamics of an environment.

arXiv: https://arxiv.org/abs/2611.18807

#worldmodels #robotics
```

</details>

---

### [Joint World Action Models through Differentiable Trajectory Optimization](https://arxiv.org/abs/2611.17626)

**Authors:** Mintae Kim, Koushil Sreenath

**Published:** 2026-11-13 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.17626) | [PDF](https://arxiv.org/pdf/2611.17626)

<details>
<summary>Abstract</summary>

Joint world action models (WAMs) generate future actions and states together, modeling world-action trajectories rather than actions alone. However, trajectory imitation does not ensure that these trajectories are task-effective or consistent with dynamics. We present \textbf{world action trajectory optimization (WATO)}, which optimizes generated actions and future states jointly for control. WATO uses both as references in a dynamics-constrained trajectory optimization problem and differentiates the task loss through the optimized trajectory to train the generator. This makes generated trajec...

</details>

<details>
<summary>Share</summary>

```
Joint World Action Models through Differentiable Trajectory Optimization

Joint world action models (WAMs) generate future actions and states together, modeling world-action trajectories rather than actions alone.

arXiv: https://arxiv.org/abs/2611.17626

#worldmodels #robotics
```

</details>

---

### [FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks](https://arxiv.org/abs/2611.14880)

**Authors:** Yinuo Du, Christopher Kiekintveld

**Published:** 2026-11-11 | **Categories:** cs.LG, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.14880) | [PDF](https://arxiv.org/pdf/2611.14880)

<details>
<summary>Abstract</summary>

Autonomous cyber defense is widely studied with deep reinforcement learning, but most work trains policies inside simulators because learning requires many trial-and-error interactions. Simulator-based training carries a fidelity gap: trained policies face authentication delays, partial action failures, service dependencies, and user traffic patterns that the simulator did not represent, and degrade on transfer. Training directly in the network being defended removes the gap but makes every interaction slow and costly, so sample efficiency becomes the binding constraint. Model-based reinforcem...

</details>

<details>
<summary>Share</summary>

```
FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks

Autonomous cyber defense is widely studied with deep reinforcement learning, but most work trains policies inside simulators because learning requires many trial-and-error interactions.

arXiv: https://arxiv.org/abs/2611.14880

#worldmodels #robotics
```

</details>

---

### [Value and Policy Calibration from Execution Feedback for Socially Compatible Driving](https://arxiv.org/abs/2611.19969)

**Authors:** Sen Shen, Ning Liu, Xiangrui Kong, Yingwei Li, Dongkun Han

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.19969) | [PDF](https://arxiv.org/pdf/2611.19969)

<details>
<summary>Abstract</summary>

Autonomous vehicle (AV) decisions at intersections affect the delay, braking, and motion smoothness of surrounding human-driven vehicles (HDVs). Learning socially compatible behavior requires connecting imagined interaction outcomes with feedback from executed actions. We propose a world-model reinforcement learning framework combines imagined policy improvement with direct value and policy calibration from finalized interactions, balancing AV progress with HDV interaction burden. An interaction-aware latent model supports imagination, while off-policy correction and replay updates enable obse...

</details>

<details>
<summary>Share</summary>

```
Value and Policy Calibration from Execution Feedback for Socially Compatible Driving

Autonomous vehicle (AV) decisions at intersections affect the delay, braking, and motion smoothness of surrounding human-driven vehicles (HDVs).

arXiv: https://arxiv.org/abs/2611.19969

#worldmodels #robotics
```

</details>

---

### [Score-Based Stochastic Closure Modeling via Offline Indirect Learning and Online Data Assimilation](https://arxiv.org/abs/2611.19676)

**Authors:** Xinghao Dong, Huchen Yang, Jin-Long Wu

**Published:** 2026-11-15 | **Categories:** cs.LG, physics.comp-ph, physics.flu-dyn | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.19676) | [PDF](https://arxiv.org/pdf/2611.19676)

<details>
<summary>Abstract</summary>

Stochastic closure modeling is an emerging area in reduced-order modeling of large and complex (e.g., multiscale, multi-physics) systems, for which the computationally affordable reduced-order physical descriptions (e.g., digital twins for additive manufacturing, world models for AI agents) in numerical simulations inevitably lead to information losses that cannot be well addressed by classical deterministic closures. However, learning stochastic closures typically requires closure data that are difficult to obtain from measurements or often prohibitively expensive to compute using first-princ...

</details>

<details>
<summary>Share</summary>

```
Score-Based Stochastic Closure Modeling via Offline Indirect Learning and Online Data Assimilation

Stochastic closure modeling is an emerging area in reduced-order modeling of large and complex (e.g., multiscale, multi-physics) systems, for which the computationally affordable reduced-order physical descriptions (e...

arXiv: https://arxiv.org/abs/2611.19676

#worldmodels #robotics
```

</details>

---

### [Spatial Foundry: A Multimodal Dataset for Spatial Intelligence](https://arxiv.org/abs/2611.17318)

**Authors:** Ethan Lin, Yang Song

**Published:** 2026-11-12 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.17318) | [PDF](https://arxiv.org/pdf/2611.17318)

<details>
<summary>Abstract</summary>

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bound...

</details>

<details>
<summary>Share</summary>

```
Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment.

arXiv: https://arxiv.org/abs/2611.17318

#worldmodels #robotics
```

</details>

---
