# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-22 19:45 UTC

**Papers shown:** 72 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning](https://arxiv.org/abs/2610.28613)

**Authors:** Zebin Xing, Yuhang Zheng, Yupeng Zheng, Yichen Zhang, Zichen Li et al. (11 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28613) | [PDF](https://arxiv.org/pdf/2610.28613) | [Project Page](https://zebinx.github.io/PhysCanvas_HomePage/)

<details>
<summary>Abstract</summary>

Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators. However, visually plausible predictions can misrepresent contact dynamics, providing unreliable feedback for policy evaluation and learning. We introduce PhysCanvas, a state-consistent visuo-tactile world model for contact-rich robot manipulation. PhysCanvas unifies multi-view RGB, tactile images, marker displacement, task state, and actions within a unified vision space. All modalities share a video VAE and pretrained...

</details>

<details>
<summary>Share</summary>

```
Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning

Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators.

arXiv: https://arxiv.org/abs/2610.28613
Project page: https://zebinx.github.io/PhysCanvas_HomePage/

#worldmodels #robotics
```

</details>

---

### [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)

**Authors:** Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu et al. (15 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.26855) | [PDF](https://arxiv.org/pdf/2610.26855) | [Project Page](https://ropedia.github.io/ropedia-w0/) | [Code](https://github.com/Ropedia/ropedia-w0)

<details>
<summary>Abstract</summary>

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through ca...

</details>

<details>
<summary>Share</summary>

```
Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited mul...

arXiv: https://arxiv.org/abs/2610.26855
Project page: https://ropedia.github.io/ropedia-w0/
Code: https://github.com/Ropedia/ropedia-w0

#worldmodels #robotics
```

</details>

---

### [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120)

**Authors:** Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei et al. (8 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.30120) | [PDF](https://arxiv.org/pdf/2610.30120) | [Project Page](https://ucsc-vlaa.github.io/ALPS/) | [Code](https://github.com/UCSC-VLAA/ALPS)

<details>
<summary>Abstract</summary>

World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection. However, existing encoders typically specialize in only one or two of these capabilities; we therefore introduce ALPS, a pretrained visual state encoder that unifies all three in a single set of patch tokens. Using only still images and text, we pretrain a ViT-B/16 from scratch with language, reconstruction,...

</details>

<details>
<summary>Share</summary>

```
ALPS: Visual State Encoders for World Models

World models turn visual representations into predictions and actions.

arXiv: https://arxiv.org/abs/2610.30120
Project page: https://ucsc-vlaa.github.io/ALPS/
Code: https://github.com/UCSC-VLAA/ALPS

#worldmodels #robotics
```

</details>

---

### [LaLa-World: Scaling Latent World Models with Natural Language Actions](https://arxiv.org/abs/2610.27851)

**Authors:** Junha Song, Geonmo Gu, Jeongeun Park, Heejeong Nam, Lucas Maes et al. (8 authors)

**Published:** 2026-10-20 (updated 2026-10-21) | **Categories:** cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.27851) | [PDF](https://arxiv.org/pdf/2610.27851) | [Project Page](https://june-page.github.io/lala-world/) | [Code](https://github.com/junha1125/LaLa-World)

<details>
<summary>Abstract</summary>

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs make this work. First, we describe both numerical actions and visual changes in language, enabling j...

</details>

<details>
<summary>Share</summary>

```
LaLa-World: Scaling Latent World Models with Natural Language Actions

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models.

arXiv: https://arxiv.org/abs/2610.27851
Project page: https://june-page.github.io/lala-world/
Code: https://github.com/junha1125/LaLa-World

#worldmodels #robotics
```

</details>

---

### [EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959)

**Authors:** X. Feng, J. Tang, Z. Lin, L. Chen, S. Shao et al. (7 authors)

**Published:** 2026-10-19 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25959) | [PDF](https://arxiv.org/pdf/2610.25959) | [Project Page](https://xiaokunfeng.github.io/EmbodiedWorld-200K/)

<details>
<summary>Abstract</summary>

Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leaving general embodied agents for open-world settings under-explored. We refer to such agents as Embodied World Agents (EWAs), whose defining property is the ability to understand diverse visual environments and execute general actions in open-world conditions. To advance EWA research, we study open-world embodied navigat...

</details>

<details>
<summary>Share</summary>

```
EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models

Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence.

arXiv: https://arxiv.org/abs/2610.25959
Project page: https://xiaokunfeng.github.io/EmbodiedWorld-200K/

#worldmodels #robotics
```

</details>

---

### [RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation](https://arxiv.org/abs/2610.27782)

**Authors:** Siyuan Ma, Yu Qi, Cheng Ye, Ruotian Peng, Xinyi Xu et al. (11 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.27782) | [PDF](https://arxiv.org/pdf/2610.27782) | [Project Page](https://spherelab.ai/RoboJudge)

<details>
<summary>Abstract</summary>

Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark measures two fundamental dimensions, Physical Adherence and Instruction Alignment, across 800 human-ann...

</details>

<details>
<summary>Share</summary>

```
RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation

Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions.

arXiv: https://arxiv.org/abs/2610.27782
Project page: https://spherelab.ai/RoboJudge

#worldmodels #robotics
```

</details>

---

### [Exploring Temporal Context-Aware Physical Grounding in Latent World Models](https://arxiv.org/abs/2610.28483)

**Authors:** Yilei Man, Yang Chen, Jingcai Guo

**Published:** 2026-10-20 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28483) | [PDF](https://arxiv.org/pdf/2610.28483) | [Code](https://github.com/myl11045/G-JEPA)

<details>
<summary>Abstract</summary>

Learning latent dynamics is fundamental to building action-conditioned world models for planning. Among existing families, Joint Embedding Predictive Architectures (JEPAs) offer a natural framework by modeling transitions directly in latent space rather than at the pixel level. However, two issues remain in JEPA-based world models: (i) physical grounding lacks explicit aggregation of temporal context and (ii) action planning always overly relies on generic sampling distributions. To this end, we propose $\mathcal{G}$-JEPA, which incorporates temporal context into physical grounding for latent...

</details>

<details>
<summary>Share</summary>

```
Exploring Temporal Context-Aware Physical Grounding in Latent World Models

Learning latent dynamics is fundamental to building action-conditioned world models for planning.

arXiv: https://arxiv.org/abs/2610.28483
Code: https://github.com/myl11045/G-JEPA

#worldmodels #robotics
```

</details>

---

### [PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125)

**Authors:** Yunhao Luo, Wentao He, Yinpei Dai, Hyelin Nam, Hongze Fu et al. (8 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.30125) | [PDF](https://arxiv.org/pdf/2610.30125) | [Project Page](https://physical-world.github.io/)

<details>
<summary>Abstract</summary>

Existing world models typically perceive a scene through current visual frame or a narrow history window. However, these observations may not reveal the physics properties that determine transition dynamics, such as an object's mass distribution, joint damping, or surface friction. Without calibrating these physics factors for world models, predictions tend to regress toward an empirical prior and induce severe drift in novel test scenes. To this end, we propose PhysiCalWorld, which calibrates action-conditioned world models to the instance-specific dynamics via in-context prompting, without f...

</details>

<details>
<summary>Share</summary>

```
PhysiCalWorld: In-Context Physics Calibration for World Models

Existing world models typically perceive a scene through current visual frame or a narrow history window.

arXiv: https://arxiv.org/abs/2610.30125
Project page: https://physical-world.github.io/

#worldmodels #robotics
```

</details>

---

### [SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)

**Authors:** Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz et al. (7 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28480) | [PDF](https://arxiv.org/pdf/2610.28480) | [Project Page](https://supermimic.github.io)

<details>
<summary>Abstract</summary>

Tracking large human-motion datasets has become the dominant route to general, expressive humanoid whole-body control, but scaling across many motions is expensive. Current pipelines use model-free reinforcement learning, either merging per-motion specialists through lossy distillation, or brute-forcing a single policy with cluster-scale compute. SuperMimic amortizes learning across all motions with one differentiable world model of their shared dynamics, fit from logged transitions of a standard rigid-body simulator. The world model and the tracking policy train together in one loop, and back...

</details>

<details>
<summary>Share</summary>

```
SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model

Tracking large human-motion datasets has become the dominant route to general, expressive humanoid whole-body control, but scaling across many motions is expensive.

arXiv: https://arxiv.org/abs/2610.28480
Project page: https://supermimic.github.io

#worldmodels #robotics
```

</details>

---

### [ACTS: Learning Visuo-Tactile World Models from Human Physical Interaction](https://arxiv.org/abs/2610.24285)

**Authors:** Yuxiang Ma, Weihan Xu, Pengfei Ye, Anna Mei, Yuxin Ray Song et al. (8 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.24285) | [PDF](https://arxiv.org/pdf/2610.24285) | [Project Page](https://acts-anon.github.io/)

<details>
<summary>Abstract</summary>

Abstract Action-conditioned world models for contact-rich manipulation require data that captures how contact forms, slides, and releases under varying force. Such data are slow to collect through robot teleoperation, which often lacks force feedback and is constrained by gripper geometry. We ask whether these dynamics can instead be learned from human physical interaction and transferred to a robot. We present ACTS, a visuo-tactile world model trained only on human interaction data. Operators manipulate handheld GelSight sensors while we record third-person and wrist video, tactile images, 6-...

</details>

<details>
<summary>Share</summary>

```
ACTS: Learning Visuo-Tactile World Models from Human Physical Interaction

Abstract Action-conditioned world models for contact-rich manipulation require data that captures how contact forms, slides, and releases under varying force.

arXiv: https://arxiv.org/abs/2610.24285
Project page: https://acts-anon.github.io/

#worldmodels #robotics
```

</details>

---

### [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)

**Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu et al. (7 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.29989) | [PDF](https://arxiv.org/pdf/2610.29989) | [Project Page](https://hellorpg.github.io/looking-ahead/)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective jointly optimized with teacher-forced denoising that predicts temporally separated chunks without access to the intervening visual context. Drawing supervision directly from training v...

</details>

<details>
<summary>Share</summary>

```
Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve.

arXiv: https://arxiv.org/abs/2610.29989
Project page: https://hellorpg.github.io/looking-ahead/

#worldmodels #robotics
```

</details>

---

### [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](https://arxiv.org/abs/2610.29408)

**Authors:** Xinyu Wang, Huafeng Shi, Yue Ma, Zijie Meng, Teng Xi et al. (12 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.29408) | [PDF](https://arxiv.org/pdf/2610.29408) | [Project Page](https://liveact-ai.github.io)

<details>
<summary>Abstract</summary>

Interactive video world models predict how an environment evolves under user actions, but most existing systems assume one controlled agent and one task-specific action interface. We study multi-agent video world modeling, where one model generates a joint visual future for multiple controlled agents while interpreting heterogeneous controls ranging from binary game buttons to continuous robot commands. This task presents two complementary challenges. First, every agent-indexed action stream must control its intended visual entity independently. Second, the model must adapt the meaning of each...

</details>

<details>
<summary>Share</summary>

```
LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces

Interactive video world models predict how an environment evolves under user actions, but most existing systems assume one controlled agent and one task-specific action interface.

arXiv: https://arxiv.org/abs/2610.29408
Project page: https://liveact-ai.github.io

#worldmodels #robotics
```

</details>

---

### [AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631)

**Authors:** Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou

**Published:** 2026-10-20 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28631) | [PDF](https://arxiv.org/pdf/2610.28631) | [Project Page](https://weiqi-zhang.github.io/AEON)

<details>
<summary>Abstract</summary>

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space whi...

</details>

<details>
<summary>Share</summary>

```
AEON: Unifying Video and 3D World Models

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D...

arXiv: https://arxiv.org/abs/2610.28631
Project page: https://weiqi-zhang.github.io/AEON

#worldmodels #robotics
```

</details>

---

### [World Models with Configurable Perception](https://arxiv.org/abs/2610.27914)

**Authors:** Yijun Shen, Delong Chen, Xianming Hu, Kai Zhang, Pascale Fung

**Published:** 2026-10-20 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.27914) | [PDF](https://arxiv.org/pdf/2610.27914) | [Project Page](https://configwm.github.io)

<details>
<summary>Abstract</summary>

Real-world observations are noisy and often contain excessive task-irrelevant information. Effective world modeling and planning need to abstract observations into world state representations while filtering out irrelevant information. However, encoders in existing world models are typically non-adaptive, leading to state representations that are easily distracted by task-irrelevant information. As a result, the model may not selectively filter observations to cater to different task demands. To address this problem, we introduce ConfigWM, which realizes configurable perception through task-co...

</details>

<details>
<summary>Share</summary>

```
World Models with Configurable Perception

Real-world observations are noisy and often contain excessive task-irrelevant information.

arXiv: https://arxiv.org/abs/2610.27914
Project page: https://configwm.github.io

#worldmodels #robotics
```

</details>

---

### [ActionRoPE: Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models](https://arxiv.org/abs/2610.25861)

**Authors:** Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin

**Published:** 2026-10-19 (updated 2026-10-20) | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25861) | [PDF](https://arxiv.org/pdf/2610.25861) | [Project Page](https://teawhite.cn/ActionRoPE/)

<details>
<summary>Abstract</summary>

Game world models have made rapid progress toward real-time interactive generation. Yet action control is still predominantly implemented as feature conditioning, leaving the model to learn from training data how each action should move the visual world. This formulation is poorly matched to a broad class of planar-camera worlds, such as top-down and isometric games. In these worlds, player motion induces a geometrically well-defined planar camera displacement. We observe that the key to spatially consistent control in such worlds is to represent the effect of each action directly in world coo...

</details>

<details>
<summary>Share</summary>

```
ActionRoPE: Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models

Game world models have made rapid progress toward real-time interactive generation.

arXiv: https://arxiv.org/abs/2610.25861
Project page: https://teawhite.cn/ActionRoPE/

#worldmodels #robotics
```

</details>

---

### [TESS: LLM-guided Translation, Exploration, Simulation, and Search for Embodied Task Planning](https://arxiv.org/abs/2610.25930)

**Authors:** Peiran Xu, Yixiang Yang, Jinghan Li, Fei Li, Cao Sheng et al. (7 authors)

**Published:** 2026-10-19 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25930) | [PDF](https://arxiv.org/pdf/2610.25930) | [Code](https://github.com/woyut/TESS_EMNLP26)

<details>
<summary>Abstract</summary>

In this work we focus on the problem of embodied task planning, which requires an agent to accomplish a complex task by separating it into atomic actions. Recent studies have developed LLM-based methods to address this problem. However, the executability and correctness of the generated plans remain suboptimal in complex environments and tasks. On the other hand, classical search algorithms have the potential to solve the planning problems perfectly, yet they require fully observable environments, known state transitions and goal state, which are often unattainable in general task domains. The...

</details>

<details>
<summary>Share</summary>

```
TESS: LLM-guided Translation, Exploration, Simulation, and Search for Embodied Task Planning

In this work we focus on the problem of embodied task planning, which requires an agent to accomplish a complex task by separating it into atomic actions.

arXiv: https://arxiv.org/abs/2610.25930
Code: https://github.com/woyut/TESS_EMNLP26

#worldmodels #robotics
```

</details>

---

### [GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations](https://arxiv.org/abs/2610.22708)

**Authors:** Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande

**Published:** 2026-10-15 | **Categories:** cs.AI, cs.CL | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22708) | [PDF](https://arxiv.org/pdf/2610.22708) | [Code](https://github.com/patronus-ai/globebench)

<details>
<summary>Abstract</summary>

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check whether models can predict the environment's response to a specific action given the full agent trajectory by understanding earlier state changes, following environment rules, and predic...

</details>

<details>
<summary>Share</summary>

```
GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases.

arXiv: https://arxiv.org/abs/2610.22708
Code: https://github.com/patronus-ai/globebench

#worldmodels #robotics
```

</details>

---

### [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088)

**Authors:** Chu Lin, Yi Sun

**Published:** 2026-10-21 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29088) | [PDF](https://arxiv.org/pdf/2610.29088)

<details>
<summary>Abstract</summary>

World models predict how embodied systems evolve under actions, but their accuracy can degrade when physical conditions move outside the training distribution. We study two components of causal modeling: which inputs a predictor may use, and how its mechanism computes their effects. In a synthetic benchmark with shortcut features, a frozen dependency mask derived from paired interventions reduces mean out-of-distribution (OOD) RMSE from 1.769 for a fully connected predictor to 0.697, close to the generator-oracle mask (0.694). For robot link-mass extrapolation in CausalWorld, with disjoint tra...

</details>

<details>
<summary>Share</summary>

```
Causal world models under physical parameter shifts

World models predict how embodied systems evolve under actions, but their accuracy can degrade when physical conditions move outside the training distribution.

arXiv: https://arxiv.org/abs/2610.29088

#worldmodels #robotics
```

</details>

---

### [Knowing When to Stop Thinking: A Dissection of Expected Free Energy as a Test-Time Compute Controller for Latent World-Model Planning](https://arxiv.org/abs/2610.28011)

**Authors:** Tong Zhang, Zhiyuan Shi, Yun Peng, Tao Xie

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28011) | [PDF](https://arxiv.org/pdf/2610.28011)

<details>
<summary>Abstract</summary>

A planner using a learned world model can improve its predicted outcome while choosing a worse action. We study when expected free energy (EFE) can help decide how much computation to spend on a plan. An EFE-inspired objective combines goal distance with disagreement among stochastic predictions. We test candidate scoring, stopping, and online predictor updates separately. Stopping when elite cost stalls reduces refinement on tasks whose success plateaus with depth, with mean success close to fixed-depth references. At the larger tested weights, rewarding disagreement lowers success with a fro...

</details>

<details>
<summary>Share</summary>

```
Knowing When to Stop Thinking: A Dissection of Expected Free Energy as a Test-Time Compute Controller for Latent World-Model Planning

A planner using a learned world model can improve its predicted outcome while choosing a worse action.

arXiv: https://arxiv.org/abs/2610.28011

#worldmodels #robotics
```

</details>

---

### [Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation](https://arxiv.org/abs/2610.25600)

**Authors:** Xuezhou Xu, Chung-Pang Wang, Zhenzhen Li, Benjamin Riviere

**Published:** 2026-10-19 (updated 2026-10-20) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.25600) | [PDF](https://arxiv.org/pdf/2610.25600)

<details>
<summary>Abstract</summary>

Visual world models have shown strong potential for robot planning, yet long-horizon manipulation remains challenging due to compounding prediction errors, large search complexity, and latent plans that the low-level controller cannot reliably reach. In this work, we introduce Vector-Quantized World Model (VQ-WM), a latent feedback motion planning framework that integrates discrete long-horizon search with continuous visual feedback control: a discrete latent predictor models transitions between vector-quantized latent states, allowing the planner to look far ahead and find a shortest path to...

</details>

<details>
<summary>Share</summary>

```
Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation

Visual world models have shown strong potential for robot planning, yet long-horizon manipulation remains challenging due to compounding prediction errors, large search complexity, and latent plans that the low-level...

arXiv: https://arxiv.org/abs/2610.25600

#worldmodels #robotics
```

</details>

---

### [Latent Projection for Latent Planning](https://arxiv.org/abs/2610.26979)

**Authors:** Yoo Sung Jang, Michael Ryoo

**Published:** 2026-10-19 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.26979) | [PDF](https://arxiv.org/pdf/2610.26979) | [Code](https://github.com/yjang43/lp2)

<details>
<summary>Abstract</summary>

Latent world models let an agent plan in latent space. The planner searches for an action sequence that minimizes a cost, and that cost is often the $\ell_2$ distance between the predicted terminal latent and the goal latent. The latent, however, is partly noise: the regularizer that prevents collapse during world model training promotes variance in the directions carrying no signal. We show that the same regularizer also supplies the structure to prune that noise in the latent. SIGReg drives the latent marginal to a standard Gaussian at every step, and assuming further that the latent sequenc...

</details>

<details>
<summary>Share</summary>

```
Latent Projection for Latent Planning

Latent world models let an agent plan in latent space.

arXiv: https://arxiv.org/abs/2610.26979
Code: https://github.com/yjang43/lp2

#worldmodels #robotics
```

</details>

---

### [BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL](https://arxiv.org/abs/2610.23127)

**Authors:** Liyun Yan, Haoyang Li, Yang Zhang, Jialing Zhu, Zhanxiang Cao et al. (14 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.23127) | [PDF](https://arxiv.org/pdf/2610.23127) | [Project Page](https://ylyem9x.github.io/BeJEPA-project)

<details>
<summary>Abstract</summary>

Humanoid control requires coordinating whole-body posture with position and heading in the world frame. Mainstream controllers imitate trajectories in the root frame, but struggle to regain the target world pose after displacement. We introduce BeJEPA, a goal-conditioned Behavior World Model learned through unsupervised reinforcement learning from human motion priors and robot interaction. BeJEPA learns a shared representation of body configuration and world placement through a joint-embedding predictive architecture (JEPA). A Dynamic Predictor predicts the next state embedding under an action...

</details>

<details>
<summary>Share</summary>

```
BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL

Humanoid control requires coordinating whole-body posture with position and heading in the world frame.

arXiv: https://arxiv.org/abs/2610.23127
Project page: https://ylyem9x.github.io/BeJEPA-project

#worldmodels #robotics
```

</details>

---

### [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363)

**Authors:** Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li et al. (14 authors)

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "action-conditioned video" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22363) | [PDF](https://arxiv.org/pdf/2610.22363) | [Project Page](https://p3-wam.pages.dev/)

<details>
<summary>Abstract</summary>

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D acti...

</details>

<details>
<summary>Share</summary>

```
Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perc...

arXiv: https://arxiv.org/abs/2610.22363
Project page: https://p3-wam.pages.dev/

#worldmodels #robotics
```

</details>

---

### [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129)

**Authors:** Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour, Patrick Pérez, David Picard

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.30129) | [PDF](https://arxiv.org/pdf/2610.30129)

<details>
<summary>Abstract</summary>

Video world models predict future frames from past frames and actions. They serve as simulators in which agents train, plan or are evaluated, and that humans can control interactively. They generate in the latent space of a video autoencoder, whose compression sets their cost per frame and how long each action waits to take effect. Yet world models often reuse the autoencoders of text-to-video generators, built for offline generation with no agent waiting and, without their training data and code, not retrainable at another compression. We therefore ask how, where and how much a world model sh...

</details>

<details>
<summary>Share</summary>

```
Rethinking Video Autoencoders for Interactive World Models

Video world models predict future frames from past frames and actions.

arXiv: https://arxiv.org/abs/2610.30129

#worldmodels #robotics
```

</details>

---

### [OccJEPA: Occlusion as Masking for Amodal Video Segmentation](https://arxiv.org/abs/2610.29061)

**Authors:** Genpei Zhang

**Published:** 2026-10-21 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.29061) | [PDF](https://arxiv.org/pdf/2610.29061) | [Code](https://github.com/zgp110/occjepa)

<details>
<summary>Abstract</summary>

Amodal video segmentation asks for the complete mask of an object in every frame, including the parts hidden behind other objects. The best current methods generate these masks with fine-tuned video diffusion models, which need many denoising steps and an extra depth network, and give a different answer for every sample. Self-supervised video world models of the JEPA family are trained on a closely related task: predicting the representation of masked space-time regions from the visible ones. We therefore treat occlusion as masking. The tokens that the object's visible mask does not cover are...

</details>

<details>
<summary>Share</summary>

```
OccJEPA: Occlusion as Masking for Amodal Video Segmentation

Amodal video segmentation asks for the complete mask of an object in every frame, including the parts hidden behind other objects.

arXiv: https://arxiv.org/abs/2610.29061
Code: https://github.com/zgp110/occjepa

#worldmodels #robotics
```

</details>

---

### [Second Thoughts: Exploring and Planning through Comparative Imagination in World Models](https://arxiv.org/abs/2610.28779)

**Authors:** Hieu Tran, Hong Yu

**Published:** 2026-10-20 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28779) | [PDF](https://arxiv.org/pdf/2610.28779)

<details>
<summary>Abstract</summary>

World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy. We introduce SDI (Sibling Disagreement in Imagination), which connects these decisions through a shared actor-based reference. SDI compares action sequences imagined from the same model state, using repeated rollouts of the actor's own sequence to measure variation under fixed behavior. This reference scales both the spread across candidate returns, which provides an exploration signal, and a proposed plan's pr...

</details>

<details>
<summary>Share</summary>

```
Second Thoughts: Exploring and Planning through Comparative Imagination in World Models

World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy.

arXiv: https://arxiv.org/abs/2610.28779

#worldmodels #robotics
```

</details>

---

### [Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models](https://arxiv.org/abs/2610.28074)

**Authors:** Peisong Wen, Qianqian Xu, Minye Lei, Siran Dai, Yang Liu et al. (6 authors)

**Published:** 2026-10-20 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28074) | [PDF](https://arxiv.org/pdf/2610.28074)

<details>
<summary>Abstract</summary>

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor to redundantly recover object structure that could otherwise be reused across tasks before modeling interactions. Second, the lack of explicit entity correspondence across time makes...

</details>

<details>
<summary>Share</summary>

```
Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations.

arXiv: https://arxiv.org/abs/2610.28074

#worldmodels #robotics
```

</details>

---

### [Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models](https://arxiv.org/abs/2610.27921)

**Authors:** Zhiyuan Liu, Sicheng Liu, Haiyu Wu

**Published:** 2026-10-20 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27921) | [PDF](https://arxiv.org/pdf/2610.27921)

<details>
<summary>Abstract</summary>

A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future representations using a conditional quantum Born prior. Circuit measurements generate binary latent actions, which a shared predictor maps to alternative future representations. We train the quantum prior through the quality and diversity of these predictions using a sampled energy objective. Our model learns distinct...

</details>

<details>
<summary>Share</summary>

```
Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models

A single observation can admit several plausible futures, making uncertainty an essential part of world modelling.

arXiv: https://arxiv.org/abs/2610.27921

#worldmodels #robotics
```

</details>

---

### [AnyGoal: On World Model Generalization Beyond Expert Rollouts](https://arxiv.org/abs/2610.26844)

**Authors:** Heejeong Nam, Divyat Mahajan, Quentin Le Lidec, Randall Balestriero, David Klindt

**Published:** 2026-10-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.26844) | [PDF](https://arxiv.org/pdf/2610.26844) | [Project Page](https://hazel-heejeong-nam.github.io/anygoal/)

<details>
<summary>Abstract</summary>

The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics generalization, and downstream planning performance remains underexplored. We study this relationship through the lens of compositional generalization: can a world model recombine familiar st...

</details>

<details>
<summary>Share</summary>

```
AnyGoal: On World Model Generalization Beyond Expert Rollouts

The goal of a world model is to capture the dynamics of an environment.

arXiv: https://arxiv.org/abs/2610.26844
Project page: https://hazel-heejeong-nam.github.io/anygoal/

#worldmodels #robotics
```

</details>

---

### [UniState: Unifying Memory and Intervention for Controllable World Simulation](https://arxiv.org/abs/2610.25414)

**Authors:** Jaeseok Jeong, Kyungmook Choi, Sohyun Chung, Youngsik Yun, Youngjung Uh

**Published:** 2026-10-18 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25414) | [PDF](https://arxiv.org/pdf/2610.25414) | [Project Page](https://curryjung.github.io/unistate/)

<details>
<summary>Abstract</summary>

World models offer increasingly rich environments for exploration, yet intervening in a world while observing the consequences from freely chosen viewpoints remains challenging. We tackle these challenges by introducing UniState, a framework for controllable world simulation built on a unified world-state representation. This representation unifies spatial memory and user interventions. Users specify object motion directly within spatial memory, while independently choosing the camera trajectory from which the resulting world state is observed. This unification makes the relationship between t...

</details>

<details>
<summary>Share</summary>

```
UniState: Unifying Memory and Intervention for Controllable World Simulation

World models offer increasingly rich environments for exploration, yet intervening in a world while observing the consequences from freely chosen viewpoints remains challenging.

arXiv: https://arxiv.org/abs/2610.25414
Project page: https://curryjung.github.io/unistate/

#worldmodels #robotics
```

</details>

---

### [World Models, Trees and Foundation Models for Retail Forecasting: Evidence from Four Public Data Sets](https://arxiv.org/abs/2610.25170)

**Authors:** Karthik Iyer, Madan Dabbeeru

**Published:** 2026-10-18 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25170) | [PDF](https://arxiv.org/pdf/2610.25170) | [Code](https://github.com/karthik-iyer-au/retail-world-models)

<details>
<summary>Abstract</summary>

A retailer makes different decisions at different grains of the product, store and time hierarchy: store orders for an item in a store, supplier funding for an item across stores, category performance by store, and the financial plan for the chain. Which forecasting model to use depends on the grain. This paper compares models at each grain on four public data sets (M5, six Dominick's categories, Breakfast at the Frat, and Corporación Favorita, the last kept out of all development), over rolling forecast origins with paired tests and model confidence sets. It covers price and promotion through...

</details>

<details>
<summary>Share</summary>

```
World Models, Trees and Foundation Models for Retail Forecasting: Evidence from Four Public Data Sets

A retailer makes different decisions at different grains of the product, store and time hierarchy: store orders for an item in a store, supplier funding for an item across stores, category performance by store, and th...

arXiv: https://arxiv.org/abs/2610.25170
Code: https://github.com/karthik-iyer-au/retail-world-models

#worldmodels #robotics
```

</details>

---

### [Beckmann World Models: Direct Terminal-Map Learning for One-Step Action-Conditioned Prediction](https://arxiv.org/abs/2610.26903)

**Authors:** Adam Lee, Shobhit Agarwal, June Pyo Suh

**Published:** 2026-10-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.26903) | [PDF](https://arxiv.org/pdf/2610.26903)

<details>
<summary>Abstract</summary>

Action-conditioned world models support planning and policy evaluation by predicting future states. However, learning an accurate one-step predictor can require substantial training computation. We introduce Beckmann World Models (BWM), which learn a direct map from noise, visual history, and actions to future frames without a pretrained generative teacher. We adapt the terminal-map conservation law of Beckmann Transport Models to action-conditioned video prediction, training directly from noise-data pairs without conditional populations of generated samples required by DriftWorld. However, tr...

</details>

<details>
<summary>Share</summary>

```
Beckmann World Models: Direct Terminal-Map Learning for One-Step Action-Conditioned Prediction

Action-conditioned world models support planning and policy evaluation by predicting future states.

arXiv: https://arxiv.org/abs/2610.26903

#worldmodels #robotics
```

</details>

---

### [Training Controllable World Models via Action Influence Maximization](https://arxiv.org/abs/2610.27387)

**Authors:** Samuel M. Bateman, Tenny Yin, Chongyi Zheng, Lei Huang, Brian Wang et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.27387) | [PDF](https://arxiv.org/pdf/2610.27387)

<details>
<summary>Abstract</summary>

Action-conditioned video generative models trained on successful, goal-directed demonstrations tend to ignore the commanded action, rendering a plausible expert-like future regardless of what is asked of them. We trace this failure to training data that lack sufficient action influence. We analyze this metric and prove that it upper bounds the action influence that any model trained on that data can express. Expert demonstrations, whose narrow action distributions let next states be predicted without attending to the action, set a low ceiling that no amount of model capacity alone can raise. R...

</details>

<details>
<summary>Share</summary>

```
Training Controllable World Models via Action Influence Maximization

Action-conditioned video generative models trained on successful, goal-directed demonstrations tend to ignore the commanded action, rendering a plausible expert-like future regardless of what is asked of them.

arXiv: https://arxiv.org/abs/2610.27387

#worldmodels #robotics
```

</details>

---

### [AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation](https://arxiv.org/abs/2610.23396)

**Authors:** Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yanwei Fu

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23396) | [PDF](https://arxiv.org/pdf/2610.23396)

<details>
<summary>Abstract</summary>

Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects. However, strong results in structured environments do not automatically transfer to open-world conditions, where clutter, occlusion, and changing viewpoints can obscure the spatial relationships required for action. To address this perceptual gap, a virtual active-perception paradigm is introduced. AWAM, an Active World-Action Model actively plans where to observe and imagines what will be seen along the planned trajectory before acting. Task-related v...

</details>

<details>
<summary>Share</summary>

```
AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation

Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects.

arXiv: https://arxiv.org/abs/2610.23396

#worldmodels #robotics
```

</details>

---

### [DriveWorld3D Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving](https://arxiv.org/abs/2610.22450)

**Authors:** Wei Wang, Yiru Veronika Wang, Yihan Wang, Zihao Li, Xiaohui Liang

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.22450) | [PDF](https://arxiv.org/pdf/2610.22450)

<details>
<summary>Abstract</summary>

Three dimensional modeling for autonomous driving must continuously estimate road geometry, obstacle occupancy, traffic participant behavior, and observational uncertainty under limited computational resources. Existing reconstruction methods can synthesize realistic novel views, but visual fidelity does not sufficiently characterize the geometric reliability required for driving. Generative world models can expand scenarios and predict future observations, yet may introduce content unsupported by measurements. We propose DriveWorld3D, a framework combining temporal video learning, measurement...

</details>

<details>
<summary>Share</summary>

```
DriveWorld3D Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving

Three dimensional modeling for autonomous driving must continuously estimate road geometry, obstacle occupancy, traffic participant behavior, and observational uncertainty under limited computational resources.

arXiv: https://arxiv.org/abs/2610.22450

#worldmodels #robotics
```

</details>

---

### [MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models](https://arxiv.org/abs/2610.21686)

**Authors:** Yi Qiao, Maolin Zheng, Haoran Sun, Lujia Dong, Wenzhao Lian

**Published:** 2026-10-15 (updated 2026-10-16) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.21686) | [PDF](https://arxiv.org/pdf/2610.21686)

<details>
<summary>Abstract</summary>

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action. Yet most monitoring methods are reactive, identifying anomalies only after they become observable. Anticipating such anomalies is challenging because visual observations only partially reveal physical interaction, while planned actions describe intended motion rather than their actual physical consequences. We address this problem with MAIA, a multimodal framework for anomaly anticipation. Its vision-action-force world model learns nominal interaction dynamics and predicts the visual...

</details>

<details>
<summary>Share</summary>

```
MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action.

arXiv: https://arxiv.org/abs/2610.21686

#worldmodels #robotics
```

</details>

---

### [Events, Not Pixels: Where World Models Get the Return Wrong](https://arxiv.org/abs/2610.29435)

**Authors:** Haoyue Liu, Xiaoying Tang

**Published:** 2026-10-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29435) | [PDF](https://arxiv.org/pdf/2610.29435)

<details>
<summary>Abstract</summary>

World models are increasingly used for planning, where a planner ranks candidate actions by returns imagined by the model. However, these models are judged mainly by how well they render frames, even though a visually faithful rollout can still assign the wrong return. To identify where this mismatch arises, we introduce a transition-level diagnostic that replaces imagined transitions with real ones and measures the reduction in return error against a budget-matched random control. Our analysis yields two findings. (1) Event transitions, the few steps where a reward is earned or an episode end...

</details>

<details>
<summary>Share</summary>

```
Events, Not Pixels: Where World Models Get the Return Wrong

World models are increasingly used for planning, where a planner ranks candidate actions by returns imagined by the model.

arXiv: https://arxiv.org/abs/2610.29435

#worldmodels #robotics
```

</details>

---

### [WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State](https://arxiv.org/abs/2610.28827)

**Authors:** Xiaoxiao Ma, Weiyang Jin, Yanwen Ma, Haoran Li, Zhixiang Wei et al. (14 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV, cs.GR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28827) | [PDF](https://arxiv.org/pdf/2610.28827)

<details>
<summary>Abstract</summary>

We present WorldStream, an open-ended 3D world model with three simultaneous capabilities: it extends playable terrain beyond any pre-specified map, acts on open-ended language in the running world, and restores visited places with their edits. A hierarchical planner over a typed decision model emits structured decision state: Macro fixes settlement, ecology, transport, and hydrological structure across a group of tiles; Micro specializes that contract into tile semantics under measured terrain and accepted neighbor commitments. Deterministic local code compiles accepted plans into terrain, ro...

</details>

<details>
<summary>Share</summary>

```
WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State

We present WorldStream, an open-ended 3D world model with three simultaneous capabilities: it extends playable terrain beyond any pre-specified map, acts on open-ended language in the running world, and restores visit...

arXiv: https://arxiv.org/abs/2610.28827

#worldmodels #robotics
```

</details>

---

### [Learning the 4D World through Point Trajectory Forecasting](https://arxiv.org/abs/2610.28594)

**Authors:** Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park et al. (13 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28594) | [PDF](https://arxiv.org/pdf/2610.28594)

<details>
<summary>Abstract</summary>

Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned multi-view processing that integrates complementary observations across cameras, and add a trajectory head that predicts how physical points move through time. Each trajectory trac...

</details>

<details>
<summary>Share</summary>

```
Learning the 4D World through Point Trajectory Forecasting

Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene.

arXiv: https://arxiv.org/abs/2610.28594

#worldmodels #robotics
```

</details>

---

### [OverSeer: Multi-Agent World Models Beyond What Agents See](https://arxiv.org/abs/2610.28554)

**Authors:** Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang et al. (9 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28554) | [PDF](https://arxiv.org/pdf/2610.28554)

<details>
<summary>Abstract</summary>

Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents. To address this gap, we introduce OverSeer, a multi-agent world model that augments egocentric agent views with auxiliary camera views. We suggest that, by fixing the auxiliary views in space, they act as a proxy for a world-centric representation: Unlike the agents' views, which can change entirely due to a simple change in agent position, changes in the auxiliary views directly map to loca...

</details>

<details>
<summary>Share</summary>

```
OverSeer: Multi-Agent World Models Beyond What Agents See

Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents.

arXiv: https://arxiv.org/abs/2610.28554

#worldmodels #robotics
```

</details>

---

### [MoDDiT: Simple Token Routing in Diffusion Transformers](https://arxiv.org/abs/2610.28086)

**Authors:** Jarek Liesen, Matthew T. Jackson, Benjamin Ellis, Shimon Whiteson, Jakob N. Foerster

**Published:** 2026-10-20 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28086) | [PDF](https://arxiv.org/pdf/2610.28086)

<details>
<summary>Abstract</summary>

Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves. Natural images are inherently sparse, as large portions of an image are often background, contribute little to the scene content, and are easy to denoise. DiTs fail to exploit this sparsity, as they process image tokens statically and uniformly. We propose MoDDiT, a simple architecture modification that learns to route tokens through both MLP and self-attention...

</details>

<details>
<summary>Share</summary>

```
MoDDiT: Simple Token Routing in Diffusion Transformers

Real-time video generation, interactive world models, and on-device image synthesis are almost a reality.

arXiv: https://arxiv.org/abs/2610.28086

#worldmodels #robotics
```

</details>

---

### [EndoWorld-JEPA: Motion-Guided Global-Local Latent World Modeling for Endoscopic Video Representation Learning](https://arxiv.org/abs/2610.27890)

**Authors:** Jie Wang, Shilong Yang, Tao Zhou, Juan Yu, Rong Qu et al. (8 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27890) | [PDF](https://arxiv.org/pdf/2610.27890)

<details>
<summary>Abstract</summary>

Endoscopic video contains state transitions induced by camera displacement, deformable tissue, and instrument interaction, yet existing pre-training methods treat dynamics implicitly. Inspired by action-conditioned joint-embedding predictive world models and by the observation that endoscopic optical flow contains both shared image-plane displacement and localized residual motion, we reformulate passive endoscopic video pre-training as causal motion-guided latent-state prediction. We present EndoWorld-JEPA, to our knowledge the first latent world-model pre-training framework designed for gener...

</details>

<details>
<summary>Share</summary>

```
EndoWorld-JEPA: Motion-Guided Global-Local Latent World Modeling for Endoscopic Video Representation Learning

Endoscopic video contains state transitions induced by camera displacement, deformable tissue, and instrument interaction, yet existing pre-training methods treat dynamics implicitly.

arXiv: https://arxiv.org/abs/2610.27890

#worldmodels #robotics
```

</details>

---

### [VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching](https://arxiv.org/abs/2610.27280)

**Authors:** Yunzhe Hu, Dong Xu

**Published:** 2026-10-19 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.27280) | [PDF](https://arxiv.org/pdf/2610.27280)

<details>
<summary>Abstract</summary>

Offline goal-conditioned reinforcement learning enables skill acquisition by reaching any goal from any state without dense rewards. Model-based methods allow for planning by scaling test-time compute to solve complex tasks. Combining both holds appealing promise for pre-training on suboptimal demonstrations and zero-shot adaptation via goal specification and planning. Yet existing methods assume effective planning requires accurate next-state prediction in pixel or latent space. In this work, we show that value prediction is more useful for planning, whereas accurate state prediction is often...

</details>

<details>
<summary>Share</summary>

```
VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching

Offline goal-conditioned reinforcement learning enables skill acquisition by reaching any goal from any state without dense rewards.

arXiv: https://arxiv.org/abs/2610.27280

#worldmodels #robotics
```

</details>

---

### [State World Models: Execute the Rules, Generate the Pixels](https://arxiv.org/abs/2610.26811)

**Authors:** Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, Xiaofeng Wang, Zheng Zhu et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.26811) | [PDF](https://arxiv.org/pdf/2610.26811)

<details>
<summary>Abstract</summary>

Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support stateful and rule-governed interaction. It maintains an evolving world state under specified rules, renders each resulting event with a frozen video model, and uses the generated cl...

</details>

<details>
<summary>Share</summary>

```
State World Models: Execute the Rules, Generate the Pixels

Existing world models can generate action-conditioned video from a single image.

arXiv: https://arxiv.org/abs/2610.26811

#worldmodels #robotics
```

</details>

---

### [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](https://arxiv.org/abs/2610.26711)

**Authors:** Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.26711) | [PDF](https://arxiv.org/pdf/2610.26711)

<details>
<summary>Abstract</summary>

Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured. Physical plausibility asks whether generated objects obey geometry, kinematics, dynamics, and conservation laws. Existing benchmarks rely on coarse visual-language model judgments or target embodied world models rather than video generation itself. We introduce PVBench, a physical video benchmark that quantitatively measures the plausibility of generated videos across 46 dimensions organized into seven domains, spanning: i) instruction and semantic fidelity, ii) behavior...

</details>

<details>
<summary>Share</summary>

```
PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements

Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured.

arXiv: https://arxiv.org/abs/2610.26711

#worldmodels #robotics
```

</details>

---

### [PrismWAM: Decoupling State Representations in World Action Models](https://arxiv.org/abs/2610.26564)

**Authors:** Tianyu Xin, Wanqi Zhong, Bowen Hu, Zhangchi Guo, Lijie Wang et al. (11 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.26564) | [PDF](https://arxiv.org/pdf/2610.26564) | [Project Page](https://prism-wam.github.io/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) typically represent the world through latent embeddings from pretrained video models, which entangle heterogeneous aspects of the world, from how it looks (e.g., texture and color) to how it is physically configured (e.g., occupancy and pose). This raises an underexplored question: $\textbf{what should constitute the state of a WAM?}$ We argue that the world state should separate how the world appears from how the world evolves under action: the former captures semantic context, while the latter is governed by physical state. To this end, we propose $\textbf{PrismWAM...

</details>

<details>
<summary>Share</summary>

```
PrismWAM: Decoupling State Representations in World Action Models

World Action Models (WAMs) typically represent the world through latent embeddings from pretrained video models, which entangle heterogeneous aspects of the world, from how it looks (e.g., texture and color) to how it...

arXiv: https://arxiv.org/abs/2610.26564
Project page: https://prism-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [Structured Latent Dynamics for Long-Horizon Embodied World Models](https://arxiv.org/abs/2610.24534)

**Authors:** Kevin Chen, Yu-Wei Zhan, Haoran Liang, Sen Cui, Changshui Zhang

**Published:** 2026-10-17 | **Categories:** cs.LG, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.24534) | [PDF](https://arxiv.org/pdf/2610.24534)

<details>
<summary>Abstract</summary>

Reliable long-horizon prediction remains a central challenge for embodied world models. Although recent generative models can synthesize visually plausible action-conditioned futures, their latent dynamics are typically learned through unconstrained transition modules, which may gradually deviate from coherent physical evolution as predictions are recursively rolled forward. We investigate whether explicitly structuring latent state evolution can improve the stability and utility of such imagined trajectories. To this end, we introduce HWM, a structured dynamics framework that represents backb...

</details>

<details>
<summary>Share</summary>

```
Structured Latent Dynamics for Long-Horizon Embodied World Models

Reliable long-horizon prediction remains a central challenge for embodied world models.

arXiv: https://arxiv.org/abs/2610.24534

#worldmodels #robotics
```

</details>

---

### [Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability](https://arxiv.org/abs/2610.23722)

**Authors:** Qingshi Wang, Huiqi Tong

**Published:** 2026-10-16 (updated 2026-10-19) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23722) | [PDF](https://arxiv.org/pdf/2610.23722)

<details>
<summary>Abstract</summary>

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This paper introduces the Mental World Model (MWM) and its implementation, the Multi-Branch Mental Evolutio...

</details>

<details>
<summary>Share</summary>

```
Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence.

arXiv: https://arxiv.org/abs/2610.23722

#worldmodels #robotics
```

</details>

---

### [Physical AI: Concepts, Techniques, and Challenges](https://arxiv.org/abs/2610.27045)

**Authors:** Weinan Zhang, Chunhua Shen, Tianfan Xue, Bin Zhao, Bingqi Jiang et al. (52 authors)

**Published:** 2026-10-19 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.27045) | [PDF](https://arxiv.org/pdf/2610.27045)

<details>
<summary>Abstract</summary>

In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscape, and examine each key technical subfield in depth. In doing so, it establishes a unified framework for Physical AI: artificial systems that perceive, model, and act upon the physical world through continuous feedback under real-world const...

</details>

<details>
<summary>Share</summary>

```
Physical AI: Concepts, Techniques, and Challenges

In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry.

arXiv: https://arxiv.org/abs/2610.27045

#worldmodels #robotics
```

</details>

---

### [Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing](https://arxiv.org/abs/2610.26757)

**Authors:** Adrian Remonda, Jiajun Xi, Nicklas Hansen, Marcus Greiff, Thomas Lew et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.LG, cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.26757) | [PDF](https://arxiv.org/pdf/2610.26757)

<details>
<summary>Abstract</summary>

Reinforcement learning enables learning high-performance control policies, but its reliance on extensive interaction limits deployment on physical systems where data collection is costly, and failures are unsafe. We introduce Prior-Informed Adaptation (PIA), an offline-to-online model-based RL framework that uses structured simulation priors for rapid adaptation. PIA pretrains a world model on heterogeneous low- and high-fidelity simulated trajectories, then adapts it with limited target-domain interaction using uncertainty-regularized planning. Rather than requiring an accurate simulator for...

</details>

<details>
<summary>Share</summary>

```
Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing

Reinforcement learning enables learning high-performance control policies, but its reliance on extensive interaction limits deployment on physical systems where data collection is costly, and failures are unsafe.

arXiv: https://arxiv.org/abs/2610.26757

#worldmodels #robotics
```

</details>

---

### [Latent World Models Should Plan with Distances Along the Latent Manifold](https://arxiv.org/abs/2610.25013)

**Authors:** Zunzhi You, Linwei Tao, Siyu Xu, Yunke Wang, Chang Xu

**Published:** 2026-10-18 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.25013) | [PDF](https://arxiv.org/pdf/2610.25013)

<details>
<summary>Abstract</summary>

Latent world models such as LeWM plan by searching for an action sequence whose predicted terminal latent is closest to the goal latent under an ambient norm, such as the Euclidean distance. Planning with such a cost assumes that proximity in the ambient latent space reflects proximity to the goal in the environment. Studying LeWM, we find that this assumption holds only in a small neighborhood around the goal, whereas farther away the L2 cost forms spurious low-cost basins that trap the planner. Yet neighborhood-based embeddings show that the latents retain the underlying physical state. We t...

</details>

<details>
<summary>Share</summary>

```
Latent World Models Should Plan with Distances Along the Latent Manifold

Latent world models such as LeWM plan by searching for an action sequence whose predicted terminal latent is closest to the goal latent under an ambient norm, such as the Euclidean distance.

arXiv: https://arxiv.org/abs/2610.25013

#worldmodels #robotics
```

</details>

---

### [Beyond Action Prediction: Learning Search-Free Planning in Latent Space](https://arxiv.org/abs/2610.23615)

**Authors:** Guanchen Du, Jinhao Du, Yanpeng Sun, Shan Zhang, Na Zhao et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23615) | [PDF](https://arxiv.org/pdf/2610.23615)

<details>
<summary>Abstract</summary>

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representations encode action-relevant information nor that predicted actions are consistent with the learned la...

</details>

<details>
<summary>Share</summary>

```
Beyond Action Prediction: Learning Search-Free Planning in Latent Space

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control.

arXiv: https://arxiv.org/abs/2610.23615

#worldmodels #robotics
```

</details>

---

### [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](https://arxiv.org/abs/2610.23156)

**Authors:** Yueyang Weng, Xiaopeng Zhang, Yuxi Ou, Yongjin Mu, Chengzhi Zhao et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.23156) | [PDF](https://arxiv.org/pdf/2610.23156)

<details>
<summary>Abstract</summary>

World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks. However, existing image-based and dense 3D world models do not explicitly impose object-level rigid motion, leaving rigid-object geometry preservation to be learned implicitly and making multi-step rollouts susceptible to shape drift or object-level motion inconsistency. To address this, we propose ORD-WM, a 3D world model that learns object-centric rigid dynamics for robotic manipulation. ORD-WM learns a vector-neuron variational autoencoder supervised by signed...

</details>

<details>
<summary>Share</summary>

```
ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation

World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks.

arXiv: https://arxiv.org/abs/2610.23156

#worldmodels #robotics
```

</details>

---

### [TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control](https://arxiv.org/abs/2610.21922)

**Authors:** Menghao Yin, Jiaju Yin, Xiyue Dong, Lixin Xu, Zhenhui Zhang et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21922) | [PDF](https://arxiv.org/pdf/2610.21922)

<details>
<summary>Abstract</summary>

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states. These limitations hinder learning from action-free videos and can encourage overfitting to demonstration conditions, weakening generalization and robustness. We present TS-WAM, a lightweight Teacher-Student World-Action Model that addresses these challenges through self-supervised temporal learning and explicit future prediction. Its vlm-jepa framework learns from heterogeneous data, including robot demonstrations and action-free human videos, usi...

</details>

<details>
<summary>Share</summary>

```
TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states.

arXiv: https://arxiv.org/abs/2610.21922

#worldmodels #robotics
```

</details>

---

### [T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](https://arxiv.org/abs/2610.22364)

**Authors:** Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang et al. (12 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22364) | [PDF](https://arxiv.org/pdf/2610.22364)

<details>
<summary>Abstract</summary>

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z for test-time optimization of environment latents, which augments a robotic world model with a learnable environment latent to condition world predictions. This compact latent captures underlying environmental variation without supervision of what environmental factors exist or what values they take...

</details>

<details>
<summary>Share</summary>

```
T2-z: Test-Time Optimization of Environment Latents for Robotic World Models

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties...

arXiv: https://arxiv.org/abs/2610.22364

#worldmodels #robotics
```

</details>

---

### [Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift](https://arxiv.org/abs/2610.22041)

**Authors:** Danqi Zhao, Keyu Chen, Wenchao Sun, Minglei Huang, Jianhe Zhang et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22041) | [PDF](https://arxiv.org/pdf/2610.22041)

<details>
<summary>Abstract</summary>

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training. At deployment, a different downstream controller may execute the same planned trajectory differently, creating a planning-execution gap between the frozen model's imagined future and actual execution. A natural remedy is to replace the planned trajectory with its predicted or observed execution. However, we find that better execution fidelity does not necessarily yield better decisions: directly substituting predicted execu...

</details>

<details>
<summary>Share</summary>

```
Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training.

arXiv: https://arxiv.org/abs/2610.22041

#worldmodels #robotics
```

</details>

---

### [LLM-Based Exogenous World Modeling for Dynamic Scheduling](https://arxiv.org/abs/2610.29308)

**Authors:** Ni Zhang, Haofeng Yuan, Jianan Zhou, Shiji Song, Zhiguang Cao

**Published:** 2026-10-21 | **Categories:** cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29308) | [PDF](https://arxiv.org/pdf/2610.29308)

<details>
<summary>Abstract</summary>

Dynamic scheduling requires dispatching online arrivals while anticipating future jobs, as poor decisions can compound downstream costs under nonlinear tardiness objectives. We show that a pretrained large language model (LLM) can serve as the exogenous component of a structured world model, forecasting uncertain future job arrivals. Specifically, we exploit an afterstate decomposition, which separates known deterministic shop transitions from uncertain exogenous job arrivals, enabling the LLM to forecast only the latter through a compact belief representation. Building on this, we develop Aft...

</details>

<details>
<summary>Share</summary>

```
LLM-Based Exogenous World Modeling for Dynamic Scheduling

Dynamic scheduling requires dispatching online arrivals while anticipating future jobs, as poor decisions can compound downstream costs under nonlinear tardiness objectives.

arXiv: https://arxiv.org/abs/2610.29308

#worldmodels #robotics
```

</details>

---

### [Learning Computational Structure for Sample-Efficient Prediction](https://arxiv.org/abs/2610.28555)

**Authors:** Hangyu Zhou, Constantine Dovrolis, Stephen Mussmann

**Published:** 2026-10-20 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28555) | [PDF](https://arxiv.org/pdf/2610.28555)

<details>
<summary>Abstract</summary>

Statistical learning in high dimensions suffers from the curse of dimensionality. Fortunately, many functions of practical interest are compositionally sparse, meaning they admit a composition of local functions, each depending on only a few variables, allowing sample complexity to depend on local arity rather than ambient dimension. Yet realizing this benefit requires exploiting hidden compositional structure, which theory does not establish for practical gradient-based training. We study this gap with CSFRBench, a controlled benchmark that hides the target's compositional computation during...

</details>

<details>
<summary>Share</summary>

```
Learning Computational Structure for Sample-Efficient Prediction

Statistical learning in high dimensions suffers from the curse of dimensionality.

arXiv: https://arxiv.org/abs/2610.28555

#worldmodels #robotics
```

</details>

---

### [Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models](https://arxiv.org/abs/2610.26179)

**Authors:** Xiang Kaibo, Liu Qingfeng

**Published:** 2026-10-19 (updated 2026-10-20) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.26179) | [PDF](https://arxiv.org/pdf/2610.26179)

<details>
<summary>Abstract</summary>

Hierarchical world models plan over long horizons by passing predicted states from a coarse model to a lower-level controller. Choosing these states can be expensive: the upper-level planner repeatedly differentiates through candidate macro-action trajectories. We replace this search with a lightweight goal-conditioned network trained through the frozen high-level predictor. The network supplies a conditioning vector, while the predictor generates the next latent waypoint. Training uses hindsight goals and state-prediction losses on offline trajectories, without search-solution targets or macr...

</details>

<details>
<summary>Share</summary>

```
Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models

Hierarchical world models plan over long horizons by passing predicted states from a coarse model to a lower-level controller.

arXiv: https://arxiv.org/abs/2610.26179

#worldmodels #robotics
```

</details>

---

### [ActTime: Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.25764)

**Authors:** Xinxing Zhou, Xiaojie Yuan, Yanlong Wen, Ming Jin

**Published:** 2026-10-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.25764) | [PDF](https://arxiv.org/pdf/2610.25764)

<details>
<summary>Abstract</summary>

Time-series models increasingly condition on known future inputs. In controlled systems, some of these inputs are actions that can be changed, compared, and optimized before execution. A model must therefore do more than predict the realized future: it must predict how outcomes change under different actions from the same observed history and support reliable comparison of candidate plans. We introduce ActTime, an action-conditioned world model for time series. Over the observed history, ActTime updates variable-specific latent states through an action-conditioned transition and corrects them...

</details>

<details>
<summary>Share</summary>

```
ActTime: Action-Conditioned World Modeling for Time Series

Time-series models increasingly condition on known future inputs.

arXiv: https://arxiv.org/abs/2610.25764

#worldmodels #robotics
```

</details>

---

### [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](https://arxiv.org/abs/2610.25666)

**Authors:** Yian Zhao, Yu Yan, Hongcan Guo, Ruochong Zheng, Jian Zhang et al. (6 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.25666) | [PDF](https://arxiv.org/pdf/2610.25666)

<details>
<summary>Abstract</summary>

Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a bottleneck: an external video model is agnostic to the actions, whereas the model's own pretrained network drifts in the same manner as the student. We observe that a long rollout n...

</details>

<details>
<summary>Share</summary>

```
Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips

Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions.

arXiv: https://arxiv.org/abs/2610.25666

#worldmodels #robotics
```

</details>

---

### [Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence](https://arxiv.org/abs/2610.25360)

**Authors:** One Octadion, Firmansyah Sundana, Novanto Yudistira

**Published:** 2026-10-18 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.25360) | [PDF](https://arxiv.org/pdf/2610.25360)

<details>
<summary>Abstract</summary>

World models are increasingly judged by how well they rank plausible futures, yet plausibility alone is the wrong target. The same scene can evolve under many latent rules, and a future that is smooth and physically valid under one rule can be incoherent under the rule actually in force. We formalize the resulting failure, operator-blindness, and show that it is systematically hidden by standard evaluation: a scorer can attain near-perfect generic ranking while separating current-world from other-world futures no better than chance. We introduce Operator-Mismatch Contrastive (OMC) learning, wh...

</details>

<details>
<summary>Share</summary>

```
Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence

World models are increasingly judged by how well they rank plausible futures, yet plausibility alone is the wrong target.

arXiv: https://arxiv.org/abs/2610.25360

#worldmodels #robotics
```

</details>

---

### [World Model Interpretability: From Decoding Representations to Understanding Latent Worlds](https://arxiv.org/abs/2610.25296)

**Authors:** Jize Wang, Yongcheng Jing, Xinyi Le, Cailian Chen, Xinping Guan et al. (6 authors)

**Published:** 2026-10-18 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.25296) | [PDF](https://arxiv.org/pdf/2610.25296)

<details>
<summary>Abstract</summary>

Emerging Joint-Embedding Predictive Architectures (JEPAs) are moving beyond representation learning towards latent world models that support prediction, planning, and control. Yet their latent worlds naturally lack a human-interpretable interface. In this Perspective, we argue that as JEPA latents become internal states for prediction and action, interpretability must move beyond what they encode to how latent variables interact, evolve, and causally drive prediction. To this end, we envision a four-stage research agenda, involving Ground, Structure, Verify, and Act, to guide this shift toward...

</details>

<details>
<summary>Share</summary>

```
World Model Interpretability: From Decoding Representations to Understanding Latent Worlds

Emerging Joint-Embedding Predictive Architectures (JEPAs) are moving beyond representation learning towards latent world models that support prediction, planning, and control.

arXiv: https://arxiv.org/abs/2610.25296

#worldmodels #robotics
```

</details>

---

### [Momentum: Persistent Dynamics for Video World Models](https://arxiv.org/abs/2610.23423)

**Authors:** Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel, Yilun Du, Xi Wang et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.23423) | [PDF](https://arxiv.org/pdf/2610.23423)

<details>
<summary>Abstract</summary>

Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears. Existing approaches rely on observation history, static point clouds, or image caches constructed from past frames. These representations are often expensive and, more importantly, cannot update dynamic scene content outside the field of view: generated vehicles and pedestrians may be forgotten after leaving the field of view or reappear in physically inaccurate states. We represent an evolving scene through synchronized videos from reference-camera...

</details>

<details>
<summary>Share</summary>

```
Momentum: Persistent Dynamics for Video World Models

Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears.

arXiv: https://arxiv.org/abs/2610.23423

#worldmodels #robotics
```

</details>

---

### [Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311)

**Authors:** Qiuhong Shen, Shizun Wang, Xinchao Wang

**Published:** 2026-10-15 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22311) | [PDF](https://arxiv.org/pdf/2610.22311)

<details>
<summary>Abstract</summary>

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using frustum slab correspondences from streaming geometry. Velox represents historical b...

</details>

<details>
<summary>Share</summary>

```
Velox: Spatial Memory Makes World Models Efficient

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation.

arXiv: https://arxiv.org/abs/2610.22311

#worldmodels #robotics
```

</details>

---

### [Learning Intrinsic Dynamics in Latent World Models](https://arxiv.org/abs/2610.21612)

**Authors:** Jiamin Shi, Yuanhong Zhang, Zhiyang Liu, Jiawei Sun, Jingwen Fu

**Published:** 2026-10-15 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.21612) | [PDF](https://arxiv.org/pdf/2610.21612)

<details>
<summary>Abstract</summary>

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models. However, visual variations unrelated to the underlying control process can obscure this relationship in learned representations. We investigate the connection between action predictability, defined as the ability to reconstruct an action from consecutive latent states, and the preservation of intrinsic dynamics. Our central hypothesis is that encouraging action predictability discourages representations from discarding the distinctions between different actions and their conse...

</details>

<details>
<summary>Share</summary>

```
Learning Intrinsic Dynamics in Latent World Models

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models.

arXiv: https://arxiv.org/abs/2610.21612

#worldmodels #robotics
```

</details>

---

### [Dexterity from Supervised Play](https://arxiv.org/abs/2610.22340)

**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma et al. (6 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22340) | [PDF](https://arxiv.org/pdf/2610.22340)

<details>
<summary>Abstract</summary>

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-...

</details>

<details>
<summary>Share</summary>

```
Dexterity from Supervised Play

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation?

arXiv: https://arxiv.org/abs/2610.22340

#worldmodels #robotics
```

</details>

---

### [From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion](https://arxiv.org/abs/2610.21374)

**Authors:** Bazeela Banday, Jishnu Keshavan

**Published:** 2026-10-15 (updated 2026-10-19) | **Categories:** cs.RO, eess.SY | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.21374) | [PDF](https://arxiv.org/pdf/2610.21374)

<details>
<summary>Abstract</summary>

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable. This letter introduces a visual safety-certification paradigm that uses scale-free, depth-normalized relative motion encoded by monocular optical flow as the representation for collision-risk certification, without reconstructing obstacle position, velocity, geometry, or a metric world model. Unlike conventional optical-flow-based navigation approaches that rely on image motion to shape avoidance behavior, the proposed framework directly encodes collision-cone geo...

</details>

<details>
<summary>Share</summary>

```
From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable.

arXiv: https://arxiv.org/abs/2610.21374

#worldmodels #robotics
```

</details>

---

### [Risk Decomposition for Hallucination-Aware Video Sampling](https://arxiv.org/abs/2610.26069)

**Authors:** Chenyan Zheng, Fan Wu, Ruibo Li, Jiaxing Li, Minghao Yang et al. (7 authors)

**Published:** 2026-10-19 (updated 2026-10-20) | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world simulator" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.26069) | [PDF](https://arxiv.org/pdf/2610.26069)

<details>
<summary>Abstract</summary>

Despite achieving high visual fidelity, video models still suffer from physical hallucinations, limiting their reliability as world simulators. Existing methods leverage model-internal or external signals to improve physical plausibility, but their roles and limitations require a unified explanation. We propose a two-dimensional physical-hallucination risk framework that defines low-density sampling risk and high-density drifting risk. The first risk captures generations assigned low likelihood by the video model, for example, a ball suddenly teleporting despite the model favoring continuous m...

</details>

<details>
<summary>Share</summary>

```
Risk Decomposition for Hallucination-Aware Video Sampling

Despite achieving high visual fidelity, video models still suffer from physical hallucinations, limiting their reliability as world simulators.

arXiv: https://arxiv.org/abs/2610.26069

#worldmodels #robotics
```

</details>

---

### [Axiomatic World Modeling for Physics Reasoning](https://arxiv.org/abs/2610.24519)

**Authors:** Xinye Yang, Zhenyang Liu, Yuxuan Wang, Yuanyuan Lei

**Published:** 2026-10-17 | **Categories:** cs.AI, cs.CL | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.24519) | [PDF](https://arxiv.org/pdf/2610.24519)

<details>
<summary>Abstract</summary>

Recent research-level physics-reasoning benchmarks for LLMs reveal a failure mode that lies not in knowledge or execution, but in modeling the world being reasoned about. Models often silently alter given quantities, fabricate laws, or inject unstated assumptions to force a problem into familiar patterns, and then reason inside this corrupted world. We define this premise-level divergence as modeling drift: the gap between a model's internal axiomatic world model (AWM) and the true physical world specified in the problem. Although RLVR and PRM have yielded substantial gains in mathematics and...

</details>

<details>
<summary>Share</summary>

```
Axiomatic World Modeling for Physics Reasoning

Recent research-level physics-reasoning benchmarks for LLMs reveal a failure mode that lies not in knowledge or execution, but in modeling the world being reasoned about.

arXiv: https://arxiv.org/abs/2610.24519

#worldmodels #robotics
```

</details>

---

### [World Action Critic (WAC) Model: Joint Foresight and Criticism for Policy Learning](https://arxiv.org/abs/2610.22825)

**Authors:** Xiangteng Zhang, Haoyuan Liu, Yang Guan, Jingliang Duan, Yao Lyu et al. (10 authors)

**Published:** 2026-10-16 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22825) | [PDF](https://arxiv.org/pdf/2610.22825)

<details>
<summary>Abstract</summary>

World models have shown considerable promise in sequential decision-making by anticipating the consequences of actions and providing predictive foresight for policy learning. However, learning to reason about counterfactual actions remains challenging, since predictive objectives may underemphasize information critical for action evaluation, while unexecuted actions lack observed futures for direct supervision. To address these challenges, we propose the World Action Critic (WAC) Model, which proposes multimodal action candidates and jointly learns candidate-conditioned future prediction and c...

</details>

<details>
<summary>Share</summary>

```
World Action Critic (WAC) Model: Joint Foresight and Criticism for Policy Learning

World models have shown considerable promise in sequential decision-making by anticipating the consequences of actions and providing predictive foresight for policy learning.

arXiv: https://arxiv.org/abs/2610.22825

#worldmodels #robotics
```

</details>

---

### [Is a Linear Probe Evidence of a Linear Representation?](https://arxiv.org/abs/2610.22655)

**Authors:** Nadir Kutluozen, Christian Internò, David Klindt

**Published:** 2026-10-15 | **Categories:** stat.ML, cs.CV, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.22655) | [PDF](https://arxiv.org/pdf/2610.22655)

<details>
<summary>Abstract</summary>

The linear representation hypothesis holds that pretrained vision models encode generative factors as linearly decodable directions in feature space, and comes with a standard methodology: train a linear probe, declare a factor represented if accuracy is high. We show this test is too permissive. Asymptotically, any sufficiently rich feature map, including a random one, admits a linear readout, so high probe accuracy is consistent with two very different geometries: a true linear world model, where the latent-aligned subspace dominates the representation, or a kernel machine, where the latents...

</details>

<details>
<summary>Share</summary>

```
Is a Linear Probe Evidence of a Linear Representation?

The linear representation hypothesis holds that pretrained vision models encode generative factors as linearly decodable directions in feature space, and comes with a standard methodology: train a linear probe, declar...

arXiv: https://arxiv.org/abs/2610.22655

#worldmodels #robotics
```

</details>

---
