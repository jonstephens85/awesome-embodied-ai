# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-02 20:22 UTC

**Papers shown:** 121 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Beyond Policy Alignment: Closing the Planning-Learning Loop for Robot Control with Learned World Models](https://arxiv.org/abs/2609.39751)

**Authors:** Kowndinya Boyalakuntla, Yuhan Liu, Abdeslam Boularias

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

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

### [Token-World: World Modeling in Vision-Language Model Token Space for Robot Manipulation](https://arxiv.org/abs/2610.00575)

**Authors:** Chuyao Fu, Xiaowei Chi, Yuhan Rui, Yu-kai Wang, Zezhong Qian et al. (17 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

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

### [Anisotropic Representations Improve Planning in JEPA World Models](https://arxiv.org/abs/2609.37441)

**Authors:** Mingu Kang, Yoori Oh, Sookyung Kim, Joonseok Lee

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37441) | [PDF](https://arxiv.org/pdf/2609.37441) | [Project Page](https://rkdrn79.github.io/AnisoWM-page/)

<details>
<summary>Abstract</summary>

Latent world models learn action-conditioned dynamics in representation space and often score candidate actions by Euclidean distance to a goal representation. Joint training typically regularizes the representation to prevent collapse, but the resulting representation geometry also determines how terminal errors are weighted during planning. We show that accurate prediction and noncollapsed representations do not guarantee a task-aligned latent planning cost: isotropic Gaussian regularization can induce a geometry that ranks feasible outcomes differently from the task cost. To address this mi...

</details>

<details>
<summary>Share</summary>

```
Anisotropic Representations Improve Planning in JEPA World Models

Latent world models learn action-conditioned dynamics in representation space and often score candidate actions by Euclidean distance to a goal representation.

arXiv: https://arxiv.org/abs/2609.37441
Project page: https://rkdrn79.github.io/AnisoWM-page/

#worldmodels #robotics
```

</details>

---

### [EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning](https://arxiv.org/abs/2609.35047)

**Authors:** Yichao Liang, Amber Li, Dat Nguyen, Emily Bunnapradist, Michelangelo Naim et al. (16 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35047) | [PDF](https://arxiv.org/pdf/2609.35047) | [Project Page](https://yichao-liang.github.io/empiric)

<details>
<summary>Abstract</summary>

A robot should be able to learn through experiments how unfamiliar objects behave and interact, then plan with that knowledge. It need not start from scratch: physics engines supply knowledge of motion and contact, but can omit entire mechanisms, such as glue curing, water heating, or wind. We present EMPIRIC, an agent that learns a residual world model: a physics engine extended with code for the missing mechanisms. The learned programs can introduce new forces, constraints, and hidden state, and Bayesian inference estimates their parameters and states from noisy observations. The resulting m...

</details>

<details>
<summary>Share</summary>

```
EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning

A robot should be able to learn through experiments how unfamiliar objects behave and interact, then plan with that knowledge.

arXiv: https://arxiv.org/abs/2609.35047
Project page: https://yichao-liang.github.io/empiric

#worldmodels #robotics
```

</details>

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

### [Honeycomb: Constant-Size Scene Memory Representation for Video World Models](https://arxiv.org/abs/2609.37690)

**Authors:** Jack Wei Lun Shi, Kaichen Zhou, Haoyu Chen, Yufeng Weng, Keane Ong et al. (9 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37690) | [PDF](https://arxiv.org/pdf/2609.37690) | [Project Page](https://jackswl.github.io/honeycomb/) | [Code](https://github.com/kaichen-z/honeycomb)

<details>
<summary>Abstract</summary>

Video world models require persistent scene memory to maintain consistency during long-horizon video generation. Existing spatial memories accumulate RGB observations or latent features, increasing storage requirements as generation proceeds. We introduce Honeycomb, a video world model built on HexMemory, our proposed low-rank representation for storing scene features in a fixed-size memory with a total of six spatial and spatiotemporal planes. A feed-forward writer maps each generated chunk into new plane features. As the spatial coverage or temporal range expands, we warp the previous planes...

</details>

<details>
<summary>Share</summary>

```
Honeycomb: Constant-Size Scene Memory Representation for Video World Models

Video world models require persistent scene memory to maintain consistency during long-horizon video generation.

arXiv: https://arxiv.org/abs/2609.37690
Project page: https://jackswl.github.io/honeycomb/
Code: https://github.com/kaichen-z/honeycomb

#worldmodels #robotics
```

</details>

---

### [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](https://arxiv.org/abs/2609.36851)

**Authors:** Hongbin Lin, Chaoda Zheng, Yiming Yang, Xiangyu Li, Shijia Chen et al. (14 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36851) | [PDF](https://arxiv.org/pdf/2609.36851) | [Project Page](https://hongbin98.github.io/RoXDrive/) | [Code](https://github.com/Hongbin98/RoXDrive)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as interactive training environments to enable future scene generation for policy improvement. Nevertheless, existing approaches either rely on reconstruction-based simulators, offering limited counterfactual interaction, or adopt synthetic simul...

</details>

<details>
<summary>Share</summary>

```
RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts

End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-worl...

arXiv: https://arxiv.org/abs/2609.36851
Project page: https://hongbin98.github.io/RoXDrive/
Code: https://github.com/Hongbin98/RoXDrive

#worldmodels #robotics
```

</details>

---

### [WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](https://arxiv.org/abs/2609.34606)

**Authors:** Zeyu Zhang, Jinyuan Mao, Dakai An, Wangbo Zhao, Hanfeng Lu et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34606) | [PDF](https://arxiv.org/pdf/2609.34606) | [Project Page](https://alibaba-damo-academy.github.io/WorldAttention) | [Code](https://github.com/alibaba-damo-academy/WorldAttention)

<details>
<summary>Abstract</summary>

Leveraging the paradigm of autoregressive diffusion, text-conditioned interactive video world models aim to simulate temporally coherent environments guided by textual instructions. While enabling low-latency, long-duration generation is pivotal for embodied AI and simulation-based planning, current frameworks primarily rely on sliding-window mechanisms to bound computational complexity. However, this approach inherently sacrifices historical context, undermining the long-range interactive capabilities. Conversely, maintaining a full-history cache remains computationally prohibitive and memory...

</details>

<details>
<summary>Share</summary>

```
WorldAttention: An Efficient Attention Architecture for Interactive Video World Models

Leveraging the paradigm of autoregressive diffusion, text-conditioned interactive video world models aim to simulate temporally coherent environments guided by textual instructions.

arXiv: https://arxiv.org/abs/2609.34606
Project page: https://alibaba-damo-academy.github.io/WorldAttention
Code: https://github.com/alibaba-damo-academy/WorldAttention

#worldmodels #robotics
```

</details>

---

### [WorldWeave: Growing Persistent Geometric Worlds for Video Generation](https://arxiv.org/abs/2609.34221)

**Authors:** Yifan Huang, Lifan Jiang, Qingyue Hao, Cheng Chen, Boxi Wu et al. (8 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34221) | [PDF](https://arxiv.org/pdf/2609.34221) | [Project Page](https://laiyindagm.github.io/WorldWeave/) | [Code](https://github.com/laiyindagm/WorldWeave)

<details>
<summary>Abstract</summary>

Despite rapid progress, world models still lack explicit, persistent structural memory, making it difficult to preserve consistent world structure during continual scene expansion and cross-view revisits. To address this limitation, we present WorldWeave, a world generation framework that decouples world-state maintenance from visual rendering. Specifically, WorldWeave combines continual elevation-map generation with agent-guided scene organization and stitching to build an expandable explicit 3D world that incrementally extends structural memory while preserving existing structure. First, its...

</details>

<details>
<summary>Share</summary>

```
WorldWeave: Growing Persistent Geometric Worlds for Video Generation

Despite rapid progress, world models still lack explicit, persistent structural memory, making it difficult to preserve consistent world structure during continual scene expansion and cross-view revisits.

arXiv: https://arxiv.org/abs/2609.34221
Project page: https://laiyindagm.github.io/WorldWeave/
Code: https://github.com/laiyindagm/WorldWeave

#worldmodels #robotics
```

</details>

---

### [FutureWorlds: Learning Robotic World Models from Alternative Futures](https://arxiv.org/abs/2610.01019)

**Authors:** Hao Wu, Shengju Qian, Weiyan Wang, Fan Xu, Fan Zhang et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

### [AD-E2E-JEPA: A Joint-Embedding Predictive Architecture For End-to-End Autonomous Driving](https://arxiv.org/abs/2609.34085)

**Authors:** Haoran Zhu, Wancong Zhang, Yann LeCun, Anna Choromanska

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34085) | [PDF](https://arxiv.org/pdf/2609.34085) | [Code](https://github.com/HaoranZhuExplorer/AD-E2E-JEPA)

<details>
<summary>Abstract</summary>

Autonomous driving requires \textit{world models} that can understand the physical world, reason and plan, and operate safely. In this paper, we first systematically evaluate existing action-conditioned joint-embedding predictive architecture (JEPA) world models, including LeWM, DINO-WM, and JEPA-WM for end-to-end autonomous driving (E2EAD). To isolate world-model quality from policy learning, we employ a goal-conditioned zero-shot planning setting that evaluates these models using ground-truth future observations as goals, without training any driving policy. We find that existing JEPA-based...

</details>

<details>
<summary>Share</summary>

```
AD-E2E-JEPA: A Joint-Embedding Predictive Architecture For End-to-End Autonomous Driving

Autonomous driving requires \textit{world models} that can understand the physical world, reason and plan, and operate safely.

arXiv: https://arxiv.org/abs/2609.34085
Code: https://github.com/HaoranZhuExplorer/AD-E2E-JEPA

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

### [4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160)

**Authors:** Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

### [Beyond a single latent space: a dual-latent world model for long-horizon planning](https://arxiv.org/abs/2609.37644)

**Authors:** Delin Zhao, Zhengrong Yue, Shaobin Zhuang, Junlin He, Xiaoyu Chen et al. (9 authors)

**Published:** 2026-09-29 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37644) | [PDF](https://arxiv.org/pdf/2609.37644) | [Code](https://github.com/DeLin1001/Dual-WM-Official)

<details>
<summary>Abstract</summary>

Latent world models often struggle with long-horizon planning despite accurate short-term predictions. Recursive rollouts accumulate errors, while distance concentration in high-dimensional latent spaces can weaken goal discrimination. We introduce the Dual-Latent World Model (Dual-WM), which separates local execution and long-range planning through distinct state representations and dynamics models. The low-level model predicts action-conditioned transitions, while the high-level model uses learned macro-actions to plan over longer temporal spans. We also propose Long-Horizon Representation L...

</details>

<details>
<summary>Share</summary>

```
Beyond a single latent space: a dual-latent world model for long-horizon planning

Latent world models often struggle with long-horizon planning despite accurate short-term predictions.

arXiv: https://arxiv.org/abs/2609.37644
Code: https://github.com/DeLin1001/Dual-WM-Official

#worldmodels #robotics
```

</details>

---

### [CAST: Reconstruction-Coupled Acceleration of Interactive World Models](https://arxiv.org/abs/2609.34144)

**Authors:** Leyang Chen, Junyi Wu, Fanqing Kong, Shaoqiu Zhang, Yulun Zhang

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34144) | [PDF](https://arxiv.org/pdf/2609.34144) | [Code](https://github.com/lokiniuniu/CAST)

<details>
<summary>Abstract</summary>

Interactive world models must respond quickly to controls while preserving scene consistency. Existing acceleration methods can miss heterogeneous control responses and spatial transport when recovering skipped features. We observe that interaction-induced feature changes correlate with approximation error, while low-frequency interpolation errors are phase-sensitive and show more predictable phase progression. These findings motivate CAST, a reconstruction-coupled inference framework. CAST selects anchors by interaction sensitivity and cross-layer coverage, reconstructs skipped residuals with...

</details>

<details>
<summary>Share</summary>

```
CAST: Reconstruction-Coupled Acceleration of Interactive World Models

Interactive world models must respond quickly to controls while preserving scene consistency.

arXiv: https://arxiv.org/abs/2609.34144
Code: https://github.com/lokiniuniu/CAST

#worldmodels #robotics
```

</details>

---

### [Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning](https://arxiv.org/abs/2610.01224)

**Authors:** Takumi Hara, Kanata Suzuki

**Published:** 2026-10-01 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving](https://arxiv.org/abs/2609.36438)

**Authors:** Jieyuan Pei, Meiyi Lu, Sining Ang, Yubo Zhao, Zhangyi Hu et al. (15 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36438) | [PDF](https://arxiv.org/pdf/2609.36438) | [Project Page](https://guobapei.github.io/World4Scorer/)

<details>
<summary>Abstract</summary>

Autonomous driving requires choosing a safe and efficient plan as surrounding traffic evolves. Generate-and-select planners propose multiple trajectories and score them for execution, and they have outperformed representative direct-prediction baselines on NAVSIM. Their scorer must compare plans that were never executed. Driving logs record the future of only the executed trajectory, so matching the logged future can leave predictions for the alternatives unconstrained; a simulator, in contrast, can label the outcome of every candidate. We introduce World4Scorer, which builds the scorer as a t...

</details>

<details>
<summary>Share</summary>

```
World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving

Autonomous driving requires choosing a safe and efficient plan as surrounding traffic evolves.

arXiv: https://arxiv.org/abs/2609.36438
Project page: https://guobapei.github.io/World4Scorer/

#worldmodels #robotics
```

</details>

---

### [In-Context Learning for Robots: Methods and Applications](https://arxiv.org/abs/2609.36012)

**Authors:** Haojian Huang, Zexi Li, Junhao Guo, Yehang Zhang, Wenxuan Peng et al. (39 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36012) | [PDF](https://arxiv.org/pdf/2609.36012) | [Project Page](https://jethrojames.github.io/awesome-robots-icl/)

<details>
<summary>Abstract</summary>

General-purpose robots must infer what a new task requires and translate that understanding into appropriate physical action. In-context learning (ICL) for robots supports this process by using demonstrations and interaction to direct existing competence with neural parameters held fixed during deployment. We organize this literature review around the interfaces connecting contextual evidence to execution, distinguishing four families: context-conditioned policies, geometric demonstration transfer, world-model-based control, and skill- and agent-based execution. Comparing these interfaces clar...

</details>

<details>
<summary>Share</summary>

```
In-Context Learning for Robots: Methods and Applications

General-purpose robots must infer what a new task requires and translate that understanding into appropriate physical action.

arXiv: https://arxiv.org/abs/2609.36012
Project page: https://jethrojames.github.io/awesome-robots-icl/

#worldmodels #robotics
```

</details>

---

### [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining](https://arxiv.org/abs/2609.35652)

**Authors:** Qiwei Liang, Guangyu Chen, Shaolong Zhu, Zikuan Xiao, Jinxuan Lu et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35652) | [PDF](https://arxiv.org/pdf/2609.35652) | [Project Page](https://mm-abc.github.io/)

<details>
<summary>Abstract</summary>

Mobile manipulation extends robot interaction beyond a fixed kinematic workspace by making the reachable region itself controllable. This flexibility introduces two central challenges: spatially grounded perception under continuous ego-motion and coordinated control of heterogeneous arm and base actions. Existing approaches strengthen geometry through explicit 3D representations or predictive world models, and often decouple mobility and manipulation into separate action streams. We argue that effective mobile manipulation requires not only decoupling, but also representations that support eff...

</details>

<details>
<summary>Share</summary>

```
MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining

Mobile manipulation extends robot interaction beyond a fixed kinematic workspace by making the reachable region itself controllable.

arXiv: https://arxiv.org/abs/2609.35652
Project page: https://mm-abc.github.io/

#worldmodels #robotics
```

</details>

---

### [RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts](https://arxiv.org/abs/2609.35311)

**Authors:** Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.35311) | [PDF](https://arxiv.org/pdf/2609.35311)

<details>
<summary>Abstract</summary>

Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric scene queryable across viewpoints and time. While existing 4D reconstruction methods offer a path to spatialize these predictions, independently reconstructing and merging each camera stream fails to enforce cross-view consistency. This limitation is particularly detrimental when combining moving robot-mounted cameras with fixed external views. To address this, we introduce RoGSW4RLD, a feed-forward framework that lifts...

</details>

<details>
<summary>Share</summary>

```
RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts

Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric scene queryable across viewpoints and time.

arXiv: https://arxiv.org/abs/2609.35311

#worldmodels #robotics
```

</details>

---

### [JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments](https://arxiv.org/abs/2609.35032)

**Authors:** Zhixi Cai, Fucai Ke, Sukai Huang, Maria Garcia de la Banda, Peter J. Stuckey et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.AI, cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35032) | [PDF](https://arxiv.org/pdf/2609.35032) | [Code](https://github.com/ControlNet/JRDB-AVR)

<details>
<summary>Abstract</summary>

In complex embodied visual reasoning scenarios, an agent often has only a limited field of view, and the evidence needed to answer a question may be distributed across time, viewpoint, and interacting objects. A model may therefore give a plausible answer without ever observing the relevant object, time, or view that supports it. Current visual reasoning benchmarks largely evaluate passive observations and final answers, overlooking settings that require active reasoning and evidence acquisition. We introduce JRDB-AVR, a benchmark derived from existing real-world JRDB robotics data through a s...

</details>

<details>
<summary>Share</summary>

```
JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments

In complex embodied visual reasoning scenarios, an agent often has only a limited field of view, and the evidence needed to answer a question may be distributed across time, viewpoint, and interacting objects.

arXiv: https://arxiv.org/abs/2609.35032
Code: https://github.com/ControlNet/JRDB-AVR

#worldmodels #robotics
```

</details>

---

### [Dexterous Tactile World Model](https://arxiv.org/abs/2609.34286)

**Authors:** Ziyao Zeng, Xiatao Sun, Hao Wang, Yueyang Pan, Zhengxiang Yu et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34286) | [PDF](https://arxiv.org/pdf/2609.34286) | [Project Page](https://adonis-galaxy.github.io/dtwm-project-page/)

<details>
<summary>Abstract</summary>

World models for manipulation are typically trained from video, yet the events that determine how manipulation unfolds, such as making and releasing contact, are difficult to observe visually and are often easier to sense through touch. We present the Dexterous Tactile World Model (DTWM), a video world model for future-frame prediction of egocentric manipulation from both observed video and tactile signals from a glove worn on each hand. We condition a pretrained video diffusion transformer on each hand's tactile signal through a zero-initialized residual at the corresponding hand location in...

</details>

<details>
<summary>Share</summary>

```
Dexterous Tactile World Model

World models for manipulation are typically trained from video, yet the events that determine how manipulation unfolds, such as making and releasing contact, are difficult to observe visually and are often easier to s...

arXiv: https://arxiv.org/abs/2609.34286
Project page: https://adonis-galaxy.github.io/dtwm-project-page/

#worldmodels #robotics
```

</details>

---

### [Scope-WM: Scoped Computation for Efficient Visual World Models](https://arxiv.org/abs/2609.33218)

**Authors:** Chunzheng Li, Zesheng Jia, Hongda Zhang, Jiaying Tang, Yuntian Wang et al. (7 authors)

**Published:** 2026-09-27 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.33218) | [PDF](https://arxiv.org/pdf/2609.33218) | [Code](https://github.com/ChunZheng2022/Scope-WM)

<details>
<summary>Abstract</summary>

Visual world models enable robotic planning by predicting future observations, but dense latent-state propagation and sample-intensive trajectory optimization incur high inference latency and peak memory usage, limiting real-time deployment on resource-constrained platforms. Existing sparse world-model acceleration methods either rely on unguided token sparsification, which may discard planning-relevant information and restrict achievable sparsity, or introduce heavy auxiliary modules and cumbersome multi-stage training pipelines. In this work, we present Scope-WM, an efficient visual world mo...

</details>

<details>
<summary>Share</summary>

```
Scope-WM: Scoped Computation for Efficient Visual World Models

Visual world models enable robotic planning by predicting future observations, but dense latent-state propagation and sample-intensive trajectory optimization incur high inference latency and peak memory usage, limiti...

arXiv: https://arxiv.org/abs/2609.33218
Code: https://github.com/ChunZheng2022/Scope-WM

#worldmodels #robotics
```

</details>

---

### [VPTwin: Real-Sim-Real Video Prediction for Robotic Manipulation Planning](https://arxiv.org/abs/2609.33104)

**Authors:** Zhenghao Xiao, Minting Pan, Nantian He, Dongzhan Zhou, Yunbo Wang

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33104) | [PDF](https://arxiv.org/pdf/2609.33104)

<details>
<summary>Abstract</summary>

While action-conditioned video prediction provides an intuitive world model for robotics, purely data-driven predictors often suffer from compounding errors and physically implausible hallucinations in long-horizon rollouts, severely undermining downstream action planning. We propose VPTwin, a Real-Sim-Real video prediction framework that anchors real-world future prediction using real-synchronized simulation twins. For a target manipulation task, a VLM reconstructs an executable digital twin from a real demonstration episode. To accommodate the ill-posed estimation of unobserved physical prop...

</details>

<details>
<summary>Share</summary>

```
VPTwin: Real-Sim-Real Video Prediction for Robotic Manipulation Planning

While action-conditioned video prediction provides an intuitive world model for robotics, purely data-driven predictors often suffer from compounding errors and physically implausible hallucinations in long-horizon ro...

arXiv: https://arxiv.org/abs/2609.33104

#worldmodels #robotics
```

</details>

---

### [FINE: Future-Informed Navigation Encoding for Data-Efficient Vision-Language Navigation](https://arxiv.org/abs/2609.32855)

**Authors:** Khang H. Nguyen, Hoang Pham Quang Nguyen, Ha Phuong Nguyen, Khanh Dinh Binh, Xuan Ha Nguyen et al. (9 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.32855) | [PDF](https://arxiv.org/pdf/2609.32855) | [Project Page](https://finevln.github.io/)

<details>
<summary>Abstract</summary>

Adapting vision-language navigation (VLN) policies to new environments is expensive because every additional route and instruction requires an embodied demonstration. Yet standard observation-to-action training uses only a small fraction of the information already contained in each trajectory. In particular, future observations reveal the instruction-relevant landmarks that the agent will encounter, including what they look like and how they are arranged in 3D. We introduce FINE, a Future-Informed Navigation Encoding framework that extracts this latent supervision from existing demonstrations....

</details>

<details>
<summary>Share</summary>

```
FINE: Future-Informed Navigation Encoding for Data-Efficient Vision-Language Navigation

Adapting vision-language navigation (VLN) policies to new environments is expensive because every additional route and instruction requires an embodied demonstration.

arXiv: https://arxiv.org/abs/2609.32855
Project page: https://finevln.github.io/

#worldmodels #robotics
```

</details>

---

### [Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092)

**Authors:** Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi et al. (13 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world simulator" in abstract; robotics / embodied focus; posted in last 2 days

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

### [Learning Commute-Time-Preserving World Models for Planning](https://arxiv.org/abs/2610.01373)

**Authors:** Michael Hauri, Peter Buttaroni, Fabian A. Mikulasch, Friedemann Zenke

**Published:** 2026-10-01 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

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

### [Lucid Dreaming for World Models: Learning to Doubt Imagination and Decide by Trust](https://arxiv.org/abs/2609.37156)

**Authors:** Ziqi Wen, Ting Xu, Lianyu Wang, Xian Lin, Yanda Meng et al. (8 authors)

**Published:** 2026-09-29 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37156) | [PDF](https://arxiv.org/pdf/2609.37156) | [Project Page](https://lucidwm.github.io)

<details>
<summary>Abstract</summary>

World models enable agents to learn and plan in imagination, but predictions beyond their experience can become unreliable and mislead decisions. Existing uncertainty estimates derived from predictions can remain overconfident on unfamiliar state-action pairs. We propose the Lucid World Model (LucidWM), which learns doubt from experience and propagates trust through imagination. By integrating Subjective Logic into categorical latent transitions, LucidWM distinguishes predicted outcomes from their evidential support and assigns each transition a degree of doubt. The complement of this doubt de...

</details>

<details>
<summary>Share</summary>

```
Lucid Dreaming for World Models: Learning to Doubt Imagination and Decide by Trust

World models enable agents to learn and plan in imagination, but predictions beyond their experience can become unreliable and mislead decisions.

arXiv: https://arxiv.org/abs/2609.37156
Project page: https://lucidwm.github.io

#worldmodels #robotics
```

</details>

---

### [FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales](https://arxiv.org/abs/2609.35138)

**Authors:** Shidu Ren, Qilin Gu, Zhenghao Ni, Junhan Sun, Jiaqi Wang et al. (7 authors)

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35138) | [PDF](https://arxiv.org/pdf/2609.35138) | [Project Page](https://shidu-ren.github.io/FlexiWorld-Project-Page/)

<details>
<summary>Abstract</summary>

Latent world models predict future states for goal-directed planning using action chunks spanning multiple primitive steps. Existing methods typically use fixed-length chunks and either omit goal-conditioned action generation or limit their supervision to short goal spans. We introduce FlexiWorld, a JEPA-based world model that combines mixed-span goal supervision with variable-length action chunks to improve long-horizon control. During training, we sample varying goal spans and randomly partition the actions into variable-length chunks. We jointly train the world model with a causal action en...

</details>

<details>
<summary>Share</summary>

```
FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales

Latent world models predict future states for goal-directed planning using action chunks spanning multiple primitive steps.

arXiv: https://arxiv.org/abs/2609.35138
Project page: https://shidu-ren.github.io/FlexiWorld-Project-Page/

#worldmodels #robotics
```

</details>

---

### [Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State](https://arxiv.org/abs/2609.33497)

**Authors:** Tamim Zoabi, Ameen Ali, Lior Wolf

**Published:** 2026-09-27 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33497) | [PDF](https://arxiv.org/pdf/2609.33497)

<details>
<summary>Abstract</summary>

Planning from pixels needs more than a latent space that is stable and predictable. The state the planner scores must also be organized by how actions move the system. Joint-embedding predictive architectures (JEPAs) avoid pixel reconstruction by predicting future representations, but existing action-conditioned JEPAs ask one embedding to serve both perception and control. We introduce H-JEPA, which separates the two. A wide perceptual code is regularized toward a well-scaled isotropic geometry with a Bures-Wasserstein prior, and a fixed orthonormal slice of that code is the control state, whi...

</details>

<details>
<summary>Share</summary>

```
Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State

Planning from pixels needs more than a latent space that is stable and predictable.

arXiv: https://arxiv.org/abs/2609.33497

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

### [ReWAM: Reciprocal World Action Models for Interactive Autonomous Driving](https://arxiv.org/abs/2609.39245)

**Authors:** Benshan Ma, Pei Liu, Ruiguo Zhong, Lang Zhang, Mingyue Feng et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [One from Infinity: Actualizing Futures from Pretrained World Models into Robot Actions](https://arxiv.org/abs/2609.36413)

**Authors:** Bang Du, Yichen Xie, Shuqi Zhao, Yuxin Chen, Menglin Wu et al. (6 authors)

**Published:** 2026-09-29 (updated 2026-10-01) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2609.36413) | [PDF](https://arxiv.org/pdf/2609.36413)

<details>
<summary>Abstract</summary>

A pretrained video world model admits many plausible futures for a scene, but a robot must realize the exact task-conditioned one. To turn world models into executable robot policies, existing methods fine-tune the heavy world model backbone using large-scale robot data and computational resources. Challenging this status quo, we argue that the expensive part has already been paid in the world model pretraining since the representation space of a video world model lays out the diverse potential futures. In this case, what remains is to select the future that accomplishes the task and to read o...

</details>

<details>
<summary>Share</summary>

```
One from Infinity: Actualizing Futures from Pretrained World Models into Robot Actions

A pretrained video world model admits many plausible futures for a scene, but a robot must realize the exact task-conditioned one.

arXiv: https://arxiv.org/abs/2609.36413

#worldmodels #robotics
```

</details>

---

### [Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163)

**Authors:** Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen et al. (15 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38163) | [PDF](https://arxiv.org/pdf/2609.38163) | [Code](https://github.com/hustvl/ReWAM)

<details>
<summary>Abstract</summary>

World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction. We study the design of this space through controlled comparisons, finding that neither reconstruction fidelity nor pre-trained perceptual features alone ensure effective policy learning. These findings motivate ReWAM, a representation-centric world-action model built on pre-trained DINO features. Feature Calibration and a Temporal Representation Bottleneck organize these features into compact world states suited to dynamics modeling. Act...

</details>

<details>
<summary>Share</summary>

```
Rethinking Representations for World-Action Modeling

World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction.

arXiv: https://arxiv.org/abs/2609.38163
Code: https://github.com/hustvl/ReWAM

#worldmodels #robotics
```

</details>

---

### [ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning](https://arxiv.org/abs/2609.36333)

**Authors:** Ke Fang, Yupu Yao, Lu Cheng

**Published:** 2026-09-28 (updated 2026-09-30) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.36333) | [PDF](https://arxiv.org/pdf/2609.36333)

<details>
<summary>Abstract</summary>

Latent world models rely on representation geometry for planning, yet regularizing the latent marginal alone does not determine the state-to-state relationships used for action selection. We show that this can cause planning-relevant novelty structure to be weakened as representations are transformed into the final latent used by the planner. We introduce Aligned Transport of Latent Structure (ATLAS), a training objective that explicitly preserves relational geometry while calibrating the global latent distribution. ATLAS transfers normalized pairwise structure from an informative encoder repr...

</details>

<details>
<summary>Share</summary>

```
ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning

Latent world models rely on representation geometry for planning, yet regularizing the latent marginal alone does not determine the state-to-state relationships used for action selection.

arXiv: https://arxiv.org/abs/2609.36333

#worldmodels #robotics
```

</details>

---

### [LRC-JEPA: Disentangling Dynamics and Residual Context for Efficient World Models](https://arxiv.org/abs/2609.34375)

**Authors:** Luzhe Huang, Lei Chu, Jingyi Liang, Yuhuan Zhao

**Published:** 2026-09-28 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.34375) | [PDF](https://arxiv.org/pdf/2609.34375)

<details>
<summary>Abstract</summary>

Compact JEPA world models enable efficient latent-space planning, but low-dimensional representation trained under reward-free self-supervision must encode both action-conditioned dynamics and predictable visual context. This competition can entangle controllable state with high-rank nuisance appearance and degrade planning as scenes become more complex. We introduce LRC-JEPA, a lightweight end-to-end world model that routes information into a compact predictive latent $\mathbf{z}$ and learned-query residual-context embeddings $\mathbf{u}$. Only $\mathbf{z}$ is propagated by the dynamics model...

</details>

<details>
<summary>Share</summary>

```
LRC-JEPA: Disentangling Dynamics and Residual Context for Efficient World Models

Compact JEPA world models enable efficient latent-space planning, but low-dimensional representation trained under reward-free self-supervision must encode both action-conditioned dynamics and predictable visual context.

arXiv: https://arxiv.org/abs/2609.34375

#worldmodels #robotics
```

</details>

---

### [Achieve What You Imagined: Learning to Align Actions with Visual Plans](https://arxiv.org/abs/2609.33832)

**Authors:** Yuheng Qiao, Ziran Wei, Xiaohan Wang, Daqiang Guo, Yichen Luo et al. (8 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.33832) | [PDF](https://arxiv.org/pdf/2609.33832) | [Project Page](https://imagine-to-achieve.github.io/)

<details>
<summary>Abstract</summary>

World-action models can jointly predict future visual observations and robot actions. However, discrepancies may exist between their visual predictions and the consequences implied by generated actions. We observe that WAMs can often generate visually plausible task-completion outcomes before producing action sequences that reliably achieve them. Consequently, we treat the WAM-generated visual prediction as a goal-conditioned visual proposal rather than a directly executable plan. We use a frozen action-conditioned world model to predict action-conditioned consequences and construct feedback b...

</details>

<details>
<summary>Share</summary>

```
Achieve What You Imagined: Learning to Align Actions with Visual Plans

World-action models can jointly predict future visual observations and robot actions.

arXiv: https://arxiv.org/abs/2609.33832
Project page: https://imagine-to-achieve.github.io/

#worldmodels #robotics
```

</details>

---

### [MomWorld: Momentum-Aware Latent World Model for Long-Horizon Autonomous Driving](https://arxiv.org/abs/2609.33737)

**Authors:** Ziying Song, Shengkai Zhang, Lei Yang, Haozhuang Chi, Yuchen Liu et al. (9 authors)

**Published:** 2026-09-27 (updated 2026-09-30) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33737) | [PDF](https://arxiv.org/pdf/2609.33737)

<details>
<summary>Abstract</summary>

Long-horizon planning enables autonomous vehicles to anticipate scene evolution and potential risks, supporting safe and stable decisions in complex interactions. However, existing methods struggle to propagate motion trends from observed history into the future. Long rollouts based on a single latent state may further attenuate useful dynamics, retain stale motion patterns, and disrupt reliable near-term plans. We introduce MomWorld, a momentum-aware latent world model for long-horizon planning. MomWorld extracts scene motion trends from historical-to-current observations and propagates laten...

</details>

<details>
<summary>Share</summary>

```
MomWorld: Momentum-Aware Latent World Model for Long-Horizon Autonomous Driving

Long-horizon planning enables autonomous vehicles to anticipate scene evolution and potential risks, supporting safe and stable decisions in complex interactions.

arXiv: https://arxiv.org/abs/2609.33737

#worldmodels #robotics
```

</details>

---

### [VIDEAS: Distilling Explicit Action Semantics from Demonstration Videos for World Models via Prior-Guided Simulation](https://arxiv.org/abs/2609.33464)

**Authors:** Jianan Wang, Haoquan Zhai, Siyang Zhang, Bin Li, Juan Chen et al. (10 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33464) | [PDF](https://arxiv.org/pdf/2609.33464)

<details>
<summary>Abstract</summary>

World models learn internal representations of environment dynamics to predict future states, enabling agents to optimize action plans without physical interactions. However, developing world models that genuinely internalize underlying causal physical laws to explicitly reason about action preconditions and subsequent state transitions remains an open challenge. In this paper, we propose VIDEAS, a data distillation framework that transforms continuous physical dynamics from operational videos into explicit action semantics for foundation models. Specifically, it deconstructs visual demonstrat...

</details>

<details>
<summary>Share</summary>

```
VIDEAS: Distilling Explicit Action Semantics from Demonstration Videos for World Models via Prior-Guided Simulation

World models learn internal representations of environment dynamics to predict future states, enabling agents to optimize action plans without physical interactions.

arXiv: https://arxiv.org/abs/2609.33464

#worldmodels #robotics
```

</details>

---

### [What Must a World Model Distinguish for Planning?](https://arxiv.org/abs/2609.33030)

**Authors:** Rongzhe Wei, Hans Hao-Hsun Hsu, Peizhi Niu, Yifan Li, Pan Li

**Published:** 2026-09-26 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33030) | [PDF](https://arxiv.org/pdf/2609.33030)

<details>
<summary>Abstract</summary>

World models simulate the consequences of action candidates, but good planning need not preserve every physical distinction required for accurate prediction. We formalize this gap through a hierarchy of mechanism, response, and decision sufficiency. Given a candidate set, the planning query determines which physical variations matter and how precisely they must be preserved: coarse decisions can discard much of the information needed for prediction, whereas fine decisions may require nearly the same resolution. In practice, planners often adaptively search to construct candidates, and informat...

</details>

<details>
<summary>Share</summary>

```
What Must a World Model Distinguish for Planning?

World models simulate the consequences of action candidates, but good planning need not preserve every physical distinction required for accurate prediction.

arXiv: https://arxiv.org/abs/2609.33030

#worldmodels #robotics
```

</details>

---

### [Network World Models as Environments for Algorithm Design on Complex Systems](https://arxiv.org/abs/2610.01048)

**Authors:** Rishab Alagharu, Hongji Pu, Zeeshan Memon, Xinyuan Song, Yuntong Hu et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](https://arxiv.org/abs/2609.38140)

**Authors:** Yu Xu, Yuxin Zhang, Xiao Yang, Haotian Yang, Yizhi Wang et al. (10 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38140) | [PDF](https://arxiv.org/pdf/2609.38140) | [Project Page](https://yuci-gpt.github.io/SplitMoE/)

<details>
<summary>Abstract</summary>

Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models. However, conventional token-wise MoE routes tokens independently within a homogeneous expert pool and regularizes expert usage toward uniformity, making it poorly matched to video data that is spatiotemporally redundant and semantically long-tailed. We show that existing visual MoEs fall into a uniformity trap: semantically under-organized routing, compounded by uniform expert-usage regularization, scatters coherent patches across disparate experts, causing routing frag...

</details>

<details>
<summary>Share</summary>

```
Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE

Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models.

arXiv: https://arxiv.org/abs/2609.38140
Project page: https://yuci-gpt.github.io/SplitMoE/

#worldmodels #robotics
```

</details>

---

### [HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123)

**Authors:** Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang et al. (16 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38123) | [PDF](https://arxiv.org/pdf/2609.38123)

<details>
<summary>Abstract</summary>

World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time. Yet prevailing interactive world models remain strictly silent, focusing exclusively on visual rendering and control while overlooking the acoustic dimension. We present HelixWorld, a real-time interactive audio-visual world model where visual scenes and camera-grounded spatial stereo sound co-evolve natively under user interaction. We curate a high-fidelity spatial audio-visual dataset with true stereo acoustics and metric camera poses, upon which we pre-train a bidirectional teacher...

</details>

<details>
<summary>Share</summary>

```
HelixWorld: A Real-time Interactive Audio-Visual World Model

World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time.

arXiv: https://arxiv.org/abs/2609.38123

#worldmodels #robotics
```

</details>

---

### [Do-JEPA: From Masking to Intervention in Latent World Models](https://arxiv.org/abs/2609.37378)

**Authors:** Hossein Resani, Javen Qinfeng Shi

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.37378) | [PDF](https://arxiv.org/pdf/2609.37378)

<details>
<summary>Abstract</summary>

Latent world models are trained to predict what happens next, so nothing in their objective separates what an action caused from what merely co-occurred with it. Object-masking models such as C-JEPA intervene on what the predictor can see; we intervene on what physically happens. From one saved simulator state we run the dynamics under an action $a$ and under a reference action $a_{\varnothing}$, and train the model to predict the difference $Δz=z^{a}-z^{a_{\varnothing}}$ between the two latent futures. The resulting objective, Do-JEPA, has an effect loss, a support loss (where the action ente...

</details>

<details>
<summary>Share</summary>

```
Do-JEPA: From Masking to Intervention in Latent World Models

Latent world models are trained to predict what happens next, so nothing in their objective separates what an action caused from what merely co-occurred with it.

arXiv: https://arxiv.org/abs/2609.37378

#worldmodels #robotics
```

</details>

---

### [Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107)

**Authors:** Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig et al. (15 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.CV, cs.HC | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37107) | [PDF](https://arxiv.org/pdf/2609.37107)

<details>
<summary>Abstract</summary>

We present Waypoint 1.5, a real-time diffusion world model for interactive video generation on consumer-grade hardware. Unlike general video diffusion models, interactive world models (iWMs) must respond to dense user controls under strict latency and throughput constraints. Waypoint 1.5 is pre-trained on 100,000 hours of diverse, control-aligned video game data across hundreds of games, and generates playable video conditioned on full keyboard and mouse input. The model includes two resolution variants that run across a wide spectrum of consumer hardware. To characterize this unique setting,...

</details>

<details>
<summary>Share</summary>

```
Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware

We present Waypoint 1.5, a real-time diffusion world model for interactive video generation on consumer-grade hardware.

arXiv: https://arxiv.org/abs/2609.37107

#worldmodels #robotics
```

</details>

---

### [Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531)

**Authors:** Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ehécatl Sacamch'en Núñez Rico, Hugo Jair Escalante

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.36531) | [PDF](https://arxiv.org/pdf/2609.36531)

<details>
<summary>Abstract</summary>

Video world models are largely regarded as predictive models of the physical world and are therefore expected to anticipate the consequences of observed events. However, evaluation has mainly focused on reference similarity, physical-law consistency, or judgment plausibility, estimating anticipation only indirectly. We address this directly: when a release or impact has just occurred but its consequence is withheld, can a world model anticipate what should happen next? We introduce an event-anchored evaluation based on 62 controlled real-world free-fall recordings and 124 clips spanning three...

</details>

<details>
<summary>Share</summary>

```
Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models

Video world models are largely regarded as predictive models of the physical world and are therefore expected to anticipate the consequences of observed events.

arXiv: https://arxiv.org/abs/2609.36531

#worldmodels #robotics
```

</details>

---

### [DynamicHOI: Coupled Dynamics for Physics-aware HOI Reconstruction](https://arxiv.org/abs/2609.36454)

**Authors:** Wenliang Guo, Zhanbo Huang, Yu Kong

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36454) | [PDF](https://arxiv.org/pdf/2609.36454) | [Project Page](https://wenliangguo.github.io/HOI-Reconstruction-Page/)

<details>
<summary>Abstract</summary>

We study hand-object interaction (HOI) reconstruction from monocular RGB videos, where partial observations can produce visually plausible yet mechanically inconsistent trajectories. Existing methods mainly enforce visual and geometric agreement, leaving the underlying interaction dynamics insufficiently constrained. We propose DynamicHOI, a physics-aware HOI reconstruction framework combining geometry-grounded diffusion refinement with coupled hand-object dynamics. Geometry spatially grounds visual evidence for trajectory refinement, while articulated inverse dynamics and Newton-Euler dynamic...

</details>

<details>
<summary>Share</summary>

```
DynamicHOI: Coupled Dynamics for Physics-aware HOI Reconstruction

We study hand-object interaction (HOI) reconstruction from monocular RGB videos, where partial observations can produce visually plausible yet mechanically inconsistent trajectories.

arXiv: https://arxiv.org/abs/2609.36454
Project page: https://wenliangguo.github.io/HOI-Reconstruction-Page/

#worldmodels #robotics
```

</details>

---

### [DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time](https://arxiv.org/abs/2609.35704)

**Authors:** Ziqi Ma, Hongqiao Chen, Georgia Gkioxari

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35704) | [PDF](https://arxiv.org/pdf/2609.35704) | [Project Page](https://glab-caltech.github.io/dynatokens/)

<details>
<summary>Abstract</summary>

Video generation must account for two sources of motion, one induced by the observer's camera path and the other caused by scene dynamics. An ideal camera-controlled video model should account for both motions: let users move the camera while evolving the scene dynamics. While current models handle camera-induced motion well in static settings, they struggle for dynamic scenes: objects are static, move incorrectly, or degrade in generation quality. We introduce DynaTokens, a lightweight set of learnable scene-specific tokens that teach dynamics to an existing camera-controlled world model. Our...

</details>

<details>
<summary>Share</summary>

```
DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time

Video generation must account for two sources of motion, one induced by the observer's camera path and the other caused by scene dynamics.

arXiv: https://arxiv.org/abs/2609.35704
Project page: https://glab-caltech.github.io/dynatokens/

#worldmodels #robotics
```

</details>

---

### [Graph World Models for Constrained Epidemic Policy Planning](https://arxiv.org/abs/2609.35545)

**Authors:** Yiqi Su, Rashed Shelim, Lingyi Wang, Walid Saad, Naren Ramakrishnan

**Published:** 2026-09-28 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.35545) | [PDF](https://arxiv.org/pdf/2609.35545)

<details>
<summary>Abstract</summary>

Epidemic policy planning often requires coordination between geographical regions, taking into account mobility-driven spillovers and how to make use of limited resources. Existing methods either lack action-conditioned models of coupled dynamics or cannot guarantee per-period feasibility. We present EpiMind, a graph world model framework for constrained epidemic policy planning across regions. A graph-factored recurrent state-space model generates joint policy-conditioned rollouts from regional latent beliefs, while graph-temporal ADMM optimizes regional interventions, enforces shared-resourc...

</details>

<details>
<summary>Share</summary>

```
Graph World Models for Constrained Epidemic Policy Planning

Epidemic policy planning often requires coordination between geographical regions, taking into account mobility-driven spillovers and how to make use of limited resources.

arXiv: https://arxiv.org/abs/2609.35545

#worldmodels #robotics
```

</details>

---

### [CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving](https://arxiv.org/abs/2609.34749)

**Authors:** Yu Meng, Baining Zhao, Junta Wu, Tengfei Wang, Rongze Tang et al. (13 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.34749) | [PDF](https://arxiv.org/pdf/2609.34749)

<details>
<summary>Abstract</summary>

Real-world driving is inherently multi-agent, yet most existing driving world models generate observations from a single ego vehicle. Independently extending them to multiple vehicles does not ensure that different agents observe a consistent shared world. We present CoDrive, a cross-vehicle, multi-view driving video generation framework that jointly generates observations of vehicles sharing the same dynamic scene with precise camera-trajectory control. CoDrive interleaves local self-attention, which models spatiotemporal dependencies among the views of each vehicle, with global self-attentio...

</details>

<details>
<summary>Share</summary>

```
CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving

Real-world driving is inherently multi-agent, yet most existing driving world models generate observations from a single ego vehicle.

arXiv: https://arxiv.org/abs/2609.34749

#worldmodels #robotics
```

</details>

---

### [Precise Editing and Flexible Referencing for Interactable Worlds](https://arxiv.org/abs/2609.34470)

**Authors:** Xinyao Liao, Xianfang Zeng, Zhu Liang, Zhoujie Fu, Qianxun Xu et al. (8 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34470) | [PDF](https://arxiv.org/pdf/2609.34470) | [Code](https://github.com/leoisufa/EditWorld)

<details>
<summary>Abstract</summary>

We present EditWorld, a video world model for precise editing and flexible referencing in interactable worlds. Existing video world models primarily focus on navigation, letting users explore generated worlds but offering limited control over how existing world content is modified. EditWorld extends world modeling from exploration to precise modification by streaming editing instructions and reference images during autoregressive generation. To support these capabilities, EditWorld introduces Gated Causal Attention for temporally varying editing conditions and reference images, together with a...

</details>

<details>
<summary>Share</summary>

```
Precise Editing and Flexible Referencing for Interactable Worlds

We present EditWorld, a video world model for precise editing and flexible referencing in interactable worlds.

arXiv: https://arxiv.org/abs/2609.34470
Code: https://github.com/leoisufa/EditWorld

#worldmodels #robotics
```

</details>

---

### [Behavioral Monitoring of JEPA World Models with Jacobian Centroids](https://arxiv.org/abs/2609.33940)

**Authors:** Thomas Walker, Randall Balestriero, Richard Baraniuk

**Published:** 2026-09-27 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33940) | [PDF](https://arxiv.org/pdf/2609.33940)

<details>
<summary>Abstract</summary>

Detecting failures in World Model (WM)-based planning requires monitoring whether the model is behaviorally aligned with the current task, which in turn requires studying its internal representations. Here, we show that centroids---sub-component Jacobian row-sums---effectively identify the behavioral properties of WMs, complementing traditional activation-based knowledge signals. The centroids of a model are easily computed through Jacobian vector products and characterize how the model organizes the geometry of its input space, yielding an efficient perspective on internal representations, in...

</details>

<details>
<summary>Share</summary>

```
Behavioral Monitoring of JEPA World Models with Jacobian Centroids

Detecting failures in World Model (WM)-based planning requires monitoring whether the model is behaviorally aligned with the current task, which in turn requires studying its internal representations.

arXiv: https://arxiv.org/abs/2609.33940

#worldmodels #robotics
```

</details>

---

### [MA-JEPA: Joint-Embedding World Models for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.33563)

**Authors:** Brandon Gary Kaplowitz, Osaze James Obahor, Christian Schroeder de Witt

**Published:** 2026-09-27 | **Categories:** cs.LG, cs.AI, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33563) | [PDF](https://arxiv.org/pdf/2609.33563)

<details>
<summary>Abstract</summary>

World models improve sample efficiency by training policies on imagined trajectories, but their usefulness depends on learning representations that capture the information needed for future control. We study whether self-supervised joint-embedding prediction (JEPA) can provide this learning signal for multi-agent reinforcement learning. We introduce MA-JEPA, a stochastic world model that replaces observation reconstruction with prediction of target representations, enabling model-based multi-agent reinforcement learning with centralized training and decentralized execution. A categorical laten...

</details>

<details>
<summary>Share</summary>

```
MA-JEPA: Joint-Embedding World Models for Multi-Agent Reinforcement Learning

World models improve sample efficiency by training policies on imagined trajectories, but their usefulness depends on learning representations that capture the information needed for future control.

arXiv: https://arxiv.org/abs/2609.33563

#worldmodels #robotics
```

</details>

---

### [TriO: Tri-Modal Unsupervised Occupancy World Model for Anything Perception](https://arxiv.org/abs/2609.32013)

**Authors:** Quinlan Sykora, Sourav Biswas, Christopher Diehl, Andrew Cunningham, Thomas Gilles et al. (6 authors)

**Published:** 2026-09-25 (updated 2026-09-29) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

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

### [Completion Aware Guidance for World Action Models](https://arxiv.org/abs/2610.01559)

**Authors:** Seungyeon Kim, Junhoo Lee, Baekseung Kim, Minkyu Kim, Nojun Kwak

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [Direct Experience World-Model Optimization: Learning the World Beyond Action Imitation](https://arxiv.org/abs/2609.37398)

**Authors:** Xiangcheng Zhan, Zirui Chen, Yicheng Zhao, Ziteng Gao, Shuo Yang

**Published:** 2026-09-29 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.37398) | [PDF](https://arxiv.org/pdf/2609.37398)

<details>
<summary>Abstract</summary>

World-Action Models (WAMs) couple action generation with predictions of how physical interactions unfold. However, current post-deployment learning paradigms typically improve behavior without requiring better world predictions. Especially in dexterous manipulation, small execution errors can compound in high-dimensional action spaces, hindering policy improvement and pushing interactions beyond the world model's training distribution. Motivated by this, we propose Direct Experience World-Model Optimization (DEWO), a post-deployment learning paradigm for WAMs that, alongside action imitation,...

</details>

<details>
<summary>Share</summary>

```
Direct Experience World-Model Optimization: Learning the World Beyond Action Imitation

World-Action Models (WAMs) couple action generation with predictions of how physical interactions unfold.

arXiv: https://arxiv.org/abs/2609.37398

#worldmodels #robotics
```

</details>

---

### [Inferring Soil Friction Angle from Robot Foot-Ground Force Histories: A Bayesian Inverse Approach to Proprioceptive Soil Sensing](https://arxiv.org/abs/2609.36582)

**Authors:** Dawei Xu, Zhijie Wang

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.36582) | [PDF](https://arxiv.org/pdf/2609.36582)

<details>
<summary>Abstract</summary>

Foot-ground interaction signals recorded by quadruped robots may enable spatially distributed, in situ characterization of soil strength. As a first step, we test whether the internal friction angle $φ$ of cohesionless soil can be identified from the force history of a simplified rotating leg. A two-dimensional continuum model implemented with the material point method, benchmarked against measured rotating-leg force histories, generates the training data, and two Gaussian-process surrogates support Bayesian inversion of the full histories. In matched-model experiments, the framework recovers...

</details>

<details>
<summary>Share</summary>

```
Inferring Soil Friction Angle from Robot Foot-Ground Force Histories: A Bayesian Inverse Approach to Proprioceptive Soil Sensing

Foot-ground interaction signals recorded by quadruped robots may enable spatially distributed, in situ characterization of soil strength.

arXiv: https://arxiv.org/abs/2609.36582

#worldmodels #robotics
```

</details>

---

### [Bilinear World Models: Learning Representations with Structured Dynamics for Efficient Control](https://arxiv.org/abs/2609.36305)

**Authors:** Antonio Pariente, Ignacio Boero, Nikolai Matni, Alejandro Ribeiro

**Published:** 2026-09-28 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.36305) | [PDF](https://arxiv.org/pdf/2609.36305)

<details>
<summary>Abstract</summary>

World models jointly learn latent representations and dynamics that predict how high-dimensional observations evolve under actions. In this work, we propose a JEPA-style world model in which, rather than learning arbitrary latent dynamics, we restrict them to follow a bilinear parameterization. This structure enables efficient planning and control while shifting the modeling burden onto the encoder, encouraging richer representations that expose the controllable geometry of the system. In particular, this structured parameterization allows us to structurally enforce action recoverability, ther...

</details>

<details>
<summary>Share</summary>

```
Bilinear World Models: Learning Representations with Structured Dynamics for Efficient Control

World models jointly learn latent representations and dynamics that predict how high-dimensional observations evolve under actions.

arXiv: https://arxiv.org/abs/2609.36305

#worldmodels #robotics
```

</details>

---

### [From Pixel to Poses: Object-centric Tool Manipulation Learning from Human Demonstrations](https://arxiv.org/abs/2609.35375)

**Authors:** Bangjun Wang, Longyan Wu, Yukun Wei, Shenghe Shao, Chaoyi Huang et al. (11 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.35375) | [PDF](https://arxiv.org/pdf/2609.35375)

<details>
<summary>Abstract</summary>

Scaling up robotic manipulation is primarily bottlenecked by the scarcity of real-world robot data. While recent approaches leverage human video demonstrations to mitigate this shortage, they remain computationally expensive and still rely on paired human-robot data for domain alignment. Although current state-of-the-arts excel at long-horizon tasks, they struggle with the delicate and precise control required for complex tool manipulation. To overcome these limitations, we introduce P2P-T, from Pixel to Poses for Tool Manipulation, a data-efficient, object-centric framework that learns tool u...

</details>

<details>
<summary>Share</summary>

```
From Pixel to Poses: Object-centric Tool Manipulation Learning from Human Demonstrations

Scaling up robotic manipulation is primarily bottlenecked by the scarcity of real-world robot data.

arXiv: https://arxiv.org/abs/2609.35375

#worldmodels #robotics
```

</details>

---

### [From World Models to World Action Models: Rethinking Next-State Prediction](https://arxiv.org/abs/2609.34414)

**Authors:** Tingyu Yuan, Ziming Ji, Biaoliang Guan, Wen Ye, Wenrui Tian et al. (12 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.34414) | [PDF](https://arxiv.org/pdf/2609.34414)

<details>
<summary>Abstract</summary>

Predicting the next state is a core paradigm of World Models for modeling physical dynamics, emphasizing prediction fidelity. As World Models evolve into World-Action Models (WAMs), existing methods still fix the next state before training as RGB, a single latent feature, or a static combination of predefined targets, thereby constraining action learning to the inductive biases preserved by a particular representation. To address this limitation, we propose CF-WAM, a dynamic next-state prediction framework that samples visual, semantic, geometric, and interaction projections of the same future...

</details>

<details>
<summary>Share</summary>

```
From World Models to World Action Models: Rethinking Next-State Prediction

Predicting the next state is a core paradigm of World Models for modeling physical dynamics, emphasizing prediction fidelity.

arXiv: https://arxiv.org/abs/2609.34414

#worldmodels #robotics
```

</details>

---

### [When World Models Lie: Adaptive Safety Analysis Under Wrong Imaginations](https://arxiv.org/abs/2609.34300)

**Authors:** John Cao, Somil Bansal

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.34300) | [PDF](https://arxiv.org/pdf/2609.34300)

<details>
<summary>Abstract</summary>

World models offer a powerful substrate for safety reasoning in high-dimensional robotic systems, but they are also fallible: their predictions can be biased, miscalibrated, or confidently wrong. This creates a central challenge for latent-space safety filters, which often learn Hamilton-Jacobi safety value functions on the dynamics of a world model. If the world model is incorrect, the resulting value function can inherit its errors and produce overconfident safety estimates. Existing latent safety filters often rely on auxiliary signals such as ensemble disagreement or value-target consisten...

</details>

<details>
<summary>Share</summary>

```
When World Models Lie: Adaptive Safety Analysis Under Wrong Imaginations

World models offer a powerful substrate for safety reasoning in high-dimensional robotic systems, but they are also fallible: their predictions can be biased, miscalibrated, or confidently wrong.

arXiv: https://arxiv.org/abs/2609.34300

#worldmodels #robotics
```

</details>

---

### [Beyond One-Step Accuracy: State-Affine Latent Transition for Reliable Visual Planning](https://arxiv.org/abs/2609.33595)

**Authors:** Boyuan Zhang, Yingjun Du, Xiantong Zhen, Ling Shao

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.33595) | [PDF](https://arxiv.org/pdf/2609.33595)

<details>
<summary>Abstract</summary>

Joint-embedding world models enable visual planning by learning action-conditioned dynamics in latent space. Yet they are commonly trained for one-step prediction on encoded states, while planning recursively applies the learned transition to its own predictions. One-step accuracy therefore does not capture how prediction errors propagate under recursive rollout. We decompose multi-step rollout error into the errors introduced at individual steps and their propagation through subsequent transitions. We show that state-affine dynamics are precisely the differentiable transitions with state-inde...

</details>

<details>
<summary>Share</summary>

```
Beyond One-Step Accuracy: State-Affine Latent Transition for Reliable Visual Planning

Joint-embedding world models enable visual planning by learning action-conditioned dynamics in latent space.

arXiv: https://arxiv.org/abs/2609.33595

#worldmodels #robotics
```

</details>

---

### [VehDyn: A Driving World Model Benchmark for Vehicle Dynamics](https://arxiv.org/abs/2609.33264)

**Authors:** Tianyi Wang, Wangsheng Du, Jiazhou Chen, Tianyi Zeng, Xiangyu Li et al. (15 authors)

**Published:** 2026-09-27 | **Categories:** cs.CV, cs.AI, cs.ET | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.33264) | [PDF](https://arxiv.org/pdf/2609.33264)

<details>
<summary>Abstract</summary>

Video world models are emerging as data engines, action planners, and generative simulators for autonomous driving, but existing benchmarks primarily assess visual fidelity and coarse physical plausibility, providing limited evidence on whether generated driving futures obey realistic vehicle kinematics and dynamics. This limitation is further compounded by the lack of datasets in which vehicle, road, maneuver, and speed conditions are independently controlled, and ground-truth vehicle states are recorded in synchrony with videos. We introduce VehDyn, a driving world model benchmark for vehicl...

</details>

<details>
<summary>Share</summary>

```
VehDyn: A Driving World Model Benchmark for Vehicle Dynamics

Video world models are emerging as data engines, action planners, and generative simulators for autonomous driving, but existing benchmarks primarily assess visual fidelity and coarse physical plausibility, providing...

arXiv: https://arxiv.org/abs/2609.33264

#worldmodels #robotics
```

</details>

---

### [SwingRL: Adaptive Observation Reinforcement Learning with World-Model Prediction for Cable-Suspended Hoisting Control](https://arxiv.org/abs/2609.33053)

**Authors:** Guangming Wang, Xiaoyu Zhang, Yucheng Xin, Wanli Ma, Jiucai Liu et al. (11 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.33053) | [PDF](https://arxiv.org/pdf/2609.33053)

<details>
<summary>Abstract</summary>

Cable-suspended hoisting is widely used to move heavy or bulky payloads that cannot be handled conveniently by rigid pick-and-place systems, for example in crane-assisted construction. Robotic hoisting using flexible cables is challenging because payload motion is underactuated, external disturbances vary, and delayed or lost visual observations can make the perceived payload state stale at control execution. These effects are particularly critical during precise insertion of a suspended payload's sockets onto rebar pins, which is a very common task in construction environments. We present Swi...

</details>

<details>
<summary>Share</summary>

```
SwingRL: Adaptive Observation Reinforcement Learning with World-Model Prediction for Cable-Suspended Hoisting Control

Cable-suspended hoisting is widely used to move heavy or bulky payloads that cannot be handled conveniently by rigid pick-and-place systems, for example in crane-assisted construction.

arXiv: https://arxiv.org/abs/2609.33053

#worldmodels #robotics
```

</details>

---

### [ROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205)

**Authors:** Zheng-Hui Huang, Guixu Lin, Yu-Ju Tsai, Jian-Kai Zhu, Fengbo Lan et al. (9 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.02205) | [PDF](https://arxiv.org/pdf/2610.02205)

<details>
<summary>Abstract</summary>

Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines. However, their visual adherence to explicit rules and interactions remains insufficiently evaluated. Existing benchmarks assess visual quality, controllability, and instruction or physical adherence, but rarely test fidelity to fine-grained, program-specified world events. We introduce PROWBench, comprising 170 programmatically constructed episodes and 600 proxy videos covering diverse scenes and interactions. PROWBench logs entity states and timestam...

</details>

<details>
<summary>Share</summary>

```
ROWBench: Do Video Models Render What the Program Specifies?

Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines.

arXiv: https://arxiv.org/abs/2610.02205

#worldmodels #robotics
```

</details>

---

### [World-as-Graph: Relational World Modeling Through Latent Space Graphs](https://arxiv.org/abs/2609.38927)

**Authors:** Yaqi Yang, Shuo Huang, Yujin Huang, Fucai Ke, Jiatong Han et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.LG, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](https://arxiv.org/abs/2609.38562)

**Authors:** Byoungwoo Park, Jaemoo Choi, Juho Lee, Yongxin Chen

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.38562) | [PDF](https://arxiv.org/pdf/2609.38562)

<details>
<summary>Abstract</summary>

World models, game simulators, and long-take video creation require coherent scene evolution and sustained dynamics over extended durations. Autoregressive (AR) video diffusion provides a natural framework for long-horizon generation, yet extended rollouts often become near-static or lose visual quality. We hypothesize that these failures reflect the limited guidance provided by short-video supervision on how ongoing scene dynamics develops over longer durations. This motivates us to introduce LongTake, a two-stage training pipeline built around Long-Horizon Teacher Forcing (TF) on curated rea...

</details>

<details>
<summary>Share</summary>

```
LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation

World models, game simulators, and long-take video creation require coherent scene evolution and sustained dynamics over extended durations.

arXiv: https://arxiv.org/abs/2609.38562

#worldmodels #robotics
```

</details>

---

### [DSWM: Decomposed Spatio-Temporal World Model for Demand-Driven UAV Base Station Repositioning](https://arxiv.org/abs/2609.36845)

**Authors:** Shengjie Zhong, Zhongliang Zhao, Jingxuan Chen, Xianbin Cao, Xinmei Qiang et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.NI, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.36845) | [PDF](https://arxiv.org/pdf/2609.36845)

<details>
<summary>Abstract</summary>

Uncrewed aerial vehicle base stations (UAV-BSs) are expected to cover traffic demand that shifts across space and time, yet most repositioning schemes either re-solve an optimization problem per slot or learn reactive policies without an explicit demand model. We cast demand-driven fleet repositioning as latent-space decision-time planning and propose DSWM, a decomposed spatio-temporal world model: an agentic controller that perceives the demand field through a rolling observation window, retains operational context in a latent recurrent state, reasons about candidate motions by imagined rollo...

</details>

<details>
<summary>Share</summary>

```
DSWM: Decomposed Spatio-Temporal World Model for Demand-Driven UAV Base Station Repositioning

Uncrewed aerial vehicle base stations (UAV-BSs) are expected to cover traffic demand that shifts across space and time, yet most repositioning schemes either re-solve an optimization problem per slot or learn reactive...

arXiv: https://arxiv.org/abs/2609.36845

#worldmodels #robotics
```

</details>

---

### [MeteoVerse: Unified Weather-Controllable Video World Model](https://arxiv.org/abs/2609.36810)

**Authors:** Renlong Wu, Guanqiao Wang, Xuan Shang, Yin Hanming, Xiaoxiao Sheng et al. (8 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.36810) | [PDF](https://arxiv.org/pdf/2609.36810)

<details>
<summary>Abstract</summary>

Video world models aim to predict future content from an observed scene while following prescribed camera motion. Real-world scene evolution is determined not only by changes in viewpoint and object dynamics, but also by environmental conditions such as weather, which can substantially alter scene appearance and visibility. Modeling such realistic weather evolution is challenging because the required weather modification depends jointly on the observed and desired weather states. Depending on their relation, the model may need to preserve, introduce, or remove a weather effect. Existing video...

</details>

<details>
<summary>Share</summary>

```
MeteoVerse: Unified Weather-Controllable Video World Model

Video world models aim to predict future content from an observed scene while following prescribed camera motion.

arXiv: https://arxiv.org/abs/2609.36810

#worldmodels #robotics
```

</details>

---

### [Control-Geometry Straightening for Sampling-Based Latent Planning](https://arxiv.org/abs/2609.35603)

**Authors:** Ziang Fu, Ning Ning

**Published:** 2026-09-28 | **Categories:** cs.LG, stat.ML | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.35603) | [PDF](https://arxiv.org/pdf/2609.35603)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures enable planning with latent world models, but accurate transition prediction alone does not ensure that the planning objective is easy to optimize. We introduce Control-Geometry Straightening (CGS), a single auxiliary loss that learns planner-friendly representations by directly straightening control geometry for sampling-efficient planning. CGS matches pairwise cosine similarities among actions to those among corresponding latent differences only using local transitions from pixel-action pairs. The loss can be applied across world-model architectures u...

</details>

<details>
<summary>Share</summary>

```
Control-Geometry Straightening for Sampling-Based Latent Planning

Joint-embedding predictive architectures enable planning with latent world models, but accurate transition prediction alone does not ensure that the planning objective is easy to optimize.

arXiv: https://arxiv.org/abs/2609.35603

#worldmodels #robotics
```

</details>

---

### [Embodied Semantic Communication for Collective Autonomous Agents: A Tutorial on Representation, Wireless Delivery, and Closed-Loop Coordination](https://arxiv.org/abs/2609.35936)

**Authors:** Yizheng Huang, Wensheng Lin, Lixin Li, Qinghe Du, Wenchi Cheng et al. (6 authors)

**Published:** 2026-09-28 | **Categories:** cs.MA, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2609.35936) | [PDF](https://arxiv.org/pdf/2609.35936)

<details>
<summary>Abstract</summary>

As autonomous systems and embodied intelligence enter the dynamic physical world, multi-agent collaboration calls for a paradigm shift in communication design. However, existing communication paradigms overlook that agents form action understanding from their own states, environmental observations, and collaboration relations through a process that evolves as a task unfolds. Consequently, reliable bit delivery, general semantic recovery, or single-task utility optimization alone cannot ensure that heterogeneous agents form coordinated actions compatible with their own conditions from shared in...

</details>

<details>
<summary>Share</summary>

```
Embodied Semantic Communication for Collective Autonomous Agents: A Tutorial on Representation, Wireless Delivery, and Closed-Loop Coordination

As autonomous systems and embodied intelligence enter the dynamic physical world, multi-agent collaboration calls for a paradigm shift in communication design.

arXiv: https://arxiv.org/abs/2609.35936

#worldmodels #robotics
```

</details>

---

### [OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052)

**Authors:** Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin et al. (16 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.35052) | [PDF](https://arxiv.org/pdf/2609.35052)

<details>
<summary>Abstract</summary>

Video world models must preserve the visual state of the world over time, but existing evaluation protocols often rely on generated histories, video reference, or selected revisit viewpoints that can confound the assessment of a model's true memory capability. To address this, we introduce OPIS, an input-grounded benchmark that strictly anchors the assessment to a fixed set of object instances from the initial observation for evaluating multi-object memory in video world models. The OPIS dataset comprises 500 cases across real-world, embodied-robotic, and game-world domains, providing dense ob...

</details>

<details>
<summary>Share</summary>

```
OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models

Video world models must preserve the visual state of the world over time, but existing evaluation protocols often rely on generated histories, video reference, or selected revisit viewpoints that can confound the asse...

arXiv: https://arxiv.org/abs/2609.35052

#worldmodels #robotics
```

</details>

---

### [Do World Models Learn Global Understanding?](https://arxiv.org/abs/2609.34058)

**Authors:** Alexander Detkov, Matt Thomson

**Published:** 2026-09-28 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.34058) | [PDF](https://arxiv.org/pdf/2609.34058)

<details>
<summary>Abstract</summary>

AI systems often feel brittle and fragmented. A large language model (LLM) may correctly explain a concept but fail to apply it, or follow safety instructions in one context but not another. This behavior suggests a general failure to lift local information to a global understanding. To gain fundamental insight, we frame "understanding" as learning constraints and propagating their consequences. We construct learning tasks on monoid worlds, sets of states connected by action transitions, where observed training transitions and an unseen constraint jointly determine held-out transitions. Measur...

</details>

<details>
<summary>Share</summary>

```
Do World Models Learn Global Understanding?

AI systems often feel brittle and fragmented.

arXiv: https://arxiv.org/abs/2609.34058

#worldmodels #robotics
```

</details>

---

### [Adaptive Latent Capacity for World Models](https://arxiv.org/abs/2609.32921)

**Authors:** Idan Achituve, Lior Dikstein, Idit Diamant, Arnon Netzer, Hai Victor Habi

**Published:** 2026-09-26 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.32921) | [PDF](https://arxiv.org/pdf/2609.32921)

<details>
<summary>Abstract</summary>

We introduce Adaptive LeWorldModel (ALeWM), a world model based on a joint-embedding predictive architecture (JEPA) that learns to concentrate predictive information in compact prefixes of a wide latent representation. To encourage this ordering, ALeWM learns a sequence-conditioned distribution over prefix lengths and trains the predictor to estimate the full next embedding from a sampled input prefix. As standard anti-collapse objectives encourage variation across latent coordinates and do not organize them by predictive importance, we also introduce MixSIGReg. MixSIGReg regularizes the maske...

</details>

<details>
<summary>Share</summary>

```
Adaptive Latent Capacity for World Models

We introduce Adaptive LeWorldModel (ALeWM), a world model based on a joint-embedding predictive architecture (JEPA) that learns to concentrate predictive information in compact prefixes of a wide latent representation.

arXiv: https://arxiv.org/abs/2609.32921

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

**Published:** 2026-09-26 (updated 2026-09-30) | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

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

### [DeltaWAM: Change-Centric Visual Foresight via Delta Tokens for an Efficient World-Action Model](https://arxiv.org/abs/2609.33177)

**Authors:** Tianyun Jiang, Wenrui Bao, Bingxin Xu, Yu Tian, Yuzhang Shang

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.33177) | [PDF](https://arxiv.org/pdf/2609.33177)

<details>
<summary>Abstract</summary>

World-Action Models (WAMs) offer visual foresight for robotic manipulation, but pixel-space models repeatedly reconstruct entire future scenes, incurring high computational cost and spatio-temporal redundancy. In physical manipulation, consecutive frames often share most of their visual context; the changes between them are what an action policy needs to anticipate. We introduce DeltaWAM, a change-centric WAM that makes a compact delta token the unit of future prediction. Each token is a single vector encoding changes between consecutive dense DINO feature maps. DeltaWAM builds on DeltaWorld,...

</details>

<details>
<summary>Share</summary>

```
DeltaWAM: Change-Centric Visual Foresight via Delta Tokens for an Efficient World-Action Model

World-Action Models (WAMs) offer visual foresight for robotic manipulation, but pixel-space models repeatedly reconstruct entire future scenes, incurring high computational cost and spatio-temporal redundancy.

arXiv: https://arxiv.org/abs/2609.33177

#worldmodels #robotics
```

</details>

---

### [Think Fast, Plan Selectively: Adaptive Deliberation for Efficient Data-Driven MPC](https://arxiv.org/abs/2609.32591)

**Authors:** Yi Xian Goh, Sze Jue Yang, Hao Luan

**Published:** 2026-09-26 (updated 2026-09-30) | **Categories:** cs.RO, cs.LG | **Relevance:** ★☆☆☆☆

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

### [An Empirical Study of Architectural Shift from Traditional to AI-Enabled Simulink Controllers](https://arxiv.org/abs/2609.38504)

**Authors:** Hadiza Umar Yusuf, Khouloud Gaaloul

**Published:** 2026-09-29 | **Categories:** cs.SE, cs.AI, eess.SY | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.38504) | [PDF](https://arxiv.org/pdf/2609.38504)

<details>
<summary>Abstract</summary>

Effective AI adoption in cyber-physical systems (CPS) depends on embedding design knowledge into engineering practice. Yet as AI-enabled components increasingly replace analytically derived control laws, this occurs without a systematic understanding of how controller architectures differ or remain similar across paradigms. We address this gap with an empirical study of traditional and AI-enabled Simulink controllers, guided by a literature-derived taxonomy of ten structural categories and nine functional roles. The study analyzes 62 real-world models spanning 8 controller types and 10 applica...

</details>

<details>
<summary>Share</summary>

```
An Empirical Study of Architectural Shift from Traditional to AI-Enabled Simulink Controllers

Effective AI adoption in cyber-physical systems (CPS) depends on embedding design knowledge into engineering practice.

arXiv: https://arxiv.org/abs/2609.38504

#worldmodels #robotics
```

</details>

---

### [Abductive World Modeling via Causal Representation Learning](https://arxiv.org/abs/2609.36985)

**Authors:** Ziqi Liu, Songhan Yang, Linfan Zhou, Jiatong Liu, Lijun Peng et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.LG, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.36985) | [PDF](https://arxiv.org/pdf/2609.36985)

<details>
<summary>Abstract</summary>

The central challenge of world modeling is to learn representations that capture how the world evolves. However, existing world models predominantly represent future states without explicitly capturing the latent causes underlying their evolution, limiting their ability to reason about why and how the world changes. To address this limitation, we propose Abductive World Modeling (AWM), a framework that learns structured causal representations by abductively inferring latent causes from predicted futures. Specifically, we realize AWM through the Hierarchical Abductive State Pyramid (HASP), whic...

</details>

<details>
<summary>Share</summary>

```
Abductive World Modeling via Causal Representation Learning

The central challenge of world modeling is to learn representations that capture how the world evolves.

arXiv: https://arxiv.org/abs/2609.36985

#worldmodels #robotics
```

</details>

---

### [Shaping Persistent Representations from Independent Interactions](https://arxiv.org/abs/2609.34604)

**Authors:** Ji Dai, Quan Fang, Junyu Gao, Rongfeng Guo, Haoyan Rong et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.34604) | [PDF](https://arxiv.org/pdf/2609.34604)

<details>
<summary>Abstract</summary>

World models learn environment dynamics from interaction experience. These dynamics depend on the current state and actions, as well as on properties that persist across interactions. Yet standard predictive training can reduce error using local evidence alone, without organizing persistent information into reusable context. We introduce SPRII, a training principle that uses relations between interactions as weak supervision for persistent context while retaining the learner's native objective. For example, different trajectories of the same system share persistent properties even when their s...

</details>

<details>
<summary>Share</summary>

```
Shaping Persistent Representations from Independent Interactions

World models learn environment dynamics from interaction experience.

arXiv: https://arxiv.org/abs/2609.34604

#worldmodels #robotics
```

</details>

---

### [ReDrive: Shaping Representations with World Modeling for End-to-End Driving](https://arxiv.org/abs/2609.33854)

**Authors:** Yueting Zhu, Shaoyu Chen, Yuehao Song, Hui Sun, Qian Zhang et al. (7 authors)

**Published:** 2026-09-27 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.33854) | [PDF](https://arxiv.org/pdf/2609.33854)

<details>
<summary>Abstract</summary>

Driving policies require capabilities of scene understanding and future evolution prediction. To achieve this goal, current end-to-end models typically construct complex perception-planning pipelines or introduce world models that explicitly predict future states, resulting in a complex system architecture. Inspired by the transferability of general-purpose visual representations, we argue that combining sufficiently strong visual representations with representation world modeling can support effective planning without relying on complex inference-time auxiliary modules. Based on this insight,...

</details>

<details>
<summary>Share</summary>

```
ReDrive: Shaping Representations with World Modeling for End-to-End Driving

Driving policies require capabilities of scene understanding and future evolution prediction.

arXiv: https://arxiv.org/abs/2609.33854

#worldmodels #robotics
```

</details>

---

### [ViBR-WM: Visual Bayesian Regression for World Modeling](https://arxiv.org/abs/2609.33844)

**Authors:** Jifan Li, Ning Ning

**Published:** 2026-09-27 | **Categories:** stat.ME, cs.CV, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.33844) | [PDF](https://arxiv.org/pdf/2609.33844)

<details>
<summary>Abstract</summary>

Modeling temporal dependence and uncertainty is central to forecasting with world models. The Visual Bayesian Regression World Model combines visual features, physical histories and known covariates through interpretable regression, within a modular architecture supporting trend, seasonal and cycle dynamics. Visual compression reduces representation dimension, while Bayesian variable selection reduces active regression dimension. Posterior prediction combines forecasts across predictor subsets using their posterior probabilities as weights and accounts for parameter uncertainty and future dist...

</details>

<details>
<summary>Share</summary>

```
ViBR-WM: Visual Bayesian Regression for World Modeling

Modeling temporal dependence and uncertainty is central to forecasting with world models.

arXiv: https://arxiv.org/abs/2609.33844

#worldmodels #robotics
```

</details>

---

### [MultiEcho: An Experimental Science of Learned Worlds](https://arxiv.org/abs/2609.33347)

**Authors:** Meng Zhu, Airui Zhang

**Published:** 2026-09-27 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.33347) | [PDF](https://arxiv.org/pdf/2609.33347)

<details>
<summary>Abstract</summary>

World models can be studied as experimental systems with response laws of their own. We introduce MultiEcho, a framework for estimating these laws through controlled counterfactual interventions, delimiting their applicability, and separately testing their physical correspondence. Across nine simulated physical systems and seven frozen model configurations, three-reference estimators predict complete intervention responses and recover intervention parameters. Estimator selection uses discovery data only; frozen fits are evaluated on validation and confirmation contexts. The experiments disting...

</details>

<details>
<summary>Share</summary>

```
MultiEcho: An Experimental Science of Learned Worlds

World models can be studied as experimental systems with response laws of their own.

arXiv: https://arxiv.org/abs/2609.33347

#worldmodels #robotics
```

</details>

---

### [Beyond Conservatism: Recoverability-Conditioned Exploration for Model-Based Imitation Learning](https://arxiv.org/abs/2609.33336)

**Authors:** Xuanlin Chen, Ziyue Wang, Xunlan Zhou, Yuan-yih Shang, Qiang Wu et al. (6 authors)

**Published:** 2026-09-27 | **Categories:** cs.LG, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.33336) | [PDF](https://arxiv.org/pdf/2609.33336)

<details>
<summary>Abstract</summary>

Model-based imitation learning (MBIL) improves real-environment interaction efficiency by optimizing policies on imagined rollouts from a learned world model. However, the gap between model-induced and real-environment occupancies makes policy learning sensitive to model error. Conservative MBIL mitigates model exploitation during policy optimization, but when real-environment interactions are collected by the same conservative policy, uncertain regions around the expert distribution remain insufficiently sampled. Generic uncertainty-driven exploration, on the other hand, may allocate interact...

</details>

<details>
<summary>Share</summary>

```
Beyond Conservatism: Recoverability-Conditioned Exploration for Model-Based Imitation Learning

Model-based imitation learning (MBIL) improves real-environment interaction efficiency by optimizing policies on imagined rollouts from a learned world model.

arXiv: https://arxiv.org/abs/2609.33336

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
