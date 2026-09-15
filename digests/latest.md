# What's New

Papers discovered in the run at **2026-09-15 19:31 UTC**.

**New this run:** 25

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [WLA$^3$: World Latent Action Modeling for Semantics, Dynamics, and Kinematics](https://arxiv.org/abs/2609.15870)

**Authors:** Peidong Liu, Zhiyuan Xiang, Mingyang Li, Wenhao Li, Jiale Zhang et al. (7 authors)

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.15870) | [PDF](https://arxiv.org/pdf/2609.15870) | [Project Page](https://wla-3.github.io/)

<details>
<summary>Abstract</summary>

Scaling generalist policy models with heterogeneous data is limited by the lack of unified, low-noise action supervision. Human egocentric videos are abundant, but only a small fraction comes with high-quality hand-action labels. Observed world transitions offer a common source of action-related supervision across data sources. We introduce WLA$^3$ (World Latent Action Modeling for Semantics, Dynamics, and Kinematics), a unified generalist policy model framework built around representations learned by a World Latent Action Model (WLAM). WLAM first learns how multimodal world states change over...

</details>

<details>
<summary>Share</summary>

```
WLA$^3$: World Latent Action Modeling for Semantics, Dynamics, and Kinematics

Scaling generalist policy models with heterogeneous data is limited by the lack of unified, low-noise action supervision.

arXiv: https://arxiv.org/abs/2609.15870
Project page: https://wla-3.github.io/

#egocentric #robotlearning
```

</details>

---

### [Talking to Me or Someone Else? Rethinking Talk-to-Me Detection in Egocentric Videos](https://arxiv.org/abs/2609.14118)

**Authors:** Feiyu Du, Xi He, Jia Li, Yapeng Tian, Weili Wu

**Published:** 2026-09-12 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.14118) | [PDF](https://arxiv.org/pdf/2609.14118)

<details>
<summary>Abstract</summary>

Online understanding of who is talking to the camera wearer is a key capability for egocentric social interaction. However, existing talk-to-me (TTM) studies are commonly formulated as offline clip-level recognition, which is poorly aligned with online interaction and overlooks the diverse non-TTM speaking states that naturally arise in egocentric videos. In this paper, we revisit this problem by reformulating it as an online, frame-level prediction task. Instead of treating TTM as a binary problem against a single negative class, we model it in the presence of diverse and previously underexpl...

</details>

<details>
<summary>Share</summary>

```
Talking to Me or Someone Else? Rethinking Talk-to-Me Detection in Egocentric Videos

Online understanding of who is talking to the camera wearer is a key capability for egocentric social interaction.

arXiv: https://arxiv.org/abs/2609.14118

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (12)

### [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)

**Authors:** Xiao Liu, Haoyu Li, Jianghao Leng, Lin Wang, Chao Sun

**Published:** 2026-09-14 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.15169) | [PDF](https://arxiv.org/pdf/2609.15169) | [Code](https://github.com/AhernResearch/grava)

<details>
<summary>Abstract</summary>

Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior. We present GRAVA, a framework built around Grounded Reasoning-to-Action (GRA), which unifies grounding, reasoning, and action generation in a single autoregressive stream. GRA links action-relevant language references to 2D visual regions and ego-centric physical states, organizes object interactions and decisions in a trajectory-anchored typed graph, and serializes this structure into g...

</details>

<details>
<summary>Share</summary>

```
GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving

Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior.

arXiv: https://arxiv.org/abs/2609.15169
Code: https://github.com/AhernResearch/grava

#VLA #robotics
```

</details>

---

### [ReWeight: Leveraging Human Data for VLA Post-Training via Demonstration Retrieval and Sample Weighting](https://arxiv.org/abs/2609.13851)

**Authors:** Chenwei Wang, Dianye Huang, Match W. L. Ko, Chenjia Bai, Zhongliang Jiang

**Published:** 2026-09-12 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.13851) | [PDF](https://arxiv.org/pdf/2609.13851) | [Project Page](https://reweight-vla.github.io/)

<details>
<summary>Abstract</summary>

Post-training vision-language-action (VLA) models for specific robots and tasks requires in-domain demonstrations, yet collecting diverse robot data is costly. Egocentric human demonstrations provide a scalable alternative, but directly mixing human and robot data can introduce cross-embodiment discrepancies and degrade policy performance. To address this challenge, we introduce ReWeight, a framework that incorporates human data into VLA post-training through demonstration-level retrieval and sample-level weighting. ReWeight learns a cross-embodiment visuomotor representation that combines vis...

</details>

<details>
<summary>Share</summary>

```
ReWeight: Leveraging Human Data for VLA Post-Training via Demonstration Retrieval and Sample Weighting

Post-training vision-language-action (VLA) models for specific robots and tasks requires in-domain demonstrations, yet collecting diverse robot data is costly.

arXiv: https://arxiv.org/abs/2609.13851
Project page: https://reweight-vla.github.io/

#VLA #robotics
```

</details>

---

### [When Faster VLA Deployment Changes Closed-Loop Behavior: Task Success-Latency Analysis of SmolVLA Across PyTorch and ONNX Variants](https://arxiv.org/abs/2609.14146)

**Authors:** Rafiqul Islam

**Published:** 2026-09-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.14146) | [PDF](https://arxiv.org/pdf/2609.14146) | [Code](https://github.com/rafiqul713/smolvla-libero-onnx)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) deployment can reduce inference latency while changing closed-loop task behavior. We evaluate HuggingFaceVLA/smolvla_libero on an RTX 2060 (6 GB) in LIBERO Spatial and Object (MuJoCo 3.3.2, LeRobot 0.6.1, seed 42), comparing PyTorch+AMP with ONNX Runtime CUDA Execution Provider (CUDA EP). The main evaluation uses 100 episodes/suite; a paired rollout uses 300 episodes/suite. PyTorch+AMP reaches 70.0%/88.0% Spatial/Object success at 1181 ms p99. Requested-FP16 and requested-INT8 ONNX reduce tether-inspect p99 to 601 ms and 532 ms, while Spatial success falls to 41.0%...

</details>

<details>
<summary>Share</summary>

```
When Faster VLA Deployment Changes Closed-Loop Behavior: Task Success-Latency Analysis of SmolVLA Across PyTorch and ONNX Variants

Vision-language-action (VLA) deployment can reduce inference latency while changing closed-loop task behavior.

arXiv: https://arxiv.org/abs/2609.14146
Code: https://github.com/rafiqul713/smolvla-libero-onnx

#VLA #robotics
```

</details>

---

### [GROOVE: Geometry-Guided Reduction of Operational-Space Jerk in VLA Execution](https://arxiv.org/abs/2609.13695)

**Authors:** Sangho Yun, Minsoo Kim, Minwoo Cho, Hwanjo Yu

**Published:** 2026-09-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.13695) | [PDF](https://arxiv.org/pdf/2609.13695) | [Project Page](https://devsangho.github.io/GROOVE-public/)

<details>
<summary>Abstract</summary>

Chunked vision language action (VLA) policies execute several commands per query, but jerk within chunks and across replanning boundaries can induce oscillatory motion and sharp actuator transients. We present GROOVE, an online regulator that searches directional correction regions around the raw three dimensional end effector (EEF) path, without retraining or additional VLA inference. It optimizes the new chunk using delivered commands as boundary conditions, reducing boundary and within chunk jerk while bounding cumulative translation and local axis angle deviation from the raw plan after ev...

</details>

<details>
<summary>Share</summary>

```
GROOVE: Geometry-Guided Reduction of Operational-Space Jerk in VLA Execution

Chunked vision language action (VLA) policies execute several commands per query, but jerk within chunks and across replanning boundaries can induce oscillatory motion and sharp actuator transients.

arXiv: https://arxiv.org/abs/2609.13695
Project page: https://devsangho.github.io/GROOVE-public/

#VLA #robotics
```

</details>

---

### [IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies](https://arxiv.org/abs/2609.15005)

**Authors:** Jinwoong Kim, Sangjin Park

**Published:** 2026-09-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15005) | [PDF](https://arxiv.org/pdf/2609.15005)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies perform robot manipulation tasks using multimodal inputs such as visual observations, proprioceptive states, and language instructions. However, it remains unclear at which execution stages each modality contributes to final task success and how input interventions propagate through subsequent states, observations, and actions. Existing attribution approaches primarily measure local sensitivity or temporally aggregated importance, limiting their ability to capture phase-dependent contributions and cross-phase dependencies. We propose Interaction-aware Mult...

</details>

<details>
<summary>Share</summary>

```
IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

Vision-Language-Action (VLA) policies perform robot manipulation tasks using multimodal inputs such as visual observations, proprioceptive states, and language instructions.

arXiv: https://arxiv.org/abs/2609.15005

#VLA #robotics
```

</details>

---

### [Visible Touch: Rendering Contact for Visuomotor Policies](https://arxiv.org/abs/2609.14156)

**Authors:** Metin Alp Dogan, Edward Sun, Feng Xu, Daniel Wu, Allen Peng et al. (7 authors)

**Published:** 2026-09-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.14156) | [PDF](https://arxiv.org/pdf/2609.14156) | [Project Page](https://visibletouch.github.io/)

<details>
<summary>Abstract</summary>

Integrating contact information into visuomotor policies remains an open problem. Touch is essential to robust manipulation, yet most modern policies, including pretrained vision-language-action (VLA) models, operate from vision and proprioception alone. Existing approaches to closing this gap require specialized tactile hardware, add separate tactile encoders, or commit to non-image policy backbones, all incompatible with the modern paradigm of image-conditioned policies built on pretrained 2D visual representations. Our key insight is that the bottleneck is not the contact information itself...

</details>

<details>
<summary>Share</summary>

```
Visible Touch: Rendering Contact for Visuomotor Policies

Integrating contact information into visuomotor policies remains an open problem.

arXiv: https://arxiv.org/abs/2609.14156
Project page: https://visibletouch.github.io/

#VLA #robotics
```

</details>

---

### [GeomVLA: Unifying Scene, Motion, and Action in 3D](https://arxiv.org/abs/2609.13812)

**Authors:** Ziyin Xiong, Nikos Gkanatsios, Moritz Reuss, Katerina Fragkiadaki

**Published:** 2026-09-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.13812) | [PDF](https://arxiv.org/pdf/2609.13812) | [Project Page](https://ziyin-xiong.github.io/geomvla.io/)

<details>
<summary>Abstract</summary>

We present GeomVLA, a Vision-Language-Action (VLA) model that unifies perception, latent scene motion prediction, and action generation within a shared robot-centric 3D coordinate frame. Our approach lifts pretrained VLM features into spatially grounded 3D scene tokens using depth and camera calibration, while retaining the semantic representations learned during VLM pretraining. We further introduce a 3D Scene Trajectory Denoiser, a task-conditioned module that learns a latent representation of how scene points are expected to move in 3D. Rather than executing the predicted trajectory as an o...

</details>

<details>
<summary>Share</summary>

```
GeomVLA: Unifying Scene, Motion, and Action in 3D

We present GeomVLA, a Vision-Language-Action (VLA) model that unifies perception, latent scene motion prediction, and action generation within a shared robot-centric 3D coordinate frame.

arXiv: https://arxiv.org/abs/2609.13812
Project page: https://ziyin-xiong.github.io/geomvla.io/

#VLA #robotics
```

</details>

---

### [How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026](https://arxiv.org/abs/2609.13679)

**Authors:** Jiaming Wang, Jizhuo Chen, Diwen Liu, Wang Song, Qiang Wang et al. (14 authors)

**Published:** 2026-09-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.13679) | [PDF](https://arxiv.org/pdf/2609.13679)

<details>
<summary>Abstract</summary>

How can robot policies learn more effectively from a fixed demonstration budget? The first Real-world Embodied AI Learning (REAL-I) Challenge at ICRA 2026 examined this question through simulation, real-robot evaluation, and an on-site final on a shared dual-arm humanoid platform. We describe the challenge tasks, data and deployment interfaces, and competition results, then compare the approaches contributed by NUS-CLEAR, RCL-Lab, and Deeptouch.ai. Their systems combined pretrained vision-language-action models and task-specific imitation policies with different strategies for data curation, s...

</details>

<details>
<summary>Share</summary>

```
How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026

How can robot policies learn more effectively from a fixed demonstration budget?

arXiv: https://arxiv.org/abs/2609.13679

#VLA #robotics
```

</details>

---

### [Beyond Single-Axis Testing: Paired Evaluation of Compound Robustness in Vision-Language-Action Policies](https://arxiv.org/abs/2609.15940)

**Authors:** Hiroki Sawada, Shunichi Kasahara

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15940) | [PDF](https://arxiv.org/pdf/2609.15940)

<details>
<summary>Abstract</summary>

Vision-language-action policies are typically evaluated one perturbation at a time, providing a useful diagnosis of their sensitivity to individual distribution shifts. Real-world deployment, however, may involve several shifts simultaneously, and it remains unclear how these individual robustness measurements compose. We ask whether compound robustness can be inferred from single-axis evaluations. We introduce LIBERO-CTRL, a six-axis benchmark that pairs each initial state across single-axis conditions and a matched simultaneous condition. This design reveals two opposing outcome changes that...

</details>

<details>
<summary>Share</summary>

```
Beyond Single-Axis Testing: Paired Evaluation of Compound Robustness in Vision-Language-Action Policies

Vision-language-action policies are typically evaluated one perturbation at a time, providing a useful diagnosis of their sensitivity to individual distribution shifts.

arXiv: https://arxiv.org/abs/2609.15940

#VLA #robotics
```

</details>

---

### [Task-Specified Active Metrological Inspection with Measurement-Steered VLA Manipulation and Deterministic Evidence Gating](https://arxiv.org/abs/2609.14219)

**Authors:** Zhiling Chen, Jingzhan Ge, Ruimin Chen, Matthew P. Castanier, David Gorsich et al. (6 authors)

**Published:** 2026-09-13 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.14219) | [PDF](https://arxiv.org/pdf/2609.14219)

<details>
<summary>Abstract</summary>

High-mix low-volume (HMLV) manufacturing requires inspection systems to adapt to changing parts, specifications, and work orders without repeated task-specific programming. Existing inspection automation typically assumes predefined sensing sequences, while general purpose robot agents optimize task completion rather than the completeness and validity of metrological evidence. We formulate task-specified active metrological inspection and propose From Requirements to Admissible Metrological Evidence (FRAME), a hierarchical dual-arm framework that converts an inspection instruction and structur...

</details>

<details>
<summary>Share</summary>

```
Task-Specified Active Metrological Inspection with Measurement-Steered VLA Manipulation and Deterministic Evidence Gating

High-mix low-volume (HMLV) manufacturing requires inspection systems to adapt to changing parts, specifications, and work orders without repeated task-specific programming.

arXiv: https://arxiv.org/abs/2609.14219

#VLA #robotics
```

</details>

---

### [What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency](https://arxiv.org/abs/2609.13984)

**Authors:** Luoyang Sun, Guoyang Xia, Fengfa Li, Lei Ren, Xinyu Cui et al. (12 authors)

**Published:** 2026-09-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.13984) | [PDF](https://arxiv.org/pdf/2609.13984)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models combine a pretrained vision encoder, a language backbone, and an action head, but their relative contribution has not been established under controlled, latency-paired conditions. We fix the backbone families (SigLIP2 and Qwen2.5) and the training pipeline, sweep action-head design and module scale, and pair each configuration with measured on-device latency. The study yields three findings. First, action-head performance is governed primarily by initialization rather than decoder architecture, loss, or inference budget: copying the last transformer layers o...

</details>

<details>
<summary>Share</summary>

```
What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency

Vision-Language-Action (VLA) models combine a pretrained vision encoder, a language backbone, and an action head, but their relative contribution has not been established under controlled, latency-paired conditions.

arXiv: https://arxiv.org/abs/2609.13984

#VLA #robotics
```

</details>

---

### [Atomic Motion Coordinate for Language-Steerable and Force-Responsive Manipulation](https://arxiv.org/abs/2609.15012)

**Authors:** Jiaqi Zhai, Jingkai Zhao, Chen Yang, Siyuan Ma, Yutian Zhang et al. (13 authors)

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15012) | [PDF](https://arxiv.org/pdf/2609.15012)

<details>
<summary>Abstract</summary>

Can changing only the language instruction redirect a VLA policy's end effector, or does the visually driven motion prior dominate? We present Atomic Motion Coordinate, a geometry-grounded coordinate for steerable and force-responsive manipulation. Each arm owns thirteen signed translation, rotation, and hold atoms grounded from text and forward kinematics with vision withheld, and the coordinate is injected into every action-expert block via weighted codebook alignment. Contact history modulates the same coordinate through a bounded spherical residual that is recomputed from a fixed nominal l...

</details>

<details>
<summary>Share</summary>

```
Atomic Motion Coordinate for Language-Steerable and Force-Responsive Manipulation

Can changing only the language instruction redirect a VLA policy's end effector, or does the visually driven motion prior dominate?

arXiv: https://arxiv.org/abs/2609.15012

#VLA #robotics
```

</details>

---

## World Models (11)

### [LPA-CWM: A Learned Physical Adjudicator for Motion Reasoning with Counterfactual World Models](https://arxiv.org/abs/2609.14073)

**Authors:** Kunwei Wu, Xiang Liu, Guocai Yao, Junming Chen, Zhikang Chen et al. (8 authors)

**Published:** 2026-09-12 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.14073) | [PDF](https://arxiv.org/pdf/2609.14073) | [Project Page](https://LPA-CWM.github.io)

<details>
<summary>Abstract</summary>

Counterfactual world models (CWM) extract motion from pretrained video predictors by comparing factual and intervened predictions. However, responses generated under different target-frame masks vary in reliability, while uniform aggregation weights them equally. We formulate response aggregation as candidate reliability learning and propose LPA-CWM with a lightweight Learned Physical Adjudicator (LPA). Trained on dense MOVi-F trajectories, the 3.0M-parameter LPA compares visual context and response structure across an unordered candidate set to predict relative weights, while the CWM predicto...

</details>

<details>
<summary>Share</summary>

```
LPA-CWM: A Learned Physical Adjudicator for Motion Reasoning with Counterfactual World Models

Counterfactual world models (CWM) extract motion from pretrained video predictors by comparing factual and intervened predictions.

arXiv: https://arxiv.org/abs/2609.14073
Project page: https://LPA-CWM.github.io

#worldmodels #robotics
```

</details>

---

### [JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion](https://arxiv.org/abs/2609.15770)

**Authors:** Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.15770) | [PDF](https://arxiv.org/pdf/2609.15770) | [Code](https://github.com/ASIG-X/JEPLO)

<details>
<summary>Abstract</summary>

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots. We introduce a proprio-exteroceptive JEPA (PE-JEPA) world model to learn predictive egocentric terrain representations from onboard observations, including raw LiDAR scans. A concurrent JEPA-teacher-student (CJTS) pipeline is further prop...

</details>

<details>
<summary>Share</summary>

```
JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping.

arXiv: https://arxiv.org/abs/2609.15770
Code: https://github.com/ASIG-X/JEPLO

#worldmodels #robotics
```

</details>

---

### [Legislating World-Model-Based Planning with Legal Reasoning](https://arxiv.org/abs/2609.15113)

**Authors:** Dylan Waldner, Yiannis Kantaros, Guido Governatori, Risto Miikkulainen, Amir Banifatemi

**Published:** 2026-09-14 | **Categories:** cs.RO, cs.AI, cs.LO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15113) | [PDF](https://arxiv.org/pdf/2609.15113)

<details>
<summary>Abstract</summary>

As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The paper introduces a legal planning stack that employs Defeasible Deontic Logic (DDL) to constrain a mo...

</details>

<details>
<summary>Share</summary>

```
Legislating World-Model-Based Planning with Legal Reasoning

As robotic systems grow more general, legal norms are needed to integrate them into society.

arXiv: https://arxiv.org/abs/2609.15113

#worldmodels #robotics
```

</details>

---

### [GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation](https://arxiv.org/abs/2609.14561)

**Authors:** I-Tak Ieong, Ruizhi Feng, Zhaoyang Lu, Yifei Cao, Jiayao Zhao et al. (8 authors)

**Published:** 2026-09-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.14561) | [PDF](https://arxiv.org/pdf/2609.14561)

<details>
<summary>Abstract</summary>

Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that prediction into actionable plans. We present GLAM, a goal-conditioned latent world model trained over global spatiotemporal memory, and GLAM NAV, the complete navigation system built around it. Given historical map tokens, a navigation goal, and the current robot pose, GLAM jointly predicts future map representations and robot-centric waypoint latents, allowing future spatial context and...

</details>

<details>
<summary>Share</summary>

```
GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation

Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that predicti...

arXiv: https://arxiv.org/abs/2609.14561

#worldmodels #robotics
```

</details>

---

### [From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation](https://arxiv.org/abs/2609.15382)

**Authors:** Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu et al. (6 authors)

**Published:** 2026-09-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15382) | [PDF](https://arxiv.org/pdf/2609.15382)

<details>
<summary>Abstract</summary>

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions. A practical world model must predict action consequences accurately, rank candidates in real time, and operate inside the closed loop of a full-size machine. We present the World-Action Model (WAM), which proposes multiple scoops, rejects geometrically inadmissible candidates, jointly predicts signed terrain change and loaded volume, executes the candidate with the largest predicted load, and replans from the newly observed terrain. On 32 geometry-disjoint MinSlope...

</details>

<details>
<summary>Share</summary>

```
From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions.

arXiv: https://arxiv.org/abs/2609.15382

#worldmodels #robotics
```

</details>

---

### [When Should a World Model Move? Loss-Conditioned State Execution](https://arxiv.org/abs/2609.15801)

**Authors:** Jintao Xu, Zhengyu Chen, Ben Zhang, Yongzhi Qi, Jianshen Zhang

**Published:** 2026-09-14 | **Categories:** cs.AI, cs.LG, math.OC | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15801) | [PDF](https://arxiv.org/pdf/2609.15801)

<details>
<summary>Abstract</summary>

We introduce loss-conditioned state execution, a model-agnostic method that decides whether to execute a world model's fixed feasible proposal or retain the current state. Predictive informativeness alone, however, does not establish whether an update will reduce downstream loss. Occurrence ranking can approach perfection while persistence remains the unique absolute-loss Bayes action. Two transition laws can also share occurrence information and conditional variance yet require opposite absolute-loss decisions. We formalize state movability as the existence of a loss-reducing feasible correct...

</details>

<details>
<summary>Share</summary>

```
When Should a World Model Move? Loss-Conditioned State Execution

We introduce loss-conditioned state execution, a model-agnostic method that decides whether to execute a world model's fixed feasible proposal or retain the current state.

arXiv: https://arxiv.org/abs/2609.15801

#worldmodels #robotics
```

</details>

---

### [When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control](https://arxiv.org/abs/2609.15781)

**Authors:** Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta

**Published:** 2026-09-14 | **Categories:** cs.CR, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15781) | [PDF](https://arxiv.org/pdf/2609.15781)

<details>
<summary>Abstract</summary>

Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees the trigger. The attack encodes no explicit trigger-to-action rule. Instead, the poisoned model rout...

</details>

<details>
<summary>Share</summary>

```
When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control

Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pre...

arXiv: https://arxiv.org/abs/2609.15781

#worldmodels #robotics
```

</details>

---

### [One Model, Two Physical Stories: Auditing Misalignment in Multi-Modal World Modeling](https://arxiv.org/abs/2609.14833)

**Authors:** Geigh Zollicoffer, Minh Vu, Rajiv Ranasinghe, Manish Bhattarai

**Published:** 2026-09-13 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.14833) | [PDF](https://arxiv.org/pdf/2609.14833)

<details>
<summary>Abstract</summary>

World models, systems that generate what happens next given current environmental conditions, are increasingly being implemented with multi-modal generation in mind. However, generating multiple modalities simultaneously, such as visual simulations alongside physical state predictions in the form of text, introduces the risk of cross-modal inconsistency. Tested separately, both outputs may look convincing while still disagreeing: a model can calculate that a ball should rebound in one modality, then generate no rebound in another modality, to say nothing of diverging from real-world dynamics e...

</details>

<details>
<summary>Share</summary>

```
One Model, Two Physical Stories: Auditing Misalignment in Multi-Modal World Modeling

World models, systems that generate what happens next given current environmental conditions, are increasingly being implemented with multi-modal generation in mind.

arXiv: https://arxiv.org/abs/2609.14833

#worldmodels #robotics
```

</details>

---

### [LePlanner: An Iterative Amortized Controller For World Models](https://arxiv.org/abs/2609.13845)

**Authors:** Saksham Bansal, Om Naphade, Chayan Aggarwal, Vrishin M

**Published:** 2026-09-12 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.13845) | [PDF](https://arxiv.org/pdf/2609.13845)

<details>
<summary>Abstract</summary>

World models trained with joint-embedding predictive architectures learn compact, structured latent representations from physical interaction, yet planning in these latent spaces typically relies on one of two costly approaches. Search-based planners such as CEM, MPPI, and iCEM optimize action sequences through many predictor rollouts, achieving strong performance at the cost of high per-decision compute and latency. Policy-based methods amortize inference into a single forward pass but can degrade on contact-rich tasks where the demonstration distribution is multimodal. We propose LePlanner,...

</details>

<details>
<summary>Share</summary>

```
LePlanner: An Iterative Amortized Controller For World Models

World models trained with joint-embedding predictive architectures learn compact, structured latent representations from physical interaction, yet planning in these latent spaces typically relies on one of two costly...

arXiv: https://arxiv.org/abs/2609.13845

#worldmodels #robotics
```

</details>

---

### [Math for AI safety: an invitation for mathematicians](https://arxiv.org/abs/2609.15289)

**Authors:** Lionel Levine

**Published:** 2026-09-14 | **Categories:** math.HO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.15289) | [PDF](https://arxiv.org/pdf/2609.15289)

<details>
<summary>Abstract</summary>

Artificial intelligence threatens to outrun human understanding and control. New mathematics is needed to design AI that is legible, steerable, and cooperative with humanity. I organize this invitation by mathematical field, so you can turn straight to your own: logic and game theory for cooperation; probability for agency and world-models; algebra and representation theory for learned features; analysis and geometry for generalization and training dynamics. Each section ends with an open problem that is accessible to a working mathematician with no prior experience in AI safety.

</details>

<details>
<summary>Share</summary>

```
Math for AI safety: an invitation for mathematicians

Artificial intelligence threatens to outrun human understanding and control.

arXiv: https://arxiv.org/abs/2609.15289

#worldmodels #robotics
```

</details>

---

### [Exploring napping paradigm for Recurrent Spiking Neural Networks](https://arxiv.org/abs/2609.13927)

**Authors:** Andreas Massey, Stefano Nichele, Aliaksandr Hubin

**Published:** 2026-09-12 | **Categories:** cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.13927) | [PDF](https://arxiv.org/pdf/2609.13927)

<details>
<summary>Abstract</summary>

Biological organisms minimize free energy by balancing two competing demands on their internal world model: it must be accurate enough to predict sensory input, yet simple enough to generalize beyond it. Two mechanisms regulate this balance offline: sleep reduces complexity through gradual synaptic downscaling, while stochastic noise attenuates precision, relaxing the constraint sensory input imposes on synaptic reorganization. Engineered Spiking Neural Networks (SNNs) leave this balance unaddressed, favoring instantaneous, noiseless weight normalization instead. This paper investigates the hy...

</details>

<details>
<summary>Share</summary>

```
Exploring napping paradigm for Recurrent Spiking Neural Networks

Biological organisms minimize free energy by balancing two competing demands on their internal world model: it must be accurate enough to predict sensory input, yet simple enough to generalize beyond it.

arXiv: https://arxiv.org/abs/2609.13927

#worldmodels #robotics
```

</details>

---
