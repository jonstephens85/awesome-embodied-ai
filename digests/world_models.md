# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-18 22:24 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Simulation Distillation: Pretraining World Models in Simulation for Rapid Real-World Adaptation](https://arxiv.org/abs/2603.15759v1)

**Authors:** Jacob Levy, Tyler Westenbroek, Kevin Huang, Fernando Palafox, Patrick Yin et al. (9 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.15759v1) | [PDF](https://arxiv.org/pdf/2603.15759v1.pdf) | [Project Page](and)

<details>
<summary>Abstract</summary>

Simulation-to-real transfer remains a central challenge in robotics, as mismatches between simulated and real-world dynamics often lead to failures. While reinforcement learning offers a principled mechanism for adaptation, existing sim-to-real finetuning methods struggle with exploration and long-horizon credit assignment in the low-data regimes typical of real-world robotics. We introduce Simulation Distillation (SimDist), a sim-to-real framework that distills structural priors from a simulato...

</details>

---

### [Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)

**Authors:** Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin et al. (13 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.15583v1) | [PDF](https://arxiv.org/pdf/2603.15583v1.pdf) | [Project Page](https://seoul-world-model.github.io/)

<details>
<summary>Abstract</summary>

What if a world simulation model could render not an imagined environment but a city that actually exists? Prior generative world models synthesize visually plausible yet artificial environments by imagining all content. We present Seoul World Model (SWM), a city-scale world model grounded in the real city of Seoul. SWM anchors autoregressive video generation through retrieval-augmented conditioning on nearby street-view images. However, this design introduces several challenges, including tempo...

</details>

---

### [NavThinker: Action-Conditioned World Models for Coupled Prediction and Planning in Social Navigation](https://arxiv.org/abs/2603.15359v1)

**Authors:** Tianshuai Hu, Zeying Gong, Lingdong Kong, XiaoDong Mei, Yiyi Ding et al. (10 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15359v1) | [PDF](https://arxiv.org/pdf/2603.15359v1.pdf) | [GitHub](https://github.com/hutslib/NavThinker)

<details>
<summary>Abstract</summary>

Social navigation requires robots to act safely in dynamic human environments. Effective behavior demands thinking ahead: reasoning about how the scene and pedestrians evolve under different robot actions rather than reacting to current observations alone. This creates a coupled prediction-planning challenge, where robot actions and human motion mutually influence each other. To address this challenge, we propose NavThinker, a future-aware framework that couples an action-conditioned world model...

</details>

---

### [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)

**Authors:** Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong et al. (8 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.14948v1) | [PDF](https://arxiv.org/pdf/2603.14948v1.pdf) | [GitHub](https://github.com/TabGuigui/WorldDrive)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving aims to generate safe and plausible planning policies from raw sensor input. Driving world models have shown great potential in learning rich representations by predicting the future evolution of a driving scene. However, existing driving world models primarily focus on visual scene representation, and motion representation is not explicitly designed to be planner-shared and inheritable, leaving a schism between the optimization of visual scene generation and the re...

</details>

---

## Other Recent Papers

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

### [CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving](https://arxiv.org/abs/2603.15771v1)

**Authors:** Yihong Guo, Dongqiangzi Ye, Sijia Chen, Anqi Liu, Xianming Liu

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.15771v1) | [PDF](https://arxiv.org/pdf/2603.15771v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving requires safe planning, but most learning-based planners lack explicit self-correction ability: once an unsafe action is proposed, there is no mechanism to correct it. Thus, we propose CorrectionPlanner, an autoregressive planner with self-correction that models planning as motion-token generation within a propose, evaluate, and correct loop. At each planning step, the policy proposes an action, namely a motion token, and a learned collision critic predicts whether it will ind...

</details>

---

### [RS-WorldModel: a Unified Model for Remote Sensing Understanding and Future Sense Forecasting](https://arxiv.org/abs/2603.14941v1)

**Authors:** Linrui Xu, Zhongan Wang, Fei Shen, Gang Xu, Huiping Zhuang et al. (7 authors)

**Published:** 2026-03-16 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.14941v1) | [PDF](https://arxiv.org/pdf/2603.14941v1.pdf)

<details>
<summary>Abstract</summary>

Remote sensing world models aim to both explain observed changes and forecast plausible futures, two tasks that share spatiotemporal priors. Existing methods, however, typically address them separately, limiting cross-task transfer. We present RS-WorldModel, a unified world model for remote sensing that jointly handles spatiotemporal change understanding and text-guided future scene forecasting, and we build RSWBench-1.1M, a 1.1 million sample dataset with rich language annotations covering both...

</details>

---

### [PerlAD: Towards Enhanced Closed-loop End-to-end Autonomous Driving with Pseudo-simulation-based Reinforcement Learning](https://arxiv.org/abs/2603.14908v1)

**Authors:** Yinfeng Gao, Qichao Zhang, Deqing Liu, Zhongpu Xia, Guang Li et al. (11 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.14908v1) | [PDF](https://arxiv.org/pdf/2603.14908v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving policies based on Imitation Learning (IL) often struggle in closed-loop execution due to the misalignment between inadequate open-loop training objectives and real driving requirements. While Reinforcement Learning (RL) offers a solution by directly optimizing driving goals via reward signals, the rendering-based training environments introduce the rendering gap and are inefficient due to high computational costs. To overcome these challenges, we present a novel Pse...

</details>

---
