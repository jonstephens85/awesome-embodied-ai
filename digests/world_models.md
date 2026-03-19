# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-19 16:58 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)

**Authors:** Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu et al. (6 authors)

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17808v1) | [PDF](https://arxiv.org/pdf/2603.17808v1.pdf) | [Project Page](https://eva-project-page.github.io/)

<details>
<summary>Abstract</summary>

Video generative models are increasingly used as world models for robotics, where a model generates a future visual rollout conditioned on the current observation and task instruction, and an inverse dynamics model (IDM) converts the generated frames into executable robot actions. However, current video world models lack explicit executability constraints. As a result, visually coherent rollouts may still violate rigid-body and kinematic consistency, producing unstable or infeasible control comm...

</details>

---

### [VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs](https://arxiv.org/abs/2603.17652v1)

**Authors:** Chaokang Jiang, Desen Zhou, Jiuming Liu, Kevin Li Sun

**Published:** 2026-03-18 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.17652v1) | [PDF](https://arxiv.org/pdf/2603.17652v1.pdf) | [GitHub](https://github.com/jiangchaokang/VectorWorld}{code})

<details>
<summary>Abstract</summary>

Closed-loop evaluation of autonomous-driving policies requires interactive simulation beyond log replay. However, existing generative world models often degrade in closed loop due to (i) history-free initialization that mismatches policy inputs, (ii) multi-step sampling latency that violates real-time budgets, and (iii) compounding kinematic infeasibility over long horizons. We propose VectorWorld, a streaming world model that incrementally generates ego-centric $64 \mathrm{m}\times 64\mathrm{m}...

</details>

---

### [Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1)

**Authors:** Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao et al. (7 authors)

**Published:** 2026-03-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.17375v1) | [PDF](https://arxiv.org/pdf/2603.17375v1.pdf) | [Project Page](https://sunyangtian.github.io/StereoWorld-web/)

<details>
<summary>Abstract</summary>

We present StereoWorld, a camera-conditioned stereo world model that jointly learns appearance and binocular geometry for end-to-end stereo video generation.Unlike monocular RGB or RGBD approaches, StereoWorld operates exclusively within the RGB modality, while simultaneously grounding geometry directly from disparity. To efficiently achieve consistent stereo generation, our approach introduces two key designs: (1) a unified camera-frame RoPE that augments latent tokens with camera-aware rotary ...

</details>

---

### [MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)

**Authors:** Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin et al. (11 authors)

**Published:** 2026-03-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.17117v1) | [PDF](https://arxiv.org/pdf/2603.17117v1.pdf) | [Project Page](https://mosaicmem.github.io/mosaicmem/)

<details>
<summary>Abstract</summary>

Video diffusion models are moving beyond short, plausible clips toward world simulators that must remain consistent under camera motion, revisits, and intervention. Yet spatial memory remains a key bottleneck: explicit 3D structures can improve reprojection-based consistency but struggle to depict moving objects, while implicit memory often produces inaccurate camera motion even with correct poses. We propose Mosaic Memory (MosaicMem), a hybrid spatial memory that lifts patches into 3D for relia...

</details>

---

### [WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)

**Authors:** Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee et al. (12 authors)

**Published:** 2026-03-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16871v1) | [PDF](https://arxiv.org/pdf/2603.16871v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Recent advances in video diffusion transformers have enabled interactive gaming world models that allow users to explore generated environments over extended horizons. However, existing approaches struggle with precise action control and long-horizon 3D consistency. Most prior works treat user actions as abstract conditioning signals, overlooking the fundamental geometric coupling between actions and the 3D world, whereby actions induce relative camera motions that accumulate into a global camer...

</details>

---

### [DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models](https://arxiv.org/abs/2603.16860v1)

**Authors:** Emily Yue-Ting Jia, Weiduo Yuan, Tianheng Shi, Vitor Guizilini, Jiageng Mao et al. (6 authors)

**Published:** 2026-03-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.16860v1) | [PDF](https://arxiv.org/pdf/2603.16860v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Robotic manipulation requires sophisticated commonsense reasoning, a capability naturally possessed by large-scale Vision-Language Models (VLMs). While VLMs show promise as zero-shot planners, their lack of grounded physical understanding often leads to compounding errors and low success rates when deployed in complex real-world environments, particularly for challenging tasks like deformable object manipulation. Although Reinforcement Learning (RL) can adapt these planners to specific task dyna...

</details>

---

### [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)

**Authors:** Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han et al. (6 authors)

**Published:** 2026-03-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16669v1) | [PDF](https://arxiv.org/pdf/2603.16669v1.pdf) | [Project Page](https://mutianxu.github.io/Kinema4D-project-page/)

<details>
<summary>Abstract</summary>

Simulating robot-world interactions is a cornerstone of Embodied AI. Recently, a few works have shown promise in leveraging video generations to transcend the rigid visual/physical constraints of traditional simulators. However, they primarily operate in 2D space or are guided by static environmental cues, ignoring the fundamental reality that robot-world interactions are inherently 4D spatiotemporal events that require precise interactive modeling. To restore this 4D essence while ensuring the ...

</details>

---

### [Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation](https://arxiv.org/abs/2603.16086v1)

**Authors:** Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu, Hesheng Wang

**Published:** 2026-03-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16086v1) | [PDF](https://arxiv.org/pdf/2603.16086v1.pdf) | [Project Page](are)

<details>
<summary>Abstract</summary>

While recent Vision-Language-Action (VLA) models have begun to incorporate audio, they typically treat sound as static pre-execution prompts or focus exclusively on human speech. This leaves a significant gap in real-time, sound-centric manipulation where fleeting environmental acoustics provide critical state verification during task execution. Consequently, key sounds are easily missed due to low-frequency updates or system latency. This problem is exacerbated by action chunking with open-loop...

</details>

---

## Other Recent Papers

### [From Digital Twins to World Models:Opportunities, Challenges, and Applications for Mobile Edge General Intelligence](https://arxiv.org/abs/2603.17420v1)

**Authors:** Jie Zheng, Dusit Niyato, Changyuan Zhao, Jiawen Kang, Jiacheng Wang

**Published:** 2026-03-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17420v1) | [PDF](https://arxiv.org/pdf/2603.17420v1.pdf)

<details>
<summary>Abstract</summary>

The rapid evolution toward 6G and beyond communication systems is accelerating the convergence of digital twins and world models at the network edge. Traditional digital twins provide high-fidelity representations of physical systems and support monitoring, analysis, and offline optimization. However, in highly dynamic edge environments, they face limitations in autonomy, adaptability, and scalability. This paper presents a systematic survey of the transition from digital twins to world models a...

</details>

---

### [Grid-World Representations in Transformers Reflect Predictive Geometry](https://arxiv.org/abs/2603.16689v1)

**Authors:** Sasha Brenner, Thomas R. Knösche, Nico Scherf

**Published:** 2026-03-17 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.16689v1) | [PDF](https://arxiv.org/pdf/2603.16689v1.pdf)

<details>
<summary>Abstract</summary>

Next-token predictors often appear to develop internal representations of the latent world and its rules. The probabilistic nature of these models suggests a deep connection between the structure of the world and the geometry of probability distributions. In order to understand this link more precisely, we use a minimal stochastic process as a controlled setting: constrained random walks on a two-dimensional lattice that must reach a fixed endpoint after a predetermined number of steps. Optimal ...

</details>

---

### [DriveFix: Spatio-Temporally Coherent Driving Scene Restoration](https://arxiv.org/abs/2603.16306v1)

**Authors:** Heyu Si, Brandon James Denis, Muyang Sun, Dragos Datcu, Yaoru Li et al. (12 authors)

**Published:** 2026-03-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16306v1) | [PDF](https://arxiv.org/pdf/2603.16306v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in 4D scene reconstruction, particularly those leveraging diffusion priors, have shown promise for novel view synthesis in autonomous driving. However, these methods often process frames independently or in a view-by-view manner, leading to a critical lack of spatio-temporal synergy. This results in spatial misalignment across cameras and temporal drift in sequences. We propose DriveFix, a novel multi-view restoration framework that ensures spatio-temporal coherence for drivi...

</details>

---

### [The Finetuner's Fallacy: When to Pretrain with Your Finetuning Data](https://arxiv.org/abs/2603.16177v1)

**Authors:** Christina Baek, Ricardo Pio Monti, David Schwab, Amro Abbas, Rishabh Adiga et al. (34 authors)

**Published:** 2026-03-17 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.16177v1) | [PDF](https://arxiv.org/pdf/2603.16177v1.pdf)

<details>
<summary>Abstract</summary>

Real-world model deployments demand strong performance on narrow domains where data is often scarce. Typically, practitioners finetune models to specialize them, but this risks overfitting to the domain and forgetting general knowledge. We study a simple strategy, specialized pretraining (SPT), where a small domain dataset, typically reserved for finetuning, is repeated starting from pretraining as a fraction of the total tokens. Across three specialized domains (ChemPile, MusicPile, and ProofPi...

</details>

---
