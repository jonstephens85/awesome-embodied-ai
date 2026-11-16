# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-16 23:58 UTC

**Papers shown:** 41 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

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

### [BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model](https://arxiv.org/abs/2611.14815)

**Authors:** Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang et al. (6 authors)

**Published:** 2026-11-10 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14815) | [PDF](https://arxiv.org/pdf/2611.14815) | [Project Page](https://research.nvidia.com/labs/sil/projects/birddreams/)

<details>
<summary>Abstract</summary>

Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and vehicles can be occluded. Prior work therefore conditions video generation on layouts that specify vehicle motion, providing control over surrounding vehicles but requiring their future trajectories as inputs. We introduce BirdDreams, an autoregressive driving world model that jointly generates pers...

</details>

<details>
<summary>Share</summary>

```
BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model

Driving world models aim to simulate how a scene unfolds under different ego actions.

arXiv: https://arxiv.org/abs/2611.14815
Project page: https://research.nvidia.com/labs/sil/projects/birddreams/

#worldmodels #robotics
```

</details>

---

### [How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324)

**Authors:** Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi

**Published:** 2026-11-09 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.12324) | [PDF](https://arxiv.org/pdf/2611.12324) | [Code](https://github.com/third-intelligence/WARC)

<details>
<summary>Abstract</summary>

World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic that the model observes is one exposure. We ask how many exposures a world model needs to predict the effects of a new environment's mechanics. We address this question on ARC-AGI-3, a benchmark of interactive games defined by their programs. We introduce MechEval, which labels 69 recurring mechanics across 20 games fr...

</details>

<details>
<summary>Share</summary>

```
How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time

World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction.

arXiv: https://arxiv.org/abs/2611.12324
Code: https://github.com/third-intelligence/WARC

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

### [From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models](https://arxiv.org/abs/2611.14365)

**Authors:** Guoqiang Liang, Yiqi Lin, Yanzhe Chen, Kevin Yuchen Ma, Mike Zheng Shou

**Published:** 2026-11-10 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14365) | [PDF](https://arxiv.org/pdf/2611.14365) | [Code](https://github.com/showlab/MetaWAM)

<details>
<summary>Abstract</summary>

Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bolting on dedicated encoders and decoders. We argue that signal injection is instead a distribution-a...

</details>

<details>
<summary>Share</summary>

```
From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models

Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations.

arXiv: https://arxiv.org/abs/2611.14365
Code: https://github.com/showlab/MetaWAM

#worldmodels #robotics
```

</details>

---

### [How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens](https://arxiv.org/abs/2611.11887)

**Authors:** Yong Hwi Song, Keon Myung Lee

**Published:** 2026-11-09 | **Categories:** cs.LG, cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11887) | [PDF](https://arxiv.org/pdf/2611.11887) | [Code](https://github.com/thddydgnl/nearest-of-m-world-models)

<details>
<summary>Abstract</summary>

One-step stochastic world models avoid the mode averaging of deterministic feature predictors without the tens of network evaluations per step that diffusion and flow matching require. The simplest such objective is nearest-of-m matching (conditional implicit maximum likelihood estimation, IMLE): draw m candidate futures and pull only the one closest to the observed outcome. Recent work conjectures that a small m suffices for feature-space world models and that a strictly proper energy score should replace the hard minimum. We test both claims with one-step world models on frozen DINOv2/v3 pat...

</details>

<details>
<summary>Share</summary>

```
How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens

One-step stochastic world models avoid the mode averaging of deterministic feature predictors without the tens of network evaluations per step that diffusion and flow matching require.

arXiv: https://arxiv.org/abs/2611.11887
Code: https://github.com/thddydgnl/nearest-of-m-world-models

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

**Published:** 2026-11-11 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

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

### [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](https://arxiv.org/abs/2611.11912)

**Authors:** Zhimin Liao, Ping Wei, Kai Mao, Shuaijia Chen

**Published:** 2026-11-09 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11912) | [PDF](https://arxiv.org/pdf/2611.11912) | [Code](https://github.com/lzzzzzm/LO-World)

<details>
<summary>Abstract</summary>

LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural potential for mutual complementarity. However, existing world models typically forecast these modalities independently or cascade them heuristically, missing the opportunity for reciprocal cross-modal regularization. To address this, we propose \textbf{LO-World}, a unified 4D world model that forecasts both modalities within a shared BEV latent space. This single-stream formulation enables dense semantics and metric...

</details>

<details>
<summary>Share</summary>

```
LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting

LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural potential for mutual complementarity.

arXiv: https://arxiv.org/abs/2611.11912
Code: https://github.com/lzzzzzm/LO-World

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

### [$Σ$-LeWM: Learning World Models via S-Information for Robot Control](https://arxiv.org/abs/2611.12732)

**Authors:** Xinrui Zu, Michael Przystupa, Zhao Yang, Shujian Yu, Kevin Sebastian Luck

**Published:** 2026-11-09 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.12732) | [PDF](https://arxiv.org/pdf/2611.12732)

<details>
<summary>Abstract</summary>

World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion. While early world model architectures relied on decoders to prevent mode collapse and learn a predictable latent space, recent works on world models, such as Joint Embedding Predictive Architecture or LeWorldModel, increasingly aim to learn embeddings without a grounding decoder, utilising only a latent forward dynamics predictor and a stabilising entropy term. In this paper, we set out to demonstrate that the further introduction of two additional latent losses t...

</details>

<details>
<summary>Share</summary>

```
$Σ$-LeWM: Learning World Models via S-Information for Robot Control

World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion.

arXiv: https://arxiv.org/abs/2611.12732

#worldmodels #robotics
```

</details>

---

### [Action Representation for Spatial Generalization in Robot World Models](https://arxiv.org/abs/2611.11869)

**Authors:** Yuhang Sun

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.11869) | [PDF](https://arxiv.org/pdf/2611.11869)

<details>
<summary>Abstract</summary>

Spatial generalization in robot world models depends on whether action representations capture the physical relationships that remain valid across changing spatial configurations. Yet different coordinates can describe the same interaction, whereas similar motions can produce different outcomes when local physical conditions change. How these distinctions affect learned prediction remains insufficiently understood. This study evaluates matched action representations defined in world, object, and surface coordinate frames using a controlled robotic peeling benchmark. Global pose and contact rel...

</details>

<details>
<summary>Share</summary>

```
Action Representation for Spatial Generalization in Robot World Models

Spatial generalization in robot world models depends on whether action representations capture the physical relationships that remain valid across changing spatial configurations.

arXiv: https://arxiv.org/abs/2611.11869

#worldmodels #robotics
```

</details>

---

### [OnlyAct: Extracting Action Representations from Foundation Models for World Models](https://arxiv.org/abs/2611.14420)

**Authors:** Runjia Li, Minghao Chen, Junyu Xie, Philip Torr, Andrea Vedaldi et al. (6 authors)

**Published:** 2026-11-10 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.14420) | [PDF](https://arxiv.org/pdf/2611.14420)

<details>
<summary>Abstract</summary>

Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the previous frame and that latent, forcing the latent to capture only new information. This has two limitations: learning the action space from scratch can limit generalization to unseen dom...

</details>

<details>
<summary>Share</summary>

```
OnlyAct: Extracting Action Representations from Foundation Models for World Models

Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with th...

arXiv: https://arxiv.org/abs/2611.14420

#worldmodels #robotics
```

</details>

---

### [PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in Text-to-Video Generation](https://arxiv.org/abs/2611.13576)

**Authors:** Huiyi Chen, Weitai Kang, Shicheng Fan, Xinshuo Wang, Zhixiang Shen et al. (8 authors)

**Published:** 2026-11-10 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.13576) | [PDF](https://arxiv.org/pdf/2611.13576)

<details>
<summary>Abstract</summary>

As text-to-video (T2V) models are increasingly positioned as world simulators, it is essential to evaluate whether their videos conform to physical commonsense. However, existing benchmarks rely on annotators who rate each video with a single score based on intuition, yielding ratings that are subjective and do not tell which physical principle is violated. We introduce PhyRubric, a rubric-grounded diagnostic framework for evaluating physical commonsense in T2V generation. For each caption, PhyRubric constructs a caption-specific rubric before any video is seen, decomposing the caption into se...

</details>

<details>
<summary>Share</summary>

```
PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in Text-to-Video Generation

As text-to-video (T2V) models are increasingly positioned as world simulators, it is essential to evaluate whether their videos conform to physical commonsense.

arXiv: https://arxiv.org/abs/2611.13576

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

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.15011) | [PDF](https://arxiv.org/pdf/2611.15011)

<details>
<summary>Abstract</summary>

Imitation policies can perform complex manipulation, yet small execution errors can accumulate and cause failure. Refinement can correct these errors, but existing approaches often require additional on-policy learning or costly online planning. Our key insight is that a pretrained policy already supplies a useful nominal behavior: refinement can focus on predicting how small action corrections change its outcome. We therefore learn this local response in a form that is cheap to optimize. Our \textit{action-affine world model} (A\textsuperscript{2}WM) learns local action sensitivities offline...

</details>

<details>
<summary>Share</summary>

```
Fast Inference-Time Policy Refinement via Action-Affine World Models

Imitation policies can perform complex manipulation, yet small execution errors can accumulate and cause failure.

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

### [Few-Shot Residual Adaptation of Pretrained Latent World Models](https://arxiv.org/abs/2611.13592)

**Authors:** Jakub Suliga, Pankhuri Vanjani, Nisarga Nilavadi, Wolfram Burgard, Rudolf Lioutikov

**Published:** 2026-11-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.13592) | [PDF](https://arxiv.org/pdf/2611.13592)

<details>
<summary>Abstract</summary>

Pretrained latent world models can support visual planning and control, but their predictions may fail when physical dynamics change at deployment. We study whether such models can adapt from only a few interactions without modifying their pretrained weights or identifying the changed physical parameters. We introduce a few-shot residual adaptation approach that learns self-supervised corrections from latent prediction errors. The corrections are applied both inside the latent predictor and directly to its predicted latent state, while the pretrained world model remains frozen. We evaluate the...

</details>

<details>
<summary>Share</summary>

```
Few-Shot Residual Adaptation of Pretrained Latent World Models

Pretrained latent world models can support visual planning and control, but their predictions may fail when physical dynamics change at deployment.

arXiv: https://arxiv.org/abs/2611.13592

#worldmodels #robotics
```

</details>

---

### [Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing](https://arxiv.org/abs/2611.13229)

**Authors:** Nikita Sarawgi, Omey M. Manyar, Satyandra K. Gupta

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.13229) | [PDF](https://arxiv.org/pdf/2611.13229)

<details>
<summary>Abstract</summary>

Efficient robotic 3D reconstruction requires selecting views that contribute new surface measurements with few physical captures. Pretrained world models can guide this choice, but a predicted surface may not produce valid depth measurements under the operating conditions of the deployed sensor. We present a deployment adaptation methodology for next-best-view selection that learns a sensor-return adapter from limited local calibration data while keeping the pretrained predictor fixed. The adapter estimates measurement dropout over each predicted surface, allowing the selection method to favor...

</details>

<details>
<summary>Share</summary>

```
Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing

Efficient robotic 3D reconstruction requires selecting views that contribute new surface measurements with few physical captures.

arXiv: https://arxiv.org/abs/2611.13229

#worldmodels #robotics
```

</details>

---

### [Library of Hands: Fix the Hands, Not the World Model](https://arxiv.org/abs/2611.12678)

**Authors:** Hasaan Ahmad, Qizhen Ying, Yuxuan Sun, Tianjin Huang, Guangming Wang

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.12678) | [PDF](https://arxiv.org/pdf/2611.12678)

<details>
<summary>Abstract</summary>

A world model predicts how a scene changes after an action, and a planner uses it to search for actions that reach a goal. If the camera moves or the controller changes, the same command moves the robot differently: when its commands are turned by 90 degrees, a frozen planner with the LeWM world model that succeeds in 77.5% of episodes succeeds in only 7.8%. Current fixes retrain the model, need training data, or forget a set-up when it returns. We propose Library of Hands (LoH), a training-free method that keeps the world model frozen and corrects only the map from commands to applied actions...

</details>

<details>
<summary>Share</summary>

```
Library of Hands: Fix the Hands, Not the World Model

A world model predicts how a scene changes after an action, and a planner uses it to search for actions that reach a goal.

arXiv: https://arxiv.org/abs/2611.12678

#worldmodels #robotics
```

</details>

---

### [Planners Exploit Deterministic Error: Dithered Low-Bit World Models](https://arxiv.org/abs/2611.11780)

**Authors:** Yong Hwi Song, Keon Myung Lee

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.11780) | [PDF](https://arxiv.org/pdf/2611.11780)

<details>
<summary>Abstract</summary>

Sampling-based planners such as MPPI and CEM query a learned world model thousands of times per control step, so low-bit world models are an obvious way to make model-based control cheaper on a robot. With round-to-nearest activation quantization and no calibration, we find that planning can collapse, by up to 100 points of success, while the world model's latent one-step prediction error stays no larger than that of a stochastic rounding scheme that plans well. At the same bit width, what decides the outcome is not the size of the rounding error but whether it persists across planner iteratio...

</details>

<details>
<summary>Share</summary>

```
Planners Exploit Deterministic Error: Dithered Low-Bit World Models

Sampling-based planners such as MPPI and CEM query a learned world model thousands of times per control step, so low-bit world models are an obvious way to make model-based control cheaper on a robot.

arXiv: https://arxiv.org/abs/2611.11780

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

### [Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning](https://arxiv.org/abs/2611.14419)

**Authors:** Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig

**Published:** 2026-11-10 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.14419) | [PDF](https://arxiv.org/pdf/2611.14419)

<details>
<summary>Abstract</summary>

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchmark of 44 scenarios spanning game, situational, and cultural settings and evaluate generated world mo...

</details>

<details>
<summary>Share</summary>

```
Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formaliz...

arXiv: https://arxiv.org/abs/2611.14419

#worldmodels #robotics
```

</details>

---

### [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)

**Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik et al. (8 authors)

**Published:** 2026-11-09 | **Categories:** q-bio.BM, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.13348) | [PDF](https://arxiv.org/pdf/2611.13348)

<details>
<summary>Abstract</summary>

Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sample a small fraction of sequence space. Thus, a central challenge is to efficiently traverse the large combinatorial space of mutations in silico. We introduce ProTEUS, a mutation-resolved world model for closed-loop protein evolution. Pretrained on deep mutational scanning assays, ProTEUS learns a joint representation of sequence, evolutionary, and structural information using MutationFormer, a mutation-biased attentio...

</details>

<details>
<summary>Share</summary>

```
ProTEUS: A mutation-resolved world model for closed-loop protein evolution

Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sample a small fraction of sequence space.

arXiv: https://arxiv.org/abs/2611.13348

#worldmodels #robotics
```

</details>

---

### [Building World Models from Intrinsic Motivation](https://arxiv.org/abs/2611.13113)

**Authors:** Reece Keller, Declan Kutscher, Xaq Pitkow, Aran Nayebi

**Published:** 2026-11-09 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.13113) | [PDF](https://arxiv.org/pdf/2611.13113)

<details>
<summary>Abstract</summary>

In the absence of extrinsic rewards or task supervision, human behavior is guided by intrinsic motivation---neural signals that drive curiosity, creativity, play, and other essential facets of intelligence. Intrinsic motivation plays an important developmental role in building robust world models that enable generalization and adaptation. Yet existing studies leave open how a broad range of intrinsic motivations interacts with world-model representation learning to support downstream control. This limits our understanding of which intrinsically collected experiences build reusable models. To a...

</details>

<details>
<summary>Share</summary>

```
Building World Models from Intrinsic Motivation

In the absence of extrinsic rewards or task supervision, human behavior is guided by intrinsic motivation---neural signals that drive curiosity, creativity, play, and other essential facets of intelligence.

arXiv: https://arxiv.org/abs/2611.13113

#worldmodels #robotics
```

</details>

---

### [WanderBench: Can World Models Explore Dynamic Worlds from Video?](https://arxiv.org/abs/2611.12557)

**Authors:** Yuhang Chen, Jiheng Li, Jiale Wang, Zai Wang, Guangyue Liu

**Published:** 2026-11-09 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.12557) | [PDF](https://arxiv.org/pdf/2611.12557)

<details>
<summary>Abstract</summary>

Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the recorded world, yet existing benchmarks start from a single image or a text prompt, and video-conditioned generation is evaluated mainly on perceptual quality and camera following. These evaluations do not directly assess whether exploration preserves subject identity, event progression, and scene consistency upon revisi...

</details>

<details>
<summary>Share</summary>

```
WanderBench: Can World Models Explore Dynamic Worlds from Video?

Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents.

arXiv: https://arxiv.org/abs/2611.12557

#worldmodels #robotics
```

</details>

---

### [An Evaluation of Tabular Foundation Models as Training-Free World Models](https://arxiv.org/abs/2611.11921)

**Authors:** Xian Yeow Lee, Ryoichi Takase, Ahmed Farahat

**Published:** 2026-11-09 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.11921) | [PDF](https://arxiv.org/pdf/2611.11921)

<details>
<summary>Abstract</summary>

World models are widely considered to be a potential key component of model-based reinforcement learning and robot planning, but typically require task-specific training on substantial interaction data. We investigate whether a pretrained tabular foundation model (TabFM) can serve as a training-free dynamics model for world modeling by framing next-state prediction as in-context regression over transition pairs, and where such a model helps and where it breaks. Across synthetic dynamical systems and robot locomotion benchmarks, TabFM is more accurate than LSTM and MLP models trained from scrat...

</details>

<details>
<summary>Share</summary>

```
An Evaluation of Tabular Foundation Models as Training-Free World Models

World models are widely considered to be a potential key component of model-based reinforcement learning and robot planning, but typically require task-specific training on substantial interaction data.

arXiv: https://arxiv.org/abs/2611.11921

#worldmodels #robotics
```

</details>

---

### [LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning](https://arxiv.org/abs/2611.14048)

**Authors:** Xuheng Zhang, Yiming Zhang, Jialin Gao, Hao Chen, Jiaming Liu et al. (17 authors)

**Published:** 2026-11-10 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.14048) | [PDF](https://arxiv.org/pdf/2611.14048)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics. Existing WAMs, encompassing both video-first action prediction and joint video-action modeling, directly transfer global physical representations from world models to action generation. However, global scene representations may underemphasize local robot-object interactions, creating a mismatch between representations optimized for world evolution and those required for manipulation. To bridge this gap, we pro...

</details>

<details>
<summary>Share</summary>

```
LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics.

arXiv: https://arxiv.org/abs/2611.14048

#worldmodels #robotics
```

</details>

---

### [GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM](https://arxiv.org/abs/2611.13528)

**Authors:** Yuchen Yang, Ming Ding, Xinyu Wu, Hesheng Wang

**Published:** 2026-11-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.13528) | [PDF](https://arxiv.org/pdf/2611.13528)

<details>
<summary>Abstract</summary>

Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over continuous operation. 3D Gaussian splatting makes such representations attainable by supplying an explicit, renderable, and queryable scene model. We present GEMOR-GS (Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM) to make the Gaussian map geometrically accurate, globally refined, and re-enterable, providing a better appearance for robot perception and decision-making. To improve the 3DGS...

</details>

<details>
<summary>Share</summary>

```
GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM

Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over continuous operation.

arXiv: https://arxiv.org/abs/2611.13528

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

### [An Energy-Based Perspective on Machine Learning](https://arxiv.org/abs/2611.14383)

**Authors:** Bo Dai, Yilun Du

**Published:** 2026-11-10 | **Categories:** cs.AI, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.14383) | [PDF](https://arxiv.org/pdf/2611.14383)

<details>
<summary>Abstract</summary>

Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, which fits the energy to data. We first develop these components, including sampling, variational infer...

</details>

<details>
<summary>Share</summary>

```
An Energy-Based Perspective on Machine Learning

Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many.

arXiv: https://arxiv.org/abs/2611.14383

#worldmodels #robotics
```

</details>

---

### [Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](https://arxiv.org/abs/2611.12319)

**Authors:** Junha Ryu, Hoi-Jun Yoo

**Published:** 2026-11-09 | **Categories:** cs.DC, cs.CV, cs.GR | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.12319) | [PDF](https://arxiv.org/pdf/2611.12319)

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators. However, existing optimizations rely on algorithmic changes that often require retraining, or on specialized accelerators that lack flexibility across evolving 3DGS variants. In this paper, we identify a fundamental inefficiency in GPU-based 3DGS rendering: severe SM-level load imbalance caused by uneven workloads across screen tiles. This imbalance creates a long execution tail, leaving most SMs idle while a few pr...

</details>

<details>
<summary>Share</summary>

```
Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs

3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators.

arXiv: https://arxiv.org/abs/2611.12319

#worldmodels #robotics
```

</details>

---

### [Benchmarking language models and agents for scientific reasoning in evolving materials laboratories](https://arxiv.org/abs/2611.12014)

**Authors:** Xuyu Dong, Yixuan Li, Jianguo Huang, Feng Chen, Yiyun Zhou et al. (8 authors)

**Published:** 2026-11-09 | **Categories:** cs.AI, cond-mat.mtrl-sci, cs.CE | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.12014) | [PDF](https://arxiv.org/pdf/2611.12014)

<details>
<summary>Abstract</summary>

Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions. Existing benchmarks establish capabilities in domain knowledge, multimodal interpretation and scientific tool use. As language models increasingly support materials research workflows, their ability to distinguish closely related material states and reason accurately with quantitative evidence remains insufficiently evaluated. These abilities are essential for comparing material responses, assessing mechanisms and maintaining r...

</details>

<details>
<summary>Share</summary>

```
Benchmarking language models and agents for scientific reasoning in evolving materials laboratories

Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions.

arXiv: https://arxiv.org/abs/2611.12014

#worldmodels #robotics
```

</details>

---
