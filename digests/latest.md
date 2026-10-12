# What's New

Papers discovered in the run at **2026-10-12 22:43 UTC**.

**New this run:** 29

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (3)

### [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](https://arxiv.org/abs/2610.13732)

**Authors:** Zhiyuan Xiang, Peidong Liu, Mingyang Li, Jiawei Li, Wenhow Li et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in abstract; 3 distinct keyword hits

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2610.13732) | [PDF](https://arxiv.org/pdf/2610.13732)

<details>
<summary>Abstract</summary>

Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame visual transitions in human videos and uses them as human-derived supervision, while LAPT-Scale-Policy...

</details>

<details>
<summary>Share</summary>

```
LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos

Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data.

arXiv: https://arxiv.org/abs/2610.13732

#egocentric #robotlearning
```

</details>

---

### [EgoReveal: Learning Active Vision and Object Manipulation under Partial Occlusions from Egocentric Demonstrations](https://arxiv.org/abs/2610.12999)

**Authors:** Hiromu Kurihara, Kazutoshi Tanaka, Masashi Hatano, Tadashi Kozuno, Hideo Saito et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric demonstration" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12999) | [PDF](https://arxiv.org/pdf/2610.12999)

<details>
<summary>Abstract</summary>

Learning from Demonstrations (LfD) enables robots to learn object manipulation directly from human demonstrations. In contrast to resource-intensive and labor-intensive teleoperation, egocentric demonstrations are easy to collect, enabling scalable data collection. Manipulated objects are often partially occluded in everyday environments, yet prior egocentric demonstration-based methods that require no robots or specialized teaching devices do not explicitly address occlusions. To fill this gap, we propose EgoReveal, a framework that learns viewpoint-repositioning together with manipulation ac...

</details>

<details>
<summary>Share</summary>

```
EgoReveal: Learning Active Vision and Object Manipulation under Partial Occlusions from Egocentric Demonstrations

Learning from Demonstrations (LfD) enables robots to learn object manipulation directly from human demonstrations.

arXiv: https://arxiv.org/abs/2610.12999

#egocentric #robotlearning
```

</details>

---

### [What Egocentric Video Embeddings Encode and How to Combine Them with Inertial Sensors for Human Activity Recognition](https://arxiv.org/abs/2610.12926)

**Authors:** Kansuke Habano

**Published:** 2026-10-09 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.12926) | [PDF](https://arxiv.org/pdf/2610.12926)

<details>
<summary>Abstract</summary>

Egocentric video and body-worn inertial sensors are increasingly recorded together, and the video is usually encoded by pretrained models. What these embeddings represent when the camera sits on the head, and how they should be combined with inertial sensing, has received little attention. Across VideoMAEv2, CLIP, DINOv2 and the egocentric VC-1, the leading principal directions of the embedding are dominated by where the camera looks. Measured head orientation explains them on Ego-Exo4D for egocentric (R^2 0.49-0.70) but not exocentric cameras, and the scene layout explains them on WEAR. The p...

</details>

<details>
<summary>Share</summary>

```
What Egocentric Video Embeddings Encode and How to Combine Them with Inertial Sensors for Human Activity Recognition

Egocentric video and body-worn inertial sensors are increasingly recorded together, and the video is usually encoded by pretrained models.

arXiv: https://arxiv.org/abs/2610.12926

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (17)

### [Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models](https://arxiv.org/abs/2610.13212)

**Authors:** Min Lin, Bokai Zhou, Jianqi Lin, Kaiyuan Yang, Yicheng Chang et al. (11 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13212) | [PDF](https://arxiv.org/pdf/2610.13212) | [Project Page](https://afceproject.github.io/AFCE-Web/)

<details>
<summary>Abstract</summary>

Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary prediction target. An offline tokenizer constructs temporally ordered Effect tokens from demonstrated actions, realized robot responses, and sparse visual transitions. Reconstruction objectives encourage the representation to retain executable d...

</details>

<details>
<summary>Share</summary>

```
Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models

Actions specify what a robot should execute, but do not describe what those commands will achieve.

arXiv: https://arxiv.org/abs/2610.13212
Project page: https://afceproject.github.io/AFCE-Web/

#VLA #robotics
```

</details>

---

### [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)

**Authors:** Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12696) | [PDF](https://arxiv.org/pdf/2610.12696) | [Project Page](https://justintiensmith.github.io/Spa-Bench/)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) offer a promising route toward general-purpose robotics by transferring semantic knowledge from large-scale vision-language pretraining into language-conditioned control. However, most VLA evaluations emphasize aggregate manipulation success under changes in objects, instructions, or environments, leaving unclear how reliably these policies ground spatial descriptions in the physical scenes where they act. We therefore ask a sharper question: how reliably can current VLAs translate spatial descriptions into appropriate real-robot behavior? To investigate th...

</details>

<details>
<summary>Share</summary>

```
Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

Vision-language-action models (VLAs) offer a promising route toward general-purpose robotics by transferring semantic knowledge from large-scale vision-language pretraining into language-conditioned control.

arXiv: https://arxiv.org/abs/2610.12696
Project page: https://justintiensmith.github.io/Spa-Bench/

#VLA #robotics
```

</details>

---

### [Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945)

**Authors:** Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13945) | [PDF](https://arxiv.org/pdf/2610.13945) | [Project Page](https://splat2act.github.io)

<details>
<summary>Abstract</summary>

A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects...

</details>

<details>
<summary>Share</summary>

```
Splat2Act: From Captured Scenes to Personalized VLA Manipulation

A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables.

arXiv: https://arxiv.org/abs/2610.13945
Project page: https://splat2act.github.io

#VLA #robotics
```

</details>

---

### [JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation](https://arxiv.org/abs/2610.13628)

**Authors:** Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov, Dzmitry Tsetserukou

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.HC, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13628) | [PDF](https://arxiv.org/pdf/2610.13628) | [Project Page](https://faithogunwoye.github.io/JitterVLA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isolating the controller's effect. We apply it to synthetic reaches, hand trajectories from 20 people, three open VLA pipelines (838 episodes) and a physical UR3. Interpolation lowered modeled p99 jerk for every source, by 83% (615 to 106 m/s^3)...

</details>

<details>
<summary>Share</summary>

```
JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation

Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people.

arXiv: https://arxiv.org/abs/2610.13628
Project page: https://faithogunwoye.github.io/JitterVLA/

#VLA #robotics
```

</details>

---

### [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation](https://arxiv.org/abs/2610.13578)

**Authors:** Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13578) | [PDF](https://arxiv.org/pdf/2610.13578) | [Project Page](https://shua-kang.github.io/RARA_robot/)

<details>
<summary>Abstract</summary>

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves...

</details>

<details>
<summary>Share</summary>

```
RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging.

arXiv: https://arxiv.org/abs/2610.13578
Project page: https://shua-kang.github.io/RARA_robot/

#VLA #robotics
```

</details>

---

### [Forward Dynamics Models](https://arxiv.org/abs/2610.13117)

**Authors:** Zipei Ma, Junzhe Jiang, Jiahui Zhang, Juntong Zhang, Chun Gu et al. (9 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13117) | [PDF](https://arxiv.org/pdf/2610.13117) | [Project Page](https://logosroboticsgroup.github.io/FDM/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively. Yet VLAs learn without explicit supervision from future world states, while WAMs that condition actions on predicted futures incur extra inference cost and let visual prediction errors propagate into actions. We present Forward Dynamics Models (FDM), a family of robotic action models that couples action and future world-state prediction through an action-to-future paradigm. Future predi...

</details>

<details>
<summary>Share</summary>

```
Forward Dynamics Models

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively.

arXiv: https://arxiv.org/abs/2610.13117
Project page: https://logosroboticsgroup.github.io/FDM/

#VLA #robotics
```

</details>

---

### [Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision](https://arxiv.org/abs/2610.12936)

**Authors:** Zile Zhong, Yuxin Du, Tao Lin, Haoxiao Wang, Wei Dai et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12936) | [PDF](https://arxiv.org/pdf/2610.12936)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide additional information for control. Action supervision alone does not explicitly encourage such anticipation, while future-image prediction entangles task-relevant motion with largely static appearance. To address these limitations, we introduce Evo-World, a lightweight VLA model that augments policy learning with future motion prediction through optical-flow supervision, thereby pr...

</details>

<details>
<summary>Share</summary>

```
Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision

Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide ad...

arXiv: https://arxiv.org/abs/2610.12936

#VLA #robotics
```

</details>

---

### [Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies](https://arxiv.org/abs/2610.12861)

**Authors:** Weiwei Chen, Chenghao Xu, Meiling Yu, Xu Yang, Cheng Deng

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12861) | [PDF](https://arxiv.org/pdf/2610.12861) | [Project Page](https://krlozhilderman287-creator.github.io/EVIDENCE-GUIDED-COUNTERFACTUAL-LEARNING-FOR-LONG-TAILED-ROBOTIC-POLICIES/)

<details>
<summary>Abstract</summary>

In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets. To investigate this issue, we study the head-task action bias in shared robot policies, particularly focusing on its relationship with task-specific visual evidence. Our experimental analysis shows that, when the visual evidence required by a tail task is insufficient, the policy increasingly falls back on action patterns reinforced by data-rich head tasks, resulting in degraded performance on u...

</details>

<details>
<summary>Share</summary>

```
Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies

In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets.

arXiv: https://arxiv.org/abs/2610.12861
Project page: https://krlozhilderman287-creator.github.io/EVIDENCE-GUIDED-COUNTERFACTUAL-LEARNING-FOR-LONG-TAILED-ROBOTIC-POLICIES/

#VLA #robotics
```

</details>

---

### [VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding](https://arxiv.org/abs/2610.12832)

**Authors:** Jingkun Yi, Shujie Zhang, Zirui Zhou, Haoxiao Wang, Haiyang Sun et al. (11 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12832) | [PDF](https://arxiv.org/pdf/2610.12832) | [Project Page](https://general-robo.github.io/EASG/)

<details>
<summary>Abstract</summary>

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation. The key challenge in turning pretrained VLMs into generalist manipulation policies is to expose these capabilities through an appropriate action interface. Vision-language-action (VLA) models provide a unified trainable policy, but typically introduce learned action tokens, action heads, or action experts whose semantics must be learned from robot data pretraining. In contrast, modular foundation-model-based manipulation methods can exploit pretrained VLM...

</details>

<details>
<summary>Share</summary>

```
VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation.

arXiv: https://arxiv.org/abs/2610.12832
Project page: https://general-robo.github.io/EASG/

#VLA #robotics
```

</details>

---

### [StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras](https://arxiv.org/abs/2610.12734)

**Authors:** Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12734) | [PDF](https://arxiv.org/pdf/2610.12734) | [Project Page](https://stereoengine.github.io)

<details>
<summary>Abstract</summary>

Stereo vision is increasingly used for robotic manipulation, with a growing body of work incorporating it into Vision-Language-Action (VLA) models. However, the scarcity of large-scale, real-world stereo datasets remains a fundamental bottleneck for scaling such policies. Recent generative monocular-to-stereo methods target settings such as VR content and autonomous driving. No prior work produces realistic synthetic stereo data for robotic manipulation, where stereo supervision has come predominantly from simulation. We propose StereoEngine, which introduces two complementary methods to synth...

</details>

<details>
<summary>Share</summary>

```
StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras

Stereo vision is increasingly used for robotic manipulation, with a growing body of work incorporating it into Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2610.12734
Project page: https://stereoengine.github.io

#VLA #robotics
```

</details>

---

### [OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models](https://arxiv.org/abs/2610.12914)

**Authors:** Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12914) | [PDF](https://arxiv.org/pdf/2610.12914)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optim...

</details>

<details>
<summary>Share</summary>

```
OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations.

arXiv: https://arxiv.org/abs/2610.12914

#VLA #robotics
```

</details>

---

### [Noise Space Learning for VLA Adaptation](https://arxiv.org/abs/2610.13943)

**Authors:** Junjie Lu, Chuheng Zhang, Yucen Wang, Yuhua Jiang, Xinyao Qin et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.13943) | [PDF](https://arxiv.org/pdf/2610.13943)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints. Noise space learning (NSL) adapts flow-matching-based VLAs by learning a context-conditioned distribution over noise while keeping the pretrained VLA fixed. Building on prior noise-steering methods, we formulate NSL as an interface for VLA adaptation that accommodates different learning algorithms and instantiate it with PPO, SAC, and AWR. Theoretically, we provide an information-theor...

</details>

<details>
<summary>Share</summary>

```
Noise Space Learning for VLA Adaptation

Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints.

arXiv: https://arxiv.org/abs/2610.13943

#VLA #robotics
```

</details>

---

### [Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving](https://arxiv.org/abs/2610.13453)

**Authors:** Yuechen Luo, He Chong, Fang Li, Shaoqing Xu, Hexin Zhang et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.13453) | [PDF](https://arxiv.org/pdf/2610.13453)

<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models. However, existing RL methods rely on scalar trajectory rewards that measure overall quality but fail to identify specific planning errors or provide actionable correction signals. In long-tail scenarios, errors in scene understanding, behavior selection, and trajectory execution are compressed into a single score. We observe that Reflective Guidance turns trajectory evaluation into explicit diagnoses and corrective instructions, substantially improving planning acc...

</details>

<details>
<summary>Share</summary>

```
Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving

Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2610.13453

#VLA #robotics
```

</details>

---

### [REMM: Revisable Embodied Memory for Manipulation](https://arxiv.org/abs/2610.12710)

**Authors:** Revanth Krishna Senthilkumaran, Ruwan Wickramarachchi, Alessandro Oltramari, Jonathan Francis

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12710) | [PDF](https://arxiv.org/pdf/2610.12710) | [Project Page](https://revanthsenthil.github.io/remm/)

<details>
<summary>Abstract</summary>

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence. Retaining observations alone does not specify which completed conditions should be withdrawn after a disturbance or which obligations require repair. We introduce REMM, Revisable Embodied Memory for Manipulation, a supervisory memory layer for a frozen G0.5 vision-language-action executor. REMM separates an append-only evidence history from revisable task state and explicitly links derived relations and completed conditions to their supporting facts. Wh...

</details>

<details>
<summary>Share</summary>

```
REMM: Revisable Embodied Memory for Manipulation

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence.

arXiv: https://arxiv.org/abs/2610.12710
Project page: https://revanthsenthil.github.io/remm/

#VLA #robotics
```

</details>

---

### [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/abs/2610.13516)

**Authors:** David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.13516) | [PDF](https://arxiv.org/pdf/2610.13516)

<details>
<summary>Abstract</summary>

Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions. Yet an accurate alarm may arrive too late for recovery, while an unnecessary intervention may disrupt an execution that would otherwise succeed. We introduce RESCUE, a counterfactual framework for evaluating whether a monitor's alarms enable useful interventions. By restoring simulator and policy states at execution checkpoints, RESCUE compares alternative actions, identifies the latest checkpoint satisfying a specified recovery criterion, and evaluates whet...

</details>

<details>
<summary>Share</summary>

```
RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions.

arXiv: https://arxiv.org/abs/2610.13516

#VLA #robotics
```

</details>

---

### [Dual-Stream Memory for Vision-Language-Action Policies](https://arxiv.org/abs/2610.13262)

**Authors:** Yang Wang, Ping Liu, Ruiyu Wang, Xuhua Chen, Lingfeng Zhang et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.13262) | [PDF](https://arxiv.org/pdf/2610.13262)

<details>
<summary>Abstract</summary>

Memory-dependent manipulation requires a policy to track execution state and recover visual evidence that is no longer observable. We propose dual-stream memory for vision-language-action policies, assigning these requirements to complementary representations. A task-agnostic Gated DeltaNet compresses history into one temporal token, supervised by progress prediction and action-conditioned feature reconstruction. A task-conditioned retriever retains frames above a fixed relevance threshold; linear multi-scale fusion encodes each frame into sixteen spatial tokens. We then freeze the temporal co...

</details>

<details>
<summary>Share</summary>

```
Dual-Stream Memory for Vision-Language-Action Policies

Memory-dependent manipulation requires a policy to track execution state and recover visual evidence that is no longer observable.

arXiv: https://arxiv.org/abs/2610.13262

#VLA #robotics
```

</details>

---

### [Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation](https://arxiv.org/abs/2610.12793)

**Authors:** Yudong Liu, Yueqian Lin, Zijia Tang, Yuxi Zheng, Yuan Li et al. (14 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.12793) | [PDF](https://arxiv.org/pdf/2610.12793)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key id...

</details>

<details>
<summary>Share</summary>

```
Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation

Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic...

arXiv: https://arxiv.org/abs/2610.12793

#VLA #robotics
```

</details>

---

## World Models (9)

### [Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](https://arxiv.org/abs/2610.13164)

**Authors:** Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13164) | [PDF](https://arxiv.org/pdf/2610.13164) | [Project Page](https://fffstrong.github.io/Grounded-Dreamer/)

<details>
<summary>Abstract</summary>

Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale. Existing methods either depend on human teleoperation, rely on simulation with limited visual realism, or use human videos that lack embodiment-specific annotations. In this paper, we introduce Grounded-Dreamer, a framework for synthesizing physically grounded robot manipulation data with video world models while avoiding human teleoperation demonstrations. Grounded-Dreamer combines the visual realism of generative vide...

</details>

<details>
<summary>Share</summary>

```
Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding

Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale.

arXiv: https://arxiv.org/abs/2610.13164
Project page: https://fffstrong.github.io/Grounded-Dreamer/

#worldmodels #robotics
```

</details>

---

### [ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409)

**Authors:** Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13409) | [PDF](https://arxiv.org/pdf/2610.13409) | [Code](https://github.com/wyh-autonomy/maneuverflow)

<details>
<summary>Abstract</summary>

End-to-end planning in complex scenes must model diverse driving intentions and select the most appropriate trajectory using scene context and future risks. However, multi-query regression may collapse to one mode, while anchor-based and generative planners share a scaling bottleneck: small candidate sets limit maneuver coverage or discovery of high-quality trajectories, whereas large sets increase generation and scoring costs. We propose ManeuverFlow to generate trajectories for distinct intentions in one step and evaluate and refine them using current and future evidence. The model selects r...

</details>

<details>
<summary>Share</summary>

```
ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving

End-to-end planning in complex scenes must model diverse driving intentions and select the most appropriate trajectory using scene context and future risks.

arXiv: https://arxiv.org/abs/2610.13409
Code: https://github.com/wyh-autonomy/maneuverflow

#worldmodels #robotics
```

</details>

---

### [SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781)

**Authors:** Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang et al. (11 authors)

**Published:** 2026-10-09 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13781) | [PDF](https://arxiv.org/pdf/2610.13781) | [Project Page](https://opendrivelab.com/SimVTA/)

<details>
<summary>Abstract</summary>

Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a simulation-grounded post-training framework that combines trajectory optimization with video supervision. First, we sample candidate trajectories for each observation and use a real-world sim...

</details>

<details>
<summary>Share</summary>

```
SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models

Driving world action models (WAMs) learn from paired trajectories and future observations.

arXiv: https://arxiv.org/abs/2610.13781
Project page: https://opendrivelab.com/SimVTA/

#worldmodels #robotics
```

</details>

---

### [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)

**Authors:** Minghao Fu, Tavis Siebert, Eryk Halicki, Randall Balestriero

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12818) | [PDF](https://arxiv.org/pdf/2610.12818) | [Project Page](https://le-wam.github.io/)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and action-conditioned dynamics before adding a control policy or solver. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic Gaussian constraint on the latent state, enabling a single model to support direct policy execution and efficient planning by evaluating sampled actions with its learned latent dyna...

</details>

<details>
<summary>Share</summary>

```
LeWAM: End-to-End World and Action Modeling with JEPAs

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction.

arXiv: https://arxiv.org/abs/2610.12818
Project page: https://le-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522)

**Authors:** Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.13522) | [PDF](https://arxiv.org/pdf/2610.13522)

<details>
<summary>Abstract</summary>

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance of successful demonstrations leaves failure dynamics substantially underrepresented, limiting the ab...

</details>

<details>
<summary>Share</summary>

```
Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions.

arXiv: https://arxiv.org/abs/2610.13522

#worldmodels #robotics
```

</details>

---

### [Dream to Remember: Continual Steering of Generalist Robot Policies with World Models](https://arxiv.org/abs/2610.13816)

**Authors:** Bahey Tharwat, Iman Nematollahi, Marvin Alles, Xingyuan Zhang, Akshay L Chandra et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.13816) | [PDF](https://arxiv.org/pdf/2610.13816)

<details>
<summary>Abstract</summary>

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering module. We propose Dream to Remember (D2R), which continually steers a frozen generalist policy toward...

</details>

<details>
<summary>Share</summary>

```
Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations.

arXiv: https://arxiv.org/abs/2610.13816

#worldmodels #robotics
```

</details>

---

### [Sampling-based Kinodynamic Planning with World Models](https://arxiv.org/abs/2610.12910)

**Authors:** Yitian Gao, Hanlan Yang, Zachary Kingston

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12910) | [PDF](https://arxiv.org/pdf/2610.12910)

<details>
<summary>Abstract</summary>

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI. However, these optimizers stall on long-horizon tasks where progress requires motion the objective does not reward, such as moving around a block before pushing it. This paper revisits kinodynamic sampling-based motion planning for world models, using the learned model as the propagator of a tree search in latent space. Our key insight is that the sampling strategies devised for high-dimensional search in configuration space apply directly to the lat...

</details>

<details>
<summary>Share</summary>

```
Sampling-based Kinodynamic Planning with World Models

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI.

arXiv: https://arxiv.org/abs/2610.12910

#worldmodels #robotics
```

</details>

---

### [Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217)

**Authors:** Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.13217) | [PDF](https://arxiv.org/pdf/2610.13217)

<details>
<summary>Abstract</summary>

Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models. State-of-the-art systems achieve controllability primarily through image-to-video (I2V) generation, in which an injected anchor image determines the identity, composition, and style of the resulting video. In modern pipelines, this anchor is synthesized by a text-to-image (T2I) generator. This raises a largely overlooked question: Are images obtained directly from the T2I model truly suitable for current video models? Our analysis shows tha...

</details>

<details>
<summary>Share</summary>

```
Golden Anchor for Video Generation

Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models.

arXiv: https://arxiv.org/abs/2610.13217

#worldmodels #robotics
```

</details>

---

### [Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing](https://arxiv.org/abs/2610.12881)

**Authors:** Zheng Ren, Yanning Wang, Ziheng Huang, Fei Huang, Shiqi Wang et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12881) | [PDF](https://arxiv.org/pdf/2610.12881)

<details>
<summary>Abstract</summary>

Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models. However, existing evaluations of multimodal large language models (MLLMs) for spatial reasoning rely predominantly on static question-answering (QA) over small-scale or synthetic scenes, rarely probing whether models can modify spatial configurations while satisfying explicit geometric constraints. We introduce GeoSpatialBench, a benchmark designed to evaluate an escalating progression of spatial cognition, ranging from spatial relation unde...

</details>

<details>
<summary>Share</summary>

```
Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing

Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models.

arXiv: https://arxiv.org/abs/2610.12881

#worldmodels #robotics
```

</details>

---
