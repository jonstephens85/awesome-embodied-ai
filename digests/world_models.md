# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-22 22:52 UTC

**Papers found:** 20

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343v1)

**Authors:** Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang et al. (11 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.19343v1) | [PDF](https://arxiv.org/pdf/2607.19343v1.pdf) | [Project Page](https://masked-visual-actions.github.io)

<details>
<summary>Abstract</summary>

Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrar...

</details>

---

### [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190v1)

**Authors:** Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma et al. (23 authors)

**Published:** 2026-07-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19190v1) | [PDF](https://arxiv.org/pdf/2607.19190v1.pdf) | [Project Page](https://ericchen321.github.io/agentic_real2sim.github.io/)

<details>
<summary>Abstract</summary>

Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across vi...

</details>

---

### [FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](https://arxiv.org/abs/2607.19038v1)

**Authors:** Jialong Zuo, Haotong Zuo, Shiwei Zhang, Xiang Wang, Chen Li et al. (8 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.19038v1) | [PDF](https://arxiv.org/pdf/2607.19038v1.pdf) | [Project Page](https://filmworld-ai.github.io)

<details>
<summary>Abstract</summary>

Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi-scene visual narratives. While current video generation models excel at short, single-scene clips within narrow temporal and spatial contexts, novel-to-film generation operates in a more complex regime, demanding long-duration content across diverse scenes with dynamically evolving entity states. To address this, we formalize novel-to...

</details>

---

### [Generative World Renderer at the Speed of Play](https://arxiv.org/abs/2607.18703v1)

**Authors:** Guixu Lin, Zheng-Hui Huang, Siqi Yang, Ming-Hsuan Yang, Kaipeng Zhang et al. (6 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.18703v1) | [PDF](https://arxiv.org/pdf/2607.18703v1.pdf) | [Project Page](https://alaya-renderer-flash.alayalab.ai/)

<details>
<summary>Abstract</summary>

Generative world renderer AlayaRenderer receives structured world states exported from physics engines and synthesizes RGB frames. Unlike models that generate frames from text/control-hints prompts, AlayaRenderer preserves scene structure without altering the underlying world dynamics. This demonstrates an alternative path toward interactive world modeling and user-controllable play. However, the original AlayaRenderer is too computationally expensive for real-time deployment. This technical rep...

</details>

---

## Other Recent Papers

### [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191v1)

**Authors:** Fan Jiang, Zhaoxu Sun, Mengchao Wang, Ziyu Zhu, Chiyu Wang et al. (41 authors)

**Published:** 2026-07-21 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.19191v1) | [PDF](https://arxiv.org/pdf/2607.19191v1.pdf)

<details>
<summary>Abstract</summary>

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a ...

</details>

---

### [NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework](https://arxiv.org/abs/2607.18887v1)

**Authors:** Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18887v1) | [PDF](https://arxiv.org/pdf/2607.18887v1.pdf)

<details>
<summary>Abstract</summary>

Vessel trajectory prediction in complex maritime environments is essential for traffic management, collision warning, route planning, and autonomous navigation. Although AIS-based learning methods have progressed rapidly, existing datasets are often released as raw message streams or irregular time series, with inconsistent sampling rates, noisy observations, heterogeneous coordinate systems, and non-unified scenario protocols. Most public AIS resources also lack structured representations of na...

</details>

---

### [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/abs/2607.18715v1)

**Authors:** Yi-Ge Zhang, Tianqi Du, Qi Zhang, Yisen Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18715v1) | [PDF](https://arxiv.org/pdf/2607.18715v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every source of state change. In real world, however, transitions arise from two heterogeneous sources: an action-driven component induced by the agent, and an action-invariant world effect -- the change that would still occur under a null action, dictated by the env...

</details>

---

### [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](https://arxiv.org/abs/2607.18709v1)

**Authors:** Ziqin Wang, Hao Li, Weijun Wang, Junhao Cai, Jia Zeng et al. (8 authors)

**Published:** 2026-07-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18709v1) | [PDF](https://arxiv.org/pdf/2607.18709v1.pdf)

<details>
<summary>Abstract</summary>

Existing robot datasets remain expensive to curate, embodiment-specific, and insufficiently annotated with the fine-grained structure required for generalizable reasoning, execution, or long-horizon environment dynamics simulation. Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling. RoboInter1.5 provides a unified resource of data, benchmarks, and models center...

</details>

---

### [Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development](https://arxiv.org/abs/2607.18696v1)

**Authors:** Yinan Wang

**Published:** 2026-07-21 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18696v1) | [PDF](https://arxiv.org/pdf/2607.18696v1.pdf)

<details>
<summary>Abstract</summary>

AI-native biotechnology companies are often designed by copying human biotech org charts into agent roles. We argue for a different abstraction: a Company World Model, defined as a persistent asset-to-value state representation with transition models, explicit value functions, planning, and updating across scientific, regulatory, BD, commercial, financial, and execution constraints. We introduce a dry-lab benchmark for testing whether AI-agent organizations should mimic departments or operate ar...

</details>

---

### [Planning as Emergent Behavior in Reinforcement Learning with Relational Hidden States](https://arxiv.org/abs/2607.18589v1)

**Authors:** Armin Sommer

**Published:** 2026-07-20 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18589v1) | [PDF](https://arxiv.org/pdf/2607.18589v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning is conventionally divided into model-based and model-free methods. In this taxonomy, model-based methods perform lookahead planning over a learned world model, whereas model-free methods learn a reactive state-action mapping. Recent work, however, has shown that planning can emerge from model-free reinforcement learning alone. The conditions under which this behavior emerges from a pure reward-maximization objective have so far remained unclear. In this paper, we present e...

</details>

---

### [Integrity-Gated Eco-CACC: Epistemic Admissibility for Cooperative Driving at Signalized Intersections](https://arxiv.org/abs/2607.18565v1)

**Authors:** Lyes Saad Saoud, Moussa Ayyash

**Published:** 2026-07-20 | **Categories:** eess.SY, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18565v1) | [PDF](https://arxiv.org/pdf/2607.18565v1.pdf)

<details>
<summary>Abstract</summary>

Eco-Cooperative Adaptive Cruise Control (Eco-CACC) systems rely on accurate localization, signal timing, and interaction awareness to optimize energy consumption at signalized intersections. Existing approaches typically assume that the internal world model used for optimization remains valid, making them vulnerable when sensing outages or semantic inconsistencies invalidate planning premises. This letter proposes an Integrity-Gated Eco-CACC framework that explicitly monitors the consistency bet...

</details>

---

### [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/abs/2607.18367v1)

**Authors:**  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge et al. (18 authors)

**Published:** 2026-07-20 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.18367v1) | [PDF](https://arxiv.org/pdf/2607.18367v1.pdf)

<details>
<summary>Abstract</summary>

Unlike conventional video game development, which relies on labor-intensive pipelines for asset production, animation, physics, and programming, video world models generate interactive environments from user inputs instantly. It enable us to create customized, explorable, and continuously evolving virtual world from text, an image, or video. Realizing this vision requires four tightly coupled capabilities: interaction, persistent spatiotemporal consistency, stable long-horizon generation, and ef...

</details>

---

### [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171v1)

**Authors:** Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra et al. (6 authors)

**Published:** 2026-07-20 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.18171v1) | [PDF](https://arxiv.org/pdf/2607.18171v1.pdf)

<details>
<summary>Abstract</summary>

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present Flas...

</details>

---

### [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/abs/2607.17973v1)

**Authors:** Letian Cheng, Qi Zhang, Yisen Wang

**Published:** 2026-07-20 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.17973v1) | [PDF](https://arxiv.org/pdf/2607.17973v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models have emerged as a powerful planning paradigm by learning action-conditioned predictive dynamics and using them as internal simulators to imagine and evaluate candidate action sequences. However, as the planning horizon grows, performance becomes increasingly constrained by proposal quality: a fixed candidate budget must search an exponentially larger action space, making it difficult to expose the world model to high-quality candidate futures for evaluation. In this paper, we...

</details>

---

### [Mobile Network Control with a World Model](https://arxiv.org/abs/2607.17747v1)

**Authors:** Maxime Bouton, Ioanna Mitsioni, Simon Lindståhl, Jaeseong Jeong

**Published:** 2026-07-20 | **Categories:** cs.NI, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.17747v1) | [PDF](https://arxiv.org/pdf/2607.17747v1.pdf)

<details>
<summary>Abstract</summary>

The increasing complexity of mobile networks necessitates intelligent and dynamic control strategies for efficient, energy-conserving management. We propose a world model-based approach for network control that enables adaptive configuration of crucial parameters. The world model is trained from historical data and predicts the impact of its actions on future network states. Our controller leverages the model's uncertainty estimate to robustly find optimal network configuration changes. Furtherm...

</details>

---

### [Planning with Transformers: Chain of Computation and Structured Context Windows](https://arxiv.org/abs/2607.17710v1)

**Authors:** Ehsan Futuhi, Nathan R. Sturtevant

**Published:** 2026-07-20 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.17710v1) | [PDF](https://arxiv.org/pdf/2607.17710v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have had a remarkable impact across many areas of machine learning. However, recent studies have shown that they struggle to reliably solve planning problems. At the same time, theoretical results have shown that transformers, the core architecture underlying modern LLMs, are Turing-complete. In this work, we investigate this apparent gap between the theoretical computational power of LLMs and their empirical planning performance. We propose Chain of Computation (COC...

</details>

---

### [Attention from Above: A Multimodal Model for Drone-Based Object Localization](https://arxiv.org/abs/2607.17669v1)

**Authors:** Hyun-Ki Jung

**Published:** 2026-07-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.17669v1) | [PDF](https://arxiv.org/pdf/2607.17669v1.pdf)

<details>
<summary>Abstract</summary>

Drone-based object detection technology has advanced rapidly, becoming increasingly sophisticated and efficient. Recently, research trends have expanded beyond the detection of predefined objects toward the identification of specified target objects. For example, desired targets can be specified through textual prompts, enabling accurate detection of objects of interest. To address this demand, this paper proposes an efficient multimodal-based object detection model aimed at improving small obje...

</details>

---

### [Reinforcement Learning: From Algorithms To Foundation Models](https://arxiv.org/abs/2607.17560v1)

**Authors:** Zihan Ding

**Published:** 2026-07-20 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.17560v1) | [PDF](https://arxiv.org/pdf/2607.17560v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) provides a framework for sequential decision making under explicit objectives. In its classical form, RL studies how an agent should act to maximise long-term reward in a dynamic environment. In richer settings, the problem extends beyond a single agent and fixed environment: intelligent behavior may require strategic interaction, adaptation to uncertainty, and reasoning over high-dimensional worlds. This thesis studies RL from two perspectives: algorithms in games an...

</details>

---

### [Thinking in Video: Can Video Generators Really Reason About the Real World?](https://arxiv.org/abs/2607.17523v1)

**Authors:** Yongheng Zhang, Guang Yang, Ruihan Hou, Qiguang Chen, Ziang Liu et al. (15 authors)

**Published:** 2026-07-20 | **Categories:** cs.CV, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.17523v1) | [PDF](https://arxiv.org/pdf/2607.17523v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in world models and video generation have given rise to an emerging reasoning paradigm that leverages video generative models to simulate, predict, and reason about real-world dynamics. We redefine this paradigm as Thinking in Video, where video is not merely an output artifact but a medium for constructing, extending, and verifying causal thought. However, this promise remains unverified: convincing rollouts may reflect memorized appearances rather than causal understanding, whi...

</details>

---

### [GeoWorldAD: Geometry World Action Model for Autonomous Driving](https://arxiv.org/abs/2607.17521v1)

**Authors:** Songyan Zhang, Jinyuan Tian, Hanbing Li, Daqi Liu, Hao Chen et al. (12 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.17521v1) | [PDF](https://arxiv.org/pdf/2607.17521v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving requires both safe and efficient planning decisions in dynamic 3D environments. Although recent Vision/Video-Action models learn policies directly from visual observations and scale well with advances in vision transformers and large-scale training data, they often lack explicit geometric grounding and future-aware spatial guidance, limiting their ability to balance collision avoidance and driving progress. In this work, we propose GeoWorldAD, a geometry world action model tha...

</details>

---
