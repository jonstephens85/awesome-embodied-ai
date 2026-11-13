# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-13 02:16 UTC

**Papers shown:** 42 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [WARP-JEPA: World-Model-in-the-Loop Amortized Rollout Planning for Frozen Hierarchical Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.10806)

**Authors:** Junjie Li, Zhaojiacheng Zhou, Kaixiang Wang, Zihan Wang, QingSong Zhao et al. (7 authors)

**Published:** 2026-11-07 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.10806) | [PDF](https://arxiv.org/pdf/2611.10806) | [Code](https://github.com/hideinsewer/WARP-JEPA)

<details>
<summary>Abstract</summary>

Hierarchical Joint-Embedding Predictive Architectures (H-JEPA) enable long-horizon visual control but rely on costly test-time gradient descent for planning. Our analysis reveals that iterative optimization consumes up to 97.7% of episode runtime and that low predicted rollout costs do not necessarily translate into successful control. We further identify a planning-horizon asymmetry between long-horizon top-level composition and short two-step subordinate planning. To address these challenges, we propose WARP-JEPA, a hierarchical amortized planning framework that replaces online gradient opti...

</details>

<details>
<summary>Share</summary>

```
WARP-JEPA: World-Model-in-the-Loop Amortized Rollout Planning for Frozen Hierarchical Joint-Embedding Predictive Architectures

Hierarchical Joint-Embedding Predictive Architectures (H-JEPA) enable long-horizon visual control but rely on costly test-time gradient descent for planning.

arXiv: https://arxiv.org/abs/2611.10806
Code: https://github.com/hideinsewer/WARP-JEPA

#worldmodels #robotics
```

</details>

---

### [ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation](https://arxiv.org/abs/2611.11605)

**Authors:** Yunyi Gao, Yixing Shi, Yize Liu, Hai-Duong Tran, Nhat-Hoang P. Nguyen et al. (11 authors)

**Published:** 2026-11-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11605) | [PDF](https://arxiv.org/pdf/2611.11605) | [Code](https://github.com/WANGSHUAIzzzz/ScanDreamer)

<details>
<summary>Abstract</summary>

Quadrotors inspecting buildings and tunnels must navigate unknown clutter with a forward-facing depth camera whose limited field of view constrains scene understanding and collision-avoiding navigation. Recent world-model agents learn navigation through imagined experience (e.g., AirDreamer), but remain data-intensive and often lack explicit geometric memory and awareness of what the camera can observe. We propose ScanDreamer, a map-grounded world model that constructs an online 2D scan-memory map from depth images and vehicle pose. Our world model, actor, and critic are conditioned on this ma...

</details>

<details>
<summary>Share</summary>

```
ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation

Quadrotors inspecting buildings and tunnels must navigate unknown clutter with a forward-facing depth camera whose limited field of view constrains scene understanding and collision-avoiding navigation.

arXiv: https://arxiv.org/abs/2611.11605
Code: https://github.com/WANGSHUAIzzzz/ScanDreamer

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

### [Breaking survivorship bias in driving world models](https://arxiv.org/abs/2611.11516)

**Authors:** Zihao Sheng, Zilin Huang, Yuhao Luo, Zhengyang Wan, Boyue Wang et al. (8 authors)

**Published:** 2026-11-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11516) | [PDF](https://arxiv.org/pdf/2611.11516) | [Project Page](https://zihaosheng.github.io/NWM/)

<details>
<summary>Abstract</summary>

World models allow autonomous vehicles to imagine the consequences of candidate actions before execution, but their reliability depends on the futures represented in their training data. We identify a survivorship bias in driving world models: because the futures recorded in prevailing driving datasets almost always end safely, existing models often imagine benign outcomes even when a collision is imminent. We introduce a neutral world model (NWM) that learns both routine and safety-critical futures from a mixture of routine driving and real accident videos with a bounding-box-guided objective...

</details>

<details>
<summary>Share</summary>

```
Breaking survivorship bias in driving world models

World models allow autonomous vehicles to imagine the consequences of candidate actions before execution, but their reliability depends on the futures represented in their training data.

arXiv: https://arxiv.org/abs/2611.11516
Project page: https://zihaosheng.github.io/NWM/

#worldmodels #robotics
```

</details>

---

### [ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset](https://arxiv.org/abs/2611.11085)

**Authors:** Haonan Chen, Sicheng Isabella Lu, Haitian Li, Jiajin Wu, Hexiang Wei et al. (12 authors)

**Published:** 2026-11-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11085) | [PDF](https://arxiv.org/pdf/2611.11085) | [Project Page](https://nus-lins-lab.github.io/ObjectWorld/)

<details>
<summary>Abstract</summary>

Generative world modeling from large-scale visual data offers a promising path toward scalable robot manipulation. This calls for an intermediate representation that can be supervised at scale and remains actionable for downstream control. We propose 3D full-object flow, an object-centric motion representation that assigns dense 3D trajectories to points across the complete surface of a target object, including its occluded regions. By extending visible-surface object flow to the full object geometry, this representation makes complete object motion explicit and applies uniformly to both rigid...

</details>

<details>
<summary>Share</summary>

```
ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset

Generative world modeling from large-scale visual data offers a promising path toward scalable robot manipulation.

arXiv: https://arxiv.org/abs/2611.11085
Project page: https://nus-lins-lab.github.io/ObjectWorld/

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

### [Tiresias: Towards Language-Conditioned World Models](https://arxiv.org/abs/2611.10392)

**Authors:** Fengyi Wu, Yifei Dong, Yetong Sha, Lingdong Kong, Qiyu Hu et al. (9 authors)

**Published:** 2026-11-07 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.10392) | [PDF](https://arxiv.org/pdf/2611.10392) | [Code](https://github.com/UWMILab/Tiresias)

<details>
<summary>Abstract</summary>

World models enable planning through internal simulation, while natural language provides intuitive task specification. Yet, language-conditioned world modeling remains fragmented across domains with disparate action spaces, datasets, and evaluation protocols. We introduce LCWM, a shared task that maps an initial agent-view observation and a language instruction to an action sequence that fulfills the instruction. Its accompanying benchmark, LCWM-Bench, integrates 15 datasets across navigation, robotics, 3D gaming, and driving under a shared action interface and evaluation protocol, pairing 14...

</details>

<details>
<summary>Share</summary>

```
Tiresias: Towards Language-Conditioned World Models

World models enable planning through internal simulation, while natural language provides intuitive task specification.

arXiv: https://arxiv.org/abs/2611.10392
Code: https://github.com/UWMILab/Tiresias

#worldmodels #robotics
```

</details>

---

### [Fast Inference-Time Policy Refinement via Action-Affine World Models](https://arxiv.org/abs/2611.15011)

**Authors:** Run Wang, Yilin Mo, Liang Wu

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

### [DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](https://arxiv.org/abs/2611.11166)

**Authors:** Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li et al. (9 authors)

**Published:** 2026-11-08 (updated 2026-11-10) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11166) | [PDF](https://arxiv.org/pdf/2611.11166) | [Project Page](https://dexforesight.github.io/)

<details>
<summary>Abstract</summary>

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight learns an action-conditioned spatial world model from offline scene depth, kinematic hand geometry, and demonstration trajectories. The world model predicts 3D hand-point motion and v...

</details>

<details>
<summary>Share</summary>

```
DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand.

arXiv: https://arxiv.org/abs/2611.11166
Project page: https://dexforesight.github.io/

#worldmodels #robotics
```

</details>

---

### [Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams](https://arxiv.org/abs/2611.10435)

**Authors:** Jamie Santos, Kagan Tumer

**Published:** 2026-11-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.10435) | [PDF](https://arxiv.org/pdf/2611.10435)

<details>
<summary>Abstract</summary>

Autonomous robot teams deployed in remote, unstructured environments may face changes in the environment, hardware, and team composition that degrade previously effective policies. Shifting mission objectives can be handled by selecting a different solution from an existing Pareto set, but shifting deployment conditions can reorder the set itself, making previously dominated policies competitive or new policies necessary. However, evaluating these policies in new contexts while minimizing risk to the hardware remains an open problem. We argue that, although largely untested in this domain, wor...

</details>

<details>
<summary>Share</summary>

```
Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams

Autonomous robot teams deployed in remote, unstructured environments may face changes in the environment, hardware, and team composition that degrade previously effective policies.

arXiv: https://arxiv.org/abs/2611.10435

#worldmodels #robotics
```

</details>

---

### [The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics](https://arxiv.org/abs/2611.10316)

**Authors:** Prerana Ramkumar, Suhas Suresh Bharadwaj, Fazal Hameed

**Published:** 2026-11-06 | **Categories:** cs.AR, cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.10316) | [PDF](https://arxiv.org/pdf/2611.10316)

<details>
<summary>Abstract</summary>

Embedded AI is moving from perception to prediction. Robots now use world models$\unicode{x2014}$learned simulators that predict the outcome of candidate actions in a compressed latent space before any is executed. Every predicted step must be computed on board within a tight power and thermal budget, yet the energy these steps fundamentally require, and how far real hardware sits from it, have not been characterized. We derive lower bounds on the arithmetic operations and the CMOS dynamic energy of a latent state transition from information theory and Boolean circuit complexity. Profiling a D...

</details>

<details>
<summary>Share</summary>

```
The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics

Embedded AI is moving from perception to prediction.

arXiv: https://arxiv.org/abs/2611.10316

#worldmodels #robotics
```

</details>

---

### [FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking](https://arxiv.org/abs/2611.08898)

**Authors:** Xiaorui Wang, Zeyu Sha, Mingyang Yang, David Chen Wang, Feitian Zhang

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.08898) | [PDF](https://arxiv.org/pdf/2611.08898)

<details>
<summary>Abstract</summary>

Reliable relative tracking is fundamental to cooperative autonomous underwater vehicles (AUVs), yet remains challenging under nonlinear vehicle dynamics and degraded underwater visual conditions. Active light markers improve robustness to appearance variation, but provide deliberately sparse observations that can become incomplete or corrupted by occlusion, reflections, and detection noise during dynamic motion. To address the resulting partial-observation control problem, this paper proposes FATHOM, a world-model-guided diffusion action-trajectory selection framework for sparse-marker AUV tra...

</details>

<details>
<summary>Share</summary>

```
FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking

Reliable relative tracking is fundamental to cooperative autonomous underwater vehicles (AUVs), yet remains challenging under nonlinear vehicle dynamics and degraded underwater visual conditions.

arXiv: https://arxiv.org/abs/2611.08898

#worldmodels #robotics
```

</details>

---

### [FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks](https://arxiv.org/abs/2611.14880)

**Authors:** Yinuo Du, Christopher Kiekintveld

**Published:** 2026-11-11 | **Categories:** cs.LG, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [K-PWM: Control-Oriented Structured Bilinear World Models under Partial Observation](https://arxiv.org/abs/2611.11521)

**Authors:** Santosh Mohan Rajkumar, Sriram Narayanan, Samuel E. Otto, Debdipta Goswami

**Published:** 2026-11-08 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.11521) | [PDF](https://arxiv.org/pdf/2611.11521)

<details>
<summary>Abstract</summary>

World models learn internal simulators of environment dynamics for prediction, planning, and control, yet learning them from limited, noisy, and partial observations remains challenging. While much progress has focused on pixel-based observations, many physical systems instead provide vector-valued measurements that reveal only part of the underlying state. We introduce K-PWM, a probabilistic world model for prediction and control under partial observation. K-PWM couples Koopman-bilinear latent dynamics with a nonlinear observation decoder and performs probabilistic latent-state inference thro...

</details>

<details>
<summary>Share</summary>

```
K-PWM: Control-Oriented Structured Bilinear World Models under Partial Observation

World models learn internal simulators of environment dynamics for prediction, planning, and control, yet learning them from limited, noisy, and partial observations remains challenging.

arXiv: https://arxiv.org/abs/2611.11521

#worldmodels #robotics
```

</details>

---

### [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](https://arxiv.org/abs/2611.10660)

**Authors:** Yinuo Jiang, Guangzhi Wang, Yiran Wang, Junfu Pu, Cheng Cheng et al. (8 authors)

**Published:** 2026-11-07 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.10660) | [PDF](https://arxiv.org/pdf/2611.10660)

<details>
<summary>Abstract</summary>

Latent world models enable visual control by planning action sequences in compact representation spaces, but a gap remains between how latent dynamics are learned and how they are used for planning. First, teacher-forced training does not expose the dynamics model to the recursively predicted latent states encountered during planning. Second, sampling-based planners typically initialize action search from goal-agnostic proposals, without exploiting the action-conditioned dynamics learned by the world model. We introduce Dynamics-Informed Action Learning (DIAL) to bridge these two gaps. During...

</details>

<details>
<summary>Share</summary>

```
Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning

Latent world models enable visual control by planning action sequences in compact representation spaces, but a gap remains between how latent dynamics are learned and how they are used for planning.

arXiv: https://arxiv.org/abs/2611.10660

#worldmodels #robotics
```

</details>

---

### [Toward the Era of Agentic Embodied Intelligence](https://arxiv.org/abs/2611.09124)

**Authors:** Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang, Yufeng Sun et al. (10 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.09124) | [PDF](https://arxiv.org/pdf/2611.09124)

<details>
<summary>Abstract</summary>

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execution history, and action proposals. MetaBrain provides training supervision and runtime guidance. A correction encoder and adapter absorb this knowledge into policy weights during training, while fresh codes adapt behavior with frozen weights at deployment. The action model, A2-WLA, adds motion-aware...

</details>

<details>
<summary>Share</summary>

```
Toward the Era of Agentic Embodied Intelligence

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery.

arXiv: https://arxiv.org/abs/2611.09124

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

### [WorldMind: Test-Time Scaling for Visual Spatial Reasoning through Latent World Simulation](https://arxiv.org/abs/2611.10151)

**Authors:** Haoming Wang, Yongjian Fu, Ju Ren, Wei Gao

**Published:** 2026-11-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.10151) | [PDF](https://arxiv.org/pdf/2611.10151)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) have continuous deficiency in spatial reasoning tasks that require \emph{mental spatial transformation}, such as reasoning under hypothetical changes in viewpoint or position, known as perspective-taking tasks. Existing approaches either scale linguistic reasoning or augment VLMs with static geometric representations, but neither directly enables active transformation of the represented scene. World models offer this capability, yet existing systems typically communicate through synthesized RGB images, introducing a latent-to-pixel-to-latent bottleneck. We introdu...

</details>

<details>
<summary>Share</summary>

```
WorldMind: Test-Time Scaling for Visual Spatial Reasoning through Latent World Simulation

Vision-Language Models (VLMs) have continuous deficiency in spatial reasoning tasks that require \emph{mental spatial transformation}, such as reasoning under hypothetical changes in viewpoint or position, known as pe...

arXiv: https://arxiv.org/abs/2611.10151

#worldmodels #robotics
```

</details>

---

### [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](https://arxiv.org/abs/2611.09625)

**Authors:** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte

**Published:** 2026-11-06 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.09625) | [PDF](https://arxiv.org/pdf/2611.09625)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-Based Reinforcement Learning (TT-MBRL), using gradient descent at test time to encode the memory of e...

</details>

<details>
<summary>Share</summary>

```
Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories.

arXiv: https://arxiv.org/abs/2611.09625

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

### [ForeAct: Geometry-Guided Action Learning from World Representations](https://arxiv.org/abs/2611.11500)

**Authors:** Wei Lu, Jiaxi Zhang, Yunheng Wang, Taowen Wang, Yuetong Fang et al. (11 authors)

**Published:** 2026-11-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.11500) | [PDF](https://arxiv.org/pdf/2611.11500)

<details>
<summary>Abstract</summary>

Robotic manipulation requires representations that capture both scene geometry and its evolution during interaction. Existing approaches have largely treated these two aspects separately. World action models capture such dynamics by coupling action prediction with future video generation, but their reliance on iterative diffusion or rectified-flow inference leads to high computational cost, while their representations lack explicit spatial structure. Explicitly modeling scene geometry typically requires auxiliary modules that increase both parameter count and computational cost. Conversely, ge...

</details>

<details>
<summary>Share</summary>

```
ForeAct: Geometry-Guided Action Learning from World Representations

Robotic manipulation requires representations that capture both scene geometry and its evolution during interaction.

arXiv: https://arxiv.org/abs/2611.11500

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

### [WorldFoundry: Towards Unified Infrastructure for World Intelligence](https://arxiv.org/abs/2611.10771)

**Authors:** Juanxi Tian, Jiadong Hou, Baiang Li, Xin Lin, Zhengbo Jiao et al. (16 authors)

**Published:** 2026-11-07 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.10771) | [PDF](https://arxiv.org/pdf/2611.10771)

<details>
<summary>Abstract</summary>

Visual generative models increasingly blur the line between synthesizing observations and simulating environments. Yet visual plausibility alone does not constitute successful world modeling: compelling outputs may lack persistent state, physical dynamics, or causally consistent responses to interactions. We define a generative world model as a predictive dynamical system that maintains a persistent, history-conditioned representation of an environment, updates that representation in response to actions or interventions, and generates temporally coherent trajectories that reflect outcomes unde...

</details>

<details>
<summary>Share</summary>

```
WorldFoundry: Towards Unified Infrastructure for World Intelligence

Visual generative models increasingly blur the line between synthesizing observations and simulating environments.

arXiv: https://arxiv.org/abs/2611.10771

#worldmodels #robotics
```

</details>

---
