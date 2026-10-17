# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-17 18:10 UTC

**Papers shown:** 85 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

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

### [ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction](https://arxiv.org/abs/2610.20223)

**Authors:** Huailiang Ma, Yuxuan Li, Ziyi Zhao, Xinkai Wang, Mingyu Li et al. (10 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20223) | [PDF](https://arxiv.org/pdf/2610.20223) | [Project Page](https://huailiangma.github.io/objdream/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions. However, most existing VLA models still operate on image-level visual representations inherited from pretrained vision-language backbones, while lacking fine-grained object understanding for manipulation. As a result, their robustness can degrade under out-of-distribution object layouts, clutter, and background variations. To address these limitations, we introduce ObjDream, an object-centric VLA framework cent...

</details>

<details>
<summary>Share</summary>

```
ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction

Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2610.20223
Project page: https://huailiangma.github.io/objdream/

#VLA #robotics
```

</details>

---

### [What Matters for World Modeling in Vision-Language-Action Models?](https://arxiv.org/abs/2610.19825)

**Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang et al. (13 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19825) | [PDF](https://arxiv.org/pdf/2610.19825) | [Project Page](https://dylanmqs.github.io/WM-in-VLAs/)

<details>
<summary>Abstract</summary>

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping. However, existing approaches vary simultaneously in their world representations, integration paradigms, and policy backbones, making it difficult to determine what truly matters for effective world model integration. To disentangle these factors, we categorize existing efforts into four representative paradigms, namely Implicit Future Alignment, Explicit Future Query, MoT Future Expert, and Extern...

</details>

<details>
<summary>Share</summary>

```
What Matters for World Modeling in Vision-Language-Action Models?

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping.

arXiv: https://arxiv.org/abs/2610.19825
Project page: https://dylanmqs.github.io/WM-in-VLAs/

#VLA #robotics
```

</details>

---

### [WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL](https://arxiv.org/abs/2610.17922)

**Authors:** Shangqing Zhou, Zhennan Jiang, Ning Ma, Xin Fu, Yupeng Zheng et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17922) | [PDF](https://arxiv.org/pdf/2610.17922) | [Project Page](https://youmo445.github.io/WoVR_Plus.github.io/)

<details>
<summary>Abstract</summary>

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization. Extending them to richer VLA interfaces and long-horizon tasks raises challenges in spatiotemporal and cross-modal consistency, exploration-reliability balance in RL, and compounding rollout errors. We present WoVR+, extending WoVR's hallucination-aware WM-RL framework by redesigning the learned environment and imagined interaction protocol: A VLA-interface-aligned world model provides multi-view predi...

</details>

<details>
<summary>Share</summary>

```
WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization.

arXiv: https://arxiv.org/abs/2610.17922
Project page: https://youmo445.github.io/WoVR_Plus.github.io/

#VLA #robotics
```

</details>

---

### [TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency](https://arxiv.org/abs/2610.17540)

**Authors:** Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17540) | [PDF](https://arxiv.org/pdf/2610.17540) | [Project Page](https://tacitvla.github.io)

<details>
<summary>Abstract</summary>

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate...

</details>

<details>
<summary>Share</summary>

```
TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding.

arXiv: https://arxiv.org/abs/2610.17540
Project page: https://tacitvla.github.io

#VLA #robotics
```

</details>

---

### [Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation](https://arxiv.org/abs/2610.14415)

**Authors:** Shihan Zhao, Henry Chen, Ya-Chuan Hsu, Minjune Hwang, Siddharth Srikanth et al. (10 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14415) | [PDF](https://arxiv.org/pdf/2610.14415) | [Project Page](https://qd-env.github.io/qdeg/)

<details>
<summary>Abstract</summary>

A long-standing goal in robotics is to develop generalist robots that can perform tasks across a wide range of settings, flexibly specified with images and text. Vision-Language-Action (VLA) models offer a promising path toward this goal by training on large collections of robot demonstrations. However, while VLAs perform well in-distribution, they often fail under minor test-time shifts, such as changes in object positions, lighting, textures, and camera poses. To address this, we propose Quality Diversity for Diverse Environment Generation (Q-DEG), a method for improving VLA robustness by ge...

</details>

<details>
<summary>Share</summary>

```
Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation

A long-standing goal in robotics is to develop generalist robots that can perform tasks across a wide range of settings, flexibly specified with images and text.

arXiv: https://arxiv.org/abs/2610.14415
Project page: https://qd-env.github.io/qdeg/

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

### [FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs](https://arxiv.org/abs/2610.20064)

**Authors:** Bingao Chen, Lihan Zha, C. Karen Liu, Guy Tevet

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20064) | [PDF](https://arxiv.org/pdf/2610.20064) | [Project Page](https://tml.stanford.edu/FoveaVLA/)

<details>
<summary>Abstract</summary>

We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions. Wrist cameras provide close-up detail but restrict the view to the end-effector's surroundings. External cameras see the whole scene, but the policy receives them at low resolution, so the fine detail needed for manipulation is lost. FoveaVLA recovers this detail by predicting, alongside each action chunk, the interaction region to observe at the next policy query. The policy then receives crops of these regions, taken from the original-resolution images, together with the f...

</details>

<details>
<summary>Share</summary>

```
FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs

We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions.

arXiv: https://arxiv.org/abs/2610.20064
Project page: https://tml.stanford.edu/FoveaVLA/

#VLA #robotics
```

</details>

---

### [Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](https://arxiv.org/abs/2610.19495)

**Authors:** Yunze Liu, Jing Wang, Shenrui Wu, Wenkun He, Guanqi Zhan et al. (19 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19495) | [PDF](https://arxiv.org/pdf/2610.19495) | [Project Page](https://robota-ai.github.io/robota-embed/)

<details>
<summary>Abstract</summary>

Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first vision-language-action (VLA) embedding model to jointly encode all three modalities in both current-state queries and recorded future continuations. Predictive retrieval training aligns these endpoints, enabling historical continuations to serve as context at inference time. We construct a multi-source corpus of 1,695,684 cleaned training anchors and introduce Robota-Embed-Bench, with 4,000 queries and a shared 8,000-e...

</details>

<details>
<summary>Share</summary>

```
Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution

Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow.

arXiv: https://arxiv.org/abs/2610.19495
Project page: https://robota-ai.github.io/robota-embed/

#VLA #robotics
```

</details>

---

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869)

**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang et al. (22 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18869) | [PDF](https://arxiv.org/pdf/2610.18869) | [Project Page](https://axis-bench.github.io/)

<details>
<summary>Abstract</summary>

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain b...

</details>

<details>
<summary>Share</summary>

```
What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning?

arXiv: https://arxiv.org/abs/2610.18869
Project page: https://axis-bench.github.io/

#VLA #robotics
```

</details>

---

### [Interaction Latents as Actions for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18855)

**Authors:** Yuhang Zheng, Yujie Zang, Yuchen Liu, Yupeng Zheng, Zhennan Jiang et al. (12 authors)

**Published:** 2026-10-13 (updated 2026-10-14) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18855) | [PDF](https://arxiv.org/pdf/2610.18855) | [Project Page](https://mrsecant.github.io/ILA/)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction. Yet most robot policies represent actions primarily as motion trajectories, using tactile signals as inputs or auxiliary prediction targets without explicitly encoding contact dynamics in the action representation. We propose ILA (Interaction Latents as Actions), which uses decodable interaction latents that jointly capture the evolution of motion, contact, and force application as policy action units, providing a shared representation for acti...

</details>

<details>
<summary>Share</summary>

```
Interaction Latents as Actions for Contact-Rich Manipulation

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction.

arXiv: https://arxiv.org/abs/2610.18855
Project page: https://mrsecant.github.io/ILA/

#VLA #robotics
```

</details>

---

### [$Δ$ Flow Matching for Robot Foundation Models](https://arxiv.org/abs/2610.15794)

**Authors:** Kuangji Zuo, Tuo An, Xinying Guo, Gen Li, Mengfei Zhao et al. (12 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15794) | [PDF](https://arxiv.org/pdf/2610.15794) | [Project Page](https://zuo-kuangji.github.io/delta-flow/)

<details>
<summary>Abstract</summary>

Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly training and iterative sampling, especially for WAMs with an additional visual branch. We introduce $Δ$-flow, which constructs the source from recent history with mild noise rather than from a fixed Gaussian prior. This moves the source closer t...

</details>

<details>
<summary>Share</summary>

```
$Δ$ Flow Matching for Robot Foundation Models

Flow matching is a common generative recipe for robot foundation models.

arXiv: https://arxiv.org/abs/2610.15794
Project page: https://zuo-kuangji.github.io/delta-flow/

#VLA #robotics
```

</details>

---

### [CoLA: Multi-VLA Coordination via Learned Adapters](https://arxiv.org/abs/2610.15337)

**Authors:** Ahaskar Kashyap, Jiawen Zong, Boyu Ma, Chuhao Zhou, Jingliang Li et al. (7 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.LG, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15337) | [PDF](https://arxiv.org/pdf/2610.15337) | [Code](https://github.com/Ahaskar04/CoLA.git)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies. When several such agents share a workspace, they can coordinate implicitly, by observing one another, or explicitly, by exchanging messages, but it remains unclear when explicit communication becomes necessary. We introduce CoLA (Coordination via Learned Adapters), which keeps each agent's VLA backbone frozen and trains a lightweight message channel and a per-arm diffusion action head on top, with fully decentralised execution. Across three tasks that differ in how much each agent can observe, the cha...

</details>

<details>
<summary>Share</summary>

```
CoLA: Multi-VLA Coordination via Learned Adapters

Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies.

arXiv: https://arxiv.org/abs/2610.15337
Code: https://github.com/Ahaskar04/CoLA.git

#VLA #robotics
```

</details>

---

### [AUGUstus: Autonomous Driving VLA Model with Unified Generation and Understanding](https://arxiv.org/abs/2610.16985)

**Authors:** Yuqi Ye, Caigao Jiang, Zhuonan Wang, Congyuan Pei, Chao Qu et al. (15 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16985) | [PDF](https://arxiv.org/pdf/2610.16985) | [Project Page](https://augustus-ad.github.io)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models show strong potential for end-to-end autonomous driving by leveraging world knowledge and understanding to excel in long-tail scenarios. However, current VLAs have two limitations: 1) Degeneration into vision-action (VA) models. For low latency, regression/flow-based methods directly generate actions but underuse VLM understanding, causing unsafe, unexplainable actions. 2) Autoregressive high latency. Autoregressive methods sequentially generate chain-of-thought (CoT) and action tokens, fully leveraging VLM understanding, but high latency hinders deployment....

</details>

<details>
<summary>Share</summary>

```
AUGUstus: Autonomous Driving VLA Model with Unified Generation and Understanding

Vision-language-action (VLA) models show strong potential for end-to-end autonomous driving by leveraging world knowledge and understanding to excel in long-tail scenarios.

arXiv: https://arxiv.org/abs/2610.16985
Project page: https://augustus-ad.github.io

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

### [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](https://arxiv.org/abs/2610.20504)

**Authors:** Xiaoman Li, Zhiqiang Yang, Jiayu Hu, Jipeng Kong, Yang Zhang et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20504) | [PDF](https://arxiv.org/pdf/2610.20504) | [Project Page](https://gr-bc.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations, failed attempts, and imperfect recoveries. The key challenge is to identify which action chunks actually advance the task, rather than uniformly cloning or discarding imperfect trajectories. We propose Graph-Reweighted Behavior Cloning (GR-BC), an offline iterative post-training framework that builds a task-conditioned goal-reachability graph over demonstrations and iteratively co...

</details>

<details>
<summary>Share</summary>

```
Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation

Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations,...

arXiv: https://arxiv.org/abs/2610.20504
Project page: https://gr-bc.github.io/

#VLA #robotics
```

</details>

---

### [One-shot Human Video-Guided Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.19746)

**Authors:** Qi Chen, Yuwei Wu, Quan Chen, Kunpeng Gao, Jin Chen et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19746) | [PDF](https://arxiv.org/pdf/2610.19746)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios. To reduce this dependence on target-task robot data, we propose CapPro, a framework that enables a...

</details>

<details>
<summary>Share</summary>

```
One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation.

arXiv: https://arxiv.org/abs/2610.19746

#VLA #robotics
```

</details>

---

### [ACRO: Actor-Critic Rollout Orchestration](https://arxiv.org/abs/2610.19677)

**Authors:** Junhoo Lee, Seungyeon Kim, Baekseung Kim, Minkyu Kim, Suhyun Jeon et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19677) | [PDF](https://arxiv.org/pdf/2610.19677) | [Project Page](https://junhoo.me/acro)

<details>
<summary>Abstract</summary>

Executing a vision-language-action (VLA) policy involves deciding when to continue an attempt and when to intervene to improve its chances of success. We introduce ACRO, an Actor--Critic rollout orchestration layer that makes these decisions for a fixed VLA. ACRO seeks interventions that offer a more promising continuation, are physically feasible, and leave sufficient time to complete the task. A Critic learned from policy rollouts estimates success prospects to decide when to intervene and select a re-entry target along the executed trajectory. Trajectory Retraction shortcuts the visited pat...

</details>

<details>
<summary>Share</summary>

```
ACRO: Actor-Critic Rollout Orchestration

Executing a vision-language-action (VLA) policy involves deciding when to continue an attempt and when to intervene to improve its chances of success.

arXiv: https://arxiv.org/abs/2610.19677
Project page: https://junhoo.me/acro

#VLA #robotics
```

</details>

---

### [ForceBench: Benchmarking Force Integration for Robotic Manipulation](https://arxiv.org/abs/2610.19604)

**Authors:** Xuan Han, Zinuo Jin, Tianlin Li, Yunfan Lou, Xin Liu et al. (11 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19604) | [PDF](https://arxiv.org/pdf/2610.19604) | [Project Page](https://forcebench-platform.github.io/)

<details>
<summary>Abstract</summary>

Force feedback provides vision-language-action (VLA) policies with physical observations that can guide action selection and execution. However, differences in tasks, demonstrations, and control settings across existing systems hinder reliable comparisons of force integration designs. We introduce ForceBench, a simulation benchmark for evaluating six-axis wrist-force integration under a unified protocol. ForceBench combines eight tasks spanning physical-property inference, resistance-dependent interaction, and contact-rich assembly with 1,600 synchronized demonstrations and task-specific succe...

</details>

<details>
<summary>Share</summary>

```
ForceBench: Benchmarking Force Integration for Robotic Manipulation

Force feedback provides vision-language-action (VLA) policies with physical observations that can guide action selection and execution.

arXiv: https://arxiv.org/abs/2610.19604
Project page: https://forcebench-platform.github.io/

#VLA #robotics
```

</details>

---

### [Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](https://arxiv.org/abs/2610.19600)

**Authors:** Zixuan Wang, Jia-Ning Li, Yinzhou Tang, Yanzhao Yu, Biao Wu et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19600) | [PDF](https://arxiv.org/pdf/2610.19600) | [Code](https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation.git)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone. To uncover these bottlenecks, we systematically diagnose failures in long-horizon mobile manipulation and identify three...

</details>

<details>
<summary>Share</summary>

```
Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System

Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation.

arXiv: https://arxiv.org/abs/2610.19600
Code: https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation.git

#VLA #robotics
```

</details>

---

### [VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning](https://arxiv.org/abs/2610.19517)

**Authors:** Diyuan Shi, Yiqi Tang, Hongyin Zhang, You Wu, Donglin Wang

**Published:** 2026-10-14 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19517) | [PDF](https://arxiv.org/pdf/2610.19517)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation. However, conventional pretrained VLA policies lack a mechanism for gradual adaptation through accumulated interaction experience during deployment. We therefore propose VLRLA, a general framework that equips existing VLA models with \textit{in-context reinforcement learning} capabilities for deployment-time adaptation. Our approach augments a VLA model with a reinforcement learning module that learns from historical observ...

</details>

<details>
<summary>Share</summary>

```
VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning

Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation.

arXiv: https://arxiv.org/abs/2610.19517

#VLA #robotics
```

</details>

---

### [The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover](https://arxiv.org/abs/2610.17746)

**Authors:** Yiqing Xu, Jiajun Wu

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17746) | [PDF](https://arxiv.org/pdf/2610.17746) | [Project Page](https://commgap.github.io/)

<details>
<summary>Abstract</summary>

A robot may know how to perform a task yet fail when a human asks for it naturally. We study this human--VLA communication gap by separating an \emph{information gap}, where task semantics, grounding, or event structure remain unresolved, from a residual \emph{execution gap}, where even a fully specified task depends on how it is organized and invoked. To do this, we characterize how people naturally express demonstrated objectives and evaluate controlled variants of the same physical tasks, with detailed analysis on $π_{0.5}$ and consistent trends on $π_0$-FAST and Cosmos3-Edge. Our study rev...

</details>

<details>
<summary>Share</summary>

```
The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover

A robot may know how to perform a task yet fail when a human asks for it naturally.

arXiv: https://arxiv.org/abs/2610.17746
Project page: https://commgap.github.io/

#VLA #robotics
```

</details>

---

### [Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?](https://arxiv.org/abs/2610.16634)

**Authors:** Zihan You, Zehua Fan, Wenqi Lyu, Aoqi Wang, Ni Wang et al. (22 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16634) | [PDF](https://arxiv.org/pdf/2610.16634)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models increasingly use natural-language instructions to condition autonomous driving behavior. Yet existing closed-loop benchmarks primarily measure route completion, safety, and rule compliance, leaving a fundamental question unresolved: does language actually determine which feasible behavior the vehicle executes? A trajectory may be safe and successful while still violating or even ignoring the passenger's instruction. To address this, we introduce \ltd, a benchmark designed to directly test this capability. Its key evaluation unit, the paired counterfac...

</details>

<details>
<summary>Share</summary>

```
Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?

Recent Vision-Language-Action (VLA) models increasingly use natural-language instructions to condition autonomous driving behavior.

arXiv: https://arxiv.org/abs/2610.16634

#VLA #robotics
```

</details>

---

### [VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2610.16567)

**Authors:** Jun Xiao, Rui Ye, Dong Cao, Jinyu Gu, Ying Wang et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16567) | [PDF](https://arxiv.org/pdf/2610.16567)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable task representation. It combines (1) paired in-distribution and out-of-distribution tasks across six c...

</details>

<details>
<summary>Share</summary>

```
VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models

Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness.

arXiv: https://arxiv.org/abs/2610.16567

#VLA #robotics
```

</details>

---

### [Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors](https://arxiv.org/abs/2610.15556)

**Authors:** Yeonseok Lee

**Published:** 2026-10-11 | **Categories:** cs.LO, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15556) | [PDF](https://arxiv.org/pdf/2610.15556) | [Code](https://github.com/ylee-sling/Vision-Predictor-Action)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency. We present Goal-Conditioned Vision-Predictor-Action (VPA), which replaces autoregressive decoders with a lightweight latent control loop. A shared vision encoder and a frozen text encoder embed observations, goal images, and instructions; a neuro-symbolic selector chooses a discrete skill; a Joint-Embedding Predictive Architecture (JEPA) predictor forecasts the ne...

</details>

<details>
<summary>Share</summary>

```
Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop co...

arXiv: https://arxiv.org/abs/2610.15556
Code: https://github.com/ylee-sling/Vision-Predictor-Action

#VLA #robotics
```

</details>

---

### [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425)

**Authors:** Xupeng Zhang, Yantai Yang, Chang Guo, Zhaokai Yin, Zhipeng Zhang

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15425) | [PDF](https://arxiv.org/pdf/2610.15425) | [Code](https://github.com/AutoLab-SAI-SJTU/RoboCombine)

<details>
<summary>Abstract</summary>

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination. The full instruction route treats skill chaining as long-horizon imitation. In a controlled study, full instruction training on limited skill combination sequences reaches 40.0% ordered success on covered combinations but only 7.7% on recombination, suggesting memorization of sequence templates rather than robust skill recombination. We introduce Hierarchical Subtask Execution (HSE), a diagno...

</details>

<details>
<summary>Share</summary>

```
Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination.

arXiv: https://arxiv.org/abs/2610.15425
Code: https://github.com/AutoLab-SAI-SJTU/RoboCombine

#VLA #robotics
```

</details>

---

### [Verify, Act, Distill: Turning Test-Time Compute into Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.14885)

**Authors:** Kaneyoshi Hiratsuka, Satoshi Yamamori, Jun Morimoto

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14885) | [PDF](https://arxiv.org/pdf/2610.14885)

<details>
<summary>Abstract</summary>

Test-time compute (TTC), which scores multiple candidate actions at inference time, is a powerful way to improve the execution performance of vision-language-action (VLA) models, but existing methods keep the policy frozen, so the gain must be recomputed at every execution. We propose Verify, Act, Distill, a framework that consolidates the gains of TTC into the VLA itself. A fixed verifier scores candidates generated by a flow-matching VLA, the weighted aggregate is executed, and the observations and aggregated chunks from successful adaptation episodes are distilled directly into LoRA paramet...

</details>

<details>
<summary>Share</summary>

```
Verify, Act, Distill: Turning Test-Time Compute into Test-Time Adaptation for Vision-Language-Action Models

Test-time compute (TTC), which scores multiple candidate actions at inference time, is a powerful way to improve the execution performance of vision-language-action (VLA) models, but existing methods keep the policy f...

arXiv: https://arxiv.org/abs/2610.14885

#VLA #robotics
```

</details>

---

### [Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies](https://arxiv.org/abs/2610.14588)

**Authors:** Chen Zhao, Zipeng Ye, Haitao Shen, Guanlin Li, Yuchen Xie et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14588) | [PDF](https://arxiv.org/pdf/2610.14588)

<details>
<summary>Abstract</summary>

Test-time sampling promises to turn one action prediction into a set of distinct executable candidates that a verifier can choose among. Downstream fine-tuning works against that promise. A vision-language-action model trained to solve one task distribution concentrates its flow-matching decoder around the dominant demonstrated action, so repeated samples differ only marginally and the verifier receives many copies of one decision. We call this proposal contraction and identify it as a key constraint on test-time scaling: repeated samples can remain highly redundant as the candidate budget gro...

</details>

<details>
<summary>Share</summary>

```
Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies

Test-time sampling promises to turn one action prediction into a set of distinct executable candidates that a verifier can choose among.

arXiv: https://arxiv.org/abs/2610.14588

#VLA #robotics
```

</details>

---

### [CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance](https://arxiv.org/abs/2610.14936)

**Authors:** Shutong Ding, Zhaoyang Liu, Yimiao Zhou, Jingya Wang, Jiayuan Gu et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14936) | [PDF](https://arxiv.org/pdf/2610.14936) | [Project Page](https://zhy-liu.github.io/cfg-policy-page)

<details>
<summary>Abstract</summary>

Diffusion policies are increasingly used in robotic control and manipulation, vision-language-action models, and world-model-based agents. Their ability to represent multimodal action distributions offers rich opportunities for exploration in reinforcement learning (RL). However, optimizing diffusion policies with RL can reduce the behavioral diversity and further limit their exploration capability. In RL post-training, directly fine-tuning a pretrained policy may also disrupt its acquired capabilities, while action-space residuals may lack the expressive power for multimodal exploration. Toge...

</details>

<details>
<summary>Share</summary>

```
CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance

Diffusion policies are increasingly used in robotic control and manipulation, vision-language-action models, and world-model-based agents.

arXiv: https://arxiv.org/abs/2610.14936
Project page: https://zhy-liu.github.io/cfg-policy-page

#VLA #robotics
```

</details>

---

### [SPECTRA-VLA: Base-Fine Hyperspectral Token Transfer at Frozen Vision-Language-Action Interfaces](https://arxiv.org/abs/2610.19651)

**Authors:** Chih-Chung Hsu

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19651) | [PDF](https://arxiv.org/pdf/2610.19651)

<details>
<summary>Abstract</summary>

Hyperspectral imaging distinguishes RGB-similar objects, but a pretrained vision-language-action model needs a state its frozen decoder can use. SPECTRA-VLA provides a native-width spectral upgrade without retraining the visual encoder or action decoder. A learned continuous residual enriches each target token through its own normalized false-color reference; projection, norm control and validation-calibrated injection regulate the change. Across 86 held-out acquisitions, category balanced accuracy rises from 0.812 to 0.883. With identical residuals and scale, own-token addition improves reuse...

</details>

<details>
<summary>Share</summary>

```
SPECTRA-VLA: Base-Fine Hyperspectral Token Transfer at Frozen Vision-Language-Action Interfaces

Hyperspectral imaging distinguishes RGB-similar objects, but a pretrained vision-language-action model needs a state its frozen decoder can use.

arXiv: https://arxiv.org/abs/2610.19651

#VLA #robotics
```

</details>

---

### [LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](https://arxiv.org/abs/2610.16782)

**Authors:** Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang, Boning Tan, Liangna Fu et al. (12 authors)

**Published:** 2026-10-12 (updated 2026-10-15) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16782) | [PDF](https://arxiv.org/pdf/2610.16782) | [Project Page](https://IAIE-PhysicalAI.github.io/LIBERO-Industry/)

<details>
<summary>Abstract</summary>

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap, we introduce LIBERO-Industry, a novel benchmark built on the widely used robot learning benchmark L...

</details>

<details>
<summary>Share</summary>

```
LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions.

arXiv: https://arxiv.org/abs/2610.16782
Project page: https://IAIE-PhysicalAI.github.io/LIBERO-Industry/

#VLA #robotics
```

</details>

---

### [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474)

**Authors:** Peidong Wang, Ying Chang, Zhiming Ma, Xiaocui Yang, Shi Feng et al. (11 authors)

**Published:** 2026-10-14 | **Categories:** cs.CL, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20474) | [PDF](https://arxiv.org/pdf/2610.20474)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose AdaRSI, an on-demand RSI framework for embodied agents. A coding agent first improves its skills and h...

</details>

<details>
<summary>Share</summary>

```
AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks.

arXiv: https://arxiv.org/abs/2610.20474

#VLA #robotics
```

</details>

---

### [When Do Discrete Actions Make Good Continuous Controllers?](https://arxiv.org/abs/2610.20429)

**Authors:** Zeji Yi, Soham Dasgupta, Xinyang Zhang, Koushil Sreenath, Guannan Qu et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20429) | [PDF](https://arxiv.org/pdf/2610.20429) | [Project Page](https://iscoyizj.github.io/discrete-action-website/)

<details>
<summary>Abstract</summary>

Though modern AI models like LLMs predict discrete tokens, today's robotic foundation models represent actions as continuous vectors. In this paper, we challenge this common consensus by asking if continuous action parametrizations are superior to their discrete counterparts. We conduct an extensive comparison of single-step regression and multi-step flow variants of both continuous and discrete policies in both from-scratch single-task and multi-task VLA training, in both simulation and on real hardware. In all regimes, we find that discrete action prediction, even the most naive, uniform-bin...

</details>

<details>
<summary>Share</summary>

```
When Do Discrete Actions Make Good Continuous Controllers?

Though modern AI models like LLMs predict discrete tokens, today's robotic foundation models represent actions as continuous vectors.

arXiv: https://arxiv.org/abs/2610.20429
Project page: https://iscoyizj.github.io/discrete-action-website/

#VLA #robotics
```

</details>

---

### [MorphAct: Robot Policies Morphing with the Worlds They Act In](https://arxiv.org/abs/2610.20019)

**Authors:** Ziyan Liu, Jiting Liu, Weihong Zhong, Wenda Yu, Yeqiu Chen et al. (10 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20019) | [PDF](https://arxiv.org/pdf/2610.20019) | [Project Page](https://mint-sjtu.github.io/MorphAct.io/)

<details>
<summary>Abstract</summary>

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When different operations favor competing parameter adjustments, fitting their mixture can leave individual operations insufficiently adapted. Our atomic-task diagnostics reveal competing update directions in both vision-language and action parameters, with source-improving updates increasing loss on other tasks. This motivates MorphAct, a contextual paramete...

</details>

<details>
<summary>Share</summary>

```
MorphAct: Robot Policies Morphing with the Worlds They Act In

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions.

arXiv: https://arxiv.org/abs/2610.20019
Project page: https://mint-sjtu.github.io/MorphAct.io/

#VLA #robotics
```

</details>

---

### [Accelerating VLA Inference with Perturbation Informed Execution](https://arxiv.org/abs/2610.19656)

**Authors:** Jehun Lee, Hajun Lee, Jimin Ryu, Youhan Lee, Beomseok Kang et al. (7 authors)

**Published:** 2026-10-14 (updated 2026-10-15) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19656) | [PDF](https://arxiv.org/pdf/2610.19656)

<details>
<summary>Abstract</summary>

Action-chunking vision-language-action (VLA) models predict sequences of future robot actions. Under fixed-horizon execution, the robot executes a fixedlength prefix of each predicted chunk before invoking the policy again, leaving the remaining predictions unused. For a given number of executed actions, short execution horizons require more policy calls. Extending the execution horizon amortizes policy inference cost over more actions. However, uniformly applying long horizons across episodes can limit opportunities for precise corrections. To address this limitation, we propose PICES (Pertur...

</details>

<details>
<summary>Share</summary>

```
Accelerating VLA Inference with Perturbation Informed Execution

Action-chunking vision-language-action (VLA) models predict sequences of future robot actions.

arXiv: https://arxiv.org/abs/2610.19656

#VLA #robotics
```

</details>

---

### [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2610.19479)

**Authors:** Liqian Ma, Vaibhav Saxena, Utkarsh Aashu Mishra, Shuo Cheng, Yongxin Chen et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19479) | [PDF](https://arxiv.org/pdf/2610.19479) | [Project Page](https://meta-gensim.github.io)

<details>
<summary>Abstract</summary>

Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data. However, existing approaches typically treat simulators as fixed data sources, relying on uniform generation, offline retrieval, or manual parameter alignment by domain experts. We formulate \textit{Active Generative Simulation}: optimizing a simulator's data-generation distribution to maximize downstream real-world performance. To solve this problem, we propose MetaGenSim, a meta-learning framework that trains an auxiliary rater network via meta-gradients...

</details>

<details>
<summary>Share</summary>

```
Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training

Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data.

arXiv: https://arxiv.org/abs/2610.19479
Project page: https://meta-gensim.github.io

#VLA #robotics
```

</details>

---

### [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](https://arxiv.org/abs/2610.19438)

**Authors:** Hanlong Li, Sihan Tan, Takeshi Ashizawa, Benjamin Yen, Kazuhiro Nakadai

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19438) | [PDF](https://arxiv.org/pdf/2610.19438)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies fine-tuned on LIBERO are trained and evaluated on the same ten instruction strings, and rewording the instruction changes base OpenVLA's success by -38.0 points. Test-time prompt ensembling, which improves language models, does not recover this loss in any setting we ran. Paraphrase consensus (the medoid action over K paraphrases) costs base OpenVLA 16.8 points when the training instruction is a member. Without it, the medoid of the paraphrases scores -32.4 points relative to the training instruction, and confidence-based selection scores -28.0. The same m...

</details>

<details>
<summary>Share</summary>

```
Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies

Vision-language-action (VLA) policies fine-tuned on LIBERO are trained and evaluated on the same ten instruction strings, and rewording the instruction changes base OpenVLA's success by -38.0 points.

arXiv: https://arxiv.org/abs/2610.19438

#VLA #robotics
```

</details>

---

### [ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures](https://arxiv.org/abs/2610.18650)

**Authors:** Chenru Wen, Huajian Zeng, Haokai Ding, Jian Kang, Anqing Duan et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18650) | [PDF](https://arxiv.org/pdf/2610.18650)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution. Recovery is typically learned during policy training or delegated to a monitor that triggers a scripted repair after detecting a failure. We introduce ForkCast, a predictive recovery framework that compares counterfactual futures to determine whether and how to intervene in a frozen VLA policy. At each decision point, ForkCast evaluates three candidates: executing the policy's nominal action chunk (Commit), adjusting the came...

</details>

<details>
<summary>Share</summary>

```
ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution.

arXiv: https://arxiv.org/abs/2610.18650

#VLA #robotics
```

</details>

---

### [ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models](https://arxiv.org/abs/2610.18596)

**Authors:** Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18596) | [PDF](https://arxiv.org/pdf/2610.18596) | [Project Page](https://accrue-rl.github.io)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency without addressing learner persistence across tasks. We propose ACCRUE, a continual off-policy RL framework that carries lightweight actor and critic networks across tasks, allowin...

</details>

<details>
<summary>Share</summary>

```
ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired...

arXiv: https://arxiv.org/abs/2610.18596
Project page: https://accrue-rl.github.io

#VLA #robotics
```

</details>

---

### [WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568)

**Authors:** Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18568) | [PDF](https://arxiv.org/pdf/2610.18568)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly large-scale video pretraining. We introduce WAVE-0 (World-model-Augmented VLA Execution), a framework that bridges VLAs and WAMs through a lightweight latent world model. By connectin...

</details>

<details>
<summary>Share</summary>

```
WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences.

arXiv: https://arxiv.org/abs/2610.18568

#VLA #robotics
```

</details>

---

### [YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation](https://arxiv.org/abs/2610.17521)

**Authors:** Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17521) | [PDF](https://arxiv.org/pdf/2610.17521) | [Project Page](https://yubi-real2sim.airoa.io)

<details>
<summary>Abstract</summary>

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation. While 3D Gaussian Splatting (3DGS) enables rapid real-to-sim scene generation, the reconstruction quality required for reliable policy evaluation remains unquantified. In particular, policies relying on wrist-mounted fisheye cameras (e.g., YUBI handheld gripper data) are heavily exposed to visual artifacts (holes, floaters) in wide-angle views, directly degrading task performance. To address this, we present YUBI-Real2Sim, a unified fram...

</details>

<details>
<summary>Share</summary>

```
YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation.

arXiv: https://arxiv.org/abs/2610.17521
Project page: https://yubi-real2sim.airoa.io

#VLA #robotics
```

</details>

---

### [End-to-End Vision-Language-Action Policies for Autonomous Lunar Rover Docking](https://arxiv.org/abs/2610.19224)

**Authors:** Sitan Huang, Grace Gao

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19224) | [PDF](https://arxiv.org/pdf/2610.19224)

<details>
<summary>Abstract</summary>

Surface navigation on the Moon is subject to extreme illumination contrast and deployment-time perceptual disturbances. While modular navigation pipelines have long supported planetary rover navigation, robustness is compromised by measurement errors that propagate through hand-engineered components. End-to-end learned policies are an alternative approach to navigation, which maps observations directly to control actions without intermediate components. Vision-language-action models, in particular, have driven significant breakthroughs in robotics and autonomous vehicle research. By leveraging...

</details>

<details>
<summary>Share</summary>

```
End-to-End Vision-Language-Action Policies for Autonomous Lunar Rover Docking

Surface navigation on the Moon is subject to extreme illumination contrast and deployment-time perceptual disturbances.

arXiv: https://arxiv.org/abs/2610.19224

#VLA #robotics
```

</details>

---

### [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843)

**Authors:** Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang et al. (9 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18843) | [PDF](https://arxiv.org/pdf/2610.18843)

<details>
<summary>Abstract</summary>

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height, and gripper pads. Each axis has five severity lev...

</details>

<details>
<summary>Share</summary>

```
LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-eff...

arXiv: https://arxiv.org/abs/2610.18843

#VLA #robotics
```

</details>

---

### [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)

**Authors:** Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18774) | [PDF](https://arxiv.org/pdf/2610.18774) | [Project Page](https://greenvla.github.io/GreenWAM)

<details>
<summary>Abstract</summary>

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that describes 20 robot families, from bimanual arms to dexterous humanoids, in common joint coordinates; (...

</details>

<details>
<summary>Share</summary>

```
GreenWAM: A World Foundation Model for Robotics

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.

arXiv: https://arxiv.org/abs/2610.18774
Project page: https://greenvla.github.io/GreenWAM

#VLA #robotics
```

</details>

---

### [Trust-Calibrated VLA Policy Post-Training with Evolving Imagination](https://arxiv.org/abs/2610.16517)

**Authors:** Wenzhan Li, Yiran Qin, Heng Zhou, Huirui Wang, Yulan Guo et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.16517) | [PDF](https://arxiv.org/pdf/2610.16517)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage. Existing refinement paradigms expose a reliability--efficiency tension: model-free refinement avoids simulator bias but is interaction-intensive, whereas model-based refinement can exploit unreliable imagination even as its simulator adapts. We propose Model-Evolving Reinforcement Learning (MERL), a trust-calibrated framework that couples policy optimization with an online-updated simulator comprising a...

</details>

<details>
<summary>Share</summary>

```
Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage.

arXiv: https://arxiv.org/abs/2610.16517

#VLA #robotics
```

</details>

---

### [Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks](https://arxiv.org/abs/2610.16238)

**Authors:** Zhi Han, Zihan Guo, Chenxi Zeng, Zicai Cui, Yue Xin et al. (9 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16238) | [PDF](https://arxiv.org/pdf/2610.16238) | [Code](https://github.com/HanZhi306/EmbodiedSkill-Bench)

<details>
<summary>Abstract</summary>

LLM agents increasingly control robots using VLA policies, perception models, and procedural knowledge. These modules are difficult to reuse because their interfaces, embodiment assumptions, and conditions of use differ, and their benefits on physical tasks remain unclear. We package them as embodied skills that extend agent skills with explicit embodiment assumptions and conditions of use, building 250 action, perception, and experience skills from 1,052 resources. On this basis we introduce EmbodiedSkillBench, which runs an agent in a closed observation-action loop and records success, actio...

</details>

<details>
<summary>Share</summary>

```
Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks

LLM agents increasingly control robots using VLA policies, perception models, and procedural knowledge.

arXiv: https://arxiv.org/abs/2610.16238
Code: https://github.com/HanZhi306/EmbodiedSkill-Bench

#VLA #robotics
```

</details>

---

### [Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.15675)

**Authors:** Seongmin Park, Jaewon Lee, Yujun Heo, Yoonsik Kim, Seheon Choi et al. (7 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15675) | [PDF](https://arxiv.org/pdf/2610.15675)

<details>
<summary>Abstract</summary>

Quantization lowers deployment costs of vision-language-action (VLA) policies but can compromise task completion. Across five VLA models and 4,050 real-world trials, we systematically reveal that quantization-aware training (QAT) generally improves on post-training quantization (PTQ) but leaves substantial gaps to full precision (FP) on long-horizon tasks and under visual and semantic shifts, while its imitation-based objective does not explicitly use rollout success or partial completion. To exploit these outcome signals, we introduce Quantization-Conditioned Reinforcement Learning (QCRL), an...

</details>

<details>
<summary>Share</summary>

```
Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning

Quantization lowers deployment costs of vision-language-action (VLA) policies but can compromise task completion.

arXiv: https://arxiv.org/abs/2610.15675

#VLA #robotics
```

</details>

---

### [DEFT-VLA: Stage-Localized Force Specialization for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2610.14854)

**Authors:** Zan Huang, Yibo Qiu, Kan Ding, Xuanping Zhang, Ao Tian et al. (7 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14854) | [PDF](https://arxiv.org/pdf/2610.14854)

<details>
<summary>Abstract</summary>

Contact-rich manipulation poses a stage-dependent sensory conflict: vision and proprioception are essential for localization and approach, when force is largely uninformative and potentially distracting, whereas force becomes critical after contact, when irrelevant visual details and correlated robot states may become shortcuts. We propose DEFT-VLA (Dual-Expert Force-specialized Training for Vision-Language-Action Manipulation), which retains the task-adapted base expert for vision-dominated non-contact behavior and introduces a force-aware contact expert for critical contact stages, localizin...

</details>

<details>
<summary>Share</summary>

```
DEFT-VLA: Stage-Localized Force Specialization for Contact-Rich Robotic Manipulation

Contact-rich manipulation poses a stage-dependent sensory conflict: vision and proprioception are essential for localization and approach, when force is largely uninformative and potentially distracting, whereas force...

arXiv: https://arxiv.org/abs/2610.14854

#VLA #robotics
```

</details>

---

### [PRISM: Precision Forcing for Generalist Vision-Language-Action Policies](https://arxiv.org/abs/2610.14704)

**Authors:** Chenghao Yue, Peiyan Li, Hao Wang, Lei Lv, Jiahao Chen et al. (8 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14704) | [PDF](https://arxiv.org/pdf/2610.14704)

<details>
<summary>Abstract</summary>

Coupling a pretrained vision-language model (VLM) with a diffusion or flow-matching action expert has become the mainstream vision-language-action (VLA) paradigm for embodied policies, yet they remain unreliable once a task demands precise manipulation, e.g., submillimeter cable insertion. We attribute this weakness to a training objective that averages flow-matching errors across contexts and flow times, allocating little supervision to the few decisive moments determining task success. Along the generative path, inference integrates a locally supervised velocity field, so equally penalized e...

</details>

<details>
<summary>Share</summary>

```
PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

Coupling a pretrained vision-language model (VLM) with a diffusion or flow-matching action expert has become the mainstream vision-language-action (VLA) paradigm for embodied policies, yet they remain unreliable once...

arXiv: https://arxiv.org/abs/2610.14704

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

### [Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2610.19753)

**Authors:** Yiming Meng, Yanming Shao, Weijie Shen, Kunyang Lin, Jiayu Sun et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19753) | [PDF](https://arxiv.org/pdf/2610.19753)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand interactions implicit within a single action vector. We introduce Coordi-$π$, a structured action representation for bimanual dexterous manipulation. Coordi-$π$ represents the right- and left-side arm--hand actions as individual action tokens an...

</details>

<details>
<summary>Share</summary>

```
Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space.

arXiv: https://arxiv.org/abs/2610.19753

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

### [Towards Agentic Robots: Model, Data, Environment, and Harness](https://arxiv.org/abs/2610.20442)

**Authors:** Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu et al. (16 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.20442) | [PDF](https://arxiv.org/pdf/2610.20442)

<details>
<summary>Abstract</summary>

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic...

</details>

<details>
<summary>Share</summary>

```
Towards Agentic Robots: Model, Data, Environment, and Harness

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execut...

arXiv: https://arxiv.org/abs/2610.20442

#VLA #robotics
```

</details>

---

### [Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand](https://arxiv.org/abs/2610.20351)

**Authors:** Nagasrikanth Kallakuri

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20351) | [PDF](https://arxiv.org/pdf/2610.20351)

<details>
<summary>Abstract</summary>

Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots in industrial and general environments depends on. A human demonstration recorded on a simple and scalable device such as a mobile phone can serve as post-training data for a robot whose body differs in structure and capability from the human who recorded it. This is made possible not by retargeting the hand's motion but the object's. A capture yields a body-free record: the objec...

</details>

<details>
<summary>Share</summary>

```
Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand

Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots...

arXiv: https://arxiv.org/abs/2610.20351

#VLA #robotics
```

</details>

---

### [PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly](https://arxiv.org/abs/2610.19248)

**Authors:** Chang Liu, Sibo Tian, Litian Gong, Zhiwen Fan, Jiachen Li et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.19248) | [PDF](https://arxiv.org/pdf/2610.19248)

<details>
<summary>Abstract</summary>

Robotic disassembly of end-of-life (EoL) products requires robots to accommodate product variation, follow prerequisite sequences, and approach components precisely for contact-rich manipulation. Supervised fine-tuning (SFT) provides a practical path for adaptation, but limited and costly disassembly data cannot capture the distribution shifts arising from changing environments and product uncertainties. The policy's own rollouts record its approach attempts, and human corrections demonstrate recovery from its errors, but turning these experiences into better policy performance remains challen...

</details>

<details>
<summary>Share</summary>

```
PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly

Robotic disassembly of end-of-life (EoL) products requires robots to accommodate product variation, follow prerequisite sequences, and approach components precisely for contact-rich manipulation.

arXiv: https://arxiv.org/abs/2610.19248

#VLA #robotics
```

</details>

---

### [ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874)

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18874) | [PDF](https://arxiv.org/pdf/2610.18874)

<details>
<summary>Abstract</summary>

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present Chunk...

</details>

<details>
<summary>Share</summary>

```
ChunkAct: Action Chunking for Agentic Robotics

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes...

arXiv: https://arxiv.org/abs/2610.18874

#VLA #robotics
```

</details>

---

### [EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning](https://arxiv.org/abs/2610.18790)

**Authors:** Haodong Yang, Runhan Huang, Bowen Zhang, Iofai Lei, Zunzhe Zhang et al. (10 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18790) | [PDF](https://arxiv.org/pdf/2610.18790)

<details>
<summary>Abstract</summary>

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve. We introduce Equilibrium Energy Control (EqC), a framework for introspective lifelong robot learning built around an explicit conditional energy landscape. EqC casts generative action refinement as equilibrium-seeking optimization, while the geometry of the refinement process reveals whether the generated behavior remains consistent with the learned landscape. This competence signal enables Energy-Gated DAgger, w...

</details>

<details>
<summary>Share</summary>

```
EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve.

arXiv: https://arxiv.org/abs/2610.18790

#VLA #robotics
```

</details>

---

### [Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments](https://arxiv.org/abs/2610.18381)

**Authors:** Zhibo Duan, Hanlin Kong, Tianran Ma, Yuze Wu, Yuxuan Xu et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18381) | [PDF](https://arxiv.org/pdf/2610.18381)

<details>
<summary>Abstract</summary>

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the same trajectories. Existing aerial benchmarks are typically confined to single-environment settings, limiting evaluation of agents across continuous environmental transitions. When interaction is evaluated, agents are often initialized near the target, leaving the transition from navigation to interaction largely unassessed. This work introduces CrossFly, a benchmark for long-horizon...

</details>

<details>
<summary>Share</summary>

```
Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the sam...

arXiv: https://arxiv.org/abs/2610.18381

#VLA #robotics
```

</details>

---

### [DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations](https://arxiv.org/abs/2610.18373)

**Authors:** Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.18373) | [PDF](https://arxiv.org/pdf/2610.18373)

<details>
<summary>Abstract</summary>

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-invariant scene representation (DISR). The framework combines vision-language understanding and laten...

</details>

<details>
<summary>Share</summary>

```
DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways.

arXiv: https://arxiv.org/abs/2610.18373

#VLA #robotics
```

</details>

---

### [Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance](https://arxiv.org/abs/2610.17983)

**Authors:** Mohammed Daba, Waleed Abdulrahman Saleh AlAkwa

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.17983) | [PDF](https://arxiv.org/pdf/2610.17983)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets. However, these models frequently suffer from distributional convergence, a phenomenon where the policy regresses to "safe" but suboptimal mean behaviors due to mode averaging in the training data. This often results in generic grasp strategies, Convergent Defaults, that fail in constrained or long-tail scenarios. In this work, we propose a novel framework to identify and correct these behaviors without parameter updates. We...

</details>

<details>
<summary>Share</summary>

```
Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets.

arXiv: https://arxiv.org/abs/2610.17983

#VLA #robotics
```

</details>

---

### [Post-Training, Finetuning, and Steering:A Field Guide for Curating Training Data](https://arxiv.org/abs/2610.19143)

**Authors:** Maria Attarian, Yifan Ruan, Claas Voelcker, Chenyang Cao, Amy Zhang et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19143) | [PDF](https://arxiv.org/pdf/2610.19143)

<details>
<summary>Abstract</summary>

While Vision-Language-Action models have enabled impressive cross-task transfer in zero-shot settings, \emph{adaptation} methods are often necessary to achieve consistent performance on novel tasks. However, even though a wealth of methods for adaptation have been proposed, it is unclear how to choose the best method based on available trajectories. We close this gap by studying the impact of the adaptation method under a variety of common data scenarios: on- and off-policy data, offline vs online adaptation, and whether the data contains optimal or suboptimal trajectories. Our evaluation span...

</details>

<details>
<summary>Share</summary>

```
Post-Training, Finetuning, and Steering:A Field Guide for Curating Training Data

While Vision-Language-Action models have enabled impressive cross-task transfer in zero-shot settings, \emph{adaptation} methods are often necessary to achieve consistent performance on novel tasks.

arXiv: https://arxiv.org/abs/2610.19143

#VLA #robotics
```

</details>

---

### [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792)

**Authors:** Xinyi Wang, Bangzheng Li, Hanyu Wang, Lin Zhang, Andrea Yaoyun Cui et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18792) | [PDF](https://arxiv.org/pdf/2610.18792)

<details>
<summary>Abstract</summary>

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fin...

</details>

<details>
<summary>Share</summary>

```
SEAR: Self-Evolving Agentic Robotics

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task.

arXiv: https://arxiv.org/abs/2610.18792

#VLA #robotics
```

</details>

---

### [UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation](https://arxiv.org/abs/2610.16969)

**Authors:** Lei Yao, Qiao Feng, Mutian Tong, Qihao Yun, Lap-Pui Chau et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16969) | [PDF](https://arxiv.org/pdf/2610.16969)

<details>
<summary>Abstract</summary>

Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action. Recent continuous alternatives mitigate this, but they are typically used as proxies for world modeling and require a further planning step to produce executable actions. We thus introduce UniLAP, a unified continuous latent-action policy that models the latent space via flow matching and bypasses reliance on future frames during inference. By distilling a LAM teacher with a flow-adaptive obje...

</details>

<details>
<summary>Share</summary>

```
UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation

Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action.

arXiv: https://arxiv.org/abs/2610.16969

#VLA #robotics
```

</details>

---

### [Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA](https://arxiv.org/abs/2610.16313)

**Authors:** Jiaqi Fan, Rui Xu, Jiakun Xia, Xuyu Fan, Shuailei Ma et al. (10 authors)

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16313) | [PDF](https://arxiv.org/pdf/2610.16313)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation. However, many manipulation tasks depend on auditory cues that cannot be reliably inferred from visual observations and may need to be elicited through physical interaction. To address this gap, we present ListenVLA, an audio-conditioned VLA policy built on GR00T N1.7 for sound-guided manipulation. ListenVLA combines semantic audio embeddings with waveform-derived acoustic cues over a causal audio history and conditions continuous action generati...

</details>

<details>
<summary>Share</summary>

```
Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA

Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation.

arXiv: https://arxiv.org/abs/2610.16313

#VLA #robotics
```

</details>

---

### [FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning](https://arxiv.org/abs/2610.16160)

**Authors:** Junhyeong Go, Mingyu Jung, Woobin Im, Jongbin Ryu

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16160) | [PDF](https://arxiv.org/pdf/2610.16160)

<details>
<summary>Abstract</summary>

Recent advances in 3D reconstruction enable the extraction of temporally consistent 3D motion from RGB observations; however, current Vision-Language-Action (VLA) models still predominantly rely on 2D image-text priors. Therefore, they do not accurately represent the fundamental dynamics of the 3D world associated with physical actions. This over-reliance on static 2D visual cues limits the capacity of VLA models in achieving robust robot manipulation. To address these limitations, we introduce FlowVLA, a reconstruction-guided, pluggable 3D flow learning framework aimed at empowering VLA model...

</details>

<details>
<summary>Share</summary>

```
FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning

Recent advances in 3D reconstruction enable the extraction of temporally consistent 3D motion from RGB observations; however, current Vision-Language-Action (VLA) models still predominantly rely on 2D image-text priors.

arXiv: https://arxiv.org/abs/2610.16160

#VLA #robotics
```

</details>

---

### [SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation](https://arxiv.org/abs/2610.15766)

**Authors:** Angen Ye, junjie xie, Yujia Song, Junkai Huang, Dapeng Zhang

**Published:** 2026-10-11 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15766) | [PDF](https://arxiv.org/pdf/2610.15766)

<details>
<summary>Abstract</summary>

Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficient precision, opaque decisions, and scarce data. This paper presents SurgiCLAW, a hierarchical skill-based framework for precision surgical manipulation. SurgiCLAW confines an MLLM to intraoperative visual understanding, structured explanation, and atomic surgical-skill selection, while delegating physical execution to...

</details>

<details>
<summary>Share</summary>

```
SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation

Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning.

arXiv: https://arxiv.org/abs/2610.15766

#VLA #robotics
```

</details>

---

### [Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution](https://arxiv.org/abs/2610.14997)

**Authors:** Wenbo Yu, Jifan Li, Wenke Xia, Yuchen Li, Yizhuo Zhang et al. (8 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.14997) | [PDF](https://arxiv.org/pdf/2610.14997)

<details>
<summary>Abstract</summary>

While asynchronous execution enables VLA models to operate in real-time environments by predicting the next chunk during execution, it inevitably introduces boundary misalignment with the committed action stream. Existing delay-aware solutions address this at the prohibitive cost of extensive retraining, architectural modifications, or fixed-prefix inpainting that inflates computation when low latency is vital. To address these problems, we propose FreeBar, a training-free real-time inference plugin that enables robust asynchronous execution with only marginal additional inference cost by cast...

</details>

<details>
<summary>Share</summary>

```
Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution

While asynchronous execution enables VLA models to operate in real-time environments by predicting the next chunk during execution, it inevitably introduces boundary misalignment with the committed action stream.

arXiv: https://arxiv.org/abs/2610.14997

#VLA #robotics
```

</details>

---

### [ADAPT: Audio-Depth Action Planning with Transition-Aware Rewards for Lights-Out Industrial Navigation](https://arxiv.org/abs/2610.15956)

**Authors:** Wenjun Huang, Shenghao Fu, Yian Jin, Yang Ni, Yifan Li et al. (15 authors)

**Published:** 2026-10-11 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.15956) | [PDF](https://arxiv.org/pdf/2610.15956)

<details>
<summary>Abstract</summary>

Vision-language-action models for embodied navigation typically rely on RGB observations, limiting their applicability in lights-out industrial environments where visible illumination may be unavailable. We study illumination-independent navigation using spatial audio for target localization and depth for obstacle-aware geometry. To support this setting, we introduce DarkNav-Bench, a benchmark with 24 industrial scenes and four progressively challenging acoustic conditions. We further propose ADAPT, an audio-depth action-planning framework equipped with spatial-audio perception and optimized f...

</details>

<details>
<summary>Share</summary>

```
ADAPT: Audio-Depth Action Planning with Transition-Aware Rewards for Lights-Out Industrial Navigation

Vision-language-action models for embodied navigation typically rely on RGB observations, limiting their applicability in lights-out industrial environments where visible illumination may be unavailable.

arXiv: https://arxiv.org/abs/2610.15956

#VLA #robotics
```

</details>

---

### [A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding](https://arxiv.org/abs/2610.15666)

**Authors:** Abdollah Pourasghari, Saeedeh Sadat Sadidpour, Mohammad Roustaei

**Published:** 2026-10-11 | **Categories:** cs.CV, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.15666) | [PDF](https://arxiv.org/pdf/2610.15666)

<details>
<summary>Abstract</summary>

Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-grounded environments, and largely assume instructions are clear and executable. We introduce the first Persian vision-language-action dataset for this task: 258 instances over 230 real household/office photographs, annotated with reference plans, deliberate ambiguity and infeasibility labels, disambiguating question-answer pairs, and an auto-generated chain-of-thought rationale f...

</details>

<details>
<summary>Share</summary>

```
A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding

Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-...

arXiv: https://arxiv.org/abs/2610.15666

#VLA #robotics
```

</details>

---

### [TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments](https://arxiv.org/abs/2610.17999)

**Authors:** Qingyu Lan, Zhihao Tian, Zifan Wang, Junwei Liang

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.17999) | [PDF](https://arxiv.org/pdf/2610.17999)

<details>
<summary>Abstract</summary>

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to the target robot.TRACE first injects kinematic priors into input and output projection layers and aligns nominal joint dynamics to reduce embodiment mismatch and support stable fine-tuning. It then combines encoder distillation with low-rank...

</details>

<details>
<summary>Share</summary>

```
TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch.

arXiv: https://arxiv.org/abs/2610.17999

#VLA #robotics
```

</details>

---

### [YOUDrive: Driving Style as a Composable Direction for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.14802)

**Authors:** Guantian Zheng, Lidong Yu, Tianyu Gao, Jiaxing Chen, Jiashu Li et al. (6 authors)

**Published:** 2026-10-10 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14802) | [PDF](https://arxiv.org/pdf/2610.14802)

<details>
<summary>Abstract</summary>

End-to-end driving policies can achieve strong task performance while offering limited control over their driving style. Driving style describes how a vehicle accelerates, brakes, and maintains distance. Policies trained without explicit preference conditioning lack a direct mechanism for adjusting these behaviors at inference. We propose YOUDrive, a vision--language--action planner for continuous and composable driving-style control. Each teacher's behavior is distilled into a task vector, a learned parameter update that induces a style direction in the planner's representation. These directi...

</details>

<details>
<summary>Share</summary>

```
YOUDrive: Driving Style as a Composable Direction for End-to-End Autonomous Driving

End-to-end driving policies can achieve strong task performance while offering limited control over their driving style.

arXiv: https://arxiv.org/abs/2610.14802

#VLA #robotics
```

</details>

---

### [Successful but Unsafe: An Analytical Benchmark for Revealing Collisions in Vision-and-Language Navigation](https://arxiv.org/abs/2610.14682)

**Authors:** Hieu D. Pham, Quoc-An Luong, Dung D. Le

**Published:** 2026-10-10 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14682) | [PDF](https://arxiv.org/pdf/2610.14682)

<details>
<summary>Abstract</summary>

Vision-and-language navigation (VLN) agents are typically evaluated by whether they reach a target and how efficiently they follow an instructed route, yet these metrics provide little information about collision behavior. Moreover, continuous VLN evaluation commonly uses a sliding regime, where an agent can slide along obstacles after a collision, potentially masking the effect of unsafe actions on navigation performance. We introduce VLN-Safe, a benchmark for analyzing collision safety under two complementary evaluation regimes: sliding, reflecting common VLN evaluation practice, and blockin...

</details>

<details>
<summary>Share</summary>

```
Successful but Unsafe: An Analytical Benchmark for Revealing Collisions in Vision-and-Language Navigation

Vision-and-language navigation (VLN) agents are typically evaluated by whether they reach a target and how efficiently they follow an instructed route, yet these metrics provide little information about collision beha...

arXiv: https://arxiv.org/abs/2610.14682

#VLA #robotics
```

</details>

---
