# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-12 22:22 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075v1)

**Authors:** Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin et al. (13 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.11075v1) | [PDF](https://arxiv.org/pdf/2602.11075v1.pdf) | [Project Page](https://opendrivelab.com/kai0-rl/)

<details>
<summary>Abstract</summary>

Despite the sustained scaling on model capacity and data acquisition, Vision-Language-Action (VLA) models remain brittle in contact-rich and dynamic manipulation tasks, where minor execution deviations can compound into failures. While reinforcement learning (RL) offers a principled path to robustness, on-policy RL in the physical world is constrained by safety risk, hardware cost, and environment reset. To bridge this gap, we present RISE, a scalable framework of robotic reinforcement learning ...

</details>

---

### [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983v1)

**Authors:** Qian Long, Yueze Wang, Jiaxi Song, Junbo Zhang, Peiyan Li et al. (16 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10983v1) | [PDF](https://arxiv.org/pdf/2602.10983v1.pdf) | [Project Page](\href{https://vista-wm.github.io/}{https://vista-wm.github.io})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are promising for generalist robot manipulation but remain brittle in out-of-distribution (OOD) settings, especially with limited real-robot data. To resolve the generalization bottleneck, we introduce a hierarchical Vision-Language-Action framework \our{} that leverages the generalization of large-scale pre-trained world model for robust and generalizable VIsual Subgoal TAsk decomposition VISTA. Our hierarchical framework \our{} consists of a world model as t...

</details>

---

### [LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer](https://arxiv.org/abs/2602.10556v1)

**Authors:** Lihan Zha, Asher J. Hancock, Mingtong Zhang, Tenny Yin, Yixuan Huang et al. (8 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.10556v1) | [PDF](https://arxiv.org/pdf/2602.10556v1.pdf) | [Project Page](https://lap-vla.github.io)

<details>
<summary>Abstract</summary>

A long-standing goal in robotics is a generalist policy that can be deployed zero-shot on new robot embodiments without per-embodiment adaptation. Despite large-scale multi-embodiment pre-training, existing Vision-Language-Action models (VLAs) remain tightly coupled to their training embodiments and typically require costly fine-tuning. We introduce Language-Action Pre-training (LAP), a simple recipe that represents low-level robot actions directly in natural language, aligning action supervisio...

</details>

---

### [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/abs/2602.10109v1)

**Authors:** Jinhui Ye, Fangjing Wang, Ning Gao, Junqiu Yu, Yangkun Zhu et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10109v1) | [PDF](https://arxiv.org/pdf/2602.10109v1.pdf) | [Project Page](https://internrobotics.github.io/internvla-m1.github.io/)

<details>
<summary>Abstract</summary>

Large vision-language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions. We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs. ST4VLA includes two stages: (i) spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory pr...

</details>

---

### [UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking](https://arxiv.org/abs/2602.10093v1)

**Authors:** Baijun Chen, Weijie Wan, Tianxing Chen, Xianda Guo, Congsheng Xu et al. (16 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10093v1) | [PDF](https://arxiv.org/pdf/2602.10093v1.pdf) | [Project Page](https://univtac.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation has seen rapid progress with vision-language-action (VLA) policies. However, visuo-tactile perception is critical for contact-rich manipulation, as tasks such as insertion are difficult to complete robustly using vision alone. At the same time, acquiring large-scale and reliable tactile data in the physical world remains costly and challenging, and the lack of a unified evaluation platform further limits policy learning and systematic analysis. To address these challenges, w...

</details>

---

### [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](https://arxiv.org/abs/2602.09722v1)

**Authors:** Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09722v1) | [PDF](https://arxiv.org/pdf/2602.09722v1.pdf) | [Project Page](https://research.beingbeyond.com/rethink_vla)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models show strong promise for generalist robot control, it remains unclear whether -- and under what conditions -- the standard "scale data" recipe translates to robotics, where training data is inherently heterogeneous across embodiments, sensors, and action spaces. We present a systematic, controlled study of VLA scaling that revisits core training choices for pretraining across diverse robots. Using a representative VLA framework that combines a vision-lang...

</details>

---

### [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106v1)

**Authors:** Modi Shi, Shijia Peng, Jin Chen, Haoran Jiang, Yinghui Li et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10106v1) | [PDF](https://arxiv.org/pdf/2602.10106v1.pdf) | [Project Page](https://opendrivelab.com/EgoHumanoid)

<details>
<summary>Abstract</summary>

Human demonstrations offer rich environmental diversity and scale naturally, making them an appealing alternative to robot teleoperation. While this paradigm has advanced robot-arm manipulation, its potential for the more challenging, data-hungry problem of humanoid loco-manipulation remains largely unexplored. We present EgoHumanoid, the first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabli...

</details>

---

## Other Recent Papers

### [RADAR: Benchmarking Vision-Language-Action Generalization via Real-World Dynamics, Spatial-Physical Intelligence, and Autonomous Evaluation](https://arxiv.org/abs/2602.10980v1)

**Authors:** Yuhao Chen, Zhihao Zhan, Xiaoxin Lin, Zijian Song, Hao Liu et al. (14 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10980v1) | [PDF](https://arxiv.org/pdf/2602.10980v1.pdf)

<details>
<summary>Abstract</summary>

VLA models have achieved remarkable progress in embodied intelligence; however, their evaluation remains largely confined to simulations or highly constrained real-world settings. This mismatch creates a substantial reality gap, where strong benchmark performance often masks poor generalization in diverse physical environments. We identify three systemic shortcomings in current benchmarking practices that hinder fair and reliable model comparison. (1) Existing benchmarks fail to model real-world...

</details>

---

### [From Representational Complementarity to Dual Systems: Synergizing VLM and Vision-Only Backbones for End-to-End Driving](https://arxiv.org/abs/2602.10719v1)

**Authors:** Sining Ang, Yuguang Yang, Chenxu Dang, Canyu Chen, Cheng Chi et al. (11 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10719v1) | [PDF](https://arxiv.org/pdf/2602.10719v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) driving augments end-to-end (E2E) planning with language-enabled backbones, yet it remains unclear what changes beyond the usual accuracy--cost trade-off. We revisit this question with 3--RQ analysis in RecogDrive by instantiating the system with a full VLM and vision-only backbones, all under an identical diffusion Transformer planner. RQ1: At the backbone level, the VLM can introduce additional subspaces upon the vision-only backbones. RQ2: This unique subspace lea...

</details>

---

### [AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models](https://arxiv.org/abs/2602.10698v1)

**Authors:** Zhifeng Rao, Wenlong Chen, Lei Xie, Xia Hua, Dongfu Yin et al. (7 authors)

**Published:** 2026-02-11 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.10698v1) | [PDF](https://arxiv.org/pdf/2602.10698v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic perception and control, yet most existing approaches primarily rely on VLM trained using 2D images, which limits their spatial understanding and action grounding in complex 3D environments. To address this limitation, we propose a novel framework that integrates depth estimation into VLA models to enrich 3D feature representations. Specifically, we employ a depth estimation baseline called VGGT to extract g...

</details>

---

### [Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning](https://arxiv.org/abs/2602.10503v1)

**Authors:** Yuan Liu, Haoran Li, Shuai Tian, Yuxing Qin, Yuhui Chen et al. (8 authors)

**Published:** 2026-02-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.10503v1) | [PDF](https://arxiv.org/pdf/2602.10503v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained on large-scale and diverse datasets, VLA models demonstrate strong generalization and adaptability as general-purpose robotic policies. However, Supervised Fine-Tuning (SFT), which serves as the primary mechanism for adapting VLAs to downstream domains, requires substantial amounts of task-specific data and is prone to catastrophic forgetting. To address these limitations, we propose LifeLong-RFT, a simple yet effective Reinforcement Fine-Tuning (RFT) strategy for VLA models independe...

</details>

---

### [Hardware Co-Design Scaling Laws via Roofline Modelling for On-Device LLMs](https://arxiv.org/abs/2602.10377v1)

**Authors:** Luoyang Sun, Jiwen Jiang, Yifeng Ding, Fengfa Li, Yan Song et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.LG, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2602.10377v1) | [PDF](https://arxiv.org/pdf/2602.10377v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) have emerged as a key paradigm of Physical AI and are increasingly deployed in autonomous vehicles, robots, and smart spaces. In these resource-constrained on-device settings, selecting an appropriate large language model (LLM) backbone is a critical challenge: models must balance accuracy with strict inference latency and hardware efficiency constraints. This makes hardware-software co-design a game-changing requirement for on-device LLM deployment, where ea...

</details>

---

### [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098v1)

**Authors:** Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu et al. (9 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.10098v1) | [PDF](https://arxiv.org/pdf/2602.10098v1.pdf)

<details>
<summary>Abstract</summary>

Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a JEPA-style pretraining framework that sidesteps these pitfalls by design. The key idea is \emph{leakage-free state prediction}: a target encoder prod...

</details>

---

### [RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation](https://arxiv.org/abs/2602.09973v1)

**Authors:** Hao Li, Ziqin Wang, Zi-han Ding, Shuai Yang, Yilun Chen et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09973v1) | [PDF](https://arxiv.org/pdf/2602.09973v1.pdf)

<details>
<summary>Abstract</summary>

Advances in large vision-language models (VLMs) have stimulated growing interest in vision-language-action (VLA) systems for robot manipulation. However, existing manipulation datasets remain costly to curate, highly embodiment-specific, and insufficient in coverage and diversity, thereby hindering the generalization of VLA models. Recent approaches attempt to mitigate these limitations via a plan-then-execute paradigm, where high-level plans (e.g., subtasks, trace) are first generated and subse...

</details>

---

### [BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation](https://arxiv.org/abs/2602.09849v2)

**Authors:** Yucheng Hu, Jianke Zhang, Yuanfei Luo, Yanjiang Guo, Xiaoyu Chen et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09849v2) | [PDF](https://arxiv.org/pdf/2602.09849v2.pdf)

<details>
<summary>Abstract</summary>

Equipping embodied agents with the ability to reason about tasks, foresee physical outcomes, and generate precise actions is essential for general-purpose manipulation. While recent Vision-Language-Action (VLA) models have leveraged pre-trained foundation models, they typically focus on either linguistic planning or visual forecasting in isolation. These methods rarely integrate both capabilities simultaneously to guide action generation, leading to suboptimal performance in complex, long-horizo...

</details>

---

### [AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild](https://arxiv.org/abs/2602.09657v1)

**Authors:** Xiaolou Sun, Wufei Si, Wenhui Ni, Yuntian Li, Dongming Wu et al. (13 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09657v1) | [PDF](https://arxiv.org/pdf/2602.09657v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI. Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes. However, real-world outdoor exploration typically occurs in unknown environments where detailed navigation instructions are unavailable. Instead, on...

</details>

---

### [Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments](https://arxiv.org/abs/2602.09430v1)

**Authors:** Yiwen Pang, Bo Zhou, Changjin Li, Xuanhao Wang, Shengxiang Xu et al. (8 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.09430v1) | [PDF](https://arxiv.org/pdf/2602.09430v1.pdf)

<details>
<summary>Abstract</summary>

Robotic laboratories play a critical role in autonomous scientific discovery by enabling scalable, continuous experimental execution. Recent vision-language-action (VLA) models offer a promising foundation for robotic laboratories. However, scientific experiments typically involve long-horizon tasks composed of multiple atomic tasks, posing a fundamental challenge to existing VLA models. While VLA models fine-tuned for scientific tasks can reliably execute atomic experimental actions seen during...

</details>

---

### [CAPER: Constrained and Procedural Reasoning for Robotic Scientific Experiments](https://arxiv.org/abs/2602.09367v1)

**Authors:** Jinghan Yang, Jingyi Hou, Xinbo Yu, Wei He, Yifan Wu

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09367v1) | [PDF](https://arxiv.org/pdf/2602.09367v1.pdf)

<details>
<summary>Abstract</summary>

Robotic assistance in scientific laboratories requires procedurally correct long-horizon manipulation, reliable execution under limited supervision, and robustness in low-demonstration regimes. Such conditions greatly challenge end-to-end vision-language-action (VLA) models, whose assumptions of recoverable errors and data-driven policy learning often break down in protocol-sensitive experiments. We propose CAPER, a framework for Constrained And ProcEdural Reasoning for robotic scientific experi...

</details>

---

### [NavDreamer: Video Models as Zero-Shot 3D Navigators](https://arxiv.org/abs/2602.09765v1)

**Authors:** Xijie Huang, Weiqi Gai, Tianyue Wu, Congyu Wang, Zhiyang Liu et al. (8 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09765v1) | [PDF](https://arxiv.org/pdf/2602.09765v1.pdf)

<details>
<summary>Abstract</summary>

Previous Vision-Language-Action models face critical limitations in navigation: scarce, diverse data from labor-intensive collection and static representations that fail to capture temporal dynamics and physical laws. We propose NavDreamer, a video-based framework for 3D navigation that leverages generative video models as a universal interface between language instructions and navigation trajectories. Our main hypothesis is that video's ability to encode spatiotemporal information and physical ...

</details>

---
