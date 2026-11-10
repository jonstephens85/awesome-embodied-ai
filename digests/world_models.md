# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-10 03:52 UTC

**Papers shown:** 31 (relevance ≥ 2, last 7 days)

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

### [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730)

**Authors:** Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang

**Published:** 2026-11-05 | **Categories:** cs.GR, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07730) | [PDF](https://arxiv.org/pdf/2611.07730) | [Project Page](https://seoneun.github.io/-NeurIPS-2026-Seeing-Beyond-the-Next-Step/)

<details>
<summary>Abstract</summary>

Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current state alone, and acting on them requires reasoning about what each candidate action will cause. World models offer exactly this, namely action-conditioned predictions of the future, but rolling them out at every decision step is a cost deployable navigation systems cannot pay, and...

</details>

<details>
<summary>Share</summary>

```
Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of cros...

arXiv: https://arxiv.org/abs/2611.07730
Project page: https://seoneun.github.io/-NeurIPS-2026-Seeing-Beyond-the-Next-Step/

#worldmodels #robotics
```

</details>

---

### [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](https://arxiv.org/abs/2611.06120)

**Authors:** Hanwei Liu, Huijia Zhang, Hanzhang Wang, Guangyu Liu, Hanbei Zhan et al. (9 authors)

**Published:** 2026-11-04 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06120) | [PDF](https://arxiv.org/pdf/2611.06120) | [Project Page](https://metaengine-world.github.io/ReactWorld/)

<details>
<summary>Abstract</summary>

Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics. Critical responses in embodied scenes often concentrate in local regions and specific time intervals. Inspired by chain-of-thought reasoning, we introduce ReactWorld, an embodied video generation model guided by structured interaction anticipation. In the generation backbone's feature space, an interaction response field predictor anticipates how the interaction will unfold, explicitly describing participant roles, future motio...

</details>

<details>
<summary>Share</summary>

```
ReactWorld: Structuring Interaction Responses for Embodied Video Generation

Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics.

arXiv: https://arxiv.org/abs/2611.06120
Project page: https://metaengine-world.github.io/ReactWorld/

#worldmodels #robotics
```

</details>

---

### [Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model](https://arxiv.org/abs/2611.05448)

**Authors:** Yansong Qu, Jiancong Chen, Samuel Labi

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05448) | [PDF](https://arxiv.org/pdf/2611.05448) | [Project Page](https://ys-qu.github.io/jev-ad-website)

<details>
<summary>Abstract</summary>

Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene. We present Jev-AD, which pairs Jev, a typed decision model that answers predefined questions with probabilities, not generated text, with a language world model that predicts for every candidate action how nearby vehicles move over the next two seconds. Code turns these predictions into foreseen consequences, which Jev compares instead of inferring them from coordinates. In simulated highway merging (...

</details>

<details>
<summary>Share</summary>

```
Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model

Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene.

arXiv: https://arxiv.org/abs/2611.05448
Project page: https://ys-qu.github.io/jev-ad-website

#worldmodels #robotics
```

</details>

---

### [Learning Robotic World Models with Semantic and Visual Feedback](https://arxiv.org/abs/2611.07850)

**Authors:** Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07850) | [PDF](https://arxiv.org/pdf/2611.07850) | [Code](https://github.com/Alexander-wu/RoboImagine)

<details>
<summary>Abstract</summary>

Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative feedback. We present RoboImagine, a framework for post-training autoregressive robotic world models through candidate-future comparisons with semantic and visual feedback. Diverse search promotes diversity among candidate trajectories under shared visual observations, action sequenc...

</details>

<details>
<summary>Share</summary>

```
Learning Robotic World Models with Semantic and Visual Feedback

Robot world models predict action-conditioned future visual states to support robotic planning and decision making.

arXiv: https://arxiv.org/abs/2611.07850
Code: https://github.com/Alexander-wu/RoboImagine

#worldmodels #robotics
```

</details>

---

### [Time-to-Goal: Learned Temporal Metrics for Long-Horizon Planning with JEPA World Models](https://arxiv.org/abs/2611.05847)

**Authors:** Ruilong Yu, Fei Ye

**Published:** 2026-11-04 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.05847) | [PDF](https://arxiv.org/pdf/2611.05847)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) support planning by comparing predicted latent states with an encoded goal. For this comparison to guide temporal progress, states closer in time to the goal should receive lower costs. However, training representations for prediction and distribution regularization does not directly enforce this ordering. We examine this mismatch in flat LeWorldModel (LeWM) by analyzing how its Euclidean goal cost changes with temporal separation. Our analysis identifies conditions under which states at different long offsets receive similar average costs, weak...

</details>

<details>
<summary>Share</summary>

```
Time-to-Goal: Learned Temporal Metrics for Long-Horizon Planning with JEPA World Models

Joint-Embedding Predictive Architectures (JEPAs) support planning by comparing predicted latent states with an encoded goal.

arXiv: https://arxiv.org/abs/2611.05847

#worldmodels #robotics
```

</details>

---

### [Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving](https://arxiv.org/abs/2611.05072)

**Authors:** Junzhe Wang, Jinqing Zhang, Qingjie Liu

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.05072) | [PDF](https://arxiv.org/pdf/2611.05072)

<details>
<summary>Abstract</summary>

Although existing candidate trajectory evaluators have substantially improved end-to-end planning accuracy, their underlying mechanism remains suboptimal. Model-based evaluators typically make scoring future-aware by explicitly predicting candidate-conditioned future states over the planning horizon, which we term rollout. However, rollout incurs high inference cost and accumulates prediction errors. We argue that planning does not require reconstructing a full future scene for each candidate, but only future-relevant information for reliable comparison. We therefore propose RFWorld, a Rollout...

</details>

<details>
<summary>Share</summary>

```
Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving

Although existing candidate trajectory evaluators have substantially improved end-to-end planning accuracy, their underlying mechanism remains suboptimal.

arXiv: https://arxiv.org/abs/2611.05072

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

### [WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation](https://arxiv.org/abs/2611.07939)

**Authors:** Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07939) | [PDF](https://arxiv.org/pdf/2611.07939) | [Project Page](https://fudan-generative-vision.github.io/WAM-Sim)

<details>
<summary>Abstract</summary>

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales: pose-aligned structural tokens encoding persistent road topology, read-only scene tokens supplying geolocated background appearance, and write-once instance tokens preserving indivi...

</details>

<details>
<summary>Share</summary>

```
WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state.

arXiv: https://arxiv.org/abs/2611.07939
Project page: https://fudan-generative-vision.github.io/WAM-Sim

#worldmodels #robotics
```

</details>

---

### [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](https://arxiv.org/abs/2611.07867)

**Authors:** Jihai Zhang, Yuhan Zhou, Junyou Li, Deheng Ye, Qi Dou et al. (6 authors)

**Published:** 2026-11-05 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07867) | [PDF](https://arxiv.org/pdf/2611.07867) | [Code](https://github.com/MajorDavidZhang/PlayGen-2)

<details>
<summary>Abstract</summary>

Building a playable world requires more than generating plausible video: it demands responsive control, persistent spatial structure, and coherent interactions with dynamic entities. Using generated frames as the sole recurrent world representation ties these requirements to view-dependent appearance synthesis, making it difficult to maintain long-term spatial and temporal consistency in generation and interaction. We present PlayGen2, a real-time interactive world model that separates learned 3D state evolution from neural rendering. PlayGen2 maintains a persistent world memory comprising sta...

</details>

<details>
<summary>Share</summary>

```
PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State

Building a playable world requires more than generating plausible video: it demands responsive control, persistent spatial structure, and coherent interactions with dynamic entities.

arXiv: https://arxiv.org/abs/2611.07867
Code: https://github.com/MajorDavidZhang/PlayGen-2

#worldmodels #robotics
```

</details>

---

### [From Video to Digital Twin: An Exploratory Study of World Models and Gaussian Splatting on In-the-Wild Video](https://arxiv.org/abs/2611.10013)

**Authors:** Somesh Mohapatra

**Published:** 2026-11-04 | **Categories:** cs.CV, cs.GR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.10013) | [PDF](https://arxiv.org/pdf/2611.10013) | [Code](https://github.com/pikulsomesh/foodbank-spatial-twin)

<details>
<summary>Abstract</summary>

Generative world models and 3D Gaussian Splatting promise to turn ordinary video into explorable 3D scenes, but little is reported on how they behave on uncurated, in-the-wild footage. We study what these models recover when the only input is a publicly available news walkthrough of a food bank warehouse, with presenters walking through every shot and no drawings, scans or site visit, and we use the result as the geometry of a digital twin. A commercial world model given 20 frames recovered camera poses and metric depth for three areas, which we fused into about 747,000 Gaussian splats for 200...

</details>

<details>
<summary>Share</summary>

```
From Video to Digital Twin: An Exploratory Study of World Models and Gaussian Splatting on In-the-Wild Video

Generative world models and 3D Gaussian Splatting promise to turn ordinary video into explorable 3D scenes, but little is reported on how they behave on uncurated, in-the-wild footage.

arXiv: https://arxiv.org/abs/2611.10013
Code: https://github.com/pikulsomesh/foodbank-spatial-twin

#worldmodels #robotics
```

</details>

---

### [MKD2World: A Typed Spatial MarkDown World Model For Web Agents](https://arxiv.org/abs/2611.06544)

**Authors:** Zhihao Nan, Sifan Zhou, Yiming Cheng, Jinkai Zheng, Zheng Zhu et al. (8 authors)

**Published:** 2026-11-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06544) | [PDF](https://arxiv.org/pdf/2611.06544) | [Code](https://github.com/OmniAI-Lab-CUHKSZ/MKD2World)

<details>
<summary>Abstract</summary>

Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces. Existing state representations fail to jointly capture interface layout, UI semantics, and explicit locations. We introduce Typed Spatial Markdown (TSM), a Markdown-style textual state representation for desktop web interfaces. TSM serializes block-level and atomic-level UI elements according to their spatial relationships, jointly encoding their types, visual semantics, explicit locations, optional control states, and hierarchi...

</details>

<details>
<summary>Share</summary>

```
MKD2World: A Typed Spatial MarkDown World Model For Web Agents

Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces.

arXiv: https://arxiv.org/abs/2611.06544
Code: https://github.com/OmniAI-Lab-CUHKSZ/MKD2World

#worldmodels #robotics
```

</details>

---

### [Readable Is Not Steerable: Pre-Registered Tests of Physical Structure in Learned Fluid Representations](https://arxiv.org/abs/2611.05577)

**Authors:** Manvendra Modgil

**Published:** 2026-11-03 | **Categories:** cs.LG, cs.AI, physics.flu-dyn | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05577) | [PDF](https://arxiv.org/pdf/2611.05577) | [Code](https://github.com/2025eb1100268-tech/readable-not-steerable)

<details>
<summary>Abstract</summary>

Self-supervised world models are often said to organize their latents around physical quantities. We test this on 2D decaying Navier-Stokes flow in three pre-registered studies, each tested once on held-out data. In Study 1, a joint-embedding predictive architecture (JEPA) trained to predict the flow fails the pre-registered criteria for organizing its latent around fluid quantities better than an untrained network of the same architecture (not supported); a JEPA trained on non-physical linear dynamics and a static invariance model that never sees time do as well or better. In Study 2, plain a...

</details>

<details>
<summary>Share</summary>

```
Readable Is Not Steerable: Pre-Registered Tests of Physical Structure in Learned Fluid Representations

Self-supervised world models are often said to organize their latents around physical quantities.

arXiv: https://arxiv.org/abs/2611.05577
Code: https://github.com/2025eb1100268-tech/readable-not-steerable

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

### [GPWM: Modeling the World as 3D Particle Motion](https://arxiv.org/abs/2611.08338)

**Authors:** Robert Ren, Matthew Bronars, He Zhu, Yikai Tang, Jianing Zhang et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08338) | [PDF](https://arxiv.org/pdf/2611.08338) | [Project Page](https://robertren1122.github.io/gpwm/)

<details>
<summary>Abstract</summary>

We introduce GPWM, a Generative Particle World Model that predicts how 3D scenes evolve by generating the motion of particles and rigid bodies over time. Unlike video world models that generate scene appearance, GPWM operates directly in 3D physical space. A single representation and architecture cover rigid, deformable, cloth, and granular materials, in both passive physics and robotic interaction. GPWM is an object-aware multi-resolution transformer that combines flow matching with diffusion forcing to generate coherent physical trajectories far beyond its training horizon. We train and eval...

</details>

<details>
<summary>Share</summary>

```
GPWM: Modeling the World as 3D Particle Motion

We introduce GPWM, a Generative Particle World Model that predicts how 3D scenes evolve by generating the motion of particles and rigid bodies over time.

arXiv: https://arxiv.org/abs/2611.08338
Project page: https://robertren1122.github.io/gpwm/

#worldmodels #robotics
```

</details>

---

### [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)

**Authors:** Travis Davies, Wentao Ma, Lihao Guo, Tengfei Ma, Xiaowen Chang et al. (13 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.04870) | [PDF](https://arxiv.org/pdf/2611.04870)

<details>
<summary>Abstract</summary>

A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon rollouts. We present PrimeSim, an action-conditioned, multiview world model simulator that addresses these challenges through progressive midtraining and posttraining. Starting from a pretrained video generator, we midtrain on 30,110 hours of robot demonstrations spanning 22 platforms. To improve action following, we introduce a unified cross-embodiment action representation and frame...

</details>

<details>
<summary>Share</summary>

```
PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations

A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon roll...

arXiv: https://arxiv.org/abs/2611.04870

#worldmodels #robotics
```

</details>

---

### [Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](https://arxiv.org/abs/2611.04492)

**Authors:** Jimmy Wang, Yifan Chou, Kaifeng Zhang, Yixuan Wang, Binghao Huang et al. (8 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.04492) | [PDF](https://arxiv.org/pdf/2611.04492)

<details>
<summary>Abstract</summary>

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future observations in 2D image or video space without explicitly modeling the underlying 3D scene, making spatial consistency across viewpoints and over long-horizon interactions challenging. We introduce 3D World Simulator, an action-conditioned multimodal world modeling framework that jointly predicts appearance, geometry, and tactile observations from a unified 3D representation. Our approach combines a hybrid particle-...

</details>

<details>
<summary>Share</summary>

```
Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning.

arXiv: https://arxiv.org/abs/2611.04492

#worldmodels #robotics
```

</details>

---

### [Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence](https://arxiv.org/abs/2611.04371)

**Authors:** Wenhao Xu, Changwei Wang, Shunpeng Chen, Yukun Song, Sifan Zhou et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.04371) | [PDF](https://arxiv.org/pdf/2611.04371)

<details>
<summary>Abstract</summary>

Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces. Robot learning builds physical competence, whereas AI for science chooses which experiment to run, each reporting different endpoints. This review treats their interface as one problem, embodied AI for science, where the experiment itself is partially observed: specimen state, apparatus state and measurement processes are latent, actions are costly and irreversible, and missingness depends on execution and outcome. We organize the literature by three closures oper...

</details>

<details>
<summary>Share</summary>

```
Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence

Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces.

arXiv: https://arxiv.org/abs/2611.04371

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

### [GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912)

**Authors:** Xiyan Su, Finn Rasmus Schäfer, Hojun Lim, Frank Diermeyer, Johannes Betz et al. (6 authors)

**Published:** 2026-11-05 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.07912) | [PDF](https://arxiv.org/pdf/2611.07912)

<details>
<summary>Abstract</summary>

World action models (WAMs) for autonomous driving couple the driving policy and the visual world model in a single generative network whose objectives are fixed post-training. Conditioning on a new driving objective requires retraining. We study energy guidance as a general mechanism and present GuidedWAM, a model-agnostic framework for injecting driving objectives into frozen WAMs at sampling time. Our framework constructs each objective as differentiable energies on the sampler's intermediate clean-action estimate, which needs only forward access to the frozen model, and is stabilized by sam...

</details>

<details>
<summary>Share</summary>

```
GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving

World action models (WAMs) for autonomous driving couple the driving policy and the visual world model in a single generative network whose objectives are fixed post-training.

arXiv: https://arxiv.org/abs/2611.07912

#worldmodels #robotics
```

</details>

---

### [Detecting Silent Action-Interface Mismatch with Calibrated Relational World Models](https://arxiv.org/abs/2611.06653)

**Authors:** Rui Zhu, Xurui Li, Haixu Tang

**Published:** 2026-11-04 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.06653) | [PDF](https://arxiv.org/pdf/2611.06653)

<details>
<summary>Abstract</summary>

A robot action can satisfy shape and range constraints yet carry the wrong semantics: axes may be permuted, signs inverted, rotations rescaled, or gripper polarity reversed. We study learned state-action-effect relations as offline contracts for detecting these mismatches and ranking their likely fields. Clean held-out transitions calibrate alarms; a fixed inverse vocabulary supports closed-set localization. On ten LIBERO Spatial tasks comprising 432 source episodes, a capacity-controlled comparison at 2.5% empirical clean false-positive rate gives 46.1% recall for a ridge forward residual, 61...

</details>

<details>
<summary>Share</summary>

```
Detecting Silent Action-Interface Mismatch with Calibrated Relational World Models

A robot action can satisfy shape and range constraints yet carry the wrong semantics: axes may be permuted, signs inverted, rotations rescaled, or gripper polarity reversed.

arXiv: https://arxiv.org/abs/2611.06653

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

### [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](https://arxiv.org/abs/2611.08128)

**Authors:** Zeping Zhang, Zhuoya Zhao, Samy Metari, Robert Laganière

**Published:** 2026-11-05 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.08128) | [PDF](https://arxiv.org/pdf/2611.08128)

<details>
<summary>Abstract</summary>

Current 4D occupancy world models use heavy cross-attention or deep recurrence to disentangle ego-motion from scene dynamics. This requires significant computational capacity. However, this effort is largely redundant since the ego-vehicle's intended future motion is provided by the downstream motion planner. We present FreeOcc, a lightweight continuous-time world model that introduces explicit $SE(2)$ geometric decoupling into a conditional flow-matching framework. By mathematically factoring out self-motion, we create a purely dynamic feature space. This space supports attention-free tempora...

</details>

<details>
<summary>Share</summary>

```
FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching

Current 4D occupancy world models use heavy cross-attention or deep recurrence to disentangle ego-motion from scene dynamics.

arXiv: https://arxiv.org/abs/2611.08128

#worldmodels #robotics
```

</details>

---

### [Motion-guided Contrastive Regularization For Latent World Models](https://arxiv.org/abs/2611.06901)

**Authors:** Yiwen Chen, Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Huaizu Jiang et al. (6 authors)

**Published:** 2026-11-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.06901) | [PDF](https://arxiv.org/pdf/2611.06901)

<details>
<summary>Abstract</summary>

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify static collapse, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because static content is temporally predictable yet diverse across episodes, this failure can persist despite regularizers such as SIGReg. A controlled study on OGBench-Cube shows that introducing randomized bac...

</details>

<details>
<summary>Share</summary>

```
Motion-guided Contrastive Regularization For Latent World Models

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for...

arXiv: https://arxiv.org/abs/2611.06901

#worldmodels #robotics
```

</details>

---

### [A research world model of power engineering learns its dynamics and reveals what-ifs](https://arxiv.org/abs/2611.04566)

**Authors:** Fanping Sui, Ying Zhang, Liwei Lin

**Published:** 2026-11-03 | **Categories:** cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.04566) | [PDF](https://arxiv.org/pdf/2611.04566)

<details>
<summary>Abstract</summary>

Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are taken, and existing forecasts of research fields extrapolate a single trajectory. Here we introduce research world models, which treat a research field as a dynamical system that can be acted upon, and establish one for power engineering from 1.1 million papers. A distilled language model reads each paper into role-typed concepts, two sophisticated, high-fidelity graph-temporal ne...

</details>

<details>
<summary>Share</summary>

```
A research world model of power engineering learns its dynamics and reveals what-ifs

Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are...

arXiv: https://arxiv.org/abs/2611.04566

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

### [EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748)

**Authors:** Yequan Bie, Dengyang Jiang, Zhixuan Chen, Xiaozhuan Liang, Haoxuan Che et al. (8 authors)

**Published:** 2026-11-04 (updated 2026-11-05) | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world simulator" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.06748) | [PDF](https://arxiv.org/pdf/2611.06748)

<details>
<summary>Abstract</summary>

Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve. Coherent world evolution requires more than visual fidelity: when an event occurs, a model must infer its consequences for the entities in the world and then render the resulting state. For example, after a wild beast appears, the model should not only depict the wild beast, but also infer whether a nearby person should flee, take cover, or fight back based on the realized scene. Existing diffusion-based v...

</details>

<details>
<summary>Share</summary>

```
EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models

Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve.

arXiv: https://arxiv.org/abs/2611.06748

#worldmodels #robotics
```

</details>

---
