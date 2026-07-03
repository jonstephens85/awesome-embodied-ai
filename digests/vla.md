# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-03 22:54 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots](https://arxiv.org/abs/2607.02501v1)

**Authors:** Ling Xu, Chuyu Han, Borui Li, Hao Wu, Shiqi Jiang et al. (9 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.CV, cs.OS

**Links:** [arXiv](https://arxiv.org/abs/2607.02501v1) | [PDF](https://arxiv.org/pdf/2607.02501v1.pdf) | [GitHub](https://github.com/SEU-PAISys/Embodied.cpp)

<details>
<summary>Abstract</summary>

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on...

</details>

---

### [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658v1)

**Authors:** Yuguang Yang, Canyu Chen, Zhewen Tan, Yizhi Wang, Zichao Feng et al. (13 authors)

**Published:** 2026-07-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.01658v1) | [PDF](https://arxiv.org/pdf/2607.01658v1.pdf) | [GitHub](https://github.com/ShivaTeam/DriveTeach-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing VLAs' training relies heavily on text-centric visual question answering and chain-of-thought reasoning data, which emphasizes linguistic reasoning rather than action-grounded planning. As a result, the learned representations capture semantic knowledge but lack spatial dependencies crucial for reliable trajectory prediction. We propose DriveTeach-VLA, a framework that exp...

</details>

---

### [Bridge-WA: Predicting Where and How the World Changes for Robotic Action](https://arxiv.org/abs/2607.02195v1)

**Authors:** Yongjie Bai, Hanting Wang, Mingtong Dai, Qijun Zhong, Yang Liu et al. (6 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.02195v1) | [PDF](https://arxiv.org/pdf/2607.02195v1.pdf) | [Project Page](https://hcplab-sysu.github.io/BRIDGE-WA)

<details>
<summary>Abstract</summary>

General-purpose vision-language-action models benefit from large vision-language priors, but effective manipulation also requires anticipating action-relevant scene changes. Existing world-action models often rely on large generative world models or dense future rollouts, which are expensive and spend capacity on visual details weakly coupled to control. We present Bridge-WA, a lightweight world-action framework that distills a frozen future-change teacher into three compact priors: future token...

</details>

---

### [Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching](https://arxiv.org/abs/2607.01378v1)

**Authors:** William English, Hao Zheng, Rickard Ewetz

**Published:** 2026-07-01 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2607.01378v1) | [PDF](https://arxiv.org/pdf/2607.01378v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated promising generalization capabilities across robotic manipulation tasks, yet their real-world deployment remains limited by the lack of effective safety measures. Specifically, existing safety measures only prevent collisions caused by the robot's next action. In this paper, we propose a neuro-symbolic safety guidance mechanism for flow matching based VLAs that enables predictive collision avoidance. Flow matching based VLAs determine the nex...

</details>

---

### [FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model](https://arxiv.org/abs/2607.01212v1)

**Authors:** Chenyang Ma, Yue Yang, Radu Corcodel, Siddarth Jain, Andrew Wu et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.01212v1) | [PDF](https://arxiv.org/pdf/2607.01212v1.pdf) | [Project Page](https://dannymcy.github.io/furniturevla/)

<details>
<summary>Abstract</summary>

Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect high-quality real-world demonstrations. To address extreme long-h...

</details>

---

### [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678v1)

**Authors:** Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin et al. (21 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00678v1) | [PDF](https://arxiv.org/pdf/2607.00678v1.pdf) | [GitHub](https://github.com/amap-cvlab/ABot-Manipulation)

<details>
<summary>Abstract</summary>

Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...

</details>

---

### [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](https://arxiv.org/abs/2607.00666v1)

**Authors:** Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.00666v1) | [PDF](https://arxiv.org/pdf/2607.00666v1.pdf) | [Project Page](https://twkang43.github.io/projects/dart) | [GitHub](https://github.com/snumprlab/dart)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models often fail to perform the same learned tasks under environmental shifts, such as changes in camera pose and shifts to a different but similar robot (e.g., from Panda to UR5e). Adapting these models to the shifted environment (i.e., target domain) often requires training on multiple demonstrations for each task, which are costly to collect. To reduce the burden of data curation and training, we propose an analogy-based method that adapts VLA models under enviro...

</details>

---

## Other Recent Papers

### [Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs](https://arxiv.org/abs/2607.02466v1)

**Authors:** Junhao Shi, Siyin Wang, Xiaopeng Yu, Li Ji, Jingjing Gong et al. (6 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.02466v1) | [PDF](https://arxiv.org/pdf/2607.02466v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of expert demonstrations -- triplets of observations, instructions, and actions that are costly to collect at scale. We argue that this bottleneck stems from conflating two distinct learning objectives: acquiring physical competence (how to move) and acquiring semantic alignment (what to do). Crucially, only the latter requires language supervision. Building on this Decomposition Hypothesis, we propose Task-Agnost...

</details>

---

### [The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection](https://arxiv.org/abs/2607.02322v1)

**Authors:** Jincheng Tang, Yilong Zhu, Zhengyuan Xie, Jiang-Jiang Liu, Jiaxing Zhang

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.02322v1) | [PDF](https://arxiv.org/pdf/2607.02322v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown remarkable promise in generalized robotic manipulation. However, their spatial generalization remains fragile. We argue that simply increasing the number of viewpoints is insufficient. Models often fall into the trap of Shortcut Learning, latching onto spurious correlations (e.g., fixed relative poses between objects or between the camera and robot base) rather than learning true spatial relationships. In this work, we propose a data-centric solutio...

</details>

---

### [Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies](https://arxiv.org/abs/2607.02092v1)

**Authors:** Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.02092v1) | [PDF](https://arxiv.org/pdf/2607.02092v1.pdf)

<details>
<summary>Abstract</summary>

Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description feat...

</details>

---

### [VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon](https://arxiv.org/abs/2607.01804v1)

**Authors:** Yi Pan, Miao Pan, Qi Lu, Jiaming Huang, Man Zhang et al. (11 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.01804v1) | [PDF](https://arxiv.org/pdf/2607.01804v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) foundation models have recently achieved strong progress in embodied intelligence. To reduce policy-call frequency while preserving temporal coherence, most generative policies adopt an action chunk mechanism, executing multiple future actions in an open-loop manner under a fixed action horizon. However, this "predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-rich physical interactions, even small local perturbations can rapidly amp...

</details>

---

### [VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment](https://arxiv.org/abs/2607.01586v1)

**Authors:** Guoyang Xia, Fengfa Li, Hongjin Ji, Lei Ren, Fangxiang Feng et al. (7 authors)

**Published:** 2026-07-02 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.01586v1) | [PDF](https://arxiv.org/pdf/2607.01586v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet the effects of different robot-data pre-training paradigms remain difficult to compare because existing models often differ in architecture, data, action space, and evaluation protocol. We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching framework for controlled comparison of VLA training objectives. Using a heterogeneous robot corpus, OXEMix, containing approximately 5,000 hours of data f...

</details>

---

### [LIME: Learning Intent-aware Camera Motion from Egocentric Video](https://arxiv.org/abs/2607.02417v1)

**Authors:** Boyang Sun, Jiajie Li, Yung-Hsu Yang, Chenyangguang Zhang, Tim Engelbracht et al. (9 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.02417v1) | [PDF](https://arxiv.org/pdf/2607.02417v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous robots often need to move their camera before they can act: to inspect an object, reveal an occluded region, or obtain a view that responds to a user's intent. While vision-language navigation translates instructions to base motion and vision-language-action policies map instructions to manipulation actions, language-conditioned camera motion remains comparatively underexplored as a first-class action. We formulate language-conditioned camera motion generation: given a current RGB obs...

</details>

---

### [CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](https://arxiv.org/abs/2607.02222v1)

**Authors:** Haokun Liu, Zhaoqi Ma, Yicheng Chen, Wentao Zhang, Masaki Kitagawa et al. (8 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.02222v1) | [PDF](https://arxiv.org/pdf/2607.02222v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Navigation has increasingly emphasized high-level instruction reasoning, memory, global map construction, and instruction decomposition, while the low-level action representation remains comparatively underexplored. We propose CoFL-S, a low-level vision-language-action framework that predicts a language-conditioned flow field over the robot's local visible sector and generates continuous trajectories by rolling out the predicted field. To train this low-level representation, we c...

</details>

---

### [Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation](https://arxiv.org/abs/2607.01067v1)

**Authors:** Chi Zhang, Penglin Cai, Ziheng Xi, Haoqi Yuan, Hao Luo et al. (9 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.01067v1) | [PDF](https://arxiv.org/pdf/2607.01067v1.pdf)

<details>
<summary>Abstract</summary>

As an essential modality for dexterous and contact-rich tasks, tactile sensing provides precise force feedback that cannot be reliably inferred from vision. However, limited by hardware and data collection systems, existing datasets with tactility remain small in scale and narrow in contact coverage. Meanwhile, Vision-Language-Action (VLA) models with tactile modality are constrained on dynamics-agnostic post-training, which limits the performance ceiling on downstream tasks. In this paper, we p...

</details>

---

### [Unleashing More Actions via Action Compositional Training for VLA Models](https://arxiv.org/abs/2607.00351v1)

**Authors:** Kai Peng, Jie Lu, Xiaojiang Peng

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00351v1) | [PDF](https://arxiv.org/pdf/2607.00351v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models excel at robotic manipulation, driven by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this overfitting, acquiring high-quality robot data remains notoriously labor...

</details>

---
