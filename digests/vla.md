# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-09-15 23:49 UTC

**Papers shown:** 37 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](https://arxiv.org/abs/2609.09119)

**Authors:** Yankai Fu, Ning Chen, Junkai Zhao, Heng Zhang, Guocai Yao et al. (8 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.09119) | [PDF](https://arxiv.org/pdf/2609.09119) | [Project Page](https://aureleopku.github.io/DeCAL)

<details>
<summary>Abstract</summary>

Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and complex contact dynamics. While recent works have incorporated tactile sensing into robotic manipulation, most approaches still rely on homogeneous multimodal fusion, lacking adaptive tactile integration and explicit modeling of physical dynamics. In this work, we present DeCAL, a physically-grounded dexterous vision-language-action model that unifies understanding, imagination and...

</details>

<details>
<summary>Share</summary>

```
DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination

Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and co...

arXiv: https://arxiv.org/abs/2609.09119
Project page: https://aureleopku.github.io/DeCAL

#VLA #robotics
```

</details>

---

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

### [IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2609.10915)

**Authors:** Kian Hosseinkhani, Qinhe Peng, George Shramko, Mehran Aghabozorgi, Jianing Qian et al. (9 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10915) | [PDF](https://arxiv.org/pdf/2609.10915) | [Project Page](https://kianhk6.github.io/IMLE-VLA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization. A leading design couples this backbone with a dedicated continuous action head trained via diffusion or flow matching. However, such heads rely on iterative multi-step sampling, for example 10 Euler steps in $π_{0.5}$. This creates an inference bottleneck that produces stop-and-go movement in the robot and slower task completion. We introduce IMLE-VLA, which replaces the iterative action head with a single-step conditional generator trained via conditional Implicit M...

</details>

<details>
<summary>Share</summary>

```
IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies

Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization.

arXiv: https://arxiv.org/abs/2609.10915
Project page: https://kianhk6.github.io/IMLE-VLA/

#VLA #robotics
```

</details>

---

### [HuRo: Robotizing Human Videos for Scalable VLA Pretraining](https://arxiv.org/abs/2609.10706)

**Authors:** Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim et al. (7 authors)

**Published:** 2026-09-09 (updated 2026-09-11) | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10706) | [PDF](https://arxiv.org/pdf/2609.10706) | [Project Page](https://3587jjh.github.io/HuRo)

<details>
<summary>Abstract</summary>

Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale. To bridge the human-to-robot embodiment gap, existing approaches either robotize videos in task-matched settings or address observation and action alignment separately at scale. In this work, we systematically examine whether robotized human videos can provide effective and scalable supervision for pretraining vision-language-action (VLA) policies. To this end, we develop a robotization pipeline that converts heterogeneous human videos into robot-aligned observations an...

</details>

<details>
<summary>Share</summary>

```
HuRo: Robotizing Human Videos for Scalable VLA Pretraining

Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale.

arXiv: https://arxiv.org/abs/2609.10706
Project page: https://3587jjh.github.io/HuRo

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

### [DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2609.12316)

**Authors:** Samrat Sahoo, Yixuan Huang, Tom Silver

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12316) | [PDF](https://arxiv.org/pdf/2609.12316)

<details>
<summary>Abstract</summary>

Collecting high-quality robot data remains a fundamental challenge for training robot foundation models. Task and motion planning (TAMP) offers a scalable way to generate demonstrations, but our experiments show that raw TAMP trajectories provide surprisingly little benefit when used to fine-tune pretrained vision-language-action (VLA) models, despite successfully solving the target tasks. We hypothesize that this failure arises from a behavioral distribution mismatch between planner-generated trajectories and the data used to pretrain the VLA. To address this mismatch, we introduce DATAFARM:...

</details>

<details>
<summary>Share</summary>

```
DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models

Collecting high-quality robot data remains a fundamental challenge for training robot foundation models.

arXiv: https://arxiv.org/abs/2609.12316

#VLA #robotics
```

</details>

---

### [UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling](https://arxiv.org/abs/2609.11875)

**Authors:** Wei Li, Rui Shao, Jie He, Lingsen Zhang, Ziwei Liu et al. (6 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.11875) | [PDF](https://arxiv.org/pdf/2609.11875) | [Project Page](https://JiuTian-VL.github.io/UniMPA-page/)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have improved robotic manipulation, yet observation-to-action learning remains limited by a fundamental transition realizability gap, manifested in three tightly coupled problems: (i) Transition ambiguity. Visually similar current observations may correspond to different manipulation phases and imply different subsequent transitions. (ii) Prediction--execution mismatch. A visually plausible predicted future observation does not necessarily correspond to a physically realizable transition. (iii) Experience--realization mismatch. A historica...

</details>

<details>
<summary>Share</summary>

```
UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling

Recent advances in Vision-Language-Action (VLA) models have improved robotic manipulation, yet observation-to-action learning remains limited by a fundamental transition realizability gap, manifested in three tightly...

arXiv: https://arxiv.org/abs/2609.11875
Project page: https://JiuTian-VL.github.io/UniMPA-page/

#VLA #robotics
```

</details>

---

### [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2609.10405)

**Authors:** Haochen Niu, Shengye Dong, Hao Liu, Peiwen Lin, Wang Chuang

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.10405) | [PDF](https://arxiv.org/pdf/2609.10405)

<details>
<summary>Abstract</summary>

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions. Yet Flow Matching--based vision-language-action (VLA) models typically generate actions in temporal coordinates, without explicitly modeling or systematically leveraging this frequency heterogeneity. We introduce \emph{FreqFM}, a frequency-conditioned Flow Matching framework for VLA models. It raises action frequency from an implicit trajectory property to an explicit conditioning dimension that spans the entire generation pipeline. Con...

</details>

<details>
<summary>Share</summary>

```
Frequency-Conditioned Flow Matching for Vision-Language-Action Models

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions.

arXiv: https://arxiv.org/abs/2609.10405

#VLA #robotics
```

</details>

---

### [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925)

**Authors:** Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang et al. (6 authors)

**Published:** 2026-09-09 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.09925) | [PDF](https://arxiv.org/pdf/2609.09925)

<details>
<summary>Abstract</summary>

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entangles them. Second, cross-phase geometry: motions of different phases (reach, contact, grasp adjustme...

</details>

<details>
<summary>Share</summary>

```
Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass.

arXiv: https://arxiv.org/abs/2609.09925

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

### [READ: Learning Risk-Informed Fields for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.12371)

**Authors:** Zhiyuan Liu, Yuanxin Tian, Zehong Ke, Jinhao Li, Hao Cheng et al. (8 authors)

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12371) | [PDF](https://arxiv.org/pdf/2609.12371)

<details>
<summary>Abstract</summary>

Autonomous driving requires more than recognizing what is present in a scene: a planner must determine how road structure, surrounding agents, and their motion states should influence a future maneuver. Existing learning-based planners can capture these influences through latent scene features and trajectory decoders, but the relationship between environmental factors and candidate actions often remains implicit. This limits the ability to inspect, diagnose, or refine how scene context affects the safety of a predicted trajectory. Classical safety fields provide an explicit spatial representat...

</details>

<details>
<summary>Share</summary>

```
READ: Learning Risk-Informed Fields for End-to-End Autonomous Driving

Autonomous driving requires more than recognizing what is present in a scene: a planner must determine how road structure, surrounding agents, and their motion states should influence a future maneuver.

arXiv: https://arxiv.org/abs/2609.12371

#VLA #robotics
```

</details>

---

### [Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model](https://arxiv.org/abs/2609.13053)

**Authors:** Hoeun Lee, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi et al. (7 authors)

**Published:** 2026-09-11 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.13053) | [PDF](https://arxiv.org/pdf/2609.13053)

<details>
<summary>Abstract</summary>

Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes. We bring these predictions into action generation and selection through a shared trajectory model. Dynin-Robotics implements this formulation on Dynin-Omni, an omnimodal masked-diffusion backbone, representing language, visual observations, goals, and actions as discrete tokens. By varying conditioning and target spans, the same model learns action prediction, action-conditioned next-observation prediction, terminal goal-state pr...

</details>

<details>
<summary>Share</summary>

```
Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model

Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes.

arXiv: https://arxiv.org/abs/2609.13053

#VLA #robotics
```

</details>

---

### [Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641)

**Authors:** Jianman Lin, Shailesh Shailesh, Zhongyi Luo, Jiafei Duan

**Published:** 2026-09-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.12641) | [PDF](https://arxiv.org/pdf/2609.12641) | [Project Page](https://magiclab-nus.github.io/LIT/?v=37955c5)

<details>
<summary>Abstract</summary>

Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine generalization when these correlations change under distribution shifts. Mitigating these shortcuts requires constraining how visual information is used for action generation while preserving task-relevant spatial information. We propose Late...

</details>

<details>
<summary>Share</summary>

```
Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts.

arXiv: https://arxiv.org/abs/2609.12641
Project page: https://magiclab-nus.github.io/LIT/?v=37955c5

#VLA #robotics
```

</details>

---

### [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)

**Authors:** Dionysios Adamopoulos, Nattapol Chanpaisit, Basel Fakhri, Christina Giannoula

**Published:** 2026-09-10 | **Categories:** cs.DC, cs.AR, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.12075) | [PDF](https://arxiv.org/pdf/2609.12075)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage. Since robots must meet strict Service-Level Objectives (SLOs) for safety, VLA inference is inherently latency-critical. Meeting these SLOs requires high-end GPUs, yet weight, cost, and power constraints preclude integrating such GPUs on-robot. Prior works offload VLA inference to edge servers that serve many robots on VLA models. However, current VLA systems lack support for multi-request, multi-mod...

</details>

<details>
<summary>Share</summary>

```
Efficient Vision-Language-Action Management and Serving for Robot Factories

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage.

arXiv: https://arxiv.org/abs/2609.12075

#VLA #robotics
```

</details>

---

### [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)

**Authors:** Yanzhe Chen, Zechen Bai, Zhijun Cao, Wenzheng Zeng, Kevin Qinghong Lin et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10522) | [PDF](https://arxiv.org/pdf/2609.10522) | [Project Page](https://showlab.github.io/Show-Harness)

<details>
<summary>Abstract</summary>

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging. We present Show-Harness, an Embodied Harness that enables VLMs to "play" robots through a compact semantic interface linking intent to action. Show-Harness exposes discrete semantic action units that VLMs can naturally reason over, while embodiment-specific interpreters deterministically ground them into local robot actions, keeping the VLM directly responsible for fine-grained physical decisions. Through the same interface, Show-Harness...

</details>

<details>
<summary>Share</summary>

```
Show-Harness: Just a VLM Agent Can Play Robots

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging.

arXiv: https://arxiv.org/abs/2609.10522
Project page: https://showlab.github.io/Show-Harness

#VLA #robotics
```

</details>

---

### [RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility](https://arxiv.org/abs/2609.10021)

**Authors:** Runze Xu, Yuanfan Xu, Cuijie Xu, Shuang Dai, Yining Li et al. (7 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.10021) | [PDF](https://arxiv.org/pdf/2609.10021)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data. Unlike pretraining, post-training targets task- and embodiment-specific adaptation, making it particularly sensitive to data quality. In practice, collected robot datasets often contain heterogeneous errors, including execution mistakes, sensor drift, and timestamp misalignment, which can impair post-training and policy performance. Manual inspection is costly, while existing data-cleaning...

</details>

<details>
<summary>Share</summary>

```
RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data.

arXiv: https://arxiv.org/abs/2609.10021

#VLA #robotics
```

</details>

---

### [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808)

**Authors:** M. Yunus Seker, Shobhit Aggarwal, Ruwan Wickramarachchi, Jonathan Francis, Oliver Kroemer

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.09808) | [PDF](https://arxiv.org/pdf/2609.09808) | [Project Page](https://gta2-project.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation tasks are often decomposed into behaviors or skills. However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills. As a result, these behaviors can remain too coarse to expose the geometric, control, and scene-dependent decisions required for execution. We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable object-centric task-axis components. Rather than predicting actions end-to-end or composing fixed task-le...

</details>

<details>
<summary>Share</summary>

```
GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes

Robotic manipulation tasks are often decomposed into behaviors or skills.

arXiv: https://arxiv.org/abs/2609.09808
Project page: https://gta2-project.github.io/

#VLA #robotics
```

</details>

---

### [3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints](https://arxiv.org/abs/2609.08224)

**Authors:** Ziqin Huang, Yingyue Li, Chenyangguang Zhang, Ruida Zhang, Yuxin Chen et al. (9 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.08224) | [PDF](https://arxiv.org/pdf/2609.08224) | [Code](https://github.com/ziqin-h/3DWay)

<details>
<summary>Abstract</summary>

Intermediate representations are key to bridging the modality gap between generalizable manipulation policies and large-scale pretrained vision-language models (VLMs). Among these, trajectory-based representations compactly represent motion-relevant cues, yet most existing approaches predict trajectories in 2D image space, resulting in intrinsic 3D ambiguity. Moreover, using 2D trajectories with depth still leaves the free-space waypoints ambiguous, limiting reliable 3D reasoning. To address this, we propose predicting 3D consistent waypoints (3DWay) from multi-view images. By reformulating 3D...

</details>

<details>
<summary>Share</summary>

```
3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints

Intermediate representations are key to bridging the modality gap between generalizable manipulation policies and large-scale pretrained vision-language models (VLMs).

arXiv: https://arxiv.org/abs/2609.08224
Code: https://github.com/ziqin-h/3DWay

#VLA #robotics
```

</details>

---

### [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209)

**Authors:** Weiwei Gu, Anmol Gupta, Anant Sah, Ryan Varghese, Lalitha Shreya Vanam et al. (8 authors)

**Published:** 2026-09-08 (updated 2026-09-09) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.08209) | [PDF](https://arxiv.org/pdf/2609.08209) | [Project Page](https://roboreel.github.io)

<details>
<summary>Abstract</summary>

Learning from Observation (LfO) is a fundamental robotic capability that replicates how humans and animals socially learn from each other. Beyond its biological parallels, this modality provides a practical solution for data scaling in sample-inefficient and data-starved domains like robotics. Recent work has demonstrated promising results in learning manipulation skills from human videos, yet progress in this area remains difficult to assess. Existing methods vary widely in assumptions, hardware choices, and environment setups making it difficult to draw meaningful comparisons and identify ad...

</details>

<details>
<summary>Share</summary>

```
Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation

Learning from Observation (LfO) is a fundamental robotic capability that replicates how humans and animals socially learn from each other.

arXiv: https://arxiv.org/abs/2609.08209
Project page: https://roboreel.github.io

#VLA #robotics
```

</details>

---

### [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158)

**Authors:** Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren et al. (7 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.09158) | [PDF](https://arxiv.org/pdf/2609.09158)

<details>
<summary>Abstract</summary>

We study the problem of navigating cluttered indoor environments with a humanoid robot. Unlike conventional methods that model navigation as a 2D path planning problem, humanoid traversal in cluttered environments requires continuous geometry-aware whole-body adaptation, including coordinated arm placement, torso adjustment, and gait modulation for collision-free movement through complex 3D spaces. We introduce TANGO, the first whole-body vision-language navigation framework for language-conditioned humanoid traversal in cluttered environments. Given a natural-language instruction and egocentr...

</details>

<details>
<summary>Share</summary>

```
TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

We study the problem of navigating cluttered indoor environments with a humanoid robot.

arXiv: https://arxiv.org/abs/2609.09158

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

### [ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies](https://arxiv.org/abs/2609.11697)

**Authors:** Jianming Ma, Rongjun Jin, Xiaxi Si, Yang Zhang, Yiheng Li et al. (6 authors)

**Published:** 2026-09-10 (updated 2026-09-14) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.11697) | [PDF](https://arxiv.org/pdf/2609.11697)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) and World-Action Models (WAMs) have demonstrated strong capabilities in general-purpose robotic manipulation, yet their generated actions may violate hard physical constraints and therefore be unsafe or infeasible for deployment. Existing safety approaches either optimize statistical safety objectives without deterministic per-step guarantees or correct unsafe actions only during inference, creating a mismatch between policy training and execution. We introduce ActSafeGuard, a differentiable and training-aligned safeguard layer for flow-matching based policies. Act...

</details>

<details>
<summary>Share</summary>

```
ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies

Vision-Language-Action (VLA) and World-Action Models (WAMs) have demonstrated strong capabilities in general-purpose robotic manipulation, yet their generated actions may violate hard physical constraints and therefor...

arXiv: https://arxiv.org/abs/2609.11697

#VLA #robotics
```

</details>

---

### [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](https://arxiv.org/abs/2609.09591)

**Authors:** Zhuodong Liu, Xiangyu Li, Chunhong Yuan, Hongyang Du, Bodong Shang et al. (8 authors)

**Published:** 2026-09-09 | **Categories:** eess.SP, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.09591) | [PDF](https://arxiv.org/pdf/2609.09591)

<details>
<summary>Abstract</summary>

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing. Vision-language-action (VLA) models offer a foundation by integrating visual perception, language understanding, and action generation into a unified closed-loop policy. However, training and adapting VLA models to distributed robotic agents introduce challenges in privacy protection, communication efficiency, and model heterogeneity. Existing federated lea...

</details>

<details>
<summary>Share</summary>

```
Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, a...

arXiv: https://arxiv.org/abs/2609.09591

#VLA #robotics
```

</details>

---

### [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](https://arxiv.org/abs/2609.08162)

**Authors:** Chi Wan, Kangrui Wang, Yuan Si, Pingyue Zhang, Manling Li

**Published:** 2026-09-08 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.08162) | [PDF](https://arxiv.org/pdf/2609.08162)

<details>
<summary>Abstract</summary>

How can vision-language-action (VLA) models adapt to new environments where world dynamics shift? While recent research has combined world modeling and action prediction to improve VLA performance, existing methods largely rely on pretraining on static datasets, without mechanisms for active adaptation at deployment time. As a result, these models often fail to generalize when deployed in unseen scenarios with novel object configurations or dynamics. We present WorldAgen, a unified framework that jointly learns world modeling and action prediction while enabling Test-Time Training (TTT) to ada...

</details>

<details>
<summary>Share</summary>

```
WorldAgen: Unified State-Action Prediction with Test-Time World Model Training

How can vision-language-action (VLA) models adapt to new environments where world dynamics shift?

arXiv: https://arxiv.org/abs/2609.08162

#VLA #robotics
```

</details>

---

### [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](https://arxiv.org/abs/2609.11308)

**Authors:** Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.11308) | [PDF](https://arxiv.org/pdf/2609.11308)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constrained design: less tool breadth, but greater interface bandwidth. 2AM makes a multimodal Agent the s...

</details>

<details>
<summary>Share</summary>

```
2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

Long-horizon robot manipulation requires memory, but not necessarily inside the action policy.

arXiv: https://arxiv.org/abs/2609.11308

#VLA #robotics
```

</details>

---

### [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](https://arxiv.org/abs/2609.10243)

**Authors:** Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.10243) | [PDF](https://arxiv.org/pdf/2609.10243)

<details>
<summary>Abstract</summary>

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world. Yet methods that perform well in simulation can degrade substantially on real robots, especially in long-horizon deformable-object manipulation, where policies must track changing states and execute reliable multi-stage bimanual interactions. Existing real-robot benchmarks mainly focus on short-horizon rigid-object tasks and offer limited coverage of long-horizon deformable manipulation. We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with gar...

</details>

<details>
<summary>Share</summary>

```
FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world.

arXiv: https://arxiv.org/abs/2609.10243

#VLA #robotics
```

</details>

---

### [No Free Checker: A Survey of Verifiers for Robot Policies](https://arxiv.org/abs/2609.09250)

**Authors:** Yang Wan, Xihang Yue, Zhirui Liu, Ziyuan Chu, Shuxun Wang et al. (10 authors)

**Published:** 2026-09-08 (updated 2026-09-13) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.09250) | [PDF](https://arxiv.org/pdf/2609.09250)

<details>
<summary>Abstract</summary>

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two properties. Availability is how much a verdict costs, how early in a rollout the verdict arrives, and how often a verdict can be asked for. Availability rises as verdicts get cheaper, earlier, and denser. Credibility is how much a high score...

</details>

<details>
<summary>Share</summary>

```
No Free Checker: A Survey of Verifiers for Robot Policies

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them.

arXiv: https://arxiv.org/abs/2609.09250

#VLA #robotics
```

</details>

---

### [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2609.11310)

**Authors:** Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao et al. (8 authors)

**Published:** 2026-09-10 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.11310) | [PDF](https://arxiv.org/pdf/2609.11310)

<details>
<summary>Abstract</summary>

We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen. We identify two key design choices. First, placing prompt tokens at the cross-modal boundary between visual and text tokens outperforms other placements (10.0 vs. 8.4 mA...

</details>

<details>
<summary>Share</summary>

```
Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision.

arXiv: https://arxiv.org/abs/2609.11310

#VLA #robotics
```

</details>

---

### [When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents](https://arxiv.org/abs/2609.10873)

**Authors:** Qinzhen Ma, Ruihai Wu

**Published:** 2026-09-09 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.10873) | [PDF](https://arxiv.org/pdf/2609.10873)

<details>
<summary>Abstract</summary>

Independent evaluation can reject harmful policy updates yet also prevent useful continual learning. We argue that update admission must be assessed through both error control and retained learning opportunities at a stated interaction budget. We identify a concrete failure: a range-based confidence gate cannot certify unchanged old-task behavior within otherwise substantial budgets. A standard paired-binomial construction reduces this burden when outcome disagreements are rare. We also specify certified historical-reference promotion and a round-level missed-opportunity metric. In a construct...

</details>

<details>
<summary>Share</summary>

```
When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents

Independent evaluation can reject harmful policy updates yet also prevent useful continual learning.

arXiv: https://arxiv.org/abs/2609.10873

#VLA #robotics
```

</details>

---
