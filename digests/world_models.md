# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-28 20:47 UTC

**Papers shown:** 50 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791)

**Authors:** Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang et al. (14 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; posted in last 2 days

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

### [GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091)

**Authors:** Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu et al. (6 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus; posted in last 2 days

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

### [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781)

**Authors:** Adam Lee, Mutian Xu, Yukang Cao, Shulin Tian, Ziwei Liu

**Published:** 2026-10-22 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.30781) | [PDF](https://arxiv.org/pdf/2610.30781) | [Project Page](https://dexplicit.github.io)

<details>
<summary>Abstract</summary>

Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typically entangle action-conditioned dynamics, camera motion, and visual synthesis within a video generation model, or represent dynamics as point trajectories without explicit object structure. We introduce DeXplicit, a dexterous manipulation world model that instead predicts how the world evolves explicitly in metric 3D before rendering its visual consequences. Given an initial scene and a future hand trajectory, a lightw...

</details>

<details>
<summary>Share</summary>

```
DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like.

arXiv: https://arxiv.org/abs/2610.30781
Project page: https://dexplicit.github.io

#worldmodels #robotics
```

</details>

---

### [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120)

**Authors:** Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei et al. (8 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo

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

### [Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663)

**Authors:** Mattia Scardecchia, Sherry Yang

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

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

### [Skeleton-Grounded Latent Action Model for Robot World Models](https://arxiv.org/abs/2610.31474)

**Authors:** Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng et al. (6 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31474) | [PDF](https://arxiv.org/pdf/2610.31474) | [Project Page](https://aopolin-lv.github.io/SkeLAM/)

<details>
<summary>Abstract</summary>

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for controllable robot world modeling. SkeLAM decomposes latent actions into a kinematic component grounded by robot skeleton supervision and a residual component retaining complementary vi...

</details>

<details>
<summary>Share</summary>

```
Skeleton-Grounded Latent Action Model for Robot World Models

Robot world models simulate how environments evolve in response to robot actions.

arXiv: https://arxiv.org/abs/2610.31474
Project page: https://aopolin-lv.github.io/SkeLAM/

#worldmodels #robotics
```

</details>

---

### [UniWorld: A Unified World Model for Real-Time Visual World Simulation](https://arxiv.org/abs/2610.32381)

**Authors:** Xin Zhang, Yabo Chen, Shuaiwei Wang, Zixuan Duan, Haibin Huang et al. (7 authors)

**Published:** 2026-10-23 (updated 2026-10-26) | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32381) | [PDF](https://arxiv.org/pdf/2610.32381) | [Project Page](https://zephipage.github.io/UniWorld)

<details>
<summary>Abstract</summary>

Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance. We present UniWorld, a unified framework that integrates depth trajectories and reference appearance within a shared video generation model. The central design maintains visual and geometric histories on a common timeline. Noise-aligned overlapping continuation places generated history at the prescribed sampling noise level and commits only newly generated latents. Rolling depth latent state preserves the corresponding geometric controls, incrementally reads newly available geome...

</details>

<details>
<summary>Share</summary>

```
UniWorld: A Unified World Model for Real-Time Visual World Simulation

Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance.

arXiv: https://arxiv.org/abs/2610.32381
Project page: https://zephipage.github.io/UniWorld

#worldmodels #robotics
```

</details>

---

### [SWIM: Learning What Matters from Behaviors for JEPA World Models](https://arxiv.org/abs/2610.36662)

**Authors:** Jiaming Hu, Shi Bo, Yan Zheng, Tian Wang, Florian Dubost et al. (14 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762)

**Authors:** Jiawei Chen, Yinxi Wang, Zihan Yang, Meijun Gao, Yaowei Liu et al. (15 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31762) | [PDF](https://arxiv.org/pdf/2610.31762) | [Project Page](https://wang-yinxi.github.io/representnav/)

<details>
<summary>Abstract</summary>

What visual representation should a navigation policy act on? Navigation policies built on vision foundation models largely leave representation design to the encoders' pretraining objectives. We present RepresentNav, a navigation foundation model built on a self-constructed representation space: a visual representation constructed by the policy's own objectives from vision foundation models. RepresentNav builds this space with Representation Residuals, a compact three-layer transformer that attends over features spanning the full depth of multiple complementary vision foundation models, so th...

</details>

<details>
<summary>Share</summary>

```
See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

What visual representation should a navigation policy act on?

arXiv: https://arxiv.org/abs/2610.31762
Project page: https://wang-yinxi.github.io/representnav/

#worldmodels #robotics
```

</details>

---

### [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](https://arxiv.org/abs/2610.30988)

**Authors:** Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen

**Published:** 2026-10-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.30988) | [PDF](https://arxiv.org/pdf/2610.30988)

<details>
<summary>Abstract</summary>

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization in manipulating a wide variety of garments in the real world. However, learned world models typically...

</details>

<details>
<summary>Share</summary>

```
In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations.

arXiv: https://arxiv.org/abs/2610.30988

#worldmodels #robotics
```

</details>

---

### [PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125)

**Authors:** Yunhao Luo, Wentao He, Yinpei Dai, Hyelin Nam, Hongze Fu et al. (8 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page

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

### [Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning](https://arxiv.org/abs/2610.37437)

**Authors:** Zengqi Zhao, Zun Wang, Shoubin Yu, Mohit Bansal, Yue Zhang

**Published:** 2026-10-27 | **Categories:** cs.CV, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

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

**Why surfaced:** "world model" in title; 2 distinct keyword hits; posted in last 2 days

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

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

### [UniAction: Unified Action Conditioning for World Models](https://arxiv.org/abs/2610.32977)

**Authors:** Bowen Xue, Zizhang Li, Hong-Xing Yu, Jiajun Wu

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32977) | [PDF](https://arxiv.org/pdf/2610.32977) | [Project Page](https://uniaction.github.io/)

<details>
<summary>Abstract</summary>

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity and a continuous spatiotemporal grounding coordinate. By mapping these coordinates directly into the pretrained video model's native positional space, UniAction allows heterogeneous actions to condit...

</details>

<details>
<summary>Share</summary>

```
UniAction: Unified Action Conditioning for World Models

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across...

arXiv: https://arxiv.org/abs/2610.32977
Project page: https://uniaction.github.io/

#worldmodels #robotics
```

</details>

---

### [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)

**Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu et al. (7 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

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

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

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

### [Rollback: Experience Backtracking in World Models for Policy Improvement](https://arxiv.org/abs/2610.36068)

**Authors:** Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao et al. (16 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in title; posted in last 2 days

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

### [Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection](https://arxiv.org/abs/2610.32742)

**Authors:** Luke Beddow, George Mavroghenis, Rodrigo Chacon Quesada, Kamil Dreczkowski, Cong Sun et al. (8 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.32742) | [PDF](https://arxiv.org/pdf/2610.32742)

<details>
<summary>Abstract</summary>

Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures. Current anomaly detection approaches often rely on direct access to the monitored system by utilizing onboard sensors, such as motor encoders, to detect anomalous states. However, legacy hardware often lacks these sensors, or strict security protocols may prohibit access altogether. We therefore present AWARE, a world model framework that is capable of anomaly detection using only external camera monitoring via system dynamics estimation and state prediction. Evaluated acro...

</details>

<details>
<summary>Share</summary>

```
Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection

Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures.

arXiv: https://arxiv.org/abs/2610.32742

#worldmodels #robotics
```

</details>

---

### [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](https://arxiv.org/abs/2610.31617)

**Authors:** Fanxing Li, Yuxiang Huang, Shengyang Wang, Fangyu Sun, Shuyu Wu et al. (10 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.31617) | [PDF](https://arxiv.org/pdf/2610.31617)

<details>
<summary>Abstract</summary>

Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control. World-model-based reinforcement learning provides a natural solution by learning latent dynamics for future imagination, yet it often entangles environmental evolution and the robot's own dynamics in a single learned rollout, where model bias can affect policy optimization efficiency. We propose DiffDreamer, a differentiable reinforcement learning framework that tightly couples a learned world model with differentiable simulation for actor optimization. In...

</details>

<details>
<summary>Share</summary>

```
DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control

Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control.

arXiv: https://arxiv.org/abs/2610.31617

#worldmodels #robotics
```

</details>

---

### [Inside-JEPA: From Prediction to Relational Grounding in Latent World Models](https://arxiv.org/abs/2610.31194)

**Authors:** Hossein Resani, Javen Qinfeng Shi

**Published:** 2026-10-22 | **Categories:** cs.LG, cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.31194) | [PDF](https://arxiv.org/pdf/2610.31194)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn world models in latent space, enabling efficient planning but leaving their states opaque. We introduce Inside-JEPA, which places relational channels for ordered entity pairs inside the JEPA latent state and shows that an inverse-dynamics loss can ground these channels without relation labels when its head reads them, either alone or as part of the full state. On Something-Something V2, latent prediction alone performs no better than a random relation head, while inverse-dynamics supervision that recovers actions from channel changes impro...

</details>

<details>
<summary>Share</summary>

```
Inside-JEPA: From Prediction to Relational Grounding in Latent World Models

Joint-embedding predictive architectures (JEPAs) learn world models in latent space, enabling efficient planning but leaving their states opaque.

arXiv: https://arxiv.org/abs/2610.31194

#worldmodels #robotics
```

</details>

---

### [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088)

**Authors:** Chu Lin, Yi Sun

**Published:** 2026-10-21 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

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

### [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588)

**Authors:** Rodrigo Gonzalez Laiz, Steffen Schneider

**Published:** 2026-10-27 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

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

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

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

**Published:** 2026-10-27 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; posted in last 2 days

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

### [World-in-Context: Interactive Video World Modeling with In-Context Conditioning](https://arxiv.org/abs/2610.33169)

**Authors:** Harold Haodong Chen, Rui Peng, Rongjin Guo, Lingteng Qiu, Kejie Qiu et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33169) | [PDF](https://arxiv.org/pdf/2610.33169) | [Project Page](https://haroldchen19.github.io/WiC-site/)

<details>
<summary>Abstract</summary>

Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion. Existing methods typically leave view modes implicit in text captions, conflate action with camera motion, and inject controls through fragmented architectural pathways that capture interdependencies only indirectly. In this work, we present World-in-Context, an interactive world modeling framework powered by In-Context Conditioning (ICC). Rather than relying on specialized conditioning pathways, World-in-Context unifies view, action, and camera controls into explicit tok...

</details>

<details>
<summary>Share</summary>

```
World-in-Context: Interactive Video World Modeling with In-Context Conditioning

Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion.

arXiv: https://arxiv.org/abs/2610.33169
Project page: https://haroldchen19.github.io/WiC-site/

#worldmodels #robotics
```

</details>

---

### [Reading, Writing, Sharing, and Interacting with the World through Video](https://arxiv.org/abs/2610.31668)

**Authors:** Shengqiong Wu, Meng Luo, Bobo Li, Ziwei Liu, Shuicheng Yan et al. (8 authors)

**Published:** 2026-10-22 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31668) | [PDF](https://arxiv.org/pdf/2610.31668) | [Project Page](https://vid-gen.github.io/video-world-model-survey)

<details>
<summary>Abstract</summary>

Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an observed video as a partial, lossy, and temporally ordered projection of a latent temporal world, we organize the literature around four complementary operations: reading infers world properties from...

</details>

<details>
<summary>Share</summary>

```
Reading, Writing, Sharing, and Interacting with the World through Video

Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict.

arXiv: https://arxiv.org/abs/2610.31668
Project page: https://vid-gen.github.io/video-world-model-survey

#worldmodels #robotics
```

</details>

---

### [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129)

**Authors:** Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour, Patrick Pérez, David Picard

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

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

**Why surfaced:** "world model" in abstract; code repo

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

### [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044)

**Authors:** Jingbo Xu, Hanchao Leng, JiaHui Huang, Hanbing Li, Jingwei Zhao et al. (10 authors)

**Published:** 2026-10-26 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

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

### [DT-JEPA: Learning to Predict Future Representations for Decision-Making](https://arxiv.org/abs/2610.32657)

**Authors:** Changxu Ni, Yiyang Ni, Jun Li, Feiran You, Hongyang Du et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.32657) | [PDF](https://arxiv.org/pdf/2610.32657)

<details>
<summary>Abstract</summary>

Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories. However, treating expected future returns as the condition provides an incomplete description of the future, as trajectories with different state transitions and behaviors may share similar returns. Moreover, expected future returns inherently depend on task-specific reward functions, which makes policy learning reliant on reward-labeled datasets and restricts its scalability to tasks with si...

</details>

<details>
<summary>Share</summary>

```
DT-JEPA: Learning to Predict Future Representations for Decision-Making

Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories.

arXiv: https://arxiv.org/abs/2610.32657

#worldmodels #robotics
```

</details>

---

### [$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model](https://arxiv.org/abs/2610.32177)

**Authors:** Khai Loong Aw, Klemen Kotar, Baihan Zhang, Yifan Liu, Lilian Chen et al. (8 authors)

**Published:** 2026-10-23 | **Categories:** cs.AI, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.32177) | [PDF](https://arxiv.org/pdf/2610.32177)

<details>
<summary>Abstract</summary>

Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds. Achieving this flexibility is a major open challenge in AI: capabilities often remain separated across specialized models, limiting how they can be composed and jointly adapted to a task. We introduce $Ψ$-0.6, a unified vision-language world model that adaptively composes perception, language, geometry, and simulation within a shared reasoning process we call streams of thought. These streams interleave images, text, and explicit representations of geometry and motion, all of which t...

</details>

<details>
<summary>Share</summary>

```
$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds.

arXiv: https://arxiv.org/abs/2610.32177

#worldmodels #robotics
```

</details>

---

### [Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://arxiv.org/abs/2610.31066)

**Authors:** Zhefan Rao, Meng Chu, Xuan Zhang, Jingfan Chen, Guohao Cai et al. (83 authors)

**Published:** 2026-10-22 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.31066) | [PDF](https://arxiv.org/pdf/2610.31066)

<details>
<summary>Abstract</summary>

World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests Agents under fixed environment response mechanisms and World Models under fixed action interventions across physical, digital, social, and scientific domains. The Agent track compares 10 configurations on 1,088 items in 15 reporting categories. The World Model track contains 400 cases across eight scenarios; 15 configu...

</details>

<details>
<summary>Share</summary>

```
Dual Exam: Controlled Evaluation of Multimodal Agents and World Models

World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement.

arXiv: https://arxiv.org/abs/2610.31066

#worldmodels #robotics
```

</details>

---

### [An Introduction to World Models for Generalist Agents](https://arxiv.org/abs/2610.30789)

**Authors:** Zhihui Zhu

**Published:** 2026-10-22 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.30789) | [PDF](https://arxiv.org/pdf/2610.30789)

<details>
<summary>Abstract</summary>

World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments. However, despite growing interest, the concept of a world model remains loosely defined, encompassing approaches ranging from predictive dynamics models and learned simulators to models that jointly generate future observations and actions. This introductory paper aims to clarify the concept of world models and provide a unified perspective on their role in developing generalist agents. Starting from the partially obser...

</details>

<details>
<summary>Share</summary>

```
An Introduction to World Models for Generalist Agents

World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments.

arXiv: https://arxiv.org/abs/2610.30789

#worldmodels #robotics
```

</details>

---

### [Anticipating Social Consequences with Distributional World Models](https://arxiv.org/abs/2610.30657)

**Authors:** Viet-Thanh Pham, Thuy-Trang Vu, Zhuang Li, Lizhen Qu, Gholamreza Haffari

**Published:** 2026-10-22 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.30657) | [PDF](https://arxiv.org/pdf/2610.30657)

<details>
<summary>Abstract</summary>

Social world models predict how interactions develop after an action, helping agents negotiate, cooperate and mediate. In these situations, one action can lead to several plausible futures, hence predicting only one future can overlook consequential alternatives, while exploring them through repeated simulations increases inference cost. We propose DSWM, a Distributional Social World Model that predicts alternative responses, their probabilities and immediate and final outcome values in one output per candidate action. We train a 4B model on repeated simulations using supervised fine-tuning an...

</details>

<details>
<summary>Share</summary>

```
Anticipating Social Consequences with Distributional World Models

Social world models predict how interactions develop after an action, helping agents negotiate, cooperate and mediate.

arXiv: https://arxiv.org/abs/2610.30657

#worldmodels #robotics
```

</details>

---

### [From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?](https://arxiv.org/abs/2610.30488)

**Authors:** Juntong Ni, Zewen Liu, Bohan Wang, Lige Zhang, Wei Jin

**Published:** 2026-10-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.30488) | [PDF](https://arxiv.org/pdf/2610.30488)

<details>
<summary>Abstract</summary>

World models help agents assess the consequences of their actions before acting. Many real systems, however, involve multiple actors who make their own decisions, can evolve even when the agent takes no action, and are only partially observed through event logs. We formalize these systems as event worlds and ask whether large language models can predict future observations from the log and the agent's proposed actions. We build complementary benchmarks from human Diplomacy games and real Polymarket trades. Our hierarchical framework compares prediction with and without other actors' actions, t...

</details>

<details>
<summary>Share</summary>

```
From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?

World models help agents assess the consequences of their actions before acting.

arXiv: https://arxiv.org/abs/2610.30488

#worldmodels #robotics
```

</details>

---

### [Events, Not Pixels: Where World Models Get the Return Wrong](https://arxiv.org/abs/2610.29435)

**Authors:** Haoyue Liu, Xiaoying Tang

**Published:** 2026-10-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

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

### [ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences](https://arxiv.org/abs/2610.32222)

**Authors:** Shibo Hong, Siyu Ren, FengJiao Chen, Zhongyuan Peng, Wei Shi et al. (6 authors)

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.32222) | [PDF](https://arxiv.org/pdf/2610.32222)

<details>
<summary>Abstract</summary>

Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matching optimization. Realizing this potential requires reward signals that reliably rank videos by both VQ and AF. However, existing rewards capture only one dimension: metric-based rewards assess VQ but require ground-truth videos and do not directly assess AF, while inverse dynamics model (IDM) rewards assess AF without references but do not guarantee VQ. Moreover, IDMs, typically tr...

</details>

<details>
<summary>Share</summary>

```
ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matchin...

arXiv: https://arxiv.org/abs/2610.32222

#worldmodels #robotics
```

</details>

---

### [Interpreting Physics in Video Encoders using Multi-Object Interaction Videos](https://arxiv.org/abs/2610.31983)

**Authors:** Ayushi Mehrotra, Sai Vidyaranya Nuthalapati

**Published:** 2026-10-22 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.31983) | [PDF](https://arxiv.org/pdf/2610.31983)

<details>
<summary>Abstract</summary>

Video encoder models are increasingly used as world models for physical AI, where a policy plans by rolling out the latent, so what physics the latent holds bounds what the agent can plan over. Moreover, existing interpretability work probes quantities belonging to a single object; the quantities that make physics relational, such as momentum transfer, restitution, and friction, are defined between bodies and have not been examined. We probe relational physics attributes in two frozen self-supervised video encoders (V-JEPA2 and VideoMAE) under two-body settings and test if they transfer across...

</details>

<details>
<summary>Share</summary>

```
Interpreting Physics in Video Encoders using Multi-Object Interaction Videos

Video encoder models are increasingly used as world models for physical AI, where a policy plans by rolling out the latent, so what physics the latent holds bounds what the agent can plan over.

arXiv: https://arxiv.org/abs/2610.31983

#worldmodels #robotics
```

</details>

---

### [LLM-Based Exogenous World Modeling for Dynamic Scheduling](https://arxiv.org/abs/2610.29308)

**Authors:** Ni Zhang, Haofeng Yuan, Jianan Zhou, Shiji Song, Zhiguang Cao

**Published:** 2026-10-21 | **Categories:** cs.AI, cs.CL | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

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
