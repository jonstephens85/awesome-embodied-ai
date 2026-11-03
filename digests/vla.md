# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-03 03:09 UTC

**Papers shown:** 46 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

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

**Published:** 2026-10-29 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

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

### [Vision-Language-Action or World-Action? Just Action Models](https://arxiv.org/abs/2610.37219)

**Authors:** Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki

**Published:** 2026-10-27 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37219) | [PDF](https://arxiv.org/pdf/2610.37219) | [Project Page](https://y0uroy.github.io/JAM)

<details>
<summary>Abstract</summary>

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupling these choices yields a common framework for both families, which we term Just Action Model (JAM):...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Action or World-Action? Just Action Models

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators.

arXiv: https://arxiv.org/abs/2610.37219
Project page: https://y0uroy.github.io/JAM

#VLA #robotics
```

</details>

---

### [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution](https://arxiv.org/abs/2610.37215)

**Authors:** Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho et al. (18 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37215) | [PDF](https://arxiv.org/pdf/2610.37215) | [Project Page](https://retrieve2act.github.io/r2a/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training experience. We introduce Retrieve to Act (R2A), a test-time scaling framework that formulates OOD robustness purely as a geometric motion primitive retrieval problem. R2A bypasses fragile visual features by structuring successful training demon...

</details>

<details>
<summary>Share</summary>

```
Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution

Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution.

arXiv: https://arxiv.org/abs/2610.37215
Project page: https://retrieve2act.github.io/r2a/

#VLA #robotics
```

</details>

---

### [SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420)

**Authors:** Truman Hickok

**Published:** 2026-10-27 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.36420) | [PDF](https://arxiv.org/pdf/2610.36420) | [Project Page](https://so101-bench.github.io/) | [Code](https://github.com/5hadytru/so101_bench)

<details>
<summary>Abstract</summary>

Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, 138 objects in seen, unseen-instance and unseen-class splits, 916 evaluation episodes with subsets f...

</details>

<details>
<summary>Share</summary>

```
SO-101 Bench: Accessible Spatial Manipulation

Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101...

arXiv: https://arxiv.org/abs/2610.36420
Project page: https://so101-bench.github.io/
Code: https://github.com/5hadytru/so101_bench

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

### [What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K](https://arxiv.org/abs/2610.37917)

**Authors:** Ruben Hammele, Samira Huber, Mohammad Nazeri, Amirreza Payandeh, Alexandyr T. Card et al. (10 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37917) | [PDF](https://arxiv.org/pdf/2610.37917) | [Project Page](https://rubenhammele.github.io/behavior2026)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for general-purpose household robotics. However, inference and data-collection strategies that have been deployed in smaller-scale settings do not necessarily generalize to large-scale, diverse task suites. To address this gap, we conduct a systematic, paired evaluation of previously proposed inference and data-collection strategies across all 100 tasks. Our evaluation uses a fine-tuned $π_{0.5}$ model based on the 2025 BEHAVIOR Challenge winner, which achieves a Q-score of 0.39 on the public test set. These results show that propo...

</details>

<details>
<summary>Share</summary>

```
What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K

Vision-Language-Action (VLA) models offer a promising paradigm for general-purpose household robotics.

arXiv: https://arxiv.org/abs/2610.37917
Project page: https://rubenhammele.github.io/behavior2026

#VLA #robotics
```

</details>

---

### [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666)

**Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang et al. (7 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.37666) | [PDF](https://arxiv.org/pdf/2610.37666) | [Project Page](https://thinkworld-project.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thou...

</details>

<details>
<summary>Share</summary>

```
ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations.

arXiv: https://arxiv.org/abs/2610.37666
Project page: https://thinkworld-project.github.io/

#VLA #robotics
```

</details>

---

### [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)

**Authors:** Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang et al. (15 authors)

**Published:** 2026-10-27 (updated 2026-10-29) | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.37381) | [PDF](https://arxiv.org/pdf/2610.37381)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation. The module learns through direct prediction of future RGB, depth, and optical-flow features, with auxiliary supervisio...

</details>

<details>
<summary>Share</summary>

```
PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited.

arXiv: https://arxiv.org/abs/2610.37381

#VLA #robotics
```

</details>

---

### [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](https://arxiv.org/abs/2610.37378)

**Authors:** Bojun Zou, Wenhao Yu, Jiaohao Li, Jiaxuan Lin, Guanting Ye et al. (9 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.37378) | [PDF](https://arxiv.org/pdf/2610.37378)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting such data is costly, especially for dynamic scenarios, and may degrade their original task capabilities. To address these limitations, we propose VLA-Stem, a lightweight, reinforcement-learning-based safety mechanism for VLA systems. Without...

</details>

<details>
<summary>Share</summary>

```
VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control.

arXiv: https://arxiv.org/abs/2610.37378

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

### [GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers](https://arxiv.org/abs/2610.36507)

**Authors:** Liang Li, Guoyao Zhang, Xingyu Chen, Sikai Wu, Qianyang Wu et al. (9 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.36507) | [PDF](https://arxiv.org/pdf/2610.36507) | [Project Page](https://graft-humanoid.github.io/)

<details>
<summary>Abstract</summary>

Humanoid behavior foundation models (BFMs) provide reusable whole-body motion priors: given a kinematic reference, they generate coordinated joint commands for motion replay, teleoperation, and VLA control. However, trained primarily on flat-ground motion, BFMs lack an explicit mechanism to adapt foot placement, swing clearance, and contact timing to local terrain. Many terrain-aware BFM approaches address this limitation by retraining or fine-tuning the tracker together with perception, incurring substantial data and computation costs while coupling ordinary tracking to the perception pathway...

</details>

<details>
<summary>Share</summary>

```
GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers

Humanoid behavior foundation models (BFMs) provide reusable whole-body motion priors: given a kinematic reference, they generate coordinated joint commands for motion replay, teleoperation, and VLA control.

arXiv: https://arxiv.org/abs/2610.36507
Project page: https://graft-humanoid.github.io/

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

**Published:** 2026-10-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

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

**Published:** 2026-10-29 (updated 2026-10-30) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

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

### [Self-Labeled Preference Transfer for Steerable Robot Manipulation](https://arxiv.org/abs/2610.38000)

**Authors:** Kaiwen Hong, Shaoting Peng, Xiangyu Zeng, Pengcheng Wang, Boyuan Tian et al. (9 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.38000) | [PDF](https://arxiv.org/pdf/2610.38000)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can learn to follow execution preferences, such as where to grasp an object or how to move around an obstacle, from demonstrations annotated with preference labels. Providing these annotations for every new task, however, is costly. We study whether learned preference control can transfer to new tasks whose demonstrations contain the desired behaviors but lack preference annotations. We find that a policy trained with preference annotations can follow preferences on a new task before adaptation but achieves limited task success. Fine-tuning on target demon...

</details>

<details>
<summary>Share</summary>

```
Self-Labeled Preference Transfer for Steerable Robot Manipulation

Vision-language-action (VLA) policies can learn to follow execution preferences, such as where to grasp an object or how to move around an obstacle, from demonstrations annotated with preference labels.

arXiv: https://arxiv.org/abs/2610.38000

#VLA #robotics
```

</details>

---

### [Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer](https://arxiv.org/abs/2610.37330)

**Authors:** Hanwen Ren, Meng Zheng, Wenzhe Cui, Benjamin Planche, Zhongpai Gao et al. (8 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.37330) | [PDF](https://arxiv.org/pdf/2610.37330)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor execution errors rapidly compound into unrecoverable, out-of-distribution failures. To address this limitation, we propose Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies. AFIL uses a pretrained VLA to generate failure rollouts online, avoiding the need...

</details>

<details>
<summary>Share</summary>

```
Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer

Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor...

arXiv: https://arxiv.org/abs/2610.37330

#VLA #robotics
```

</details>

---

### [Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition](https://arxiv.org/abs/2610.36765)

**Authors:** Lifan Zheng, Guotao Chen, Zhenyang Li, Shujie Cui, Qiang Huang et al. (6 authors)

**Published:** 2026-10-27 (updated 2026-10-29) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.36765) | [PDF](https://arxiv.org/pdf/2610.36765)

<details>
<summary>Abstract</summary>

We fine-tuned a separate $π_{0.5}$ policy for each of the five tasks in the MetaFine Open Competition, with a task-specific training mixture and number of actions executed per prediction. Training started from the official demonstrations and expert procedures. Local evaluation exposed recurring grasping, pushing, and insertion failures. We addressed them by revising the demonstrated motions and by adding expert continuations from states the policy reached, while keeping nominal demonstrations in training. Checkpoints were compared on every instruction, so that a gain on one instruction could n...

</details>

<details>
<summary>Share</summary>

```
Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition

We fine-tuned a separate $π_{0.5}$ policy for each of the five tasks in the MetaFine Open Competition, with a task-specific training mixture and number of actions executed per prediction.

arXiv: https://arxiv.org/abs/2610.36765

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

### [World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer](https://arxiv.org/abs/2610.37518)

**Authors:** Guoning Wu, Zijian Cai, Yuhang Zhang, Ying Liu, Yongbin Zheng

**Published:** 2026-10-27 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.37518) | [PDF](https://arxiv.org/pdf/2610.37518)

<details>
<summary>Abstract</summary>

Multi-robot control requires integrating distributed camera views while predicting separate action sequences. Most vision-language-action and world-action models target one robot. Combining multiple views alone does not establish spatial correspondence between them. World Dreamer v5-lite is a multi-robot world-action model built around a shared world state for robot-specific action prediction. Calibrated features from a pretrained video encoder populate this state in workspace coordinates; its spatial size remains fixed as views are added. A vision-language model provides scene context and one...

</details>

<details>
<summary>Share</summary>

```
World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer

Multi-robot control requires integrating distributed camera views while predicting separate action sequences.

arXiv: https://arxiv.org/abs/2610.37518

#VLA #robotics
```

</details>

---

### [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](https://arxiv.org/abs/2610.36761)

**Authors:** Zihan Zhang, Zeyu Wu, Xin Zhang, Mingyu Luo, Haohui Que et al. (6 authors)

**Published:** 2026-10-27 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.36761) | [PDF](https://arxiv.org/pdf/2610.36761)

<details>
<summary>Abstract</summary>

Self-driving laboratories (SDLs) are laboratory systems that couple experimental planning, automated execution, and measurement feedback in a closed loop. Integrating flexible robot control with the typed application programming interfaces (APIs) and continuous measurements exposed by laboratory instruments remains an execution-interface challenge. To address this challenge, we propose a traceable framework comprising four components: LAM (Lab Action Model), OpenSDL, Safe-SDL, and L3-Bench. LAM is a proposed measurement-conditioned policy architecture that extends vision-language-action paradi...

</details>

<details>
<summary>Share</summary>

```
Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution

Self-driving laboratories (SDLs) are laboratory systems that couple experimental planning, automated execution, and measurement feedback in a closed loop.

arXiv: https://arxiv.org/abs/2610.36761

#VLA #robotics
```

</details>

---
