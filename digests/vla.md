# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-07 19:54 UTC

**Papers shown:** 59 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing](https://arxiv.org/abs/2611.08425)

**Authors:** Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva et al. (9 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08425) | [PDF](https://arxiv.org/pdf/2611.08425) | [Project Page](https://vla-tug.github.io)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people. Deploying VLAs in real-world systems therefore requires a runtime monitor that is timely, calibrated, and informative while being efficient enough to run on the edge. Existing methods fail to fulfill these requirements. We present VLA-Tug, a lightweight probe over the latent layers of a VLA backbone that improves early failure detection and bounds the missed-detection and false-alarm r...

</details>

<details>
<summary>Share</summary>

```
Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people.

arXiv: https://arxiv.org/abs/2611.08425
Project page: https://vla-tug.github.io

#VLA #robotics
```

</details>

---

### [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373)

**Authors:** Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08373) | [PDF](https://arxiv.org/pdf/2611.08373) | [Project Page](https://SLA.github.io/) | [Code](https://github.com/OpenHelix-Team/Spatial-Forcing)

<details>
<summary>Abstract</summary>

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it durin...

</details>

<details>
<summary>Share</summary>

```
SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space.

arXiv: https://arxiv.org/abs/2611.08373
Project page: https://SLA.github.io/
Code: https://github.com/OpenHelix-Team/Spatial-Forcing

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

### [From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)

**Authors:** Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang et al. (17 authors)

**Published:** 2026-11-04 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06918) | [PDF](https://arxiv.org/pdf/2611.06918) | [Code](https://github.com/EvolvingLMMs-Lab/NEO)

<details>
<summary>Abstract</summary>

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch c...

</details>

<details>
<summary>Share</summary>

```
From Pixels to Actions - Towards Native Vision-Language-Action Policies

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards.

arXiv: https://arxiv.org/abs/2611.06918
Code: https://github.com/EvolvingLMMs-Lab/NEO

#VLA #robotics
```

</details>

---

### [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)

**Authors:** Chengcheng Wang, Wei He, Wenhao Li, Hongguang Li, Kai Han et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07513) | [PDF](https://arxiv.org/pdf/2611.07513) | [Code](https://github.com/lose4578/Concertina)

<details>
<summary>Abstract</summary>

Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the same model, shifting from a decoupled VLA to an Embodied Vision-Language Model (eVLM). We introduce C...

</details>

<details>
<summary>Share</summary>

```
Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model

Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors b...

arXiv: https://arxiv.org/abs/2611.07513
Code: https://github.com/lose4578/Concertina

#VLA #robotics
```

</details>

---

### [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156)

**Authors:** Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08156) | [PDF](https://arxiv.org/pdf/2611.08156) | [Code](https://github.com/mt-clemente/lajepa)

<details>
<summary>Abstract</summary>

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Latent Action JEPA (La-JEPA), a compact world-action model whose policy transformer is trained from scratch in the feature space of a pretrained V-JEPA 2.1 encoder. Following Fast-WAM, La-JEPA learns to predict future features jointly with acti...

</details>

<details>
<summary>Share</summary>

```
La-JEPA: Compact Robot Policies with Latent World Modeling

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed fo...

arXiv: https://arxiv.org/abs/2611.08156
Code: https://github.com/mt-clemente/lajepa

#VLA #robotics
```

</details>

---

### [RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)

**Authors:** Deng-Ke Wu, Yifan Jin, Yida Yang, Lei Qian, Zhaoye Zhou et al. (11 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03850) | [PDF](https://arxiv.org/pdf/2611.03850) | [Project Page](https://roboscope.pages.dev/) | [Code](https://github.com/MINT-SJTU/RoboScope-Kit)

<details>
<summary>Abstract</summary>

Simulation benchmarks are the standard way to compare robot policies, but each benchmark brings its own evaluator, observation layout, and action convention, and evaluation is slow: 500 RoboTwin Easy episodes with one simulator and one model on one GPU take 359.7 minutes. Profiling the official StarVLA evaluator shows that simulation occupies CPU cores while the GPU averages 14.3% utilization. RoboScope Kit wraps each model once in a Python class called a Policy, and each benchmark once in an adapter around the benchmark's own evaluator, so the benchmark's rules and scoring stay unchanged. Sch...

</details>

<details>
<summary>Share</summary>

```
RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation

Simulation benchmarks are the standard way to compare robot policies, but each benchmark brings its own evaluator, observation layout, and action convention, and evaluation is slow: 500 RoboTwin Easy episodes with one...

arXiv: https://arxiv.org/abs/2611.03850
Project page: https://roboscope.pages.dev/
Code: https://github.com/MINT-SJTU/RoboScope-Kit

#VLA #robotics
```

</details>

---

### [VLALagBench: Understanding When and Why VLA Inference Latency Matters](https://arxiv.org/abs/2611.03103)

**Authors:** Qi Wen, Borui Xu, Hussein Amro, Hongshi Tan, Hanmin Lin et al. (14 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

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

### [Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)

**Authors:** Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04391) | [PDF](https://arxiv.org/pdf/2611.04391) | [Project Page](https://junhyeong-park.me/h2rb/)

<details>
<summary>Abstract</summary>

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB b...

</details>

<details>
<summary>Share</summary>

```
Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations.

arXiv: https://arxiv.org/abs/2611.04391
Project page: https://junhyeong-park.me/h2rb/

#VLA #robotics
```

</details>

---

### [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](https://arxiv.org/abs/2611.08462)

**Authors:** Arpit Bahety, Skand Peri, Sriniket Ambatipudi, Chen Xu, Haruki Nishimura et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.08462) | [PDF](https://arxiv.org/pdf/2611.08462)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment. Teaching them to recover from these failures requires substantial corrective data: existing approaches learn to recover from failures by directly associating corrective actions with the observations in which they were demonstrated. For instance, DAgger-like fine-tuning can require tens to hundreds of interactions, yet the resulting policy may still fail to generalize the learned corrections beyond the demonstrated scenarios. We hypothesize that semantics can capture the...

</details>

<details>
<summary>Share</summary>

```
OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions

Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment.

arXiv: https://arxiv.org/abs/2611.08462

#VLA #robotics
```

</details>

---

### [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](https://arxiv.org/abs/2611.08413)

**Authors:** Mohammed Hassan, Zhenyang Chen, Zheng Wang, Zhixin Zhu, Tianlong Chen et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.08413) | [PDF](https://arxiv.org/pdf/2611.08413)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem from two complementary forms of redundancy: many visual tokens are spatially irrelevant, while attention over the remaining tokens is often misallocated. Based on this observation, we propose T3R, a Training-Free Two-Stage Token Refinement...

</details>

<details>
<summary>Share</summary>

```
T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive.

arXiv: https://arxiv.org/abs/2611.08413

#VLA #robotics
```

</details>

---

### [AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction](https://arxiv.org/abs/2611.07712)

**Authors:** Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Yara Mahmoud, Iana Zhura et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.07712) | [PDF](https://arxiv.org/pdf/2611.07712)

<details>
<summary>Abstract</summary>

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction intent from two onboard cameras and converts it into a language prompt for the VLA policy. Low-confidence predictions suppress motion execution, reducing unintended activations. During physical contact, interaction-specific compl...

</details>

<details>
<summary>Share</summary>

```
AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact.

arXiv: https://arxiv.org/abs/2611.07712

#VLA #robotics
```

</details>

---

### [$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](https://arxiv.org/abs/2611.06447)

**Authors:** Shengzhe Zhang, Qi Zhang, Dazhong Shen, Chao Wang, Shaopeng Zhai et al. (6 authors)

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.06447) | [PDF](https://arxiv.org/pdf/2611.06447)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions. However, the action prediction objective itself lacks fine-grained task-specific perceptual supervision, making it prone to relying on task-irrelevant visual shortcuts, leading attention away from target objects and key interaction areas, thereby limiting its operational performance and generalization ability. To address this, we propose Automatic Perception-Guided Attention Alignment for Robot Manipulation ($A^3$...

</details>

<details>
<summary>Share</summary>

```
$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation

Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.06447

#VLA #robotics
```

</details>

---

### [Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning](https://arxiv.org/abs/2611.05667)

**Authors:** Xinkai Jiang, Jing Jiang, Hongyi Zhou, Pankhuri Vanjani, Ahmad Baki et al. (10 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05667) | [PDF](https://arxiv.org/pdf/2611.05667) | [Project Page](https://intuitive-robots.github.io/PHIL-page/)

<details>
<summary>Abstract</summary>

This paper presents Proactive Human-in-the-Loop (PHIL), a framework for proactive policy correction and preference-based post-training. PHIL enables operators to preview policy-predicted future motion and intervene before anticipated undesirable actions. During takeover, PHIL continues querying the policy and displaying its predicted trajectories in the physical workspace through an extended reality (XR) interface. PHIL pairs rejected policy predictions with corrective action chunks subsequently executed from the same physical state over the same horizon, and preference-based post-training enc...

</details>

<details>
<summary>Share</summary>

```
Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning

This paper presents Proactive Human-in-the-Loop (PHIL), a framework for proactive policy correction and preference-based post-training.

arXiv: https://arxiv.org/abs/2611.05667
Project page: https://intuitive-robots.github.io/PHIL-page/

#VLA #robotics
```

</details>

---

### [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)

**Authors:** Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05372) | [PDF](https://arxiv.org/pdf/2611.05372) | [Code](https://github.com/Tinaliu0123/PolicyIK)

<details>
<summary>Abstract</summary>

Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depends on hand-tuned controllers, and training data on physical robots are costly to collect. We present PolicyIK, a goal-conditioned reinforcement learning policy for high-precision IK. It updates joint-position references from pose feedback and observes its accumulated reference relative to the measu...

</details>

<details>
<summary>Share</summary>

```
PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning

Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments.

arXiv: https://arxiv.org/abs/2611.05372
Code: https://github.com/Tinaliu0123/PolicyIK

#VLA #robotics
```

</details>

---

### [LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models](https://arxiv.org/abs/2611.05093)

**Authors:** Syed Umer Bukhari, Magnus Almgren, Ahmed Ali-Eldin

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.05093) | [PDF](https://arxiv.org/pdf/2611.05093)

<details>
<summary>Abstract</summary>

Post-training quantization (PTQ) for vision-language-action (VLA) models promises smaller and faster VLA deployments. However, when analyzing existing VLA quantization works, we realised that it is hard to reason about the performance of the suggested quantization method compared to existing, similar, or in many cases, simpler PTQ methods. We present LoopQ, a closed-loop benchmark that compares multiple quantization policies on the same checkpoint, layers and engine, varying only the method and the kernels. We evaluate RTN, AWQ, GPTQ, ActQuant and QuantVLA on four VLAs with more than 180,000 e...

</details>

<details>
<summary>Share</summary>

```
LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models

Post-training quantization (PTQ) for vision-language-action (VLA) models promises smaller and faster VLA deployments.

arXiv: https://arxiv.org/abs/2611.05093

#VLA #robotics
```

</details>

---

### [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)

**Authors:** Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng, Tsung-Wei Ke

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05080) | [PDF](https://arxiv.org/pdf/2611.05080) | [Project Page](https://embodiedai-ntu.github.io/cronos/)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments. However, standard RL pipelines rely on episodic training with frequent scene resets, which is impractical for real-world deployment due to the need for substantial human intervention. While prior work has studied non-episodic RL in relatively small policies trained from scratch, its behavior when fine-tuning modern large-scale pre-trained vision-language-action (VLA) models remains underexplored. In this work, we introduce CRONOS, a simulation benchmark for RL fine-tuning of VLAs under...

</details>

<details>
<summary>Share</summary>

```
CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments.

arXiv: https://arxiv.org/abs/2611.05080
Project page: https://embodiedai-ntu.github.io/cronos/

#VLA #robotics
```

</details>

---

### [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392)

**Authors:** Yeonseok Lee

**Published:** 2026-11-03 | **Categories:** cs.LO, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04392) | [PDF](https://arxiv.org/pdf/2611.04392) | [Code](https://github.com/ylee-sling/Aero-VPA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by streaming billions of parameters from memory. We present Aero-VPA, a lightweight Vision-Predictor-Action architecture for 3D navigation on edge hardware. A compact RGB-D Vision Transformer and a five-head ensemble predictor, trained without pixel reconstruction, forecast the next latent state; a Conditional Flow Matching solver generates a velocity and yaw-rate chunk in two Euler ste...

</details>

<details>
<summary>Share</summary>

```
Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware

Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by str...

arXiv: https://arxiv.org/abs/2611.04392
Code: https://github.com/ylee-sling/Aero-VPA

#VLA #robotics
```

</details>

---

### [FineCraft: Enhancing VLA Models for Fine-Grained Manipulation](https://arxiv.org/abs/2611.03163)

**Authors:** Shuaike Zhang, Ziheng Quan, Junhao Ran, Muhe Ding, Shaokun Wang et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

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

### [AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)

**Authors:** Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa, Jason Wang et al. (20 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03815) | [PDF](https://arxiv.org/pdf/2611.03815) | [Project Page](https://a-0.airoa.io)

<details>
<summary>Abstract</summary>

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a...

</details>

<details>
<summary>Share</summary>

```
AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage.

arXiv: https://arxiv.org/abs/2611.03815
Project page: https://a-0.airoa.io

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

### [MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic](https://arxiv.org/abs/2611.06007)

**Authors:** Varun A. Paturkar, Shankar Gangisetty, C. V. Jawahar

**Published:** 2026-11-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06007) | [PDF](https://arxiv.org/pdf/2611.06007) | [Code](https://github.com/VarunIIITH/MotoVerse)

<details>
<summary>Abstract</summary>

Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS. We introduce MotoVerse, a benchmark for predictive perception from an MTW's ego-centric perspective. MotoVerse comprises 949 maneuver clips collected in dense, unstructured traffic and trajectory annotations for over 31,000 surrounding road agents, including over 16,000 MTWs, enabling two complementary tasks: Ego-Rider Maneuver Anticipation (ERMA) and Traffic Agent Trajectory Prediction (TATP). Each clip is f...

</details>

<details>
<summary>Share</summary>

```
MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic

Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS.

arXiv: https://arxiv.org/abs/2611.06007
Code: https://github.com/VarunIIITH/MotoVerse

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

### [Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs](https://arxiv.org/abs/2611.06710)

**Authors:** Muhammad Danish Waseem, Ahmed Ali-Eldin Hassan

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.06710) | [PDF](https://arxiv.org/pdf/2611.06710)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models map camera observations and language instructions to robot actions. However, their large backbones and repeated action generation can make inference take longer than the robot's real-time requirements for its next action. To reduce the load of VLA computations, researchers have proposed multiple optimization approaches, including quantization and pruning. These optimizations can be combined with other general optimizations such as better kernel compilation or using CUDA graphs instead of the eager mode. However, most of these optimization results are usually...

</details>

<details>
<summary>Share</summary>

```
Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs

Vision-language-action (VLA) models map camera observations and language instructions to robot actions.

arXiv: https://arxiv.org/abs/2611.06710

#VLA #robotics
```

</details>

---

### [Can Astra Solve RoboMME without Breaking the Bank?](https://arxiv.org/abs/2611.06184)

**Authors:** Bingao Chen, Haoquan Fang, C. Karen Liu

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06184) | [PDF](https://arxiv.org/pdf/2611.06184) | [Project Page](https://bingaochen.github.io/Astra-on-RoboMME/)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence. A large vision-language planner can read this history, but calling it before every action chunk is slow and costly. We present a three-tier system for the RoboMME benchmark. GPT-6 Astra (System 2) selects a grounded subtask from stored visual history, a $π_{0.5}$ vision-language-action policy (System 1) executes it, and a fine-tuned Qwen3-VL-4B monitor (System 1.5) checks after each action chunk whether the subtask...

</details>

<details>
<summary>Share</summary>

```
Can Astra Solve RoboMME without Breaking the Bank?

Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence.

arXiv: https://arxiv.org/abs/2611.06184
Project page: https://bingaochen.github.io/Astra-on-RoboMME/

#VLA #robotics
```

</details>

---

### [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567)

**Authors:** Albert Wilcox, Frank Chang, Nhi Nguyen, Aishani Chakraborty, Jeremy A. Collins et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05567) | [PDF](https://arxiv.org/pdf/2611.05567) | [Project Page](https://pairlab.github.io/MESA)

<details>
<summary>Abstract</summary>

Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of controlled experimentation, or require training on large, messy open-source datasets. We introduce MESA, an evaluation framework designed for precise, reproducible measurement of language-conditioned policy generalization. MESA provides five evaluation suites that isolate in-distribution performance and four distinct axes...

</details>

<details>
<summary>Share</summary>

```
MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics

Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive.

arXiv: https://arxiv.org/abs/2611.05567
Project page: https://pairlab.github.io/MESA

#VLA #robotics
```

</details>

---

### [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](https://arxiv.org/abs/2611.05249)

**Authors:** Asher James Hancock, Boyi Li, Yuxiao Chen, Shuhan Tan, Wenhao Ding et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.05249) | [PDF](https://arxiv.org/pdf/2611.05249)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations. Those representations must carry information useful for control, yet the VLM was never trained for the action expert's flow-matching objective. Two signals can address this: gradients backpropagated from the expert's loss (coupling), or VLM supervision to predict discrete tokens encoding the same target actions. Prominent training recipes forgo the first, blocking expert-to-VLM gradients (insul...

</details>

<details>
<summary>Share</summary>

```
Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs

Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations.

arXiv: https://arxiv.org/abs/2611.05249

#VLA #robotics
```

</details>

---

### [Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training](https://arxiv.org/abs/2611.04873)

**Authors:** Zicheng Kong, Zhenbo Xu, Haoyan Zhang, Jinghan Yang, Zhenzhen Li et al. (10 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.04873) | [PDF](https://arxiv.org/pdf/2611.04873)

<details>
<summary>Abstract</summary>

Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality. We introduce Trusting Imagined Futures (TIF), an offline supervision selection method for vision-language-action (VLA) post-training that audits predicted rewards using execution feedback. A multidimensional reward model predicts a utility score for candidate ranking and five dimensions of execution quality. An auditor uses reward predictions and uncertainty to identify overestimation patterns learned from paired imagined videos a...

</details>

<details>
<summary>Share</summary>

```
Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training

Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality.

arXiv: https://arxiv.org/abs/2611.04873

#VLA #robotics
```

</details>

---

### [Future Representation Distillation for Imagination-free World Action Models](https://arxiv.org/abs/2611.04527)

**Authors:** Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah et al. (8 authors)

**Published:** 2026-11-03 (updated 2026-11-04) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04527) | [PDF](https://arxiv.org/pdf/2611.04527) | [Project Page](https://harryjo97.github.io/dreamfree/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction without generating future videos. We introduce DreamFree, a WAM that repurposes a pretrained video diffusion model as a predictive visual encoder through representation distillation. Th...

</details>

<details>
<summary>Share</summary>

```
Future Representation Distillation for Imagination-free World Action Models

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

arXiv: https://arxiv.org/abs/2611.04527
Project page: https://harryjo97.github.io/dreamfree/

#VLA #robotics
```

</details>

---

### [RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training](https://arxiv.org/abs/2611.04368)

**Authors:** Shresth Grover, Andrey Kolobov, Dhruv Shah

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04368) | [PDF](https://arxiv.org/pdf/2611.04368)

<details>
<summary>Abstract</summary>

Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training procedure: RAFT first trains low-rank adapters on task-relevant reasoning annotations, then freezes them while fine-tuning the policy on action demonstrations. On a physical DROID robot, RAFT achieves $75.0\%$ out-of-distribution success, compared with $27.9\%$ for plain fine-tuning; on a multi-stage bim...

</details>

<details>
<summary>Share</summary>

```
RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training

Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions.

arXiv: https://arxiv.org/abs/2611.04368

#VLA #robotics
```

</details>

---

### [Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](https://arxiv.org/abs/2611.04166)

**Authors:** Zihao Feng, Qingzhao Zhang, Chunyu Xia, Bo Yu, Z. Morley Mao et al. (6 authors)

**Published:** 2026-11-03 | **Categories:** cs.LG, cs.CR, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04166) | [PDF](https://arxiv.org/pdf/2611.04166)

<details>
<summary>Abstract</summary>

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety. Prior attacks on VLA reasoning corrupt the rationale itself and leave visible evidence in the text. We show that visual perturbations can instead alter the physical action while keeping the generated rationale word-for-word identical. At the shared text/action interface of Alpamayo for driving and InstructVLA for manipulation, our text-neutral action-subspace (TNAS) diagnostic shows that the locally most action-sensitive direction is nearly...

</details>

<details>
<summary>Share</summary>

```
Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety.

arXiv: https://arxiv.org/abs/2611.04166

#VLA #robotics
```

</details>

---

### [Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies](https://arxiv.org/abs/2611.02777)

**Authors:** Zhennan Jiang, Tingying Xie, Shilong Ji, Shu'ang Yu, Tianxing Zhou et al. (14 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

### [Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy](https://arxiv.org/abs/2611.04006)

**Authors:** Ruijie Zhang, Jiayin Zheng, Yequan Zhao, Liyan Tan, Ziyue Liu et al. (11 authors)

**Published:** 2026-11-02 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.04006) | [PDF](https://arxiv.org/pdf/2611.04006)

<details>
<summary>Abstract</summary>

Modern learning systems increasingly combine pretrained models with downstream heads. Despite the growing importance of such modular designs, how the downstream model co-adapts to the geometry of pretrained representations remains relatively underexplored. We study this problem through vision-language-action models (VLAs), where a pretrained vision-language model (VLM) conditions an action model for control. We find that the action model progressively concentrates its sensitivity on high-variance dimensions of the VLM outputs. Through controlled experiments across different backbone-head model...

</details>

<details>
<summary>Share</summary>

```
Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy

Modern learning systems increasingly combine pretrained models with downstream heads.

arXiv: https://arxiv.org/abs/2611.04006

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

### [Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks](https://arxiv.org/abs/2611.07411)

**Authors:** Yuze Lu

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.07411) | [PDF](https://arxiv.org/pdf/2611.07411)

<details>
<summary>Abstract</summary>

Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck. Existing video codecs spend bits on content the receiver could predict: the robot's own motion. We introduce the kinematic hypothesis context, a zero-rate conditioning signal that both ends build from joint states, the robot model and the camera calibration. Ego-motion homographies, per-link robot reprojections, an end-effector plane and a background memory warp the previous reconstruction into hypotheses that condition a learned video codec. We prove that history-only and...

</details>

<details>
<summary>Share</summary>

```
Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks

Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck.

arXiv: https://arxiv.org/abs/2611.07411

#VLA #robotics
```

</details>

---

### [Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)

**Authors:** Sombit Dey, Luc Van Gool, Danda Pani Paudel

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.05155) | [PDF](https://arxiv.org/pdf/2611.05155)

<details>
<summary>Abstract</summary>

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity. Existing Vision-Language-Action (VLA) architectures execute high-level semantic reasoning and action ex- ecution sequentially within the primary control loop, creating a fundamental tension between semantic-reasoning capability and robot agility. To address this, we propose Asynchronous Robot Policy (ARP), an architectural framework that decouples semantic reasoning from low-level action g...

</details>

<details>
<summary>Share</summary>

```
Asynchronous Robot Policies

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity.

arXiv: https://arxiv.org/abs/2611.05155

#VLA #robotics
```

</details>

---

### [Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture](https://arxiv.org/abs/2611.04972)

**Authors:** Abhijeet M. Kulkarni, Saimouli Katragadda, Yuze Du, Zijun Sha, Guoquan Huang

**Published:** 2026-11-03 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04972) | [PDF](https://arxiv.org/pdf/2611.04972)

<details>
<summary>Abstract</summary>

By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting language-based navigation commands but lack the physical grounding and explicit safety assurance required for real-world operation. Therefore, this paper aims to cage Legged-Vision-Language Navigation (VLN) through a safety architecture that provides physical grounding and ensures navigation safety. The key idea is not to abandon the powerful capabilities of end-to-end VLA planning, b...

</details>

<details>
<summary>Share</summary>

```
Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture

By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting lang...

arXiv: https://arxiv.org/abs/2611.04972

#VLA #robotics
```

</details>

---

### [Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots](https://arxiv.org/abs/2611.04522)

**Authors:** Zhiqian Xia, Lianyang Ma, Haifeng Xia, Siyu Xia, Wei Wang et al. (6 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04522) | [PDF](https://arxiv.org/pdf/2611.04522)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved promising performance for generalized robotic manipulation, yet their reliance on expensive real-robot data remains a fundamental bottleneck. A scalable alternative is to transfer knowledge from off-the-shelf human-centric videos. However, existing methods extract latent action representations that are entangled with scene-specific noise, diluting the transferred knowledge. Motivated by this limitation, we propose Action-Intent Transfer (AIT), a two-stage method that transfers knowledge through a clean action representation shared across humans...

</details>

<details>
<summary>Share</summary>

```
Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots

Vision-Language-Action (VLA) models have achieved promising performance for generalized robotic manipulation, yet their reliance on expensive real-robot data remains a fundamental bottleneck.

arXiv: https://arxiv.org/abs/2611.04522

#VLA #robotics
```

</details>

---

### [DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226)

**Authors:** Renkai Yi, Yuwei Wu, Haoyu Zhang, Penghao Dai, Zhi Gao et al. (7 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04226) | [PDF](https://arxiv.org/pdf/2611.04226)

<details>
<summary>Abstract</summary>

Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework for robot-use agents that uses phase-specific evidence and method preconditions to select program reuse or predefined recovery skills, including bounded vision-language-action (VLA) grasping. After the original program exits, a multimodal large language model (MLLM) can generate corrective code from images and execution...

</details>

<details>
<summary>Share</summary>

```
DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution

Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful.

arXiv: https://arxiv.org/abs/2611.04226

#VLA #robotics
```

</details>

---

### [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](https://arxiv.org/abs/2611.04096)

**Authors:** Kevin Weekly, Alexandre M. Bayen

**Published:** 2026-11-03 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04096) | [PDF](https://arxiv.org/pdf/2611.04096)

<details>
<summary>Abstract</summary>

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically been performed offline. As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic policies, a deterministic safety layer with formal guarantees is an essential complement. We present a CUDA implementation of the canonical WENO5 + TVD-RK3 + Lax-Friedrichs level-set Hamilton-Jacobi-Isaacs solver for 2D, 3D, and 4...

</details>

<details>
<summary>Share</summary>

```
Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically...

arXiv: https://arxiv.org/abs/2611.04096

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

**Published:** 2026-10-31 (updated 2026-11-05) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

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

### [AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241)

**Authors:** Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei et al. (8 authors)

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.04241) | [PDF](https://arxiv.org/pdf/2611.04241)

<details>
<summary>Abstract</summary>

Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not necessarily reflect changes in task objectives. We introduce AceAction, a dataset of human gameplay across multiple 3D games for learning skill composition and subgoal transitions. AceAction organizes demonstrations around complete tasks, linking overall instructions, ordered subgoals, and local skill instructions to...

</details>

<details>
<summary>Share</summary>

```
AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds

Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly.

arXiv: https://arxiv.org/abs/2611.04241

#VLA #robotics
```

</details>

---

### [Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.06475)

**Authors:** Sihang Chen, Chen Ye, Wei Chen, Xiaohan Lei, Zhipeng Tang et al. (11 authors)

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.06475) | [PDF](https://arxiv.org/pdf/2611.06475)

<details>
<summary>Abstract</summary>

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specifically, the tasks are grouped into two categories of memory: One is environment memory, which captures sp...

</details>

<details>
<summary>Share</summary>

```
Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable.

arXiv: https://arxiv.org/abs/2611.06475

#VLA #robotics
```

</details>

---

### [Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks](https://arxiv.org/abs/2611.03168)

**Authors:** Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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

### [Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)

**Authors:** Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang, Wenbo Zhang, Kwanyoung Park et al. (28 authors)

**Published:** 2026-11-01 (updated 2026-11-03) | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

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
