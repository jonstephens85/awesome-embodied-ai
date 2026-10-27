# What's New

Papers discovered in the run at **2026-10-27 20:26 UTC**.

**New this run:** 27

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (1)

### [EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models](https://arxiv.org/abs/2610.33685)

**Authors:** Qingyuan Cai, Bo Zhang, Yongzhen Huang, Jianyu Chen

**Published:** 2026-10-24 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.33685) | [PDF](https://arxiv.org/pdf/2610.33685)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are bottlenecked by the scarcity of robot data. Egocentric human manipulation videos offer an abundant, diverse, and semantically-rich alternative that inherently captures manipulation intent. However, the embodiment gap makes it difficult to extract action-relevant representations from these videos. From the perspective of action execution, human hands and robots share analogous manipulation primitives---reaching, grasping, placing---yet exhibit distinct kinematics tied to their embodiments. This might motivate our key approach: egocentric video pretraining...

</details>

<details>
<summary>Share</summary>

```
EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

Vision-Language-Action (VLA) models are bottlenecked by the scarcity of robot data.

arXiv: https://arxiv.org/abs/2610.33685

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (18)

### [RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions](https://arxiv.org/abs/2610.34356)

**Authors:** Haoyu Zhao, Xingyue Zhao, Zhian Su, Bohan Hou, Yinzhou Tang et al. (14 authors)

**Published:** 2026-10-25 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34356) | [PDF](https://arxiv.org/pdf/2610.34356) | [Project Page](https://alibaba-damo-academy.github.io/RynnVLA-Latent.github.io/) | [Code](https://github.com/alibaba-damo-academy/RynnVLA-Latent)

<details>
<summary>Abstract</summary>

Scaling vision-language-action (VLA) models is constrained by scarce action-labeled demonstrations and incompatible control spaces across robot embodiments. We present RynnVLA-Latent, a framework that turns heterogeneous interaction videos into scalable supervision for robot policy pretraining. At its core, RynnLAM learns continuous, 3D-grounded latent actions from visual transitions without requiring native robot controls. By combining residual future-feature prediction, camera-compensated 3D-flow supervision, and camera-motion decoupling, RynnLAM encourages representations that capture contr...

</details>

<details>
<summary>Share</summary>

```
RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

Scaling vision-language-action (VLA) models is constrained by scarce action-labeled demonstrations and incompatible control spaces across robot embodiments.

arXiv: https://arxiv.org/abs/2610.34356
Project page: https://alibaba-damo-academy.github.io/RynnVLA-Latent.github.io/
Code: https://github.com/alibaba-damo-academy/RynnVLA-Latent

#VLA #robotics
```

</details>

---

### [Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies](https://arxiv.org/abs/2610.35626)

**Authors:** Zuoxu Wang, Xiao Liang

**Published:** 2026-10-26 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.35626) | [PDF](https://arxiv.org/pdf/2610.35626) | [Project Page](https://001-wang.github.io/PrecisionReach-GS/)

<details>
<summary>Abstract</summary>

Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment. This challenge is particularly severe in electronic-waste disassembly, where robots operate in cluttered assemblies of densely packed, visually similar components. Full digital-twin simulation is difficult because many parts are thin, reflective, or mechanically complex, making accurate object-level meshes and contact models difficult to obtain. In this work, we focus on pre-contact reaching...

</details>

<details>
<summary>Share</summary>

```
Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment.

arXiv: https://arxiv.org/abs/2610.35626
Project page: https://001-wang.github.io/PrecisionReach-GS/

#VLA #robotics
```

</details>

---

### [JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.35010)

**Authors:** Wei Wang, Wenqiao Zhang, Zheqi Lv, Zheng Dong, Yingjie Niu et al. (9 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.35010) | [PDF](https://arxiv.org/pdf/2610.35010) | [Code](https://github.com/ZJU4EmbodiedAI/JevVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can select among discrete candidates for pick-and-place manipulation or generate continuous action chunks for motion control. Improving both forms of decision making through a common mechanism while retaining the capabilities of a pretrained policy is an important adaptation problem. Inspired by Jev's structured, probabilistic decision interface, we propose JevVLA, a lightweight energy-based adaptation framework for VLA policies. JevVLA instantiates this inspiration by modeling the relative quality of action proposals: with the base policy frozen, it learn...

</details>

<details>
<summary>Share</summary>

```
JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies

Vision-language-action (VLA) policies can select among discrete candidates for pick-and-place manipulation or generate continuous action chunks for motion control.

arXiv: https://arxiv.org/abs/2610.35010
Code: https://github.com/ZJU4EmbodiedAI/JevVLA

#VLA #robotics
```

</details>

---

### [AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2610.33074)

**Authors:** Xuhong Qiu, Zhuoyu Wu, Qiawei Zheng, Wenhui Ou, Wenqi Fang et al. (6 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33074) | [PDF](https://arxiv.org/pdf/2610.33074) | [Code](https://github.com/Qiuxu00/AGQ)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to perform tasks specified through natural-language instructions, but their large weight footprint challenges deployment on memory-constrained onboard platforms. Ultra-low-bit quantization reduces this footprint, yet preserving task performance and controlling weight recovery costs remain challenging. We propose Action-Guided Quantization, which combines action sensitivity with a measured proxy for weight recovery cost to allocate matrix bitwidths under storage budgets. Per-channel calibration compensates for quantization error, while a uniform...

</details>

<details>
<summary>Share</summary>

```
AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models

Vision-language-action (VLA) models enable robots to perform tasks specified through natural-language instructions, but their large weight footprint challenges deployment on memory-constrained onboard platforms.

arXiv: https://arxiv.org/abs/2610.33074
Code: https://github.com/Qiuxu00/AGQ

#VLA #robotics
```

</details>

---

### [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832)

**Authors:** Yifei Yao, Yude Zou, Guanbo Jiao, Xing Gao, Ning Gao et al. (15 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.35832) | [PDF](https://arxiv.org/pdf/2610.35832) | [Project Page](https://internrobotics.github.io/EBench-Astra-Tech-Report/)

<details>
<summary>Abstract</summary>

Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be thoroughly evaluated. In this report, we evaluate GPT-6-Astra on EBench as the core of an agent that controls a robot through an agent harness under the same visual and proprioceptive observation protocol as post-trained policies. We study two agent configurations: direct control, in which the agent generates waypoint com...

</details>

<details>
<summary>Share</summary>

```
Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy

Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action mod...

arXiv: https://arxiv.org/abs/2610.35832
Project page: https://internrobotics.github.io/EBench-Astra-Tech-Report/

#VLA #robotics
```

</details>

---

### [RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)

**Authors:** Lingjun Mao, Jinglin Cao, Lukun He, Wenpeng Xu, Yuchen Yan et al. (25 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34649) | [PDF](https://arxiv.org/pdf/2610.34649) | [Project Page](https://aetherlabsai.github.io/RobotAgentBench/)

<details>
<summary>Abstract</summary>

Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing to capture the complexity of open-world robot autonomy. We introduce RobotAgentBench (RAB), a compre...

</details>

<details>
<summary>Share</summary>

```
RobotAgentBench: Towards Open-world Robot Autonomy

Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executi...

arXiv: https://arxiv.org/abs/2610.34649
Project page: https://aetherlabsai.github.io/RobotAgentBench/

#VLA #robotics
```

</details>

---

### [HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience](https://arxiv.org/abs/2610.34186)

**Authors:** Yang Liu, Jiacheng Liu, Hengtao Li, Yuheng Huang, Zijian Yang et al. (17 authors)

**Published:** 2026-10-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.34186) | [PDF](https://arxiv.org/pdf/2610.34186)

<details>
<summary>Abstract</summary>

Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios. Although egocentric human demonstrations provide a complementary source of task experience, differences in visual embodiment and missing robot proprioception complicate transfer to humanoid policies. To address these challenges, we introduce HuGe, a family of Humanoid Generalist VLAs pre-trained on over 2,000 hours of egocentric human and robot data. Specifically, HuGe employs three existing representative VLA a...

</details>

<details>
<summary>Share</summary>

```
HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios.

arXiv: https://arxiv.org/abs/2610.34186

#VLA #robotics
```

</details>

---

### [RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models](https://arxiv.org/abs/2610.34108)

**Authors:** Jie Wang, Bo Zhang, Renzhi Lu, Jianyu Chen

**Published:** 2026-10-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34108) | [PDF](https://arxiv.org/pdf/2610.34108)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map a language instruction and the current observation directly to actions, without checking whether the instruction has been completed. For long-horizon tasks, a single failed step therefore goes unnoticed and leaves the whole task unfinished. Such failed episodes, however, often end with the task partially complete. Moreover, the unfinished steps are reusable atomic skills that recur across demonstrations. A failed attempt can thus be recovered by composing with atomic skills. We propose RoboDuo, a closed-loop dual-system framework that uses code as the in...

</details>

<details>
<summary>Share</summary>

```
RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models

Vision-Language-Action (VLA) models map a language instruction and the current observation directly to actions, without checking whether the instruction has been completed.

arXiv: https://arxiv.org/abs/2610.34108

#VLA #robotics
```

</details>

---

### [Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models](https://arxiv.org/abs/2610.34251)

**Authors:** Xinyu Liu, Daiying Tian, Chenwei Tang, Ruyang Han, Chengyang Zhang et al. (9 authors)

**Published:** 2026-10-25 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34251) | [PDF](https://arxiv.org/pdf/2610.34251)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling. Existing methods either rely on implicit temporal representations within policy networks, where historical information can be gradually diluted, or maintain explicit memory buffers that suffer from redundancy, noise accumulation, and inefficient retrieval. In this paper, we propose CogMemory, a novel variational cognitive memory framework that enables VLA systems to selectively preserve and reuse t...

</details>

<details>
<summary>Share</summary>

```
Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models

Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling.

arXiv: https://arxiv.org/abs/2610.34251

#VLA #robotics
```

</details>

---

### [VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717)

**Authors:** Borui Xu, Hongshi Tan, Wenqi Jiang, Bingsheng He, Ming Wu et al. (7 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34717) | [PDF](https://arxiv.org/pdf/2610.34717)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) models increasingly run on edge devices aboard robots, where inference latency constrains closed-loop robot control. However, it remains unclear how to design VLA models, their inference software and edge hardware so that robots can run VLA inference in real time. Most VLA models report only task success, while prior studies cover limited action-generation strategies, divide inference into at most three stages, and lack comparisons of inference optimizations on the same models.benchmarking 18 open VLA models across released and alternative backends on NVIDIA Jets...

</details>

<details>
<summary>Share</summary>

```
VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware

Vision--language--action (VLA) models increasingly run on edge devices aboard robots, where inference latency constrains closed-loop robot control.

arXiv: https://arxiv.org/abs/2610.34717

#VLA #robotics
```

</details>

---

### [TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning](https://arxiv.org/abs/2610.34519)

**Authors:** Sooyoung Kwon, Carlee Joe-Wong, Kyunghan Lee

**Published:** 2026-10-25 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34519) | [PDF](https://arxiv.org/pdf/2610.34519)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are increasingly used for robot manipulation because they map camera images and a language instruction directly to actions. Robots that cannot be tethered to a workstation, such as mobile manipulators and humanoids, must run them on onboard embedded boards, where the prefill latency of the language backbone grows with the hundreds of visual tokens processed at every control step. To meet real-time limits, training-free accelerators recompute only a subset of the visual tokens and skip the rest, either by pruning them or by reusing their cached key-value (KV)...

</details>

<details>
<summary>Share</summary>

```
TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning

Vision-language-action (VLA) models are increasingly used for robot manipulation because they map camera images and a language instruction directly to actions.

arXiv: https://arxiv.org/abs/2610.34519

#VLA #robotics
```

</details>

---

### [Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics](https://arxiv.org/abs/2610.34051)

**Authors:** Sirui Chen, Huang Huang, Qineng Wang, Wenlong Huang, Manling Li et al. (8 authors)

**Published:** 2026-10-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34051) | [PDF](https://arxiv.org/pdf/2610.34051) | [Project Page](https://arielchen07.github.io/behavior-spatial/)

<details>
<summary>Abstract</summary>

Robot tasks require grounding spatial language in physical scenes, but task success alone cannot establish whether spatial instructions are followed. We present BEHAVIOR-Spatial, a benchmark built on BEHAVIOR-1K that measures spatial question answering, point-based target grounding, and robot action to examine how VLM spatial understanding relates to VLA behavior. It comprises 3,256 spatial questions across 49 activities, 1,240 grounding queries across 14 manipulation tasks, and action evaluations covering those 14 tasks and 10 navigation tasks. Our manipulation protocol evaluates held-out con...

</details>

<details>
<summary>Share</summary>

```
Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics

Robot tasks require grounding spatial language in physical scenes, but task success alone cannot establish whether spatial instructions are followed.

arXiv: https://arxiv.org/abs/2610.34051
Project page: https://arielchen07.github.io/behavior-spatial/

#VLA #robotics
```

</details>

---

### [Beyond Behaviour: A Stimulus-Response Safety Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2610.34837)

**Authors:** Vy Vo, Dinh Phung

**Published:** 2026-10-26 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34837) | [PDF](https://arxiv.org/pdf/2610.34837)

<details>
<summary>Abstract</summary>

Humans exhibit biological sensitivity to safety-critical stimuli that can trigger defensive action. Across three models and two video benchmarks, we investigate whether similar responses emerge in vision-language-action models by examining their internal representations and action tendencies in response to visible hazards and harmful consequences. Our findings suggest that task execution may remain the default response even when danger is internally registered.

</details>

<details>
<summary>Share</summary>

```
Beyond Behaviour: A Stimulus-Response Safety Evaluation of Vision-Language-Action Models

Humans exhibit biological sensitivity to safety-critical stimuli that can trigger defensive action.

arXiv: https://arxiv.org/abs/2610.34837

#VLA #robotics
```

</details>

---

### [Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)

**Authors:** Hyunwoong Bae, Jisu Han, Jiyeon Choi, Dohoon Kim, Taesup Moon

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34674) | [PDF](https://arxiv.org/pdf/2610.34674)

<details>
<summary>Abstract</summary>

Safe household navigation requires robots to regulate clearance and speed according to what an obstacle is and how close it is, without unnecessary conservatism. Yet existing evaluations do not test whether semantic safety distinctions are reflected in continuous motion. To that end, we introduce OSMA-Bench, an Obstacle-Conditioned Safe Motion Adaptation Benchmark built on spatially matched scenario sets that differ only in obstacle type. We also propose the \emph{Semantic Sensitivity Index} (SSI), which measures whether clearance and distance-dependent speed and smoothness follow the caution...

</details>

<details>
<summary>Share</summary>

```
Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation

Safe household navigation requires robots to regulate clearance and speed according to what an obstacle is and how close it is, without unnecessary conservatism.

arXiv: https://arxiv.org/abs/2610.34674

#VLA #robotics
```

</details>

---

### [Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference](https://arxiv.org/abs/2610.33658)

**Authors:** Rui Liu, He Lv, Ziyao Zhang, Rui Ma, Rongxiang Nie

**Published:** 2026-10-24 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.33658) | [PDF](https://arxiv.org/pdf/2610.33658)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on dense, continuous-valued computation presents a fundamental challenge for energy-constrained deployment. Inspired by the sparse, event-driven signaling and temporal integration mechanisms of biological neurons, a promising alternative is to introduce spiking computation into VLA models. However, enabling such computation without restructuring pretrained policies or compromising closed-loop control remains an open challenge. To address this challenge, we introduce the Power-o...

</details>

<details>
<summary>Share</summary>

```
Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference

Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on dense, continuous-valued computation presents a fundamental challenge for energy-constrained dep...

arXiv: https://arxiv.org/abs/2610.33658

#VLA #robotics
```

</details>

---

### [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817)

**Authors:** Benjamin Pikus, Daniel Saunders, Mircea Mironenco, Salman Mohammadi, Mathew Mathew et al. (14 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.35817) | [PDF](https://arxiv.org/pdf/2610.35817)

<details>
<summary>Abstract</summary>

A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot via a simple tool harness. We use a pretrained 27B parameter model to bootstrap world understanding and reasoning, followed by supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move the robot. Without any real-world robot data during training, ZAP reaches 96.7% success on real-world tasks, m...

</details>

<details>
<summary>Share</summary>

```
Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent

A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task.

arXiv: https://arxiv.org/abs/2610.35817

#VLA #robotics
```

</details>

---

### [Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](https://arxiv.org/abs/2610.35252)

**Authors:** Shitong Liu, Jingwei Zhang, Sheng Lian, Xinyu Zhuang, Kaiwen Guo et al. (20 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.35252) | [PDF](https://arxiv.org/pdf/2610.35252)

<details>
<summary>Abstract</summary>

Realizing Embodied AI for Science requires robots to translate experimental goals into reliable physical procedures, reducing hazardous and repetitive human work while generating evidence for scientific discovery. Although language-based planning and learned manipulation provide complementary capabilities, their integration requires robots to adapt subsequent operations to actual execution outcomes. For example, an unsuccessful placement changes what must be done next, even when the experimental goal remains unchanged. Existing benchmarks assess planning, manipulation, and laboratory workflows...

</details>

<details>
<summary>Share</summary>

```
Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories

Realizing Embodied AI for Science requires robots to translate experimental goals into reliable physical procedures, reducing hazardous and repetitive human work while generating evidence for scientific discovery.

arXiv: https://arxiv.org/abs/2610.35252

#VLA #robotics
```

</details>

---

### [One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation](https://arxiv.org/abs/2610.33794)

**Authors:** Zhuoyuan Yu, Yuxing Long, Du Wang, Junyang Wang, Hongwei Fan et al. (6 authors)

**Published:** 2026-10-24 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.33794) | [PDF](https://arxiv.org/pdf/2610.33794)

<details>
<summary>Abstract</summary>

Deploying a language-guided navigation policy in a new building usually means watching it fail. Public-benchmark VLAs degrade scene by scene as layout, appearance, and language drift, and the standard fix of teleoperating fresh trajectories on site does not scale. We replace human demonstration with a single brief iPhone scan. Scan2Instruction compiles that scan into a complete training environment, automatically synthesizing executable navigation episodes with grounded instructions. PRPT-KS then adapts the policy through a closed-form Pareto utility read directly off the reconstructed scene,...

</details>

<details>
<summary>Share</summary>

```
One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation

Deploying a language-guided navigation policy in a new building usually means watching it fail.

arXiv: https://arxiv.org/abs/2610.33794

#VLA #robotics
```

</details>

---

## World Models (8)

### [Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663)

**Authors:** Mattia Scardecchia, Sherry Yang

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34663) | [PDF](https://arxiv.org/pdf/2610.34663) | [Code](https://github.com/mattia-scardecchia/predictable-latents)

<details>
<summary>Abstract</summary>

Video world models trained on large-scale robot data promise a safe and scalable approach for learning and evaluating policies that act in the physical world. However, they still struggle with long-horizon rollouts and out-of-distribution generalization, and they remain computationally demanding at inference time. Typically, video world models make predictions in the latent space of a reconstruction-trained autoencoder, which however is not directly optimized for dynamics modeling. On the other hand, world models designed for latent planning usually optimize latents to be predictable, but they...

</details>

<details>
<summary>Share</summary>

```
Video World Models Need Predictable Latents

Video world models trained on large-scale robot data promise a safe and scalable approach for learning and evaluating policies that act in the physical world.

arXiv: https://arxiv.org/abs/2610.34663
Code: https://github.com/mattia-scardecchia/predictable-latents

#worldmodels #robotics
```

</details>

---

### [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564)

**Authors:** Meryem Koksal, Yunzhe Wang, Volkan Ustun

**Published:** 2026-10-25 | **Categories:** cs.CV, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.34564) | [PDF](https://arxiv.org/pdf/2610.34564)

<details>
<summary>Abstract</summary>

Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents. We introduce FlockWorld, an artificial-life environment built on Reynolds's Boids algorithm for studying population-scale multi-agent video world models. Specifically, FlockWorld renders synchronized egocentric crops, assigns distinct colors to preserve camera-agent identity across views, exposes rule-derived accelerations as actions, and lets the number of camera agents be configured independently of the size of the surrounding population....

</details>

<details>
<summary>Share</summary>

```
FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation

Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents.

arXiv: https://arxiv.org/abs/2610.34564

#worldmodels #robotics
```

</details>

---

### [Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation](https://arxiv.org/abs/2610.35636)

**Authors:** Akshay Mete, Dileep Kalathil, P. R. Kumar

**Published:** 2026-10-26 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.35636) | [PDF](https://arxiv.org/pdf/2610.35636)

<details>
<summary>Abstract</summary>

Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift. Test-time adaptation (TTA) can mitigate this degradation by updating the model during deployment. Unlike pre-training on fixed data, TTA for planning is closed-loop: the planner uses model rollouts to select actions, and the resulting transitions drive the next update. This raises the question: which objective should guide TTA for planning? Under a prediction-only objective, the model is fit only to the outcomes of its own actions, so it can remain wro...

</details>

<details>
<summary>Share</summary>

```
Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation

Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift.

arXiv: https://arxiv.org/abs/2610.35636

#worldmodels #robotics
```

</details>

---

### [WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU](https://arxiv.org/abs/2610.35529)

**Authors:** Bingnan Liu, Ruini Xue

**Published:** 2026-10-26 | **Categories:** cs.DC, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.35529) | [PDF](https://arxiv.org/pdf/2610.35529)

<details>
<summary>Abstract</summary>

Interactive world models keep the KV of past chunks as retrieval memory so that revisited places stay consistent. On a single consumer machine (one RTX 4090, 32 GiB of host memory, one NVMe SSD), long sessions with such memory hit two walls. The first is capacity: the KV of Matrix-Game 2.0 exhausts host memory after 45 seconds of video in bf16 and after 2.8 minutes in int4. The second is the model's positional horizon of 4.3 minutes. We show that this memory is capacity-bound rather than bandwidth-bound and that its access set is known before compute, because the camera pose is an input. An an...

</details>

<details>
<summary>Share</summary>

```
WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU

Interactive world models keep the KV of past chunks as retrieval memory so that revisited places stay consistent.

arXiv: https://arxiv.org/abs/2610.35529

#worldmodels #robotics
```

</details>

---

### [TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting](https://arxiv.org/abs/2610.34797)

**Authors:** Hang Ni, Weijia Zhang, Hao Liu

**Published:** 2026-10-26 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34797) | [PDF](https://arxiv.org/pdf/2610.34797)

<details>
<summary>Abstract</summary>

Time series forecasting supports decision-making in web applications such as online retail and network management, where planned actions can reshape future dynamics. World models provide a natural paradigm for predicting such action-dependent changes beyond extrapolating historical patterns. However, existing time series world models (TSWMs) typically rely on fixed, domain-specific covariate schemas that limit flexible intervention specification, while multimodal forecasters treat text primarily as passive predictive context. To investigate these gaps, we introduce TSWM-Bench, a cross-domain b...

</details>

<details>
<summary>Share</summary>

```
TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting

Time series forecasting supports decision-making in web applications such as online retail and network management, where planned actions can reshape future dynamics.

arXiv: https://arxiv.org/abs/2610.34797

#worldmodels #robotics
```

</details>

---

### [How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3](https://arxiv.org/abs/2610.34523)

**Authors:** Shuzhi Liu, Archana Warrier, Dat Nguyen, Chengqi Zheng, Kevin Ellis et al. (6 authors)

**Published:** 2026-10-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.34523) | [PDF](https://arxiv.org/pdf/2610.34523) | [Project Page](https://arc3-human-think-aloud.github.io/](https://arc3-human-think-aloud.github.io/)

<details>
<summary>Abstract</summary>

Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence. Understanding these capabilities requires tracing how learners build, use, and revise world models during interaction. We construct the first dataset that records how humans discover and use the mechanisms of novel environments, using ARC-AGI-3 as a testbed: 144 trajectories from 64 participants across 25 public games, each pairing time-synchronized actions with think-aloud audio, plus 250 trajectories from large language model (LLM) agents with and without harness...

</details>

<details>
<summary>Share</summary>

```
How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3

Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence.

arXiv: https://arxiv.org/abs/2610.34523
Project page: https://arc3-human-think-aloud.github.io/](https://arc3-human-think-aloud.github.io/

#worldmodels #robotics
```

</details>

---

### [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](https://arxiv.org/abs/2610.34650)

**Authors:** Jonathan DeCastro, Thomas Balch, Emily Sumner, Deepak Gopinath, Laporsha Dees et al. (12 authors)

**Published:** 2026-10-26 | **Categories:** cs.RO, cs.HC, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.34650) | [PDF](https://arxiv.org/pdf/2610.34650)

<details>
<summary>Abstract</summary>

Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time. We present Dream2Assist, a model-based reinforcement learning framework for tightly-coupled shared decision making that addresses both sides of this challenge. Our approach extends a recurrent state-space world model with intent inference, enabling an assistive policy trained via fictitious co-play to anticipate and support discrete human objectives without overriding human agency...

</details>

<details>
<summary>Share</summary>

```
Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control

Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time.

arXiv: https://arxiv.org/abs/2610.34650

#worldmodels #robotics
```

</details>

---

### [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044)

**Authors:** Jingbo Xu, Hanchao Leng, JiaHui Huang, Hanbing Li, Jingwei Zhao et al. (10 authors)

**Published:** 2026-10-26 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.35044) | [PDF](https://arxiv.org/pdf/2610.35044)

<details>
<summary>Abstract</summary>

World models are emerging as a fundamental component of policy learning for real-world agents, enabling agents to predict future world states and plan actions within a learned representation of the dynamic environment. Existing approaches, however, often model appearance, metric geometry represented by projected LiDAR depth, and ego motion either partially or independently, overlooking the fact that these modalities are different projections of a shared underlying world state. This separation can lead to information loss and cross-modal inconsistency, ultimately limiting downstream performance...

</details>

<details>
<summary>Share</summary>

```
DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models

World models are emerging as a fundamental component of policy learning for real-world agents, enabling agents to predict future world states and plan actions within a learned representation of the dynamic environment.

arXiv: https://arxiv.org/abs/2610.35044

#worldmodels #robotics
```

</details>

---
