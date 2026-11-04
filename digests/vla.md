# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-04 01:45 UTC

**Papers shown:** 48 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [VLALagBench: Understanding When and Why VLA Inference Latency Matters](https://arxiv.org/abs/2611.03103)

**Authors:** Qi Wen, Borui Xu, Hussein Amro, Hongshi Tan, Hanmin Lin et al. (14 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03103) | [PDF](https://arxiv.org/pdf/2611.03103) | [Code](https://github.com/codestrongestx/VLALagBench)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models offer a promising path toward general-purpose robot manipulation. While inference latency can affect task success in a constantly evolving physical world, the relationship between latency and task success rate remains poorly understood. In this paper, we introduce VLALagBench, a comprehensive benchmark for studying VLA inference latency sensitivity across task types, object speeds, execution modes (synchronous and asynchronous), and VLA policies. Using VLALagBench, we find that even a modest inference latency of 100 ms can nearly halve task success on moving...

</details>

<details>
<summary>Share</summary>

```
VLALagBench: Understanding When and Why VLA Inference Latency Matters

Vision-language-action (VLA) models offer a promising path toward general-purpose robot manipulation.

arXiv: https://arxiv.org/abs/2611.03103
Code: https://github.com/codestrongestx/VLALagBench

#VLA #robotics
```

</details>

---

### [Scene-Adaptive Readout and Decoding in Diffusion Driving VLAs](https://arxiv.org/abs/2611.02076)

**Authors:** Seungjun Yu, Jiho Choi, Inha Kang, Hojun Choi, Seungwook Kim et al. (6 authors)

**Published:** 2026-11-01 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.02076) | [PDF](https://arxiv.org/pdf/2611.02076) | [Code](https://github.com/sjyu001/SARD)

<details>
<summary>Abstract</summary>

Diffusion driving vision-language-action models repeatedly execute the backbone at every denoising stage, incurring substantial inference cost, while it remains unclear whether all scenes require the same decoding computation. To distinguish when a trajectory becomes readable from how much further refinement it requires, we analyze trajectory readout across network depth and decoding progress. We identify a depth-decoding dissociation in which late-layer representations already support useful trajectory readout after the first forward sweep, whereas early-layer representations benefit more fro...

</details>

<details>
<summary>Share</summary>

```
Scene-Adaptive Readout and Decoding in Diffusion Driving VLAs

Diffusion driving vision-language-action models repeatedly execute the backbone at every denoising stage, incurring substantial inference cost, while it remains unclear whether all scenes require the same decoding com...

arXiv: https://arxiv.org/abs/2611.02076
Code: https://github.com/sjyu001/SARD

#VLA #robotics
```

</details>

---

### [From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2610.39543)

**Authors:** Yixue Zhang, Wenke Xia, Kun Wu, Wenbo Yu, Pei Ren et al. (9 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39543) | [PDF](https://arxiv.org/pdf/2610.39543) | [Project Page](https://onlyxingxingzyx.github.io/CoRAct/)

<details>
<summary>Abstract</summary>

Reasoning informs decision-making by connecting intended actions with their expected consequences. Recent vision-language-action (VLA) models incorporate embodied chains of thought (ECoTs) to guide action generation. However, such guidance remains implicit, as actions are conditioned on ECoTs rather than explicitly optimized to align with them. We introduce CoRAct, a consequence-grounded reasoning-to-action alignment framework that explicitly aligns reasoning and action through reward-guided optimization in action noise space. CoRAct formulates two physically grounded ECoT components as verifi...

</details>

<details>
<summary>Share</summary>

```
From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models

Reasoning informs decision-making by connecting intended actions with their expected consequences.

arXiv: https://arxiv.org/abs/2610.39543
Project page: https://onlyxingxingzyx.github.io/CoRAct/

#VLA #robotics
```

</details>

---

### [Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2610.38661)

**Authors:** Jiuyi Xu, Xiao Hu, Meida Chen, Song Wang, Yang Ye et al. (6 authors)

**Published:** 2026-10-28 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.38661) | [PDF](https://arxiv.org/pdf/2610.38661) | [Code](https://github.com/jiuyixu25/QbD-VLA)

<details>
<summary>Abstract</summary>

Post-training quantization (PTQ) reduces the memory footprint of vision-language-action (VLA) models, but lowering bit widths while maintaining task performance remains challenging. Existing work has used sensitivity estimates from calibration data to assign bit widths to different model components. However, using task success directly to guide mixed-precision allocation is underexplored because closed-loop evaluations are costly and the effect of quantizing one component depends on the precision of other components. To this end, we propose \textbf{QbD-VLA}, a task-guided mixed-precision quant...

</details>

<details>
<summary>Share</summary>

```
Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models

Post-training quantization (PTQ) reduces the memory footprint of vision-language-action (VLA) models, but lowering bit widths while maintaining task performance remains challenging.

arXiv: https://arxiv.org/abs/2610.38661
Code: https://github.com/jiuyixu25/QbD-VLA

#VLA #robotics
```

</details>

---

### [FineCraft: Enhancing VLA Models for Fine-Grained Manipulation](https://arxiv.org/abs/2611.03163)

**Authors:** Shuaike Zhang, Ziheng Quan, Junhao Ran, Muhe Ding, Shaokun Wang et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03163) | [PDF](https://arxiv.org/pdf/2611.03163) | [Code](https://github.com/eqcy/FineCraft)

<details>
<summary>Abstract</summary>

Fine-grained manipulation couples instruction grounding, local visual precision, and sustained execution. We present FineCraft, a framework that adapts pretrained models for fine-grained manipulation in the MetaFine Challenge. A task-routed mixture of policies selects independently adapted DINOv2-DiT or pretrained $π_{0.5}$ policies through a common observation-action interface. Local visual features help identify the instructed object parts, demonstrations and expert continuations teach the required actions, and new observations guide replanning during execution. FineCraft ranks fourth with a...

</details>

<details>
<summary>Share</summary>

```
FineCraft: Enhancing VLA Models for Fine-Grained Manipulation

Fine-grained manipulation couples instruction grounding, local visual precision, and sustained execution.

arXiv: https://arxiv.org/abs/2611.03163
Code: https://github.com/eqcy/FineCraft

#VLA #robotics
```

</details>

---

### [HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation](https://arxiv.org/abs/2611.02660)

**Authors:** Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.02660) | [PDF](https://arxiv.org/pdf/2611.02660) | [Project Page](https://kimspacehuni.github.io/HeLM/)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have enabled fine manipulation capabilities, yet performing tasks that require working memory remains a key challenge. Most existing VLA architectures operate under a Markovian assumption, mapping only the current observation to an action, which leads to failure in non-Markovian environments. Inspired by the human 'inner monologue', we propose Hierarchical Explicit Language Memory (HeLM), a hierarchical VLA framework that maintains task-relevant history in explicit language through factorized event detection and event-triggered memory upda...

</details>

<details>
<summary>Share</summary>

```
HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation

Recent advances in Vision-Language-Action (VLA) models have enabled fine manipulation capabilities, yet performing tasks that require working memory remains a key challenge.

arXiv: https://arxiv.org/abs/2611.02660
Project page: https://kimspacehuni.github.io/HeLM/

#VLA #robotics
```

</details>

---

### [RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)

**Authors:** Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh, Gang Yang, Jiamo Hu et al. (27 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.02497) | [PDF](https://arxiv.org/pdf/2611.02497) | [Project Page](https://robocolosseum.ai/)

<details>
<summary>Abstract</summary>

General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that combines unified policy serving and standardized protocols across a network of locally operated robots in diverse environments. Our initial study evaluates five vision-language-action (VLA) policies and three frontier AI agents across four embodiments (SO-101, Franka, Bimanual-YAM, and G1 Humanoid). The Open Track compares models without task-specific...

</details>

<details>
<summary>Share</summary>

```
RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild

General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce.

arXiv: https://arxiv.org/abs/2611.02497
Project page: https://robocolosseum.ai/

#VLA #robotics
```

</details>

---

### [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)

**Authors:** Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang, Jinjing Zhao et al. (21 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01112) | [PDF](https://arxiv.org/pdf/2611.01112) | [Project Page](https://auriga.stelledge.com/) | [Code](https://github.com/lose4578/Auriga)

<details>
<summary>Abstract</summary>

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3% of this gap in zero-shot manipulation without target-task trials or resets. In Auriga, the model makes all task decisions over an explicit task belief and acts through either direc...

</details>

<details>
<summary>Share</summary>

```
Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies.

arXiv: https://arxiv.org/abs/2611.01112
Project page: https://auriga.stelledge.com/
Code: https://github.com/lose4578/Auriga

#VLA #robotics
```

</details>

---

### [VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression](https://arxiv.org/abs/2610.41609)

**Authors:** Minsu Jang, Jae-Woo Choi, Youngwoo Yoon, Dohyung Kim

**Published:** 2026-10-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.41609) | [PDF](https://arxiv.org/pdf/2610.41609) | [Code](https://github.com/zebehn/vla-start-suppression)

<details>
<summary>Abstract</summary>

A robot should act only on an instruction from a person or on an intent that the robot explicitly represents and generates. Unintended actions taken without such an instruction can cause risk or inconvenience to people and the environment. We examine how recent vision-language-action (VLA) policies respond when the instruction is missing or meaningless. We apply a paired protocol with empty, neutral, nonsense, infeasible, and wrong-task instructions to six model checkpoints in LIBERO-Goal simulation. Holding the initial state fixed and varying only the instruction, we ask three questions: whet...

</details>

<details>
<summary>Share</summary>

```
VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression

A robot should act only on an instruction from a person or on an intent that the robot explicitly represents and generates.

arXiv: https://arxiv.org/abs/2610.41609
Code: https://github.com/zebehn/vla-start-suppression

#VLA #robotics
```

</details>

---

### [STAR: Steering Action Representations during Inference](https://arxiv.org/abs/2610.41009)

**Authors:** Guangyu Zhao, Yongchang Zhang, Haoxuan Ru, Kaichen He, Haoran Wen et al. (9 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.41009) | [PDF](https://arxiv.org/pdf/2610.41009) | [Code](https://github.com/PKU-VaLuE-Lab/STAR)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) map language instructions and visual observations to robot actions, showing strong capabilities across robotic manipulation tasks. However, in our probing experiment, we find that action representations near the action output do not fully preserve task-relevant visual grounding. Motivated by this late-layer grounding gap, we introduce STAR, for STeering Action Representations, a training-free inference method for pre-trained VLAs. STAR applies an exponential moving average over late-layer residual updates, allowing later action representations to inherit ob...

</details>

<details>
<summary>Share</summary>

```
STAR: Steering Action Representations during Inference

Vision-language-action models (VLAs) map language instructions and visual observations to robot actions, showing strong capabilities across robotic manipulation tasks.

arXiv: https://arxiv.org/abs/2610.41009
Code: https://github.com/PKU-VaLuE-Lab/STAR

#VLA #robotics
```

</details>

---

### [Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565)

**Authors:** Pranjal Aggarwal, Sean Welleck

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40565) | [PDF](https://arxiv.org/pdf/2610.40565) | [Project Page](https://gym-anything.github.io/robotics)

<details>
<summary>Abstract</summary>

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything for Robotics, a framework in which coding agents create realistic robotics simulations. Our core insight is that simulation creation is a coding agent task, so improvements in codi...

</details>

<details>
<summary>Share</summary>

```
Gym-Anything for Robotics: Scaling physical simulations with digital agents

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world.

arXiv: https://arxiv.org/abs/2610.40565
Project page: https://gym-anything.github.io/robotics

#VLA #robotics
```

</details>

---

### [RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence](https://arxiv.org/abs/2610.40026)

**Authors:** Xin Ma, Furong Chen, Xinlong Man, Bo Zhang, Yalong Guo et al. (12 authors)

**Published:** 2026-10-29 (updated 2026-11-02) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40026) | [PDF](https://arxiv.org/pdf/2610.40026) | [Code](https://github.com/PrimitiveX/RoboSeed)

<details>
<summary>Abstract</summary>

Choosing a robot action model requires evidence about task capability, adaptation cost, deployment requirements, and the reliability of reported conclusions. Success rates alone offer limited guidance to researchers with different computing budgets and goals. We propose RoboSeed, a multidimensional evaluation framework for vision-language-action (VLA) and world-action models (WAM), within a continuing program to train, evaluate, and openly release robot models with verifiable evidence for model selection. The framework defines five dimensions: capability, downstream training affordability, dep...

</details>

<details>
<summary>Share</summary>

```
RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence

Choosing a robot action model requires evidence about task capability, adaptation cost, deployment requirements, and the reliability of reported conclusions.

arXiv: https://arxiv.org/abs/2610.40026
Code: https://github.com/PrimitiveX/RoboSeed

#VLA #robotics
```

</details>

---

### [OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287)

**Authors:** Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian et al. (12 authors)

**Published:** 2026-10-29 (updated 2026-10-30) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39287) | [PDF](https://arxiv.org/pdf/2610.39287) | [Code](https://github.com/Ideal-ljl/AeroBrain)

<details>
<summary>Abstract</summary>

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act. Endowing aerial robots with an analogous functional organization remains challenging, as existing systems are often specialized for individual capabilities, dependent on offboard computation, or unable to sustain closed-loop operation on resource-constrained platforms. We present OpenFlyV2, a unified onboard vision-language-action architecture that uses a shared vision-language representation to support semantic understanding,...

</details>

<details>
<summary>Share</summary>

```
OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act.

arXiv: https://arxiv.org/abs/2610.39287
Code: https://github.com/Ideal-ljl/AeroBrain

#VLA #robotics
```

</details>

---

### [Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies](https://arxiv.org/abs/2611.02777)

**Authors:** Zhennan Jiang, Tingying Xie, Shilong Ji, Shu'ang Yu, Tianxing Zhou et al. (14 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.02777) | [PDF](https://arxiv.org/pdf/2611.02777)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can handle noncritical stages of long-horizon manipulation yet fail during short precision-critical phases. Lightweight reinforcement learning (RL) specialists can address these failures without directly applying RL to the full VLA, but retain auxiliary controllers and switching mechanisms at deployment. We study how to transfer their capabilities into a single flow-matching VLA. Direct imitation of specialist rollouts can reproduce action jitter and leave the VLA unprepared for states encountered during its own execution. We introduce REPAIR, a value-guid...

</details>

<details>
<summary>Share</summary>

```
Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies

Vision-language-action (VLA) policies can handle noncritical stages of long-horizon manipulation yet fail during short precision-critical phases.

arXiv: https://arxiv.org/abs/2611.02777

#VLA #robotics
```

</details>

---

### [Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models](https://arxiv.org/abs/2611.01713)

**Authors:** Chan Park, Sunwoo Hong, Kirak Kim, Yoonjeong Park, Alexander W. Olson et al. (6 authors)

**Published:** 2026-11-01 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01713) | [PDF](https://arxiv.org/pdf/2611.01713)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can generate task-oriented robot actions, but they do not guarantee safe execution in obstacle-rich manipulation scenes. Although CBF-QP safety filters can locally project unsafe actions into a safe set, such correction may push the robot away from the learned task trajectory and leave the VLA policy without a reliable recovery direction. We propose Route-Guided CBF-QP Repair, a post-hoc repair module that uses the short-horizon action chunk predicted by the VLA to detect blocked nominal trajectories and generate entry-exit-rejoin guidance around obstacles....

</details>

<details>
<summary>Share</summary>

```
Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models

Vision-language-action (VLA) models can generate task-oriented robot actions, but they do not guarantee safe execution in obstacle-rich manipulation scenes.

arXiv: https://arxiv.org/abs/2611.01713

#VLA #robotics
```

</details>

---

### [Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency](https://arxiv.org/abs/2611.01390)

**Authors:** Fuyi Chen

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01390) | [PDF](https://arxiv.org/pdf/2611.01390)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict chunks of future actions, yet deployed robots waste time in two ways that are independent of model capability: they halt while the next chunk is inferred, and they move at the speed of slow, cautious demonstrations. Existing remedies remove one loss each, and stacking them fails, because asynchrony and speed-up each change the correspondence between planned progress and executed motion. We present Path-preserving Time Scaling (PTS), a training-free execution layer for frozen action-chunking policies built on one principle: the robot's motion is a tim...

</details>

<details>
<summary>Share</summary>

```
Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

Vision-language-action (VLA) models predict chunks of future actions, yet deployed robots waste time in two ways that are independent of model capability: they halt while the next chunk is inferred, and they move at t...

arXiv: https://arxiv.org/abs/2611.01390

#VLA #robotics
```

</details>

---

### [Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2611.00896)

**Authors:** Rafiqul Islam

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00896) | [PDF](https://arxiv.org/pdf/2611.00896)

<details>
<summary>Abstract</summary>

Simulation-based VLA evaluation often treats matching task, seed, and episode identifiers as sufficient evidence that two policies faced identical test conditions. Under specific vectorized reset and autoreset conditions, different termination timing can change subsequent initial-state assignment, so the same episode index need not mean the same test state. We present an evaluation-integrity framework for paired comparison - invariants I1-I5, provenance logging, optional scene fingerprints, and an automated checker - and a controlled LeRobot 0.6.1 LIBERO harness study with emulated controllers...

</details>

<details>
<summary>Share</summary>

```
Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models

Simulation-based VLA evaluation often treats matching task, seed, and episode identifiers as sufficient evidence that two policies faced identical test conditions.

arXiv: https://arxiv.org/abs/2611.00896

#VLA #robotics
```

</details>

---

### [Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)

**Authors:** James Tcheng, Feiyu Gavin Zhu

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00522) | [PDF](https://arxiv.org/pdf/2611.00522)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is increasingly used to adapt pretrained vision-language-action models (VLAs). We investigate the problem of behavioral steering: adapting a VLA's execution style to preferences such as carrying objects higher. To investigate how little trainable capacity such steering requires and how much pretrained capability can be retained, we freeze an OpenVLA-OFT 7B policy and optimize TinyLoRA adapters with 8 to 384 trainable parameters using either policy-gradient RL (GRPO) or evolutionary search (CMA-ES). With just 256 trainable parameters, we raise carry height by 120 mm...

</details>

<details>
<summary>Share</summary>

```
Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime

Reinforcement learning (RL) is increasingly used to adapt pretrained vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.00522

#VLA #robotics
```

</details>

---

### [ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding](https://arxiv.org/abs/2611.01190)

**Authors:** Zilong Huang, Zipeng Ye, Caicheng Wang, Yuchen Xie, Jiaxiang Luo

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01190) | [PDF](https://arxiv.org/pdf/2611.01190) | [Project Page](https://clothdojo.github.io/)

<details>
<summary>Abstract</summary>

Garment flattening and folding require robots to identify garment structure during manipulation and adapt their actions as the cloth deforms. We present ClothDojo, a simulation platform that generates adaptive manipulation trajectories at scale across diverse garments and initial states and evaluates policies in closed loop. ClothDojo encodes each garment's canonical mesh coordinates as an NOCS texture, providing canonical surface-position cues through the visual interface of a pretrained vision-language-action model. We fine-tune the model on human demonstrations and corrections to obtain a d...

</details>

<details>
<summary>Share</summary>

```
ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding

Garment flattening and folding require robots to identify garment structure during manipulation and adapt their actions as the cloth deforms.

arXiv: https://arxiv.org/abs/2611.01190
Project page: https://clothdojo.github.io/

#VLA #robotics
```

</details>

---

### [SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2610.41408)

**Authors:** Haesung Lee, Insu Han

**Published:** 2026-10-30 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.41408) | [PDF](https://arxiv.org/pdf/2610.41408)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms. Weight quantization is a natural remedy, yet post-training quantization (PTQ) recipes inherited from large language models degrade when applied to VLAs at ultra-low precision. Existing low-bit PTQ methods often fail to explicitly account for the structure of downstream operations and allocate precision without considering its effect on the policy actions. We introduce SACQ, an ultra- low-bit weight-only vector-codebook quantization fra...

</details>

<details>
<summary>Share</summary>

```
SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models

Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms.

arXiv: https://arxiv.org/abs/2610.41408

#VLA #robotics
```

</details>

---

### [When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)

**Authors:** Alex Zhou, Junhao Wu, Xueyang Zhou, Yixiao Huo, Hongcheng Gao et al. (8 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.41857) | [PDF](https://arxiv.org/pdf/2610.41857) | [Code](https://github.com/ALEXander22568/simuguard)

<details>
<summary>Abstract</summary>

Simulation benchmarks score robot policies by success rate, and every failed episode counts against the policy. Many of these failures are the simulator's fault, not the policy's; we find the cause and fix it. Testing a vision language action model and a world action model in simulation, we find that the policy often places the object and the simulator then ejects it, and that the benchmark's own scripted demonstrations fail the same way. We present SimuGuard, an auditing plugin for LIBERO, RoboTwin, RoboCasa and RoboDojo. It leaves the evaluation unchanged. At every physics step, it records t...

</details>

<details>
<summary>Share</summary>

```
When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks

Simulation benchmarks score robot policies by success rate, and every failed episode counts against the policy.

arXiv: https://arxiv.org/abs/2610.41857
Code: https://github.com/ALEXander22568/simuguard

#VLA #robotics
```

</details>

---

### [BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing](https://arxiv.org/abs/2610.40532)

**Authors:** Xiangyu Xu, Bangshuai Peng, Ziyi Liu, Mengjie Zhao, Chenhao Lu et al. (8 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.40532) | [PDF](https://arxiv.org/pdf/2610.40532) | [Project Page](https://siyingzhao.github.io/BURGER/)

<details>
<summary>Abstract</summary>

How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-conditioned robotic drawing benchmark with a scalable, prompt-driven pipeline for generating continuous drawing trajectories, both in simulation and the real world. In BURGER, an agent starts from the same blank canvas and controls a robot arm to draw the object or spatial composition specified by language, while each...

</details>

<details>
<summary>Share</summary>

```
BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing

How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales?

arXiv: https://arxiv.org/abs/2610.40532
Project page: https://siyingzhao.github.io/BURGER/

#VLA #robotics
```

</details>

---

### [HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373)

**Authors:** Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang et al. (7 authors)

**Published:** 2026-10-29 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.40373) | [PDF](https://arxiv.org/pdf/2610.40373)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately, while directly incorporating predicted futures into action policies without sufficiently considering their relevance to current action requirements. To address these limitations, we...

</details>

<details>
<summary>Share</summary>

```
HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation.

arXiv: https://arxiv.org/abs/2610.40373

#VLA #robotics
```

</details>

---

### [Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation](https://arxiv.org/abs/2610.38199)

**Authors:** Greta Perez-Haiek, Luca Macesanu, Kevin Angers, Mohammed Imam, Timothy Gambin et al. (6 authors)

**Published:** 2026-10-28 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.38199) | [PDF](https://arxiv.org/pdf/2610.38199) | [Project Page](https://lair-research-nyu.github.io/Embodied-at-Sea/)

<details>
<summary>Abstract</summary>

Behavior Cloning has demonstrated promising generalization capabilities for robotic manipulation in terrestrial environments. However, marine visual distortions and dynamic currents create a severe domain shift that remains a key bottleneck in adapting generalist architectures to underwater field manipulation. To address this, 1616 episodes of underwater manipulation data were collected in calm and turbulent waters and were used to train 14 generalist Vision-Language-Action (VLA) models (DynamicVLA) with varying proprioception observation configurations. Across three tasks on 1260 gradable on-...

</details>

<details>
<summary>Share</summary>

```
Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation

Behavior Cloning has demonstrated promising generalization capabilities for robotic manipulation in terrestrial environments.

arXiv: https://arxiv.org/abs/2610.38199
Project page: https://lair-research-nyu.github.io/Embodied-at-Sea/

#VLA #robotics
```

</details>

---

### [SVD-Prune: Spectral Vision Token Pruning under Extreme Compression](https://arxiv.org/abs/2611.02284)

**Authors:** Yvon Apedo, Martyna Poreba, Michal Szczepanski, Samia Bouchafa

**Published:** 2026-11-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.02284) | [PDF](https://arxiv.org/pdf/2611.02284) | [Code](https://github.com/anoncvlab/svdPrune)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models process hundreds of visual tokens, making visual representations a major computational bottleneck. We argue that visual token pruning should be formulated not as identifying individually important tokens, but as preserving the dominant low-rank spectral structure of the visual representation. Based on this formulation, we introduce SVD-Prune, a training-free framework that leverages Singular Value Decomposition (SVD) and statistical leverage scores for globally informed token selection. SVD-Prune is architecture-agnostic and...

</details>

<details>
<summary>Share</summary>

```
SVD-Prune: Spectral Vision Token Pruning under Extreme Compression

Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models process hundreds of visual tokens, making visual representations a major computational bottleneck.

arXiv: https://arxiv.org/abs/2611.02284
Code: https://github.com/anoncvlab/svdPrune

#VLA #robotics
```

</details>

---

### [CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision](https://arxiv.org/abs/2611.00394)

**Authors:** Boniface Chukwuemeka Godwin

**Published:** 2026-10-30 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00394) | [PDF](https://arxiv.org/pdf/2611.00394)

<details>
<summary>Abstract</summary>

Can a vision-language-action (VLA) policy signal likely task failure from its own action probabilities? We introduce CalVLA, which shapes native action-token confidence using successful and failed rollouts and an Action-Confidence Alignment (ACal) squared margin-ranking loss. Low-rank adapters update OpenVLA-7B without an auxiliary failure detector. Observations are paired within tasks at similar normalized elapsed times, not necessarily equivalent physical progress. On a held-out test split from 500 LIBERO-10 configurations, adapted confidence achieves a joint failure-discrimination AUROC of...

</details>

<details>
<summary>Share</summary>

```
CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision

Can a vision-language-action (VLA) policy signal likely task failure from its own action probabilities?

arXiv: https://arxiv.org/abs/2611.00394

#VLA #robotics
```

</details>

---

### [CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents](https://arxiv.org/abs/2610.40799)

**Authors:** Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang et al. (6 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.40799) | [PDF](https://arxiv.org/pdf/2610.40799)

<details>
<summary>Abstract</summary>

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-...

</details>

<details>
<summary>Share</summary>

```
CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it.

arXiv: https://arxiv.org/abs/2610.40799

#VLA #robotics
```

</details>

---

### [How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function](https://arxiv.org/abs/2610.40002)

**Authors:** Dabin Seo, Eunhyek Joa

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.40002) | [PDF](https://arxiv.org/pdf/2610.40002)

<details>
<summary>Abstract</summary>

Reasoning vision-language-action (VLA) policies write a reasoning trace and then decode the action from it. A wrong trace yields a wrong action, and even a correct-looking trace can mislead the plan. Existing remedies ask whether the reasoning is right. We ask how strongly it should steer. CoC-CFG applies classifier-free guidance between the policy's context and the same context without the reasoning span. One weight per Euler step attenuates or amplifies the reasoning, and w=1 recovers the original policy. We treat the choice of this weight as a Markov decision process whose action values are...

</details>

<details>
<summary>Share</summary>

```
How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function

Reasoning vision-language-action (VLA) policies write a reasoning trace and then decode the action from it.

arXiv: https://arxiv.org/abs/2610.40002

#VLA #robotics
```

</details>

---

### [UMI-Live for In-The-Wild Bimanual Robotics Data Collection](https://arxiv.org/abs/2610.39385)

**Authors:** Govind Velamoor, Adrian Lin, Sam Jung, Spencer Mateega, Brandon Y. Yang et al. (6 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.39385) | [PDF](https://arxiv.org/pdf/2610.39385) | [Project Page](https://umi-live.github.io/)

<details>
<summary>Abstract</summary>

Universal Manipulation Interface (UMI) devices allow human experts to demonstrate tasks for robot learning without teleoperating physical robots. Using these demonstrations as training data still requires a consistent hardware setup, calibration, and data processing. We present UMI-Live, a full-stack open-source bimanual UMI system for in-the-wild data collection. We design our custom UMI-Live hardware to integrate camera and LiDAR--inertial sensing, onboard compute, and power, without external tracking equipment or calibration within the collection environment. We implement a simple user inte...

</details>

<details>
<summary>Share</summary>

```
UMI-Live for In-The-Wild Bimanual Robotics Data Collection

Universal Manipulation Interface (UMI) devices allow human experts to demonstrate tasks for robot learning without teleoperating physical robots.

arXiv: https://arxiv.org/abs/2610.39385
Project page: https://umi-live.github.io/

#VLA #robotics
```

</details>

---

### [SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control](https://arxiv.org/abs/2610.38508)

**Authors:** Rufeng Xiao, Ruihao Xiao, Wei Chen, Xinhai Sun

**Published:** 2026-10-28 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.38508) | [PDF](https://arxiv.org/pdf/2610.38508)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn to predict representations rather than pixels, offering a compact way to model how visual scenes evolve. We ask whether this predictive objective improves closed-loop control when a vision-language-action (VLA) policy already uses V-JEPA features. We call our JEPA-conditioned flow policy family SaiVLA-JEPA. It combines a vision-language model with a diffusion transformer action expert and receives features from a frozen V-JEPA encoder. Two lightweight auxiliary heads predict future representations during training and are omitted at inferen...

</details>

<details>
<summary>Share</summary>

```
SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control

Joint-embedding predictive architectures (JEPAs) learn to predict representations rather than pixels, offering a compact way to model how visual scenes evolve.

arXiv: https://arxiv.org/abs/2610.38508

#VLA #robotics
```

</details>

---

### [Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone](https://arxiv.org/abs/2611.01011)

**Authors:** Lin Yang, Yunjie Shen, Zheyu Li, Zhenjie Tian, Yongli Wang et al. (11 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01011) | [PDF](https://arxiv.org/pdf/2611.01011)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive control requires 20-50 Hz. We present a VLA that decouples the two: a VLM runs as a low-frequency semantic anchor whose cached context is reused across control steps, while a flow-matching action expert operates at high frequency, consuming the cached semantics with a fresh, low-latency visual stream from a compact encoder pretrained on robot video with masked reconstruction, opt...

</details>

<details>
<summary>Share</summary>

```
Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone

Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive...

arXiv: https://arxiv.org/abs/2611.01011

#VLA #robotics
```

</details>

---

### [Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks](https://arxiv.org/abs/2611.03168)

**Authors:** Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.03168) | [PDF](https://arxiv.org/pdf/2611.03168)

<details>
<summary>Abstract</summary>

We release all 3,718 episodes from the ArmnetBench v0.1 evaluation (arXiv:2607.24481), which contains 600 teleoperated demonstrations and 3,118 rollouts of seven imitation-learning and vision-language-action policies on 12 tabletop tasks, recorded on low-cost SO-101 arms; 73% of the rollouts are failures. Every policy for a task was trained or fine-tuned on the same 50 demonstrations and rolled out on the same cell, so the corpus contains many policies' failures on shared tasks. An operator labelled every rollout successful, suboptimal or failure. Each episode has three camera views, joint sta...

</details>

<details>
<summary>Share</summary>

```
Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks

We release all 3,718 episodes from the ArmnetBench v0.1 evaluation (arXiv:2607.24481), which contains 600 teleoperated demonstrations and 3,118 rollouts of seven imitation-learning and vision-language-action policies...

arXiv: https://arxiv.org/abs/2611.03168

#VLA #robotics
```

</details>

---

### [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729)

**Authors:** Jindou Jia, Jingliang Li, Kuangji Zuo, Tuo An, Yuxuan Hu et al. (12 authors)

**Published:** 2026-11-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01729) | [PDF](https://arxiv.org/pdf/2611.01729)

<details>
<summary>Abstract</summary>

Most robot policies, whether trained by imitation learning (IL) or reinforcement learning (RL), map observations to action values at discrete control steps and leave the continuity of physical motion to be learned implicitly. We propose ODE policy, which learns the dynamics of the action rather than the action itself. A neural ordinary differential equation (ODE) learns the vector field of the action by matching the integrated actions to the targets over short action chunks in IL and single control steps in RL. A lightweight diversity head captures multi-modal behavior by randomizing the direc...

</details>

<details>
<summary>Share</summary>

```
ODE Policy: Robot Learning via Action Dynamics, Not Actions

Most robot policies, whether trained by imitation learning (IL) or reinforcement learning (RL), map observations to action values at discrete control steps and leave the continuity of physical motion to be learned imp...

arXiv: https://arxiv.org/abs/2611.01729

#VLA #robotics
```

</details>

---

### [GatedVLA with Camera-Based Emergency Braking: AlpaSim E2E Closed Loop Challenge Technical Report](https://arxiv.org/abs/2611.01663)

**Authors:** Kaneyoshi Hiratsuka, Naoki Takada, Makoto Kawano

**Published:** 2026-11-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01663) | [PDF](https://arxiv.org/pdf/2611.01663)

<details>
<summary>Abstract</summary>

This report presents GatedVLA, our entry for the Physical AI AV (PAI-AV) track. Our learned vision-language-action (VLA) policy pairs the driving-pretrained Qwen-Drive-1.0-4B vision-language model with a layer-wise flow-matching action expert that outputs a 2.5 s horizon of acceleration and curvature controls, augmented with a soft visual mask applied to the expert's cross-attention. Compared to an identically trained baseline, the masked policy achieves comparable overall open-loop error while reducing error on left turns. In local closed-loop evaluation across the same 150 scenes (two rollou...

</details>

<details>
<summary>Share</summary>

```
GatedVLA with Camera-Based Emergency Braking: AlpaSim E2E Closed Loop Challenge Technical Report

This report presents GatedVLA, our entry for the Physical AI AV (PAI-AV) track.

arXiv: https://arxiv.org/abs/2611.01663

#VLA #robotics
```

</details>

---

### [Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control](https://arxiv.org/abs/2611.01404)

**Authors:** Sida He

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01404) | [PDF](https://arxiv.org/pdf/2611.01404)

<details>
<summary>Abstract</summary>

Agentic robots combine a vision-language brain, a tool-using harness, and a vision-language-action (VLA) policy. Serving a fleet of these agents introduces two coupled resource constraints: the brain repeatedly revisits long, growing key-value (KV) cache states, while the VLA executes action chunks under tight control deadlines. We characterize 80 LIBERO-PRO episodes generated by GPT-6-Astra, RPent, and pi0.5 (1,862 brain turns and 1,582 VLA inference chunks), profile both layers on H800 graphics processing units (GPUs), and replay the resulting agent programs on a vLLM serving engine. Brain c...

</details>

<details>
<summary>Share</summary>

```
Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control

Agentic robots combine a vision-language brain, a tool-using harness, and a vision-language-action (VLA) policy.

arXiv: https://arxiv.org/abs/2611.01404

#VLA #robotics
```

</details>

---

### [When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem](https://arxiv.org/abs/2611.02101)

**Authors:** Liangkai Liu, Bimal Thapa Magar

**Published:** 2026-11-01 | **Categories:** cs.RO, cs.CV, cs.ET | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.02101) | [PDF](https://arxiv.org/pdf/2611.02101)

<details>
<summary>Abstract</summary>

Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations in the physical environment, the model, the computing platform, and execution interact in closed loop. We formalize this as cross-layer variation propagation across these system layers and use an interaction contrast to measure when joint var...

</details>

<details>
<summary>Share</summary>

```
When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods...

arXiv: https://arxiv.org/abs/2611.02101

#VLA #robotics
```

</details>

---

### [Vision-Language Models Are Joint Denoisers in Robotic Action Generation](https://arxiv.org/abs/2611.01215)

**Authors:** Xicheng Gong, Wenxuan Song, Chengze Liu, Qiwei Li, Qize Yu et al. (8 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01215) | [PDF](https://arxiv.org/pdf/2611.01215)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning. This separation limits how much pretrained perception and reasoning can guide action generation, especially in out-of-distribution settings. We introduce JADE, a Joint Action DEnoiser that enables the VLM and action expert to jointly refine actions. Our key insight is that structured action latents allow the VLM to read the current noisy action together with visual observations and language instructi...

</details>

<details>
<summary>Share</summary>

```
Vision-Language Models Are Joint Denoisers in Robotic Action Generation

Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning.

arXiv: https://arxiv.org/abs/2611.01215

#VLA #robotics
```

</details>

---

### [STEER: Route-Aware Adaptive Reasoning for Autonomous Driving](https://arxiv.org/abs/2611.00718)

**Authors:** Yangang Zou, Pei Liu, Nan Song, Bozhou Zhang, Mingyu Guo et al. (9 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00718) | [PDF](https://arxiv.org/pdf/2611.00718)

<details>
<summary>Abstract</summary>

Vision-language action (VLA) models excel for end-to-end autonomous driving, yet their tendency to over-invoke chain-of-thought (CoT) reasoning mirrors a human cognitive pitfall: overthinking. Just as deliberate reasoning can slow or mislead human judgment in routine tasks, excessive CoT in VLA incurs unnecessary compute overhead and can paradoxically degrade planning performance. Recent research tackles this via adaptive reasoning, which dynamically modulates inference complexity by selectively triggering CoT for complex scenes while responding directly to routine ones. While prior adaptive m...

</details>

<details>
<summary>Share</summary>

```
STEER: Route-Aware Adaptive Reasoning for Autonomous Driving

Vision-language action (VLA) models excel for end-to-end autonomous driving, yet their tendency to over-invoke chain-of-thought (CoT) reasoning mirrors a human cognitive pitfall: overthinking.

arXiv: https://arxiv.org/abs/2611.00718

#VLA #robotics
```

</details>

---

### [Learning from an Imitable Teacher: Competition Solution for the MetaFine Challenge](https://arxiv.org/abs/2611.00615)

**Authors:** Yanze Zhang, Hao Liu, Haochang Hao, Zhixiang Shen, Chunyu Miao et al. (6 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00615) | [PDF](https://arxiv.org/pdf/2611.00615)

<details>
<summary>Abstract</summary>

The MetaFine Open Competition (RoboFineMani workshop, CoRL 2026) evaluates fine-grained manipulation beyond binary success. Its five simulated tasks, from grasping a bottle by an instructed part to inserting letter-shaped pegs with 4 mm clearance, are scored on perception under lighting and camera changes, instruction understanding, and behavior. This report presents Team Friday's solution, which got second place with an overall score of 0.947, more than twice the $π_0$ baseline. Instead of fine-tuning a large vision-language-action (VLA) model, we train one 19M-parameter policy per task with...

</details>

<details>
<summary>Share</summary>

```
Learning from an Imitable Teacher: Competition Solution for the MetaFine Challenge

The MetaFine Open Competition (RoboFineMani workshop, CoRL 2026) evaluates fine-grained manipulation beyond binary success.

arXiv: https://arxiv.org/abs/2611.00615

#VLA #robotics
```

</details>

---

### [TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking](https://arxiv.org/abs/2610.41275)

**Authors:** Mingyang Lyu, Gongce Cao, Yiyang Jia, Lu Jia, Erliang Lin et al. (10 authors)

**Published:** 2026-10-30 (updated 2026-11-02) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.41275) | [PDF](https://arxiv.org/pdf/2610.41275)

<details>
<summary>Abstract</summary>

Embodied visual tracking requires a robot to follow a language-specified person under occlusion, look-alike distractors, and ambiguous instructions. We show that improving tracking persistence can simultaneously increase safety violations. Using a compact 0.6B vision-language-action (VLA) tracker with a frozen backbone, we update only the planner head with proximal policy optimization (PPO). PPO improves success and following rates across all three EVT-Bench settings, but increases the collision rate on distracted tracking because episodes that previously ended in target loss can instead end i...

</details>

<details>
<summary>Share</summary>

```
TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking

Embodied visual tracking requires a robot to follow a language-specified person under occlusion, look-alike distractors, and ambiguous instructions.

arXiv: https://arxiv.org/abs/2610.41275

#VLA #robotics
```

</details>

---

### [TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](https://arxiv.org/abs/2610.40349)

**Authors:** Haozhe Zhang, Gu Zhang, Zirui Zou, Yuzheng Chen, Jinlong Wu et al. (10 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.40349) | [PDF](https://arxiv.org/pdf/2610.40349)

<details>
<summary>Abstract</summary>

Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions. We present TouchBridge, a hardware--software co-designed framework for human-to-robot data transformation. A wearable human demonstration interface and a corresponding robot interface establish cross-embodiment correspondence in visual and fingertip tactile sensing. We introduce Tac-Retarget, a tactile-conditioned retargeting method that uses measured contact to align fingertip contact patches...

</details>

<details>
<summary>Share</summary>

```
TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation

Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions.

arXiv: https://arxiv.org/abs/2610.40349

#VLA #robotics
```

</details>

---

### [LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks](https://arxiv.org/abs/2610.40016)

**Authors:** Enqiao Lu, Yuxiang Xie, Xingrui Yu, Yuyang Wang, Yipeng Gu et al. (13 authors)

**Published:** 2026-10-29 (updated 2026-11-02) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.40016) | [PDF](https://arxiv.org/pdf/2610.40016)

<details>
<summary>Abstract</summary>

Agentic robots must turn a high-level goal into actions while keeping the physical conditions needed for future steps valid. A completed action does not ensure that its effects will persist: a later disturbance can invalidate support that the remaining plan still assumes. We present LOGIV, a graph engineering framework for agentic robot execution that uses an explicit task graph to connect symbolic planning, observation-based verification, and embodied action. LOGIV compiles a validated plan into condition-support and resource-ordering edges, checks their physical validity during execution, an...

</details>

<details>
<summary>Share</summary>

```
LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks

Agentic robots must turn a high-level goal into actions while keeping the physical conditions needed for future steps valid.

arXiv: https://arxiv.org/abs/2610.40016

#VLA #robotics
```

</details>

---

### [Smooth Action Chunking Via Movement-Primitive Representations for Imitation Learning](https://arxiv.org/abs/2610.39451)

**Authors:** Shota Nomura, Takayuki Osa, Yasuhiro Kato, Kazuki Ota, Naoki Shitanda et al. (6 authors)

**Published:** 2026-10-29 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.39451) | [PDF](https://arxiv.org/pdf/2610.39451)

<details>
<summary>Abstract</summary>

Imitation learning has become a widely adopted approach for vision-based robot policies, owing to its conceptual simplicity, scalability, and ability to leverage large-scale datasets. As these policies have grown more capable, action chunking has become their standard interface. At each decision step the policy outputs several future actions at once. Backbones from diffusion policies to large vision-language-action models all share it. Whatever backbone produces the chunk, its temporal structure is learned only implicitly. The commanded trajectory is therefore jerky both within a chunk and bet...

</details>

<details>
<summary>Share</summary>

```
Smooth Action Chunking Via Movement-Primitive Representations for Imitation Learning

Imitation learning has become a widely adopted approach for vision-based robot policies, owing to its conceptual simplicity, scalability, and ability to leverage large-scale datasets.

arXiv: https://arxiv.org/abs/2610.39451

#VLA #robotics
```

</details>

---

### [Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)

**Authors:** Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang, Wenbo Zhang, Kwanyoung Park et al. (28 authors)

**Published:** 2026-11-01 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.01560) | [PDF](https://arxiv.org/pdf/2611.01560)

<details>
<summary>Abstract</summary>

Robot-use Agents (RUAs) have shown promising zero-shot manipulation capabilities, but reliance on frontier, proprietary models limits research into further training. To democratize RUA research, we introduce uni-robot-agent, a unified harness for competitive open-weight robot use that supports further training. Without privileged inputs, an out-of-the-box Qwen3.8-Flash-Next achieves a RoboDojo Score of 31.39, surpassing the published GPT-6 Astra-RoboProbe result of 28.97 and many VLA/WAM baselines, and performs competitively on 19 real-world tasks. Our analysis across model generations, famili...

</details>

<details>
<summary>Share</summary>

```
Democratizing Robot-Use Agents: A Unified Harness with Open Models

Robot-use Agents (RUAs) have shown promising zero-shot manipulation capabilities, but reliance on frontier, proprietary models limits research into further training.

arXiv: https://arxiv.org/abs/2611.01560

#VLA #robotics
```

</details>

---

### [PREM: Prediction-Regulated Memory for Robot Manipulation](https://arxiv.org/abs/2611.00634)

**Authors:** Xiao Huang, Ya Zhang, Weidi Xie

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.00634) | [PDF](https://arxiv.org/pdf/2611.00634)

<details>
<summary>Abstract</summary>

A robot's next action can depend on recent motion or earlier visual evidence absent from its current observation. A recurrent visual-memory architecture can retain this history in a visual state, but its usefulness depends on what the state represents and how it is updated with new observations. We introduce Prediction-Regulated Memory (PREM), a framework that uses action-conditioned future prediction to guide both memory learning and updating in vision-language-action policies. During training, predicting future visual features provides temporal supervision for memory learning. During executi...

</details>

<details>
<summary>Share</summary>

```
PREM: Prediction-Regulated Memory for Robot Manipulation

A robot's next action can depend on recent motion or earlier visual evidence absent from its current observation.

arXiv: https://arxiv.org/abs/2611.00634

#VLA #robotics
```

</details>

---

### [REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](https://arxiv.org/abs/2610.42053)

**Authors:** Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, Haoyuan Chen, Zhenglin Wan et al. (8 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.42053) | [PDF](https://arxiv.org/pdf/2610.42053)

<details>
<summary>Abstract</summary>

Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative brain (foundation models) with a reactive cerebellum (fast policies) seems natural for embodied systems, two obstacles remain: methods are built and scored on incompatible stacks, and their asynchronous coordination is difficult. For example, an agent that calls the VLA in the agentic loop can stal...

</details>

<details>
<summary>Share</summary>

```
REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers.

arXiv: https://arxiv.org/abs/2610.42053

#VLA #robotics
```

</details>

---

### [From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation](https://arxiv.org/abs/2610.40828)

**Authors:** Ammar N. Abbas, Aayush Jain, Prashanth Viswanath, Nivesh Gadipudi, Giulia Vilone et al. (6 authors)

**Published:** 2026-10-29 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.40828) | [PDF](https://arxiv.org/pdf/2610.40828)

<details>
<summary>Abstract</summary>

Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered rob...

</details>

<details>
<summary>Share</summary>

```
From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation

Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion.

arXiv: https://arxiv.org/abs/2610.40828

#VLA #robotics
```

</details>

---

### [Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design](https://arxiv.org/abs/2610.40430)

**Authors:** Jingxu Gu, Dongze Lian

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.40430) | [PDF](https://arxiv.org/pdf/2610.40430)

<details>
<summary>Abstract</summary>

Fine-grained manipulation requires a robot policy to follow instructions, remain robust to visual variations, and translate predicted actions into precise robot control. We present Demonstration Expansion and Execution Design (DEED), a framework for adapting a pretrained vision-language-action policy to the five MetaFine tasks through structured demonstration expansion and execution design. DEED generates demonstrations for different instructions from the same initial scene and renders each physical trajectory under different camera positions and lighting conditions while preserving its origin...

</details>

<details>
<summary>Share</summary>

```
Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design

Fine-grained manipulation requires a robot policy to follow instructions, remain robust to visual variations, and translate predicted actions into precise robot control.

arXiv: https://arxiv.org/abs/2610.40430

#VLA #robotics
```

</details>

---
