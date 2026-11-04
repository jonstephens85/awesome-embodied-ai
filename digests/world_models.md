# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-11-04 21:43 UTC

**Papers shown:** 60 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](https://arxiv.org/abs/2611.01844)

**Authors:** Dujun Nie, Ruiqi Song, Zixuan Wang, Hanqing Wang, Yifan Han et al. (9 authors)

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

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

### [Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving](https://arxiv.org/abs/2611.05072)

**Authors:** Junzhe Wang, Jinqing Zhang, Qingjie Liu

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232)

**Authors:** Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li et al. (8 authors)

**Published:** 2026-10-29 (updated 2026-10-30) | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39232) | [PDF](https://arxiv.org/pdf/2610.39232) | [Project Page](https://gensight-rbs.github.io/)

<details>
<summary>Abstract</summary>

Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world. We present GenSight, a unified embodied world model that brings future video generation and dense perception into a single pretrained video diffusion transformer. GenSight uses a unified spatiotemporal representation for video, depth, embodiment segmentation, and first-frame-relative 2D flow. Built on a shared DiT backbone, GenSight uses lightweight task modulation to predict all modalities within the same architecture. All tasks are jointly op...

</details>

<details>
<summary>Share</summary>

```
Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling

Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world.

arXiv: https://arxiv.org/abs/2610.39232
Project page: https://gensight-rbs.github.io/

#worldmodels #robotics
```

</details>

---

### [Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](https://arxiv.org/abs/2611.04073)

**Authors:** Anh Nguyen, Tianyi Xu, Phat Tran, Harry Yu, Huazheng Wang et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

### [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)

**Authors:** Travis Davies, Wentao Ma, Lihao Guo, Tengfei Ma, Xiaowen Chang et al. (13 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](https://arxiv.org/abs/2611.00455)

**Authors:** Jiaxin Shi, Zibin Wu, Yichi Zhang, Jianghua Duan, Siyu Zhu et al. (6 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.00455) | [PDF](https://arxiv.org/pdf/2611.00455) | [Project Page](https://tacmind-bench.github.io/)

<details>
<summary>Abstract</summary>

Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipulation. However, existing tactile manipulation studies are often developed and evaluated within specific task settings, making it difficult to systematically compare how tactile information contributes under different interaction conditions. In this work, we develop a benchmark in simulation comprising 128 tasks organized around three complementary evaluation regimes: Precise, Recognition, and Dynamic. The benchmark f...

</details>

<details>
<summary>Share</summary>

```
TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation

Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.00455
Project page: https://tacmind-bench.github.io/

#worldmodels #robotics
```

</details>

---

### [Hierarchical World Models with Implicit Dynamics](https://arxiv.org/abs/2610.42146)

**Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran et al. (7 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.42146) | [PDF](https://arxiv.org/pdf/2610.42146) | [Project Page](https://id-wm.github.io)

<details>
<summary>Abstract</summary>

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from local control. Our framework utilizes a high-level model to sample feasible transitions across the st...

</details>

<details>
<summary>Share</summary>

```
Hierarchical World Models with Implicit Dynamics

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning.

arXiv: https://arxiv.org/abs/2610.42146
Project page: https://id-wm.github.io

#worldmodels #robotics
```

</details>

---

### [PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528)

**Authors:** Huabin Peng, Fagang Jin, Yancong Wei, Tengfei Ma, Chuhang Liu et al. (7 authors)

**Published:** 2026-10-29 (updated 2026-11-03) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.39528) | [PDF](https://arxiv.org/pdf/2610.39528)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel at instruction following, yet most remain feed-forward: they condition actions only on the current observation and discard both long-horizon temporal context and the hierarchical structure of VLM representations. We present PRIME W0, a hierarchical conditional flow-matching framework that closes this gap through three synergistic designs: (1)per-layer KV injection from a pretrained VLM into an Adaptive MoE action expert; (2)dynamics-aware conditioning via asynchronous world-model subgoal-image prediction and a DINOv2 historical-frame semantic bridge; a...

</details>

<details>
<summary>Share</summary>

```
PRIME W0: Physical Priors from World Models for Embodied Manipulation

Vision-Language-Action (VLA) models excel at instruction following, yet most remain feed-forward: they condition actions only on the current observation and discard both long-horizon temporal context and the hierarchi...

arXiv: https://arxiv.org/abs/2610.39528

#worldmodels #robotics
```

</details>

---

### [Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence](https://arxiv.org/abs/2611.04371)

**Authors:** Wenhao Xu, Changwei Wang, Shunpeng Chen, Yukun Song, Sifan Zhou et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

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

### [Fight World Model: Customizable Combat through Visual Interaction Proxies](https://arxiv.org/abs/2610.40607)

**Authors:** Jiahua Li, Zixu John, Tom Zhong, Fuping Wu, Tianhao Xu et al. (8 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40607) | [PDF](https://arxiv.org/pdf/2610.40607) | [Project Page](https://fight-world-model.github.io)

<details>
<summary>Abstract</summary>

A playable, programmable game world must maintain persistent state, enforce executable rules, and support extensible gameplay mechanics. Existing video world models can generate plausible combat, yet struggle to keep hit reactions and health updates consistent with game rules. We introduce Fight World Model (FWM), which separates rule-governed combat execution from video rendering. An executable engine maintains state and resolves interactions. A deterministic compiler encodes these outcomes and attempted actions in a spatially and temporally aligned interaction proxy. The proxy aligns action...

</details>

<details>
<summary>Share</summary>

```
Fight World Model: Customizable Combat through Visual Interaction Proxies

A playable, programmable game world must maintain persistent state, enforce executable rules, and support extensible gameplay mechanics.

arXiv: https://arxiv.org/abs/2610.40607
Project page: https://fight-world-model.github.io

#worldmodels #robotics
```

</details>

---

### [Algebraic World Model: From Exploration to Proofs](https://arxiv.org/abs/2610.40503)

**Authors:** Guancheng Pan, Qixin Tan, Yang Yuan, Andrew Chi-Chih Yao

**Published:** 2026-10-29 (updated 2026-10-30) | **Categories:** cs.AI, cs.LO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40503) | [PDF](https://arxiv.org/pdf/2610.40503) | [Project Page](https://ephemeral6.github.io/awm-site/)

<details>
<summary>Abstract</summary>

AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit mathematical models supporting formal reasoning. AWM explores the environment and develops executable Python hypotheses, continually testing and revising them against observations. It then st...

</details>

<details>
<summary>Share</summary>

```
Algebraic World Model: From Exploration to Proofs

AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications.

arXiv: https://arxiv.org/abs/2610.40503
Project page: https://ephemeral6.github.io/awm-site/

#worldmodels #robotics
```

</details>

---

### [Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191)

**Authors:** Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu et al. (21 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40191) | [PDF](https://arxiv.org/pdf/2610.40191) | [Project Page](https://agentic-videogen.github.io/)

<details>
<summary>Abstract</summary>

Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context, exposes tools, maintains state, routes feedback, and manages budgets around video models. This report examines three directions. First, agentic video generation, where harnesses coordin...

</details>

<details>
<summary>Share</summary>

```
Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement

Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos.

arXiv: https://arxiv.org/abs/2610.40191
Project page: https://agentic-videogen.github.io/

#worldmodels #robotics
```

</details>

---

### [Toward Uncertainty-Aware, Physics-Grounded Human World Models](https://arxiv.org/abs/2611.03428)

**Authors:** Yufei Zhang, Zijun Cui

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

### [Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics](https://arxiv.org/abs/2610.41330)

**Authors:** Zhidong Wang, Zirui Li, Haoran Xu, Yujie Yan, Zitong Shan et al. (8 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.41330) | [PDF](https://arxiv.org/pdf/2610.41330)

<details>
<summary>Abstract</summary>

Motion planning in clutter is embodiment-specific: the feasible free space and reachable commands depend on each robot's geometry and dynamics. Existing cross-embodiment policies output normalized commands that disregard these differences, or compensate through per-robot training and distillation. World models can in principle pool cross-embodiment data, yet command-conditioned models bind their latent dynamics to a single action space, while pose-conditioned models omit the mapping from commands to body-specific motion. On flat ground, however, embodiment affects the planner's observations on...

</details>

<details>
<summary>Share</summary>

```
Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics

Motion planning in clutter is embodiment-specific: the feasible free space and reachable commands depend on each robot's geometry and dynamics.

arXiv: https://arxiv.org/abs/2610.41330

#worldmodels #robotics
```

</details>

---

### [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)

**Authors:** Yuhao Lu, Jiongxu Chen, Hexiang Wei, Jiajin Wu, Juelin Li et al. (12 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39278) | [PDF](https://arxiv.org/pdf/2610.39278) | [Project Page](https://worldflow-rbs.github.io/)

<details>
<summary>Abstract</summary>

Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce \method{}, a generative world model that jointly predicts future video and query-based 3D trajectories. By parameterizing 3D motion as continuous displacement tokens aligned with the video grid, a unified Mixture-of-Tr...

</details>

<details>
<summary>Share</summary>

```
WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining

Predicting future physical states stands as a central challenge in embodied intelligence.

arXiv: https://arxiv.org/abs/2610.39278
Project page: https://worldflow-rbs.github.io/

#worldmodels #robotics
```

</details>

---

### [Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation](https://arxiv.org/abs/2610.38657)

**Authors:** Jacob Levy, Arthur Bouton, Tristan D. Hassler, Hari Nayar, David Fridovich-Keil

**Published:** 2026-10-28 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.38657) | [PDF](https://arxiv.org/pdf/2610.38657) | [Project Page](https://terra-explore.github.io)

<details>
<summary>Abstract</summary>

Future planetary rovers will traverse steep, deformable terrain where slip, sinkage, and terrain deformation can threaten mobility. Although simulation can capture some wheel-soil effects, unmodeled deformable-terrain phenomena create sim-to-real gaps requiring deployment-time adaptation. Yet, rover operations leave little room for extensive trial-and-error. We introduce TERRA (Targeted Exploration for Reward-Relevant Adaptation), an online adaptation framework that efficiently seeks deployment data exposing task-relevant model errors and corrects them. TERRA adapts a simulation-trained world...

</details>

<details>
<summary>Share</summary>

```
Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation

Future planetary rovers will traverse steep, deformable terrain where slip, sinkage, and terrain deformation can threaten mobility.

arXiv: https://arxiv.org/abs/2610.38657
Project page: https://terra-explore.github.io

#worldmodels #robotics
```

</details>

---

### [A research world model of power engineering learns its dynamics and reveals what-ifs](https://arxiv.org/abs/2611.04566)

**Authors:** Fanping Sui, Ying Zhang, Liwei Lin

**Published:** 2026-11-03 | **Categories:** cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

### [Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339)

**Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40339) | [PDF](https://arxiv.org/pdf/2610.40339) | [Project Page](https://wyzardwu.github.io/wizard)

<details>
<summary>Abstract</summary>

Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined motion patterns, generalize poorly to unseen environments and characters, and offer limited real-time interactivity. In this paper, we introduce Wizard, an agentic game world model that...

</details>

<details>
<summary>Share</summary>

```
Wizard: Manipulate Any World in Real Time via Agentic Control

Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay.

arXiv: https://arxiv.org/abs/2610.40339
Project page: https://wyzardwu.github.io/wizard

#worldmodels #robotics
```

</details>

---

### [Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information](https://arxiv.org/abs/2610.40030)

**Authors:** Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll

**Published:** 2026-10-29 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40030) | [PDF](https://arxiv.org/pdf/2610.40030) | [Project Page](https://corl2026-memory.github.io/)

<details>
<summary>Abstract</summary>

Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model. We obtain that, when read at the observation, it yields a provable lower bound on the optimal value of the acquiring action, which floors its TD target and attributes this floor to t...

</details>

<details>
<summary>Share</summary>

```
Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information

Memory in reinforcement learning raises two problems.

arXiv: https://arxiv.org/abs/2610.40030
Project page: https://corl2026-memory.github.io/

#worldmodels #robotics
```

</details>

---

### [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](https://arxiv.org/abs/2610.39619)

**Authors:** Guangyuan Li, Kelu Yao, Shuolin Xu, Xinlei Yu, Wei Xing et al. (9 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39619) | [PDF](https://arxiv.org/pdf/2610.39619) | [Project Page](https://GuangYuanKK.github.io/futureworld)

<details>
<summary>Abstract</summary>

Interactive video world models aim to follow user actions while maintaining scene consistency over extended interactions. History-based methods reuse generated latents to preserve scene content, but three limitations of this reuse contribute to error recirculation. 1) The latent generated at each interaction is retained as history, potentially containing blurred details, geometric distortions, or semantic drift. 2) Although retrieved historical content matches the current scene, it can still contain errors that are carried into the next chunk. 3) New outputs then become history for later inter...

</details>

<details>
<summary>Share</summary>

```
FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration

Interactive video world models aim to follow user actions while maintaining scene consistency over extended interactions.

arXiv: https://arxiv.org/abs/2610.39619
Project page: https://GuangYuanKK.github.io/futureworld

#worldmodels #robotics
```

</details>

---

### [An intelligent satellite must do nothing well](https://arxiv.org/abs/2611.02922)

**Authors:** Fabrizio Pilone, Giordana Bucchioni

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation](https://arxiv.org/abs/2610.41654)

**Authors:** Weyl Lu, Yubei Chen

**Published:** 2026-10-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.41654) | [PDF](https://arxiv.org/pdf/2610.41654)

<details>
<summary>Abstract</summary>

Robot policy learning is dominated by zeroth-order methods such as PPO, which treat the simulator as a black box and pay for it with enormous sample counts. First-order policy learning differentiates through the dynamics, but on contact-rich whole-body control it has rarely worked: its gradients explode. A recent world-model method showed that derivative information can make humanoid motion tracking far more efficient, using surrogate gradients of a learned model. We show that exact gradients of the simulator itself do better, once two obstacles are removed. Exact gradients contain rare unboun...

</details>

<details>
<summary>Share</summary>

```
$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation

Robot policy learning is dominated by zeroth-order methods such as PPO, which treat the simulator as a black box and pay for it with enormous sample counts.

arXiv: https://arxiv.org/abs/2610.41654

#worldmodels #robotics
```

</details>

---

### [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](https://arxiv.org/abs/2610.40401)

**Authors:** Liangyu Li, Qingwen Liu

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.40401) | [PDF](https://arxiv.org/pdf/2610.40401)

<details>
<summary>Abstract</summary>

We introduce Continuous-Action World Models (CoAWM), a framework for learning cross-embodiment spatiotemporal dynamics priors that support robot action generation across embodiments and execution frequencies. At its core is a shared latent function space that captures the spatial and temporal structure of robot actions. We learn this space through two stages. First, function pretraining brings trajectories from different embodiments and sampling frequencies into a common representation, learning shared dynamics priors through action reconstruction and consistency across temporal sampling views...

</details>

<details>
<summary>Share</summary>

```
Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors

We introduce Continuous-Action World Models (CoAWM), a framework for learning cross-embodiment spatiotemporal dynamics priors that support robot action generation across embodiments and execution frequencies.

arXiv: https://arxiv.org/abs/2610.40401

#worldmodels #robotics
```

</details>

---

### [Assuring Learning-Enabled Cyber-Physical Systems with Foundation Models: A Neuro-Symbolic Agenda for Testing, Verification, and Runtime Assurance](https://arxiv.org/abs/2610.39547)

**Authors:** Xi Zheng, Ivan Ruchkin, Hong Jin Kang, Tevfik Bultan, Vijay Ganesh et al. (14 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.39547) | [PDF](https://arxiv.org/pdf/2610.39547)

<details>
<summary>Abstract</summary>

Learning-enabled cyber-physical systems (CPS), including autonomous vehicles and UAVs, increasingly incorporate foundation models, yet fragmented assurance practices provide insufficient support for system-level guarantees. We argue that restoring engineering control across stochastic neural, symbolic, and physical boundaries requires a shift from model-centric evaluation to system-level assurance. We introduce the Foundation Model Assurance Stack, connecting three directions: (i) neuro-symbolic architectures that constrain foundation models through explicit symbolic world models, reasoning la...

</details>

<details>
<summary>Share</summary>

```
Assuring Learning-Enabled Cyber-Physical Systems with Foundation Models: A Neuro-Symbolic Agenda for Testing, Verification, and Runtime Assurance

Learning-enabled cyber-physical systems (CPS), including autonomous vehicles and UAVs, increasingly incorporate foundation models, yet fragmented assurance practices provide insufficient support for system-level guara...

arXiv: https://arxiv.org/abs/2610.39547

#worldmodels #robotics
```

</details>

---

### [Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation](https://arxiv.org/abs/2610.38266)

**Authors:** Xiaofeng Han, Kaize Luo, Zenghuang Fu, Zichong Zhu, Zhe Feng et al. (9 authors)

**Published:** 2026-10-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.38266) | [PDF](https://arxiv.org/pdf/2610.38266)

<details>
<summary>Abstract</summary>

Embodied systems can update policies, world models, skills, and executable programs from deployment experience, allowing one interaction to benefit later tasks. When a system also revises and reuses its data-acquisition, feedback, or learning procedures, experience changes the process that produces capability, introducing recursive self-improvement. This paper surveys research in physical AI through the connection between persistent capability and its improvement process. We first explain the functional distinction between learner updates and improvers, then compare policy learning, imagined e...

</details>

<details>
<summary>Share</summary>

```
Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation

Embodied systems can update policies, world models, skills, and executable programs from deployment experience, allowing one interaction to benefit later tasks.

arXiv: https://arxiv.org/abs/2610.38266

#worldmodels #robotics
```

</details>

---

### [Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data](https://arxiv.org/abs/2611.03626)

**Authors:** Rafal Karp, Gene Liu, Shih-Hsin Li, Eric Courtemanche, Shengze Wang et al. (13 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

**Published:** 2026-11-02 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel](https://arxiv.org/abs/2611.00427)

**Authors:** Kunal Bhosikar, Nicole Meng, Charu Sharma, Yingjie Lao

**Published:** 2026-10-30 | **Categories:** cs.CV, cs.CR, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.00427) | [PDF](https://arxiv.org/pdf/2611.00427)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) have recently emerged as general-purpose visual world models for control. A prominent example is LeWorldModel (LeWM), which trains end-to-end from pixels using an isotropic Gaussian anti-collapse regularizer (SIGReg) and plans by minimizing the squared Euclidean distance between predicted and goal embeddings. In this work, we investigate the test-time robustness of this latent planning interface. Analyzing the learned metric on Push-T, we first find that task-relevant object state heavily dominates latent distance: shifting the block by a single...

</details>

<details>
<summary>Share</summary>

```
Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel

Joint-embedding predictive architectures (JEPAs) have recently emerged as general-purpose visual world models for control.

arXiv: https://arxiv.org/abs/2611.00427

#worldmodels #robotics
```

</details>

---

### [SPT-Flow: One Integration, Many Futures in Continuous-Time World Models](https://arxiv.org/abs/2610.41273)

**Authors:** Mingyang Lyu, Yinqian Sun, Gongce Cao, Yuhao Zhang, Lu Jia et al. (8 authors)

**Published:** 2026-10-30 (updated 2026-11-02) | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.41273) | [PDF](https://arxiv.org/pdf/2610.41273)

<details>
<summary>Abstract</summary>

Continuous-time world models generate a latent trajectory through a single ODE integration, but adding stochastic conditioning does not ensure that the model uses it. In our teacher-forced baseline, posterior means vary by only about 1% of the prior scale, and matched and swapped latents yield indistinguishable reconstruction PSNR at the reported precision. We study a supervision-shortcut hypothesis: ground-truth intermediate states can reduce the need for trajectory-associated latent information. We introduce SPT-Flow, which samples one latent per trajectory and matches a free-running ODE rol...

</details>

<details>
<summary>Share</summary>

```
SPT-Flow: One Integration, Many Futures in Continuous-Time World Models

Continuous-time world models generate a latent trajectory through a single ODE integration, but adding stochastic conditioning does not ensure that the model uses it.

arXiv: https://arxiv.org/abs/2610.41273

#worldmodels #robotics
```

</details>

---

### [One Verdict Is Not Enough: Regression Testing Learned World Models and Their Test Harnesses](https://arxiv.org/abs/2610.41130)

**Authors:** Junyu Huo, Zihao Wan, Ziqi Mao, Gouri Ginde

**Published:** 2026-10-30 | **Categories:** cs.SE, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.41130) | [PDF](https://arxiv.org/pdf/2610.41130)

<details>
<summary>Abstract</summary>

Learned world models ship as software components whose model versions, preprocessing, and test harnesses change between releases. Work on model updates already counts per-sample regressions, or negative flips, that an accuracy check hides. Two problems remain: a test can pass under one configuration and fail under another, and a harness fault can produce erroneous scores and wrong verdicts without a crash. We present TetraState, a regression-testing protocol for paired possible/impossible video tests. Each test runs under four fixed model-native configurations; its number of correct verdicts a...

</details>

<details>
<summary>Share</summary>

```
One Verdict Is Not Enough: Regression Testing Learned World Models and Their Test Harnesses

Learned world models ship as software components whose model versions, preprocessing, and test harnesses change between releases.

arXiv: https://arxiv.org/abs/2610.41130

#worldmodels #robotics
```

</details>

---

### [Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models](https://arxiv.org/abs/2610.41041)

**Authors:** Amir Mesbah, Di Wu

**Published:** 2026-10-29 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.41041) | [PDF](https://arxiv.org/pdf/2610.41041)

<details>
<summary>Abstract</summary>

Continual reinforcement learning (CRL) requires agents to operate under environmental changes while reusing prior knowledge whenever possible. We argue that model-based reinforcement learning provides a promising framework for this setting because learned world models (WMs) can, in principle, support change detection, knowledge reuse, adaptation, and acquisition of new knowledge. However, such benefits depend heavily on whether the learned model can generalize beyond the contexts in which it was trained. In this work, we propose to formulate this problem with a contextual Markov decision proce...

</details>

<details>
<summary>Share</summary>

```
Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models

Continual reinforcement learning (CRL) requires agents to operate under environmental changes while reusing prior knowledge whenever possible.

arXiv: https://arxiv.org/abs/2610.41041

#worldmodels #robotics
```

</details>

---

### [Dreams Are Cheaper Than Flights: Curated World-Model Data Improves Aerial Detection](https://arxiv.org/abs/2610.41030)

**Authors:** Rugved Katole, Vedant Patil, Jenna Kline, Christopher Stewart

**Published:** 2026-10-29 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.41030) | [PDF](https://arxiv.org/pdf/2610.41030)

<details>
<summary>Abstract</summary>

Robot perception is increasingly data driven, yet field data is slow, costly, and sometimes disruptive to collect. Video world models offer a cheaper source: seeded with real frames, they extend a recorded scene into new footage with the deployment's sensor, altitude, and environment. We ask whether such synthetic data matches the utility of real field data and whether detectors trained with it perform in the field. Seeding a 7B-parameter world model with wildlife drone video, we more than double the training set with curated frames. On held-out videos from the same drones, mAP@50--95 rises 4....

</details>

<details>
<summary>Share</summary>

```
Dreams Are Cheaper Than Flights: Curated World-Model Data Improves Aerial Detection

Robot perception is increasingly data driven, yet field data is slow, costly, and sometimes disruptive to collect.

arXiv: https://arxiv.org/abs/2610.41030

#worldmodels #robotics
```

</details>

---

### [Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning](https://arxiv.org/abs/2610.41022)

**Authors:** Shashank Gupta, Pilhwa Lee

**Published:** 2026-10-29 | **Categories:** cs.LG, stat.ML | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.41022) | [PDF](https://arxiv.org/pdf/2610.41022)

<details>
<summary>Abstract</summary>

Latent world models allow reinforcement learning agents to learn policies from imagined trajectories, yet determining the optimal depth of model reliance remains a fundamental challenge. Fixed imagination horizons apply uniform prediction depths regardless of trajectory reliability, exposing target values to compounding model error or over-relying on critic approximations. We introduce density-guided bootstrap boundaries, a trajectory-dependent mechanism that adapts the depth of imagined returns using a score-informed relative density proxy. The proxy accumulates the estimated divergence of a...

</details>

<details>
<summary>Share</summary>

```
Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning

Latent world models allow reinforcement learning agents to learn policies from imagined trajectories, yet determining the optimal depth of model reliance remains a fundamental challenge.

arXiv: https://arxiv.org/abs/2610.41022

#worldmodels #robotics
```

</details>

---

### [UFMF: Radar-Guided Kinematic Priors for Real-Time 4D Occupancy Forecasting](https://arxiv.org/abs/2610.40947)

**Authors:** Zeping Zhang, Zhuoya Zhao, Robert Laganière

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.40947) | [PDF](https://arxiv.org/pdf/2610.40947)

<details>
<summary>Abstract</summary>

Real-time 4D occupancy forecasting requires reliably extrapolating both ego motion and surrounding actor motion under strict latency budgets. Recent occupancy world models improve long-horizon fidelity through generative decoders and 3D volumetric modeling, yet their computational cost makes real-time deployment challenging. Light-weight BEV forecasters meet latency requirements but often blur or suppress fast-moving actors at longer horizons. We present UFMF (Ultra-Fast Multi-modal Forecaster), a real-time forecaster that keeps an attention-free diagonal state-space temporal core while inject...

</details>

<details>
<summary>Share</summary>

```
UFMF: Radar-Guided Kinematic Priors for Real-Time 4D Occupancy Forecasting

Real-time 4D occupancy forecasting requires reliably extrapolating both ego motion and surrounding actor motion under strict latency budgets.

arXiv: https://arxiv.org/abs/2610.40947

#worldmodels #robotics
```

</details>

---

### [Let LiDAR Decide Where to Look: Geometry-Measured Token Selection for Efficient Sparse Latent World Models](https://arxiv.org/abs/2610.40935)

**Authors:** Zeping Zhang, Zhuoya Zhao, Robert Laganière

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.40935) | [PDF](https://arxiv.org/pdf/2610.40935)

<details>
<summary>Abstract</summary>

Vision-centric autonomous driving models encode thousands of image tokens per frame, yet most depict sky, buildings, or empty road---content irrelevant to planning. Worse, these tokens dilute the planner's attention: we show that randomly discarding 75% of tokens already outperforms the dense model, because the planner can concentrate on the remaining driving-critical content. Building on this finding, we present Geometry-Aware Token Selection (GATS), which uses LiDAR and radar point projections to select a small fraction of image tokens before the vision backbone runs. Because the selector op...

</details>

<details>
<summary>Share</summary>

```
Let LiDAR Decide Where to Look: Geometry-Measured Token Selection for Efficient Sparse Latent World Models

Vision-centric autonomous driving models encode thousands of image tokens per frame, yet most depict sky, buildings, or empty road---content irrelevant to planning.

arXiv: https://arxiv.org/abs/2610.40935

#worldmodels #robotics
```

</details>

---

### [Beyond Plausible Prediction: Safety Sufficiency in Web World Models](https://arxiv.org/abs/2610.40798)

**Authors:** Zhifei Hu, Alexandra I. Cristea, Adel Bibi, Jialin Yu

**Published:** 2026-10-29 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.40798) | [PDF](https://arxiv.org/pdf/2610.40798)

<details>
<summary>Abstract</summary>

Web world models increasingly predict the consequences of candidate actions before agents act, yet a plausible predicted future does not necessarily support the correct safety decision. In a matched human evaluation of 3,000 predictions from ten frozen open models, 86.1% are judged semantically plausible. However, several models exhibit highly asymmetric authorisation behaviour, combining low false-safe execution with poor recall of clarifiable ASK cases and a strong preference for BLOCK. This motivates safety sufficiency: whether a predictive interface preserves and exposes the policy-decisiv...

</details>

<details>
<summary>Share</summary>

```
Beyond Plausible Prediction: Safety Sufficiency in Web World Models

Web world models increasingly predict the consequences of candidate actions before agents act, yet a plausible predicted future does not necessarily support the correct safety decision.

arXiv: https://arxiv.org/abs/2610.40798

#worldmodels #robotics
```

</details>

---

### [Generating Critic-Guided Synthetic Experience in Latent World Models](https://arxiv.org/abs/2610.39100)

**Authors:** Jorge de Freitas, Christos Ziakas, Alessandra Russo

**Published:** 2026-10-29 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.39100) | [PDF](https://arxiv.org/pdf/2610.39100)

<details>
<summary>Abstract</summary>

Learning from offline datasets is limited in scalability, as collecting new experience is often costly or unsafe in the real world. World models offer an alternative way to generate new experience through a learned dynamics model, yet learning policies in latent space is limited due to compounding errors in imagined rollouts. To this end, we propose using the world model as a local transition generator, leveraging critic guidance to choose actions inside that model to generate synthetic experiences. We study action refinement methodologies, introducing Critic-Guided Synthetic Experience (CGSE)...

</details>

<details>
<summary>Share</summary>

```
Generating Critic-Guided Synthetic Experience in Latent World Models

Learning from offline datasets is limited in scalability, as collecting new experience is often costly or unsafe in the real world.

arXiv: https://arxiv.org/abs/2610.39100

#worldmodels #robotics
```

</details>

---

### [Structural-Test Geometry as an Inductive Bias for Partially Observable World Models](https://arxiv.org/abs/2610.38903)

**Authors:** Todd Y. Zhou

**Published:** 2026-10-28 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.38903) | [PDF](https://arxiv.org/pdf/2610.38903)

<details>
<summary>Abstract</summary>

Predictive world-model objectives need not organize latent histories according to distinctions required for later control. With privileged simulator access during training, should response-derived structural information be predicted, decoded, or imposed directly on latent geometry--and how do these choices compare with structured belief distillation? We define posterior-marginalized structural tests whose response distributions induce a pseudometric over histories, then train quotient-preserving (QP) world models by aligning shared latent Euclidean distances to that metric. Across a fixed six-...

</details>

<details>
<summary>Share</summary>

```
Structural-Test Geometry as an Inductive Bias for Partially Observable World Models

Predictive world-model objectives need not organize latent histories according to distinctions required for later control.

arXiv: https://arxiv.org/abs/2610.38903

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

### [Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection](https://arxiv.org/abs/2610.39076)

**Authors:** Li Guan, Rachael Granberry, Sahar Aseeri, Sahar Rostami, Taylor Niehues et al. (104 authors)

**Published:** 2026-10-29 (updated 2026-10-31) | **Categories:** cs.RO, cs.AI, cs.AR | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.39076) | [PDF](https://arxiv.org/pdf/2610.39076)

<details>
<summary>Abstract</summary>

Collecting naturalistic human manipulation demonstrations with accurate contact force and hand pose is essential for robot dexterous manipulation policy and foundational world model learning - yet no existing wearable platform provides both calibrated fingertip force sensing and occlusion-resilient hand tracking in a form factor that preserves natural manipulation behavior. We present Tactus, a textile-integrated sensing glove that co-optimizes three design pillars: (1) a thin, conformal 3D-knit form factor (1.5 mm fingertip stackup) designed to minimize interference with natural manipulation,...

</details>

<details>
<summary>Share</summary>

```
Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection

Collecting naturalistic human manipulation demonstrations with accurate contact force and hand pose is essential for robot dexterous manipulation policy and foundational world model learning - yet no existing wearable...

arXiv: https://arxiv.org/abs/2610.39076

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

### [Agentic World Modeling for Agent Test-time Scaling without Environment Replica](https://arxiv.org/abs/2610.40927)

**Authors:** Wendi Li, Huseyin A. Inan, Wei-Ning Chen, Yanzhi Chen, Chetan Bansal et al. (7 authors)

**Published:** 2026-10-29 | **Categories:** cs.AI, cs.CL, cs.MA | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.40927) | [PDF](https://arxiv.org/pdf/2610.40927)

<details>
<summary>Abstract</summary>

Test-time scaling (TTS) improves large language model agents by sampling and selecting among multiple candidate trajectories, but common realizations assume that these trajectories can be executed in parallel. This assumption breaks in realistic deployments, where enterprise workspaces and cloud services are shared and persistent, costly or infeasible to replicate, and actions may introduce irreversible side effects or cross-trajectory interference. Existing generative world models avoid direct execution, but typically compress environment state into a single prompt, limiting their ability to...

</details>

<details>
<summary>Share</summary>

```
Agentic World Modeling for Agent Test-time Scaling without Environment Replica

Test-time scaling (TTS) improves large language model agents by sampling and selecting among multiple candidate trajectories, but common realizations assume that these trajectories can be executed in parallel.

arXiv: https://arxiv.org/abs/2610.40927

#worldmodels #robotics
```

</details>

---

### [Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion](https://arxiv.org/abs/2610.39516)

**Authors:** Christoph B Rist, Larissa T Triess, Markus Enzweiler, Dariu M Gavrila

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.39516) | [PDF](https://arxiv.org/pdf/2610.39516)

<details>
<summary>Abstract</summary>

We study domain generalization for LIDAR semantic segmentation. Deep neural networks achieve strong performance on 3D point clouds, yet real-world LIDAR exhibits sensor-specific sampling patterns that hinder transfer across datasets. In many applications, performance on completely unseen sensors is crucial. A model should preferably work on a new setup without prior access to its data or labels. To this end, we introduce a source-only training scheme that adds an occupancy prediction auxiliary objective. We aggregate source-domain scans into a simple world model and use it as the supervision s...

</details>

<details>
<summary>Share</summary>

```
Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion

We study domain generalization for LIDAR semantic segmentation.

arXiv: https://arxiv.org/abs/2610.39516

#worldmodels #robotics
```

</details>

---
