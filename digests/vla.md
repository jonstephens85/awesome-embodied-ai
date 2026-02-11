# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-11 22:20 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](https://arxiv.org/abs/2602.09017v1)

**Authors:** Zichen Jeff Cui, Omar Rayyan, Haritheja Etukuru, Bowen Tan, Zavier Andrianarivo et al. (19 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.09017v1) | [PDF](https://arxiv.org/pdf/2602.09017v1.pdf) | [Project Page](https://cap-policy.github.io/)

<details>
<summary>Abstract</summary>

The prevalent paradigm in robot learning attempts to generalize across environments, embodiments, and tasks with language prompts at runtime. A fundamental tension limits this approach: language is often too abstract to guide the concrete physical understanding required for robust manipulation. In this work, we introduce Contact-Anchored Policies (CAP), which replace language conditioning with points of physical contact in space. Simultaneously, we structure CAP as a library of modular utility m...

</details>

---

### [SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios](https://arxiv.org/abs/2602.08440v1)

**Authors:** Tian Gao, Celine Tan, Catherine Glossop, Timothy Gao, Jiankai Sun et al. (11 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.08440v1) | [PDF](https://arxiv.org/pdf/2602.08440v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

A fundamental challenge in autonomous driving is the integration of high-level, semantic reasoning for long-tail events with low-level, reactive control for robust driving. While large vision-language models (VLMs) trained on web-scale data offer powerful common-sense reasoning, they lack the grounded experience necessary for safe vehicle control. We posit that an effective autonomous agent should leverage the world knowledge of VLMs to guide a steerable driving policy toward robust control in d...

</details>

---

## Other Recent Papers

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

### [BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation](https://arxiv.org/abs/2602.09849v1)

**Authors:** Yucheng Hu, Jianke Zhang, Yuanfei Luo, Yanjiang Guo, Xiaoyu Chen et al. (12 authors)

**Published:** 2026-02-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09849v1) | [PDF](https://arxiv.org/pdf/2602.09849v1.pdf)

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

### [TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation](https://arxiv.org/abs/2602.09023v1)

**Authors:** Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han et al. (14 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.09023v1) | [PDF](https://arxiv.org/pdf/2602.09023v1.pdf)

<details>
<summary>Abstract</summary>

Despite strong generalization capabilities, Vision-Language-Action (VLA) models remain constrained by the high cost of expert demonstrations and insufficient real-world interaction. While online reinforcement learning (RL) has shown promise in improving general foundation models, applying RL to VLA manipulation in real-world settings is still hindered by low exploration efficiency and a restricted exploration space. Through systematic real-world experiments, we observe that the effective explora...

</details>

---

### [Any-to-All MRI Synthesis: A Unified Foundation Model for Nasopharyngeal Carcinoma and Its Downstream Applications](https://arxiv.org/abs/2602.08822v1)

**Authors:** Yao Pu, Yiming Shi, Zhenxi Zhang, Peixin Yu, Yitao Zhuang et al. (9 authors)

**Published:** 2026-02-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.08822v1) | [PDF](https://arxiv.org/pdf/2602.08822v1.pdf)

<details>
<summary>Abstract</summary>

Magnetic resonance imaging (MRI) is essential for nasopharyngeal carcinoma (NPC) radiotherapy (RT), but practical constraints, such as patient discomfort, long scan times, and high costs often lead to incomplete modalities in clinical practice, compromising RT planning accuracy. Traditional MRI synthesis methods are modality-specific, limited in anatomical adaptability, and lack clinical interpretability-failing to meet NPC's RT needs. Here, we developed a unified foundation model integrating co...

</details>

---

### [Mimic Intent, Not Just Trajectories](https://arxiv.org/abs/2602.08602v1)

**Authors:** Renming Huang, Chendong Zeng, Wenjing Tang, Jingtian Cai, Cewu Lu et al. (6 authors)

**Published:** 2026-02-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.08602v1) | [PDF](https://arxiv.org/pdf/2602.08602v1.pdf)

<details>
<summary>Abstract</summary>

While imitation learning (IL) has achieved impressive success in dexterous manipulation through generative modeling and pretraining, state-of-the-art approaches like Vision-Language-Action (VLA) models still struggle with adaptation to environmental changes and skill transfer. We argue this stems from mimicking raw trajectories without understanding the underlying intent. To address this, we propose explicitly disentangling behavior intent from execution details in end-2-end IL: \textit{``Mimic ...

</details>

---

### [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167v1)

**Authors:** Milan Ganai, Katie Luo, Jonas Frey, Clark Barrett, Marco Pavone

**Published:** 2026-02-09 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.08167v1) | [PDF](https://arxiv.org/pdf/2602.08167v1.pdf)

<details>
<summary>Abstract</summary>

Embodied Chain-of-Thought (CoT) reasoning has significantly enhanced Vision-Language-Action (VLA) models, yet current methods rely on rigid templates to specify reasoning primitives (e.g., objects in the scene, high-level plans, structural affordances). These templates can force policies to process irrelevant information that distracts from critical action-prediction signals. This creates a bottleneck: without successful policies, we cannot verify reasoning quality; without quality reasoning, we...

</details>

---
