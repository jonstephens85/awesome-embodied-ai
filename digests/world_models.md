# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-25 00:22 UTC

**Papers shown:** 106 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting](https://arxiv.org/abs/2611.30573)

**Authors:** ZiAn Wang, Tianyi Wang, Zhihao Chen, Manni Cui, Junkai Chen et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30573) | [PDF](https://arxiv.org/pdf/2611.30573) | [Project Page](https://wangzian828.github.io/PersistWorld) | [Code](https://github.com/wangzian828/PersistWorld)

<details>
<summary>Abstract</summary>

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather than to forecast what will change. We therefore make what the model has seen its state. PersistWorld streams camera frames into a persistent 3D world state anchored in the scene, writ...

</details>

<details>
<summary>Share</summary>

```
Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead.

arXiv: https://arxiv.org/abs/2611.30573
Project page: https://wangzian828.github.io/PersistWorld
Code: https://github.com/wangzian828/PersistWorld

#worldmodels #robotics
```

</details>

---

### [DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2611.30907)

**Authors:** Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30907) | [PDF](https://arxiv.org/pdf/2611.30907) | [Project Page](https://vinaymohan0409.github.io/DexLatentWorld/)

<details>
<summary>Abstract</summary>

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability to previously unseen robot morphologies. We introduce a 3D latent-action world model that learns continuous action representations directly from point-cloud observations of retargeted human manipulation demonstrations. A contrastive objectiv...

</details>

<details>
<summary>Share</summary>

```
DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions.

arXiv: https://arxiv.org/abs/2611.30907
Project page: https://vinaymohan0409.github.io/DexLatentWorld/

#worldmodels #robotics
```

</details>

---

### [JEPA-Shield: Safe Diffusion Planning with Latent World Models via Conformal Shielding](https://arxiv.org/abs/2611.29609)

**Authors:** Taekyung Kim, Ege Yuceel, Steven Hong, Georgios Fainekos, Dimitra Panagou et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29609) | [PDF](https://arxiv.org/pdf/2611.29609) | [Project Page](https://www.taekyung.me/jepa-shield)

<details>
<summary>Abstract</summary>

Latent world models enable planning from images, but their predictions do not directly establish whether a robot will satisfy physical constraints. We present JEPA-Shield, which connects a frozen action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model to task-space safety enforcement. Two downstream models predict relative motion from imagined latent rollouts and decode unsafe geometry from the current image. Split conformal prediction turns end-to-end motion-prediction errors into multi-horizon uncertainty tubes. A backup-based shield checks these tubes against physical...

</details>

<details>
<summary>Share</summary>

```
JEPA-Shield: Safe Diffusion Planning with Latent World Models via Conformal Shielding

Latent world models enable planning from images, but their predictions do not directly establish whether a robot will satisfy physical constraints.

arXiv: https://arxiv.org/abs/2611.29609
Project page: https://www.taekyung.me/jepa-shield

#worldmodels #robotics
```

</details>

---

### [DriveOddsBench: Are Driving Video World Models Aligned with Real-World Odds?](https://arxiv.org/abs/2611.29275)

**Authors:** Jiaxi Liu, Keshu Wu, Bin Ran, Xiaopeng Li

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29275) | [PDF](https://arxiv.org/pdf/2611.29275) | [Project Page](https://hhjj233.github.io/DriveOddsBench-page/) | [Code](https://github.com/hhjj233/DriveOddsBench)

<details>
<summary>Abstract</summary>

Video world models predict how a scene will evolve, and their sampled futures are increasingly used in place of the real one, from planning to simulation. These uses assume that the samples are aligned with real-world odds, with each future appearing among them as often as it would follow the same history in reality, yet current evaluations only score how real each sample looks. Testing this assumption on real driving data is hard for three reasons. Each recorded history has only one real future, so the true probabilities are unknown. Physical quantities must be read from video, where reading...

</details>

<details>
<summary>Share</summary>

```
DriveOddsBench: Are Driving Video World Models Aligned with Real-World Odds?

Video world models predict how a scene will evolve, and their sampled futures are increasingly used in place of the real one, from planning to simulation.

arXiv: https://arxiv.org/abs/2611.29275
Project page: https://hhjj233.github.io/DriveOddsBench-page/
Code: https://github.com/hhjj233/DriveOddsBench

#worldmodels #robotics
```

</details>

---

### [WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation](https://arxiv.org/abs/2611.25251)

**Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus

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

### [Does the Action Matter? Probing Action-Conditioned Semantic Forecasting as a World Model for Autonomous Driving](https://arxiv.org/abs/2611.24840)

**Authors:** Binay Kumar Singh, Niels Da Vitoria Lobo

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24840) | [PDF](https://arxiv.org/pdf/2611.24840) | [Code](https://github.com/binayksingh/does-action-matter)

<details>
<summary>Abstract</summary>

World models are increasingly used in autonomous driving to predict how a scene evolves under the ego vehicle's actions, supporting counterfactual reasoning and model-based planning. However, existing evaluations focus on prediction fidelity and planning performance, and rarely verify that the predictions depend on the conditioning action. In this paper, we study action dependence in action-conditioned semantic forecasting, which predicts future semantic segmentation from past segmentations and the ego action. We compare a forecaster with feature-wise and input-level action conditioning agains...

</details>

<details>
<summary>Share</summary>

```
Does the Action Matter? Probing Action-Conditioned Semantic Forecasting as a World Model for Autonomous Driving

World models are increasingly used in autonomous driving to predict how a scene evolves under the ego vehicle's actions, supporting counterfactual reasoning and model-based planning.

arXiv: https://arxiv.org/abs/2611.24840
Code: https://github.com/binayksingh/does-action-matter

#worldmodels #robotics
```

</details>

---

### [Non-penetrating World Models](https://arxiv.org/abs/2611.27963)

**Authors:** Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang

**Published:** 2026-11-20 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27963) | [PDF](https://arxiv.org/pdf/2611.27963) | [Project Page](https://nopeworld.github.io) | [Code](https://github.com/yuhangdai427/NoPeWorld)

<details>
<summary>Abstract</summary>

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict such violations. We find that the hidden states of diffusion transformers (DiTs) can predict whether a candidate action will penetrate an obstacle. Building on this, we introduce NoPe...

</details>

<details>
<summary>Share</summary>

```
Non-penetrating World Models

We study a new problem of preventing object penetration in interactive video world models.

arXiv: https://arxiv.org/abs/2611.27963
Project page: https://nopeworld.github.io
Code: https://github.com/yuhangdai427/NoPeWorld

#worldmodels #robotics
```

</details>

---

### [EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution](https://arxiv.org/abs/2611.30004)

**Authors:** Zehao Liu, Huashuo Lei, Xi Lin, Haoang Li, Yuliang Chen et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CR, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30004) | [PDF](https://arxiv.org/pdf/2611.30004) | [Code](https://github.com/INKSIR/Envtrap)

<details>
<summary>Abstract</summary>

As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface. Prior attacks on embodied systems have used crafted instructions, adversarial visual inputs, and training-time policy modifications; we study environment-only object rearrangements with unchanged models and instructions. We reveal an attack surface in safety-critical spatial relations among existing objects. An adversary who rearranges objects, without modifying instructions or accessing models, can cause hazardous consequences. In this work, we propose EnvTrap, a diagnostic...

</details>

<details>
<summary>Share</summary>

```
EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution

As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface.

arXiv: https://arxiv.org/abs/2611.30004
Code: https://github.com/INKSIR/Envtrap

#worldmodels #robotics
```

</details>

---

### [SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning](https://arxiv.org/abs/2611.27639)

**Authors:** Anqi Li, Kai Liu, Linghe Kong, Yulun Zhang

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27639) | [PDF](https://arxiv.org/pdf/2611.27639) | [Code](https://github.com/starrywiki/SOAR)

<details>
<summary>Abstract</summary>

Latent world models plan by rolling out hundreds of candidate action sequences through a transformer predictor, so a single decision can take tens of seconds. Existing accelerations prune spatial tokens as in vision-language models, yet a sampling-based planner uses predicted costs only to rank candidates, so a rollout can be compressed freely as long as the ranking survives. We propose SOAR, a training-free method that adapts rollout compression to each planning decision. At every decision, SOAR probes a few candidates under several token budgets and keeps the smallest budget that preserves t...

</details>

<details>
<summary>Share</summary>

```
SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning

Latent world models plan by rolling out hundreds of candidate action sequences through a transformer predictor, so a single decision can take tens of seconds.

arXiv: https://arxiv.org/abs/2611.27639
Code: https://github.com/starrywiki/SOAR

#worldmodels #robotics
```

</details>

---

### [Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models](https://arxiv.org/abs/2611.26825)

**Authors:** Tomás Couso Coddou, Christ Devia, Rex G. Liu, Rodrigo Toro Icarte

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26825) | [PDF](https://arxiv.org/pdf/2611.26825) | [Code](https://github.com/tcouso/Skill-JEPA)

<details>
<summary>Abstract</summary>

World models based on Joint-Embedding Predictive Architectures (JEPAs) learn from pixels to predict the outcome of actions in a latent space. To reach a goal, a planner samples many candidate action sequences, uses the model to predict where each one leads, and executes the best one. However, standard planners draw their candidates from a Gaussian, while the model has only seen the structured, state-dependent actions of its training data. Its predictions for such candidates are unreliable, and planning fails more often as goals move farther away. We propose Skill-JEPA, which learns an action s...

</details>

<details>
<summary>Share</summary>

```
Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models

World models based on Joint-Embedding Predictive Architectures (JEPAs) learn from pixels to predict the outcome of actions in a latent space.

arXiv: https://arxiv.org/abs/2611.26825
Code: https://github.com/tcouso/Skill-JEPA

#worldmodels #robotics
```

</details>

---

### [Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models](https://arxiv.org/abs/2611.25927)

**Authors:** Yao Zhang, Bin Yu, Shijie Lian, Haishan Liu, Changti Wu et al. (7 authors)

**Published:** 2026-11-19 (updated 2026-11-22) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25927) | [PDF](https://arxiv.org/pdf/2611.25927) | [Project Page](https://deepcybo-physai.github.io/Fast-JEPA)

<details>
<summary>Abstract</summary>

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time. We introduce Fast-JEPA, a latent world model planning framework that advances the success-latency Pareto frontier of predictive search. Fast-JEPA reorganizes predictive computation to support effective action-sequence search at low planning cost. It constructs a goal-directed plan to guide search and directly predicts the outcomes of complete candidates for efficient comparison, avoiding recursive state rollout during refinement. Across PushT, Re...

</details>

<details>
<summary>Share</summary>

```
Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time.

arXiv: https://arxiv.org/abs/2611.25927
Project page: https://deepcybo-physai.github.io/Fast-JEPA

#worldmodels #robotics
```

</details>

---

### [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617)

**Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "action-conditioned video" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26617) | [PDF](https://arxiv.org/pdf/2611.26617) | [Project Page](https://showlab.github.io/o2laf) | [Code](https://github.com/showlab/O2LaF)

<details>
<summary>Abstract</summary>

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics...

</details>

<details>
<summary>Share</summary>

```
One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning

Videos reveal how the world changes, but rarely the actions that cause those changes.

arXiv: https://arxiv.org/abs/2611.26617
Project page: https://showlab.github.io/o2laf
Code: https://github.com/showlab/O2LaF

#worldmodels #robotics
```

</details>

---

### [Render the Robot, Generate the World: One Video World Model Across Embodiments](https://arxiv.org/abs/2611.24925)

**Authors:** Yash Jangir, Karan Mirakhor, Renos Zabounidis, Muhammad Zubair Irshad, Sergey Zakharov et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24925) | [PDF](https://arxiv.org/pdf/2611.24925) | [Project Page](https://doppelwm.github.io/)

<details>
<summary>Abstract</summary>

Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion. We introduce Doppel, an embodiment-agnostic video world model conditioned on camera-aligned renderings of future body configurations and numerical action trajectories. By explicitly providing the intended motion, Doppel can focus on predicting object motion and interaction-driven changes in the environment. Rendered motion also prov...

</details>

<details>
<summary>Share</summary>

```
Render the Robot, Generate the World: One Video World Model Across Embodiments

Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response.

arXiv: https://arxiv.org/abs/2611.24925
Project page: https://doppelwm.github.io/

#worldmodels #robotics
```

</details>

---

### [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](https://arxiv.org/abs/2611.30714)

**Authors:** Yuxuan Jiang, Zehua Chen, Yusheng Dai, Andong Wang, Weibei Dou et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.SD, cs.CV, cs.MM | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30714) | [PDF](https://arxiv.org/pdf/2611.30714) | [Project Page](https://streamaudio.github.io)

<details>
<summary>Abstract</summary>

Video-to-audio generation synthesizes sound that matches a video in content and timing, with applications ranging from film post-production to live streaming, games and interactive world models. Interactive applications receive video continuously and need the sound to follow it in real time, yet most existing video-to-audio models are bidirectional and must observe an entire clip before producing any sound. We propose LiveAudio, a streaming video-to-audio framework that generates high-quality and synchronized audio in real time while the video is playing. In contrast to prior streaming models...

</details>

<details>
<summary>Share</summary>

```
LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation

Video-to-audio generation synthesizes sound that matches a video in content and timing, with applications ranging from film post-production to live streaming, games and interactive world models.

arXiv: https://arxiv.org/abs/2611.30714
Project page: https://streamaudio.github.io

#worldmodels #robotics
```

</details>

---

### [AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events](https://arxiv.org/abs/2611.30120)

**Authors:** Haiyu Xu, Yiyang Chen, Jiayi Zhou, Jiaming Ji, Juntao Dai et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30120) | [PDF](https://arxiv.org/pdf/2611.30120) | [Project Page](https://AxEBench.github.io)

<details>
<summary>Abstract</summary>

Edge cases are not the long tail; they are the norm. An embodied system deployed across changing environments, bodies, objects, and tasks will routinely encounter combinations that were absent from its training data. General-purpose physical intelligence therefore requires world models that reuse prior knowledge, predict consequences, and adapt with little or no additional training. Yet current evaluations of conditional video generation emphasize visual quality, prompt alignment, or isolated physical plausibility, leaving systematic generalization difficult to measure. We introduce AxE Bench,...

</details>

<details>
<summary>Share</summary>

```
AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events

Edge cases are not the long tail; they are the norm.

arXiv: https://arxiv.org/abs/2611.30120
Project page: https://AxEBench.github.io

#worldmodels #robotics
```

</details>

---

### [Two Actions from One State: Fork Futures Teach JEPA World Models to Compare](https://arxiv.org/abs/2611.28350)

**Authors:** Yihao Wu, Runjia Zeng, Tongyan Wang, Renzhong Huang, Chongzhou Fang et al. (8 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28350) | [PDF](https://arxiv.org/pdf/2611.28350) | [Project Page](https://fork-jepa.github.io/)

<details>
<summary>Abstract</summary>

JEPA world models are trained to predict logged transitions but used to compare counterfactual actions from one state. The logged behavior data show one action per state, and under a local linear approximation we prove the action response is unidentified along any direction the policy never varies within a state. We therefore supplement behavior data with measured outcomes of alternative actions from the same state. Our fork futures execute two actions from one restored state, and their outcome difference cancels the state term, identifying the action response on the sampled span. The resultin...

</details>

<details>
<summary>Share</summary>

```
Two Actions from One State: Fork Futures Teach JEPA World Models to Compare

JEPA world models are trained to predict logged transitions but used to compare counterfactual actions from one state.

arXiv: https://arxiv.org/abs/2611.28350
Project page: https://fork-jepa.github.io/

#worldmodels #robotics
```

</details>

---

### [ReactDrive: Self-Reactive Driving World Model](https://arxiv.org/abs/2611.27024)

**Authors:** Yifan Wang, Xiaoqi Wang, Cho-Ying Wu, Wenbin He, Chenyu You et al. (6 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27024) | [PDF](https://arxiv.org/pdf/2611.27024) | [Project Page](https://reactdrive.github.io/)

<details>
<summary>Abstract</summary>

The world evolves through the dynamics of its constituent entities and their interactions, with changes in one entity influencing the behavior of others. To simulate this evolution under different actions, interactive world models need to capture the resulting agent responses as part of the world's own dynamics. In autonomous driving, errors in modeling these responses can misrepresent maneuver safety and undermine the reliability of generated videos used for policy evaluation and learning. To formalize this intrinsic requirement for driving world model, we define self-reactivity as the capabi...

</details>

<details>
<summary>Share</summary>

```
ReactDrive: Self-Reactive Driving World Model

The world evolves through the dynamics of its constituent entities and their interactions, with changes in one entity influencing the behavior of others.

arXiv: https://arxiv.org/abs/2611.27024
Project page: https://reactdrive.github.io/

#worldmodels #robotics
```

</details>

---

### [ViewDreamer: A Robot World Model beyond Fixed Camera Setups](https://arxiv.org/abs/2611.26981)

**Authors:** Ye Mao, Jinhui Xiong, Egor Larionov, Shiyang Lu, Krystian Mikolajczyk et al. (6 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26981) | [PDF](https://arxiv.org/pdf/2611.26981) | [Project Page](https://matchlab-imperial.github.io/ViewDreamer/)

<details>
<summary>Abstract</summary>

Video generation models are increasingly important for robot learning, yet most generate each camera view separately or tile all views in a fixed layout. Robot demonstrations, however, are captured by synchronized cameras whose number, placement, and order vary across embodiments. We present ViewDreamer, a single world model that handles variable sets of cameras by disentangling per-view generation from cross-view interaction. Each view follows the generation path of a pretrained single-view model, and views interact only through shared slot tokens. We stabilize multi-view training with a curr...

</details>

<details>
<summary>Share</summary>

```
ViewDreamer: A Robot World Model beyond Fixed Camera Setups

Video generation models are increasingly important for robot learning, yet most generate each camera view separately or tile all views in a fixed layout.

arXiv: https://arxiv.org/abs/2611.26981
Project page: https://matchlab-imperial.github.io/ViewDreamer/

#worldmodels #robotics
```

</details>

---

### [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](https://arxiv.org/abs/2611.25838)

**Authors:** Runze Wang, Fei Zha, Bing He, Ke Xu, Zhongyuan Wu et al. (10 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.GR | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25838) | [PDF](https://arxiv.org/pdf/2611.25838) | [Project Page](https://rainzor.github.io/contextrenderer/)

<details>
<summary>Abstract</summary>

Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations. During sustained gameplay, however, existing generative renderers struggle to follow changing conditions while preserving visual continuity across diverse proxies and target styles. We therefore introduce ContextRenderer, an autoregressive video diffusion framework designed for both dynamic conditioning and cross-proxy generalization. It couples Dynamic-Context Learning (DCL) for chunk-level interaction supervis...

</details>

<details>
<summary>Share</summary>

```
ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds

Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations.

arXiv: https://arxiv.org/abs/2611.25838
Project page: https://rainzor.github.io/contextrenderer/

#worldmodels #robotics
```

</details>

---

### [TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation](https://arxiv.org/abs/2611.25553)

**Authors:** Yijun Liu, Shijia Ge, Tongtong Feng, Xin Wang, Yuan Meng et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "action-conditioned video" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25553) | [PDF](https://arxiv.org/pdf/2611.25553) | [Code](https://github.com/PlantPotatoOnMoon/TwoPass)

<details>
<summary>Abstract</summary>

Action-conditioned video prediction lets robots anticipate the visual consequences of their actions for planning and policy evaluation. Existing predictors denoise each future from noise without using their own estimate of it, which limits the quality of the predicted future, in particular of the manipulated objects, and requires many network calls. We present TwoPass, a self-conditioned training-and-inference framework that keeps the standard flow-matching objective. Self-Generated Draft Training supplies a detached clean-video estimate from the shared network as conditioning at the same nois...

</details>

<details>
<summary>Share</summary>

```
TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation

Action-conditioned video prediction lets robots anticipate the visual consequences of their actions for planning and policy evaluation.

arXiv: https://arxiv.org/abs/2611.25553
Code: https://github.com/PlantPotatoOnMoon/TwoPass

#worldmodels #robotics
```

</details>

---

### [VeriTouch: Verified Visuo-Tactile World Models that Improve Robot Policy Learning](https://arxiv.org/abs/2611.30572)

**Authors:** Shuxun Wang, Xiaonan Jiang, Zhaoyu Wang, Ziyuan Chu, Xihang Yue et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30572) | [PDF](https://arxiv.org/pdf/2611.30572)

<details>
<summary>Abstract</summary>

Scaling visuo-tactile policy learning is constrained by the high cost of real-world data collection and the difficulty of building realistic simulations. Generative models offer a scalable source of training data, yet useful demonstrations require plausible tactile feedback, temporal alignment with visual contact, and accurate actions. To this end, we present VeriTouch, a framework for generating and verifying synthetic visuo-tactile trajectories for policy learning. Conditioned on initial images and task instructions, our world model, VeriGen, jointly generates high-fidelity dual-view videos...

</details>

<details>
<summary>Share</summary>

```
VeriTouch: Verified Visuo-Tactile World Models that Improve Robot Policy Learning

Scaling visuo-tactile policy learning is constrained by the high cost of real-world data collection and the difficulty of building realistic simulations.

arXiv: https://arxiv.org/abs/2611.30572

#worldmodels #robotics
```

</details>

---

### [Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation](https://arxiv.org/abs/2611.30310)

**Authors:** Haihong Hao, Lei Chen, Mingfei Han, Chenglong Yan, Dong An et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30310) | [PDF](https://arxiv.org/pdf/2611.30310)

<details>
<summary>Abstract</summary>

Multi-robot embodied systems are typically designed to collaborate by coordinating actions, sharing trajectories, or learning joint policies. We ask a complementary question: can collaboration emerge before decision-making, by first building a shared understanding of the environment? We introduce Shared Environmental Understanding, a policy-agnostic representation that aggregates partial egocentric observations from multiple robots into a shared latent world model. This shifts collaboration from the policy space to the representation space, enabling decentralized decision-making with shared en...

</details>

<details>
<summary>Share</summary>

```
Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation

Multi-robot embodied systems are typically designed to collaborate by coordinating actions, sharing trajectories, or learning joint policies.

arXiv: https://arxiv.org/abs/2611.30310

#worldmodels #robotics
```

</details>

---

### [How Latent Transition Geometry Matters for Planning in World Models](https://arxiv.org/abs/2611.30064)

**Authors:** Xuanya Zhu, Da Li, Xiatian Zhu

**Published:** 2026-11-23 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30064) | [PDF](https://arxiv.org/pdf/2611.30064)

<details>
<summary>Abstract</summary>

World models support planning by predicting how the environment evolves under candidate actions. However, one-step predictive accuracy alone does not characterize multi-step planning utility, which depends on distinguishing candidate futures. This raises a natural question: How does latent transition geometry shape planning? We investigate this through an action-conditioned transition-field view, using curvature regularization as a controlled intervention. Across four continuous-control tasks, appropriately tuned regularization improves planning, while excessive regularization can be detriment...

</details>

<details>
<summary>Share</summary>

```
How Latent Transition Geometry Matters for Planning in World Models

World models support planning by predicting how the environment evolves under candidate actions.

arXiv: https://arxiv.org/abs/2611.30064

#worldmodels #robotics
```

</details>

---

### [Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving](https://arxiv.org/abs/2611.28779)

**Authors:** Feiyang Jia, Lin Liu, Zhicheng Bao, Caiyan Jia, Ziying Song et al. (9 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28779) | [PDF](https://arxiv.org/pdf/2611.28779) | [Code](https://github.com/MoyangSensei/FastWorld)

<details>
<summary>Abstract</summary>

World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost. Efficiency efforts, such as knowledge distillation and domain-specific pre-training, often shift this burden to costly teachers or training pipelines, leaving lightweight world modeling an open challenge. We introduce FastWorld, a natively lightweight world-model framework for efficient autonomous driving planning. FastWorld reduces computation through compact scene representations, short-horizon action-conditioned prediction, and selective ca...

</details>

<details>
<summary>Share</summary>

```
Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving

World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost.

arXiv: https://arxiv.org/abs/2611.28779
Code: https://github.com/MoyangSensei/FastWorld

#worldmodels #robotics
```

</details>

---

### [SANA-Robot: Efficient World Action Model with Hybrid Memory](https://arxiv.org/abs/2611.28943)

**Authors:** Yuyang Zhao, Zekai Li, Yicheng Pan, Jiaming Tang, Zhuoyang Zhang et al. (12 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28943) | [PDF](https://arxiv.org/pdf/2611.28943) | [Project Page](https://nvlabs.github.io/Sana/Robot/)

<details>
<summary>Abstract</summary>

World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction. However, their prediction overhead prevents real-time deployment on edge devices, and they usually lack an effective long-term memory. We introduce SANA-Robot, a 4.5B WAM with minute-level memory that runs in real time on edge devices, built on the following core designs: (1) hybrid memory at constant cost: our WAM relies on linear attention to maintain a global memory with a fixed-size state, and on sliding window softmax attenti...

</details>

<details>
<summary>Share</summary>

```
SANA-Robot: Efficient World Action Model with Hybrid Memory

World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction.

arXiv: https://arxiv.org/abs/2611.28943
Project page: https://nvlabs.github.io/Sana/Robot/

#worldmodels #robotics
```

</details>

---

### [PACE-WM: Parallel World Modeling with Action History for Visual Planning](https://arxiv.org/abs/2611.27173)

**Authors:** Haishan Liu, Shijie Lian, Bin Yu, Yao Zhang, Changti Wu et al. (10 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27173) | [PDF](https://arxiv.org/pdf/2611.27173) | [Code](https://github.com/LHS180/PACE-WM)

<details>
<summary>Abstract</summary>

JEPA-style world models support visual planning by predicting future representations conditioned on future actions. However, similar observations can conceal different motion states, making temporal context essential for interpreting future action effects. We propose PACE-WM, a parallel world model that uses executed-action history to contextualize future prediction and planning. Specifically, PACE-WM maintains a recurrent memory of executed actions and uses this memory to condition a causal Transformer. PACE-WM predicts multiple future representations in parallel without recursive predicted-s...

</details>

<details>
<summary>Share</summary>

```
PACE-WM: Parallel World Modeling with Action History for Visual Planning

JEPA-style world models support visual planning by predicting future representations conditioned on future actions.

arXiv: https://arxiv.org/abs/2611.27173
Code: https://github.com/LHS180/PACE-WM

#worldmodels #robotics
```

</details>

---

### [Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners](https://arxiv.org/abs/2611.25415)

**Authors:** Junhyeok Lee, Dongheon Lee, Kyu Sung Choi

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

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

**Why surfaced:** "world model" in title; project page

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

### [CommDreamer: Radio-Geometric World Models for Mapless Cellular-Connected UAV Trajectory Planning](https://arxiv.org/abs/2611.24244)

**Authors:** Yuqi Ping, Tianhao Liang, Tingting Zhang

**Published:** 2026-11-18 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24244) | [PDF](https://arxiv.org/pdf/2611.24244)

<details>
<summary>Abstract</summary>

Reliable cellular connectivity and collision-free flight are essential for unmanned aerial vehicle (UAV) operations in low-altitude urban canyons, where dense 3D buildings obstruct flight clearance, shadow serving base stations, and create strong co-channel interference at street intersections. Existing planners either require prior 3D city meshes and channel knowledge maps unavailable onboard, or rely on model-free reinforcement learning with low sample efficiency and poor cross-city generalization. We propose CommDreamer, a mapless radio-geometric world model that fuses raw onboard 3D LiDAR...

</details>

<details>
<summary>Share</summary>

```
CommDreamer: Radio-Geometric World Models for Mapless Cellular-Connected UAV Trajectory Planning

Reliable cellular connectivity and collision-free flight are essential for unmanned aerial vehicle (UAV) operations in low-altitude urban canyons, where dense 3D buildings obstruct flight clearance, shadow serving bas...

arXiv: https://arxiv.org/abs/2611.24244

#worldmodels #robotics
```

</details>

---

### [JEPA Dots: Dual-Latent World Model for Language-Guided Robot Control](https://arxiv.org/abs/2611.24062)

**Authors:** Xianhao Pan, Chi Li, Hanchao Li, Yunxin Liu, Jiankai Sun et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24062) | [PDF](https://arxiv.org/pdf/2611.24062)

<details>
<summary>Abstract</summary>

Predictive world models for language-guided robot control face a fundamental conditioning challenge: instructions should influence action selection without altering the predicted consequences of fixed actions under identical observations. To address this challenge, we introduce JEPA Dots (Dynamics-Oriented Task Separation), a compact dual-latent framework that jointly learns visual dynamics and language-guided control through separate dynamics and task representations. Language-conditioned task features guide a flow-matching policy, while masked attention restricts world prediction to instruct...

</details>

<details>
<summary>Share</summary>

```
JEPA Dots: Dual-Latent World Model for Language-Guided Robot Control

Predictive world models for language-guided robot control face a fundamental conditioning challenge: instructions should influence action selection without altering the predicted consequences of fixed actions under id...

arXiv: https://arxiv.org/abs/2611.24062

#worldmodels #robotics
```

</details>

---

### [Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning](https://arxiv.org/abs/2611.30666)

**Authors:** Yu Zhang, Jingrui Li, Congyu Wang, Yuhang Cheng, Wenbo Chen et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30666) | [PDF](https://arxiv.org/pdf/2611.30666)

<details>
<summary>Abstract</summary>

Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified. We introduce Zhengrong (Zhengrong-PoleWM), a world model that decomposes a latent trajectory into an initial-condition anchor, a free response, and delayed responses to action innovations. Nonlinear networks map visual history and causal action prefixes to response coefficients. A shared bank of stable conjugate poles determines how each response evolves with elapsed time. This factorization preserves nonlinear inter...

</details>

<details>
<summary>Share</summary>

```
Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning

Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified.

arXiv: https://arxiv.org/abs/2611.30666

#worldmodels #robotics
```

</details>

---

### [Point Dynamics as Proxy for Robotic World Models](https://arxiv.org/abs/2611.25946)

**Authors:** Dong An, Tianyu Liu, Haoran Ding, Wen Yang, Anqing Duan et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25946) | [PDF](https://arxiv.org/pdf/2611.25946) | [Project Page](https://marsaki.github.io/point-dynamics-proxy/)

<details>
<summary>Abstract</summary>

Robotic world models predict future video frames from the current observation and a sequence of robot actions. While recent models follow the given actions closely, manipulated objects often collapse or move inconsistently with the action. We attribute this to the conditioning: an action, or a rendering of the robot, specifies where the robot goes but not how the scene responds, leaving a single video model to infer the interaction dynamics implicitly while also rendering appearance. We therefore separate dynamics prediction from visual rendering, with 3D point dynamics as the proxy between th...

</details>

<details>
<summary>Share</summary>

```
Point Dynamics as Proxy for Robotic World Models

Robotic world models predict future video frames from the current observation and a sequence of robot actions.

arXiv: https://arxiv.org/abs/2611.25946
Project page: https://marsaki.github.io/point-dynamics-proxy/

#worldmodels #robotics
```

</details>

---

### [StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model](https://arxiv.org/abs/2611.24408)

**Authors:** Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song et al. (12 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24408) | [PDF](https://arxiv.org/pdf/2611.24408) | [Code](https://github.com/chuangwang123/strideworld)

<details>
<summary>Abstract</summary>

Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free scale. Such references can absorb gradual scene deformation and changes in pace and route length, so these errors can pass undetected. We therefore introduce StrideWorld, a benchma...

</details>

<details>
<summary>Share</summary>

```
StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model

Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect.

arXiv: https://arxiv.org/abs/2611.24408
Code: https://github.com/chuangwang123/strideworld

#worldmodels #robotics
```

</details>

---

### [Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?](https://arxiv.org/abs/2611.30836)

**Authors:** Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang, Shou-Po Tsai, Jing-Zhe Huang et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30836) | [PDF](https://arxiv.org/pdf/2611.30836)

<details>
<summary>Abstract</summary>

Embodied vision systems rely on complementary sensors to perceive and act as conditions change. Even models that accept arbitrary sensor subsets can exhibit negative fusion: adding a sensor increases prediction error. We propose MakeSense, a multimodal fusion framework that preserves sensor-specific evidence in private streams and combines information through shared bottleneck tokens. Training pairs full and subset views of the same degraded observations, penalizing higher error with more sensors. Where geometry permits, the distance readout uses range measurements alone, while the rest of the...

</details>

<details>
<summary>Share</summary>

```
Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?

Embodied vision systems rely on complementary sensors to perceive and act as conditions change.

arXiv: https://arxiv.org/abs/2611.30836

#worldmodels #robotics
```

</details>

---

### [MOVER: Planning Beyond Motion](https://arxiv.org/abs/2611.30022)

**Authors:** Xiangyu Li, Yu Jiang, Tianyi Wang, Liang He, Qixing Huang et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30022) | [PDF](https://arxiv.org/pdf/2611.30022)

<details>
<summary>Abstract</summary>

Residual world models forecast a driving scene through its temporal change, so feature components that stay constant over time vanish from the residual pathway. We ask whether evidence with weak temporal change, such as a waiting pedestrian or a stopped vehicle, can be used more effectively for planning, and introduce MOVER, a complementary event-routing mechanism. A training-time teacher measures how each spatially grounded event query responds when a past frame is removed from shared history and contrasts that sensitivity with the event's pooled temporal residual, prioritizing events that de...

</details>

<details>
<summary>Share</summary>

```
MOVER: Planning Beyond Motion

Residual world models forecast a driving scene through its temporal change, so feature components that stay constant over time vanish from the residual pathway.

arXiv: https://arxiv.org/abs/2611.30022

#worldmodels #robotics
```

</details>

---

### [CarlHOI: Counterfactual Predictive Imagination for Generalizable Multi-Humanoid Object Interaction under Constrained Environments](https://arxiv.org/abs/2611.29749)

**Authors:** Wenjie Lin, Jin Wei-Kocsis

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29749) | [PDF](https://arxiv.org/pdf/2611.29749) | [Project Page](https://carlhoi.github.io)

<details>
<summary>Abstract</summary>

Recent advances in physics-based humanoid control enable teams of varying sizes to coordinate their movements and cooperatively transport shared objects. However, adapting learned cooperative behaviors to unseen environmental constraints remains challenging, particularly when obstacles require coordinated detours and changes in team configuration. We propose CarlHOI, a counterfactual predictive imagination framework built upon a counterfactual-anchored relational latent world model (CarlWM) for human-object interaction (HOI), enabling multi-humanoid teams to adapt to unseen environmental const...

</details>

<details>
<summary>Share</summary>

```
CarlHOI: Counterfactual Predictive Imagination for Generalizable Multi-Humanoid Object Interaction under Constrained Environments

Recent advances in physics-based humanoid control enable teams of varying sizes to coordinate their movements and cooperatively transport shared objects.

arXiv: https://arxiv.org/abs/2611.29749
Project page: https://carlhoi.github.io

#worldmodels #robotics
```

</details>

---

### [PhysPPF: Learning Robotic Manipulation with Past, Present, and Future Physical Representations](https://arxiv.org/abs/2611.28551)

**Authors:** Junjie Li, Dawei Yan, Guoting Wei, Ruike Song, Lu Wang et al. (9 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.28551) | [PDF](https://arxiv.org/pdf/2611.28551)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have advanced robotic manipulation, yet complex tasks requiring both precise 3D contact and long-horizon coordination remain challenging. Most existing studies enhance spatial perception or temporal reasoning in VLAs separately. Spatial methods primarily inject geometric or affordance priors into current-frame perception without tracking multi-step transitions, while history-aware and world-model VLAs typically capture past context or future dynamics in 2D feature or pixel spaces, either lacking explicit 3D contact cues or incurring high generation overhead....

</details>

<details>
<summary>Share</summary>

```
PhysPPF: Learning Robotic Manipulation with Past, Present, and Future Physical Representations

Vision-language-action (VLA) models have advanced robotic manipulation, yet complex tasks requiring both precise 3D contact and long-horizon coordination remain challenging.

arXiv: https://arxiv.org/abs/2611.28551

#worldmodels #robotics
```

</details>

---

### [Knowing What You Carry: Scalable Physics-Anchored World Models for Robotic Planning with Liquid Payloads](https://arxiv.org/abs/2611.28387)

**Authors:** Yicheng Zhu, Linfeng Tian, Yang Chen, Tao Li, Zilin Bian

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28387) | [PDF](https://arxiv.org/pdf/2611.28387)

<details>
<summary>Abstract</summary>

Payload-carrying robots, such as delivery robots and autonomous trucks, must choose motions that keep them and their payload safe, so their planners predict the outcome of each candidate motion. Modern planners compare thousands of candidates per step on a GPU, using world models such as batched simulators or learned predictors. Most of them assume a rigid payload, but a liquid payload keeps moving after a maneuver, and its state is rarely measured. Near a safety limit, small prediction errors can make an unsafe plan look safe. Coupled fluid simulations are accurate but too costly for every ca...

</details>

<details>
<summary>Share</summary>

```
Knowing What You Carry: Scalable Physics-Anchored World Models for Robotic Planning with Liquid Payloads

Payload-carrying robots, such as delivery robots and autonomous trucks, must choose motions that keep them and their payload safe, so their planners predict the outcome of each candidate motion.

arXiv: https://arxiv.org/abs/2611.28387

#worldmodels #robotics
```

</details>

---

### [What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage](https://arxiv.org/abs/2611.27939)

**Authors:** Hassan Iqbal, Krishna Kumar

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.27939) | [PDF](https://arxiv.org/pdf/2611.27939)

<details>
<summary>Abstract</summary>

When a robot is damaged, it must decide which routes it can still afford, and the amount of risk it may accept can change from one mission to the next. We argue that whether a learned model helps such a robot depends on its decision interface, that is, on what the model hands to the planner. A decision policy tells the planner what to do, whereas an outcome model, a kind of world model, predicts the consequences of each route. We study simulated Unitree Go2 quadrupeds and H1 humanoids with weakened motors, added payloads, or reduced foot friction. We compare four interfaces. The first is a dec...

</details>

<details>
<summary>Share</summary>

```
What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage

When a robot is damaged, it must decide which routes it can still afford, and the amount of risk it may accept can change from one mission to the next.

arXiv: https://arxiv.org/abs/2611.27939

#worldmodels #robotics
```

</details>

---

### [Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation](https://arxiv.org/abs/2611.27418)

**Authors:** Kangyi Wu, Pengna Li, Yucheng Wang, Yance Fang, Xihan Ma et al. (10 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.27418) | [PDF](https://arxiv.org/pdf/2611.27418)

<details>
<summary>Abstract</summary>

Vision-Language Navigation(VLN) requires an embodied agent to follow language instructions through unseen 3D environments, where the target spaces often lie beyond the current observation. Navigation world models address this challenge by predicting future views either as pixels or latent representations, providing valuable look-ahead information for action decision. Both paradigms define the future primarily through what the agent may observe, raising a fundamental question: is predicting future views the ultimate form to represent the future for VLN? Cognitive studies show that the human hip...

</details>

<details>
<summary>Share</summary>

```
Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation

Vision-Language Navigation(VLN) requires an embodied agent to follow language instructions through unseen 3D environments, where the target spaces often lie beyond the current observation.

arXiv: https://arxiv.org/abs/2611.27418

#worldmodels #robotics
```

</details>

---

### [Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models](https://arxiv.org/abs/2611.27344)

**Authors:** Yongkang He, Xiaofen Xing, Xiangmin Xu

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.27344) | [PDF](https://arxiv.org/pdf/2611.27344)

<details>
<summary>Abstract</summary>

Action-conditioned video world models imagine future observations under candidate robot actions, providing a promising visual tool for robot policy evaluation and interaction simulation. However, existing video world models often optimize global reconstruction errors instead of emphasizing interaction-relevant regions. As a result, they may preserve overall scene appearance but overlook local interaction details, leading to physically implausible outcomes such as hallucinated contact effects and inconsistent robot-object interactions. We introduce MoReWorld, a unified motion-region-guided fram...

</details>

<details>
<summary>Share</summary>

```
Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models

Action-conditioned video world models imagine future observations under candidate robot actions, providing a promising visual tool for robot policy evaluation and interaction simulation.

arXiv: https://arxiv.org/abs/2611.27344

#worldmodels #robotics
```

</details>

---

### [Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans](https://arxiv.org/abs/2611.25243)

**Authors:** Chrisantus Eze, Christopher Crick

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

### [DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play](https://arxiv.org/abs/2611.24836)

**Authors:** Akshay L Chandra, Iman Nematollahi, Lingyue Zhao, Daria Kulikova, Angela P. Schoellig et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24836) | [PDF](https://arxiv.org/pdf/2611.24836)

<details>
<summary>Abstract</summary>

Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Humans can demonstrate skills in seconds, but their demonstrations lack the required robot actions. We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. DiWALI infers latent actions from consecutive frames using an inverse dynamics model, enabling world model training without action labels, and grounds them in robot commands through a decoder trained separately on robot play. Skill policie...

</details>

<details>
<summary>Share</summary>

```
DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play

Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models.

arXiv: https://arxiv.org/abs/2611.24836

#worldmodels #robotics
```

</details>

---

### [Counterfactual World Models: JEPAs That Reason About "What If"](https://arxiv.org/abs/2611.24778)

**Authors:** Randall Balestriero, Yann LeCun, Kerda Varaku

**Published:** 2026-11-18 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24778) | [PDF](https://arxiv.org/pdf/2611.24778)

<details>
<summary>Abstract</summary>

World models operate in a world they cannot fully observe. When a hidden disturbance, such as a current pushing a boat, changes the outcome of an action, a counterfactual question follows: what would have happened under a different action, subject to the same disturbance? Its answer separates bad decisions from bad luck. We prove that world models trained on factual transitions cannot answer it on their own, whatever their data or capacity. For many physical systems, the observed outcome and a simple property of the dynamics suffice: natura non facit saltus, nature makes no leaps. When actions...

</details>

<details>
<summary>Share</summary>

```
Counterfactual World Models: JEPAs That Reason About "What If"

World models operate in a world they cannot fully observe.

arXiv: https://arxiv.org/abs/2611.24778

#worldmodels #robotics
```

</details>

---

### [ProbeShare: Probing a Few, Sharing Across Many for Fast World-Model Planning](https://arxiv.org/abs/2611.24229)

**Authors:** Zejian Kang, Xiantao Lin, Zekai Chen, Boyang Shen, Mingyu Ma et al. (8 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24229) | [PDF](https://arxiv.org/pdf/2611.24229)

<details>
<summary>Abstract</summary>

Visual planning with a frozen joint-embedding world model supports robotic reaching and object manipulation by evaluating candidate action sequences against an image goal before execution. Standard cross-entropy method (CEM) planners roll out every candidate independently through a billion-parameter predictor, even when nearby actions induce similar scene changes. This redundant computation grows with population size and search rounds, slowing closed-loop replanning. We observe that candidates within a planning step share an observation history and thus a common action-to-feature map. Based on...

</details>

<details>
<summary>Share</summary>

```
ProbeShare: Probing a Few, Sharing Across Many for Fast World-Model Planning

Visual planning with a frozen joint-embedding world model supports robotic reaching and object manipulation by evaluating candidate action sequences against an image goal before execution.

arXiv: https://arxiv.org/abs/2611.24229

#worldmodels #robotics
```

</details>

---

### [Worth Another Look:Constrained World-Model Planning for Visual Inspection](https://arxiv.org/abs/2611.24187)

**Authors:** Ziyue Kang, Zixi Qi, Yuchen Dai, Nana Lv, Xirong Cheng et al. (9 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24187) | [PDF](https://arxiv.org/pdf/2611.24187)

<details>
<summary>Abstract</summary>

Visual inspection in field robotics and environmental monitoring must localize multiple targets under strict compute and sensing caps. Exhaustive sweeps waste calls on absent classes, while myopic and search-free policies stumble over heterogeneous tariff cliffs or discard viewport edits whose value emerges only after re-querying. We formulate inspection over frozen detectors as neuro-symbolic observation planning under partial observability, decoupling a compact recurrent world model (WM) from exact symbolic feasibility and tariff rules. Receding-horizon beam search with online replanning joi...

</details>

<details>
<summary>Share</summary>

```
Worth Another Look:Constrained World-Model Planning for Visual Inspection

Visual inspection in field robotics and environmental monitoring must localize multiple targets under strict compute and sensing caps.

arXiv: https://arxiv.org/abs/2611.24187

#worldmodels #robotics
```

</details>

---

### [Efficient World-Model Planning via Physics-Guided Search Distillation](https://arxiv.org/abs/2611.24171)

**Authors:** Hongyu Zhang, Xiaoshuai Hao, Heye Huang, Qingwen Meng, Wenjun Shi et al. (10 authors)

**Published:** 2026-11-18 (updated 2026-11-19) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24171) | [PDF](https://arxiv.org/pdf/2611.24171)

<details>
<summary>Abstract</summary>

World models support autonomous driving by evaluating candidate trajectories through predicted future scene evolution. However, accurate future prediction does not ensure road-compliant execution; when all candidates violate road boundaries, re-ranking cannot select a feasible trajectory. We propose Physics-Guided Search Distillation (PGSD), a single-view planning framework that combines future representations and execution feedback for verified beyond-pool repair through three components: (1) Execution-Aware Selection checks ego-vehicle road compliance under simulated execution and selects th...

</details>

<details>
<summary>Share</summary>

```
Efficient World-Model Planning via Physics-Guided Search Distillation

World models support autonomous driving by evaluating candidate trajectories through predicted future scene evolution.

arXiv: https://arxiv.org/abs/2611.24171

#worldmodels #robotics
```

</details>

---

### [SemPhys: Semantic-Physical Co-Learning for Humanoid Motion Generation via Differentiable World Models](https://arxiv.org/abs/2611.24074)

**Authors:** Zejian Kang, Yeqiang Wang, Zekai Chen, Boyang Shen, Mingyu Ma et al. (12 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24074) | [PDF](https://arxiv.org/pdf/2611.24074)

<details>
<summary>Abstract</summary>

In human-robot collaboration, natural language lets people direct a humanoid's whole-body movements without programming joint trajectories. A common approach generates a kinematic reference from an instruction and relies on a tracking controller to execute it. However, as the controller maintains balance under contact constraints, the executed motion can depart from the reference in ways that change the action it conveys. Our central insight is that semantic alignment must be evaluated directly on the complete motion the robot physically executes. Building on this insight, we introduce \textbf...

</details>

<details>
<summary>Share</summary>

```
SemPhys: Semantic-Physical Co-Learning for Humanoid Motion Generation via Differentiable World Models

In human-robot collaboration, natural language lets people direct a humanoid's whole-body movements without programming joint trajectories.

arXiv: https://arxiv.org/abs/2611.24074

#worldmodels #robotics
```

</details>

---

### [SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042)

**Authors:** Jenna Kang, Bingxuan Li, Colin Groth, Anatolii Evdokimov, Sai Zhang et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30042) | [PDF](https://arxiv.org/pdf/2611.30042)

<details>
<summary>Abstract</summary>

Interactive world models generate virtual environments autoregressively from player actions and visual history. However, visual history alone cannot reliably capture the evolving states of independently acting non-player characters (NPCs) in real games, particularly when they are outside the camera view. Recent multi-agent world models address this challenge through joint multi-view generation or persistent shared state, but often rely on external observations, like maps or scene geometry, or predefined state transitions. We present SWAM, a State-aware World Action Model that separates agent-s...

</details>

<details>
<summary>Share</summary>

```
SWAM: State-aware World Action Model for Multi-Agent 3D Environments

Interactive world models generate virtual environments autoregressively from player actions and visual history.

arXiv: https://arxiv.org/abs/2611.30042

#worldmodels #robotics
```

</details>

---

### [World Models and the Law](https://arxiv.org/abs/2611.29899)

**Authors:** Claudio Novelli

**Published:** 2026-11-23 | **Categories:** cs.ET, cs.AI, cs.CY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29899) | [PDF](https://arxiv.org/pdf/2611.29899)

<details>
<summary>Abstract</summary>

Current AI may have a model of how we use human language, but this does not translate into a reliable representation of physical reality. World models promise to fill this gap by learning how an environment changes over time and predicting the consequences of an action, and they are already used to steer robots and generate explorable worlds. This article asks how AI regulation in three major legal contexts, the European Union, California, and China, copes with the distinctive challenges they raise. I propose a definition and a taxonomy of world models based on who or what acts on their predic...

</details>

<details>
<summary>Share</summary>

```
World Models and the Law

Current AI may have a model of how we use human language, but this does not translate into a reliable representation of physical reality.

arXiv: https://arxiv.org/abs/2611.29899

#worldmodels #robotics
```

</details>

---

### [World Models Are the Right Foundation for Simulating Mars Terraforming](https://arxiv.org/abs/2611.29856)

**Authors:** Sameera S Kashyap, Akshitha Nagaraj, Razvan Marinescu

**Published:** 2026-11-23 | **Categories:** cs.LG, astro-ph.EP, astro-ph.IM | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29856) | [PDF](https://arxiv.org/pdf/2611.29856)

<details>
<summary>Abstract</summary>

Terraforming Mars is a long-horizon, action-conditioned control problem that requires predicting atmospheric responses to interventions over centuries to identify effective policies. This position paper argues that physics-regularized recurrent state-space world models are the most promising foundation for this setting. Data-driven climate emulators lack action-conditioning, and physics-based general circulation models (GCMs) are too expensive for policy search. Among learned world models, recurrent state-space architectures with physics constraints are better suited than transformer-based alt...

</details>

<details>
<summary>Share</summary>

```
World Models Are the Right Foundation for Simulating Mars Terraforming

Terraforming Mars is a long-horizon, action-conditioned control problem that requires predicting atmospheric responses to interventions over centuries to identify effective policies.

arXiv: https://arxiv.org/abs/2611.29856

#worldmodels #robotics
```

</details>

---

### [SilentWAM: Planning in the Masked State of a Diffusion World Model](https://arxiv.org/abs/2611.29125)

**Authors:** Ziyu Zhao, Casey Sun, Zeyu Wang, Shicong Ma, Emily T Zhang et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.29125) | [PDF](https://arxiv.org/pdf/2611.29125)

<details>
<summary>Abstract</summary>

World-action models learn from future prediction, but accessing their future representations directly at test time can require costly frame generation. Methods that generate future frames before planning incur additional forward passes, while future co-training methods omit explicit future predictions at inference. We introduce \method, a planner that reads the hidden states of masked future tokens without decoding future frames. We pretrain MMaDA-Parallel-M on driving video using frame-level masked world modeling, which predicts a masked suffix of future frames and explicitly includes inputs...

</details>

<details>
<summary>Share</summary>

```
SilentWAM: Planning in the Masked State of a Diffusion World Model

World-action models learn from future prediction, but accessing their future representations directly at test time can require costly frame generation.

arXiv: https://arxiv.org/abs/2611.29125

#worldmodels #robotics
```

</details>

---

### [When Do Better Visual World Models Make Better Plans? Decision-Aligned Selection for Latent Planning](https://arxiv.org/abs/2611.28919)

**Authors:** Chan Aristella Lu, Arya Fayyazi, Junil Yeo, Jin Lu, Kyu Hyung Lee et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28919) | [PDF](https://arxiv.org/pdf/2611.28919)

<details>
<summary>Abstract</summary>

Visual world models enable goal-conditioned planning by predicting the outcomes of candidate actions in latent space. However, planning depends on how well a model ranks candidates, whereas training optimizes how accurately it predicts each one. We identify the Decision-Relevant Residual (DRR), the part of the cost error that can reorder candidates, and show that the more training reduces the DRR, the more it improves selection (Spearman $ρ= 0.82$, vs. $0.61$ for prediction error). Building on this insight, we introduce Decision-Aligned Selection (DAS), a plug-in selection rule that scores can...

</details>

<details>
<summary>Share</summary>

```
When Do Better Visual World Models Make Better Plans? Decision-Aligned Selection for Latent Planning

Visual world models enable goal-conditioned planning by predicting the outcomes of candidate actions in latent space.

arXiv: https://arxiv.org/abs/2611.28919

#worldmodels #robotics
```

</details>

---

### [ViTrust: Learning 3D Observation Trust for Deformable Physical World Models](https://arxiv.org/abs/2611.28815)

**Authors:** Zhihao Guo, Zhihao Li, Xu Ge, Lijian Zhong, Yu Lu et al. (8 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28815) | [PDF](https://arxiv.org/pdf/2611.28815)

<details>
<summary>Abstract</summary>

Learning deformable physical world models requires dynamics that generalize beyond observed motion. Accurate reconstruction alone does not ensure accurate future prediction, motivating us to learn how observations should influence physical identification. However, visual reliability alone does not determine how informative an observation is about physical dynamics. We propose ViTrust to learn 3D observation trust, determining how strongly each tracked point influences physical identification. Its key design is a visual-contact trust adapter that combines pointwise spatiotemporal evidence with...

</details>

<details>
<summary>Share</summary>

```
ViTrust: Learning 3D Observation Trust for Deformable Physical World Models

Learning deformable physical world models requires dynamics that generalize beyond observed motion.

arXiv: https://arxiv.org/abs/2611.28815

#worldmodels #robotics
```

</details>

---

### [ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2611.28792)

**Authors:** Weiming Chen, Shuaiyan Liu, Xinyu Shao, Zhewen Chen, Tian Guan et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28792) | [PDF](https://arxiv.org/pdf/2611.28792) | [Project Page](https://m4a1tastegood.github.io/ArgsWorld/)

<details>
<summary>Abstract</summary>

Autoregressive diffusion world models deliver strong video generation performance, yet they typically output only RGB frames rather than explicit 3D Gaussian Splatting (3DGS) scene representations, creating a gap between learned visual world dynamics and usable 3D assets for downstream robotics, simulation and rendering. To bridge this gap, we introduce ArgsWorld, an autoregressive diffusion model that also produces an explicit 3DGS scene. For each generation chunk, the diffusion transformer jointly processes clean historical image latents and noisy latents for new views. It keeps the historic...

</details>

<details>
<summary>Share</summary>

```
ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer

Autoregressive diffusion world models deliver strong video generation performance, yet they typically output only RGB frames rather than explicit 3D Gaussian Splatting (3DGS) scene representations, creating a gap betw...

arXiv: https://arxiv.org/abs/2611.28792
Project page: https://m4a1tastegood.github.io/ArgsWorld/

#worldmodels #robotics
```

</details>

---

### [AERIN: Aerial Instance Navigation with a Visual World Model](https://arxiv.org/abs/2611.28723)

**Authors:** Zhenzhen Jiao, Rui Tian, Zhineng Chen

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28723) | [PDF](https://arxiv.org/pdf/2611.28723)

<details>
<summary>Abstract</summary>

Searching from high altitude and navigating to a target instance specified by a reference image is a common application for UAVs. In such tasks, high-altitude observations provide broad ground coverage for efficient search, but targets occupy fewer pixels, making instance verification and action selection more difficult. We present AERIN, a visual world model that uses action-conditioned prediction to guide the UAV toward the target while adjusting its viewpoint to obtain higherquality observations for subsequent instance verification. Highaltitude navigation requires fine-grained target detai...

</details>

<details>
<summary>Share</summary>

```
AERIN: Aerial Instance Navigation with a Visual World Model

Searching from high altitude and navigating to a target instance specified by a reference image is a common application for UAVs.

arXiv: https://arxiv.org/abs/2611.28723

#worldmodels #robotics
```

</details>

---

### [RecallWorld: Episodic Memory for Persistent Embodied Video World Models](https://arxiv.org/abs/2611.28666)

**Authors:** Sarosij Bose, Gitika Karumuri, Chenqi Li, Allen Tu, Srikumar Sastry et al. (10 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28666) | [PDF](https://arxiv.org/pdf/2611.28666)

<details>
<summary>Abstract</summary>

Video world models generate plausible novel views but often lack persistent memory, failing to preserve a place's geometry and appearance when an agent revisits a scene. A central challenge is how previous views should be effectively used for creating memory. Reconstructing them independently underutilizes geometric constraints between nearby views, while repeatedly reconstructing a growing history can propagate later prediction errors into earlier geometry. We introduce RecallWorld, a persistent embodied video world model that jointly reconstructs short multi-view episodes into Scenelets whil...

</details>

<details>
<summary>Share</summary>

```
RecallWorld: Episodic Memory for Persistent Embodied Video World Models

Video world models generate plausible novel views but often lack persistent memory, failing to preserve a place's geometry and appearance when an agent revisits a scene.

arXiv: https://arxiv.org/abs/2611.28666

#worldmodels #robotics
```

</details>

---

### [WorldWeave: Rethinking Embodied Navigation through Cross-Task World Modeling](https://arxiv.org/abs/2611.28553)

**Authors:** Xuan Yao, Jiahao Zhang, Rongjunchen Zhang, Kaixuan Huang, Junyu Gao et al. (6 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28553) | [PDF](https://arxiv.org/pdf/2611.28553)

<details>
<summary>Abstract</summary>

Mobile embodied agents continuously alter their observations through their own motion, while external dynamics further shape future interactions. Different mobile embodied tasks therefore capture complementary patterns of state evolution, yet jointly learning world dynamics across such interactions remains less explored. We investigate this problem through Vision-and-Language Navigation (VLN) and Embodied Visual Tracking (EVT), which respectively involve navigation toward a stationary goal and interaction with a moving target. We propose WorldWeave, a cross-task world model that couples shared...

</details>

<details>
<summary>Share</summary>

```
WorldWeave: Rethinking Embodied Navigation through Cross-Task World Modeling

Mobile embodied agents continuously alter their observations through their own motion, while external dynamics further shape future interactions.

arXiv: https://arxiv.org/abs/2611.28553

#worldmodels #robotics
```

</details>

---

### [Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics](https://arxiv.org/abs/2611.27029)

**Authors:** Weikang Qiu, Zheng Huang, Tinglin Huang, Yujun Yan, Rex Ying

**Published:** 2026-11-20 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.27029) | [PDF](https://arxiv.org/pdf/2611.27029)

<details>
<summary>Abstract</summary>

Motor decoding from electroencephalography (EEG) supports non-invasive brain-computer interfaces, yet existing methods either rely on costly cue-based trials and coarse categorical labels or use pretraining objectives that do not directly capture how movement unfolds, limiting their ability to learn transferable motor representations. To this end, we propose the Mind World Model (MWM), a framework that learns motor EEG representations from scalable naturalistic EEG and egocentric video without action annotations. MWM treats EEG observed up to the current frame as the latent action of a world m...

</details>

<details>
<summary>Share</summary>

```
Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics

Motor decoding from electroencephalography (EEG) supports non-invasive brain-computer interfaces, yet existing methods either rely on costly cue-based trials and coarse categorical labels or use pretraining objectives...

arXiv: https://arxiv.org/abs/2611.27029

#worldmodels #robotics
```

</details>

---

### [Scalable Beckmann Maps Improve One-step Generation](https://arxiv.org/abs/2611.28286)

**Authors:** Ulrik Unneberg, Shiyi Wang, Lee Cheuk-Kit, Felix Berg, Boris Kozinsky et al. (8 authors)

**Published:** 2026-11-20 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28286) | [PDF](https://arxiv.org/pdf/2611.28286) | [Project Page](https://tullebulle.github.io/projects/sbm/)

<details>
<summary>Abstract</summary>

Beckmann Transport Models (BTM) learn one-step generative maps end-to-end from data, without a teacher, a distillation stage, or pretrained features. We introduce Scalable Beckmann Maps (SBM), which bring to BTM the two ingredients behind the quality of modern multistep generators: classifier-free guidance (CFG) and a training recipe that scales, while keeping sampling at a single network evaluation. CFG combines conditional and unconditional velocity or score predictions, which a Beckmann map does not have. Our guidance rests on one observation: the BTM current is a positive multiple of an au...

</details>

<details>
<summary>Share</summary>

```
Scalable Beckmann Maps Improve One-step Generation

Beckmann Transport Models (BTM) learn one-step generative maps end-to-end from data, without a teacher, a distillation stage, or pretrained features.

arXiv: https://arxiv.org/abs/2611.28286
Project page: https://tullebulle.github.io/projects/sbm/

#worldmodels #robotics
```

</details>

---

### [Where Structure Enters a World Model: From Predictive Fit to Physical Rollout](https://arxiv.org/abs/2611.27149)

**Authors:** Panayiotis Christou, Satyapragnya Kar, Flavjo Xhelollari, Parijat Dube, Rajarshi Das

**Published:** 2026-11-20 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.27149) | [PDF](https://arxiv.org/pdf/2611.27149)

<details>
<summary>Abstract</summary>

Predictive world models learn to forecast observations, but accurate short-term predictions do not necessarily produce physically coherent behavior over longer horizons. We investigate how incorporating physical structure can strengthen world models while retaining their underlying predictive objectives. Across token-based models of planetary motion and JEPA-style visual models of mechanical systems, we study conserved-quantity supervision, symmetry-aware representations, temporal consistency, and learned structured dynamics. In planetary motion, angular-momentum supervision improves autonomou...

</details>

<details>
<summary>Share</summary>

```
Where Structure Enters a World Model: From Predictive Fit to Physical Rollout

Predictive world models learn to forecast observations, but accurate short-term predictions do not necessarily produce physically coherent behavior over longer horizons.

arXiv: https://arxiv.org/abs/2611.27149

#worldmodels #robotics
```

</details>

---

### [Plan4D: Generative Plannable 4D Worlds](https://arxiv.org/abs/2611.26516)

**Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu et al. (6 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26516) | [PDF](https://arxiv.org/pdf/2611.26516) | [Project Page](https://fogradio.github.io/plan4d-project)

<details>
<summary>Abstract</summary>

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth, cameras, point clouds, and scene flow from an observed scene context and text-specified actions. Since training data with paired actions and dense 4D annotations is inherently scarce, pla...

</details>

<details>
<summary>Share</summary>

```
Plan4D: Generative Plannable 4D Worlds

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling.

arXiv: https://arxiv.org/abs/2611.26516
Project page: https://fogradio.github.io/plan4d-project

#worldmodels #robotics
```

</details>

---

### [LATER: Learning Action-Conditioned Temporal Evidence Retrieval for Predictive World Models](https://arxiv.org/abs/2611.25671)

**Authors:** Zihan Zhou, Wenxi Xu, Qilin Wang, Hao Tang

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.25671) | [PDF](https://arxiv.org/pdf/2611.25671)

<details>
<summary>Abstract</summary>

Early interactions can reveal physical properties that later observations no longer show. These properties can still gov- ern the effects of future actions. Inspired by the distinction between retention and selective readout in working mem- ory and cognitive science, we introduce LATER, an action- conditioned world model built on CF-JEPA. LATER stores completed real transitions in partitioned memories that remain fixed during candidate rollouts. A response bridge queries these memories using the current state and candidate action, while multi-cut auxiliary supervision trains the memory writ- e...

</details>

<details>
<summary>Share</summary>

```
LATER: Learning Action-Conditioned Temporal Evidence Retrieval for Predictive World Models

Early interactions can reveal physical properties that later observations no longer show.

arXiv: https://arxiv.org/abs/2611.25671

#worldmodels #robotics
```

</details>

---

### [Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response](https://arxiv.org/abs/2611.25626)

**Authors:** Yutao Li, Chen Wang, Wangmeng Zuo, Hui Li

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.25626) | [PDF](https://arxiv.org/pdf/2611.25626)

<details>
<summary>Abstract</summary>

Do video world models learn physical laws without a physics loss, or merely imitate motion? Overall motion and appearance scores cannot settle it. We investigate this through nonlinear forced response: an excitation shakes the support of a suspended object. We introduce dual visual-numeric conditioning and adapt six image-to-video backbones to predict this motion using only the flow-matching loss. Wan predicts motion accurately and generalizes to unseen excitations, objects, poses, and scenes. Counterfactual tests suggest capabilities beyond replaying training videos. But what laws have they l...

</details>

<details>
<summary>Share</summary>

```
Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response

Do video world models learn physical laws without a physics loss, or merely imitate motion?

arXiv: https://arxiv.org/abs/2611.25626

#worldmodels #robotics
```

</details>

---

### [WorldRuler: Interactive World Modeling under Configurable Rules](https://arxiv.org/abs/2611.24869)

**Authors:** Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu et al. (9 authors)

**Published:** 2026-11-18 (updated 2026-11-19) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24869) | [PDF](https://arxiv.org/pdf/2611.24869) | [Project Page](https://alaya-lab.github.io/WorldRuler/)

<details>
<summary>Abstract</summary>

Rules govern how player actions change interactive worlds. Different rules create distinct gameplay experiences within similar scenes and action spaces. For customizable gameplay, generative world models must follow user-defined rules beyond real-world behaviors. However, realizing user-defined rules presents two challenges: Rule-State Persistence and Rule-to-Visual Realization. The former requires preserving rule definitions, dependencies, and world states across saving and loading, so that restored worlds follow the established rules. The latter requires accurately realizing rule-induced cha...

</details>

<details>
<summary>Share</summary>

```
WorldRuler: Interactive World Modeling under Configurable Rules

Rules govern how player actions change interactive worlds.

arXiv: https://arxiv.org/abs/2611.24869
Project page: https://alaya-lab.github.io/WorldRuler/

#worldmodels #robotics
```

</details>

---

### [ShoWorld: Shape-Faithful Multi-Hypothesis Occupancy World Model](https://arxiv.org/abs/2611.24457)

**Authors:** Zhiqiang Yan, Guangfa Wang, Yuan Wu, Jian Yang, Gim Hee Lee

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24457) | [PDF](https://arxiv.org/pdf/2611.24457)

<details>
<summary>Abstract</summary>

Occupancy world models struggle to forecast moving objects due to motion uncertainty and shape distortion. A single trajectory can average plausible futures into an implausible path, and repeated re-voxelization can erode or inflate object shape even under correct motion. We introduce ShoWorld to address these challenges through separate motion and shape representations. The motion forecaster predicts probabilistic trajectories conditioned on scene layout, nearby agents and the future ego trajectory. Each hypothesis is rendered into occupancy and fused according to its probability to retain al...

</details>

<details>
<summary>Share</summary>

```
ShoWorld: Shape-Faithful Multi-Hypothesis Occupancy World Model

Occupancy world models struggle to forecast moving objects due to motion uncertainty and shape distortion.

arXiv: https://arxiv.org/abs/2611.24457

#worldmodels #robotics
```

</details>

---

### [Embodied Graph: A Relational World Model for Long-Horizon Tasks](https://arxiv.org/abs/2611.24115)

**Authors:** Zongyuan Wu, Xin Wang, Tongtong Feng, Yuan Meng, Zeyang Zhang et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24115) | [PDF](https://arxiv.org/pdf/2611.24115)

<details>
<summary>Abstract</summary>

Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success. World models tackle this by learning latent dynamics for imagination-based planning. However, existing approaches merely rely on dense pixel-level observations, which forces the model to absorb redundant information while overlooking relations among task-relevant entities. Consequently, small errors may accumulate over long imagined rollouts and gradually corrupt the predictions. In this paper, we explore world models that imagine over spar...

</details>

<details>
<summary>Share</summary>

```
Embodied Graph: A Relational World Model for Long-Horizon Tasks

Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success.

arXiv: https://arxiv.org/abs/2611.24115

#worldmodels #robotics
```

</details>

---

### [Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models](https://arxiv.org/abs/2611.29839)

**Authors:** Xin Zhou, Cong Miao

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.29839) | [PDF](https://arxiv.org/pdf/2611.29839)

<details>
<summary>Abstract</summary>

Causal video world models generate block by block from their own previous outputs. Small errors in early blocks are fed back as history and grow until the scene and the robot fall apart. Teacher forcing trains on clean ground-truth history, so the model never sees the history it will actually condition on, and it also finds a shortcut: copying the previous frame instead of predicting how the scene changes. We present Dynamics Forcing, a training scheme that keeps real video as the only supervision and reshapes how history is presented. History is perturbed in three ways: random noising, self-r...

</details>

<details>
<summary>Share</summary>

```
Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models

Causal video world models generate block by block from their own previous outputs.

arXiv: https://arxiv.org/abs/2611.29839

#worldmodels #robotics
```

</details>

---

### [What Test-Time Training Corrects in Latent World Models? A Slow-Fast Approach](https://arxiv.org/abs/2611.29453)

**Authors:** Shuaicheng Niu, Guohao Chen, Kevin Z. Shen, Yunbei Zhang, Peilin Zhao et al. (7 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.29453) | [PDF](https://arxiv.org/pdf/2611.29453)

<details>
<summary>Abstract</summary>

Latent world models plan toward a goal by predicting the outcomes of candidate actions, but under the distribution shift, prediction errors can lead the planner astray. Test-time training using executed actions helps, yet what it corrects and whether its updates should persist across episodes remains unclear. We address both by analyzing the world model's prediction error. On PushObj, an object-pushing task, we probe multiple actions from the same state and decompose the error into an offset shared across actions and an action-dependent component. The offset effectively shifts the planner's go...

</details>

<details>
<summary>Share</summary>

```
What Test-Time Training Corrects in Latent World Models? A Slow-Fast Approach

Latent world models plan toward a goal by predicting the outcomes of candidate actions, but under the distribution shift, prediction errors can lead the planner astray.

arXiv: https://arxiv.org/abs/2611.29453

#worldmodels #robotics
```

</details>

---

### [World Models for Ocean Engineering: A Critical Review of Maritime Autonomy, Adaptive Latent Prediction, Digital Twins, and Biodiversity Monitoring](https://arxiv.org/abs/2611.28978)

**Authors:** Basma Dokkara, Esteban W. G. Cluab, Luiz M. G. Goncalves, Paolo Spagnolo, Cosimo Distante

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.28978) | [PDF](https://arxiv.org/pdf/2611.28978)

<details>
<summary>Abstract</summary>

Marine robots face partial observability, non-stationary dynamics, and sparse communication, motivating WMs that learn compact predictive states for planning. This review develops a functional taxonomy of WMs for ocean engineering, focusing on Joint-Embedding Predictive Architectures (JEPAs) and AdaJEPA's test-time adaptation within model predictive control, mapping them to navigation, adaptive sampling, digital twins, and biodiversity monitoring, and separating demonstrated evidence from prospective applications. The synthesis identifies key Gaps: benchmarks, uncertainty calibration, safe ada...

</details>

<details>
<summary>Share</summary>

```
World Models for Ocean Engineering: A Critical Review of Maritime Autonomy, Adaptive Latent Prediction, Digital Twins, and Biodiversity Monitoring

Marine robots face partial observability, non-stationary dynamics, and sparse communication, motivating WMs that learn compact predictive states for planning.

arXiv: https://arxiv.org/abs/2611.28978

#worldmodels #robotics
```

</details>

---

### [Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking](https://arxiv.org/abs/2611.27648)

**Authors:** Xuzhe Dang, Stefan Edelkamp

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.27648) | [PDF](https://arxiv.org/pdf/2611.27648)

<details>
<summary>Abstract</summary>

Training a humanoid motion tracker by backpropagating imagined returns through a learned world model is fast, because the model gives a first-order policy gradient. We ask how much of that gradient holds in the simulator. On a tracker for the Unitree G1, the $0.5\%$ of imagined rollouts with the largest gradients carry $22\%$ of the summed gradient norm, yet neither a second rollout from the same state nor the simulator confirms them. When the actions are moved along the model's gradient, the simulator returns 94% of the predicted change in return where the gradient norm is below the batch med...

</details>

<details>
<summary>Share</summary>

```
Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking

Training a humanoid motion tracker by backpropagating imagined returns through a learned world model is fast, because the model gives a first-order policy gradient.

arXiv: https://arxiv.org/abs/2611.27648

#worldmodels #robotics
```

</details>

---

### [Latent Space Planning with Sequential Monte Carlo](https://arxiv.org/abs/2611.26706)

**Authors:** Hrishikesh Viswanath, Anindita Ghosh, Uttaran Bhattacharya, Aniket Bera

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.26706) | [PDF](https://arxiv.org/pdf/2611.26706)

<details>
<summary>Abstract</summary>

Planning with learned world models amounts to finding action sequences whose predicted rollouts reach a goal. Sampling-based planners often struggle at longer horizons, while gradient-based methods can become trapped in local minima. Meanwhile, model predictive path integral control (MPPI), a complementary approach, alternates between estimating an expectation under a cost-weighted distribution from samples and updating the plan from this estimate. Its samples, however, are drawn afresh at every iteration from a Gaussian proposal and reach the target distribution only through importance weight...

</details>

<details>
<summary>Share</summary>

```
Latent Space Planning with Sequential Monte Carlo

Planning with learned world models amounts to finding action sequences whose predicted rollouts reach a goal.

arXiv: https://arxiv.org/abs/2611.26706

#worldmodels #robotics
```

</details>

---

### [Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models](https://arxiv.org/abs/2611.25980)

**Authors:** John Won, Yonghoon Dong, Jinwoo Shin

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.25980) | [PDF](https://arxiv.org/pdf/2611.25980)

<details>
<summary>Abstract</summary>

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. Yet despite producing increasingly realistic videos, current world models often fail to capture how small action changes affect future observations. This limits their use in tasks such as robotic policy evaluation and model-based planning, where nearly identical actions can lead to qualitatively different outcomes. To address this, we propose AFFECT, an auxiliary training objective for learning the distribution of visual changes induced by act...

</details>

<details>
<summary>Share</summary>

```
Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world.

arXiv: https://arxiv.org/abs/2611.25980

#worldmodels #robotics
```

</details>

---

### [When to Refine: Selective Search for Frozen Visual World Models](https://arxiv.org/abs/2611.24470)

**Authors:** Jingni Huang

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.24470) | [PDF](https://arxiv.org/pdf/2611.24470)

<details>
<summary>Abstract</summary>

Planning with a visual world model requires deciding both which actions to execute and how long to search for them. We introduce Selective CEM Refinement (SCR), a learned rule for deciding whether to continue cross-entropy method (CEM) search with a frozen LeWorldModel. After five it- erations, the gate measures how far the mean first action chunk has moved, how much the mean terminal cost of elite plans has fallen, and how widely their first chunks vary. It returns the current plan for execution or continues the same search for ten more iterations. The gate requires no addi- tional world-mode...

</details>

<details>
<summary>Share</summary>

```
When to Refine: Selective Search for Frozen Visual World Models

Planning with a visual world model requires deciding both which actions to execute and how long to search for them.

arXiv: https://arxiv.org/abs/2611.24470

#worldmodels #robotics
```

</details>

---

### [Measuring the Conservatism of Latent Safety Filters for World Models](https://arxiv.org/abs/2611.23685)

**Authors:** Johannes Mootz, Mani Amani, Reza Akhavian

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.LG, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.23685) | [PDF](https://arxiv.org/pdf/2611.23685)

<details>
<summary>Abstract</summary>

A latent safety filter decides from the latent of a world model whether a planned action is safe. Conformal calibration sets the threshold of the filter so that it accepts an unsafe action only with a small probability. However, the filter can still be conservative and refuse many safe actions, depending on the latent. To measure the conservatism that a latent forces on the filter, we group similar latents and actions into cells. A filter that gives one decision per cell can refuse the unsafe transitions of a cell only by refusing the safe ones in it as well. We call the share of safe transiti...

</details>

<details>
<summary>Share</summary>

```
Measuring the Conservatism of Latent Safety Filters for World Models

A latent safety filter decides from the latent of a world model whether a planned action is safe.

arXiv: https://arxiv.org/abs/2611.23685

#worldmodels #robotics
```

</details>

---

### [ActField: Learning Action Effects as Continuous-Time Latent Dynamics](https://arxiv.org/abs/2611.30659)

**Authors:** Yunpeng Qing, Yuheng Huang, Changxu Wei, Yilun Kong, Yichen Shi et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30659) | [PDF](https://arxiv.org/pdf/2611.30659)

<details>
<summary>Abstract</summary>

Learning how actions change visual states is essential for prediction and decision-making in embodied tasks. Existing action-conditioned JEPA world models typically predict future representations at discrete observation intervals, leaving the temporal evolution of action effects implicit. We introduce ActField, a continuous-time JEPA world model that explicitly models latent state evolution through an action-conditioned vector field integrated over physical time. ActField separates action-independent evolution from action-induced changes, with the latter modulated by the latent context. A refe...

</details>

<details>
<summary>Share</summary>

```
ActField: Learning Action Effects as Continuous-Time Latent Dynamics

Learning how actions change visual states is essential for prediction and decision-making in embodied tasks.

arXiv: https://arxiv.org/abs/2611.30659

#worldmodels #robotics
```

</details>

---

### [What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion](https://arxiv.org/abs/2611.29759)

**Authors:** Renhao Zhang, Abhranil Chandra, Bruno Castro da Silva

**Published:** 2026-11-22 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.29759) | [PDF](https://arxiv.org/pdf/2611.29759)

<details>
<summary>Abstract</summary>

We introduce MotionPort, which learns low-dimensional latent representations of body motion for accurate dynamics prediction and effective long-horizon planning. Existing world-model planners often search over action representations learned for prediction, yet we show that predictive accuracy alone does not ensure that optimization can discover successful trajectories. MotionPort addresses this mismatch by representing body trajectories rather than action chunks and organizing the search space by motion similarity, helping predicted improvements translate into successful execution. Without fin...

</details>

<details>
<summary>Share</summary>

```
What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion

We introduce MotionPort, which learns low-dimensional latent representations of body motion for accurate dynamics prediction and effective long-horizon planning.

arXiv: https://arxiv.org/abs/2611.29759

#worldmodels #robotics
```

</details>

---

### [RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields](https://arxiv.org/abs/2611.29282)

**Authors:** Hu Zhou, Jiazhou Zhou, Shuowen Zhang, Ying-Chang Liang, Liang Liu

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.NI, eess.SP | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.29282) | [PDF](https://arxiv.org/pdf/2611.29282)

<details>
<summary>Abstract</summary>

Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing. However, existing neural RF field methods suffer from three fundamental limitations: (1) they predominantly rely on per-scene optimization and cannot generalize to unseen scenes; (2) they require costly reference RF measurements in each target scene; and (3) they degrade severely when extrapolating beyond the vicinity of reference measurements. To overcome these limitations, we present RadioWorld, a general framework that ad...

</details>

<details>
<summary>Share</summary>

```
RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields

Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing.

arXiv: https://arxiv.org/abs/2611.29282

#worldmodels #robotics
```

</details>

---

### [Learning Land-Surface Hydrology World Model from Satellite Observations](https://arxiv.org/abs/2611.28963)

**Authors:** Suya Li, Zekun Qi, Xiaochong Xu, Duo Zhang

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.28963) | [PDF](https://arxiv.org/pdf/2611.28963)

<details>
<summary>Abstract</summary>

A world model should tell us not only what will happen, but what would happen under a different action. Learned Earth models now forecast remarkably well, yet forecast skill says little about what their state means or how it responds to a changed driver. We build LandWM, a world model of land-surface water in which rain is the action, learned from seven years of SMAP and CYGNSS observations: physical observation operators tie its latent state to soil water, and a mass-conserving balance governs how that state responds to rain. Over the U.S. Southern Great Plains, the model, never shown a soil-...

</details>

<details>
<summary>Share</summary>

```
Learning Land-Surface Hydrology World Model from Satellite Observations

A world model should tell us not only what will happen, but what would happen under a different action.

arXiv: https://arxiv.org/abs/2611.28963

#worldmodels #robotics
```

</details>

---

### [Toward Adversarially Robust World Models](https://arxiv.org/abs/2611.28345)

**Authors:** Ethan Rathbun, Jonathan Nöther, Christopher Amato, Alina Oprea, Goran Radanović

**Published:** 2026-11-20 | **Categories:** cs.LG, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.28345) | [PDF](https://arxiv.org/pdf/2611.28345)

<details>
<summary>Abstract</summary>

Latent dynamic world models have proven to be highly versatile tools for embodied artificial intelligence systems, enabling online action planning, safe policy evaluation, and scalable policy learning. However, this versatility makes world models a vulnerable and centralized point of failure as a compromised model can impact planning, evaluation, and training at once. Therefore it is critical that the security and robustness properties of world models are properly understood before they are universally deployed in embodied AI systems. In this work we take a unifying approach towards this under...

</details>

<details>
<summary>Share</summary>

```
Toward Adversarially Robust World Models

Latent dynamic world models have proven to be highly versatile tools for embodied artificial intelligence systems, enabling online action planning, safe policy evaluation, and scalable policy learning.

arXiv: https://arxiv.org/abs/2611.28345

#worldmodels #robotics
```

</details>

---

### [Beyond Visual Fidelity: Comparing Categorical and Continuous World Models](https://arxiv.org/abs/2611.27870)

**Authors:** Sarah Parisot, Melanie Fernandez Pradier, David Bignell, Sergio Valcarcel Macua, Katja Hofmann

**Published:** 2026-11-20 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.27870) | [PDF](https://arxiv.org/pdf/2611.27870)

<details>
<summary>Abstract</summary>

Visual world models can now generate compelling interactive worlds, but visual realism does not guarantee faithful dynamics. We systematically compare how categorical and continuous prediction shape learned dynamics under both next-token and iterative whole-frame generation. These choices are often bundled in approaches such as autoregressive token models and whole-frame flow matching. We design controlled 2D and 3D environments and evaluate dynamics validity, calibration, and visual quality. In 2D with lossless visual encoding, categorical models achieve higher rollout validity with less trai...

</details>

<details>
<summary>Share</summary>

```
Beyond Visual Fidelity: Comparing Categorical and Continuous World Models

Visual world models can now generate compelling interactive worlds, but visual realism does not guarantee faithful dynamics.

arXiv: https://arxiv.org/abs/2611.27870

#worldmodels #robotics
```

</details>

---

### [PhysForce: Physics-aware Force Control for Interactive Video World Model](https://arxiv.org/abs/2611.27164)

**Authors:** Xuancheng Xu, Xiaofeng Wang, Yue Ma, Zheng Zhu, Bing-Kun Bao

**Published:** 2026-11-20 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.27164) | [PDF](https://arxiv.org/pdf/2611.27164)

<details>
<summary>Abstract</summary>

Interactive video world models aim to predict how visual environments evolve in response to user interventions, including physically consistent state changes induced by applied forces. Existing methods often represent forces as motion trajectories, which may introduce inappropriate motion priors, causing the model to over-rely on encoded displacement patterns. More fundamentally, the model's internal representations do not reliably localize force-induced state changes, making it difficult to associate applied forces with their resulting physical responses. Also, limited force-annotated data ma...

</details>

<details>
<summary>Share</summary>

```
PhysForce: Physics-aware Force Control for Interactive Video World Model

Interactive video world models aim to predict how visual environments evolve in response to user interventions, including physically consistent state changes induced by applied forces.

arXiv: https://arxiv.org/abs/2611.27164

#worldmodels #robotics
```

</details>

---

### [A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models](https://arxiv.org/abs/2611.27124)

**Authors:** Huiyuan Tian, Chih-Yung Wen, Shijian Li

**Published:** 2026-11-20 | **Categories:** cs.LG, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.27124) | [PDF](https://arxiv.org/pdf/2611.27124)

<details>
<summary>Abstract</summary>

If we optimize an image until a classifier is confident it shows a cat, we may get an adversarial example, not a cat. Planning with a latent world model is a similar search for actions whose predicted future is closest to the goal. Is the result a plan, or an adversarial example of the world model? We show that it can be either. On the released DINO-WM and LeWM, more iterations of the cross-entropy method (CEM) lower the predicted cost but lose up to half of the problems CEM had already solved. The model's own predictions do not reveal these failures. We propose a simple test that executes the...

</details>

<details>
<summary>Share</summary>

```
A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models

If we optimize an image until a classifier is confident it shows a cat, we may get an adversarial example, not a cat.

arXiv: https://arxiv.org/abs/2611.27124

#worldmodels #robotics
```

</details>

---

### [FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities](https://arxiv.org/abs/2611.26419)

**Authors:** Bassam El Said, Adam Sobey

**Published:** 2026-11-19 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.26419) | [PDF](https://arxiv.org/pdf/2611.26419)

<details>
<summary>Abstract</summary>

Each fibre-reinforced composite structure has a unique material architecture. The manufacturing methods used and the presence of defects lead to local variations which require material-scale models that can resolve the response in real time at every location in the structure. Concurrent multi-scale schemes provide this capability, but at a prohibitive computational cost for large structures as the number of integration points and time increments scales with size. Surrogates have been studied extensively as replacements for material-scale models to mitigate these computational limitations. A su...

</details>

<details>
<summary>Share</summary>

```
FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities

Each fibre-reinforced composite structure has a unique material architecture.

arXiv: https://arxiv.org/abs/2611.26419

#worldmodels #robotics
```

</details>

---

### [World Models Favor Learned Priors over Visual Evidence](https://arxiv.org/abs/2611.26366)

**Authors:** Han Xiao, Zhiyong Bao, Xiaotong Liu, Yanhao Chen, Qingqiang Wu

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.26366) | [PDF](https://arxiv.org/pdf/2611.26366)

<details>
<summary>Abstract</summary>

World models are increasingly used to simulate physical interactions, but training a separate model for each environment limits scalability. Cross-environment prediction requires identifying the current physical rule, which appearance alone may not reveal. We therefore study visual calibration: using object motion and interactions in a short video as direct evidence to infer the current rule and predict motion under that rule from a different initial state. However, differences in data availability across physical conditions can yield a long-tailed training distribution, biasing models toward...

</details>

<details>
<summary>Share</summary>

```
World Models Favor Learned Priors over Visual Evidence

World models are increasingly used to simulate physical interactions, but training a separate model for each environment limits scalability.

arXiv: https://arxiv.org/abs/2611.26366

#worldmodels #robotics
```

</details>

---

### [SpecWM: Turning Verification into Refinement for Streaming World Models](https://arxiv.org/abs/2611.26211)

**Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu et al. (12 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.26211) | [PDF](https://arxiv.org/pdf/2611.26211)

<details>
<summary>Abstract</summary>

Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference. Existing speculative methods combine their strengths through fast draft generation and selective target regeneration guided by rewards on decoded frames. However, verification covers only the external scorer's evaluation dimensions and adds decoding and scoring costs. Moreover, these scores provide no correction, requiring costly target regeneration for rejected drafts. To address these limitations, we propose Speculative World Model (SpecWM...

</details>

<details>
<summary>Share</summary>

```
SpecWM: Turning Verification into Refinement for Streaming World Models

Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference.

arXiv: https://arxiv.org/abs/2611.26211

#worldmodels #robotics
```

</details>

---

### [Can World Models Predict Rice Growth? Toward Agricultural World Models](https://arxiv.org/abs/2611.26145)

**Authors:** Wenkai Ji, Zeteng Li, Yinkun Guo, Jie Zhou, Liang He et al. (6 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.26145) | [PDF](https://arxiv.org/pdf/2611.26145)

<details>
<summary>Abstract</summary>

World models can imagine how a physical scene evolves over the next few seconds, but growers need to know how a crop will develop over weeks to months: will this rice plant have headed a month from now, and how will it look at harvest? We introduce agricultural world modeling, the task of predicting how the same plant will look at a requested horizon of days to months, from one photo of it, its cultivar, and its camera view. In preliminary analysis, even state-of-the-art image generators get this wrong: they often grow the plant too little or give it the color and form of the wrong growth stag...

</details>

<details>
<summary>Share</summary>

```
Can World Models Predict Rice Growth? Toward Agricultural World Models

World models can imagine how a physical scene evolves over the next few seconds, but growers need to know how a crop will develop over weeks to months: will this rice plant have headed a month from now, and how will i...

arXiv: https://arxiv.org/abs/2611.26145

#worldmodels #robotics
```

</details>

---

### [Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models](https://arxiv.org/abs/2611.25594)

**Authors:** Xinze Shi, Litian Zhang, Zhenjie Su, Zelong Yu, Yuting Zhang et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.25594) | [PDF](https://arxiv.org/pdf/2611.25594)

<details>
<summary>Abstract</summary>

Comparative feedback, in which a judge says which of two candidate outcomes is closer to what happened, is a practical way to train language world models that assign probabilities to an action's outcomes. We show that, fitted with a Bradley-Terry objective, it need not teach the true outcome probabilities and can distort accurate ones. On a simulated robot push with enumerated outcome distributions, this objective takes a model that is accurate on unseen layouts (hazard error 2.4 percentage points, pp) and moves 33 to 43 pp of its probability onto outcomes that none of a condition's enumerated...

</details>

<details>
<summary>Share</summary>

```
Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models

Comparative feedback, in which a judge says which of two candidate outcomes is closer to what happened, is a practical way to train language world models that assign probabilities to an action's outcomes.

arXiv: https://arxiv.org/abs/2611.25594

#worldmodels #robotics
```

</details>

---

### [Search or Scoring? Diagnosing Why Visual World-Model Planners Fail](https://arxiv.org/abs/2611.25347)

**Authors:** Haoxuan Jia, Yang Liu, Shang Luo, Chenhao Wu, Zixiang Ni et al. (13 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

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

### [HandWorldBench: A Unified Benchmark for Hand-Centric World Models](https://arxiv.org/abs/2611.24731)

**Authors:** Zhaolu Wang, Jiacheng Xu, Lihong Wang, Shuqing Wang, Jianjie Fang et al. (15 authors)

**Published:** 2026-11-18 (updated 2026-11-21) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.24731) | [PDF](https://arxiv.org/pdf/2611.24731)

<details>
<summary>Abstract</summary>

Recent advances in world models are opening new possibilities for fine-grained embodied tasks, with hand-object interaction offering a particularly demanding setting. Modeling these interactions involves capturing how hand actions change objects and how the resulting states persist over time. Yet systematic evaluation tailored to these hand-centric capabilities remains underdeveloped. To address this gap, we introduce HandWorldBench, a unified benchmark that systematically evaluates hand-centric world models across human hands, simulated dexterous hands, and real dexterous hands along six dime...

</details>

<details>
<summary>Share</summary>

```
HandWorldBench: A Unified Benchmark for Hand-Centric World Models

Recent advances in world models are opening new possibilities for fine-grained embodied tasks, with hand-object interaction offering a particularly demanding setting.

arXiv: https://arxiv.org/abs/2611.24731

#worldmodels #robotics
```

</details>

---

### [Comparing Each Generation with Independent Siblings Gives Video World Model Post-Training a Proper Objective for Outcome Frequencies](https://arxiv.org/abs/2611.24512)

**Authors:** Xin Li, Yiwen Chen

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.24512) | [PDF](https://arxiv.org/pdf/2611.24512)

<details>
<summary>Abstract</summary>

Video world models are used as simulators, so when a first frame leaves several physical outcomes open, repeated generations should produce each outcome as often as it occurs in the data. Physics post-training scores every generation against the single recorded future of its history, which makes single videos more faithful, but the expected score is linear in the model distribution and is maximized by always producing the most likely outcome. The log-likelihood of the recorded outcome is maximized by the data distribution, and its gradient weights agreement with the record by the inverse of ho...

</details>

<details>
<summary>Share</summary>

```
Comparing Each Generation with Independent Siblings Gives Video World Model Post-Training a Proper Objective for Outcome Frequencies

Video world models are used as simulators, so when a first frame leaves several physical outcomes open, repeated generations should produce each outcome as often as it occurs in the data.

arXiv: https://arxiv.org/abs/2611.24512

#worldmodels #robotics
```

</details>

---

### [Target-Consistent Action Guidance via Semi-Unbalanced Optimal Transport for Drifting World Models](https://arxiv.org/abs/2611.24222)

**Authors:** Md Abtahi Majeed Chowdhury, Md Rifat Ur Rahman, Md Sakib Hossain Shovon, Jaesik Choi, Minhyuk Sung

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.24222) | [PDF](https://arxiv.org/pdf/2611.24222)

<details>
<summary>Abstract</summary>

Action-conditioned world models let robots imagine the outcomes of their actions for planning and offline policy evaluation, but these uses need many rollouts, which multi-step diffusion makes expensive. Drifting models move the iteration from inference to training and generate samples in one network pass. DriftWorld brought this paradigm to action-conditioned world models; to strengthen action following, it repels predictions from the current frame, a construction borrowed from classifier-free guidance. We show that this accentuation has a target bias: the push persists even when a prediction...

</details>

<details>
<summary>Share</summary>

```
Target-Consistent Action Guidance via Semi-Unbalanced Optimal Transport for Drifting World Models

Action-conditioned world models let robots imagine the outcomes of their actions for planning and offline policy evaluation, but these uses need many rollouts, which multi-step diffusion makes expensive.

arXiv: https://arxiv.org/abs/2611.24222

#worldmodels #robotics
```

</details>

---

### [PhysResponse: Probing the Physics of Video Generation with Controlled Interventions](https://arxiv.org/abs/2611.24419)

**Authors:** Yuhan Li, Shuran Zhang, Haixin Tian, Baonuo Rao, Weipeng Li et al. (15 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.24419) | [PDF](https://arxiv.org/pdf/2611.24419)

<details>
<summary>Abstract</summary>

Video generation models are increasingly viewed as world simulators, which requires not only plausible motion but dynamics that respond correctly to specified physical parameters. Existing models, datasets and benchmarks, however, largely target physical plausibility, leaving this physical parameter responsiveness insufficiently explored. We introduce PhysResponse, a benchmark that measures it at two levels: scene-conditioned simulator inversion recovers the effective gravity, friction and initial speed of generated motion, and event evaluation tests outcomes near and across critical transitio...

</details>

<details>
<summary>Share</summary>

```
PhysResponse: Probing the Physics of Video Generation with Controlled Interventions

Video generation models are increasingly viewed as world simulators, which requires not only plausible motion but dynamics that respond correctly to specified physical parameters.

arXiv: https://arxiv.org/abs/2611.24419

#worldmodels #robotics
```

</details>

---

### [Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface](https://arxiv.org/abs/2611.27513)

**Authors:** Yang Liu, Chao Ye, Jiahao Zhang, Zeyuan Hou, Ruijie Fang et al. (8 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.27513) | [PDF](https://arxiv.org/pdf/2611.27513)

<details>
<summary>Abstract</summary>

We present Ego4Gen (Egocentric 4D Future Generation), a world model for 4D future generation in robotic manipu lation. Given a single egocentric image and a text prompt, Ego4Gen jointly generates temporally aligned RGB frames, dense point maps, and dense scene flow, explicitly pre dicting the evolution of scene appearance, spatial struc ture, and motion. Built on Cosmos3-Nano, Ego4Gen ex tends the pretrained generative backbone through modality routed LoRA and asymmetric attention, using geometric pseudo-labels from MotionCrafter to learn to predict future geometry and motion latents. These la...

</details>

<details>
<summary>Share</summary>

```
Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface

We present Ego4Gen (Egocentric 4D Future Generation), a world model for 4D future generation in robotic manipu lation.

arXiv: https://arxiv.org/abs/2611.27513

#worldmodels #robotics
```

</details>

---

### [From States to Dynamics: Detecting Rule Violations in OthelloGPT](https://arxiv.org/abs/2611.29715)

**Authors:** David L. Cao, Sai Sumedh R. Hindupur, Demba Ba

**Published:** 2026-11-22 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.29715) | [PDF](https://arxiv.org/pdf/2611.29715)

<details>
<summary>Abstract</summary>

Sequence models trained on game moves have been shown to encode world models, with structured linear probes revealing the underlying game states. World models, however, are inherently dynamic: in deterministic board games, a set of rules constrain how states evolve over time. We therefore ask if and how OthelloGPT, a transformer trained only on Othello move sequences, manifests the rules of the game in its activation space. We divide the rules of Othello, and symmetrically their violations, into three classes: placing a disc on an empty square (R1), flanking an opponent's disc (R2), and moving...

</details>

<details>
<summary>Share</summary>

```
From States to Dynamics: Detecting Rule Violations in OthelloGPT

Sequence models trained on game moves have been shown to encode world models, with structured linear probes revealing the underlying game states.

arXiv: https://arxiv.org/abs/2611.29715

#worldmodels #robotics
```

</details>

---

### [ClothCast: Generative Cloth World Modeling under Partial Observability](https://arxiv.org/abs/2611.29369)

**Authors:** Yushen Hu, Yilong Song, Zhen Zhou, Apurv Kushwaha, Harshvardhan Chandirasekar et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.29369) | [PDF](https://arxiv.org/pdf/2611.29369)

<details>
<summary>Abstract</summary>

World models support robotic manipulation by predicting how the scene evolves under a planned action. For garments this prediction is notoriously difficult: deformations are complex, and self-occlusion leaves much of the cloth unobserved. Planned gripper trajectories provide a useful motion prior because cloth held by a gripper moves with it, while the remaining deformation must be predicted. We introduce ClothCast, a world model that applies this prior to the cloth's points and learns the residual motion. ClothCast takes one RGB-D observation, the camera pose, the robot's own model and the pl...

</details>

<details>
<summary>Share</summary>

```
ClothCast: Generative Cloth World Modeling under Partial Observability

World models support robotic manipulation by predicting how the scene evolves under a planned action.

arXiv: https://arxiv.org/abs/2611.29369

#worldmodels #robotics
```

</details>

---

### [KineState-SWAM: A Surgical World Action Model with Explicit Kinematics and Causal Interaction Dynamics](https://arxiv.org/abs/2611.28871)

**Authors:** Rulin Zhou, Yujie Ma, Rui Tang, Qiujie Song, Wanhao Liu et al. (9 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.28871) | [PDF](https://arxiv.org/pdf/2611.28871)

<details>
<summary>Abstract</summary>

Existing surgical world models often leave implicit how instrument motion drives localized tissue responses and how interaction history informs subsequent actions. We introduce KineState-SWAM, a surgical world-action model coupling action prediction and video generation through a persistent interaction state, separating kinematically determined instrument motion from learned scene evolution. A flow-matching policy predicts joint trajectories conditioned on interaction state, robot configuration, and task instruction. Kinematic Geometry Conditioning converts these trajectories into surface-moti...

</details>

<details>
<summary>Share</summary>

```
KineState-SWAM: A Surgical World Action Model with Explicit Kinematics and Causal Interaction Dynamics

Existing surgical world models often leave implicit how instrument motion drives localized tissue responses and how interaction history informs subsequent actions.

arXiv: https://arxiv.org/abs/2611.28871

#worldmodels #robotics
```

</details>

---

### [Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus](https://arxiv.org/abs/2611.28660)

**Authors:** Bangyan Ju, Xiaolin Sun, Yibin Hu, Zizhan Zheng

**Published:** 2026-11-21 | **Categories:** cs.AI, cs.MA | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.28660) | [PDF](https://arxiv.org/pdf/2611.28660)

<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers over multiple rounds and a resolution mechanism aggregates them into a final outcome. Most multi-agent LLM frameworks assume that every participant shares the system objective. In practice, however, a malicious agent can join as a legitimate member of the group and persuade the other agents toward a hidden adversarial goal. We formalize such attacks as a sequential decision-making...

</details>

<details>
<summary>Share</summary>

```
Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus

Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers...

arXiv: https://arxiv.org/abs/2611.28660

#worldmodels #robotics
```

</details>

---

### [GameScrub: Learning HUD Removal from Real Gameplay with Recovered Targets](https://arxiv.org/abs/2611.27547)

**Authors:** Mohammad Areeb Qazi, Yiyan Hu, Yanan Wang, Xuezhi Liang, Xin Li et al. (8 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.27547) | [PDF](https://arxiv.org/pdf/2611.27547)

<details>
<summary>Abstract</summary>

Gameplay videos are a rich source of experience for learning virtual-world dynamics, yet their frames contain heads-up displays (HUDs) that follow interface rules rather than scene dynamics. Removing HUDs would make this footage directly usable for learning world dynamics. However, training a removal model requires paired clips with and without HUDs, whereas real recordings contain only HUD-overlaid footage. Existing work synthesizes pairs by compositing HUD graphics onto HUD-free footage, requiring a separately curated clean corpus and producing HUDs that only approximate real ones. Models tr...

</details>

<details>
<summary>Share</summary>

```
GameScrub: Learning HUD Removal from Real Gameplay with Recovered Targets

Gameplay videos are a rich source of experience for learning virtual-world dynamics, yet their frames contain heads-up displays (HUDs) that follow interface rules rather than scene dynamics.

arXiv: https://arxiv.org/abs/2611.27547

#worldmodels #robotics
```

</details>

---

### [PhiJEPA: Denoising Latent Predictions for Visual Representation Learning](https://arxiv.org/abs/2611.27516)

**Authors:** Makoto Yamada, Yao-Hung Hubert Tsai

**Published:** 2026-11-20 | **Categories:** cs.CV, cs.AI, stat.ML | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.27516) | [PDF](https://arxiv.org/pdf/2611.27516)

<details>
<summary>Abstract</summary>

Can a predictor trained to infer hidden image regions still help a world model plan when part of an object disappears from view and the visible context is blurred? We introduce PhiJEPA, a joint-embedding predictive architecture that adapts PhiNet's two-stage prediction to masked Transformers. From sparse, photometrically corrupted context, a Transformer block predicts hidden tokens of an independently corrupted teacher view. A token-wise MLP then maps these predictions to clean teacher tokens. Controlled ablations show that the combined objective improves dense features over the tested one-sta...

</details>

<details>
<summary>Share</summary>

```
PhiJEPA: Denoising Latent Predictions for Visual Representation Learning

Can a predictor trained to infer hidden image regions still help a world model plan when part of an object disappears from view and the visible context is blurred?

arXiv: https://arxiv.org/abs/2611.27516

#worldmodels #robotics
```

</details>

---

### [Coherence by Construction: Synthesizing CTI Knowledge Graphs and the Formal Limits of Coherence Validation](https://arxiv.org/abs/2611.26717)

**Authors:** Tanzimul Alam Fahim, Mohammad Arif Hossain

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.26717) | [PDF](https://arxiv.org/pdf/2611.26717)

<details>
<summary>Abstract</summary>

Synthesizing relational training data such as knowledge graphs with a large language model typically emits structured objects one at a time, which keeps each object valid but leaves the relationships between them ungrounded. We study an alternative paradigm, generation by simulation: rather than describing a relational artifact, we simulate a process that produces it and take the artifact to be its causal record. Language-model agents propose intent and a deterministic referee resolves outcomes against an explicit world model, so a relation is emitted only when the event it represents occurs,...

</details>

<details>
<summary>Share</summary>

```
Coherence by Construction: Synthesizing CTI Knowledge Graphs and the Formal Limits of Coherence Validation

Synthesizing relational training data such as knowledge graphs with a large language model typically emits structured objects one at a time, which keeps each object valid but leaves the relationships between them ungr...

arXiv: https://arxiv.org/abs/2611.26717

#worldmodels #robotics
```

</details>

---

### [What One Sample Cannot See: Why Fewer Denoising Steps Can Score Higher on Physics Benchmarks](https://arxiv.org/abs/2611.25632)

**Authors:** Yutao Li, Chen Wang

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25632) | [PDF](https://arxiv.org/pdf/2611.25632)

<details>
<summary>Abstract</summary>

When a storm can head north or south, a forecast down the middle may score better under squared error than either plausible path. The same paradox appears when video generators are tested as world models: fewer denoising steps can raise physics scores even as videos blur or stop moving early. Why? Physics-IQ compares each generated video with one recording, although a scene can have multiple valid futures. An exact decomposition shows its scores can reward reduced variation among generated futures, even when their distribution becomes less accurate. We introduce Kernel Physics-IQ to remove thi...

</details>

<details>
<summary>Share</summary>

```
What One Sample Cannot See: Why Fewer Denoising Steps Can Score Higher on Physics Benchmarks

When a storm can head north or south, a forecast down the middle may score better under squared error than either plausible path.

arXiv: https://arxiv.org/abs/2611.25632

#worldmodels #robotics
```

</details>

---

### [PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds](https://arxiv.org/abs/2611.25500)

**Authors:** Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang et al. (11 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25500) | [PDF](https://arxiv.org/pdf/2611.25500)

<details>
<summary>Abstract</summary>

3D worlds can now be captured, reconstructed, and generated at scale, yet the objects in them stay still: a pressed pillow does not compress, and a pulled door does not swing. Bringing these objects into interactive 4D world models requires a representation of how they can move, deform, and respond physically to user actions in real time. We present PRIO, a pre-trained representation for interactive objects. Given static geometry, PRIO predicts an object-specific configuration space in a single forward pass. This space provides generalized coordinates for Lagrangian mechanics, allowing physica...

</details>

<details>
<summary>Share</summary>

```
PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds

3D worlds can now be captured, reconstructed, and generated at scale, yet the objects in them stay still: a pressed pillow does not compress, and a pulled door does not swing.

arXiv: https://arxiv.org/abs/2611.25500

#worldmodels #robotics
```

</details>

---

### [PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction](https://arxiv.org/abs/2611.24999)

**Authors:** Ziyuan Qin, Yang Qiao, Summer B. Frandsen, Michael T. Treadway, Liang Zhao

**Published:** 2026-11-18 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

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

### [Risk-Triggered Search: Behavior-Preserving Safe Control](https://arxiv.org/abs/2611.24409)

**Authors:** Xinyu Deng, Bohao Lan, Kunpeng Li, Mingkai Yuan, Weihang Pan et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.24409) | [PDF](https://arxiv.org/pdf/2611.24409)

<details>
<summary>Abstract</summary>

Pre-trained visual world models generate multi-step action plans from current and goal observations, yet terminal-proximity objectives fail to prevent forbidden-zone traversal or rigid-body collision sliding. Purely visual interfaces may lack analytical dynamics, structured states, or explicit collision geometry, requiring internal prediction of action-conditioned process risk. We propose Risk-Triggered Search (RTS) for frozen Joint-Embedding Predictive Architecture (JEPA) world models. Rather than relying on static state features that cannot distinguish candidate plans sharing an observation,...

</details>

<details>
<summary>Share</summary>

```
Risk-Triggered Search: Behavior-Preserving Safe Control

Pre-trained visual world models generate multi-step action plans from current and goal observations, yet terminal-proximity objectives fail to prevent forbidden-zone traversal or rigid-body collision sliding.

arXiv: https://arxiv.org/abs/2611.24409

#worldmodels #robotics
```

</details>

---
