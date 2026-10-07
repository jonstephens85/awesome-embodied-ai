# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-07 21:00 UTC

**Papers shown:** 93 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [DepthWorld: 3D World Model for Robot Manipulation](https://arxiv.org/abs/2610.08780)

**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08780) | [PDF](https://arxiv.org/pdf/2610.08780) | [Project Page](https://www.jaibardhan.com/depthworld)

<details>
<summary>Abstract</summary>

World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absorb it without disturbing strong pretrained video priors. We introduce a calibration pipeline that com...

</details>

<details>
<summary>Share</summary>

```
DepthWorld: 3D World Model for Robot Manipulation

World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning.

arXiv: https://arxiv.org/abs/2610.08780
Project page: https://www.jaibardhan.com/depthworld

#worldmodels #robotics
```

</details>

---

### [SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](https://arxiv.org/abs/2610.06598)

**Authors:** Xiaodong Wang, Tianle Li, Chuanxin Song, Junliang Xie, Zhanmi Zhong et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06598) | [PDF](https://arxiv.org/pdf/2610.06598) | [Code](https://github.com/Wang-Xiaodong1899/SimForcing)

<details>
<summary>Abstract</summary>

Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation. We present SimForcing, a simulation-guided framework that uses simulation both as a source of transferable motion knowledge and as a controllable reference for prediction. First, we transfer motion knowledge from a simulation te...

</details>

<details>
<summary>Share</summary>

```
SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging.

arXiv: https://arxiv.org/abs/2610.06598
Code: https://github.com/Wang-Xiaodong1899/SimForcing

#worldmodels #robotics
```

</details>

---

### [PWM: Personalized World Models with Online Reinforcement Learning](https://arxiv.org/abs/2610.04920)

**Authors:** Zhexin Lou, Guancheng Lu, Zeyu Zhang, Yi Zhang, Yang Zhao et al. (6 authors)

**Published:** 2026-10-04 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04920) | [PDF](https://arxiv.org/pdf/2610.04920) | [Project Page](https://aigeeksgroup.github.io/PWM) | [Code](https://github.com/AIGeeksGroup/PWM)

<details>
<summary>Abstract</summary>

Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video. This requires learning the scene's visual identity while retaining the quality of action-conditioned generation. We introduce Personalized World Models (PWM), a framework for customizing interactive world models from short scene videos through online reinforcement learning. In PWM, the support trajectory and its associated controls provide reward feedback on continuations sampled from the current policy. In the GRPO instantiation, group-relative optimizati...

</details>

<details>
<summary>Share</summary>

```
PWM: Personalized World Models with Online Reinforcement Learning

Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video.

arXiv: https://arxiv.org/abs/2610.04920
Project page: https://aigeeksgroup.github.io/PWM
Code: https://github.com/AIGeeksGroup/PWM

#worldmodels #robotics
```

</details>

---

### [DeltaWorld: Physically Consistent Interactive World Simulators via Action-Conditioned Latent Increment Learning](https://arxiv.org/abs/2610.02691)

**Authors:** Boyuan Hou, Xiaoge Cao, Chaofan Zhang, Shuo Wang, Shaowei Cui

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world simulator" in title; 3 distinct keyword hits; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.02691) | [PDF](https://arxiv.org/pdf/2610.02691)

<details>
<summary>Abstract</summary>

Interactive world simulators can provide scalable environments for robot planning, policy training, and evaluation by predicting action consequences while reducing reliance on repeated physical rollouts. To serve these applications, they must generate future image sequences that respond faithfully to robot actions and preserve the dynamics of robot-object interactions over long horizons. However, existing world models typically predict the entire next latent state and often fail to capture subtle changes induced by robot actions. Such omissions can produce physically implausible outcomes, incl...

</details>

<details>
<summary>Share</summary>

```
DeltaWorld: Physically Consistent Interactive World Simulators via Action-Conditioned Latent Increment Learning

Interactive world simulators can provide scalable environments for robot planning, policy training, and evaluation by predicting action consequences while reducing reliance on repeated physical rollouts.

arXiv: https://arxiv.org/abs/2610.02691

#worldmodels #robotics
```

</details>

---

### [Beyond Policy Alignment: Closing the Planning-Learning Loop for Robot Control with Learned World Models](https://arxiv.org/abs/2609.39751)

**Authors:** Kowndinya Boyalakuntla, Yuhan Liu, Abdeslam Boularias

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39751) | [PDF](https://arxiv.org/pdf/2609.39751) | [Project Page](https://pl-mpc-humanoid.github.io)

<details>
<summary>Abstract</summary>

Planning with learned world models combines online trajectory optimization with learned value and policy functions for high-dimensional control. Because the planner determines the experience used for learning, while the learned critic and actor in turn score and propose future plans, planning and learning form a closed feedback loop. TD-MPC is a prominent instance of this design. Recent policy-constrained variants strengthen one part of the loop by aligning the learned policy with planner behavior. We introduce PL-MPC (Planning-Learning MPC), which additionally modifies critic supervision and...

</details>

<details>
<summary>Share</summary>

```
Beyond Policy Alignment: Closing the Planning-Learning Loop for Robot Control with Learned World Models

Planning with learned world models combines online trajectory optimization with learned value and policy functions for high-dimensional control.

arXiv: https://arxiv.org/abs/2609.39751
Project page: https://pl-mpc-humanoid.github.io

#worldmodels #robotics
```

</details>

---

### [JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts](https://arxiv.org/abs/2610.00722)

**Authors:** Zheyuan Zhang, Suyu Ye, Nakul Agarwal, Hossein Nourkhiz Mahjoub, Ehsan Moradi Pari et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00722) | [PDF](https://arxiv.org/pdf/2610.00722) | [Project Page](https://jepa-ttt.github.io/)

<details>
<summary>Abstract</summary>

World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen during training. We present JEPA-TTT, which adapts the latent dynamics predictor of a pretrained action-conditioned Joint-Embedding Predictive Architecture world model throughout test time. Self-supervised updates accumulate across episodes, while the visual encoder and reward head remain fixed, preserving the pretrained representation and task objective. Planning requires neither a goal image nor online environment reward...

</details>

<details>
<summary>Share</summary>

```
JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts

World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen during training.

arXiv: https://arxiv.org/abs/2610.00722
Project page: https://jepa-ttt.github.io/

#worldmodels #robotics
```

</details>

---

### [Modeling Latent Disturbances for Robust Decision-Making in World Models](https://arxiv.org/abs/2610.07599)

**Authors:** Junwon Seo, Andrea Bajcsy

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.07599) | [PDF](https://arxiv.org/pdf/2610.07599) | [Project Page](https://junwon.me/LatentDisturbance/)

<details>
<summary>Abstract</summary>

In this paper, we study robust decision-making in the latent space of world models (WMs). Robust optimization is a mathematical framework where, given explicitly specified dynamics and physically meaningful disturbances, a robot can select actions that remain effective even under worst-case disturbances. However, applying this principle to the learned latent space of WMs introduces a fundamental challenge: because WMs have fully learned state spaces and dynamics inferred from high-dimensional observations, it is unclear how to define latent-space disturbances that faithfully represent uncertai...

</details>

<details>
<summary>Share</summary>

```
Modeling Latent Disturbances for Robust Decision-Making in World Models

In this paper, we study robust decision-making in the latent space of world models (WMs).

arXiv: https://arxiv.org/abs/2610.07599
Project page: https://junwon.me/LatentDisturbance/

#worldmodels #robotics
```

</details>

---

### [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805)

**Authors:** Wancong Zhang, Basile Terver, Michael Rabbat, Yann LeCun, Randall Balestriero

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06805) | [PDF](https://arxiv.org/pdf/2610.06805)

<details>
<summary>Abstract</summary>

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and each level's predictions become subgoals for the planner below it. When factors in the data evolve at...

</details>

<details>
<summary>Share</summary>

```
H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction.

arXiv: https://arxiv.org/abs/2610.06805

#worldmodels #robotics
```

</details>

---

### [KineWorld: Action-Induced Transport Fields for Embodied World Modeling](https://arxiv.org/abs/2610.06349)

**Authors:** Ziying Song, Yuchen Liu, Zhuoran Xu, Ziyang Liu, Jian Jin et al. (9 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06349) | [PDF](https://arxiv.org/pdf/2610.06349) | [Project Page](https://modaxiansheng.github.io/KineWorld/)

<details>
<summary>Abstract</summary>

Embodied world models predict the visual consequences of candidate actions before execution. However, existing action-conditioned world models often adopt uniformly weighted visual generation objectives that can be misaligned with embodied prediction needs. Even with explicit motion conditioning, these objectives can underemphasize spatially sparse changes that are critical to interaction. We propose KineWorld, a transport-aware world-modeling framework that extends robot kinematics from motion conditioning to the spatial allocation of generative supervision. Kinematic Transport Lifting (KTL)...

</details>

<details>
<summary>Share</summary>

```
KineWorld: Action-Induced Transport Fields for Embodied World Modeling

Embodied world models predict the visual consequences of candidate actions before execution.

arXiv: https://arxiv.org/abs/2610.06349
Project page: https://modaxiansheng.github.io/KineWorld/

#worldmodels #robotics
```

</details>

---

### [Flow Policies as Actions of Skill-Level World Models: Learned and Symbolic Abstractions for Long-Horizon Planning](https://arxiv.org/abs/2610.04767)

**Authors:** Andreu Matoses Gimenez, Andrei-Carlo Papuc, Chris Pek, Javier Alonso-Mora

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04767) | [PDF](https://arxiv.org/pdf/2610.04767) | [Project Page](https://andreumatoses.github.io/research/flow-skill-wm)

<details>
<summary>Abstract</summary>

Latent world models enable robots to plan by predicting the consequences of actions. Planning long tasks with control-rate actions requires many prediction steps, which enlarges the search space and accumulates error. Skill-level actions shorten these sequences, but a symbolic skill vocabulary requires domain knowledge and labeled demonstrations. We construct skill-level actions from the inputs of a flow-matching policy trained on demonstrations segmented into complete skills. The policy maps a noise seed and an observation, optionally with a code or label, to a complete skill execution, so on...

</details>

<details>
<summary>Share</summary>

```
Flow Policies as Actions of Skill-Level World Models: Learned and Symbolic Abstractions for Long-Horizon Planning

Latent world models enable robots to plan by predicting the consequences of actions.

arXiv: https://arxiv.org/abs/2610.04767
Project page: https://andreumatoses.github.io/research/flow-skill-wm

#worldmodels #robotics
```

</details>

---

### [Token-World: World Modeling in Vision-Language Model Token Space for Robot Manipulation](https://arxiv.org/abs/2610.00575)

**Authors:** Chuyao Fu, Xiaowei Chi, Yuhan Rui, Yu-kai Wang, Zezhong Qian et al. (17 authors)

**Published:** 2026-09-30 (updated 2026-10-05) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00575) | [PDF](https://arxiv.org/pdf/2610.00575) | [Project Page](https://chuyaofu.github.io/Token-World/)

<details>
<summary>Abstract</summary>

A common approach to world-model simulation for vision-language-action (VLA) systems is to predict future RGB observations and then re-encode them into policy inputs, introducing an indirect interface between simulation and downstream policy execution. We instead investigate whether world dynamics can be modeled in a compact, policy-oriented state derived from VLM visual tokens. A key challenge is that raw VLM visual tokens are high-dimensional, making efficient and accurate autoregressive dynamics modeling challenging. To address this, we introduce Token-World, an action-conditioned world mod...

</details>

<details>
<summary>Share</summary>

```
Token-World: World Modeling in Vision-Language Model Token Space for Robot Manipulation

A common approach to world-model simulation for vision-language-action (VLA) systems is to predict future RGB observations and then re-encode them into policy inputs, introducing an indirect interface between simulati...

arXiv: https://arxiv.org/abs/2610.00575
Project page: https://chuyaofu.github.io/Token-World/

#worldmodels #robotics
```

</details>

---

### [CF-JEPA: Improving Robustness of JEPA World Models via Controllability Factorization](https://arxiv.org/abs/2610.00727)

**Authors:** Morgan Byrd, Robert Wright, Sehoon Ha

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00727) | [PDF](https://arxiv.org/pdf/2610.00727) | [Project Page](https://morganbyrd03.github.io/cf-jepa/)

<details>
<summary>Abstract</summary>

Controlling an agent with vision requires being able to separate useful information from irrelevant background information. JEPA-style latent world models seem like a natural approach for this, as they do not perform pixel-level reconstruction; however, they are still sensitive to these distractor signals and experience latent collapse. In this work, we introduce Controllability Factorized JEPA (CF-JEPA), a JEPA-style world model which splits the latent space into controllable and uncontrollable subspaces. This factorization allows us to capture all the distractor information into the uncontro...

</details>

<details>
<summary>Share</summary>

```
CF-JEPA: Improving Robustness of JEPA World Models via Controllability Factorization

Controlling an agent with vision requires being able to separate useful information from irrelevant background information.

arXiv: https://arxiv.org/abs/2610.00727
Project page: https://morganbyrd03.github.io/cf-jepa/

#worldmodels #robotics
```

</details>

---

### [RoboCoach: World Models as Active Coaches for Compositional Robot Skills](https://arxiv.org/abs/2609.39685)

**Authors:** Jiajun Liu, Yifan Chen, Yichao Liu, Jiayi Zhang, Ruoqu Chen et al. (10 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39685) | [PDF](https://arxiv.org/pdf/2609.39685) | [Project Page](https://robocoach-ai.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation reuses skills across many task compositions, but improving these compositions with additional end-to-end demonstrations is costly. A practical self-improving system must decide both what to teach next and where to apply that supervision. We present ROBOCOACH, a world-model-guided coaching framework that uses imagined failures to guide demonstration requests and expert updates. Its Route-Imagine-Diagnose-Improve (RIDI) loop executes reusable skill experts inside COACHWORLD, our shared action-conditioned world model, and uses a progress judge to record the first s...

</details>

<details>
<summary>Share</summary>

```
RoboCoach: World Models as Active Coaches for Compositional Robot Skills

Long-horizon robot manipulation reuses skills across many task compositions, but improving these compositions with additional end-to-end demonstrations is costly.

arXiv: https://arxiv.org/abs/2609.39685
Project page: https://robocoach-ai.github.io/

#worldmodels #robotics
```

</details>

---

### [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](https://arxiv.org/abs/2610.08777)

**Authors:** Shangye Song, Dong Gong, Hong Jia, Yun Sing Koh, Xinyu Zhang

**Published:** 2026-10-06 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08777) | [PDF](https://arxiv.org/pdf/2610.08777) | [Project Page](https://wrecklong.github.io/CtrlCache/)

<details>
<summary>Abstract</summary>

Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explicitly exposes a signal they do not use: the controls for a chunk arrive before it is denoised, so a sc...

</details>

<details>
<summary>Share</summary>

```
CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching

Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls.

arXiv: https://arxiv.org/abs/2610.08777
Project page: https://wrecklong.github.io/CtrlCache/

#worldmodels #robotics
```

</details>

---

### [AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](https://arxiv.org/abs/2610.08773)

**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.CL, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08773) | [PDF](https://arxiv.org/pdf/2610.08773) | [Code](https://github.com/Sarim-MBZUAI/advsim2real)

<details>
<summary>Abstract</summary>

Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a task stops teaching once the agent solves it. We introduce AdvSim2Real, which co-evolves a task curri...

</details>

<details>
<summary>Share</summary>

```
AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal.

arXiv: https://arxiv.org/abs/2610.08773
Code: https://github.com/Sarim-MBZUAI/advsim2real

#worldmodels #robotics
```

</details>

---

### [Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training](https://arxiv.org/abs/2610.05861)

**Authors:** Yongxin Ning, Runliang Niu, Qianli Xing, Zhiyi Duan, Qingzu He et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05861) | [PDF](https://arxiv.org/pdf/2610.05861) | [Code](https://github.com/swaydy-n/Infinite-Dreamer)

<details>
<summary>Abstract</summary>

Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications. However, training highly capable and generalizable agents fundamentally relies on massive, high-fidelity visual-action trajectories, which are notoriously difficult to acquire. While human demonstrations are unscalable, existing GUI world models rely on text descriptions or HTML rendering, discarding crucial pixel-level visual details like icons and layout styles. To address this issue, we introduce Infinite-Dreamer, a simulation-free data synthesis m...

</details>

<details>
<summary>Share</summary>

```
Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training

Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications.

arXiv: https://arxiv.org/abs/2610.05861
Code: https://github.com/swaydy-n/Infinite-Dreamer

#worldmodels #robotics
```

</details>

---

### [How Much Planning Is Enough? Reducing Search and Computation in World-Model Planning](https://arxiv.org/abs/2610.08350)

**Authors:** Changbai Li, Sirui Li, Yichen Yang, Tongfei Chen, Zichao Feng et al. (7 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08350) | [PDF](https://arxiv.org/pdf/2610.08350)

<details>
<summary>Abstract</summary>

Visual world models enable goal-directed control through decision-time action search, but their deployment efficiency is often limited by conservatively large planning budgets. We show that competitive task performance can be achieved without agreement with the Full-budget action, that sufficient budgets vary across model--task pairs, and that iterative planners repeatedly encode solve-invariant context. To address these inefficiencies, we propose {SufficientPlan}, a simple deployment framework that requires no modification to pretrained world models or planner updates. Its {Paired Sequential...

</details>

<details>
<summary>Share</summary>

```
How Much Planning Is Enough? Reducing Search and Computation in World-Model Planning

Visual world models enable goal-directed control through decision-time action search, but their deployment efficiency is often limited by conservatively large planning budgets.

arXiv: https://arxiv.org/abs/2610.08350

#worldmodels #robotics
```

</details>

---

### [Commit While Futures Agree: Consequence-Aware Adaptive Action Chunking for Robot Manipulation](https://arxiv.org/abs/2610.07949)

**Authors:** Yuyan Li, Yujia Wang, Yusong Huang, Junjie Yang, Yanggang Sheng et al. (11 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.07949) | [PDF](https://arxiv.org/pdf/2610.07949)

<details>
<summary>Abstract</summary>

Action-chunking policies predict multi-step control sequences, but a fundamental question remains: how much of a predicted action chunk should be committed before replanning? Existing systems typically execute a fixed-length prefix, implicitly assuming that the same execution horizon remains trustworthy across states. Some adaptive methods estimate this horizon from the similarity or stability of predicted actions. However, different actions may lead to the same successful outcome, whereas similar actions can produce different futures, suggesting that commitment should be determined by agreeme...

</details>

<details>
<summary>Share</summary>

```
Commit While Futures Agree: Consequence-Aware Adaptive Action Chunking for Robot Manipulation

Action-chunking policies predict multi-step control sequences, but a fundamental question remains: how much of a predicted action chunk should be committed before replanning?

arXiv: https://arxiv.org/abs/2610.07949

#worldmodels #robotics
```

</details>

---

### [Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models](https://arxiv.org/abs/2610.07540)

**Authors:** Leonardo F. Toso, Yann LeCun, James Anderson, Oumayma Bounou

**Published:** 2026-10-06 | **Categories:** cs.LG, cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.07540) | [PDF](https://arxiv.org/pdf/2610.07540)

<details>
<summary>Abstract</summary>

Robotic systems often exhibit unstable modes, along which small perturbations and disturbances can cause unbounded growth unless corrected through feedback. Controlling such systems from high-dimensional visual observations requires representations that preserve these modes. Joint-embedding predictive architectures (JEPAs) provide a natural framework for learning such representations and their dynamics from visual data. However, we demonstrate that next step prediction combined with anti-collapse regularization does not guarantee that controllable unstable modes are preserved: the training los...

</details>

<details>
<summary>Share</summary>

```
Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models

Robotic systems often exhibit unstable modes, along which small perturbations and disturbances can cause unbounded growth unless corrected through feedback.

arXiv: https://arxiv.org/abs/2610.07540

#worldmodels #robotics
```

</details>

---

### [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)

**Authors:** Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, Yichen Feng, Yaorui Ding et al. (11 authors)

**Published:** 2026-10-05 (updated 2026-10-06) | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06814) | [PDF](https://arxiv.org/pdf/2610.06814) | [Project Page](https://tapdreamer.github.io)

<details>
<summary>Abstract</summary>

World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action models that instead uses a public encoder alone to construct a fixed local perturbation that transfer...

</details>

<details>
<summary>Share</summary>

```
TAPDreamer: Transferable Adversarial Patches for World Action Models

World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control.

arXiv: https://arxiv.org/abs/2610.06814
Project page: https://tapdreamer.github.io

#worldmodels #robotics
```

</details>

---

### [EpicWorldModel: Exploration-driven Planning with Latent World Models](https://arxiv.org/abs/2610.05996)

**Authors:** Bowen Feng, Julian Ost, May Mei, Anirudha Majumdar, Felix Heide

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05996) | [PDF](https://arxiv.org/pdf/2610.05996)

<details>
<summary>Abstract</summary>

Latent world models based on Joint-Embedding Predictive Architecture (JEPA) are deterministic by design. While successful in fully observable scenarios, this paradigm breaks down when past observations and actions lead to multiple plausible future possibilities, e.g., due to occlusion. We introduce EpicWorldModel, a framework to train stochastic JEPAs for environments and tasks with inherent uncertainty under partially observability. We jointly train the EpicWorldModel predictor with its latent representation space to directly predict multiple potential future states using a flow-matching obje...

</details>

<details>
<summary>Share</summary>

```
EpicWorldModel: Exploration-driven Planning with Latent World Models

Latent world models based on Joint-Embedding Predictive Architecture (JEPA) are deterministic by design.

arXiv: https://arxiv.org/abs/2610.05996

#worldmodels #robotics
```

</details>

---

### [Tackling Sim-to-Real Mismatch Through Sampling-Based Disturbance Observers: From Analytical Models to Learned World Models](https://arxiv.org/abs/2610.04896)

**Authors:** Tianqi Zhu, Jun Yang, Jianliang Mao, Cong Li, Shihua Li

**Published:** 2026-10-04 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04896) | [PDF](https://arxiv.org/pdf/2610.04896) | [Project Page](https://sampling-based-dob.github.io/)

<details>
<summary>Abstract</summary>

Robotic controllers increasingly rely on analytical models, simulators, cost-query interfaces, and learned world models. However, physical deployment can deviate from nominal assumptions, and additional disturbances may arise even when the model itself is accurate. In control systems, disturbance observers (DOB) are widely used to estimate such unmeasured effects from nominal models and measured feedback. Classical DOB formulations are generally built around explicit plant models. This paper develops the sampling-based disturbance observer (SDOB), extending the DOB principle to a broader range...

</details>

<details>
<summary>Share</summary>

```
Tackling Sim-to-Real Mismatch Through Sampling-Based Disturbance Observers: From Analytical Models to Learned World Models

Robotic controllers increasingly rely on analytical models, simulators, cost-query interfaces, and learned world models.

arXiv: https://arxiv.org/abs/2610.04896
Project page: https://sampling-based-dob.github.io/

#worldmodels #robotics
```

</details>

---

### [FutureWorlds: Learning Robotic World Models from Alternative Futures](https://arxiv.org/abs/2610.01019)

**Authors:** Hao Wu, Shengju Qian, Weiyan Wang, Fan Xu, Fan Zhang et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01019) | [PDF](https://arxiv.org/pdf/2610.01019) | [Code](https://github.com/Alexander-wu/FutureWorlds)

<details>
<summary>Abstract</summary>

Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes. However, turning alternative predictions into useful learning signals remains challenging: similar candidates limit informative quality comparisons, while diverging trajectories require persistent maintenance of their individual histories. We introduce FutureWorlds, a framework that unifies candidate construction, history maintenance, and learning from relative quality. Built on a multimodal discrete autoregressive model, FutureWorlds uses diverse beam search during reinforc...

</details>

<details>
<summary>Share</summary>

```
FutureWorlds: Learning Robotic World Models from Alternative Futures

Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes.

arXiv: https://arxiv.org/abs/2610.01019
Code: https://github.com/Alexander-wu/FutureWorlds

#worldmodels #robotics
```

</details>

---

### [Social-WM: Safety-Aware Latent World Models for Robot Social Navigation](https://arxiv.org/abs/2609.40177)

**Authors:** Zhihao Zheng, Mooi Choo Chuah

**Published:** 2026-09-30 (updated 2026-10-01) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.40177) | [PDF](https://arxiv.org/pdf/2609.40177)

<details>
<summary>Abstract</summary>

Safe social navigation requires a robot to anticipate not only the future consequences of its actions, but also whether a nominal action can actually be executed under surrounding physical and social constraints. We present Social-WM, an efficient latent world-model planning framework trained from egocentric RGB video sequences. Our key observation is that social-navigation experience contains a systematic discrepancy between the nominal action and the realizable action: a nominal forward action may be fully executed in free space, but needs to be constrained when heading towards a pedestrian...

</details>

<details>
<summary>Share</summary>

```
Social-WM: Safety-Aware Latent World Models for Robot Social Navigation

Safe social navigation requires a robot to anticipate not only the future consequences of its actions, but also whether a nominal action can actually be executed under surrounding physical and social constraints.

arXiv: https://arxiv.org/abs/2609.40177

#worldmodels #robotics
```

</details>

---

### [LocoWM: High-Precision Locomotion through World-Model-Guided Residual Adaptation](https://arxiv.org/abs/2609.39179)

**Authors:** Zijie Zhao, Shengqian Chen, Xiaoxu Wang, Han Jiang, Yuanheng Zhu et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39179) | [PDF](https://arxiv.org/pdf/2609.39179) | [Project Page](https://zhaozijie2022.github.io/LocoWM)

<details>
<summary>Abstract</summary>

High-precision locomotion combines motion-command tracking with precise regulation of task-relevant physical states, enabling robots to interact reliably with their surroundings during motion. Joint end-to-end optimization can leave precision objectives insufficiently optimized, while reactive residual control adjusts actions only after deviations become observable. We present \textbf{LocoWM}, a world-model-guided preactive residual adaptation framework for high-precision locomotion. A base policy provides command-following locomotion, while an action-conditioned world model predicts a sequenc...

</details>

<details>
<summary>Share</summary>

```
LocoWM: High-Precision Locomotion through World-Model-Guided Residual Adaptation

High-precision locomotion combines motion-command tracking with precise regulation of task-relevant physical states, enabling robots to interact reliably with their surroundings during motion.

arXiv: https://arxiv.org/abs/2609.39179
Project page: https://zhaozijie2022.github.io/LocoWM

#worldmodels #robotics
```

</details>

---

### [DeepJEPA: Scaling World Models from Within](https://arxiv.org/abs/2610.00368)

**Authors:** Zijian Jin, Yunbei Zhang, Yuanzhe Liu, Ming Liu, Baian Chen et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00368) | [PDF](https://arxiv.org/pdf/2610.00368) | [Project Page](https://deepjepa.github.io/)

<details>
<summary>Abstract</summary>

World-model planners typically scale outward by rolling farther, sampling more trajectories, or optimizing longer, while assigning the same computation to every imagined transition. We show that making every transition uniformly deeper wastes computation and can degrade planning because useful refinement is concentrated at a small set of decision-critical events. We introduce DeepJEPA, a weight-tied joint-embedding predictive world model that treats transition depth as an inner test-time scaling axis and learns when another recurrent update is worth computing for each candidate and rollout ste...

</details>

<details>
<summary>Share</summary>

```
DeepJEPA: Scaling World Models from Within

World-model planners typically scale outward by rolling farther, sampling more trajectories, or optimizing longer, while assigning the same computation to every imagined transition.

arXiv: https://arxiv.org/abs/2610.00368
Project page: https://deepjepa.github.io/

#worldmodels #robotics
```

</details>

---

### [WorldSonus: Bringing Sound to Worlds](https://arxiv.org/abs/2610.08760)

**Authors:** Pengjun Fang, Jingyi Fa, Kam Man Wu, Jiaming Wang, Haoyuan Huang et al. (12 authors)

**Published:** 2026-10-06 | **Categories:** cs.SD, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08760) | [PDF](https://arxiv.org/pdf/2610.08760) | [Project Page](https://noizai.github.io/WorldSonus/)

<details>
<summary>Abstract</summary>

Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To address these demands, we introduce WorldSonus, an interactive video-to-audio framework designed for real-time spatial sound synthesis in world models. For real-time generation, WorldSo...

</details>

<details>
<summary>Share</summary>

```
WorldSonus: Bringing Sound to Worlds

Recent advances in world models have enabled increasingly realistic visual synthesis.

arXiv: https://arxiv.org/abs/2610.08760
Project page: https://noizai.github.io/WorldSonus/

#worldmodels #robotics
```

</details>

---

### [Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning](https://arxiv.org/abs/2610.08627)

**Authors:** Wanjin Feng, Baobin Zhang, Ao Yu, Shibo Feng, Xi Wang et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08627) | [PDF](https://arxiv.org/pdf/2610.08627)

<details>
<summary>Abstract</summary>

Long-horizon world-model planning typically relies on autoregressive rollouts, where predicted states are repeatedly fed back into the model. This preserves temporal structure but creates a horizon-length sequential path and exposes later predictions to recursive decoded-state feedback. We introduce Parallel Predictive World Models (PPWM), which predict a finite-horizon trajectory in parallel while retaining causal interaction among future representations. Each horizon is conditioned on its causal action prefix, and future representations interact before decoding, separating temporal causality...

</details>

<details>
<summary>Share</summary>

```
Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning

Long-horizon world-model planning typically relies on autoregressive rollouts, where predicted states are repeatedly fed back into the model.

arXiv: https://arxiv.org/abs/2610.08627

#worldmodels #robotics
```

</details>

---

### [Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA](https://arxiv.org/abs/2610.08033)

**Authors:** Jordy Kieto

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08033) | [PDF](https://arxiv.org/pdf/2610.08033) | [Code](https://github.com/JordyKieto/puffermoba-dyna)

<details>
<summary>Abstract</summary>

World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to 6,000 ticks), train a policy only inside it with 1,400-tick free-running imagined episodes, and measure that policy in the real game against the opponent the game ships with. The real game never provides a gradient; it provides the policy's own games as training data for the world m...

</details>

<details>
<summary>Share</summary>

```
Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA

World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look.

arXiv: https://arxiv.org/abs/2610.08033
Code: https://github.com/JordyKieto/puffermoba-dyna

#worldmodels #robotics
```

</details>

---

### [Artemis: Geometry-Grounded Multi-Agent Driving World Models with Shared 3D State and Progressive Memory Update](https://arxiv.org/abs/2610.07031)

**Authors:** Sitian Shen, Jiuming Liu, Mengmeng Liu, Yian Wang, Michael Ying Yang et al. (10 authors)

**Published:** 2026-10-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.07031) | [PDF](https://arxiv.org/pdf/2610.07031) | [Project Page](https://liujiuming123.github.io/Artemis/)

<details>
<summary>Abstract</summary>

Recent video world models have witnessed the paradigm shift from single-agent to multi-agent involvements, which can reveal more complicated dynamics and cross-agent interaction in the real world. However, existing approaches commonly adopt implicit inter-agent communications via cross attention, which lack explicit geometry constraints and unified 3D state, thereby leading to poor multi-view consistency and struggling with recovering out-of-sight agents. In addition, most of them assume a static background, failing to represent uncontrolled background dynamics. To address these problems, we p...

</details>

<details>
<summary>Share</summary>

```
Artemis: Geometry-Grounded Multi-Agent Driving World Models with Shared 3D State and Progressive Memory Update

Recent video world models have witnessed the paradigm shift from single-agent to multi-agent involvements, which can reveal more complicated dynamics and cross-agent interaction in the real world.

arXiv: https://arxiv.org/abs/2610.07031
Project page: https://liujiuming123.github.io/Artemis/

#worldmodels #robotics
```

</details>

---

### [Kepler4D: Controllable Future Video Generation via 4D Scene State Evolution](https://arxiv.org/abs/2610.04152)

**Authors:** Feiran Wang, Bin Duan, Junyi Wu, Gaowen Liu, Yan Yan

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04152) | [PDF](https://arxiv.org/pdf/2610.04152) | [Project Page](https://brack-wang.github.io/kepler4d/)

<details>
<summary>Abstract</summary>

Video world models aim to preserve scene structure and predict how dynamic objects evolve beyond visual observations. We present Kepler4D, a framework for future video generation through explicit 4D scene state evolution. Given a monocular video, Kepler4D constructs a shared 3D representation of background geometry, object motion histories, coarse spatial supports, and semantic context. Chain-of-Motion summarizes observed motion and uses a vision-language model to select structured speed and heading decisions and decide whether to bound object-center height from below. A deterministic rollout...

</details>

<details>
<summary>Share</summary>

```
Kepler4D: Controllable Future Video Generation via 4D Scene State Evolution

Video world models aim to preserve scene structure and predict how dynamic objects evolve beyond visual observations.

arXiv: https://arxiv.org/abs/2610.04152
Project page: https://brack-wang.github.io/kepler4d/

#worldmodels #robotics
```

</details>

---

### [EVEWorld: Physical Evolution Supervision for Embodied World Models](https://arxiv.org/abs/2610.03374)

**Authors:** Kaiqi Wang, Songxin Zhang, Zejian Xie, Xiao Xiong, Zhuoyang Song et al. (10 authors)

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.03374) | [PDF](https://arxiv.org/pdf/2610.03374)

<details>
<summary>Abstract</summary>

Embodied world models enable scalable simulation of embodied interactions for robot learning. However, existing models are prone to Model Laziness, as they focus on visual fidelity at the expense of physical reasoning and lack process-level supervision over the temporal dynamics of manipulated objects. In this work, we propose EVEWorld, a physical evolution-supervision framework for physically consistent target evolution. EVEWorld consists of two components: Instance-Guided Restoration (IGR) and Temporal Instance Alignment (TIA). First, IGR promotes instance consistency through restoration sup...

</details>

<details>
<summary>Share</summary>

```
EVEWorld: Physical Evolution Supervision for Embodied World Models

Embodied world models enable scalable simulation of embodied interactions for robot learning.

arXiv: https://arxiv.org/abs/2610.03374

#worldmodels #robotics
```

</details>

---

### [Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521)

**Authors:** Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02521) | [PDF](https://arxiv.org/pdf/2610.02521) | [Project Page](https://spatial-memory-intelligence.github.io/)

<details>
<summary>Abstract</summary>

Long-video generation and world models have shown strong potential for interactive entertainment and embodied simulation by predicting future observations conditioned on user actions and historical memory. However, as memory sequences grow longer and their structures become increasingly complex, managing long-range spatial context becomes increasingly challenging, calling for a more intelligent and systematic memory-management strategy. Building on the advancing spatial reasoning capabilities of multimodal large language models (MLLMs) and the broader vision of unified models, we propose Spati...

</details>

<details>
<summary>Share</summary>

```
Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory

Long-video generation and world models have shown strong potential for interactive entertainment and embodied simulation by predicting future observations conditioned on user actions and historical memory.

arXiv: https://arxiv.org/abs/2610.02521
Project page: https://spatial-memory-intelligence.github.io/

#worldmodels #robotics
```

</details>

---

### [World Editing: Intervening on Executable Worlds at Increasing Depth](https://arxiv.org/abs/2610.02331)

**Authors:** Max Ku, Nok-Kan Law, Yu-Chien Tang, Shih-Ying Yeh, Ping Nie et al. (18 authors)

**Published:** 2026-10-01 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02331) | [PDF](https://arxiv.org/pdf/2610.02331) | [Project Page](https://vinesmsuic.github.io/IGMWorld/)

<details>
<summary>Abstract</summary>

Interactive world models are increasingly capable of generating environments and acting within them, yet deliberately editing an existing executable world remains underexplored. We formulate world editing as intervening on an existing world while preserving properties that should remain unchanged, and introduce intervention depth as an axis describing how strongly an edit couples world entities, dynamics, and systems. We instantiate this capability through industry-grade game modding and introduce IGMWorld, together with IGMBench, a benchmark of 110 tasks and over 1.1K executable state and beh...

</details>

<details>
<summary>Share</summary>

```
World Editing: Intervening on Executable Worlds at Increasing Depth

Interactive world models are increasingly capable of generating environments and acting within them, yet deliberately editing an existing executable world remains underexplored.

arXiv: https://arxiv.org/abs/2610.02331
Project page: https://vinesmsuic.github.io/IGMWorld/

#worldmodels #robotics
```

</details>

---

### [4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160)

**Authors:** Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02160) | [PDF](https://arxiv.org/pdf/2610.02160) | [Project Page](https://stability-ai.github.io/4director/)

<details>
<summary>Abstract</summary>

Precise control over camera and object motion is essential for professional video production. Existing methods control objects only coarsely, through image-plane cues that are ambiguous in depth and rotation or through 3D tracks and blobs that lack complete geometry and lose consistency across viewpoint changes. We introduce 4Director, a video world model conditioned on an explicit 4D scene representation: each object is reconstructed once from the input image as a canonical mesh and moved by one prescribed rigid transformation per frame. This representation provides an intuitive 3D control in...

</details>

<details>
<summary>Share</summary>

```
4Director: Controlling Video World Models with Rigid 3D Geometry

Precise control over camera and object motion is essential for professional video production.

arXiv: https://arxiv.org/abs/2610.02160
Project page: https://stability-ai.github.io/4director/

#worldmodels #robotics
```

</details>

---

### [Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models](https://arxiv.org/abs/2610.01942)

**Authors:** Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01942) | [PDF](https://arxiv.org/pdf/2610.01942) | [Code](https://github.com/Sta8is/Latent-Foresight)

<details>
<summary>Abstract</summary>

Predicting the future evolution of a scene is a fundamental capability for world modeling. Recent work has shown that operating in the feature space of Vision Foundation Models (VFMs) yields semantically rich representations that support diverse future scene understanding tasks. However, existing approaches rely on two-stage pipelines, where VFM features are first compressed using fixed dimensionality reduction (e.g., PCA) or independently trained autoencoders, and a separate predictor is trained on top of the resulting frozen latent space. This decoupling between representation learning and t...

</details>

<details>
<summary>Share</summary>

```
Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models

Predicting the future evolution of a scene is a fundamental capability for world modeling.

arXiv: https://arxiv.org/abs/2610.01942
Code: https://github.com/Sta8is/Latent-Foresight

#worldmodels #robotics
```

</details>

---

### [Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614)

**Authors:** Xindi Yang, Baolu Li, Liam Lee, Zhenfei Yin, Songxin Zhang et al. (11 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01614) | [PDF](https://arxiv.org/pdf/2610.01614) | [Project Page](https://madaoer.github.io/projects/oneira)

<details>
<summary>Abstract</summary>

Generative video world models can now synthesize open-ended environments that agents can navigate and interact with in simple ways. Yet open-ended generation does not imply full interaction: as a generated world expands, newly created content through navigation should expand what the agent can act upon, and as the agent changes the world, those changes should become persistent parts of the environment rather than transient visual effects. We characterize these two requirements as Open-World Interactivity, where newly generated or encountered entities are incorporated into the actionable world,...

</details>

<details>
<summary>Share</summary>

```
Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models

Generative video world models can now synthesize open-ended environments that agents can navigate and interact with in simple ways.

arXiv: https://arxiv.org/abs/2610.01614
Project page: https://madaoer.github.io/projects/oneira

#worldmodels #robotics
```

</details>

---

### [HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation](https://arxiv.org/abs/2610.02197)

**Authors:** Tahira Kazimi, Shubhankar Borse, Munawar Hayat, Fatih Porikli, Pinar Yanardag

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02197) | [PDF](https://arxiv.org/pdf/2610.02197) | [Project Page](https://hiphy-video.github.io/)

<details>
<summary>Abstract</summary>

Video generation models have achieved remarkable visual fidelity and have strong potential to become general-purpose world simulators. Despite this progress, they still fail to generate videos which adhere to laws of physics. The problem becomes even more apparent in realistic settings where multiple physical principles must work together within the same video; for example, "a balloon floating upward while steam rises from a pot" requires buoyancy and fluid dynamics to unfold coherently and simultaneously. Yet existing methods largely ignore multi-principle interactions, focusing on a single p...

</details>

<details>
<summary>Share</summary>

```
HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation

Video generation models have achieved remarkable visual fidelity and have strong potential to become general-purpose world simulators.

arXiv: https://arxiv.org/abs/2610.02197
Project page: https://hiphy-video.github.io/

#worldmodels #robotics
```

</details>

---

### [DashVMC: Real-Time Discrete World Model Control in Geometry Dash](https://arxiv.org/abs/2609.40003)

**Authors:** Florent Tariolle, Florian Yger

**Published:** 2026-09-30 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.40003) | [PDF](https://arxiv.org/pdf/2609.40003) | [Project Page](https://tariolle.github.io/dash-vmc/)

<details>
<summary>Abstract</summary>

World-model agents are usually evaluated in simulators that can wait for the policy; live games impose the opposite constraint, requiring capture, prediction, and action before the next frame. We present DashVMC, which learns a compact, action-conditioned world model from approximately two hours of recorded Geometry Dash gameplay. To test whether the learned dynamics are actionable, a controller is initialized by behavioural cloning (BC) and refined with Proximal Policy Optimization (PPO) entirely in frozen-model rollouts, without further interaction with the live game. Across three controller...

</details>

<details>
<summary>Share</summary>

```
DashVMC: Real-Time Discrete World Model Control in Geometry Dash

World-model agents are usually evaluated in simulators that can wait for the policy; live games impose the opposite constraint, requiring capture, prediction, and action before the next frame.

arXiv: https://arxiv.org/abs/2609.40003
Project page: https://tariolle.github.io/dash-vmc/

#worldmodels #robotics
```

</details>

---

### [Why Do Conventional World Models Fail to Learn Cellular Automata?](https://arxiv.org/abs/2609.39604)

**Authors:** Shaoyang Guo, Ziming Liu

**Published:** 2026-09-30 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39604) | [PDF](https://arxiv.org/pdf/2609.39604) | [Code](https://github.com/guoshaoyang-pku/momentum-induction)

<details>
<summary>Abstract</summary>

Although conventional world models - auto-regressive or diffusion models based on transformers or convolutional networks - may learn surface statistics of world dynamics, can they learn the exact world dynamics from its observed history? Leveraging cellular automata as a simple testbed, we find the answer to be no in many cases. Conventional architectures predict most pixels correctly yet rarely complete a rollout: a CNN predicts 96.3% of cells but completes 18.9% of rollouts; a joint diffusion model completes none. We trace the gap to three failure modes of these world models - namely, they f...

</details>

<details>
<summary>Share</summary>

```
Why Do Conventional World Models Fail to Learn Cellular Automata?

Although conventional world models - auto-regressive or diffusion models based on transformers or convolutional networks - may learn surface statistics of world dynamics, can they learn the exact world dynamics from i...

arXiv: https://arxiv.org/abs/2609.39604
Code: https://github.com/guoshaoyang-pku/momentum-induction

#worldmodels #robotics
```

</details>

---

### [RIWANav: Recursive World-Action Models with Self-Improvement for Urban Navigation](https://arxiv.org/abs/2610.08640)

**Authors:** Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Haitao Yang et al. (7 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08640) | [PDF](https://arxiv.org/pdf/2610.08640)

<details>
<summary>Abstract</summary>

Long-horizon urban navigation requires sequential local decisions whose errors can compound over time. Imitation learning (IL) rarely learns from failures, while physical trial-and-error reinforcement learning (RL) is costly. Action-conditioned world models can provide imagined feedback by predicting visual consequences for candidate actions. However, a frozen world model may become less reliable as the policy evolves. In this paper, we introduce RIWANAV, a post-training framework that casts the coupled adaptation of a world model and an action model (policy) as task-specific recursive self-im...

</details>

<details>
<summary>Share</summary>

```
RIWANav: Recursive World-Action Models with Self-Improvement for Urban Navigation

Long-horizon urban navigation requires sequential local decisions whose errors can compound over time.

arXiv: https://arxiv.org/abs/2610.08640

#worldmodels #robotics
```

</details>

---

### [DreamFormer: Dream Imitation with a Transformer World Model for Language-Conditioned Robotic Manipulation](https://arxiv.org/abs/2610.04540)

**Authors:** Mostafa Kotb, Cornelius Weber, Muhammad Burhan Hafez, Stefan Wermter

**Published:** 2026-10-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04540) | [PDF](https://arxiv.org/pdf/2610.04540)

<details>
<summary>Abstract</summary>

We introduce DreamFormer, a model-based agent that acquires language-conditioned, multi-task skills by imitating expert demonstrations within the latent imagination of a learned world model. DreamFormer first learns a task-agnostic Transformer world model from unstructured play data, then acquires task-specific behaviors by optimizing an intrinsic reward that aligns agent-generated rollouts with expert demonstrations in latent space. Since the policy is trained on-policy inside imagination, it is exposed to its own errors during training, mitigating the covariate shift inherent to offline beha...

</details>

<details>
<summary>Share</summary>

```
DreamFormer: Dream Imitation with a Transformer World Model for Language-Conditioned Robotic Manipulation

We introduce DreamFormer, a model-based agent that acquires language-conditioned, multi-task skills by imitating expert demonstrations within the latent imagination of a learned world model.

arXiv: https://arxiv.org/abs/2610.04540

#worldmodels #robotics
```

</details>

---

### [AVL-JEPA: Preventing Causal Dynamics Information Collapse In Joint Embedding Predictive Architecture World Models](https://arxiv.org/abs/2610.03587)

**Authors:** Yikang Qiao, Ling Zhang, Ziying Song, Duan Huang

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.03587) | [PDF](https://arxiv.org/pdf/2610.03587)

<details>
<summary>Abstract</summary>

Joint embedding predictive architectures (JEPAs) predict future latent representations without reconstructing observations, enabling world models to focus on high-level semantic dynamics. However, a JEPA can preserve high dimensional visual information while discarding information about the physical consequences of actions. We call this failure mode causal dynamics information collapse and propose action-grounded vision-invariance latent (AVL) to prevent this collapse. We first use the executed action as an auxiliary dynamics anchor that encourages the model to preserve dynamics information, a...

</details>

<details>
<summary>Share</summary>

```
AVL-JEPA: Preventing Causal Dynamics Information Collapse In Joint Embedding Predictive Architecture World Models

Joint embedding predictive architectures (JEPAs) predict future latent representations without reconstructing observations, enabling world models to focus on high-level semantic dynamics.

arXiv: https://arxiv.org/abs/2610.03587

#worldmodels #robotics
```

</details>

---

### [Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning](https://arxiv.org/abs/2610.01224)

**Authors:** Takumi Hara, Kanata Suzuki

**Published:** 2026-10-01 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.01224) | [PDF](https://arxiv.org/pdf/2610.01224)

<details>
<summary>Abstract</summary>

Latent world models plan by scoring candidate action sequences with distances in latent space. However, task success is judged by physical quantities, which we call the success-criterion quantities. In all four latent world models we examine, the end-effector position is encoded in the latent state with an error larger than the success criterion allows. Such a latent state cannot separate successful candidates from failing ones. We propose an auxiliary loss that uses success-criterion quantities as training targets, whereas existing latent world models take them only as inputs. During training...

</details>

<details>
<summary>Share</summary>

```
Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning

Latent world models plan by scoring candidate action sequences with distances in latent space.

arXiv: https://arxiv.org/abs/2610.01224

#worldmodels #robotics
```

</details>

---

### [PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162)

**Authors:** Isaiah Milkey, Som Sagar, Aditya Taparia, Xinyuan Liu, Jiqing Wen et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.01162) | [PDF](https://arxiv.org/pdf/2610.01162)

<details>
<summary>Abstract</summary>

Reliable video world models could provide scalable predictive environments for robot learning, planning, and evaluation. However, generated robot videos can violate physical principles and complete tasks through physically implausible behavior, limiting their reliability for robot learning and planning. Current video-generation benchmarks exclude physics that are inherently hidden by visuals (e.g., weight, viscosity, friction). Due to this, video models are evaluated on the fidelity of physics, not the underlying accuracy of physics. We introduce PhysicsLENS, a dataset and benchmark for evalua...

</details>

<details>
<summary>Share</summary>

```
PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models

Reliable video world models could provide scalable predictive environments for robot learning, planning, and evaluation.

arXiv: https://arxiv.org/abs/2610.01162

#worldmodels #robotics
```

</details>

---

### [The Planning Limits of Latent World Models](https://arxiv.org/abs/2609.39235)

**Authors:** Ali Alrasheed, Basim Azam, Naveed Akhtar

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2609.39235) | [PDF](https://arxiv.org/pdf/2609.39235)

<details>
<summary>Abstract</summary>

World models offer a promising way to help robots understand how the physical world evolves and plan complex behaviours through imagination. Yet existing studies mainly demonstrate what these models can accomplish, leaving unclear when their predictions remain useful for planning and where they fail. We study this question using action-conditioned predictors built on five frozen self-supervised visual backbones: V-JEPA 2, V-JEPA 2.1, VideoMAEv2, VideoPrism, and DINOv2. We use frozen backbones to test representations intended to transfer across environments. We evaluate these models on diverse...

</details>

<details>
<summary>Share</summary>

```
The Planning Limits of Latent World Models

World models offer a promising way to help robots understand how the physical world evolves and plan complex behaviours through imagination.

arXiv: https://arxiv.org/abs/2609.39235

#worldmodels #robotics
```

</details>

---

### [Linear Recurrent Memory Suffices to Distil a World-Model Policy for Robot Air Hockey](https://arxiv.org/abs/2609.39151)

**Authors:** F. Olivia Fan, Oliver Obst

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.39151) | [PDF](https://arxiv.org/pdf/2609.39151)

<details>
<summary>Abstract</summary>

Does memory-dependent control need nonlinear recurrent dynamics? We study simulated air-hockey defence under temporary loss of puck tracking. A DreamerV3 teacher outperforms a memoryless policy under tracking loss, while resetting the teacher's recurrent state sharply reduces performance, which demonstrates that the task requires memory. We distil this teacher into compact recurrent policies with a 64 dimensional state, with a combination of a diagonal linear recurrence and an optional rank-$k$ nonlinear innovation while retaining nonlinear observation encoders and action heads. Across five ma...

</details>

<details>
<summary>Share</summary>

```
Linear Recurrent Memory Suffices to Distil a World-Model Policy for Robot Air Hockey

Does memory-dependent control need nonlinear recurrent dynamics?

arXiv: https://arxiv.org/abs/2609.39151

#worldmodels #robotics
```

</details>

---

### [World Models' Last Exam in Physics](https://arxiv.org/abs/2610.08791)

**Authors:** Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin et al. (11 authors)

**Published:** 2026-10-06 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08791) | [PDF](https://arxiv.org/pdf/2610.08791)

<details>
<summary>Abstract</summary>

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks spanning mechanics, optics, fluids, thermal and phase-change phenomena, electromagnetism, and surface...

</details>

<details>
<summary>Share</summary>

```
World Models' Last Exam in Physics

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems.

arXiv: https://arxiv.org/abs/2610.08791

#worldmodels #robotics
```

</details>

---

### [Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models](https://arxiv.org/abs/2610.07704)

**Authors:** Fernando Martinez, Tao Li, Yingdong Lu, Juntao Chen

**Published:** 2026-10-06 | **Categories:** cs.MA, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.07704) | [PDF](https://arxiv.org/pdf/2610.07704)

<details>
<summary>Abstract</summary>

Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized critic or inter-agent communication. Such a stringent information structure renders the conventional reward signal ambiguous. A poor return may result from an ineffective ego action, an incompatible teammate response, or an effective opponent response, yet scalar rewards alone do not reveal which explanation is responsible. We argue that agents can learn more effectively by prospectiv...

</details>

<details>
<summary>Share</summary>

```
Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models

Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized crit...

arXiv: https://arxiv.org/abs/2610.07704

#worldmodels #robotics
```

</details>

---

### [Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object](https://arxiv.org/abs/2610.07355)

**Authors:** Peng Xie, Amr Alanwar

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.07355) | [PDF](https://arxiv.org/pdf/2610.07355)

<details>
<summary>Abstract</summary>

Video world models track objects they can see; we ask what they keep of objects they cannot. We hide an object from a frozen V-JEPA 2 predictor and compare its prediction for the hidden region with the encoder's representation of two worlds that differ only inside that region. The predictor's decision keeps a stationary object in part and one carried inside a container not at all, and loses a moving one within 0.3 s (0.5 s under V-JEPA's own tube mask; ViT-H keeps it to 1.1 s at pretraining's 90% masking ratio); in projection a trace remains, below the midpoint, at 14-60% of what a baseline co...

</details>

<details>
<summary>Share</summary>

```
Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object

Video world models track objects they can see; we ask what they keep of objects they cannot.

arXiv: https://arxiv.org/abs/2610.07355

#worldmodels #robotics
```

</details>

---

### [Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control](https://arxiv.org/abs/2610.06582)

**Authors:** Shengtao Wen, Xiang Chen, Yu Tian, Lingbing Guo, Lina Gong et al. (6 authors)

**Published:** 2026-10-05 | **Categories:** cs.AI, cs.CL, cs.IR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06582) | [PDF](https://arxiv.org/pdf/2610.06582)

<details>
<summary>Abstract</summary>

World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator buffering. We study how asynchronous execution changes the action semantics assumed within world-model controllers, rather than treating it only as an external control disturbance. Through controlled interventions, we identify two architecture-dependent failure modes: planning-based controllers such as TD-MPC2 suffer from a future-action timeline mismatch between imagined and exe...

</details>

<details>
<summary>Share</summary>

```
Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control

World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator...

arXiv: https://arxiv.org/abs/2610.06582

#worldmodels #robotics
```

</details>

---

### [Generative World Models Enable Predictive Control of Laser Melt Pool Dynamics](https://arxiv.org/abs/2610.06250)

**Authors:** Yiyang Yan, Markus Bambach, Mohamadreza Afrasiabi

**Published:** 2026-10-05 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06250) | [PDF](https://arxiv.org/pdf/2610.06250)

<details>
<summary>Abstract</summary>

World models, which learn how environments respond to actions, are emerging as a powerful paradigm for planning through imagined futures, transforming decision-making across games, robotics and autonomous driving. Bringing this capability to manufacturing could enable process decisions on timescales inaccessible to high-fidelity simulation. Here we introduce a generative world model for localized highly dynamic laser melt pool that predicts evolution from histories of temperature and phase morphology under candidate actions. Its generative latent dynamics capture the effects of unresolved melt...

</details>

<details>
<summary>Share</summary>

```
Generative World Models Enable Predictive Control of Laser Melt Pool Dynamics

World models, which learn how environments respond to actions, are emerging as a powerful paradigm for planning through imagined futures, transforming decision-making across games, robotics and autonomous driving.

arXiv: https://arxiv.org/abs/2610.06250

#worldmodels #robotics
```

</details>

---

### [When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models](https://arxiv.org/abs/2610.05550)

**Authors:** Rui Min, Xianyao Li, Fang Xu, Jing Du

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.05550) | [PDF](https://arxiv.org/pdf/2610.05550)

<details>
<summary>Abstract</summary>

The component that dominates a latent world model's prediction error need not be the one whose repair most improves action selection. We show this by comparing action sequences from identical physical starts and separating endpoint error into a candidate-pool center and action-relative responses. Across four model families and four tasks, a confirmation pool of 256 new starts per task and 300 shared candidates per start shows that center error dominates MSE in 14/16 model-task cells. Yet in six of these cells, an oracle that corrects only the action-relative responses yields better physical ra...

</details>

<details>
<summary>Share</summary>

```
When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models

The component that dominates a latent world model's prediction error need not be the one whose repair most improves action selection.

arXiv: https://arxiv.org/abs/2610.05550

#worldmodels #robotics
```

</details>

---

### [How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models](https://arxiv.org/abs/2610.04988)

**Authors:** Lama Moukheiber, Haotian Xue, Yongxin Chen

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04988) | [PDF](https://arxiv.org/pdf/2610.04988)

<details>
<summary>Abstract</summary>

Latent world models plan by rolling a frozen predictor forward under candidate action sequences and ranking the candidates by the latent distance between their imagined end state and the goal. However, this ranking breaks down when the goal lies several plans away, because the latent distance measures how closely an end state resembles the goal rather than how far it remains from reaching it. To address this, we propose TEMPO, a temporal-distance planning objective that leaves the world model untouched, learns only from the demonstrations already used to train it, and adds negligible cost to t...

</details>

<details>
<summary>Share</summary>

```
How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models

Latent world models plan by rolling a frozen predictor forward under candidate action sequences and ranking the candidates by the latent distance between their imagined end state and the goal.

arXiv: https://arxiv.org/abs/2610.04988

#worldmodels #robotics
```

</details>

---

### [Frozen in a Frame: The Velocity Blind Spot in JEPA World Models](https://arxiv.org/abs/2610.04585)

**Authors:** Tinghe Zhang, Chunyu Liu, Yu Leon Liu, Zerui Zhao, Jiaheng Chen et al. (9 authors)

**Published:** 2026-10-03 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04585) | [PDF](https://arxiv.org/pdf/2610.04585)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) for world modeling train an encoder so a predictor maps a current embedding and action to the next frame's embedding, always from a single rendered frame. This has a structural blind spot: a renderer without motion blur draws a scene from configuration alone, so a single-frame embedding carries no velocity information, for any encoder, including the official released LeWM weights. We confirm this on official checkpoints across four real benchmarks (PushT, Reacher, Cube, TwoRoom): every linear velocity probe sits at or below chance while position...

</details>

<details>
<summary>Share</summary>

```
Frozen in a Frame: The Velocity Blind Spot in JEPA World Models

Joint-embedding predictive architectures (JEPAs) for world modeling train an encoder so a predictor maps a current embedding and action to the next frame's embedding, always from a single rendered frame.

arXiv: https://arxiv.org/abs/2610.04585

#worldmodels #robotics
```

</details>

---

### [Action-Consequence Alignment for Reliable Planning and Self-Improving in Latent World Models](https://arxiv.org/abs/2610.04539)

**Authors:** Jinping Wang1, Zhiqiang Gao, Xiantong Zhen, Ling Shao

**Published:** 2026-10-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04539) | [PDF](https://arxiv.org/pdf/2610.04539)

<details>
<summary>Abstract</summary>

Latent world models learn to predict observed transitions, yet low prediction error alone does not guarantee reliable planning. Inspired by self tickling experiments in neuroscience showing that disrupting motor sensory correspondence increases prediction mismatch, we examine whether learned world models preserve an analogous action consequence correspondence.The results show nearby alternatives can receive lower prediction errors despite producing physical outcomes farther from the recorded target. With that future treated as a goal, this reveals a concrete prediction planning mismatch: the m...

</details>

<details>
<summary>Share</summary>

```
Action-Consequence Alignment for Reliable Planning and Self-Improving in Latent World Models

Latent world models learn to predict observed transitions, yet low prediction error alone does not guarantee reliable planning.

arXiv: https://arxiv.org/abs/2610.04539

#worldmodels #robotics
```

</details>

---

### [Keeping JEPA World Models Plannable When Little of the Frame Moves](https://arxiv.org/abs/2610.03137)

**Authors:** Florian Strohm, Patrick Wagner, Jannik Schwab, Marco Huber

**Published:** 2026-10-02 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.03137) | [PDF](https://arxiv.org/pdf/2610.03137)

<details>
<summary>Abstract</summary>

Specifying a goal in language rather than as a goal frame is a natural interface for planning with a latent world model, but testing it needs scenes in which language must discriminate between several objects. We build SLIM, a pushing benchmark with several small objects and paired visual and language goals on identical scenes. On SLIM a LeWM world model that solves PushT succeeds on under 1% of trials, although a scripted controller with simulator state solves every tier. Probes locate the failure in the encoder: its latent is nearly action-insensitive, neither pusher nor object positions can...

</details>

<details>
<summary>Share</summary>

```
Keeping JEPA World Models Plannable When Little of the Frame Moves

Specifying a goal in language rather than as a goal frame is a natural interface for planning with a latent world model, but testing it needs scenes in which language must discriminate between several objects.

arXiv: https://arxiv.org/abs/2610.03137

#worldmodels #robotics
```

</details>

---

### [Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092)

**Authors:** Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi et al. (13 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.01092) | [PDF](https://arxiv.org/pdf/2610.01092)

<details>
<summary>Abstract</summary>

Video generation models are increasingly being explored as world simulators for embodied planning and learning. To do so effectively, these models must not only generate visually appealing frames, but also predict how environments dynamically evolve when executing goal-directed actions. While evaluating these capabilities is crucial, existing benchmarks focus mainly on single short actions or step-by-step instructions. This leaves multi-step physical reasoning underexplored, especially in egocentric video generation that requires planning to simulate proper execution to accomplish high-level g...

</details>

<details>
<summary>Share</summary>

```
Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation

Video generation models are increasingly being explored as world simulators for embodied planning and learning.

arXiv: https://arxiv.org/abs/2610.01092

#worldmodels #robotics
```

</details>

---

### [PROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205)

**Authors:** Zheng-Hui Huang, Guixu Lin, Yu-Ju Tsai, Jian-Kai Zhu, Fengbo Lan et al. (9 authors)

**Published:** 2026-10-01 (updated 2026-10-05) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02205) | [PDF](https://arxiv.org/pdf/2610.02205) | [Project Page](https://alaya-lab.github.io/PROWBench)

<details>
<summary>Abstract</summary>

Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines. However, their visual adherence to explicit rules and interactions remains insufficiently evaluated. Existing benchmarks assess visual quality, controllability, and instruction or physical adherence, but rarely test fidelity to fine-grained, program-specified world events. We introduce PROWBench, comprising 170 programmatically constructed episodes and 600 proxy videos covering diverse scenes and interactions. PROWBench logs entity states and timestam...

</details>

<details>
<summary>Share</summary>

```
PROWBench: Do Video Models Render What the Program Specifies?

Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines.

arXiv: https://arxiv.org/abs/2610.02205
Project page: https://alaya-lab.github.io/PROWBench

#worldmodels #robotics
```

</details>

---

### [Learning Commute-Time-Preserving World Models for Planning](https://arxiv.org/abs/2610.01373)

**Authors:** Michael Hauri, Peter Buttaroni, Fabian A. Mikulasch, Friedemann Zenke

**Published:** 2026-10-01 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.01373) | [PDF](https://arxiv.org/pdf/2610.01373)

<details>
<summary>Abstract</summary>

World models allow agents to plan in latent space by choosing a sequence of actions that most reduces the distance to a given goal state. Thus, planning can benefit from latent representations whose distances mirror commute-times in the environment. The spectral embedding space of the graph Laplacian provides such a representation, if it obeys a specific eigenvalue-dependent scaling. Unfortunately, instantiating the graph Laplacian is intractable in large, continuous environments. Self-supervised learning offers a natural route to such commute-time-preserving embeddings at scale. However, here...

</details>

<details>
<summary>Share</summary>

```
Learning Commute-Time-Preserving World Models for Planning

World models allow agents to plan in latent space by choosing a sequence of actions that most reduces the distance to a given goal state.

arXiv: https://arxiv.org/abs/2610.01373

#worldmodels #robotics
```

</details>

---

### [iSEE: Object Permanence Through Self-Supervision](https://arxiv.org/abs/2610.01201)

**Authors:** Pramish Paudel, Ajad Chhatkuli, Luc Van Gool, Danda Pani Paudel

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01201) | [PDF](https://arxiv.org/pdf/2610.01201) | [Project Page](https://insait-institute.github.io/iSEE/)

<details>
<summary>Abstract</summary>

Object permanence, keeping track of an object's identity and position while it is occluded, is central to video representations that track, predict and plan. Trackers that achieve it learn from boxes, track identities and visibility labels. On the other hand, self-supervised object-centric methods discover objects without labels: through slot attention, it represents a video as slots that bind to objects and follow them across frames. However, these slots are lost under occlusion, making the desired permanence impossible. Reasoning permanence is a hard problem because it requires to detect whe...

</details>

<details>
<summary>Share</summary>

```
iSEE: Object Permanence Through Self-Supervision

Object permanence, keeping track of an object's identity and position while it is occluded, is central to video representations that track, predict and plan.

arXiv: https://arxiv.org/abs/2610.01201
Project page: https://insait-institute.github.io/iSEE/

#worldmodels #robotics
```

</details>

---

### [Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358)

**Authors:** Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao et al. (17 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.40358) | [PDF](https://arxiv.org/pdf/2609.40358)

<details>
<summary>Abstract</summary>

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video ge...

</details>

<details>
<summary>Share</summary>

```
Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles.

arXiv: https://arxiv.org/abs/2609.40358

#worldmodels #robotics
```

</details>

---

### [Code to Control: Synthesizing Parameterized Reactive Controllers](https://arxiv.org/abs/2609.38733)

**Authors:** Zergham Ahmed, Joshua B. Tenenbaum, Chris Bates, Samuel J. Gershman

**Published:** 2026-09-30 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38733) | [PDF](https://arxiv.org/pdf/2609.38733) | [Code](https://github.com/ZerghamAhmed/code-to-control)

<details>
<summary>Abstract</summary>

Recent LLM-based approaches to control either invoke a language model to select actions or synthesize world models that require planning at every decision, introducing latency that can limit real-time use. We introduce Code to Control, an approach that synthesizes Python controllers which execute directly as policies. Code to Control separates program structure from parameters. An LLM synthesizes the controller structure, while derivative-free search fits its parameters for continuous control using feedback from the environment. Once learned, the resulting controllers require neither LLM infer...

</details>

<details>
<summary>Share</summary>

```
Code to Control: Synthesizing Parameterized Reactive Controllers

Recent LLM-based approaches to control either invoke a language model to select actions or synthesize world models that require planning at every decision, introducing latency that can limit real-time use.

arXiv: https://arxiv.org/abs/2609.38733
Code: https://github.com/ZerghamAhmed/code-to-control

#worldmodels #robotics
```

</details>

---

### [FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning](https://arxiv.org/abs/2610.05483)

**Authors:** R. Khorrambakht, Joseph Amigo, Félix Lebel, Leon Seetoo, Jean Ponce et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.05483) | [PDF](https://arxiv.org/pdf/2610.05483)

<details>
<summary>Abstract</summary>

World--action models (WAMs) promise a unified model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination. However, existing joint video--action models often use computationally heavy, fixed-horizon backbones ill-suited to streaming inference and stable long-horizon open-loop rollouts. We introduce FLEX-WAM, a Flexible and Efficient Block-Causal World--Action Model for unified simulation and policy inference. FLEX-WAM supports variable-length contexts and non-causal prediction horizons, as well as infinite autoregressive generation frame by...

</details>

<details>
<summary>Share</summary>

```
FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning

World--action models (WAMs) promise a unified model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination.

arXiv: https://arxiv.org/abs/2610.05483

#worldmodels #robotics
```

</details>

---

### [PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation](https://arxiv.org/abs/2610.04916)

**Authors:** Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Junwei Yang et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04916) | [PDF](https://arxiv.org/pdf/2610.04916)

<details>
<summary>Abstract</summary>

Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations. However, existing agentic navigation methods often struggle to translate distant goals into coherent local decisions in large-scale physical environments. Their reliance on linguistic reasoning over transient observations or limited history constrains anticipation of the consequences of actions and future conditions, despite the importance of such foresight for navigating long and complex urban routes. To bridge this gap, we propose PreAct-Nav, an agentic navigation...

</details>

<details>
<summary>Share</summary>

```
PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation

Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations.

arXiv: https://arxiv.org/abs/2610.04916

#worldmodels #robotics
```

</details>

---

### [Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation](https://arxiv.org/abs/2610.02368)

**Authors:** Shukai Gong, Xuanran Zhai, Yintianrun Zhang, Ruopeng Cui, Ye Huang et al. (19 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.02368) | [PDF](https://arxiv.org/pdf/2610.02368)

<details>
<summary>Abstract</summary>

Long-horizon compositional manipulation has become increasingly important for real-world robot deployment, where a single task involves multiple coordinated subtasks. Existing world-action models (WAMs) jointly predict short-horizon visual futures and actions, but typically lack explicit subtask-level reasoning. We propose Visual Goal-conditioned Action Reasoning (ViGAR), a hierarchical framework that factorizes manipulation into a visual subgoal planner and a subgoal executor. Given the current observation and global instruction, the subgoal planner predicts a visual subgoal for the next subt...

</details>

<details>
<summary>Share</summary>

```
Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation

Long-horizon compositional manipulation has become increasingly important for real-world robot deployment, where a single task involves multiple coordinated subtasks.

arXiv: https://arxiv.org/abs/2610.02368

#worldmodels #robotics
```

</details>

---

### [ReWAM: Reciprocal World Action Models for Interactive Autonomous Driving](https://arxiv.org/abs/2609.39245)

**Authors:** Benshan Ma, Pei Liu, Ruiguo Zhong, Lang Zhang, Mingyue Feng et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.39245) | [PDF](https://arxiv.org/pdf/2609.39245)

<details>
<summary>Abstract</summary>

In interactive scenarios, an autonomous driving system is required to generate ego actions under the influence of other agents' behaviors. Existing World Action Models (WAMs) typically model other agents as components of the world model rather than as decision-makers that fundamentally shape the action of the ego agent, which impairs their performance in dense interaction scenarios. We introduce Reciprocal World Action Models (ReWAM), a game-theoretic world action modeling framework that captures the reciprocal influence between the ego agent and other agents by representing them as conditiona...

</details>

<details>
<summary>Share</summary>

```
ReWAM: Reciprocal World Action Models for Interactive Autonomous Driving

In interactive scenarios, an autonomous driving system is required to generate ego actions under the influence of other agents' behaviors.

arXiv: https://arxiv.org/abs/2609.39245

#worldmodels #robotics
```

</details>

---

### [GeoWM: Efficient Direct World Modeling in Explicit Geometry](https://arxiv.org/abs/2610.07381)

**Authors:** Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai

**Published:** 2026-10-05 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.07381) | [PDF](https://arxiv.org/pdf/2610.07381)

<details>
<summary>Abstract</summary>

Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics. A common paradigm is to use world models to predict future images or latent representations of the environment and subsequently recover geometry from these predictions. However, this paradigm does not explicitly model geometric structure and typically relies on recursive rollouts to reach longer prediction horizons, leading to error accumulation and increasing computational cost. To address these limitations, we present GeoWM, a geometry world model that directly forecasts future scene geom...

</details>

<details>
<summary>Share</summary>

```
GeoWM: Efficient Direct World Modeling in Explicit Geometry

Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics.

arXiv: https://arxiv.org/abs/2610.07381

#worldmodels #robotics
```

</details>

---

### [Identifiable World Models from Pretrained Diffusion Representations](https://arxiv.org/abs/2610.07028)

**Authors:** Ruchi Sandilya, Conor Liston, Logan Grosenick

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.07028) | [PDF](https://arxiv.org/pdf/2610.07028)

<details>
<summary>Abstract</summary>

Diffusion-based world models can generate and predict trajectories in high-dimensional dynamical systems, but predictive accuracy does not imply that their latent coordinates recover the underlying state variables or causal interactions. We ask whether a frozen pretrained diffusion model can be equipped with identifiable coordinates without retraining its generative backbone. We show that auxiliary-variable nonlinear ICA guarantees can be transferred to Contrastive Diffusion Alignment (ConDA), which learns only a lightweight alignment map on top of frozen diffusion latents. Under standard TCL/...

</details>

<details>
<summary>Share</summary>

```
Identifiable World Models from Pretrained Diffusion Representations

Diffusion-based world models can generate and predict trajectories in high-dimensional dynamical systems, but predictive accuracy does not imply that their latent coordinates recover the underlying state variables or...

arXiv: https://arxiv.org/abs/2610.07028

#worldmodels #robotics
```

</details>

---

### [DreamTest: World-Model Surrogates for Search-Based Testing of Deep Reinforcement Learning Agents](https://arxiv.org/abs/2610.04494)

**Authors:** Qinghua Xu, Guancheng Wang, Boxi Yu, Liting Lin, Lionel Briand

**Published:** 2026-10-03 | **Categories:** cs.SE, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.04494) | [PDF](https://arxiv.org/pdf/2610.04494)

<details>
<summary>Abstract</summary>

Testing deep reinforcement learning (DRL) agents in cyber-physical systems aims to uncover diverse failures before deployment, but each execution can be expensive. Surrogate-assisted testing reduces this cost by learning to predict which test configurations are likely to fail. Prior surrogates treat the system as a black box and predict pass or fail outcomes directly; we instead model how a test unfolds and estimate failure from an imagined episode. We introduce DreamTest, a world-model surrogate for testing DRL agents. DreamTest adapts a recurrent state-space model to learn agent behaviour an...

</details>

<details>
<summary>Share</summary>

```
DreamTest: World-Model Surrogates for Search-Based Testing of Deep Reinforcement Learning Agents

Testing deep reinforcement learning (DRL) agents in cyber-physical systems aims to uncover diverse failures before deployment, but each execution can be expensive.

arXiv: https://arxiv.org/abs/2610.04494

#worldmodels #robotics
```

</details>

---

### [A differentiable Lagrangian-coupled 3D Gaussian Splatting-SPH model for forward simulation and inverse analysis in solid mechanics](https://arxiv.org/abs/2610.04336)

**Authors:** Tian Xu, Soroush Atashi, Tianju Xue

**Published:** 2026-10-03 | **Categories:** cs.CV, physics.comp-ph | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04336) | [PDF](https://arxiv.org/pdf/2610.04336)

<details>
<summary>Abstract</summary>

Recent advances in generative world models have increased interest in digital models that reproduce both the appearance of real objects and their response to physical interaction. Three-dimensional reconstruction techniques, including 3D Gaussian Splatting, capture detailed surface geometry and appearance from images and videos. However, extending these representations beyond plausible animation to mechanically interpretable models for constitutive behavior, boundary conditions, and inverse parameter identification remains less explored. In this work, a differentiable Lagrangian-coupled 3DGS-s...

</details>

<details>
<summary>Share</summary>

```
A differentiable Lagrangian-coupled 3D Gaussian Splatting-SPH model for forward simulation and inverse analysis in solid mechanics

Recent advances in generative world models have increased interest in digital models that reproduce both the appearance of real objects and their response to physical interaction.

arXiv: https://arxiv.org/abs/2610.04336

#worldmodels #robotics
```

</details>

---

### [EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI](https://arxiv.org/abs/2610.04301)

**Authors:** Kabir Swain, Sijie Han, Antonio Torralba

**Published:** 2026-10-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.04301) | [PDF](https://arxiv.org/pdf/2610.04301)

<details>
<summary>Abstract</summary>

Large datasets and high capacity models have accelerated progress in vision and language. This work introduces a platform aimed at bringing comparable gains to embodied learning, world models, and robotics. We present EnvDreamer, a framework that uses large language and vision language models to generate Unreal Engine 5 environments for embodied AI and robot training. EnvDreamer enables sampling of large, diverse, interactive, customizable, and validator passed virtual environments for training and evaluation across navigation, interaction, and manipulation. We illustrate the platform with a l...

</details>

<details>
<summary>Share</summary>

```
EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI

Large datasets and high capacity models have accelerated progress in vision and language.

arXiv: https://arxiv.org/abs/2610.04301

#worldmodels #robotics
```

</details>

---

### [What Should World Models Forget? Stratified Retention for Continual Adaptation](https://arxiv.org/abs/2610.03713)

**Authors:** Nishit Anand, Ramani Duraiswami, Dinesh Manocha

**Published:** 2026-10-02 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.03713) | [PDF](https://arxiv.org/pdf/2610.03713)

<details>
<summary>Abstract</summary>

Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding it is required behavior rather than a defect. Non-stationary ground truth is well studied in the concept drift literature and in the temporal factuality of language models, but has not been formulated...

</details>

<details>
<summary>Share</summary>

```
What Should World Models Forget? Stratified Retention for Continual Adaptation

Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely.

arXiv: https://arxiv.org/abs/2610.03713

#worldmodels #robotics
```

</details>

---

### [ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models](https://arxiv.org/abs/2610.03356)

**Authors:** Hainiu Xu, Vítor N. Lourenço, Mohnish Dubey, Yunfei Bai, Yulan He et al. (10 authors)

**Published:** 2026-10-02 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.03356) | [PDF](https://arxiv.org/pdf/2610.03356)

<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, and can therefore cause irreversible equipment damage, production loss, or personnel harm. Existing be...

</details>

<details>
<summary>Share</summary>

```
ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models

Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles.

arXiv: https://arxiv.org/abs/2610.03356

#worldmodels #robotics
```

</details>

---

### [Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models](https://arxiv.org/abs/2610.03154)

**Authors:** Jonas Kneifl, Jakub Skalski, Bartłomiej Twardowski, Kamil Deja

**Published:** 2026-10-02 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.03154) | [PDF](https://arxiv.org/pdf/2610.03154)

<details>
<summary>Abstract</summary>

Video generation models produce strikingly realistic sequences and are increasingly proposed as world models, yet recent benchmarks reveal pronounced deficits in their physical reasoning. This raises the question of whether these models internalize physical principles or merely reproduce familiar motion patterns. We address this by probing internal representations of video Diffusion Transformers (DiTs) for simulator-derived ground-truth physical quantities spanning kinematic motion and rigid-body dynamics under gravity and contact. We find that these quantities are linearly decodable with high...

</details>

<details>
<summary>Share</summary>

```
Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models

Video generation models produce strikingly realistic sequences and are increasingly proposed as world models, yet recent benchmarks reveal pronounced deficits in their physical reasoning.

arXiv: https://arxiv.org/abs/2610.03154

#worldmodels #robotics
```

</details>

---

### [Counterfactual Action Evaluation, Observation Bottlenecks, and Representation Geometry in Joint-Embedding Predictive World Models](https://arxiv.org/abs/2610.02860)

**Authors:** Arjun Subramanian

**Published:** 2026-10-02 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.02860) | [PDF](https://arxiv.org/pdf/2610.02860)

<details>
<summary>Abstract</summary>

Low latent prediction error does not establish that a world model distinguishes the consequences of its actions. We introduce an evaluation protocol that traces the same intervention through simulator state, raster observations, target embeddings, and predictor outputs. Exact simulator-state forks in a controlled deformable-physics testbed reveal distinct bottlenecks. Changed commands alter particle motion, yet 41.5% of one-step raster pairs are identical. Observation loss is not the whole explanation: among 579 high-visibility counterfactuals, median predictor-to-target response is 0.0051 and...

</details>

<details>
<summary>Share</summary>

```
Counterfactual Action Evaluation, Observation Bottlenecks, and Representation Geometry in Joint-Embedding Predictive World Models

Low latent prediction error does not establish that a world model distinguishes the consequences of its actions.

arXiv: https://arxiv.org/abs/2610.02860

#worldmodels #robotics
```

</details>

---

### [SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726)

**Authors:** Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu et al. (9 authors)

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.02726) | [PDF](https://arxiv.org/pdf/2610.02726)

<details>
<summary>Abstract</summary>

Flow-matching-based multi-view world models generate realistic videos, but are commonly restricted to fixed camera rigs. Extending them to continuously varying camera poses requires paired pose--video observations with dense pose coverage, which are costly to acquire. We introduce \emph{SymRegFlow}, a symmetry-regularized flow-matching framework for multi-view-consistent video generation across continuous viewpoints without ground-truth novel-view RGB supervision. For each target pose, SymRegFlow geometrically warps source views into noisy anchors and combines masked dual-anchor supervision wi...

</details>

<details>
<summary>Share</summary>

```
SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models

Flow-matching-based multi-view world models generate realistic videos, but are commonly restricted to fixed camera rigs.

arXiv: https://arxiv.org/abs/2610.02726

#worldmodels #robotics
```

</details>

---

### [SpectralCache: Accelerating Diffusion-Based World Models via Spectral Feature Caching](https://arxiv.org/abs/2610.02660)

**Authors:** Zhendong Mi, Pu Zhao, Ziyu Hu, Xiaodong Yu, Yanzhi Wang et al. (7 authors)

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.02660) | [PDF](https://arxiv.org/pdf/2610.02660)

<details>
<summary>Abstract</summary>

Diffusion-based world models enable high-quality interactive environment generation but suffer from substantial inference overhead due to repeated Transformer evaluations during denoising. Existing caching methods mainly exploit temporal redundancy at the feature or token level, leaving the underlying mathematical structure of diffusion features largely unexplored. In this work, we reveal that world-model features exhibit highly stable singular subspaces across nearby denoising steps, while their singular values follow predictable evolution patterns. Building on this observation, we propose Sp...

</details>

<details>
<summary>Share</summary>

```
SpectralCache: Accelerating Diffusion-Based World Models via Spectral Feature Caching

Diffusion-based world models enable high-quality interactive environment generation but suffer from substantial inference overhead due to repeated Transformer evaluations during denoising.

arXiv: https://arxiv.org/abs/2610.02660

#worldmodels #robotics
```

</details>

---

### [How To Train Your World Model: Fine-tuning vs RAG for LM-based World Modeling](https://arxiv.org/abs/2610.02542)

**Authors:** Dhananjay Ashok, Shantanu Agarwal, Vivek Datla, Jonathan May, Alfy Samuel

**Published:** 2026-10-01 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.02542) | [PDF](https://arxiv.org/pdf/2610.02542)

<details>
<summary>Abstract</summary>

World models (WMs) simulate the transition dynamics of environments, enabling agents to plan over the consequences of their actions. In text-based environments, fine-tuning a Language Model (LM) to serve as a WM has emerged as a dominant paradigm. However, despite the widespread success of non-parametric approaches such as Retrieval Augmented Generation (RAG), retrieval for LM-based world modelling remains underexplored. We conduct a systematic evaluation across five diverse environments spanning embodied, web navigation and social settings, comparing fine-tuning and RAG-based approaches for L...

</details>

<details>
<summary>Share</summary>

```
How To Train Your World Model: Fine-tuning vs RAG for LM-based World Modeling

World models (WMs) simulate the transition dynamics of environments, enabling agents to plan over the consequences of their actions.

arXiv: https://arxiv.org/abs/2610.02542

#worldmodels #robotics
```

</details>

---

### [IGNITE Tokamak World Model Architecture](https://arxiv.org/abs/2610.02515)

**Authors:** Peter Steiner, Azarakhsh Jalalvand, Nathaniel Chen, Kouroche Bouchiat, Ricardo Shousha et al. (7 authors)

**Published:** 2026-10-01 | **Categories:** physics.plasm-ph, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.02515) | [PDF](https://arxiv.org/pdf/2610.02515)

<details>
<summary>Abstract</summary>

We introduce IGNITE, a generative world foundation model for fusion plasma behavior simulation trained in a self-supervised manner from over a decade of unlabeled experimental data at the DIII-D National Fusion Facility. The core of IGNITE is a dynamics model that can simulate DIII-D discharges from a given set of actuator trajectories. These trajectories can be supplied or generated on-the-fly from a textual prompt or from desired experimental outcomes. The model architecture consists of several spatio-temporal tokenizers that embed the different input modalities, including time-series like s...

</details>

<details>
<summary>Share</summary>

```
IGNITE Tokamak World Model Architecture

We introduce IGNITE, a generative world foundation model for fusion plasma behavior simulation trained in a self-supervised manner from over a decade of unlabeled experimental data at the DIII-D National Fusion Facility.

arXiv: https://arxiv.org/abs/2610.02515

#worldmodels #robotics
```

</details>

---

### [Network World Models as Environments for Algorithm Design on Complex Systems](https://arxiv.org/abs/2610.01048)

**Authors:** Rishab Alagharu, Hongji Pu, Zeeshan Memon, Xinyuan Song, Yuntong Hu et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.01048) | [PDF](https://arxiv.org/pdf/2610.01048)

<details>
<summary>Abstract</summary>

World models, which simulate an environment and predict how it changes under actions, are increasingly used in real-world applications such as robotics. Complex systems call for the same tool because the effect of an action is not immediate. Seeding nodes for a campaign, or immunizing nodes against an epidemic, changes little on its own; what matters is the outcome that unfolds over the steps that follow. Designing an algorithm that selects such actions to maximize expected performance on a task is inherently iterative, and every candidate must be scored by the outcome it produces. Obtaining t...

</details>

<details>
<summary>Share</summary>

```
Network World Models as Environments for Algorithm Design on Complex Systems

World models, which simulate an environment and predict how it changes under actions, are increasingly used in real-world applications such as robotics.

arXiv: https://arxiv.org/abs/2610.01048

#worldmodels #robotics
```

</details>

---

### [Calibration-risk routing for controlled world-model adaptation](https://arxiv.org/abs/2610.01001)

**Authors:** Yifan Zhang, Liang Zheng

**Published:** 2026-10-01 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.01001) | [PDF](https://arxiv.org/pdf/2610.01001)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (MBRL) can exploit simulated experience, but a simulator-to-target shift creates a model-selection problem: correcting the simulator and fitting the target directly can each fail under limited target data. We introduce the Model-Corrected World Model (MC-WM), which separates initial target data into disjoint fit, selection, and calibration partitions and deploys the family with lower standardized calibration risk. A learned confidence signal and deterministic validity predicates weight one-step imagined policy updates without rewriting physical rewards. We ev...

</details>

<details>
<summary>Share</summary>

```
Calibration-risk routing for controlled world-model adaptation

Model-based reinforcement learning (MBRL) can exploit simulated experience, but a simulator-to-target shift creates a model-selection problem: correcting the simulator and fitting the target directly can each fail und...

arXiv: https://arxiv.org/abs/2610.01001

#worldmodels #robotics
```

</details>

---

### [Variational Streaming Flow: Probabilistic Forecasting in Physical Time](https://arxiv.org/abs/2610.00976)

**Authors:** Hans Hao-Hsun Hsu, Minseon Gwak, Soon Hoe Lim, Pan Li, N. Benjamin Erichson

**Published:** 2026-10-01 (updated 2026-10-03) | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.00976) | [PDF](https://arxiv.org/pdf/2610.00976)

<details>
<summary>Abstract</summary>

Probabilistic forecasting is important for predicting complex dynamical systems because intrinsic randomness and incomplete observations can cause the same observed state to evolve into multiple plausible futures. While flow matching is a flexible approach for probabilistic forecasting, it is computationally expensive. Streaming flow (SF) reformulates this approach to model temporal evolution efficiently by learning a continuous velocity field directly in physical time. However, SF learns a deterministic velocity field. Thus, it provides only a single future trajectory for a given fixed initia...

</details>

<details>
<summary>Share</summary>

```
Variational Streaming Flow: Probabilistic Forecasting in Physical Time

Probabilistic forecasting is important for predicting complex dynamical systems because intrinsic randomness and incomplete observations can cause the same observed state to evolve into multiple plausible futures.

arXiv: https://arxiv.org/abs/2610.00976

#worldmodels #robotics
```

</details>

---

### [Kepler: Auditable World Models for ARC-AGI-3](https://arxiv.org/abs/2610.00834)

**Authors:** Wensen Wu

**Published:** 2026-09-30 | **Categories:** cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.00834) | [PDF](https://arxiv.org/pdf/2610.00834)

<details>
<summary>Abstract</summary>

ARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation. We present Kepler, an open-source harness that represents hypotheses as executable world models and validates them through retrospective transition checks and conditional prediction checks. Under one frozen Claude Opus 5 configuration, Kepler obtained a server-verified 100.00 RHAE on all 25 public games, with no per-game model selection or score-conditioned reruns. On 181 of 183 completed levels, the final Opus attempt used no more actions than the corresponding median-human bas...

</details>

<details>
<summary>Share</summary>

```
Kepler: Auditable World Models for ARC-AGI-3

ARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation.

arXiv: https://arxiv.org/abs/2610.00834

#worldmodels #robotics
```

</details>

---

### [SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.00686)

**Authors:** Mikhail Dereviannykh, Vikram Voleti, Simon Donne, Mallikarjun Byrasandra Ramalinga Reddy, Shimon Vainer et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.00686) | [PDF](https://arxiv.org/pdf/2610.00686)

<details>
<summary>Abstract</summary>

Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models. The choice of scene tokenizer is paramount for the optimal performance of each of these, both in terms of fidelity and semantics. Flexible-length, coarse-to-fine tokenizers yield exactly that: the first coarse tokens carry the clip's global semantics while later tokens further specify details. Existing flexible tokenizers only apply a representation-alignment (REPA) loss on early decoder hidden states, a target the decoder can partly meet from its noised input ins...

</details>

<details>
<summary>Share</summary>

```
SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation

Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models.

arXiv: https://arxiv.org/abs/2610.00686

#worldmodels #robotics
```

</details>

---

### [MEND: Label-Free Detection, Localisation, and Correction of Latent Hallucination in World Models](https://arxiv.org/abs/2609.39182)

**Authors:** Ali J Alrasheed, Aryan Yazdan Parast, Basim Azam, James Bailey, Naveed Akhtar

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.39182) | [PDF](https://arxiv.org/pdf/2609.39182)

<details>
<summary>Abstract</summary>

World Models are appearing as the next major frontier in computer vision. However, their robustness is currently largely unexplored. We identify the phenomenon of hallucination in latent World Models: given a state and an action, the predicted next latent can decode to a scene that never occurs. Because the prediction is statistically ordinary and is fed back autoregressively by the model, the error is both silent and compounding. We study whether such latent hallucination can be detected, localised, and corrected at inference time, on a frozen self-supervised world model in the absence of gro...

</details>

<details>
<summary>Share</summary>

```
MEND: Label-Free Detection, Localisation, and Correction of Latent Hallucination in World Models

World Models are appearing as the next major frontier in computer vision.

arXiv: https://arxiv.org/abs/2609.39182

#worldmodels #robotics
```

</details>

---

### [FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation](https://arxiv.org/abs/2609.38839)

**Authors:** Bo Yin, Xiaobin Hu, Jiaqi Zhao, Shuicheng Yan

**Published:** 2026-09-30 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.38839) | [PDF](https://arxiv.org/pdf/2609.38839)

<details>
<summary>Abstract</summary>

Long-horizon video generation requires models to effectively leverage an increasingly long generation history. As the generated history grows, retaining all previous content becomes increasingly expensive and redundant, making effective historical selection essential. Existing approaches often determine historical relevance based on the current content. However, information relevant to the present is not necessarily useful for future generation, while seemingly less relevant history may become important later. Our key insight is that historical information should be selected according to its r...

</details>

<details>
<summary>Share</summary>

```
FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation

Long-horizon video generation requires models to effectively leverage an increasingly long generation history.

arXiv: https://arxiv.org/abs/2609.38839

#worldmodels #robotics
```

</details>

---

### [Completion Aware Guidance for World Action Models](https://arxiv.org/abs/2610.01559)

**Authors:** Seungyeon Kim, Junhoo Lee, Baekseung Kim, Minkyu Kim, Nojun Kwak

**Published:** 2026-10-01 (updated 2026-10-06) | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.01559) | [PDF](https://arxiv.org/pdf/2610.01559)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) predict visual futures and robot actions, yet they remain susceptible to task-incomplete imagination, where plausible, action-consistent predictions omit the transition needed for task completion. In this paper, we show that this failure is not inherent to the world model backbone, but emerges when adapted for short-chunk control, which can repeatedly favor plausible local continuations over task-completing transitions. To address this, we introduce Completion Aware Guidance (CAG), a training-free sampling method that guides generation toward task completion. Across...

</details>

<details>
<summary>Share</summary>

```
Completion Aware Guidance for World Action Models

World Action Models (WAMs) predict visual futures and robot actions, yet they remain susceptible to task-incomplete imagination, where plausible, action-consistent predictions omit the transition needed for task compl...

arXiv: https://arxiv.org/abs/2610.01559

#worldmodels #robotics
```

</details>

---

### [Cross-entropy optimization with prioritized constraints](https://arxiv.org/abs/2610.01319)

**Authors:** Francisco Roldan Sanchez, Pau de las Heras Molins, David Fridovich-Keil, Georgios Bakirtzis

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.01319) | [PDF](https://arxiv.org/pdf/2610.01319)

<details>
<summary>Abstract</summary>

When constraints conflict, an optimizer must determine which requirements to preserve and which to relax. On the one hand, a priority ordering specifies which requirements take precedence. On the other hand, penalty-based formulations encode their relative importance through numerical weights. Depending on these weights, a solution can improve its weighted score while violating intended priorities. We introduce TierCEM, a variant of the cross-entropy method that incorporates strict constraint priorities directly into elite selection without requiring per-constraint importance weights. TierCEM...

</details>

<details>
<summary>Share</summary>

```
Cross-entropy optimization with prioritized constraints

When constraints conflict, an optimizer must determine which requirements to preserve and which to relax.

arXiv: https://arxiv.org/abs/2610.01319

#worldmodels #robotics
```

</details>

---

### [Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153)

**Authors:** Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun et al. (9 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.40153) | [PDF](https://arxiv.org/pdf/2609.40153)

<details>
<summary>Abstract</summary>

Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling. However, joint-space action vectors lack explicit image-space structure and vary in dimensionality and semantics across embodiments, making it challenging to directly leverage the rich spatiotemporal priors of VGMs. End-effector visualizations provide an alternative but do not specify the full articulated configuration needed for robot execution. We present Dream4ACT, a world model built for joint video-action modeling across embodiments. To unify action representations across embodimen...

</details>

<details>
<summary>Share</summary>

```
Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling

Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling.

arXiv: https://arxiv.org/abs/2609.40153

#worldmodels #robotics
```

</details>

---

### [Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents](https://arxiv.org/abs/2610.04168)

**Authors:** Nijesh Upreti, Chris Sypherd, Vaishak Belle

**Published:** 2026-10-03 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.04168) | [PDF](https://arxiv.org/pdf/2610.04168)

<details>
<summary>Abstract</summary>

Agentic large language model (LLM) systems are commonly implemented as an LLM in a loop with Planning, Memory, Tools, and Control Flow. This application-focused view connects agentic LLM research with deployable systems and leaves open how such systems should be evaluated beyond end-to-end task success. Building on this view, we define agentic cognitive depth as a trajectory-level profile across five operational criteria. The profile contains context sensitivity ($C$), temporal continuity ($T$), multimodal coordination ($M$), adaptive interaction ($A$), and metacognitive monitoring ($Mc$). The...

</details>

<details>
<summary>Share</summary>

```
Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents

Agentic large language model (LLM) systems are commonly implemented as an LLM in a loop with Planning, Memory, Tools, and Control Flow.

arXiv: https://arxiv.org/abs/2610.04168

#worldmodels #robotics
```

</details>

---

### [World Embedding Benchmark](https://arxiv.org/abs/2610.03632)

**Authors:** Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai et al. (10 authors)

**Published:** 2026-10-02 | **Categories:** cs.CV, cs.CL | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.03632) | [PDF](https://arxiv.org/pdf/2610.03632)

<details>
<summary>Abstract</summary>

Physical fidelity has received increasing attention in world models and video generation, yet how video representations encode physical information remains less understood. We introduce the World Embedding Benchmark, comprising 8,000 controlled simulation cases from 80 families spanning fluid mechanics, solid mechanics, dynamics, and optics & electromagnetism. Each case pairs a rendered video with simulation-derived physical annotations, supporting three complementary tasks: text-video retrieval, physical-property regression, and multiple-choice video-description pair classification. We use th...

</details>

<details>
<summary>Share</summary>

```
World Embedding Benchmark

Physical fidelity has received increasing attention in world models and video generation, yet how video representations encode physical information remains less understood.

arXiv: https://arxiv.org/abs/2610.03632

#worldmodels #robotics
```

</details>

---

### [World-as-Graph: Relational World Modeling Through Latent Space Graphs](https://arxiv.org/abs/2609.38927)

**Authors:** Yaqi Yang, Shuo Huang, Yujin Huang, Fucai Ke, Jiatong Han et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.LG, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.38927) | [PDF](https://arxiv.org/pdf/2609.38927)

<details>
<summary>Abstract</summary>

World models aim to learn representations of real-world environments and predict their future evolution. Recent object-centric world models have made expressive progress by representing visual scenes as sets of object-level latent states, but object-object relations are often captured only implicitly, which limits explicit relational and temporal structure modeling and object-centric dynamic memory modeling. To address such challenges, we propose World-As-Graph (WAG), a graph-based object-centric world model that introduces relational inductive bias into JEPA-style predictive representation le...

</details>

<details>
<summary>Share</summary>

```
World-as-Graph: Relational World Modeling Through Latent Space Graphs

World models aim to learn representations of real-world environments and predict their future evolution.

arXiv: https://arxiv.org/abs/2609.38927

#worldmodels #robotics
```

</details>

---
