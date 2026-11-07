# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-07 19:54 UTC

**Papers shown:** 44 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](https://arxiv.org/abs/2611.01844)

**Authors:** Dujun Nie, Ruiqi Song, Zixuan Wang, Hanqing Wang, Yifan Han et al. (9 authors)

**Published:** 2026-11-01 (updated 2026-11-05) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01844) | [PDF](https://arxiv.org/pdf/2611.01844) | [Project Page](https://openspace-lab.github.io/OpenNWM/) | [Code](https://github.com/OpenSpace-Lab/OpenNWM)

<details>
<summary>Abstract</summary>

Navigation world models predict future observations conditioned on navigation actions to support planning, but their generalization across real-world environments remains constrained by the limited coverage of action-labeled data. Action-free navigation videos provide diverse visual experience, yet lack the recorded actions required for action-conditioned training. We introduce OpenNWM, a generalist navigation world model with latent action pretraining. It learns universal latent actions from large-scale action-free videos through visual prediction pretraining, and further aligns them with phy...

</details>

<details>
<summary>Share</summary>

```
OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining

Navigation world models predict future observations conditioned on navigation actions to support planning, but their generalization across real-world environments remains constrained by the limited coverage of action-...

arXiv: https://arxiv.org/abs/2611.01844
Project page: https://openspace-lab.github.io/OpenNWM/
Code: https://github.com/OpenSpace-Lab/OpenNWM

#worldmodels #robotics
```

</details>

---

### [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730)

**Authors:** Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang

**Published:** 2026-11-05 | **Categories:** cs.GR, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

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

### [Learning Robotic World Models with Semantic and Visual Feedback](https://arxiv.org/abs/2611.07850)

**Authors:** Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

### [WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation](https://arxiv.org/abs/2611.07939)

**Authors:** Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-11-05 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

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

### [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677)

**Authors:** Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu et al. (23 authors)

**Published:** 2026-11-01 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01677) | [PDF](https://arxiv.org/pdf/2611.01677) | [Project Page](https://xiaomiautoworldmodel.github.io/CausalWorldModel/)

<details>
<summary>Abstract</summary>

We present Xiaomi Auto World Model 2.0, a unified streaming causal world model for Physical AI. It models and generates causal physical evolution in the real world, and unifies heterogeneous conditioning inputs for view-consistent generation. The architecture integrates View-Temporal Attention (VTA) to capture cross-view spatial dependencies and temporal dynamics, together with Multi-view Rotary Position Encoding (RoPE) to encode positional relationships across views and time. WorldRec 2.0 reconstructs static and dynamic 3D Gaussians from multi-view, multi-temporal observations in a single for...

</details>

<details>
<summary>Share</summary>

```
Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence

We present Xiaomi Auto World Model 2.0, a unified streaming causal world model for Physical AI.

arXiv: https://arxiv.org/abs/2611.01677
Project page: https://xiaomiautoworldmodel.github.io/CausalWorldModel/

#worldmodels #robotics
```

</details>

---

### [GPWM: Modeling the World as 3D Particle Motion](https://arxiv.org/abs/2611.08338)

**Authors:** Robert Ren, Matthew Bronars, He Zhu, Yikai Tang, Jianing Zhang et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

### [pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model](https://arxiv.org/abs/2611.01039)

**Authors:** Keivalya Pandya

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01039) | [PDF](https://arxiv.org/pdf/2611.01039) | [Code](https://github.com/keivalya/pico-wam)

<details>
<summary>Abstract</summary>

When a World Action Model fails at control, is the bottleneck proposal generation or trajectory scoring? We introduce pico-WAM, a compact model with supplied physical state for tracing policy-dynamics interactions. Using 206 Push-T demonstrations and 15 training seeds, we compare data regimes and search configurations. Counterfactual branch training improves short-horizon cost ranking and enlarges the coverage advantage of policy-restarted over warm-started search by 4.8 percentage points; restart wins under both data regimes. Replacing learned trajectory scores with simulator costs improves c...

</details>

<details>
<summary>Share</summary>

```
pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model

When a World Action Model fails at control, is the bottleneck proposal generation or trajectory scoring?

arXiv: https://arxiv.org/abs/2611.01039
Code: https://github.com/keivalya/pico-wam

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

### [Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](https://arxiv.org/abs/2611.04073)

**Authors:** Anh Nguyen, Tianyi Xu, Phat Tran, Harry Yu, Huazheng Wang et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04073) | [PDF](https://arxiv.org/pdf/2611.04073) | [Code](https://github.com/realjoenguyen/RAGPJ-official)

<details>
<summary>Abstract</summary>

Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has not been evaluated in isolation. To fill this gap, we first construct OSWorld-Tutorial and ScienceBoard-Tutorial: two datasets for CUAs with curated multimodal tutorials, covering everyday and scientific domains. We then propose RAG-PolicyJudge (RAG-PJ), a policy-judge framework for CUAs conditioned on task-specific tut...

</details>

<details>
<summary>Share</summary>

```
Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials

Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges.

arXiv: https://arxiv.org/abs/2611.04073
Code: https://github.com/realjoenguyen/RAGPJ-official

#worldmodels #robotics
```

</details>

---

### [History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models](https://arxiv.org/abs/2611.02782)

**Authors:** Hangyi Kuang, Chengzhi Wang, Yefei He, Weijie Wang, Yuke Zhao et al. (11 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.02782) | [PDF](https://arxiv.org/pdf/2611.02782) | [Project Page](https://ziplab.co/History-Forcing-Project-Page/)

<details>
<summary>Abstract</summary>

Few-step autoregressive video diffusion enables efficient generation, yet maintaining consistency over long rollouts remains challenging, especially when subjects or scenes reappear after going out of sight. Despite progress in fidelity and rollout robustness, existing distillation methods do not fully exploit richer historical information to constrain the student's current prediction. To address this gap, we introduce \textbf{History Forcing}, a unified on-policy distillation framework that strengthens historical supervision for few-step autoregressive video generators. The framework uses the...

</details>

<details>
<summary>Share</summary>

```
History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models

Few-step autoregressive video diffusion enables efficient generation, yet maintaining consistency over long rollouts remains challenging, especially when subjects or scenes reappear after going out of sight.

arXiv: https://arxiv.org/abs/2611.02782
Project page: https://ziplab.co/History-Forcing-Project-Page/

#worldmodels #robotics
```

</details>

---

### [GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912)

**Authors:** Xiyan Su, Finn Rasmus Schäfer, Hojun Lim, Frank Diermeyer, Johannes Betz et al. (6 authors)

**Published:** 2026-11-05 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [Physical Experience Builds Continual Spatial World Models](https://arxiv.org/abs/2611.04016)

**Authors:** Yuhang Sun

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.04016) | [PDF](https://arxiv.org/pdf/2611.04016)

<details>
<summary>Abstract</summary>

World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters. Continual operation faces a different problem. A familiar environment may change, and the agent must use previous experience without allowing old expectations to override current physical evidence. This study asks what repeated physical experience must contribute for a spatial world model to become progressively more useful rather than simply more persistent. A physics-grounded dynamic maze separates recurri...

</details>

<details>
<summary>Share</summary>

```
Physical Experience Builds Continual Spatial World Models

World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters.

arXiv: https://arxiv.org/abs/2611.04016

#worldmodels #robotics
```

</details>

---

### [Right Ranking, Wrong Scale: Reproducing the Robotic World Model's Dynamics Model and Testing the Uncertainty of Its Follow-up](https://arxiv.org/abs/2611.02699)

**Authors:** Joyjeet Singh

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.02699) | [PDF](https://arxiv.org/pdf/2611.02699)

<details>
<summary>Abstract</summary>

We reimplement the dynamics model of the Robotic World Model (RWM) and test the uncertainty estimate that its follow-up, RWM-U, uses to penalize reward in offline policy optimization. Our implementation matches the released model's gradients. On held-out data, training on the model's own rollouts beats one-step training at the preregistered long horizon for all ten episodes, but loses on short one-step windows. RWM-U's ensemble disagreement ranks rollout errors better than forecast step (Spearman rho = 0.90 at 100 steps), yet its spread substantially understates error: one-sigma coverage on th...

</details>

<details>
<summary>Share</summary>

```
Right Ranking, Wrong Scale: Reproducing the Robotic World Model's Dynamics Model and Testing the Uncertainty of Its Follow-up

We reimplement the dynamics model of the Robotic World Model (RWM) and test the uncertainty estimate that its follow-up, RWM-U, uses to penalize reward in offline policy optimization.

arXiv: https://arxiv.org/abs/2611.02699

#worldmodels #robotics
```

</details>

---

### [SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](https://arxiv.org/abs/2611.01600)

**Authors:** Amir Hossain Raj, Xuesu Xiao

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.01600) | [PDF](https://arxiv.org/pdf/2611.01600)

<details>
<summary>Abstract</summary>

Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space. Reactive policies often miss these hidden constraints, while exhaustive search becomes computationally prohibitive in dense clutter. We present SCOUT, an occlusion-aware planning framework that bridges high-level deliberation with grounded physical rollouts. SCOUT leverages an object-centric scene representation to reconstruct hidden geometry and derive a relational planning state capturing blocker hierarchies and accessibility cor...

</details>

<details>
<summary>Share</summary>

```
SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts

Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space.

arXiv: https://arxiv.org/abs/2611.01600

#worldmodels #robotics
```

</details>

---

### [WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation](https://arxiv.org/abs/2611.00513)

**Authors:** Jiaming Wang

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.00513) | [PDF](https://arxiv.org/pdf/2611.00513)

<details>
<summary>Abstract</summary>

Most agentic robotic systems use vision-language models (VLMs) either to orchestrate predefined skills or to directly generate actions, constraints, and control programs. The former is limited by the available skill library, while the latter requires VLMs to reason about precise geometry and contact. In this paper, we propose WorldSketch, a new paradigm for agentic robotics in which a VLM constructs a world model rather than generating robot actions. The VLM acts as an agent that actively queries perception tools to build and visually validate a minimal kinematic world model, capturing only ta...

</details>

<details>
<summary>Share</summary>

```
WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation

Most agentic robotic systems use vision-language models (VLMs) either to orchestrate predefined skills or to directly generate actions, constraints, and control programs.

arXiv: https://arxiv.org/abs/2611.00513

#worldmodels #robotics
```

</details>

---

### [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](https://arxiv.org/abs/2611.08128)

**Authors:** Zeping Zhang, Zhuoya Zhao, Samy Metari, Robert Laganière

**Published:** 2026-11-05 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [FlowBench: Counterfactual Imagination Training for Spatial Intelligence](https://arxiv.org/abs/2611.03937)

**Authors:** Yifan Liu, Baihan Zhang, Khai Loong Aw, Klemen Kotar, Daniel L. K. Yamins

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03937) | [PDF](https://arxiv.org/pdf/2611.03937) | [Code](https://github.com/liuyifan22/FlowBench)

<details>
<summary>Abstract</summary>

Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning. However, this capability remains underexplored in vision-language models and world models. We formalize this capability as Counterfactual Spatial Imagination (CSI) and introduce FlowBench, a resource for training and evaluating both, with 428K training examples spanning simulated and real-world scenes, household environments and tabletop manipulation, and diverse question types. A scalable, fully automatic pipeline pairs each hypothetical motion with spatial questions and, in...

</details>

<details>
<summary>Share</summary>

```
FlowBench: Counterfactual Imagination Training for Spatial Intelligence

Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning.

arXiv: https://arxiv.org/abs/2611.03937
Code: https://github.com/liuyifan22/FlowBench

#worldmodels #robotics
```

</details>

---

### [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](https://arxiv.org/abs/2611.01815)

**Authors:** Anton Hristov, Aleksandar Slavov, Vasil Vasilev

**Published:** 2026-11-01 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.01815) | [PDF](https://arxiv.org/pdf/2611.01815)

<details>
<summary>Abstract</summary>

Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty. We present an evaluation framework that separates what frozen representations contain, how they organize appearance and physical differences, and what changes a model's own prediction error. On IntPhys2, a benchmark of physically possible and impossible events, we compare representations from latent prediction, masked pixel reconstruction, and simple visual statistics. Appearance remains easy to decode, while V-JEPA2...

</details>

<details>
<summary>Share</summary>

```
When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?

Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty.

arXiv: https://arxiv.org/abs/2611.01815

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

### [Toward Uncertainty-Aware, Physics-Grounded Human World Models](https://arxiv.org/abs/2611.03428)

**Authors:** Yufei Zhang, Zijun Cui

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.03428) | [PDF](https://arxiv.org/pdf/2611.03428)

<details>
<summary>Abstract</summary>

A robot that acts around people needs a world model of the human: a belief over the person's body state and a dynamics model that predicts where that state goes next. This abstract argues that two published components form exactly these two halves, and specifies how to couple them. KNOWN [1] reconstructs the 3D human body while estimating both aleatoric and epistemic uncertainty in real time (11.6 ms per frame); its aleatoric term identifies unreliable observations, its epistemic term identifies inputs from low-density regions of the training data, and refinement driven by the epistemic term r...

</details>

<details>
<summary>Share</summary>

```
Toward Uncertainty-Aware, Physics-Grounded Human World Models

A robot that acts around people needs a world model of the human: a belief over the person's body state and a dynamics model that predicts where that state goes next.

arXiv: https://arxiv.org/abs/2611.03428

#worldmodels #robotics
```

</details>

---

### [Roz: A Taste Test for World Model Latents](https://arxiv.org/abs/2611.00612)

**Authors:** Kenneth Ge, Dhruv Sheth, Kunvar Thaman

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.00612) | [PDF](https://arxiv.org/pdf/2611.00612)

<details>
<summary>Abstract</summary>

State of the art latent dynamics world models achieve impressive performance for robot planning. But do they actually encode the physics of the world? In this paper, we show that popular world models today achieve strong results on tasks that reduce to image similarity but forget key details about objects in the scene like mass, deformation, friction, and bounciness. We achieve this by defining precisely what ought to be encoded in such a world model and introducing two new evaluation methods that can directly tease physical properties and easily scale to new ones. Our evaluation, which we cal...

</details>

<details>
<summary>Share</summary>

```
Roz: A Taste Test for World Model Latents

State of the art latent dynamics world models achieve impressive performance for robot planning.

arXiv: https://arxiv.org/abs/2611.00612

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

### [Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028)

**Authors:** Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Kaiwen Geng et al. (8 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.04028) | [PDF](https://arxiv.org/pdf/2611.04028)

<details>
<summary>Abstract</summary>

Effective world modeling requires compressing salient history information that facilitates future prediction. However, most existing approaches inherit tokenization and conditioning mechanisms from video generation, where objectives are centered around perceptual realism rather than predictive utility. This discrepancy limits the world model's effectiveness, especially in environments dominated by visual nuisances or task-irrelevant background details. To this end, we introduce Compression Forcing (CF), a general framework that aligns history compression with the predictive objective of world...

</details>

<details>
<summary>Share</summary>

```
Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models

Effective world modeling requires compressing salient history information that facilitates future prediction.

arXiv: https://arxiv.org/abs/2611.04028

#worldmodels #robotics
```

</details>

---

### [INTERACT: Learning Interaction-Aware World Dynamics from Driving Videos for Autonomous Driving](https://arxiv.org/abs/2611.02526)

**Authors:** Zhan Chen, Songyan Zhang, Wenhui Huang, Zirui Li, Zhidong Wang et al. (8 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.02526) | [PDF](https://arxiv.org/pdf/2611.02526)

<details>
<summary>Abstract</summary>

Safe autonomous driving requires more than recognizing the current scene: the ego vehicle must anticipate how surrounding traffic participants will evolve under its own motion. However, existing end-to-end driving models typically encode scenes into dense visual or BEV features, leaving object-level interactions implicit. We propose (INTERACT INTERaction-aware Action-Conditioned Trajectory learning), a three-stage framework that learns a slot-based object-centric world model from unlabeled driving videos and transfers it to trajectory planning. INTERACT first learns recurrent slots that group...

</details>

<details>
<summary>Share</summary>

```
INTERACT: Learning Interaction-Aware World Dynamics from Driving Videos for Autonomous Driving

Safe autonomous driving requires more than recognizing the current scene: the ego vehicle must anticipate how surrounding traffic participants will evolve under its own motion.

arXiv: https://arxiv.org/abs/2611.02526

#worldmodels #robotics
```

</details>

---

### [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341)

**Authors:** Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun, Haitian Zheng et al. (10 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.02341) | [PDF](https://arxiv.org/pdf/2611.02341)

<details>
<summary>Abstract</summary>

Recent interactive video world models generate visually compelling videos from a single image, following user-provided camera motion and text prompts. However, such low-level control demands substantial user effort to realize a high-level intent, and the generated world struggles to remain persistent as the exploration proceeds. In this work, we present AgiWorld, an agentic video world model that explores and builds a persistent world from a single image and a free-form instruction. For high-level planning, our agent AgiWorld-Agent designs the world and the journey through it in a world state...

</details>

<details>
<summary>Share</summary>

```
AgiWorld: An Agentic Video World Model for Building Persistent Worlds

Recent interactive video world models generate visually compelling videos from a single image, following user-provided camera motion and text prompts.

arXiv: https://arxiv.org/abs/2611.02341

#worldmodels #robotics
```

</details>

---

### [Stand-In Effects and Pooling Amplification: Design-Based Tests of Whether Biological World Models Use Actions](https://arxiv.org/abs/2611.01666)

**Authors:** Bowen Xu, Boyu Chen

**Published:** 2026-11-01 | **Categories:** cs.LG, q-bio.QM, stat.ME | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.01666) | [PDF](https://arxiv.org/pdf/2611.01666)

<details>
<summary>Abstract</summary>

Action-conditioned world models are increasingly trained on data from randomized experiments, and whether their predictions respond to actions is usually checked by replacing or removing the actions and measuring the loss in accuracy. We show that such diagnostics report action effects where there are none: under autocorrelated designs, future actions stand in for history the model does not see, and a better model learns the stand-in better. When the design law is known, a conditional randomization test written as an e-value is valid in finite samples whatever the model, provided the resampler...

</details>

<details>
<summary>Share</summary>

```
Stand-In Effects and Pooling Amplification: Design-Based Tests of Whether Biological World Models Use Actions

Action-conditioned world models are increasingly trained on data from randomized experiments, and whether their predictions respond to actions is usually checked by replacing or removing the actions and measuring the...

arXiv: https://arxiv.org/abs/2611.01666

#worldmodels #robotics
```

</details>

---

### [World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits](https://arxiv.org/abs/2611.01139)

**Authors:** Ahanaf Hasan Ariq, Hasaan Ahmad

**Published:** 2026-10-31 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.01139) | [PDF](https://arxiv.org/pdf/2611.01139)

<details>
<summary>Abstract</summary>

Selecting a reinforcement-learning (RL) policy usually requires additional environment interaction, while learned world models offer cheap but potentially biased evaluations. This raises two distinct questions: can shared model errors preserve pairwise rankings despite poor absolute values, and do they make a small number of real audits more informative? We derive an exact pairwise simulation identity and a relative bound separating common-mode Bellman residuals from policy-specific error. The analysis motivates RAVEL (Relative Auditing of Value Errors in Learned models), a selective policy to...

</details>

<details>
<summary>Share</summary>

```
World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits

Selecting a reinforcement-learning (RL) policy usually requires additional environment interaction, while learned world models offer cheap but potentially biased evaluations.

arXiv: https://arxiv.org/abs/2611.01139

#worldmodels #robotics
```

</details>

---

### [X-World 1.6: Building Controllable Virtual Cities with World Models](https://arxiv.org/abs/2611.00596)

**Authors:** XPeng, :, Boyang Wang, Boyi Sun, Chaoda Zheng et al. (36 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.00596) | [PDF](https://arxiv.org/pdf/2611.00596)

<details>
<summary>Abstract</summary>

Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions. This report presents \emph{X-World~1.6}, advancing X-World~1.0 toward a more reliable and versatile driving simulator. The upgraded base model offers finer-grained control over traffic semantics, including traffic lights and road markings, together with improved spatial consistency across cameras. Virtual City capabilities broaden scenario construction through a family of models con...

</details>

<details>
<summary>Share</summary>

```
X-World 1.6: Building Controllable Virtual Cities with World Models

Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions.

arXiv: https://arxiv.org/abs/2611.00596

#worldmodels #robotics
```

</details>

---

### [An intelligent satellite must do nothing well](https://arxiv.org/abs/2611.02922)

**Authors:** Fabrizio Pilone, Giordana Bucchioni

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.02922) | [PDF](https://arxiv.org/pdf/2611.02922)

<details>
<summary>Abstract</summary>

Autonomous inspection of a resident space object is usually posed as a contest between classical next-best-view planning and reinforcement learning. We argue that the choice of algorithm is the least informative of the design axes. An inspector spacecraft has no rest state: when it stops thrusting, orbital dynamics carry it along a natural trajectory that can be used to observe the target at no fuel cost. On a controlled ladder in which one design axis is varied at a time, fuel efficiency turns out to be set by three things: whether the agent is allowed to drift, whether its state records wher...

</details>

<details>
<summary>Share</summary>

```
An intelligent satellite must do nothing well

Autonomous inspection of a resident space object is usually posed as a contest between classical next-best-view planning and reinforcement learning.

arXiv: https://arxiv.org/abs/2611.02922

#worldmodels #robotics
```

</details>

---

### [Beyond Ensemble Disagreement: Predictive STL Monitoring of RL Locomotion under Distribution Shift](https://arxiv.org/abs/2611.02218)

**Authors:** Qurban Ali, Badaruddin Chachar, Maqsood Ali, Sajjad Ali Rajper

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.02218) | [PDF](https://arxiv.org/pdf/2611.02218)

<details>
<summary>Abstract</summary>

RL locomotion policies trained under nominal simulation conditions may encounter distribution shifts that compromise safety. Predictive monitors could anticipate violations, but their world-model forecasts may become unreliable under shift, and ensemble disagreement is not calibrated. We evaluate predictive Signal Temporal Logic (STL) monitoring for frozen Ant-v5 and HalfCheetah-v5 policies using closed-loop world-model rollouts and a three-model ensemble. Across external-force, observation-noise, and mass shifts, predicted robustness ranks HalfCheetah's future STL violations strongly, whereas...

</details>

<details>
<summary>Share</summary>

```
Beyond Ensemble Disagreement: Predictive STL Monitoring of RL Locomotion under Distribution Shift

RL locomotion policies trained under nominal simulation conditions may encounter distribution shifts that compromise safety.

arXiv: https://arxiv.org/abs/2611.02218

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

### [Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data](https://arxiv.org/abs/2611.03626)

**Authors:** Rafal Karp, Gene Liu, Shih-Hsin Li, Eric Courtemanche, Shengze Wang et al. (13 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.03626) | [PDF](https://arxiv.org/pdf/2611.03626)

<details>
<summary>Abstract</summary>

We present Isekai3D Synthetic Data Generation (SDG), a platform for simulating and capturing synthetic 3D gameplay for research in vision and world models, neural graphics, gameplay agents, and other applications. The platform combines reusable environment and character assets with Unreal Engine plugins in a two-stage workflow. First, world simulation generates gameplay while recording the world state, character movements, actions, and camera tracks needed for replay. Second, the recorded simulation is replayed to capture selected outputs, such as rendered video, images, and depth maps, at a s...

</details>

<details>
<summary>Share</summary>

```
Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data

We present Isekai3D Synthetic Data Generation (SDG), a platform for simulating and capturing synthetic 3D gameplay for research in vision and world models, neural graphics, gameplay agents, and other applications.

arXiv: https://arxiv.org/abs/2611.03626

#worldmodels #robotics
```

</details>

---

### [Predictive Safety Guardrails Do Not Always Make LLM Agents Safer](https://arxiv.org/abs/2611.02815)

**Authors:** Weixiang Zhao, Zhihao Liu, Guancheng Li, Yanyan Zhao, Bing Qin et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.02815) | [PDF](https://arxiv.org/pdf/2611.02815)

<details>
<summary>Abstract</summary>

Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps. This has motivated world-model-driven predictive safety guardrails, which anticipate future consequences before execution. However, existing evaluations largely focus on end-to-end safety outcomes, leaving unclear whether safety gains arise from reliable prediction and faithful use of predicted risks. In this work, we systematically diagnose the prediction-to-action pipeline along three dimensions: how world-model predict...

</details>

<details>
<summary>Share</summary>

```
Predictive Safety Guardrails Do Not Always Make LLM Agents Safer

Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps.

arXiv: https://arxiv.org/abs/2611.02815

#worldmodels #robotics
```

</details>

---

### [GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](https://arxiv.org/abs/2611.01001)

**Authors:** Allan Grosvenor, Anton Zemlyansky, Abdul Wahab, Kyrylo Bohachov, Aras Dogan et al. (7 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI, cs.CE, cs.MA | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.01001) | [PDF](https://arxiv.org/pdf/2611.01001)

<details>
<summary>Abstract</summary>

An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose, rank, and accelerate; a symbolic rules engine checks every consequential action against hard limits before it executes; and validated physics confirms and decides. GURU runs a workflow as a closed control loop, with Navigation, Action, and Planning agents sharing one Common Internal Language and one training factory....

</details>

<details>
<summary>Share</summary>

```
GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations

An AI can find a safe action faster than any human, but it must never decide what counts as safe.

arXiv: https://arxiv.org/abs/2611.01001

#worldmodels #robotics
```

</details>

---
