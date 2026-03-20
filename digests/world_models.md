# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-20 22:18 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding](https://arxiv.org/abs/2603.19219v1)

**Authors:** Dong Zhuo, Wenzhao Zheng, Sicheng Zuo, Siming Yan, Lu Hou et al. (7 authors)

**Published:** 2026-03-19 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.19219v1) | [PDF](https://arxiv.org/pdf/2603.19219v1.pdf) | [Project Page](https://paryi555.github.io/DriveTok/) | [GitHub](https://github.com/paryi555/DriveTok)

<details>
<summary>Abstract</summary>

With the growing adoption of vision-language-action models and world models in autonomous driving systems, scalable image tokenization becomes crucial as the interface for the visual modality. However, most existing tokenizers are designed for monocular and 2D scenes, leading to inefficiency and inter-view inconsistency when applied to high-resolution multi-view driving scenes. To address this, we propose DriveTok, an efficient 3D driving scene tokenizer for unified multi-view reconstruction and...

</details>

---

### [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201v1)

**Authors:** Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang et al. (15 authors)

**Published:** 2026-03-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.19201v1) | [PDF](https://arxiv.org/pdf/2603.19201v1.pdf) | [Project Page](https://mrsecant.github.io/OmniVTA)

<details>
<summary>Abstract</summary>

Contact-rich manipulation tasks, such as wiping and assembly, require accurate perception of contact forces, friction changes, and state transitions that cannot be reliably inferred from vision alone. Despite growing interest in visuo-tactile manipulation, progress is constrained by two persistent limitations: existing datasets are small in scale and narrow in task coverage, and current methods treat tactile signals as passive observations rather than using them to model contact dynamics or enab...

</details>

---

### [ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics](https://arxiv.org/abs/2603.18336v1)

**Authors:** Gaotian Wang, Kejia Ren, Andrew S. Morgan, Kaiyu Hang

**Published:** 2026-03-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.18336v1) | [PDF](https://arxiv.org/pdf/2603.18336v1.pdf) | [Project Page](at) | [GitHub](https://github.com/Rice-RobotPI-Lab/ManiDreams)

<details>
<summary>Abstract</summary>

Dynamics models, whether simulators or learned world models, have long been central to robotic manipulation, but most focus on minimizing prediction error rather than confronting a more fundamental challenge: real-world manipulation is inherently uncertain. We argue that robust manipulation under uncertainty is fundamentally an integration problem: uncertainties must be represented, propagated, and constrained within the planning loop, not merely suppressed during training. We present and open-s...

</details>

---

### [R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation](https://arxiv.org/abs/2603.18202v1)

**Authors:** Naoki Morihira, Amal Nahar, Kartik Bharadwaj, Yasuhiro Kato, Akinobu Hayashi et al. (6 authors)

**Published:** 2026-03-18 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.18202v1) | [PDF](https://arxiv.org/pdf/2603.18202v1.pdf) | [GitHub](https://github.com/NM512/r2dreamer)

<details>
<summary>Abstract</summary>

A central challenge in image-based Model-Based Reinforcement Learning (MBRL) is to learn representations that distill essential information from irrelevant visual details. While promising, reconstruction-based methods often waste capacity on large task-irrelevant regions. Decoder-free methods instead learn robust representations by leveraging Data Augmentation (DA), but reliance on such external regularizers limits versatility. We propose R2-Dreamer, a decoder-free MBRL framework with a self-sup...

</details>

---

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

## Other Recent Papers

### [AcceRL: A Distributed Asynchronous Reinforcement Learning and World Model Framework for Vision-Language-Action Models](https://arxiv.org/abs/2603.18464v1)

**Authors:** Chengxuan Lu, Shukuan Wang, Yanjie Li, Wei Liu, Shiji Jin et al. (9 authors)

**Published:** 2026-03-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.18464v1) | [PDF](https://arxiv.org/pdf/2603.18464v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) for large-scale Vision-Language-Action (VLA) models faces significant challenges in computational efficiency and data acquisition. We propose AcceRL, a fully asynchronous and decoupled RL framework designed to eliminate synchronization barriers by physically isolating training, inference, and rollouts. Crucially, AcceRL is the first to integrate a plug-and-play, trainable world model into a distributed asynchronous RL pipeline to generate virtual experiences. Experime...

</details>

---

### [Enactor: From Traffic Simulators to Surrogate World Models](https://arxiv.org/abs/2603.18266v1)

**Authors:** Yash Ranjan, Rahul Sengupta, Anand Rangarajan, Sanjay Ranka

**Published:** 2026-03-18 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.18266v1) | [PDF](https://arxiv.org/pdf/2603.18266v1.pdf)

<details>
<summary>Abstract</summary>

Traffic microsimulators are widely used to evaluate road network performance under various ``what-if" conditions. However, the behavior models controlling the actions of the actors are overly simplistic and fails to capture realistic actor-actor interactions. Deep learning-based methods have been applied to model vehicles and pedestrians as ``agents" responding to their surrounding ``environment" (including lanes, signals, and neighboring agents). Although effective in learning actor-actor inter...

</details>

---

### [From Digital Twins to World Models:Opportunities, Challenges, and Applications for Mobile Edge General Intelligence](https://arxiv.org/abs/2603.17420v1)

**Authors:** Jie Zheng, Dusit Niyato, Changyuan Zhao, Jiawen Kang, Jiacheng Wang

**Published:** 2026-03-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.17420v1) | [PDF](https://arxiv.org/pdf/2603.17420v1.pdf)

<details>
<summary>Abstract</summary>

The rapid evolution toward 6G and beyond communication systems is accelerating the convergence of digital twins and world models at the network edge. Traditional digital twins provide high-fidelity representations of physical systems and support monitoring, analysis, and offline optimization. However, in highly dynamic edge environments, they face limitations in autonomy, adaptability, and scalability. This paper presents a systematic survey of the transition from digital twins to world models a...

</details>

---
