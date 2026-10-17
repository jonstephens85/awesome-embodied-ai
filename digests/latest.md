# What's New

Papers discovered in the run at **2026-10-17 18:10 UTC**.

**New this run:** 31

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (3)

### [KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration](https://arxiv.org/abs/2610.21152)

**Authors:** Zibo Zhou, Yueru Chen, Junsong Wu, Weiji Xie, Qingyao Xu et al. (11 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric demonstration" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21152) | [PDF](https://arxiv.org/pdf/2610.21152)

<details>
<summary>Abstract</summary>

Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that still require robot data for adaptation or generate controller-specific commands that limit reuse. Conversion also requires robot-view observations aligned with the generated whole-body motion. We present KODA (Kinematics-Observation Data Ali...

</details>

<details>
<summary>Share</summary>

```
KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration

Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels.

arXiv: https://arxiv.org/abs/2610.21152

#egocentric #robotlearning
```

</details>

---

### [EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos](https://arxiv.org/abs/2610.20904)

**Authors:** Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang et al. (15 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20904) | [PDF](https://arxiv.org/pdf/2610.20904)

<details>
<summary>Abstract</summary>

Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappings require meticulous recal- ibration across different embodiments and risk propagating hand-tracking errors into downstream robot control pipelines. To this end, we propose EgoJEPA, a three-stage framework that learns embodiment-agnostic r...

</details>

<details>
<summary>Share</summary>

```
EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging.

arXiv: https://arxiv.org/abs/2610.20904

#egocentric #robotlearning
```

</details>

---

### [Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation](https://arxiv.org/abs/2610.22342)

**Authors:** Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang et al. (22 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22342) | [PDF](https://arxiv.org/pdf/2610.22342)

<details>
<summary>Abstract</summary>

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histori...

</details>

<details>
<summary>Share</summary>

```
Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images.

arXiv: https://arxiv.org/abs/2610.22342

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (18)

### [REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178)

**Authors:** Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary, Shizhe Chen, Moritz Böhle

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22178) | [PDF](https://arxiv.org/pdf/2610.22178) | [Code](https://github.com/kyutai-labs/reki)

<details>
<summary>Abstract</summary>

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in th...

</details>

<details>
<summary>Share</summary>

```
REKI: Registering Knowledge in VLAs

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa36...

arXiv: https://arxiv.org/abs/2610.22178
Code: https://github.com/kyutai-labs/reki

#VLA #robotics
```

</details>

---

### [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146)

**Authors:** Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu, Yang Sui, Yangming Shi

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22146) | [PDF](https://arxiv.org/pdf/2610.22146) | [Code](https://github.com/jiuyixu25/FastVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets...

</details>

<details>
<summary>Share</summary>

```
FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often mu...

arXiv: https://arxiv.org/abs/2610.22146
Code: https://github.com/jiuyixu25/FastVLA

#VLA #robotics
```

</details>

---

### [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)

**Authors:** Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21306) | [PDF](https://arxiv.org/pdf/2610.21306) | [Code](https://github.com/ZJU-OmniAI/VLA-Delta)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. W...

</details>

<details>
<summary>Share</summary>

```
VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks.

arXiv: https://arxiv.org/abs/2610.21306
Code: https://github.com/ZJU-OmniAI/VLA-Delta

#VLA #robotics
```

</details>

---

### [Fast-VLA: You Only Think Once for Robot Manipulation](https://arxiv.org/abs/2610.21389)

**Authors:** Kehong Gong, Guanli Hou, Xiaoxu Zheng, Qi Wang, Mingxi Xu et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21389) | [PDF](https://arxiv.org/pdf/2610.21389) | [Project Page](https://garfield-kh.github.io/FastVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk. Yet task understanding changes far more slowly than the robot state. We introduce Fast-VLA, which invokes a frozen 4B VLM once per episode to contextualize the instruction and initial views as fixed, multi-layer key-value task memory. During execution, a lightweight online actor fuses learned time- and arm-indexed queries with current visual and proprioceptive feedback to form action queries. These queries r...

</details>

<details>
<summary>Share</summary>

```
Fast-VLA: You Only Think Once for Robot Manipulation

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk.

arXiv: https://arxiv.org/abs/2610.21389
Project page: https://garfield-kh.github.io/FastVLA

#VLA #robotics
```

</details>

---

### [LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.21362)

**Authors:** Qixin Sun, WenLong Gao, Xiansheng Chen, Zhongyuan Wang, Si Liu et al. (6 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21362) | [PDF](https://arxiv.org/pdf/2610.21362) | [Code](https://github.com/buaa-colalab/LTM-pi)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires remembering interactions that are no longer visible. We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations. Instantiated on $π_{0.5}$ as LTM-$π$, our method uses a frozen latent action encoder, a lightweight adapter, and causal KV caching for incremental inference without memory-specific semantic annotations or external reasoning-model calls. With DreamDojo transitions, LTM-$π$ achieves 58.54% success on RoboMME and 80.5% on LIBERO-Mem, performing best among baselines without external...

</details>

<details>
<summary>Share</summary>

```
LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models

Robotic manipulation often requires remembering interactions that are no longer visible.

arXiv: https://arxiv.org/abs/2610.21362
Code: https://github.com/buaa-colalab/LTM-pi

#VLA #robotics
```

</details>

---

### [Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2610.21522)

**Authors:** Lichao Ni, Yuhan Liu, Pengfei Li, Guanghuan Fang

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21522) | [PDF](https://arxiv.org/pdf/2610.21522)

<details>
<summary>Abstract</summary>

Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging. On-policy distillation (OPD) transfers teacher knowledge on inputs induced by the student, addressing the distribution mismatch encountered during deployment. For flow-based VLAs, this mismatch arises at two levels: environment observations and intermediate action-generation states. We propose a two-level on-policy distillation framework that couples student-driven environment interaction with teacher velocity supervision along stud...

</details>

<details>
<summary>Share</summary>

```
Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models

Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging.

arXiv: https://arxiv.org/abs/2610.21522

#VLA #robotics
```

</details>

---

### [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](https://arxiv.org/abs/2610.21453)

**Authors:** Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21453) | [PDF](https://arxiv.org/pdf/2610.21453) | [Project Page](https://vincent2311.github.io/Projects/CarryOn/)

<details>
<summary>Abstract</summary>

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution. Second, reliable deployment demands explainable safety assurance that proactively prevents hazards and gracefully recovers from occasional physical failures. To address these gaps, we present Car...

</details>

<details>
<summary>Share</summary>

```
CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable exe...

arXiv: https://arxiv.org/abs/2610.21453
Project page: https://vincent2311.github.io/Projects/CarryOn/

#VLA #robotics
```

</details>

---

### [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2610.21251)

**Authors:** Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21251) | [PDF](https://arxiv.org/pdf/2610.21251)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions that specify how to carry it out. Through our diagnoses, we find that How-level instructions do not help current VLAs and lower task success. We hypothesize that pairing each training episode with a single instruction limits How-level instruction following, and show that training with segment-level enriched instructions makes actions respond to such instructions without consistently...

</details>

<details>
<summary>Share</summary>

```
Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions tha...

arXiv: https://arxiv.org/abs/2610.21251

#VLA #robotics
```

</details>

---

### [When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models](https://arxiv.org/abs/2610.21160)

**Authors:** Shilin Zhang

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21160) | [PDF](https://arxiv.org/pdf/2610.21160)

<details>
<summary>Abstract</summary>

Dual-system vision-language-action (VLA) models pair a high-frequency fast policy with a slow, expensive module, and published trigger mechanisms for invoking it lack a shared objective, measured costs, and any standard separating schedule quality from module quality. We provide the missing account: invocation is formalized as a calibrated decision problem whose fixed-ratio, fixed-budget, and history-gated schedules are degenerate cases of one quantity, the Value of Intervention (VoI); a renewal baseline proves the optimal schedule periodic under state-independent collapse, with adaptive gains...

</details>

<details>
<summary>Share</summary>

```
When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models

Dual-system vision-language-action (VLA) models pair a high-frequency fast policy with a slow, expensive module, and published trigger mechanisms for invoking it lack a shared objective, measured costs, and any standa...

arXiv: https://arxiv.org/abs/2610.21160

#VLA #robotics
```

</details>

---

### [LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](https://arxiv.org/abs/2610.22372)

**Authors:** Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22372) | [PDF](https://arxiv.org/pdf/2610.22372) | [Project Page](https://libero-perm.github.io/)

<details>
<summary>Abstract</summary>

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings; 2) how they learn single preferences from demonstrations; 3) how efficiently they acquire preferenc...

</details>

<details>
<summary>Share</summary>

```
LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality.

arXiv: https://arxiv.org/abs/2610.22372
Project page: https://libero-perm.github.io/

#VLA #robotics
```

</details>

---

### [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models](https://arxiv.org/abs/2610.21985)

**Authors:** Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen et al. (7 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21985) | [PDF](https://arxiv.org/pdf/2610.21985)

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the c...

</details>

<details>
<summary>Share</summary>

```
VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation.

arXiv: https://arxiv.org/abs/2610.21985

#VLA #robotics
```

</details>

---

### [What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning](https://arxiv.org/abs/2610.21915)

**Authors:** Haitao Shen, Hanyu Liu, Yihan Lin, Huiping Liu, Junbo Cui et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21915) | [PDF](https://arxiv.org/pdf/2610.21915)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV) prediction are often added to improve policy learning, yet they compete with action prediction for the same training budget. We ask whether, under a fixed budget, allocating a substantial share of training samples to such objectives, rather than to further action prediction, can improve policy learning. We build a unified VLA framework that couples a two-stream multim...

</details>

<details>
<summary>Share</summary>

```
What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions.

arXiv: https://arxiv.org/abs/2610.21915

#VLA #robotics
```

</details>

---

### [Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution](https://arxiv.org/abs/2610.21434)

**Authors:** Minkyu Kim, Junhoo Lee, Seungyeon Kim, Suhyun Jeon, Baekseung Kim et al. (7 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21434) | [PDF](https://arxiv.org/pdf/2610.21434)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies generate action sequences that reduce repeated inference, but deciding how much of each sequence to execute is critical to task success. Existing adaptive methods make this decision using generation stability or prediction agreement, yet these signals do not establish whether executing a candidate prefix preserves the ability to complete the task. We introduce a policy-aligned predictive verifier (PAV) that anticipates the consequences of candidate action prefixes and evaluates their compatibility with successful continuation before execution. Rather than...

</details>

<details>
<summary>Share</summary>

```
Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution

Vision-language-action (VLA) policies generate action sequences that reduce repeated inference, but deciding how much of each sequence to execute is critical to task success.

arXiv: https://arxiv.org/abs/2610.21434

#VLA #robotics
```

</details>

---

### [An Agentic Framework for Proactive Robots with Procedural Assistance Memory](https://arxiv.org/abs/2610.21211)

**Authors:** Dohyun Lee, Minho Park, Jeonghoon Park, Dongyoon Hwang, Junha Hyung et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21211) | [PDF](https://arxiv.org/pdf/2610.21211) | [Project Page](https://davian-robotics.github.io/PAM/)

<details>
<summary>Abstract</summary>

Proactive robots should anticipate user needs and provide assistance before being explicitly asked. A straightforward approach is to infer human intentions from commonsense knowledge, but the same observed behavior can imply different needs across users, potentially leading to unwanted assistance. We observe that everyday routines in the real world exhibit recurring patterns, so learning these patterns can reduce ambiguity in proactive decisions. Based on this, we propose a memory-based agentic framework in which a VLM task predictor reads a Procedural Assistance Memory (PAM) alongside the cur...

</details>

<details>
<summary>Share</summary>

```
An Agentic Framework for Proactive Robots with Procedural Assistance Memory

Proactive robots should anticipate user needs and provide assistance before being explicitly asked.

arXiv: https://arxiv.org/abs/2610.21211
Project page: https://davian-robotics.github.io/PAM/

#VLA #robotics
```

</details>

---

### [A Phenomenology of Neural Geometry in Vision-Language-Action Models](https://arxiv.org/abs/2610.20840)

**Authors:** Mozes Jacobs, Aiden Swann, Mathilde Papillon, Siddharth Boppana, Fenil R. Doshi et al. (19 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20840) | [PDF](https://arxiv.org/pdf/2610.20840)

<details>
<summary>Abstract</summary>

Robotic manipulation is inherently geometric, but what shape does the world take inside the policy that performs it? Prior work on vision-language-action (VLA) policies establishes that task-relevant variables are linearly readable from activations, yet readability certifies only that a variable is present and says nothing about the shape its values trace, which may be curved and multi-dimensional. Using controlled sweeps, natural rollouts, linear probes, and activation interventions, we build a taxonomy of seven task-relevant concepts in VLA models. We find that realized geometry is predomina...

</details>

<details>
<summary>Share</summary>

```
A Phenomenology of Neural Geometry in Vision-Language-Action Models

Robotic manipulation is inherently geometric, but what shape does the world take inside the policy that performs it?

arXiv: https://arxiv.org/abs/2610.20840

#VLA #robotics
```

</details>

---

### [Memory as Weights: Internalizing Long-Term History for Streaming Videos](https://arxiv.org/abs/2610.22070)

**Authors:** Zhuoming Liu, Jinhong Lin, Lin Zhang, Yiwu Zhong, Yin Li

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22070) | [PDF](https://arxiv.org/pdf/2610.22070)

<details>
<summary>Abstract</summary>

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries. Existing memory mechanisms typically compress, retrieve, or cache historical observations and reintroduce them into the input context, forcing historical memory and current observations to compete for limited context. We propose MaLoW, a streaming memory framework that instead internalizes historical context into evolving lightweight parameter updates. MaLoW uses a recurrent HyperNetwork to incrementally consolidate incoming video ob...

</details>

<details>
<summary>Share</summary>

```
Memory as Weights: Internalizing Long-Term History for Streaming Videos

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries.

arXiv: https://arxiv.org/abs/2610.22070

#VLA #robotics
```

</details>

---

### [Causal Analysis of Robot Foundation Models Enables Efficiency Gains](https://arxiv.org/abs/2610.20750)

**Authors:** Aiden Swann, Mathilde Papillon, Mozes Jacobs, Siddharth Boppana, Tal Haklay et al. (16 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20750) | [PDF](https://arxiv.org/pdf/2610.20750)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($π_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input image and the instruction shape actions. Across the three models, activation patching shows that caus...

</details>

<details>
<summary>Share</summary>

```
Causal Analysis of Robot Foundation Models Enables Efficiency Gains

Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation.

arXiv: https://arxiv.org/abs/2610.20750

#VLA #robotics
```

</details>

---

### [Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models](https://arxiv.org/abs/2610.20767)

**Authors:** Aiden Swann, Mozes Jacobs, Mathilde Papillon, Siddharth Boppana, David Chanin et al. (15 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20767) | [PDF](https://arxiv.org/pdf/2610.20767)

<details>
<summary>Abstract</summary>

Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover several multi-dimensional task-relevant features underlying the model's computation (e.g., perception, lan...

</details>

<details>
<summary>Share</summary>

```
Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

Can better feature discovery improve control over robot behavior through internal interventions and training data?

arXiv: https://arxiv.org/abs/2610.20767

#VLA #robotics
```

</details>

---

## World Models (10)

### [Orbia: Do Generated Videos Form a Consistent 3D World?](https://arxiv.org/abs/2610.20693)

**Authors:** Dongyue Lu, Guian Fang, Hur Lim, Yonggang Wu, Yanrong Wang et al. (23 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20693) | [PDF](https://arxiv.org/pdf/2610.20693) | [Project Page](https://orbia-bench.github.io/) | [Code](https://github.com/worldbench/Orbia)

<details>
<summary>Abstract</summary>

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world. Existing benchmarks assess selected geometric properties or use vision-language models to judge memory and consistency, leaving systematic 3D evaluation underexplored. We introduce Orbia, the first benchmark dedicated to a systematic and comprehensive evaluation of 3D consistency in interactive world models. Through controlled exploration and revisit, we organize the evaluation into three dimensions: input preservation, genera...

</details>

<details>
<summary>Share</summary>

```
Orbia: Do Generated Videos Form a Consistent 3D World?

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world.

arXiv: https://arxiv.org/abs/2610.20693
Project page: https://orbia-bench.github.io/
Code: https://github.com/worldbench/Orbia

#worldmodels #robotics
```

</details>

---

### [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363)

**Authors:** Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li et al. (14 authors)

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "action-conditioned video" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22363) | [PDF](https://arxiv.org/pdf/2610.22363) | [Project Page](https://p3-wam.pages.dev/)

<details>
<summary>Abstract</summary>

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D acti...

</details>

<details>
<summary>Share</summary>

```
Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perc...

arXiv: https://arxiv.org/abs/2610.22363
Project page: https://p3-wam.pages.dev/

#worldmodels #robotics
```

</details>

---

### [MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models](https://arxiv.org/abs/2610.21686)

**Authors:** Yi Qiao, Maolin Zheng, Haoran Sun, Lujia Dong, Wenzhao Lian

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21686) | [PDF](https://arxiv.org/pdf/2610.21686)

<details>
<summary>Abstract</summary>

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action. Yet most monitoring methods are reactive, identifying anomalies only after they become observable. Anticipating such anomalies is challenging because visual observations only partially reveal physical interaction, while planned actions describe intended motion rather than their actual physical consequences. We address this problem with MAIA, a multimodal framework for anomaly anticipation. Its vision-action-force world model learns nominal interaction dynamics and predicts the visual...

</details>

<details>
<summary>Share</summary>

```
MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action.

arXiv: https://arxiv.org/abs/2610.21686

#worldmodels #robotics
```

</details>

---

### [TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control](https://arxiv.org/abs/2610.21922)

**Authors:** Menghao Yin, Jiaju Yin, Xiyue Dong, Lixin Xu, Zhenhui Zhang et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21922) | [PDF](https://arxiv.org/pdf/2610.21922)

<details>
<summary>Abstract</summary>

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states. These limitations hinder learning from action-free videos and can encourage overfitting to demonstration conditions, weakening generalization and robustness. We present TS-WAM, a lightweight Teacher-Student World-Action Model that addresses these challenges through self-supervised temporal learning and explicit future prediction. Its vlm-jepa framework learns from heterogeneous data, including robot demonstrations and action-free human videos, usi...

</details>

<details>
<summary>Share</summary>

```
TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states.

arXiv: https://arxiv.org/abs/2610.21922

#worldmodels #robotics
```

</details>

---

### [T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](https://arxiv.org/abs/2610.22364)

**Authors:** Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang et al. (12 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22364) | [PDF](https://arxiv.org/pdf/2610.22364)

<details>
<summary>Abstract</summary>

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z for test-time optimization of environment latents, which augments a robotic world model with a learnable environment latent to condition world predictions. This compact latent captures underlying environmental variation without supervision of what environmental factors exist or what values they take...

</details>

<details>
<summary>Share</summary>

```
T2-z: Test-Time Optimization of Environment Latents for Robotic World Models

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties...

arXiv: https://arxiv.org/abs/2610.22364

#worldmodels #robotics
```

</details>

---

### [Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift](https://arxiv.org/abs/2610.22041)

**Authors:** Danqi Zhao, Keyu Chen, Wenchao Sun, Minglei Huang, Jianhe Zhang et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22041) | [PDF](https://arxiv.org/pdf/2610.22041)

<details>
<summary>Abstract</summary>

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training. At deployment, a different downstream controller may execute the same planned trajectory differently, creating a planning-execution gap between the frozen model's imagined future and actual execution. A natural remedy is to replace the planned trajectory with its predicted or observed execution. However, we find that better execution fidelity does not necessarily yield better decisions: directly substituting predicted execu...

</details>

<details>
<summary>Share</summary>

```
Plans Are Not Executions: Adapting Frozen World-Model Planners to Controller-Induced Execution Shift

World-model planners evaluate candidate trajectories by predicting their future consequences, implicitly relying on the plan-to-motion relationship learned during training.

arXiv: https://arxiv.org/abs/2610.22041

#worldmodels #robotics
```

</details>

---

### [Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311)

**Authors:** Qiuhong Shen, Shizun Wang, Xinchao Wang

**Published:** 2026-10-15 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22311) | [PDF](https://arxiv.org/pdf/2610.22311)

<details>
<summary>Abstract</summary>

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using frustum slab correspondences from streaming geometry. Velox represents historical b...

</details>

<details>
<summary>Share</summary>

```
Velox: Spatial Memory Makes World Models Efficient

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation.

arXiv: https://arxiv.org/abs/2610.22311

#worldmodels #robotics
```

</details>

---

### [Learning Intrinsic Dynamics in Latent World Models](https://arxiv.org/abs/2610.21612)

**Authors:** Jiamin Shi, Yuanhong Zhang, Zhiyang Liu, Jiawei Sun, Jingwen Fu

**Published:** 2026-10-15 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21612) | [PDF](https://arxiv.org/pdf/2610.21612)

<details>
<summary>Abstract</summary>

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models. However, visual variations unrelated to the underlying control process can obscure this relationship in learned representations. We investigate the connection between action predictability, defined as the ability to reconstruct an action from consecutive latent states, and the preservation of intrinsic dynamics. Our central hypothesis is that encouraging action predictability discourages representations from discarding the distinctions between different actions and their conse...

</details>

<details>
<summary>Share</summary>

```
Learning Intrinsic Dynamics in Latent World Models

Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models.

arXiv: https://arxiv.org/abs/2610.21612

#worldmodels #robotics
```

</details>

---

### [Dexterity from Supervised Play](https://arxiv.org/abs/2610.22340)

**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma et al. (6 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.22340) | [PDF](https://arxiv.org/pdf/2610.22340)

<details>
<summary>Abstract</summary>

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-...

</details>

<details>
<summary>Share</summary>

```
Dexterity from Supervised Play

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation?

arXiv: https://arxiv.org/abs/2610.22340

#worldmodels #robotics
```

</details>

---

### [From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion](https://arxiv.org/abs/2610.21374)

**Authors:** Bazeela Banday, Jishnu Keshavan

**Published:** 2026-10-15 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.21374) | [PDF](https://arxiv.org/pdf/2610.21374)

<details>
<summary>Abstract</summary>

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable. This letter introduces a visual safety-certification paradigm that uses scale-free, depth-normalized relative motion encoded by monocular optical flow as the representation for collision-risk certification, without reconstructing obstacle position, velocity, geometry, or a metric world model. Unlike conventional optical-flow-based navigation approaches that rely on image motion to shape avoidance behavior, the proposed framework directly encodes collision-cone geo...

</details>

<details>
<summary>Share</summary>

```
From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable.

arXiv: https://arxiv.org/abs/2610.21374

#worldmodels #robotics
```

</details>

---
