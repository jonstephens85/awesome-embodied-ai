# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-31 19:44 UTC

**Papers shown:** 41 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](https://arxiv.org/abs/2610.33894)

**Authors:** Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta, Zilin Dai, Yuyuan Wu et al. (16 authors)

**Published:** 2026-10-24 (updated 2026-10-27) | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33894) | [PDF](https://arxiv.org/pdf/2610.33894) | [Code](https://github.com/hao-ai-lab/WMEval)

<details>
<summary>Abstract</summary>

Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on perceptual similarity rather than the physical-causal coherence essential for real-world utility. We introduce WMEval, a comprehensive benchmark that evaluates interactive world models against Unity-based physical simulations. By leveraging Unity as a high-fidelity ground-truth oracle, we shift evaluation beyond perceptual visual assessment toward the objective state-based verification required for downstream application...

</details>

<details>
<summary>Share</summary>

```
WMEval: Evaluating Interactive World Models Grounded on Physical Simulations

Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on perceptual similarity rather than the phy...

arXiv: https://arxiv.org/abs/2610.33894
Code: https://github.com/hao-ai-lab/WMEval

#worldmodels #robotics
```

</details>

---

### [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232)

**Authors:** Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li et al. (8 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

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

### [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791)

**Authors:** Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang et al. (14 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.36791) | [PDF](https://arxiv.org/pdf/2610.36791) | [Project Page](https://alibaba-damo-academy.github.io/RynnWorld-Latent.github.io) | [Code](https://github.com/alibaba-damo-academy/RynnWorld-Latent)

<details>
<summary>Abstract</summary>

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a common native action space. Built on a pretrained video transformer, RynnWorld-Latent combines glob...

</details>

<details>
<summary>Share</summary>

```
RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels.

arXiv: https://arxiv.org/abs/2610.36791
Project page: https://alibaba-damo-academy.github.io/RynnWorld-Latent.github.io
Code: https://github.com/alibaba-damo-academy/RynnWorld-Latent

#worldmodels #robotics
```

</details>

---

### [PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528)

**Authors:** Huabin Peng, Fagang Jin, Yancong Wei, Tengfei Ma, Chuhang Liu et al. (7 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091)

**Authors:** Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu et al. (6 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37091) | [PDF](https://arxiv.org/pdf/2610.37091) | [Code](https://github.com/gaoxiang12/ga-wm)

<details>
<summary>Abstract</summary>

World-action models (WAMs) incorporate the prediction of future observations into robot policy learning. However, most WAMs build on billion-parameter vision-language or video-generation backbones, which incur high training cost and inference latency. In this letter, we present GAWM (Geometry-Aware World Model), a compact multi-task WAM that predicts future observations in the latent space of a frozen DINOv3 encoder. GAWM compresses the features of each camera view into a small set of tokens. A lightweight predictor, conditioned on the task rather than on actions, forecasts these tokens at two...

</details>

<details>
<summary>Share</summary>

```
GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation

World-action models (WAMs) incorporate the prediction of future observations into robot policy learning.

arXiv: https://arxiv.org/abs/2610.37091
Code: https://github.com/gaoxiang12/ga-wm

#worldmodels #robotics
```

</details>

---

### [Fight World Model: Customizable Combat through Visual Interaction Proxies](https://arxiv.org/abs/2610.40607)

**Authors:** Jiahua Li, Zixu John, Tom Zhong, Fuping Wu, Tianhao Xu et al. (8 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Published:** 2026-10-29 | **Categories:** cs.AI, cs.LO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

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

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

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

### [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)

**Authors:** Yuhao Lu, Jiongxu Chen, Hexiang Wei, Jiajin Wu, Juelin Li et al. (12 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

### [Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663)

**Authors:** Mattia Scardecchia, Sherry Yang

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34663) | [PDF](https://arxiv.org/pdf/2610.34663) | [Code](https://github.com/mattia-scardecchia/predictable-latents)

<details>
<summary>Abstract</summary>

Video world models trained on large-scale robot data promise a safe and scalable approach for learning and evaluating policies that act in the physical world. However, they still struggle with long-horizon rollouts and out-of-distribution generalization, and they remain computationally demanding at inference time. Typically, video world models make predictions in the latent space of a reconstruction-trained autoencoder, which however is not directly optimized for dynamics modeling. On the other hand, world models designed for latent planning usually optimize latents to be predictable, but they...

</details>

<details>
<summary>Share</summary>

```
Video World Models Need Predictable Latents

Video world models trained on large-scale robot data promise a safe and scalable approach for learning and evaluating policies that act in the physical world.

arXiv: https://arxiv.org/abs/2610.34663
Code: https://github.com/mattia-scardecchia/predictable-latents

#worldmodels #robotics
```

</details>

---

### [Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339)

**Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

### [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564)

**Authors:** Meryem Koksal, Yunzhe Wang, Volkan Ustun

**Published:** 2026-10-25 | **Categories:** cs.CV, cs.MA | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.34564) | [PDF](https://arxiv.org/pdf/2610.34564)

<details>
<summary>Abstract</summary>

Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents. We introduce FlockWorld, an artificial-life environment built on Reynolds's Boids algorithm for studying population-scale multi-agent video world models. Specifically, FlockWorld renders synchronized egocentric crops, assigns distinct colors to preserve camera-agent identity across views, exposes rule-derived accelerations as actions, and lets the number of camera agents be configured independently of the size of the surrounding population....

</details>

<details>
<summary>Share</summary>

```
FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation

Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents.

arXiv: https://arxiv.org/abs/2610.34564

#worldmodels #robotics
```

</details>

---

### [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](https://arxiv.org/abs/2610.40401)

**Authors:** Liangyu Li, Qingwen Liu

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

### [When More Planning Hurts: Learned Planners for World Models](https://arxiv.org/abs/2610.37891)

**Authors:** Josef Chen

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.37891) | [PDF](https://arxiv.org/pdf/2610.37891)

<details>
<summary>Abstract</summary>

On PushT, our fixed action updater (1,505 parameters) solves 8 of 16 scenes reserved from our configuration selection. The comparison planners perform as follows: Selected Adam (7 tasks solved, total planning and encoding time 218.440s), adapted iCEM (2 tasks solved, total planning and encoding time 49.309s), released LePlanner (16 tasks solved, total planning and encoding time 5.652s). The total planning and encoding time for our action updater is 59.079s. Note that our action updater does not satisfy the task-cost criterion we fixed before evaluation. We also conduct another matched experime...

</details>

<details>
<summary>Share</summary>

```
When More Planning Hurts: Learned Planners for World Models

On PushT, our fixed action updater (1,505 parameters) solves 8 of 16 scenes reserved from our configuration selection.

arXiv: https://arxiv.org/abs/2610.37891

#worldmodels #robotics
```

</details>

---

### [SWIM: Learning What Matters from Behaviors for JEPA World Models](https://arxiv.org/abs/2610.36662)

**Authors:** Jiaming Hu, Shi Bo, Yan Zheng, Tian Wang, Florian Dubost et al. (14 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.36662) | [PDF](https://arxiv.org/pdf/2610.36662)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) enable world models to plan from images by predicting future embeddings. However, their visual prediction objectives do not explicitly incorporate task-relevant state information, so the physical state that determines task progress may not be reliably captured in the latent space. Supervising world models with simulator state can make planning more informative, but it requires deciding which state features matter. Features are typically selected by hand or weighted uniformly, and a uniform weighting gives every standardized state feature equal i...

</details>

<details>
<summary>Share</summary>

```
SWIM: Learning What Matters from Behaviors for JEPA World Models

Joint-embedding predictive architectures (JEPAs) enable world models to plan from images by predicting future embeddings.

arXiv: https://arxiv.org/abs/2610.36662

#worldmodels #robotics
```

</details>

---

### [Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation](https://arxiv.org/abs/2610.35636)

**Authors:** Akshay Mete, Dileep Kalathil, P. R. Kumar

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.35636) | [PDF](https://arxiv.org/pdf/2610.35636)

<details>
<summary>Abstract</summary>

Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift. Test-time adaptation (TTA) can mitigate this degradation by updating the model during deployment. Unlike pre-training on fixed data, TTA for planning is closed-loop: the planner uses model rollouts to select actions, and the resulting transitions drive the next update. This raises the question: which objective should guide TTA for planning? Under a prediction-only objective, the model is fit only to the outcomes of its own actions, so it can remain wro...

</details>

<details>
<summary>Share</summary>

```
Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation

Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift.

arXiv: https://arxiv.org/abs/2610.35636

#worldmodels #robotics
```

</details>

---

### [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](https://arxiv.org/abs/2610.33807)

**Authors:** Doanh Le Thien, Viet-Thanh Nguyen, Pham Tri Quang, Nhi Pham, Christopher Wewer et al. (21 authors)

**Published:** 2026-10-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.33807) | [PDF](https://arxiv.org/pdf/2610.33807)

<details>
<summary>Abstract</summary>

Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation. However, most benchmarks only evaluate them as open-world video generators, using Vision-Language Models (VLMs) that lack strict 3D spatial and kinematic reasoning. To bridge this gap, we introduce RoboWorM, a comprehensive, deployment-aware benchmark that leverages known hardware priors such as robot kinematic trees and fixed camera configurations, to systematically examine structural and spatiotemporal fidelity. RoboWorM curates 1,605 episodes across single-arm, bimanual, and humanoid morph...

</details>

<details>
<summary>Share</summary>

```
RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models

Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation.

arXiv: https://arxiv.org/abs/2610.33807

#worldmodels #robotics
```

</details>

---

### [Generating Critic-Guided Synthetic Experience in Latent World Models](https://arxiv.org/abs/2610.39100)

**Authors:** Jorge de Freitas, Christos Ziakas, Alessandra Russo

**Published:** 2026-10-29 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

### [Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning](https://arxiv.org/abs/2610.37437)

**Authors:** Zengqi Zhao, Zun Wang, Shoubin Yu, Mohit Bansal, Yue Zhang

**Published:** 2026-10-27 | **Categories:** cs.CV, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37437) | [PDF](https://arxiv.org/pdf/2610.37437) | [Project Page](https://imagirep.github.io/)

<details>
<summary>Abstract</summary>

Visual world models increasingly support spatial reasoning by generating RGB views of unobserved states. However, RGB has become the default interface largely because it is well suited for visual generation, rather than necessarily being the most effective representation for downstream reasoning. Different spatial questions may benefit from different representations of the same imagined state: top-down geometry can facilitate global distance comparisons, while panoramic views provide broader context for reasoning about open space. To isolate the role of representation in spatial imagination, w...

</details>

<details>
<summary>Share</summary>

```
Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning

Visual world models increasingly support spatial reasoning by generating RGB views of unobserved states.

arXiv: https://arxiv.org/abs/2610.37437
Project page: https://imagirep.github.io/

#worldmodels #robotics
```

</details>

---

### [BoxWorld: Let World Engines Control and Video Generators Render](https://arxiv.org/abs/2610.36371)

**Authors:** Zike Wu, Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin et al. (7 authors)

**Published:** 2026-10-26 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.36371) | [PDF](https://arxiv.org/pdf/2610.36371) | [Project Page](https://boxworld-web.github.io)

<details>
<summary>Abstract</summary>

We tackle the challenge of building real-time interactive video worlds with user-defined behaviors. Such worlds must track object states, apply interaction rules, and render the resulting consequences as users act. Yet existing end-to-end video world models typically learn interaction dynamics within the generator, making it difficult to specify object-level rules and reason about their consequences. In this work, we introduce BoxWorld, which separates interaction reasoning from generative rendering. Given user-specified rules, a coding agent creates a Box World Engine that determines interact...

</details>

<details>
<summary>Share</summary>

```
BoxWorld: Let World Engines Control and Video Generators Render

We tackle the challenge of building real-time interactive video worlds with user-defined behaviors.

arXiv: https://arxiv.org/abs/2610.36371
Project page: https://boxworld-web.github.io

#worldmodels #robotics
```

</details>

---

### [WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU](https://arxiv.org/abs/2610.35529)

**Authors:** Bingnan Liu, Ruini Xue

**Published:** 2026-10-26 | **Categories:** cs.DC, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.35529) | [PDF](https://arxiv.org/pdf/2610.35529)

<details>
<summary>Abstract</summary>

Interactive world models keep the KV of past chunks as retrieval memory so that revisited places stay consistent. On a single consumer machine (one RTX 4090, 32 GiB of host memory, one NVMe SSD), long sessions with such memory hit two walls. The first is capacity: the KV of Matrix-Game 2.0 exhausts host memory after 45 seconds of video in bf16 and after 2.8 minutes in int4. The second is the model's positional horizon of 4.3 minutes. We show that this memory is capacity-bound rather than bandwidth-bound and that its access set is known before compute, because the camera pose is an input. An an...

</details>

<details>
<summary>Share</summary>

```
WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU

Interactive world models keep the KV of past chunks as retrieval memory so that revisited places stay consistent.

arXiv: https://arxiv.org/abs/2610.35529

#worldmodels #robotics
```

</details>

---

### [TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting](https://arxiv.org/abs/2610.34797)

**Authors:** Hang Ni, Weijia Zhang, Hao Liu

**Published:** 2026-10-26 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.34797) | [PDF](https://arxiv.org/pdf/2610.34797)

<details>
<summary>Abstract</summary>

Time series forecasting supports decision-making in web applications such as online retail and network management, where planned actions can reshape future dynamics. World models provide a natural paradigm for predicting such action-dependent changes beyond extrapolating historical patterns. However, existing time series world models (TSWMs) typically rely on fixed, domain-specific covariate schemas that limit flexible intervention specification, while multimodal forecasters treat text primarily as passive predictive context. To investigate these gaps, we introduce TSWM-Bench, a cross-domain b...

</details>

<details>
<summary>Share</summary>

```
TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting

Time series forecasting supports decision-making in web applications such as online retail and network management, where planned actions can reshape future dynamics.

arXiv: https://arxiv.org/abs/2610.34797

#worldmodels #robotics
```

</details>

---

### [How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3](https://arxiv.org/abs/2610.34523)

**Authors:** Shuzhi Liu, Archana Warrier, Dat Nguyen, Chengqi Zheng, Kevin Ellis et al. (6 authors)

**Published:** 2026-10-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34523) | [PDF](https://arxiv.org/pdf/2610.34523) | [Project Page](https://arc3-human-think-aloud.github.io/](https://arc3-human-think-aloud.github.io/)

<details>
<summary>Abstract</summary>

Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence. Understanding these capabilities requires tracing how learners build, use, and revise world models during interaction. We construct the first dataset that records how humans discover and use the mechanisms of novel environments, using ARC-AGI-3 as a testbed: 144 trajectories from 64 participants across 25 public games, each pairing time-synchronized actions with think-aloud audio, plus 250 trajectories from large language model (LLM) agents with and without harness...

</details>

<details>
<summary>Share</summary>

```
How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3

Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence.

arXiv: https://arxiv.org/abs/2610.34523
Project page: https://arc3-human-think-aloud.github.io/](https://arc3-human-think-aloud.github.io/

#worldmodels #robotics
```

</details>

---

### [TurboWAM: Learning What Matters for Fast World Action Models](https://arxiv.org/abs/2610.33941)

**Authors:** Guile Wu, Shuangzhi Li, Xingxin Chen, Chengjie Huang, Sam Hosseini et al. (8 authors)

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33941) | [PDF](https://arxiv.org/pdf/2610.33941) | [Project Page](https://turbowam.github.io/)

<details>
<summary>Abstract</summary>

World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment. Recent approaches have sought to improve inference efficiency by reducing test-time future-frame imagination or accelerating action prediction. However, these methods often leverage representations from all video world model layers without explicitly considering their varying relevance to action prediction, leading to redundant computation and suboptimal representation utilization. In this work, we propose TurboWAM, a fa...

</details>

<details>
<summary>Share</summary>

```
TurboWAM: Learning What Matters for Fast World Action Models

World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment.

arXiv: https://arxiv.org/abs/2610.33941
Project page: https://turbowam.github.io/

#worldmodels #robotics
```

</details>

---

### [Distilling Dense Trajectory Teachers For Large-Motion Video World Models](https://arxiv.org/abs/2610.33566)

**Authors:** Shuofeng Sun, Linqing Zhao, Haibin Yan

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.33566) | [PDF](https://arxiv.org/pdf/2610.33566)

<details>
<summary>Abstract</summary>

Video world models are expected to generate videos that accurately follow specified camera trajectories while maintaining consistent 3D structures. However, existing models are predominantly trained on densely sampled videos with small inter-frame camera motions. When applied to sparse, large step trajectories, they often produce frozen frames, inaccurate camera motion, and severe geometric drift. We attribute this degradation to a mismatch between the gradual viewpoint transitions seen during training and the large viewpoint changes required at inference time. To address this problem, we prop...

</details>

<details>
<summary>Share</summary>

```
Distilling Dense Trajectory Teachers For Large-Motion Video World Models

Video world models are expected to generate videos that accurately follow specified camera trajectories while maintaining consistent 3D structures.

arXiv: https://arxiv.org/abs/2610.33566

#worldmodels #robotics
```

</details>

---

### [Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection](https://arxiv.org/abs/2610.39076)

**Authors:** Li Guan, Rachael Granberry, Sahar Aseeri, Sahar Rostami, Taylor Niehues et al. (104 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI, cs.AR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [Rollback: Experience Backtracking in World Models for Policy Improvement](https://arxiv.org/abs/2610.36068)

**Authors:** Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao et al. (16 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.36068) | [PDF](https://arxiv.org/pdf/2610.36068)

<details>
<summary>Abstract</summary>

Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies. However, existing world-model-based methods largely treat world models as forward-only surrogates of the physical environment, leaving untapped a capability no physical environment affords: rewinding to past decision points to explore counterfactual futures. We introduce Rollback, a policy improvement paradigm that turns world models from passive simulators into counterfactual engines: it rolls back to critical decision points, branches into alternative actions, and contr...

</details>

<details>
<summary>Share</summary>

```
Rollback: Experience Backtracking in World Models for Policy Improvement

Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies.

arXiv: https://arxiv.org/abs/2610.36068

#worldmodels #robotics
```

</details>

---

### [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](https://arxiv.org/abs/2610.34650)

**Authors:** Jonathan DeCastro, Thomas Balch, Emily Sumner, Deepak Gopinath, Laporsha Dees et al. (12 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.HC, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.34650) | [PDF](https://arxiv.org/pdf/2610.34650)

<details>
<summary>Abstract</summary>

Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time. We present Dream2Assist, a model-based reinforcement learning framework for tightly-coupled shared decision making that addresses both sides of this challenge. Our approach extends a recurrent state-space world model with intent inference, enabling an assistive policy trained via fictitious co-play to anticipate and support discrete human objectives without overriding human agency...

</details>

<details>
<summary>Share</summary>

```
Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control

Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time.

arXiv: https://arxiv.org/abs/2610.34650

#worldmodels #robotics
```

</details>

---

### [WorldFailBench: Do World Models Understand Policy Failures?](https://arxiv.org/abs/2610.33565)

**Authors:** Zheng Zhang, Xiaoyang Tang, Shuaiqi Cheng, Jiakai Huang, Zhongbo Wu et al. (14 authors)

**Published:** 2026-10-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.33565) | [PDF](https://arxiv.org/pdf/2610.33565)

<details>
<summary>Abstract</summary>

Robot policy evaluation informs deployment decisions and policy improvement, but physical testing and simulator preparation require substantial effort. World models offer a complementary route through closed-loop interaction in generated environments. Recent benchmarks have demonstrated their potential as policy evaluators through outcome-based evaluation (i.e., assessing task success or failure). However, such evaluation does not establish whether world models faithfully simulate how policies fail. Misrepresenting failures can lead to incorrect diagnoses of policy weaknesses and make policies...

</details>

<details>
<summary>Share</summary>

```
WorldFailBench: Do World Models Understand Policy Failures?

Robot policy evaluation informs deployment decisions and policy improvement, but physical testing and simulator preparation require substantial effort.

arXiv: https://arxiv.org/abs/2610.33565

#worldmodels #robotics
```

</details>

---

### [Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion](https://arxiv.org/abs/2610.39516)

**Authors:** Christoph B Rist, Larissa T Triess, Markus Enzweiler, Dariu M Gavrila

**Published:** 2026-10-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [Self-Supervised Latent Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.37963)

**Authors:** Chia-Han Kuo, Chengshuai Zhao, Huan Liu, Lo Pang-Yun Ting

**Published:** 2026-10-27 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.37963) | [PDF](https://arxiv.org/pdf/2610.37963)

<details>
<summary>Abstract</summary>

Time-series data play an important role in various tasks, such as weather forecasting, web traffic analysis, and speech recognition. Recently, pioneering studies have increasingly adopted Joint-Embedding Predictive Architecture (JEPA) based encoders to learn time-series representations through latent-space prediction. However, they often overlook the underlying factors governing transitions between time-series observations. In this work, we hypothesize that explicitly modeling the information behind changes in time series can facilitate time-series modeling. Building on this hypothesis, we pro...

</details>

<details>
<summary>Share</summary>

```
Self-Supervised Latent Action-Conditioned World Modeling for Time Series

Time-series data play an important role in various tasks, such as weather forecasting, web traffic analysis, and speech recognition.

arXiv: https://arxiv.org/abs/2610.37963

#worldmodels #robotics
```

</details>

---

### [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588)

**Authors:** Rodrigo Gonzalez Laiz, Steffen Schneider

**Published:** 2026-10-27 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.37588) | [PDF](https://arxiv.org/pdf/2610.37588)

<details>
<summary>Abstract</summary>

World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics that reflect the underlying structure of the environment. Here we introduce the concept of faithful latent world models as an equivariance condition between the environment's transition map and the learned latent dynamics. We propose latent rollout consistency (LRC) as a metric to evaluate action-conditioned latent pr...

</details>

<details>
<summary>Share</summary>

```
Understanding the limits of latent world models

World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons.

arXiv: https://arxiv.org/abs/2610.37588

#worldmodels #robotics
```

</details>

---

### [JEPA-Inspired Latent Field Prediction for Sparse-Pilot MIMO-OFDM Channel Reconstruction](https://arxiv.org/abs/2610.37391)

**Authors:** Yuzhi Yang, Brahim Mefgouda, Hang Zou, Lina Bariah, Anis Bara et al. (8 authors)

**Published:** 2026-10-27 | **Categories:** eess.SP, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.37391) | [PDF](https://arxiv.org/pdf/2610.37391)

<details>
<summary>Abstract</summary>

Accurate acquisition of full channel state information (CSI) is essential for multiple-input multiple-output orthogonal frequency-division multiplexing (MIMO-OFDM) wireless systems, while dense pilot-based estimation incurs substantial overhead. Directly minimizing the prediction error over raw CSI coefficients is fragile in realistic propagation environments, since small-scale fading, mobility, local scattering, and small spatial perturbations can induce large phase-sensitive variations. Nevertheless, wireless channels contain strong spatial, temporal, and frequency-domain correlations that c...

</details>

<details>
<summary>Share</summary>

```
JEPA-Inspired Latent Field Prediction for Sparse-Pilot MIMO-OFDM Channel Reconstruction

Accurate acquisition of full channel state information (CSI) is essential for multiple-input multiple-output orthogonal frequency-division multiplexing (MIMO-OFDM) wireless systems, while dense pilot-based estimation...

arXiv: https://arxiv.org/abs/2610.37391

#worldmodels #robotics
```

</details>

---

### [GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling](https://arxiv.org/abs/2610.37257)

**Authors:** Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu et al. (10 authors)

**Published:** 2026-10-27 (updated 2026-10-29) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.37257) | [PDF](https://arxiv.org/pdf/2610.37257)

<details>
<summary>Abstract</summary>

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that describe whole clips in coarse and undifferentiated text, which is insufficient for controllable long-horizon generation. We address this with GameVerse, a minute-scale gameplay video data...

</details>

<details>
<summary>Share</summary>

```
GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs.

arXiv: https://arxiv.org/abs/2610.37257

#worldmodels #robotics
```

</details>

---

### [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044)

**Authors:** Jingbo Xu, Hanchao Leng, JiaHui Huang, Hanbing Li, Jingwei Zhao et al. (10 authors)

**Published:** 2026-10-26 | **Categories:** cs.CV, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.35044) | [PDF](https://arxiv.org/pdf/2610.35044)

<details>
<summary>Abstract</summary>

World models are emerging as a fundamental component of policy learning for real-world agents, enabling agents to predict future world states and plan actions within a learned representation of the dynamic environment. Existing approaches, however, often model appearance, metric geometry represented by projected LiDAR depth, and ego motion either partially or independently, overlooking the fact that these modalities are different projections of a shared underlying world state. This separation can lead to information loss and cross-modal inconsistency, ultimately limiting downstream performance...

</details>

<details>
<summary>Share</summary>

```
DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models

World models are emerging as a fundamental component of policy learning for real-world agents, enabling agents to predict future world states and plan actions within a learned representation of the dynamic environment.

arXiv: https://arxiv.org/abs/2610.35044

#worldmodels #robotics
```

</details>

---
