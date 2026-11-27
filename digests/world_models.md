# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-27 23:54 UTC

**Papers shown:** 112 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Long-Horizon Planning with Latent World Models via Graph Anchors](https://arxiv.org/abs/2611.34509)

**Authors:** Syed Nazmus Sakib, Abdul Monaf Chowdhury, Peizhen Li, Nafiul Haque, Chandak Chakma et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★★

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34509) | [PDF](https://arxiv.org/pdf/2611.34509) | [Project Page](https://syed-nazmus-sakib.github.io/graph-anchors/) | [Code](https://github.com/syed-nazmus-sakib/graph-anchors)

<details>
<summary>Abstract</summary>

Latent world models plan in a compact latent space by predicting the outcomes of actions. Their planners judge a plan by the latent distance between its predicted end state and the goal image. We show that this distance fails in two distinct ways. First, it loses directional signal a few steps from the goal, causing distant goals to fail. Second, it weighs the robot arm over the manipulated object, causing manipulation to fail at contact. We measure both failures directly on recorded data by asking whether a lower latent distance corresponds to true progress toward the goal. Across five enviro...

</details>

<details>
<summary>Share</summary>

```
Long-Horizon Planning with Latent World Models via Graph Anchors

Latent world models plan in a compact latent space by predicting the outcomes of actions.

arXiv: https://arxiv.org/abs/2611.34509
Project page: https://syed-nazmus-sakib.github.io/graph-anchors/
Code: https://github.com/syed-nazmus-sakib/graph-anchors

#worldmodels #robotics
```

</details>

---

### [Simulator-as-Proxy World Model for Robot Manipulation](https://arxiv.org/abs/2611.32786)

**Authors:** Tingting Liao, Mingjia Huo, Hao Li, Zhengzhong Liu, Eric P. Xing et al. (6 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★★

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32786) | [PDF](https://arxiv.org/pdf/2611.32786) | [Project Page](https://sim-pwm.pages.dev) | [Code](https://github.com/TingtingLiao/SimPWM)

<details>
<summary>Abstract</summary>

Video world models for robots are increasingly conditioned on a simulated or rendered proxy of the scene, on the assumption that the video will show what the proxy shows. Testing this assumption requires a proxy whose state is explicit and can be perturbed. We present SimPWM (Simulator-as-Proxy World Model): given a calibrated camera, it represents, from the first frame alone, the robot by its 3D model and the objects the gripper may touch as 3D points; a rule-based simulator with no trained parameters moves them under the actions, and a video model renders the result. SimPWM returns the reali...

</details>

<details>
<summary>Share</summary>

```
Simulator-as-Proxy World Model for Robot Manipulation

Video world models for robots are increasingly conditioned on a simulated or rendered proxy of the scene, on the assumption that the video will show what the proxy shows.

arXiv: https://arxiv.org/abs/2611.32786
Project page: https://sim-pwm.pages.dev
Code: https://github.com/TingtingLiao/SimPWM

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

### [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](https://arxiv.org/abs/2611.34693)

**Authors:** Yiren Song, Guian Fang, Mike Zheng Shou

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34693) | [PDF](https://arxiv.org/pdf/2611.34693) | [Code](https://github.com/showlab/ShowNow)

<details>
<summary>Abstract</summary>

Interactive world models must generate video continuously while responding promptly to user actions. Real-time throughput alone leaves input latency unresolved: coarse generation blocks delay action updates, and generation after input adds work to the response path. We introduce ShowNow, a fine-grained speculative streaming framework that uses computation available during playback to prepare action-conditioned futures before input arrives. Single-latent commitment enables frequent decisions, while configurable preparation covers one to eight actions. We construct a matched multi-future dataset...

</details>

<details>
<summary>Share</summary>

```
ShowNow: Fine-Grained Speculative Streaming for Responsive World Models

Interactive world models must generate video continuously while responding promptly to user actions.

arXiv: https://arxiv.org/abs/2611.34693
Code: https://github.com/showlab/ShowNow

#worldmodels #robotics
```

</details>

---

### [Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model](https://arxiv.org/abs/2611.34435)

**Authors:** Zanyi Wang, Xia Chen, Liu Liu, Xianglong Guo, Dengyang Jiang et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34435) | [PDF](https://arxiv.org/pdf/2611.34435) | [Project Page](https://xmz111.github.io/Dianjing/)

<details>
<summary>Abstract</summary>

Modern video generators excel at producing visually plausible futures guided by text and image prompts. Yet their emphasis on semantic plausibility does not guarantee fidelity to the physical consequences of specific actions. Action-conditioned world models (ACWMs), in contrast, aim to simulate how the world responds to robot actions, enabling scalable policy evaluation and improvement without costly real-world rollouts. The challenge is not merely to generate a plausible future, but to predict what follows from a specific physical action. As video priors grow stronger, we ask how little adapt...

</details>

<details>
<summary>Share</summary>

```
Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model

Modern video generators excel at producing visually plausible futures guided by text and image prompts.

arXiv: https://arxiv.org/abs/2611.34435
Project page: https://xmz111.github.io/Dianjing/

#worldmodels #robotics
```

</details>

---

### [SPAR: Self-Referenced World-Model Rewards for Physical Alignment in Video Generation](https://arxiv.org/abs/2611.31958)

**Authors:** Junyi Zhang, Qichao Wang, Wenzhe Qian, Yuanchuan Wang, Min Zhang

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31958) | [PDF](https://arxiv.org/pdf/2611.31958) | [Project Page](https://gavin-jy.github.io/spar-page/)

<details>
<summary>Abstract</summary>

Generating videos with physically plausible dynamics remains challenging despite advances in visual quality. Latent world models offer predictive signals for evaluating physical plausibility, but higher agreement between predicted and observed features may reflect easier-to-predict scene content rather than more plausible dynamics. We propose \textbf{S}elf-Referenced \textbf{P}hysical \textbf{A}lignment \textbf{R}ewards (\textbf{SPAR}), a framework that uses world-model predictions for inference-time physical alignment. SPAR compares each video's prediction error with that of static clips cons...

</details>

<details>
<summary>Share</summary>

```
SPAR: Self-Referenced World-Model Rewards for Physical Alignment in Video Generation

Generating videos with physically plausible dynamics remains challenging despite advances in visual quality.

arXiv: https://arxiv.org/abs/2611.31958
Project page: https://gavin-jy.github.io/spar-page/

#worldmodels #robotics
```

</details>

---

### [Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting](https://arxiv.org/abs/2611.30573)

**Authors:** ZiAn Wang, Tianyi Wang, Zhihao Chen, Manni Cui, Junkai Chen et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus

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

### [Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2611.33993)

**Authors:** Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang, Jianhua Han et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.33993) | [PDF](https://arxiv.org/pdf/2611.33993)

<details>
<summary>Abstract</summary>

Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution. Although future prediction can inform action correction, an accurate forecast does not establish whether modifying an existing action would be beneficial. We present Aegis-VLA, a world-model-guided vision-language-action (VLA) framework that generates predictive action corrections and separately determines whether and how strongly to apply them. A Trajectory World Model combines kinematic extrapolation with learned residual dynamics to predict objec...

</details>

<details>
<summary>Share</summary>

```
Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation

Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution.

arXiv: https://arxiv.org/abs/2611.33993

#worldmodels #robotics
```

</details>

---

### [$μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation](https://arxiv.org/abs/2611.34597)

**Authors:** Devesh Nath, Glen Chou

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34597) | [PDF](https://arxiv.org/pdf/2611.34597) | [Project Page](https://www.deveshnath.com/projects/micrompc/)

<details>
<summary>Abstract</summary>

We present $μ$MPC, a fast model predictive control (MPC) framework that reduces online computation using learned Koopman-linearized dynamics. By precomputing finite-horizon control-to-output maps, $μ$MPC eliminates lifted-state trajectories, yielding an action-only Koopman-Compiled QP (KC-QP) with $Hn_u$ decision variables, independent of lifted dimension. A fixed, precomputed primal operator enables efficient primal-dual iterations using only matrix-vector products and projections, accommodating changing goals and constraints without refactorization. This efficiency also enables control-aware...

</details>

<details>
<summary>Share</summary>

```
$μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation

We present $μ$MPC, a fast model predictive control (MPC) framework that reduces online computation using learned Koopman-linearized dynamics.

arXiv: https://arxiv.org/abs/2611.34597
Project page: https://www.deveshnath.com/projects/micrompc/

#worldmodels #robotics
```

</details>

---

### [DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model](https://arxiv.org/abs/2611.33779)

**Authors:** Zixuan Li, Kangyao Huang, Meng Xu, Wan Tian, Xiaoyu Tang et al. (11 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33779) | [PDF](https://arxiv.org/pdf/2611.33779)

<details>
<summary>Abstract</summary>

Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformations to ground the induced scene motion. We further introduce transform-aware pretraining, which pair...

</details>

<details>
<summary>Share</summary>

```
DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model

Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformati...

arXiv: https://arxiv.org/abs/2611.33779

#worldmodels #robotics
```

</details>

---

### [DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2611.30907)

**Authors:** Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

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

### [WorldUAV: Scaling UAV Data Synthesis via World Models](https://arxiv.org/abs/2611.33682)

**Authors:** Xuewen Liu, Mengjuan Chen, Jing Zhang, Mengzhe Shen, Zekun Xu et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33682) | [PDF](https://arxiv.org/pdf/2611.33682) | [Project Page](https://bienluky.github.io/WorldUAV/)

<details>
<summary>Abstract</summary>

UAV detection and tracking remain constrained by the scarcity of high-quality training data. Existing game-engine-based synthetic UAV data suffer from a substantial synthetic-to-real gap, while the high cost of manually collected real-world UAV data limits dataset scale. Therefore, we introduce WorldUAV, a high-quality UAV dataset constructed through an efficient framework powered by world models. Specifically, WorldUAV directly integrates UAVs into readily available real-world videos, naturally preserving realistic backgrounds, illumination, and scene dynamics. Leveraging the spatiotemporal p...

</details>

<details>
<summary>Share</summary>

```
WorldUAV: Scaling UAV Data Synthesis via World Models

UAV detection and tracking remain constrained by the scarcity of high-quality training data.

arXiv: https://arxiv.org/abs/2611.33682
Project page: https://bienluky.github.io/WorldUAV/

#worldmodels #robotics
```

</details>

---

### [VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors](https://arxiv.org/abs/2611.33591)

**Authors:** Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33591) | [PDF](https://arxiv.org/pdf/2611.33591) | [Project Page](https://research.nvidia.com/labs/sil/projects/vivaworld/)

<details>
<summary>Abstract</summary>

Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D grounding. We introduce \textbf{VivaWorld}, a framework for generating geometry- and view-consistent long videos from an image. We first construct a compositional hybrid 3D representation that combines reconstructed point clouds, which preserve observed scene geometry and appearance, with generated textured meshes, which provide complete object geometry across $360^\circ$ novel views. W...

</details>

<details>
<summary>Share</summary>

```
VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors

Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D ground...

arXiv: https://arxiv.org/abs/2611.33591
Project page: https://research.nvidia.com/labs/sil/projects/vivaworld/

#worldmodels #robotics
```

</details>

---

### [MemAnchorWorld: A Sparse World Model with Horizon-Conditioned Memory Retrieval for Autonomous Driving](https://arxiv.org/abs/2611.32745)

**Authors:** Xinyang Jia, Yuqi Zhang, Jiakai Wang, Yahu Yang, Guandong Pan et al. (7 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32745) | [PDF](https://arxiv.org/pdf/2611.32745) | [Project Page](https://memanchorworld.github.io/)

<details>
<summary>Abstract</summary>

Sparse world models for 4D semantic occupancy forecasting represent scenes with a small set of evolving queries to efficiently predict future geometry and semantics for autonomous driving. However, existing sparse world models face a bottleneck in using historical temporal evidence for long-horizon forecasting. They rely on scene states to carry historical information implicitly, allowing errors to propagate and accumulate across successive forecasting steps and causing geometric and semantic deviations. To address this limitation, we present MemAnchorWorld, a sparse occupancy world model that...

</details>

<details>
<summary>Share</summary>

```
MemAnchorWorld: A Sparse World Model with Horizon-Conditioned Memory Retrieval for Autonomous Driving

Sparse world models for 4D semantic occupancy forecasting represent scenes with a small set of evolving queries to efficiently predict future geometry and semantics for autonomous driving.

arXiv: https://arxiv.org/abs/2611.32745
Project page: https://memanchorworld.github.io/

#worldmodels #robotics
```

</details>

---

### [OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution](https://arxiv.org/abs/2611.32473)

**Authors:** Zhilu Zhang, Xiaoyu Liu, Wenxi Liu, Shengfeng He

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32473) | [PDF](https://arxiv.org/pdf/2611.32473) | [Project Page](https://omnipersist.github.io) | [Code](https://github.com/cszhilu1998/OmniPersist)

<details>
<summary>Abstract</summary>

Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence. When the camera turns away and returns, out-of-view moving entities fail to evolve plausibly in latent space, often mutating or vanishing entirely due to bounded perspective views. To resolve this issue, we propose OmniPersist, a unified framework that couples perspective video generation with panoramic evolution within a single-stage diffusion model, without relying on auxiliary models or initial panoramic inputs. To maintai...

</details>

<details>
<summary>Share</summary>

```
OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution

Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence.

arXiv: https://arxiv.org/abs/2611.32473
Project page: https://omnipersist.github.io
Code: https://github.com/cszhilu1998/OmniPersist

#worldmodels #robotics
```

</details>

---

### [Learning Agent States for Latent Action Modeling](https://arxiv.org/abs/2611.32017)

**Authors:** Shaoan Xie, Fan Feng, Peiyuan Zhu, Peter Spirtes, Kun Zhang

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32017) | [PDF](https://arxiv.org/pdf/2611.32017) | [Project Page](https://agent-state-lam.github.io) | [Code](https://github.com/Mid-Push/Agent-State-LAM)

<details>
<summary>Abstract</summary>

Latent action models (LAMs) learn action-like latents from unlabeled video by coupling frame-pair inference with latent-conditioned prediction, enabling policy and world-model pretraining. However, what the latent must explain depends on the representation space used for action inference and transition prediction. When this space entangles the agent's evolving physical state with visual context, such as background and persistent agent appearance, inferred latents can encode information unrelated to the agent's actions. To address this challenge, we propose Agent-State LAM, which jointly learns...

</details>

<details>
<summary>Share</summary>

```
Learning Agent States for Latent Action Modeling

Latent action models (LAMs) learn action-like latents from unlabeled video by coupling frame-pair inference with latent-conditioned prediction, enabling policy and world-model pretraining.

arXiv: https://arxiv.org/abs/2611.32017
Project page: https://agent-state-lam.github.io
Code: https://github.com/Mid-Push/Agent-State-LAM

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

### [Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models](https://arxiv.org/abs/2611.34739)

**Authors:** Ajmain Istiak Apon, Md Mehedi Hasan, Sejuti Rahman

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34739) | [PDF](https://arxiv.org/pdf/2611.34739)

<details>
<summary>Abstract</summary>

World models are evaluated by predicting future observations from actions. These evaluations assume that actions are prepared the same way as during training, but an unchecked mismatch can make a model appear less accurate than it is. We audit this assumption in Navigation World Models (NWM) and find three interacting differences between its training and rollout code. Correcting the inputs, without retraining, reduces mean visual prediction error by 42%, measured with DreamSim on the RECON navigation dataset. The correction also changes the ranking of NWM checkpoints in an exploratory analysis...

</details>

<details>
<summary>Share</summary>

```
Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models

World models are evaluated by predicting future observations from actions.

arXiv: https://arxiv.org/abs/2611.34739

#worldmodels #robotics
```

</details>

---

### [Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics](https://arxiv.org/abs/2611.34644)

**Authors:** Chengzhi Zhao, Juelin Li, Zhennan Wang, Sheng Wang, Zhuoman Liu et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34644) | [PDF](https://arxiv.org/pdf/2611.34644) | [Project Page](https://xyz1206.github.io/MotionRep/)

<details>
<summary>Abstract</summary>

Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation. We present MotionRep, a visual representation world model that jointly generates future DINO representations and 3D object flow, coupling semantic and geometric information with object-centric dynamics. To make high-dimensional DINO features amenable to generative modeling, we introduce DINO-VAE, which combines temporal and channel compression with latent regularization to produce compact latent...

</details>

<details>
<summary>Share</summary>

```
Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics

Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation.

arXiv: https://arxiv.org/abs/2611.34644
Project page: https://xyz1206.github.io/MotionRep/

#worldmodels #robotics
```

</details>

---

### [Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics](https://arxiv.org/abs/2611.34302)

**Authors:** Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34302) | [PDF](https://arxiv.org/pdf/2611.34302)

<details>
<summary>Abstract</summary>

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning. Existing methods, however, either retarget human-specific geometry or match only static visual goals, and thus stumble over the cross-embodiment dynamics mismatch and the ungrounded action execution. We present the Co-World Model (CoWM), a predictive framework jointly optimized from paired yet unsynchronized human and robot streams. To bridge the cross-embodiment dynamics gap, CoWM di...

</details>

<details>
<summary>Share</summary>

```
Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning.

arXiv: https://arxiv.org/abs/2611.34302

#worldmodels #robotics
```

</details>

---

### [Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models](https://arxiv.org/abs/2611.34288)

**Authors:** Guangyu Liu, Hanzhang Wang, Huijia Zhang, Hanbei Zhan, Linjie Hu et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34288) | [PDF](https://arxiv.org/pdf/2611.34288)

<details>
<summary>Abstract</summary>

Embodied world models aim to predict future interactions that are both visually realistic and physically consistent. Yet explicit 3D motion prediction alone does not guarantee that object structure and contact relationships are preserved. Beyond motion prediction, 3D representations provide an explicit state space for imposing structural and physical constraints. Building on this insight, we introduce RehearsalWorld, an editable robot world model driven by 3D Interaction Rehearsal (3DIR). Given an initial RGB-D observation and robot actions, Interaction-Consistent Rehearsal (ICR) uses a pretra...

</details>

<details>
<summary>Share</summary>

```
Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models

Embodied world models aim to predict future interactions that are both visually realistic and physically consistent.

arXiv: https://arxiv.org/abs/2611.34288

#worldmodels #robotics
```

</details>

---

### [WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](https://arxiv.org/abs/2611.34130)

**Authors:** Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang, Jinan Zhang, Linchao Zhu

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34130) | [PDF](https://arxiv.org/pdf/2611.34130)

<details>
<summary>Abstract</summary>

World models are increasingly used in robotics to improve the performance of embodied models. Compared with general-purpose video generation, robotics places more stringent requirements on world models. Generated videos must satisfy fine-grained physical constraints on robot motion and object interactions. However, existing world model benchmarks can overlook robotics specific physical details and struggle to assess them accurately. To address this problem, we introduce WorldPhy, a world model benchmark for accurate, fine-grained evaluation of physical plausibility in robotics. Our benchmark c...

</details>

<details>
<summary>Share</summary>

```
WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics

World models are increasingly used in robotics to improve the performance of embodied models.

arXiv: https://arxiv.org/abs/2611.34130

#worldmodels #robotics
```

</details>

---

### [Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](https://arxiv.org/abs/2611.33925)

**Authors:** Zhiyue Zhao, Mingyu Liu, Bolin Zhang, Liyang Li, Guangyu Huang et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33925) | [PDF](https://arxiv.org/pdf/2611.33925)

<details>
<summary>Abstract</summary>

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, their predictions break down. Across five pretrained action-conditioned models, object-motion error is at most 10.4% lower than that of a static baseline that copies the first frame, and two models are worse than this baseline. We present WorldReforge, which teaches world models what happens when manipulation goes wrong. We construct the Reforge dataset o...

</details>

<details>
<summary>Share</summary>

```
Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations.

arXiv: https://arxiv.org/abs/2611.33925

#worldmodels #robotics
```

</details>

---

### [RoboProbe: Benchmarking Physical Plausibility of Robot World Models](https://arxiv.org/abs/2611.32152)

**Authors:** Zhuoying Yang, Jiachen Ni, Yichen Guo, Xiaoshan Wu, Mengyu Wang

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.32152) | [PDF](https://arxiv.org/pdf/2611.32152)

<details>
<summary>Abstract</summary>

Evaluating the physical plausibility of generated videos is critical for reliable robotic planning with world models. These videos inform action proposal and assessment before real-world execution, so undetected physical violations can lead to erroneous assessments of action feasibility and safety. Yet current video generators often produce physically implausible interactions. Detecting such violations directly with vision-language models (VLMs) remains challenging as physical verification requires evidence-grounded spatiotemporal reasoning beyond high-level semantic understanding. We develop...

</details>

<details>
<summary>Share</summary>

```
RoboProbe: Benchmarking Physical Plausibility of Robot World Models

Evaluating the physical plausibility of generated videos is critical for reliable robotic planning with world models.

arXiv: https://arxiv.org/abs/2611.32152

#worldmodels #robotics
```

</details>

---

### [EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution](https://arxiv.org/abs/2611.30004)

**Authors:** Zehao Liu, Huashuo Lei, Xi Lin, Haoang Li, Yuliang Chen et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CR, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

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

### [Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models](https://arxiv.org/abs/2611.34830)

**Authors:** Simon Baur, Wojciech Samek, Jackie Ma

**Published:** 2026-11-25 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34830) | [PDF](https://arxiv.org/pdf/2611.34830)

<details>
<summary>Abstract</summary>

World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as the model's predictive capabilities, and predictions in turn are only reliable within the model's experience. Epistemic uncertainty (EU) is the signal that marks where that experience ends. In this work we offer an extensive empirical study on how training objectives and architectures shape epistemic uncertainty of world models. More precisely, we present a controlled comparison of post-hoc EU (las...

</details>

<details>
<summary>Share</summary>

```
Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models

World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution.

arXiv: https://arxiv.org/abs/2611.34830

#worldmodels #robotics
```

</details>

---

### [WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation](https://arxiv.org/abs/2611.33745)

**Authors:** Xu Yang, Kailai Sun, Qianchuan Zhao

**Published:** 2026-11-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33745) | [PDF](https://arxiv.org/pdf/2611.33745)

<details>
<summary>Abstract</summary>

World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation. Factual transitions alone determine action-wise marginal futures and average effects, but not individual effects or the probability that switching actions causes harm. We introduce WhatIf, a counterfactual world model for manipulation that couples candidate futures through shared latent physics and transition noise inferred from factual history. Each candidate action induces a sparse object-factor causal graph describing the physical pathways it acti...

</details>

<details>
<summary>Share</summary>

```
WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation

World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation.

arXiv: https://arxiv.org/abs/2611.33745

#worldmodels #robotics
```

</details>

---

### [SceneMemBench: A Benchmark for Scene Memory in Interactive Video World Models](https://arxiv.org/abs/2611.31803)

**Authors:** Yuheng Si, Linye Lyu, Jiawei Zhou, Lingyi Du, Nanfei Ye et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31803) | [PDF](https://arxiv.org/pdf/2611.31803) | [Project Page](https://yuheng-si.github.io/SceneMemBench/)

<details>
<summary>Abstract</summary>

Interactive video world models generate navigable worlds frame by frame, but a persistent world requires previously observed scenes to remain recoverable as users move away and return. Existing memory evaluations, however, often focus on seen-view revisits and full rollouts, leaving cross-view scene recovery underexplored while entangling memory with trajectory-following errors and accumulated generation degradation. We introduce SceneMemBench, a benchmark for scene memory in interactive video world models. It evaluates two complementary dimensions: seen-view recall versus novel-view recovery,...

</details>

<details>
<summary>Share</summary>

```
SceneMemBench: A Benchmark for Scene Memory in Interactive Video World Models

Interactive video world models generate navigable worlds frame by frame, but a persistent world requires previously observed scenes to remain recoverable as users move away and return.

arXiv: https://arxiv.org/abs/2611.31803
Project page: https://yuheng-si.github.io/SceneMemBench/

#worldmodels #robotics
```

</details>

---

### [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](https://arxiv.org/abs/2611.30714)

**Authors:** Yuxuan Jiang, Zehua Chen, Yusheng Dai, Andong Wang, Weibei Dou et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.SD, cs.CV, cs.MM | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page

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

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

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

### [Can Visual World Models See Force?](https://arxiv.org/abs/2611.34422)

**Authors:** Felix Tristram, Benjamin D. Killeen, Nassir Navab

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.34422) | [PDF](https://arxiv.org/pdf/2611.34422)

<details>
<summary>Abstract</summary>

World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation. They predict how scenes evolve and which actions to take, yet successful manipulation depends not solely on following observable trajectories but also on the hidden variable of interaction force. Neurophysiology has shown that humans possess a visual prior for this hidden variable, motivating us to ask the question: Do the representations of visual foundation models also capture the forces involved in an interaction? We define force awareness as the ability of representations...

</details>

<details>
<summary>Share</summary>

```
Can Visual World Models See Force?

World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation.

arXiv: https://arxiv.org/abs/2611.34422

#worldmodels #robotics
```

</details>

---

### [CARE-WM: Same-Horizon Self-Conditioning with Constraint-Adaptive Regularization for Latent World Models](https://arxiv.org/abs/2611.34054)

**Authors:** Yuchen Lin, Kai Zhao

**Published:** 2026-11-25 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34054) | [PDF](https://arxiv.org/pdf/2611.34054)

<details>
<summary>Abstract</summary>

Planning with latent world models requires both accurate multi-step predictions and latent distances that reflect physical proximity to the goal. However, models are typically trained on ground-truth observations but must rely on their own imaginations during planning, while closer latent distances do not necessarily correspond to better task outcomes. Existing methods resort to auxiliary training objectives or additional task-cost readouts, which respectively incur extra training overhead or leave the latent geometry itself misaligned with task cost. We introduce CARE-WM, a drop-in training m...

</details>

<details>
<summary>Share</summary>

```
CARE-WM: Same-Horizon Self-Conditioning with Constraint-Adaptive Regularization for Latent World Models

Planning with latent world models requires both accurate multi-step predictions and latent distances that reflect physical proximity to the goal.

arXiv: https://arxiv.org/abs/2611.34054

#worldmodels #robotics
```

</details>

---

### [DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation](https://arxiv.org/abs/2611.32654)

**Authors:** Hongjia Liu, Dacheng Zhou, Minghao Fu, Chuanjun Guo, Tianze Wang et al. (8 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.32654) | [PDF](https://arxiv.org/pdf/2611.32654)

<details>
<summary>Abstract</summary>

Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success. Recent world-action models (WAMs) extend vision-language-action (VLA) models with the first signal by jointly predicting actions and future observations, yet this predictive ability serves only as an auxiliary loss for policy learning. Meanwhile, most policy improvement methods learn dynamics and values in separate models, increasing training overhead and limiting representation sharing between these complementary objectives. We introduce DexWAC,...

</details>

<details>
<summary>Share</summary>

```
DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation

Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success.

arXiv: https://arxiv.org/abs/2611.32654

#worldmodels #robotics
```

</details>

---

### [Disentangling Visual Dynamics for World Model Planning](https://arxiv.org/abs/2611.32228)

**Authors:** Yuhong Shi, Yihan Guo, Jie Wei, Jianyi Liu, Jingwen Fu

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.32228) | [PDF](https://arxiv.org/pdf/2611.32228)

<details>
<summary>Abstract</summary>

Visual world models enable planning through predictive latent states. However, entangled agent and exogenous dynamics can obscure task progress. Disentangling visual dynamics for planning requires addressing two challenges: 1) suppressing cross-factor interference while retaining useful information; and 2) linking factors to task-relevant signals, since stability alone does not ensure meaningful planning distances. Therefore, we introduce FactorWorld, a disentangled visual dynamics framework for world model planning. To separate agent and exogenous dynamics, we propose a Counterfactual Consens...

</details>

<details>
<summary>Share</summary>

```
Disentangling Visual Dynamics for World Model Planning

Visual world models enable planning through predictive latent states.

arXiv: https://arxiv.org/abs/2611.32228

#worldmodels #robotics
```

</details>

---

### [VeriTouch: Verified Visuo-Tactile World Models that Improve Robot Policy Learning](https://arxiv.org/abs/2611.30572)

**Authors:** Shuxun Wang, Xiaonan Jiang, Zhaoyu Wang, Ziyuan Chu, Xihang Yue et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

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

**Published:** 2026-11-23 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

### [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](https://arxiv.org/abs/2611.34730)

**Authors:** Ahmed Hatem, Caoliwen Wang, Robert Hoang, Siyuan Chen, Spencer Szabados et al. (12 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34730) | [PDF](https://arxiv.org/pdf/2611.34730)

<details>
<summary>Abstract</summary>

Video world models aim to create interactive physical worlds that capture how diverse materials move and interact. Yet material-dependent dynamics remain underexplored in controllable video generation, limiting reliable control in scenes with different materials. We present WorldInteract, a streaming video generation framework that decomposes cross-material interaction into material-dependent behavior generation and contact response computation. External pushes and contact impulses are expressed through a shared velocity-increment interface, allowing material behaviors learned from interaction...

</details>

<details>
<summary>Share</summary>

```
WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions

Video world models aim to create interactive physical worlds that capture how diverse materials move and interact.

arXiv: https://arxiv.org/abs/2611.34730

#worldmodels #robotics
```

</details>

---

### [Do We Still Need Reinforcement Learning When We Can Read the World Model?](https://arxiv.org/abs/2611.34656)

**Authors:** Mingchao Zhang, Miduo Cui, Kangze He, Yuanjun Li, Dapeng Li et al. (13 authors)

**Published:** 2026-11-25 | **Categories:** cs.LG, cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34656) | [PDF](https://arxiv.org/pdf/2611.34656)

<details>
<summary>Abstract</summary>

Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding agents directly synthesize control policies by reasoning over readable world models. By examining environment source code, these agents translate environmental knowledge into execut...

</details>

<details>
<summary>Share</summary>

```
Do We Still Need Reinforcement Learning When We Can Read the World Model?

Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience.

arXiv: https://arxiv.org/abs/2611.34656

#worldmodels #robotics
```

</details>

---

### [Normalizing Flows are Capable World Models](https://arxiv.org/abs/2611.33872)

**Authors:** Zijia Li, Yong-Hyun Park, Shusheng Yang, Jiatao Gu

**Published:** 2026-11-25 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33872) | [PDF](https://arxiv.org/pdf/2611.33872)

<details>
<summary>Abstract</summary>

A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encoder is invertible, the predicted distribution over latent states defines a distribution over future observations. Maximizing the exact conditional likelihood of those observations therefore trains the representation and dynamics jointly. An agent can plan directly in the learned latent space and decode sampled trajector...

</details>

<details>
<summary>Share</summary>

```
Normalizing Flows are Capable World Models

A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions.

arXiv: https://arxiv.org/abs/2611.33872

#worldmodels #robotics
```

</details>

---

### [Improving Building Energy Efficiency with an Indoor Environmental World Model and Counterfactual Adaptive Learning](https://arxiv.org/abs/2611.33764)

**Authors:** Xu Yang, Kailai Sun, Dianyu Zhong, Irfan Qaisar, Yu Yang et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33764) | [PDF](https://arxiv.org/pdf/2611.33764)

<details>
<summary>Abstract</summary>

Optimizing indoor climate systems plays a critical role in achieving the United Nations' Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing reinforcement learning (RL) methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors during long-horizon rollouts. Thus, we propose a novel occupant-centric indoor climate control framework. It develops indoor environmental world models to predict future physical thermal baselines and dynamic occup...

</details>

<details>
<summary>Share</summary>

```
Improving Building Energy Efficiency with an Indoor Environmental World Model and Counterfactual Adaptive Learning

Optimizing indoor climate systems plays a critical role in achieving the United Nations' Sustainable Development Goals 11 and 13.

arXiv: https://arxiv.org/abs/2611.33764

#worldmodels #robotics
```

</details>

---

### [DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.33734)

**Authors:** Lifan Jiang, Yifan Huang, Jixuan Zhang, Peifeng Wang, Yuying Ma et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33734) | [PDF](https://arxiv.org/pdf/2611.33734)

<details>
<summary>Abstract</summary>

Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories. However, capturing synchronized camera trajectories often requires game-specific pipelines, limiting scalability. We therefore propose GameWeaver, a unified diffusion framework that automatically produces paired video--camera data through three complementary tasks: camera pose estimation from observed video, video generation along a prescribed camera trajectory, and joint video--camera generation from a reference image and text. First, each...

</details>

<details>
<summary>Share</summary>

```
DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation

Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories.

arXiv: https://arxiv.org/abs/2611.33734

#worldmodels #robotics
```

</details>

---

### [GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting](https://arxiv.org/abs/2611.33693)

**Authors:** Shijun Guo, Yaming Yang, Haoran Xu, Wei Zhao, Ziyu Guan et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33693) | [PDF](https://arxiv.org/pdf/2611.33693)

<details>
<summary>Abstract</summary>

4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models. Semantic occupancy abstracts image color and texture into discrete labels, leaving 3D voxel arrangements as the primary cues for distinguishing local shapes within each class. Existing methods borrow image-encoding frameworks to obtain compact latent representations through height channelization or plane factorization, but do not sufficiently model within-column height patterns and cross-column relations jointly before compression, weakening these geometri...

</details>

<details>
<summary>Share</summary>

```
GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting

4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models.

arXiv: https://arxiv.org/abs/2611.33693

#worldmodels #robotics
```

</details>

---

### [Do Occupancy World Models Really Follow Actions?](https://arxiv.org/abs/2611.32029)

**Authors:** Jongseong Bae, Ha Young Kim

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.32029) | [PDF](https://arxiv.org/pdf/2611.32029)

<details>
<summary>Abstract</summary>

Occupancy world models predict future 3D scenes conditioned on ego actions, yet their predictions may not faithfully follow the specified trajectory under counterfactual actions. Because driving datasets provide sparse coverage of alternative trajectories for each scene, existing models learn the spatial effect of ego motion implicitly from observed scene--trajectory combinations, which may entangle action effects with scene--trajectory correlations. We propose ReCast, an ego-trajectory-guided transformer that grounds future prediction in action-induced geometric correspondence across ego-cent...

</details>

<details>
<summary>Share</summary>

```
Do Occupancy World Models Really Follow Actions?

Occupancy world models predict future 3D scenes conditioned on ego actions, yet their predictions may not faithfully follow the specified trajectory under counterfactual actions.

arXiv: https://arxiv.org/abs/2611.32029

#worldmodels #robotics
```

</details>

---

### [Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning](https://arxiv.org/abs/2611.30666)

**Authors:** Yu Zhang, Jingrui Li, Congyu Wang, Yuhang Cheng, Wenbo Chen et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

### [A Simple Yet Effective Agent for Open-World Aerial Object Search](https://arxiv.org/abs/2611.34115)

**Authors:** Jitai Hao, Liangxing Yang, Zhenyang Li, Fan Liu, Qiang Huang et al. (6 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34115) | [PDF](https://arxiv.org/pdf/2611.34115)

<details>
<summary>Abstract</summary>

Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how far a minimal, training-free design can go, we introduce SimpleUAV, an agent built around a frozen, off-the-shelf vision-language model (VLM). SimpleUAV separates current-view target assessment from history-conditioned action selection, combining fresh candidate evidence with lightweight search context. Local geometry converts visual selections into bounded straight-line movements, depth-based checks halt blocked segments, and measured execution...

</details>

<details>
<summary>Share</summary>

```
A Simple Yet Effective Agent for Open-World Aerial Object Search

Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training.

arXiv: https://arxiv.org/abs/2611.34115

#worldmodels #robotics
```

</details>

---

### [iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction](https://arxiv.org/abs/2611.33141)

**Authors:** Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman, Max Simchowitz, Aviral Kumar

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.33141) | [PDF](https://arxiv.org/pdf/2611.33141)

<details>
<summary>Abstract</summary>

World-action models (WAMs) build policies on pretrained video-generation models, on the premise that predicting how a scene evolves helps determine how to act. However, generating future scenes is expensive for real-time control. This motivates efficient proxies for future imagination, but how to train such proxies without sacrificing action-prediction quality remains unclear. An effective proxy need not generate a high-resolution frame; it only needs to provide enough information to distinguish between possible futures. This leads to the design principle behind iWAM: rather than denoising an...

</details>

<details>
<summary>Share</summary>

```
iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction

World-action models (WAMs) build policies on pretrained video-generation models, on the premise that predicting how a scene evolves helps determine how to act.

arXiv: https://arxiv.org/abs/2611.33141

#worldmodels #robotics
```

</details>

---

### [DynaMimic: A Physics-Informed World Model for Humanoid Motion Tracking](https://arxiv.org/abs/2611.32944)

**Authors:** Chaoyue Xing, Linyi Huang, Yiting He, Yixuan Yin, Siqi Hou et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.32944) | [PDF](https://arxiv.org/pdf/2611.32944)

<details>
<summary>Abstract</summary>

Whole-body motion tracking enables humanoid robots to reproduce diverse skills from human demonstrations. Existing model-free reinforcement learning methods either distill motion specialists into a single policy at the cost of performance or train a generalist policy directly using cluster-scale computation. SuperMimic reduces this computational cost through a differentiable world model that implicitly learns the physics shared across motions by predicting the next state from the current state and action. However, this implicit formulation may not fully capture the underlying physical processe...

</details>

<details>
<summary>Share</summary>

```
DynaMimic: A Physics-Informed World Model for Humanoid Motion Tracking

Whole-body motion tracking enables humanoid robots to reproduce diverse skills from human demonstrations.

arXiv: https://arxiv.org/abs/2611.32944

#worldmodels #robotics
```

</details>

---

### [CodeWAM: A Code World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.32483)

**Authors:** Zhisheng Chen, Jinpeng Wang, Beicheng Lou, Zhengwei Xie, Hao Wu et al. (8 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.32483) | [PDF](https://arxiv.org/pdf/2611.32483)

<details>
<summary>Abstract</summary>

Driving world models anticipate action consequences through representations of how the world evolves. For autonomous driving, these representations must capture both the surrounding scene and the ego vehicle's motion under a candidate plan. We propose CodeWAM, a driving world model that incorporates executable code as part of its world representation. Code represents ego dynamics by expressing how the vehicle state evolves under plan execution, while a learned visual model captures scene-dependent consequences. Executing the code produces a candidate-conditioned motion sequence, which is evalu...

</details>

<details>
<summary>Share</summary>

```
CodeWAM: A Code World Action Model for End-to-End Autonomous Driving

Driving world models anticipate action consequences through representations of how the world evolves.

arXiv: https://arxiv.org/abs/2611.32483

#worldmodels #robotics
```

</details>

---

### [Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?](https://arxiv.org/abs/2611.30836)

**Authors:** Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang, Shou-Po Tsai, Jing-Zhe Huang et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus

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

### [CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching](https://arxiv.org/abs/2611.33939)

**Authors:** Shizhuang Wang, Tianhao Wang, Xingqun Zhan

**Published:** 2026-11-25 | **Categories:** cs.LG, stat.ML | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33939) | [PDF](https://arxiv.org/pdf/2611.33939)

<details>
<summary>Abstract</summary>

Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems. The errors of such systems often vary with factors such as input quality and operating conditions, and thus cannot be accurately described by a single Gaussian model. Although Gaussian mixture models and calibrated quantiles can approximate such error distributions, their unconditional forms do not capture how the error behavior depends on these factors. Hence, we propose condUQ, an approach...

</details>

<details>
<summary>Share</summary>

```
CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching

Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems.

arXiv: https://arxiv.org/abs/2611.33939

#worldmodels #robotics
```

</details>

---

### [Motion Conditioned World Modeling for Embodied Visual Tracking](https://arxiv.org/abs/2611.32900)

**Authors:** Jiahao Zhang, Xuan Yao, Junyu Gao, Changsheng Xu

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.32900) | [PDF](https://arxiv.org/pdf/2611.32900)

<details>
<summary>Abstract</summary>

World models support embodied decision-making by predicting future environment states. In embodied visual tracking, uncertain target motion and robot-induced viewpoint changes jointly affect visual observations, making future-state prediction challenging. We propose Motion-Conditioned World Modeling, which incorporates predicted target-motion distributions and robot ego-motion into latent state transitions. A Geometry--Progress module jointly models geometric paths and single-step travel distances through shared motion modes and path-conditioned progress distributions. This formulation capture...

</details>

<details>
<summary>Share</summary>

```
Motion Conditioned World Modeling for Embodied Visual Tracking

World models support embodied decision-making by predicting future environment states.

arXiv: https://arxiv.org/abs/2611.32900

#worldmodels #robotics
```

</details>

---

### [Interactive Neural Computers](https://arxiv.org/abs/2611.32811)

**Authors:** Ross Murphy, Marcel Hedman, Gabriel Brostow

**Published:** 2026-11-24 | **Categories:** cs.AI, cs.NE, cs.SC | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.32811) | [PDF](https://arxiv.org/pdf/2611.32811)

<details>
<summary>Abstract</summary>

Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents. This is limiting when someone needs a different workflow, or an interface suited to hands-free use or a disability. We explore an overlooked alternative. Rather than training an agent to operate an existing computer, we train a generative model to be the computer, predicting each next screen from past screens and the user's mouse and keyboard actions. Treating a desktop as an interactive world model raises problems that natural-video world...

</details>

<details>
<summary>Share</summary>

```
Interactive Neural Computers

Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents.

arXiv: https://arxiv.org/abs/2611.32811

#worldmodels #robotics
```

</details>

---

### [Learning World Models through Contrastive Identification of Actions](https://arxiv.org/abs/2611.32776)

**Authors:** Hayeong Lee, Youngjun Suh, Byung-Jun Lee

**Published:** 2026-11-24 (updated 2026-11-25) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.32776) | [PDF](https://arxiv.org/pdf/2611.32776)

<details>
<summary>Abstract</summary>

Latent world models enable goal-directed planning from offline visual data, but prediction alone does not specify which action-related distinctions their representations should preserve. Inverse dynamics provides auxiliary supervision, yet squared-error action regression rewards additional information only through changes in the conditional action mean. We propose Contrastive Identification of Actions (CIA), which identifies the executed action among alternatives sampled from a history-conditioned behavior proposal. Comparing actions plausible in the same context targets information supplied b...

</details>

<details>
<summary>Share</summary>

```
Learning World Models through Contrastive Identification of Actions

Latent world models enable goal-directed planning from offline visual data, but prediction alone does not specify which action-related distinctions their representations should preserve.

arXiv: https://arxiv.org/abs/2611.32776

#worldmodels #robotics
```

</details>

---

### [Economic World Model](https://arxiv.org/abs/2611.32663)

**Authors:** Qirui Mi, Yujia Ming, Bo Li, Haifeng Zhang

**Published:** 2026-11-24 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.32663) | [PDF](https://arxiv.org/pdf/2611.32663)

<details>
<summary>Abstract</summary>

Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an economic system works, enabling counterfactual simulation and decision-making under resource constraints. We then propose a general framework for studying EWMs that links three tasks: simulating agent behaviour, learning economic transitions and systematically evaluating the dynamics. As an initial implementation, we learn...

</details>

<details>
<summary>Share</summary>

```
Economic World Model

Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions?

arXiv: https://arxiv.org/abs/2611.32663

#worldmodels #robotics
```

</details>

---

### [CriticJEPA: World Models Are Better Critics Than Optimizers](https://arxiv.org/abs/2611.32357)

**Authors:** Xvyuan Liu, Jianjie Fang, Honglin Zhang, Zhaolu Wang, Xin Zhang et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.32357) | [PDF](https://arxiv.org/pdf/2611.32357)

<details>
<summary>Abstract</summary>

Visual world models enable goal-directed planning by predicting action outcomes. Gradient-based planners optimize actions to lower predicted goal cost, but continued optimization can exploit prediction errors after execution stops improving. Comparing plans requires informative relative scores; improving them also requires reliable update directions. Exact-state execution reveals that a frozen hierarchical world model ranks goal-conditioned proposals even when its rankings among outputs of prolonged gradient search are uninformative. Effective planning pairs goal-directed candidates with predi...

</details>

<details>
<summary>Share</summary>

```
CriticJEPA: World Models Are Better Critics Than Optimizers

Visual world models enable goal-directed planning by predicting action outcomes.

arXiv: https://arxiv.org/abs/2611.32357

#worldmodels #robotics
```

</details>

---

### [PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models](https://arxiv.org/abs/2611.32113)

**Authors:** Yicheng Huang, Feng Ke, Linhan Chen, Ziyi Jiang, Xiu Yin Zhang

**Published:** 2026-11-24 | **Categories:** cs.LG, cs.CV, eess.SP | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.32113) | [PDF](https://arxiv.org/pdf/2611.32113)

<details>
<summary>Abstract</summary>

Adapting Large Language Models (LLMs) to millimeter-wave (mmWave) radar enables privacy-preserving, all-weather physical scene understanding across darkness, smoke, and walls. However, standard instruction tuning treats continuous radar streams as static text-like tokens, causing near-random global radar-to-text retrieval and severe physical drift under sensor blackouts. Conversely, coupling pairwise contrastive losses (e.g., SigLIP) directly into the shared backbone improves retrieval but injects $O(B^2)$ repulsive gradients that fracture continuous coordinate manifolds ($R^2 < 0$). We presen...

</details>

<details>
<summary>Share</summary>

```
PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models

Adapting Large Language Models (LLMs) to millimeter-wave (mmWave) radar enables privacy-preserving, all-weather physical scene understanding across darkness, smoke, and walls.

arXiv: https://arxiv.org/abs/2611.32113

#worldmodels #robotics
```

</details>

---

### [ADE: A Zero-Training Unlearning Method for Latent World Models](https://arxiv.org/abs/2611.31998)

**Authors:** Sirui He, Chi Zhang

**Published:** 2026-11-24 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.31998) | [PDF](https://arxiv.org/pdf/2611.31998)

<details>
<summary>Abstract</summary>

Latent world models learn compact recurrent dynamics from offline trajectories, yet deployed simulators can retain backdoor triggers or stale transitions from outdated physical regimes. Existing unlearning methods fail in autoregressive physics: gradient updates distort latent manifolds and compound rollout drift, naive output zeroing suppresses valid control responses on trigger onset, and single-step deletion leaves corruption inside recurrent hidden states. We propose Analytical Dynamics Excision (ADE), a deterministic, zero-training closed-form unlearning algorithm for latent world models....

</details>

<details>
<summary>Share</summary>

```
ADE: A Zero-Training Unlearning Method for Latent World Models

Latent world models learn compact recurrent dynamics from offline trajectories, yet deployed simulators can retain backdoor triggers or stale transitions from outdated physical regimes.

arXiv: https://arxiv.org/abs/2611.31998

#worldmodels #robotics
```

</details>

---

### [ReJEPA: Bounded Predictive Regulation for Latent World Models](https://arxiv.org/abs/2611.31910)

**Authors:** Fangzhou Lin, Yuping Wang, Shuo Xing, Yang Chen, Yuwen Heng et al. (10 authors)

**Published:** 2026-11-24 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.31910) | [PDF](https://arxiv.org/pdf/2611.31910)

<details>
<summary>Abstract</summary>

Latent world models learn representations by predicting future states in an abstract embedding space rather than reconstructing raw pixels. When training across multi-frame sequences, however, not all frames and spatial regions are equally informative or predictable. We argue that forcing a world model to minimize every prediction error may be unnecessary and harmful. Under standard $L_2$ loss, unbounded gradients force the encoder and predictor to overfit noisy or transient frames at the expense of core physical structure, while amplifying gradient conflict with representation regularizers. C...

</details>

<details>
<summary>Share</summary>

```
ReJEPA: Bounded Predictive Regulation for Latent World Models

Latent world models learn representations by predicting future states in an abstract embedding space rather than reconstructing raw pixels.

arXiv: https://arxiv.org/abs/2611.31910

#worldmodels #robotics
```

</details>

---

### [Gaze World Model](https://arxiv.org/abs/2611.31836)

**Authors:** Jiawen Zhang, Houze Yang, Xu Cao, Yifan Shen, Zhongyi Zhou et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.31836) | [PDF](https://arxiv.org/pdf/2611.31836)

<details>
<summary>Abstract</summary>

Where a person looks indicates their focus of attention, and how their gaze shifts between targets reveals how that attention responds to a changing scene. Existing gaze target estimation methods largely operate frame by frame and do not model these shifts. Gaze shifts are often driven by dynamic changes in the scene, which is the kind of information world models are designed to encode. This relationship is subtle, however, since an event far across the frame may produce only a slight movement of the person's head or eyes. We therefore introduce the Gaze World Model (GWM), which co-trains late...

</details>

<details>
<summary>Share</summary>

```
Gaze World Model

Where a person looks indicates their focus of attention, and how their gaze shifts between targets reveals how that attention responds to a changing scene.

arXiv: https://arxiv.org/abs/2611.31836

#worldmodels #robotics
```

</details>

---

### [SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042)

**Authors:** Jenna Kang, Bingxuan Li, Colin Groth, Anatolii Evdokimov, Sai Zhang et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "world model" in title

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

**Why surfaced:** "world model" in title

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

### [SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467)

**Authors:** Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.33467) | [PDF](https://arxiv.org/pdf/2611.33467)

<details>
<summary>Abstract</summary>

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We present SplatWAM (Splatting World Action Model), a generative world model that learns action-conditioned dynamics directly over compact 3D Gaussian primitives. A tokenizer SplatWAM-T first encodes a variable number of unposed views into a fixed budget of Gaussian tokens. A dynamics model SplatWAM-D then predicts future Gaussian states in a single forward pass per action, using log-Euclidean covariance coordinates and differentiable rendering supe...

</details>

<details>
<summary>Share</summary>

```
SplatWAM: Splatting World Action Models for Real-Time 3D Imagination

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution.

arXiv: https://arxiv.org/abs/2611.33467

#worldmodels #robotics
```

</details>

---

### [Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty](https://arxiv.org/abs/2611.31843)

**Authors:** Yonglong Zhang

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.31843) | [PDF](https://arxiv.org/pdf/2611.31843)

<details>
<summary>Abstract</summary>

Reactive robotic manipulation is acutely sensitive to simultaneous sensing noise, measurement dropouts, joint execution errors, and contact parameter variations. While single-frame frameworks like Domain-Randomized Instance Set (DRIS) achieve strong robustness under isolated uncertainties (86.4%), they degrade severely when perception and actuation uncertainties co-occur (27.6% across 10 coupled stress scenarios) due to memoryless encoding and fixed high-stiffness PD control. We propose Co-DRIS + SuperMimic, a perception-action co-design framework coupling: (i) an inertial world-frame physics-...

</details>

<details>
<summary>Share</summary>

```
Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty

Reactive robotic manipulation is acutely sensitive to simultaneous sensing noise, measurement dropouts, joint execution errors, and contact parameter variations.

arXiv: https://arxiv.org/abs/2611.31843

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

### [DreamTour: Layout Steering for Training-Free World Exploration](https://arxiv.org/abs/2611.33378)

**Authors:** Srikumar Sastry, Meher Gitika Karumuri, Chenqi Li, Sarosij Bose, Mellon Zhang et al. (10 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.33378) | [PDF](https://arxiv.org/pdf/2611.33378)

<details>
<summary>Abstract</summary>

Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance. We present DreamTour, a training-free framework that generates camera tours from a single image with more accurate control over camera motion. DreamTour first uses a frozen image inpainting prior to extend the photograph beyond its original field of view while preserving the input pixels. Depth-based rendering of this extended scene along the requested camera path produces approximate target views that serve as spatial guidance. We introduce Layout Steering,...

</details>

<details>
<summary>Share</summary>

```
DreamTour: Layout Steering for Training-Free World Exploration

Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance.

arXiv: https://arxiv.org/abs/2611.33378

#worldmodels #robotics
```

</details>

---

### [Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035)

**Authors:** Sabrine Aroua, Osama Arouk, Pegah Alizadeh

**Published:** 2026-11-24 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.33035) | [PDF](https://arxiv.org/pdf/2611.33035)

<details>
<summary>Abstract</summary>

AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles. This survey introduces a technique-agnostic taxonomy of RAN decision-making organized around four complementary capabilities: Representation and Reasoning, Prediction and Simulation, Adaptive Control, and Decision Synthesis. These capabilities are defined by their roles in the control process, independently of the tec...

</details>

<details>
<summary>Share</summary>

```
Hybrid AI for AI-Native RAN Control: A Functional Perspective

AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales.

arXiv: https://arxiv.org/abs/2611.33035

#worldmodels #robotics
```

</details>

---

### [EEG-World: Context-Conditioned Dynamics of the Watching Brain](https://arxiv.org/abs/2611.32825)

**Authors:** Junxiang Zhang, Jiayu Zuo, Wenhao Ye, Junfeng Xia, Xiang Chen et al. (7 authors)

**Published:** 2026-11-24 (updated 2026-11-25) | **Categories:** cs.CV, q-bio.NC | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.32825) | [PDF](https://arxiv.org/pdf/2611.32825)

<details>
<summary>Abstract</summary>

Brain encoding models predict neural responses from audiovisual input, but typically overlook how ongoing brain activity shapes an individual's response. We introduce EEG-World, a recurrent world model that forecasts 10 seconds of EEG band-power dynamics from 6 seconds of preceding EEG and the subsequent audiovisual stimulus. Pretrained on continuous EEG, EEG-World learns shared neural dynamics and adapts to unseen individuals through lightweight subject-specific readouts. Using 2,584 hours of EEG from 78 participants, we show that nonlinear recurrent forecasting surpasses strong history-aware...

</details>

<details>
<summary>Share</summary>

```
EEG-World: Context-Conditioned Dynamics of the Watching Brain

Brain encoding models predict neural responses from audiovisual input, but typically overlook how ongoing brain activity shapes an individual's response.

arXiv: https://arxiv.org/abs/2611.32825

#worldmodels #robotics
```

</details>

---

### [ActField: Learning Action Effects as Continuous-Time Latent Dynamics](https://arxiv.org/abs/2611.30659)

**Authors:** Yunpeng Qing, Yuheng Huang, Changxu Wei, Yilun Kong, Yichen Shi et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

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
