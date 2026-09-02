# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-09-02 19:13 UTC

**Papers shown:** 36 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks](https://arxiv.org/abs/2608.30536)

**Authors:** Chunyun Ma, Lun Luo, Xingjian Luo, Xiexing Feng, Hang Zhang et al. (10 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.30536) | [PDF](https://arxiv.org/pdf/2608.30536) | [Code](https://github.com/nubot-nudt/Behavior-Skill)

<details>
<summary>Abstract</summary>

Reliable execution of long-horizon mobile manipulation tasks remains challenging because overall task success depends on the successful completion of multiple constituent skills. Existing benchmarks, however, still rely primarily on full-task rollouts and aggregate task-level metrics, making intermediate failures difficult to observe and analyze. We present Behavior-Skill, a benchmark that reformulates the learning and evaluation of long-horizon tasks around executable constituent skills. It contains 235,492 skill instances from 10,000 demonstrations across 50 household tasks and 34 semantic s...

</details>

<details>
<summary>Share</summary>

```
Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

Reliable execution of long-horizon mobile manipulation tasks remains challenging because overall task success depends on the successful completion of multiple constituent skills.

arXiv: https://arxiv.org/abs/2608.30536
Code: https://github.com/nubot-nudt/Behavior-Skill

#VLA #robotics
```

</details>

---

### [PHR-VLA: Planning Horizon Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2608.27609)

**Authors:** Davood Soleymanzadeh, Kaidi Zhang, Zhiyuan Zhang, Bihao Zhang, Xiao Liang et al. (7 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.27609) | [PDF](https://arxiv.org/pdf/2608.27609) | [Project Page](https://davoodsz.github.io/PHR-VLA.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) have shown strong promise for general-purpose robotic manipulation by mapping language instructions and vision observations directly to actions. However, most VLAs primarily condition action prediction on current observations and lack an explicit mechanism for reasoning over future task dynamics, which is particularly important for fine-grained, contact-rich manipulation. We present PHR-VLA, a framework that enables planning-horizon reasoning in VLAs through privileged latent representations of future dynamics. PHR-VLA introduces a lightweight auxiliary fut...

</details>

<details>
<summary>Share</summary>

```
PHR-VLA: Planning Horizon Reasoning for Vision-Language-Action Models

Vision-language-action models (VLAs) have shown strong promise for general-purpose robotic manipulation by mapping language instructions and vision observations directly to actions.

arXiv: https://arxiv.org/abs/2608.27609
Project page: https://davoodsz.github.io/PHR-VLA.github.io/

#VLA #robotics
```

</details>

---

### [Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models](https://arxiv.org/abs/2608.27550)

**Authors:** Senqiao Yang, Chengyao Wang, Yuxin Chen, Zixuan Wang, Longxiang Tang et al. (16 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.27550) | [PDF](https://arxiv.org/pdf/2608.27550) | [Project Page](https://starvla.github.io/VLAct)

<details>
<summary>Abstract</summary>

Scaling robot data is crucial for building generalist Vision-Language-Action (VLA) models, yet robot trajectories are harder to scale than web-scale image-text data because embodied collection is costly and sparsely covers the physical world. This makes representation quality a central bottleneck: under a fixed robot-data budget, continued pre-training must turn limited trajectories into transferable visual-action knowledge rather than merely fit actions. We propose VLAct, a VLA-oriented VLM backbone trained on broad, heterogeneous, multi-embodiment robot data before task-specific fine-tuning....

</details>

<details>
<summary>Share</summary>

```
Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models

Scaling robot data is crucial for building generalist Vision-Language-Action (VLA) models, yet robot trajectories are harder to scale than web-scale image-text data because embodied collection is costly and sparsely c...

arXiv: https://arxiv.org/abs/2608.27550
Project page: https://starvla.github.io/VLAct

#VLA #robotics
```

</details>

---

### [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)

**Authors:** Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, Xu-Han Chen, Yinghao Li et al. (12 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.26578) | [PDF](https://arxiv.org/pdf/2608.26578) | [Project Page](https://john-liua.github.io/TrapVLA/)

<details>
<summary>Abstract</summary>

This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failure modes. Unlike prior backdoor attacks that treat any task failure as a successful attack, Configured Failure Trapping requires the attacker to control how the robot fails (e.g., causing the robot to grasp with a specified positional offset), making it substantially more challenging and hard to detect. To support the new task, we propose an effective data engine for synthesizing h...

</details>

<details>
<summary>Share</summary>

```
TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes

This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failur...

arXiv: https://arxiv.org/abs/2608.26578
Project page: https://john-liua.github.io/TrapVLA/

#VLA #robotics
```

</details>

---

### [MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization](https://arxiv.org/abs/2608.25864)

**Authors:** Zaibin Zhang, Junlan Xiao, Zhongbo Zhang, Yifan Wang, Li Kang et al. (14 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.25864) | [PDF](https://arxiv.org/pdf/2608.25864) | [Code](https://github.com/zhangzaibin/future-robots)

<details>
<summary>Abstract</summary>

Multi-arm collaboration is becoming a core capability in embodied manipulation. Recent vision-language-action (VLA) models integrate perception, language, and control, but most represent language as a single global instruction and do not provide an explicit mechanism for assigning and composing arm-specific behaviors. This design limits transfer to collaboration patterns that differ from those observed during training. We present MA-VLA, a unified framework for multi-arm collaboration via atomic action assignment. MA-VLA decomposes cooperative behavior into mid-level atomic prompts and allocat...

</details>

<details>
<summary>Share</summary>

```
MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization

Multi-arm collaboration is becoming a core capability in embodied manipulation.

arXiv: https://arxiv.org/abs/2608.25864
Code: https://github.com/zhangzaibin/future-robots

#VLA #robotics
```

</details>

---

### [Temporal Forcing: 4D Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2608.30643)

**Authors:** Xingyu Ding, Yuzhong Zhao, Chunhai Zhao, Yinghuan Shi, Chaoyang Zhao et al. (6 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2608.30643) | [PDF](https://arxiv.org/pdf/2608.30643)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) methods improve manipulation performance by aligning their representations with 3D scene geometry. However, these methods often struggle with long-horizon manipulation and observation aliasing between visually similar states due to a lack of temporal information: the 3D scene geometry captures only the current state, rather than how it has evolved over time. To resolve this, we present Temporal Forcing, a 4D representation alignment method for VLA models. Specifically, we first introduce a history pathway that enables a vanilla VLA model to summarize observa...

</details>

<details>
<summary>Share</summary>

```
Temporal Forcing: 4D Representation Alignment for Vision-Language-Action Models

Recent vision-language-action (VLA) methods improve manipulation performance by aligning their representations with 3D scene geometry.

arXiv: https://arxiv.org/abs/2608.30643

#VLA #robotics
```

</details>

---

### [Training-Free Action Correction for VLA Model Failures via Language Feedback](https://arxiv.org/abs/2608.29967)

**Authors:** Owen Kwon, Pablo Ortega-Kral, Arthur Bucker, Jean Oh

**Published:** 2026-08-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.29967) | [PDF](https://arxiv.org/pdf/2608.29967) | [Project Page](https://correctvla.github.io)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate strong semantic understanding yet exhibit systematic failures during deployment. The conditions under which these failures occur, and whether they can be corrected without retraining, remain poorly understood. In this paper, we take steps toward addressing this gap. We present CorrectVLA, a framework that translates task-level natural language corrections into additive action magnitude adjustments without modifying policy weights. A human provides a single task-level correction, applied uniformly across all rollouts without per-episode interventi...

</details>

<details>
<summary>Share</summary>

```
Training-Free Action Correction for VLA Model Failures via Language Feedback

Vision-Language-Action (VLA) models demonstrate strong semantic understanding yet exhibit systematic failures during deployment.

arXiv: https://arxiv.org/abs/2608.29967
Project page: https://correctvla.github.io

#VLA #robotics
```

</details>

---

### [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281)

**Authors:** Wei Wang, Wenqiao Zhang, Yutong Lin, Yuqian Yuan, Tianwei Lin et al. (17 authors)

**Published:** 2026-09-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.01281) | [PDF](https://arxiv.org/pdf/2609.01281)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, but long-horizon tasks require more than action prediction. An agent must coordinate perception, planning, execution, progress verification, and recovery as the physical state evolves. An action prediction or a model-generated skill decision does not, by itself, guarantee that the proposed operation is valid in the current state or that its outcome will be verified. We propose EmbodiedSkills, a unified framework that treats each skill decision as an execution proposal: the runtime c...

</details>

<details>
<summary>Share</summary>

```
EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents

Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, but long-horizon tasks require more than action prediction.

arXiv: https://arxiv.org/abs/2609.01281

#VLA #robotics
```

</details>

---

### [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://arxiv.org/abs/2609.01215)

**Authors:** Riyaaz Shaik, Chandru Venkataraman

**Published:** 2026-09-01 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2609.01215) | [PDF](https://arxiv.org/pdf/2609.01215)

<details>
<summary>Abstract</summary>

Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's dynamics. We introduce REFACTOR-VLA, a wake/sleep system for learning reusable skills. Its sleep phas...

</details>

<details>
<summary>Share</summary>

```
REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs

Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade o...

arXiv: https://arxiv.org/abs/2609.01215

#VLA #robotics
```

</details>

---

### [Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs](https://arxiv.org/abs/2609.00908)

**Authors:** Runze Xu, Xiaolong Shan, Shuang Dai, Yu Wang, Jincheng Yu

**Published:** 2026-09-01 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.00908) | [PDF](https://arxiv.org/pdf/2609.00908)

<details>
<summary>Abstract</summary>

Action chunking is a standard execution strategy in modern Vision-Language-Action (VLA) frameworks, but fixed execution horizons impose a trade-off between efficiency and accuracy. Short chunks require frequent inference and may cause oscillatory behavior, whereas long chunks can become misaligned with newly observed states. We address this limitation with an adaptive action chunking approach based on internal cross-attention dynamics in the action expert. We observe that, as the prediction horizon extends, action-to-observation cross-attention becomes increasingly dispersed and its entropy ri...

</details>

<details>
<summary>Share</summary>

```
Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs

Action chunking is a standard execution strategy in modern Vision-Language-Action (VLA) frameworks, but fixed execution horizons impose a trade-off between efficiency and accuracy.

arXiv: https://arxiv.org/abs/2609.00908

#VLA #robotics
```

</details>

---

### [Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving](https://arxiv.org/abs/2608.30144)

**Authors:** Tongfei Guo, Lili Su

**Published:** 2026-08-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2608.30144) | [PDF](https://arxiv.org/pdf/2608.30144)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are reshaping autonomous driving (AD) by unifying perception, reasoning, and control through language, enabling semantic grounding, interpretable decisions, and better long-tail generalization. But language is expensive onboard: latency and memory budgets are tight, and autoregressive decoding is inherently sequential. This work reframes the central question as when and where language should act at inference, since inference cost recurs at every deployed frame while training cost is paid once. We introduce the Language Residue taxonomy to organize methods by...

</details>

<details>
<summary>Share</summary>

```
Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving

Vision-Language-Action (VLA) models are reshaping autonomous driving (AD) by unifying perception, reasoning, and control through language, enabling semantic grounding, interpretable decisions, and better long-tail gen...

arXiv: https://arxiv.org/abs/2608.30144

#VLA #robotics
```

</details>

---

### [AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models](https://arxiv.org/abs/2608.29208)

**Authors:** Sunghwan Han, Youngtae Han, Youngmin Yi

**Published:** 2026-08-29 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.29208) | [PDF](https://arxiv.org/pdf/2608.29208)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to privacy and proprietary concerns. Moreover, although flow-matching-based VLAs have emerged as efficient...

</details>

<details>
<summary>Share</summary>

```
AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models

Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning.

arXiv: https://arxiv.org/abs/2608.29208

#VLA #robotics
```

</details>

---

### [DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA](https://arxiv.org/abs/2608.28108)

**Authors:** Kango Yanagida, Tatsuya Aoki, Yuichiro Yoshikawa, Takato Horii

**Published:** 2026-08-28 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.28108) | [PDF](https://arxiv.org/pdf/2608.28108)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) allow users to specify manipulation tasks in natural language, but distinguishing a target or placement goal among objects of the same category or similar appearance requires detailed expressions that VLAs may not use reliably. We propose DeicticVLA, which canonicalizes Language Instruction (LI), Vision-Language Instruction (VLI), and Visual Instruction (VI) into a text prompt and deictic masks through text-prompt completion and deictic gesture grounding, enabling a single pretrained VLA to handle all three instruction modes. With a shared backbone, demonst...

</details>

<details>
<summary>Share</summary>

```
DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA

Vision-Language-Action models (VLAs) allow users to specify manipulation tasks in natural language, but distinguishing a target or placement goal among objects of the same category or similar appearance requires detai...

arXiv: https://arxiv.org/abs/2608.28108

#VLA #robotics
```

</details>

---

### [One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058)

**Authors:** Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li et al. (24 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.26058) | [PDF](https://arxiv.org/pdf/2608.26058) | [Project Page](https://public-bots.github.io/UCAG-P)

<details>
<summary>Abstract</summary>

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action formulation that structurally aligns heterogeneous embodied datasets into a shared geometric action...

</details>

<details>
<summary>Share</summary>

```
One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spa...

arXiv: https://arxiv.org/abs/2608.26058
Project page: https://public-bots.github.io/UCAG-P

#VLA #robotics
```

</details>

---

### [A Taxonomy of Construction Task Activities for Robot Workers](https://arxiv.org/abs/2608.25395)

**Authors:** Sadman Sakib, Zhangyi None Peng, Yujie Pang, Yu Otsuki, Mohammad Abdullah Al Faruque

**Published:** 2026-08-26 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2608.25395) | [PDF](https://arxiv.org/pdf/2608.25395) | [Code](https://github.com/AICPS/TARCAT-Taxonomy)

<details>
<summary>Abstract</summary>

Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems. Construction deployment, however, requires a precise inventory of worker activities and the capabilities needed to execute them. We present TARCAT, an occupation-grounded taxonomy derived from 91 O*NET tasks across seven high-employment construction occupations and 30 instructional videos of physical work. TARCAT defines 41 action primitives in 12 groups and three classes and provides a mechanism for composing parameterized primitive sequences into reusable skills....

</details>

<details>
<summary>Share</summary>

```
A Taxonomy of Construction Task Activities for Robot Workers

Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems.

arXiv: https://arxiv.org/abs/2608.25395
Code: https://github.com/AICPS/TARCAT-Taxonomy

#VLA #robotics
```

</details>

---

### [Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving](https://arxiv.org/abs/2608.30122)

**Authors:** Tian Zhang, Zhuo Huang, Hongrui Ye, Yu Wu, Zengmao Wang et al. (6 authors)

**Published:** 2026-08-31 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2608.30122) | [PDF](https://arxiv.org/pdf/2608.30122)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) driving methods increasingly combine multi-trajectory imitation learning with group-relative policy optimization (GRPO), making trajectory selection critical to final performance. However, some high-scoring trajectories that improve imitation can degrade subsequent GRPO by inducing advantage estimates misaligned with the current policy's feasible behavior distribution, driving updates away from safe and compliant behaviors. To address this, we propose a novel framework that aligns multi-trajectory supervision with policy optimization. To address the policy gradient...

</details>

<details>
<summary>Share</summary>

```
Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving

Vision-language-action (VLA) driving methods increasingly combine multi-trajectory imitation learning with group-relative policy optimization (GRPO), making trajectory selection critical to final performance.

arXiv: https://arxiv.org/abs/2608.30122

#VLA #robotics
```

</details>

---

### [StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.26067)

**Authors:** Zhe Liu, Jinghua Hou, Yuxiang Lu, Zhenya Yang, Xianzhe Fan et al. (10 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.26067) | [PDF](https://arxiv.org/pdf/2608.26067)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored temporal modeling. It treats each (visual observation, language instruction) pair as an atomic temp...

</details>

<details>
<summary>Share</summary>

```
StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observa...

arXiv: https://arxiv.org/abs/2608.26067

#VLA #robotics
```

</details>

---

### [V-Link: Recovering Lost Visual Representations in Action DiT for Vision-Language-Action Models](https://arxiv.org/abs/2608.25308)

**Authors:** Yehao Lu, Jiarui Yang, Yuning Su, Yufeng Xie, Yu Zhong et al. (13 authors)

**Published:** 2026-08-26 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.25308) | [PDF](https://arxiv.org/pdf/2608.25308)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a scalable path toward generalist robotic manipulation by integrating visual perception, language understanding, and continuous action control. However, we reveal a critical limitation of VLA architectures: the action expert has limited access to the 3D geometric and 2D semantic information available in VLM features. This accessibility gap weakens perceptual grounding and limits performance on fine-grained robotic manipulation. To address this issue, we propose V-Link, which explicitly recovers visual representations during the vision-language (VL) t...

</details>

<details>
<summary>Share</summary>

```
V-Link: Recovering Lost Visual Representations in Action DiT for Vision-Language-Action Models

Vision-language-action (VLA) models provide a scalable path toward generalist robotic manipulation by integrating visual perception, language understanding, and continuous action control.

arXiv: https://arxiv.org/abs/2608.25308

#VLA #robotics
```

</details>

---

### [Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching](https://arxiv.org/abs/2609.01404)

**Authors:** Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon et al. (14 authors)

**Published:** 2026-09-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.01404) | [PDF](https://arxiv.org/pdf/2609.01404)

<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) are strong perceivers of images and video. We ask how far that reach extends into acting: dropping an MLLM directly into a drone's control loop, with its entire action space declared solely in the prompt. Recent systems approach this setting but increasingly narrow the model's decision-making. We widen it back. We introduce DroneCATS-Agent, an architecture where the MLLM is a swappable component, and DroneCATS, a benchmark treating the model as the independent variable. Beyond merely flying toward a pixel, our agent entrusts the model to yaw and search,...

</details>

<details>
<summary>Share</summary>

```
Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching

Multimodal Large Language Models (MLLMs) are strong perceivers of images and video.

arXiv: https://arxiv.org/abs/2609.01404

#VLA #robotics
```

</details>

---

### [CometVLA: Co-Training on an Embodied Data Pyramid towards Physical Understanding](https://arxiv.org/abs/2608.30289)

**Authors:** Hanwen Wan, Dafeng Chi, Linbo Zhai, Tianao Shen, Yuzheng Zhuang et al. (9 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2608.30289) | [PDF](https://arxiv.org/pdf/2608.30289)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models remain brittle in manipulation tasks that require physical commonsense. Current physical VQA data is typically disembodied and misaligned with robot action domains. Egocentric videos are used only as auxiliary pre-training. It remains unclear whether improved VLM physical understanding actually benefits downstream action generation. Therefore, we present CometVLA to close this gap. We construct CometData and CometBench, an embodied physical VQA corpus and benchmark strictly aligned with the robot's action data and embodiment. We introduce Global Action Prior...

</details>

<details>
<summary>Share</summary>

```
CometVLA: Co-Training on an Embodied Data Pyramid towards Physical Understanding

Vision-language-action (VLA) models remain brittle in manipulation tasks that require physical commonsense.

arXiv: https://arxiv.org/abs/2608.30289

#VLA #robotics
```

</details>

---

### [DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting](https://arxiv.org/abs/2608.29749)

**Authors:** Yuxuan Gao, Shiqi Zhang, Yedong Shen, Yifan Duan, Wenhao Yu et al. (9 authors)

**Published:** 2026-08-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.29749) | [PDF](https://arxiv.org/pdf/2608.29749)

<details>
<summary>Abstract</summary>

Conventional flow-based vision-language-action (VLA) models support expressive continuous action generation but rely on multi-step refinement to produce each action chunk, increasing latency in online robot control. To address this issue, we introduce DriftingVLA, a native one-step VLA that generates a complete action chunk with a single action-expert forward pass. Rather than learning a flow field that requires iterative integration at inference, DriftingVLA uses a distribution-drifting objective to learn a direct noise-to-action-chunk mapping for one-step deployment. Since robot action dimen...

</details>

<details>
<summary>Share</summary>

```
DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting

Conventional flow-based vision-language-action (VLA) models support expressive continuous action generation but rely on multi-step refinement to produce each action chunk, increasing latency in online robot control.

arXiv: https://arxiv.org/abs/2608.29749

#VLA #robotics
```

</details>

---

### [AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies](https://arxiv.org/abs/2608.29537)

**Authors:** Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li

**Published:** 2026-08-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.29537) | [PDF](https://arxiv.org/pdf/2608.29537)

<details>
<summary>Abstract</summary>

Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen VLA policies that represents a task as a subgoal sequence with a progress pointer and advances this m...

</details>

<details>
<summary>Share</summary>

```
AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies

Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or termi...

arXiv: https://arxiv.org/abs/2608.29537

#VLA #robotics
```

</details>

---

### [SMILE: Smooth Motion for Improved Long-Horizon VLA Execution](https://arxiv.org/abs/2608.29432)

**Authors:** Jongwoo Park, E-Ro Nguyen, Kanchana Ranasinghe, Cristina Mata, Xiang Li et al. (6 authors)

**Published:** 2026-08-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.29432) | [PDF](https://arxiv.org/pdf/2608.29432)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models reduce inference cost by executing multiple actions per call, but longer horizons often degrade accuracy because raw chunks contain jitter and outliers. We introduce SMILE, an architecture-preserving interface that predicts B-spline coefficients and decodes them into smooth action sequences. SMILE changes only the action representation, enabling longer fixed horizons while retaining each baseline's backbone and model scale. We apply SMILE to SmolVLA, Evo1, VPP, and DAWN, improving accuracy and amortized inference efficiency across LIBERO, CALVIN, and real-wo...

</details>

<details>
<summary>Share</summary>

```
SMILE: Smooth Motion for Improved Long-Horizon VLA Execution

Vision-Language-Action (VLA) models reduce inference cost by executing multiple actions per call, but longer horizons often degrade accuracy because raw chunks contain jitter and outliers.

arXiv: https://arxiv.org/abs/2608.29432

#VLA #robotics
```

</details>

---

### [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384)

**Authors:** Zekai Li, Jiaming Tang, Zhijian Liu

**Published:** 2026-08-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.27384) | [PDF](https://arxiv.org/pdf/2608.27384)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly promising for robotic manipulation, yet their real-world deployment remains bottlenecked by high inference latency and unstable asynchronous execution. This challenge is particularly pronounced in flow-matching-based VLA models, where action decoding requires multiple iterative steps conditioned on the VLM context. While efficient inference methods improve control frequency and asynchronous methods reduce execution idle time, existing approaches often fail to jointly achieve low-latency inference and accurate, temporally consistent asynchron...

</details>

<details>
<summary>Share</summary>

```
FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference

Vision-Language-Action (VLA) models are increasingly promising for robotic manipulation, yet their real-world deployment remains bottlenecked by high inference latency and unstable asynchronous execution.

arXiv: https://arxiv.org/abs/2608.27384

#VLA #robotics
```

</details>

---

### [TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2608.26821)

**Authors:** Jiarui Yang, Yehao Lu, Yuning Su, Yu Zhong, Yufeng Xie et al. (12 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.26821) | [PDF](https://arxiv.org/pdf/2608.26821)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models leverage pretrained vision-language representations for robot control, yet simply adding historical frames does not reliably capture recent physical change. This is especially problematic in multi-stage manipulation, where visually similar states may require different actions depending on prior execution. To address this challenge, we present TemporalFlow-VLA, which learns compact execution history through physically grounded temporal supervision. Using recorded robot states, robot geometry, and calibrated cameras, we construct robot-surface temporal flow as...

</details>

<details>
<summary>Share</summary>

```
TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation

Vision-language-action (VLA) models leverage pretrained vision-language representations for robot control, yet simply adding historical frames does not reliably capture recent physical change.

arXiv: https://arxiv.org/abs/2608.26821

#VLA #robotics
```

</details>

---

### [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645)

**Authors:** Ganlong Zhao, Zijia Tang, Xingping Chen, Zhanghui Kuang, Ye Tian et al. (6 authors)

**Published:** 2026-08-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.26645) | [PDF](https://arxiv.org/pdf/2608.26645)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models~(VLAs) have demonstrated significant promise in generalizing to complex, long-horizon robotic manipulation tasks. However, their performance remains brittle, as they are typically trained on trajectory-monotonic, failure-free demonstrations. This reliance on ``perfect" data leaves them unable to recover from common execution errors, such as a missed grasp, a dropped object, or an unexpected collision. In this paper, we propose FLARE, a novel framework that endows VLAs with robust error recovery capabilities through a ``Retry" and ``Reset" paradigm. First, we intro...

</details>

<details>
<summary>Share</summary>

```
FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

Vision-Language-Action Models~(VLAs) have demonstrated significant promise in generalizing to complex, long-horizon robotic manipulation tasks.

arXiv: https://arxiv.org/abs/2608.26645

#VLA #robotics
```

</details>

---

### [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](https://arxiv.org/abs/2608.25585)

**Authors:** Sanghwan Jang, Minjin Jeon, Minsoo Kim, Seongjin Choi, Dongha Kim et al. (6 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.25585) | [PDF](https://arxiv.org/pdf/2608.25585)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a versatile foundation for general robotic manipulation, yet they exhibit significant brittleness when confronted with novel task distributions. While In-Context Imitation Learning (ICIL) offers a training-free alternative, existing frameworks suffer from an adaptation bottleneck that hinders the effective translation of expert context to executable actions. This failure originates from superficial retrieval mechanisms and an inherent behavioral inertia that anchors the policy to its pre-trained priors. To address these limitations, we present RA-VLA...

</details>

<details>
<summary>Share</summary>

```
RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation

Vision-Language-Action (VLA) models provide a versatile foundation for general robotic manipulation, yet they exhibit significant brittleness when confronted with novel task distributions.

arXiv: https://arxiv.org/abs/2608.25585

#VLA #robotics
```

</details>

---

### [Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation](https://arxiv.org/abs/2608.30880)

**Authors:** Fu Chen, Xin Ding, Bingjia Huang, Xiangyu Li, Mingju Wang et al. (11 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2608.30880) | [PDF](https://arxiv.org/pdf/2608.30880)

<details>
<summary>Abstract</summary>

Generalizable embodied manipulation remains difficult to achieve through pretraining alone, due to unseen physical conditions in the real world. We argue that robots need to learn from their own physical interactions on the fly during real-world deployment and use this knowledge to inform subsequent actions. We present Zeva, the first framework that enables in-context learning from a robot's own physical interaction experience while keeping the policy model frozen. Zeva employs a Causal Interaction Extractor to encode an executed action and its induced state change into a causal interaction si...

</details>

<details>
<summary>Share</summary>

```
Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation

Generalizable embodied manipulation remains difficult to achieve through pretraining alone, due to unseen physical conditions in the real world.

arXiv: https://arxiv.org/abs/2608.30880

#VLA #robotics
```

</details>

---

### [PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies](https://arxiv.org/abs/2608.30378)

**Authors:** Botong Zhao, Fang Yu, Tim, Senhua Zhu, Xinyuan Chen et al. (6 authors)

**Published:** 2026-08-31 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2608.30378) | [PDF](https://arxiv.org/pdf/2608.30378)

<details>
<summary>Abstract</summary>

Direct vision-language-action policies generate continuous robot actions efficiently, but standard behavior cloning leaves two complementary gaps: their representations are not explicitly required to describe how the scene evolves over multiple time scales, and deployment trajectories of unequal quality are often reused without separating useful dynamics from undesirable behavior. We introduce \method, a direct world-action policy that combines outcome-agnostic predictive learning with outcome-aware policy improvement. \method first retains a local fixed-offset JEPA objective and adds trajecto...

</details>

<details>
<summary>Share</summary>

```
PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies

Direct vision-language-action policies generate continuous robot actions efficiently, but standard behavior cloning leaves two complementary gaps: their representations are not explicitly required to describe how the...

arXiv: https://arxiv.org/abs/2608.30378

#VLA #robotics
```

</details>

---

### [DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation](https://arxiv.org/abs/2608.29078)

**Authors:** Makoto Sato, Tatsuya Matsushima, Yutaka Matsuo, Yusuke Iwasawa

**Published:** 2026-08-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.29078) | [PDF](https://arxiv.org/pdf/2608.29078)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have made strong progress in language-conditioned robot manipulation, but improving their performance in a new workspace still often requires action-labeled data from that environment. Collecting such data by human teleoperation is costly, especially when each workspace, object arrangement, or task may require new demonstrations. We present DREAM, a framework that generates fine-tuning data for a pretrained VLA from a captured workspace and a language instruction, without requiring a task-specific human demonstration. DREAM reconstructs the workspace, automa...

</details>

<details>
<summary>Share</summary>

```
DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation

Vision-language-action (VLA) models have made strong progress in language-conditioned robot manipulation, but improving their performance in a new workspace still often requires action-labeled data from that environment.

arXiv: https://arxiv.org/abs/2608.29078

#VLA #robotics
```

</details>

---

### [GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.27079)

**Authors:** Yibo Qiu, Haoliang Ye, Shu'ang Sun, Zan Huang, Ronald X Xu et al. (6 authors)

**Published:** 2026-08-27 (updated 2026-08-28) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.27079) | [PDF](https://arxiv.org/pdf/2608.27079)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) policies provide strong priors for robot manipulation, yet adapting them online to fine-grained biomedical tasks remains challenging. Task success often hinges on subtle, view-dependent visual cues, while task-level rewards provide little guidance about which regions matter, making it difficult to learn task-relevant visual grounding from limited real-robot interaction. Online adaptation is further constrained by the computational cost of VLA inference and replay-based updates. We introduce GRAFT (Grounded Reinforcement Adaptation for Fast Task Learning)...

</details>

<details>
<summary>Share</summary>

```
GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation

Pretrained vision-language-action (VLA) policies provide strong priors for robot manipulation, yet adapting them online to fine-grained biomedical tasks remains challenging.

arXiv: https://arxiv.org/abs/2608.27079

#VLA #robotics
```

</details>

---

### [PredVLA: Predictive Sensorimotor Modeling for Sub-Million-Parameter Robot Manipulation](https://arxiv.org/abs/2608.26673)

**Authors:** Hiroki Sawada, Shunichi Kasahara

**Published:** 2026-08-27 (updated 2026-08-30) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.26673) | [PDF](https://arxiv.org/pdf/2608.26673)

<details>
<summary>Abstract</summary>

Large pretrained vision-language-action models achieve strong robot-manipulation performance, while compact alternatives have largely pursued efficiency by compressing the prevailing observation-to-action paradigm. We investigate whether predictive sensorimotor modeling can make more effective use of a limited parameter budget than direct observation-to-action mapping. We present PredVLA, a language-conditioned predictive-coding policy with only 0.68 million trainable network parameters and no robot-data pretraining. Its hierarchical recurrent dynamics predict visual features and proprioceptio...

</details>

<details>
<summary>Share</summary>

```
PredVLA: Predictive Sensorimotor Modeling for Sub-Million-Parameter Robot Manipulation

Large pretrained vision-language-action models achieve strong robot-manipulation performance, while compact alternatives have largely pursued efficiency by compressing the prevailing observation-to-action paradigm.

arXiv: https://arxiv.org/abs/2608.26673

#VLA #robotics
```

</details>

---

### [LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation](https://arxiv.org/abs/2608.25757)

**Authors:** Jin Lou, Zhiyuan Jing, Andong Chen, Xupeng Wang, Yuan Xu et al. (23 authors)

**Published:** 2026-08-26 (updated 2026-08-27) | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.25757) | [PDF](https://arxiv.org/pdf/2608.25757)

<details>
<summary>Abstract</summary>

Generalist vision--language--action (VLA) policies learn long-horizon behavior mainly through short-horizon action prediction and reveal little beyond sampled commands. This creates two coupled bottlenecks: a single action target must implicitly absorb task progress, intermediate intent, and local reliability, while these control states remain hidden during execution. Inspired by functional principles of biological sensorimotor control, we introduce LM-X , which organizes prediction across task, event, and motor scales without claiming anatomical correspondence. Three explicitly supervised sig...

</details>

<details>
<summary>Share</summary>

```
LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation

Generalist vision--language--action (VLA) policies learn long-horizon behavior mainly through short-horizon action prediction and reveal little beyond sampled commands.

arXiv: https://arxiv.org/abs/2608.25757

#VLA #robotics
```

</details>

---

### [GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659)

**Authors:** Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He et al. (11 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.25659) | [PDF](https://arxiv.org/pdf/2608.25659)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have advanced language-conditioned robotic manipulation, yet action-imitation objectives provide only weak supervision for metric 3D structure and short-horizon physical evolution. Geometry-enhanced policies mainly improve current-scene grounding, whereas predictive policies often model future dynamics in RGB or latent spaces and may incur substantial deployment cost. GaussianDream demonstrates that training-time current Gaussian reconstruction and future Gaussian prediction provide effective 3D supervision, but its dense VGGT/TGE-based prefix jointly carr...

</details>

<details>
<summary>Share</summary>

```
GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation

Vision-Language-Action (VLA) policies have advanced language-conditioned robotic manipulation, yet action-imitation objectives provide only weak supervision for metric 3D structure and short-horizon physical evolution.

arXiv: https://arxiv.org/abs/2608.25659

#VLA #robotics
```

</details>

---

### [TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback](https://arxiv.org/abs/2608.25798)

**Authors:** Jianbo Zhou, Boyuan Zhao, Yuzheng Zhang, Yiyang Chen, Wenxin Chen et al. (11 authors)

**Published:** 2026-08-26 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2608.25798) | [PDF](https://arxiv.org/pdf/2608.25798)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon. However, chunk-based vision-language-action models predict complete action chunks from observations collected before execution, leaving tactile conditioning stale during execution. Existing tactile-reactive approaches typically rely on separate high-frequency controllers, which increase both architectural and training complexity. In this paper, we introduce TacForcing, a streaming action-generation framework that effectively incorporates execution-time tactile feedback. Instead...

</details>

<details>
<summary>Share</summary>

```
TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback

Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon.

arXiv: https://arxiv.org/abs/2608.25798

#VLA #robotics
```

</details>

---

### [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005)

**Authors:** Haohua Que, Handong Yao

**Published:** 2026-08-29 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2608.29005) | [PDF](https://arxiv.org/pdf/2608.29005)

<details>
<summary>Abstract</summary>

Camera-only end-to-end (E2E) driving models are nearing deployment, where the camera stream is degraded by blur, noise, low light, weather, frame loss, and memory faults. How much a policy tolerates before its driving breaks is unclear. Corruption-robustness benchmarks target detection or bird's-eye-view perception, not the planning output that drives the car. We present DriveDegrade, a benchmark for image-degradation tolerance in camera-only E2E driving. Sixteen corruption families at five severities are injected on the fly inside the image loader, one operator reaching fifteen policies, and...

</details>

<details>
<summary>Share</summary>

```
A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving

Camera-only end-to-end (E2E) driving models are nearing deployment, where the camera stream is degraded by blur, noise, low light, weather, frame loss, and memory faults.

arXiv: https://arxiv.org/abs/2608.29005

#VLA #robotics
```

</details>

---
