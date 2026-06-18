# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-18 18:25 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Physics-IQ Verified](https://arxiv.org/abs/2606.18943v1)

**Authors:** Tim Rädsch, Yuki M Asano, Hilde Kuehne, Stefan Bauer, Priyank Jaini et al. (7 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18943v1) | [PDF](https://arxiv.org/pdf/2606.18943v1.pdf) | [GitHub](https://github.com/google-deepmind/physics-iq-benchmark)

<details>
<summary>Abstract</summary>

Video generative models ( VGMs) have become a new frontier that can be used not just for video generation but for a multitude of downstream tasks, including world modeling. To advance these tasks, a good video model must understand the physical reality of the world. Evaluating this understanding is an emerging field and has led to the Physics-IQ benchmark, which quantifies this explicitly by comparing model-generated videos to real-world videos of physical experiments. In this work, we present a...

</details>

---

### [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/abs/2606.18250v1)

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab et al. (7 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18250v1) | [PDF](https://arxiv.org/pdf/2606.18250v1.pdf) | [Project Page](https://fr3d-wm.github.io)

<details>
<summary>Abstract</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. U...

</details>

---

### [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/abs/2606.17730v1)

**Authors:** Zhexiao Xiong, Yizhi Song, Hao Kang, Qing Yan, Liming Jiang et al. (14 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17730v1) | [PDF](https://arxiv.org/pdf/2606.17730v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable...

</details>

---

## Other Recent Papers

### [Lifecycle-Aware Dynamic Analysis for Secure ML Model Execution](https://arxiv.org/abs/2606.19023v1)

**Authors:** Gabriele Digregorio, Marco Di Gennaro, Francesco Pastore, Stefano Zanero, Stefano Longari et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.19023v1) | [PDF](https://arxiv.org/pdf/2606.19023v1.pdf)

<details>
<summary>Abstract</summary>

The growing reliance on pre-trained Machine Learning (ML) models has introduced new attack surfaces. Recent vulnerabilities demonstrate that malicious behavior can be embedded within model artifacts, often bypassing existing defenses. Current model-scanning solutions primarily rely on static, format-specific rules or known attack signatures, which limit their ability to generalize across frameworks and to detect novel exploitation paths. In contrast, we propose a solution that focuses on the eff...

</details>

---

### [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960v1)

**Authors:** Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li et al. (10 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18960v1) | [PDF](https://arxiv.org/pdf/2606.18960v1.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts. However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames. Existing m...

</details>

---

### [DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration](https://arxiv.org/abs/2606.18825v1)

**Authors:** Luoyao Kang, Yuelin Zhang, Jiwei Shan, Haifan Gong, Qingpeng Ding et al. (6 authors)

**Published:** 2026-06-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18825v1) | [PDF](https://arxiv.org/pdf/2606.18825v1.pdf)

<details>
<summary>Abstract</summary>

Ultrasound (US) is widely used for surgical navigation, yet real-time registration between intraoperative 2D slices and preoperative 3D volumes remains challenging due to partial observability, speckle noise, and the action-dependent US acquisition. Existing methods are one-shot or short-horizon, making it hard for them to gather evidence over time or capture how surgeons adjust probe motion based on on-screen feedback. We propose DreamReg, a belief-driven world-model framework that formulates 2...

</details>

---

### [Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/abs/2606.18697v1)

**Authors:** Yibin Hu, Xiaolin Sun, Zizhan Zheng

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.CR, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18697v1) | [PDF](https://arxiv.org/pdf/2606.18697v1.pdf)

<details>
<summary>Abstract</summary>

Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. However, the process of updating world models from collected experience creates a training-time attack surface: adversarially poisoned fine-tuning trajectories can manipulate the learned dynamics and thereby corrupt downstream planning. In this paper, we propose SWAAP, the first two-stage data poisoning framework for learned world models. In the first stage, SWAAP identifie...

</details>

---

### [Dual-Channel Grounded World Modeling (DCGWM): Structural Prevention of Objective Interference Collapse via Heterogeneous External Grounding with Inward-Only Gradient Flow](https://arxiv.org/abs/2606.18688v1)

**Authors:** Akshay Hazare

**Published:** 2026-06-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.18688v1) | [PDF](https://arxiv.org/pdf/2606.18688v1.pdf)

<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) are a leading approach to world model representation learning. We identify a failure mode in JEPA-based world models grounded against two qualitatively distinct external signals: physical dynamics (sparse, high-magnitude, constraint-satisfying gradient corrections) and social-behavioral dynamics (diffuse, distribution-matching corrections). We term this Objective Interference Collapse (OIC): we argue that joint learning in a shared latent space ca...

</details>

---

### [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610v1)

**Authors:** Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi et al. (12 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18610v1) | [PDF](https://arxiv.org/pdf/2606.18610v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating generalist robot manipulation policies in the real world is expensive, slow, and difficult to scale. Action-conditioned video world models offer a scalable alternative by simulating policy rollouts. Autoregressive rollouts accumulate compounding errors, observations across multiple camera views must remain mutually consistent, and the evaluator must generalize to policies whose behaviors lie outside the training distribution. We address these challenges with SC3-Eval, a self-consisten...

</details>

---

### [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589v1)

**Authors:** Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She et al. (9 authors)

**Published:** 2026-06-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18589v1) | [PDF](https://arxiv.org/pdf/2606.18589v1.pdf)

<details>
<summary>Abstract</summary>

Action chunking has become a common interface for vision-language-action (VLA) models, enabling low-frequency policy inference to drive high-frequency robot execution. However, once an action chunk is committed, its open-loop execution can be brittle under stochastic dynamics, hardware execution errors, and partial observability. We propose DREAM-Chunk, a test-time scaling method that augments chunking-based policies with a lightweight latent world model, without requiring additional policy fine...

</details>

---

### [PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation](https://arxiv.org/abs/2606.18375v1)

**Authors:** Yuhang Huang, Xuan Lv, Junyan Xu, Zhiyuan Yu, Jiazhao Zhang et al. (28 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18375v1) | [PDF](https://arxiv.org/pdf/2606.18375v1.pdf)

<details>
<summary>Abstract</summary>

World foundation models (WFMs) are powerful simulators, yet they predominantly operate in a single-view setting and lack the multi-view 3D consistency required for robotic manipulation. While robotic systems rely on multiple cameras (egocentric, eye-to-hand, and wrist-mounted) for policy learning, current multi-view world models simply concatenate view tokens without explicit geometric reasoning. This causes cross-view object drift, depth inconsistency, and texture misalignment. We trace these f...

</details>

---

### [Looped World Models](https://arxiv.org/abs/2606.18208v1)

**Authors:** Hongyuan Adam Lu, Z. L. Victor Wei, Qun Zhang, Jinrui Zeng, Bowen Cao et al. (31 authors)

**Published:** 2026-06-16 | **Categories:** cs.LG, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.18208v1) | [PDF](https://arxiv.org/pdf/2606.18208v1.pdf)

<details>
<summary>Abstract</summary>

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive compu...

</details>

---

### [EgoCS-400K: An Egocentric Gameplay Dataset for World Models](https://arxiv.org/abs/2606.18180v1)

**Authors:** Rongjin Guo, Dong Liang, Yuhao Liu, Fang Liu, Tianyu Huang et al. (7 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.18180v1) | [PDF](https://arxiv.org/pdf/2606.18180v1.pdf)

<details>
<summary>Abstract</summary>

The shift from video generation to interactive world modeling places new demands on data: beyond captioned videos, world models require temporally aligned video-action-language trajectories grounded in the actions, camera motion, states, and events that drive future scene changes. However, such data is difficult to obtain at scale. Web video datasets offer broad visual coverage but lack executable actions and reliable states; robotic datasets provide action and state supervision but are costly a...

</details>

---

### [PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space](https://arxiv.org/abs/2606.17924v1)

**Authors:** Bochen Yang, Lianlei Shan

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17924v1) | [PDF](https://arxiv.org/pdf/2606.17924v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model...

</details>

---

### [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906v1)

**Authors:** Zezhong Qian, Xiaowei Chi, Yu Qi, Haozhan Li, Zhi Yang Chen et al. (6 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17906v1) | [PDF](https://arxiv.org/pdf/2606.17906v1.pdf)

<details>
<summary>Abstract</summary>

Recent World-Action (WA) models demonstrate strong generalization ability and data efficiency, but they typically rely on expert trajectories for training. This reliance limits their ability to acquire fine-grained manipulation skills beyond the demonstration distribution and prevents them from continuously improving through real-world interaction. To address these limitations, we propose WAM-RL, a reinforcement learning framework that enables joint optimization of the world model and the action...

</details>

---

### [MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model](https://arxiv.org/abs/2606.17800v1)

**Authors:** Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong et al. (17 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17800v1) | [PDF](https://arxiv.org/pdf/2606.17800v1.pdf)

<details>
<summary>Abstract</summary>

As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies. In this work, we define the position of social world models and build a prototype model as the first step towards this goal. While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric...

</details>

---

### [OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation](https://arxiv.org/abs/2606.17536v1)

**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu et al. (11 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17536v1) | [PDF](https://arxiv.org/pdf/2606.17536v1.pdf)

<details>
<summary>Abstract</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-c...

</details>

---

### [NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama](https://arxiv.org/abs/2606.17391v1)

**Authors:** Logan Mann, Abdur Rahman, Mohammad Saifullah, Taaha Kazi, Vasu Sharma

**Published:** 2026-06-16 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17391v1) | [PDF](https://arxiv.org/pdf/2606.17391v1.pdf)

<details>
<summary>Abstract</summary>

Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open b...

</details>

---
