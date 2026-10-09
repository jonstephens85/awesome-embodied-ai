# What's New

Papers discovered in the run at **2026-10-09 20:33 UTC**.

**New this run:** 29

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (3)

### [Fixed-Reference Pose Residuals for Measuring Cross-Dataset Cue Transfer in Human-Robot Interaction Anticipation](https://arxiv.org/abs/2610.12245)

**Authors:** Bowen Yang, Xinliang Xiao, Wenjing Zhang, Li Yang, Wei Zhou

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric dataset" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12245) | [PDF](https://arxiv.org/pdf/2610.12245) | [Code](https://github.com/WeiZhou96/FRPR-interaction-anticipation)

<details>
<summary>Abstract</summary>

Social and service robots in public spaces need to anticipate which nearby person is about to approach and touch them, so that a response can be prepared before contact. It is largely unknown which cues support this anticipation when a model trained with one robot is used on another robot at a different site. We study this question with a fixed-reference pose residual (FRPR) model: a geometry predictor built from the person's bounding box and mask is trained and frozen, and a temporal network then learns from body pose an additive correction to its logit, so that every prediction splits exactl...

</details>

<details>
<summary>Share</summary>

```
Fixed-Reference Pose Residuals for Measuring Cross-Dataset Cue Transfer in Human-Robot Interaction Anticipation

Social and service robots in public spaces need to anticipate which nearby person is about to approach and touch them, so that a response can be prepared before contact.

arXiv: https://arxiv.org/abs/2610.12245
Code: https://github.com/WeiZhou96/FRPR-interaction-anticipation

#egocentric #robotlearning
```

</details>

---

### [EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248)

**Authors:** Heeseung Kim

**Published:** 2026-10-08 | **Categories:** cs.CL, cs.CV, cs.SD | **Relevance:** ★★☆☆☆

**Why surfaced:** "first-person video" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12248) | [PDF](https://arxiv.org/pdf/2610.12248) | [Project Page](https://egocentricvoice.github.io/)

<details>
<summary>Abstract</summary>

Wearable augmented reality (AR) assistants are moving toward continuous real-world interaction, where they perceive the user's activity through first-person video and audio and provide timely spoken guidance without being explicitly asked. While proactive video assistants, spoken dialog systems, and egocentric task understanding have each advanced rapidly, existing systems do not address the joint problem of deciding when to speak and what to say from continuous first-person streams. We introduce EgoVoice, a framework for training and evaluating proactive egocentric spoken assistants. From Hol...

</details>

<details>
<summary>Share</summary>

```
EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams

Wearable augmented reality (AR) assistants are moving toward continuous real-world interaction, where they perceive the user's activity through first-person video and audio and provide timely spoken guidance without b...

arXiv: https://arxiv.org/abs/2610.12248
Project page: https://egocentricvoice.github.io/

#egocentric #robotlearning
```

</details>

---

### [LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442)

**Authors:** Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12442) | [PDF](https://arxiv.org/pdf/2610.12442)

<details>
<summary>Abstract</summary>

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but translates depth errors into misplaced content. We ask what a video diffusion model sh...

</details>

<details>
<summary>Share</summary>

```
LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved.

arXiv: https://arxiv.org/abs/2610.12442

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (15)

### [VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation](https://arxiv.org/abs/2610.12451)

**Authors:** Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12451) | [PDF](https://arxiv.org/pdf/2610.12451) | [Project Page](https://boyaohan.github.io/VersaCamVLA.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-A...

</details>

<details>
<summary>Share</summary>

```
VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pos...

arXiv: https://arxiv.org/abs/2610.12451
Project page: https://boyaohan.github.io/VersaCamVLA.github.io/

#VLA #robotics
```

</details>

---

### [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models](https://arxiv.org/abs/2610.12007)

**Authors:** Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren et al. (11 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12007) | [PDF](https://arxiv.org/pdf/2610.12007) | [Project Page](https://react-vla.github.io)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon...

</details>

<details>
<summary>Share</summary>

```
REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, wherea...

arXiv: https://arxiv.org/abs/2610.12007
Project page: https://react-vla.github.io

#VLA #robotics
```

</details>

---

### [CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding](https://arxiv.org/abs/2610.11971)

**Authors:** Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11971) | [PDF](https://arxiv.org/pdf/2610.11971) | [Project Page](https://capable-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that mot...

</details>

<details>
<summary>Share</summary>

```
CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed.

arXiv: https://arxiv.org/abs/2610.11971
Project page: https://capable-vla.github.io/

#VLA #robotics
```

</details>

---

### [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](https://arxiv.org/abs/2610.12090)

**Authors:** Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12090) | [PDF](https://arxiv.org/pdf/2610.12090)

<details>
<summary>Abstract</summary>

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and...

</details>

<details>
<summary>Share</summary>

```
Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions.

arXiv: https://arxiv.org/abs/2610.12090

#VLA #robotics
```

</details>

---

### [ARC: A Reasoning Recipe for Robot Foundation Models](https://arxiv.org/abs/2610.12386)

**Authors:** Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12386) | [PDF](https://arxiv.org/pdf/2610.12386) | [Project Page](https://arc-robot-reasoning.github.io/)

<details>
<summary>Abstract</summary>

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces s...

</details>

<details>
<summary>Share</summary>

```
ARC: A Reasoning Recipe for Robot Foundation Models

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale.

arXiv: https://arxiv.org/abs/2610.12386
Project page: https://arc-robot-reasoning.github.io/

#VLA #robotics
```

</details>

---

### [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.12285)

**Authors:** Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen et al. (14 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12285) | [PDF](https://arxiv.org/pdf/2610.12285)

<details>
<summary>Abstract</summary>

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented representation space, reducing the need to predict control-irrelevant visual details. Built on a Mixture-of-Transformers architecture, PLaW-VLA conditions action generation on observation history, current task semantics, and predicted future stat...

</details>

<details>
<summary>Share</summary>

```
PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and...

arXiv: https://arxiv.org/abs/2610.12285

#VLA #robotics
```

</details>

---

### [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](https://arxiv.org/abs/2610.12185)

**Authors:** Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12185) | [PDF](https://arxiv.org/pdf/2610.12185) | [Code](https://github.com/JIA-Lab-research/RESETTLE)

<details>
<summary>Abstract</summary>

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery w...

</details>

<details>
<summary>Share</summary>

```
RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors.

arXiv: https://arxiv.org/abs/2610.12185
Code: https://github.com/JIA-Lab-research/RESETTLE

#VLA #robotics
```

</details>

---

### [Tell Robot What Not to Do: A Negation Understanding Perspective](https://arxiv.org/abs/2610.11952)

**Authors:** Fazeng Li, Gan Sun, Hao Cheng, Weihong Ren, Yang Cong

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11952) | [PDF](https://arxiv.org/pdf/2610.11952)

<details>
<summary>Abstract</summary>

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-play framework that extends pretrained VLAs to follow negated instructions through image-language super...

</details>

<details>
<summary>Share</summary>

```
Tell Robot What Not to Do: A Negation Understanding Perspective

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction.

arXiv: https://arxiv.org/abs/2610.11952

#VLA #robotics
```

</details>

---

### [PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies](https://arxiv.org/abs/2610.11771)

**Authors:** Qing Huang, Yifei Yang, Ziqing Zou, Anzhe Chen, Zhenjie Zhu et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11771) | [PDF](https://arxiv.org/pdf/2610.11771)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace. This coupling complicates adaptation from teleoperation: useful geometric guidance comes with timing shaped by interface delays and operator behavior. Our key insight is to bring the path-time parameterization of classical motion planning into the learned action representation of a VLA. We introduce PathTime-VLA, which represents motion as a progress-indexed interaction path $X(s)$ and a positive interval-time profile. The latter defines a monoton...

</details>

<details>
<summary>Share</summary>

```
PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace.

arXiv: https://arxiv.org/abs/2610.11771

#VLA #robotics
```

</details>

---

### [Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning](https://arxiv.org/abs/2610.12231)

**Authors:** Yuchen Zhou, Jiacheng You, Weikang Wan, Weijun Dong, Yang Gao et al. (6 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12231) | [PDF](https://arxiv.org/pdf/2610.12231) | [Project Page](https://the-labone.github.io/regression-policy-project/)

<details>
<summary>Abstract</summary>

Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective of statistical modeling: how action-prediction residuals shape policy optimization. Our analysis of real-world robot demonstration data reveals substantial state-dependent variation in residual scales and heavier-than-Gaussian tails. While bo...

</details>

<details>
<summary>Share</summary>

```
Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning

Learning from demonstration has enabled impressive robot behaviors.

arXiv: https://arxiv.org/abs/2610.12231
Project page: https://the-labone.github.io/regression-policy-project/

#VLA #robotics
```

</details>

---

### [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](https://arxiv.org/abs/2610.12089)

**Authors:** Guoting Wei, Dawei Yan, Xia Yuan, Gengming Zhang, Yelin He et al. (13 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12089) | [PDF](https://arxiv.org/pdf/2610.12089)

<details>
<summary>Abstract</summary>

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction. Learning and evaluating these skills present three challenges: similar observations under a fixed task instruction may make skill selection ambiguous; even when a preceding skill succeeds, the robot state inherited by the next skill may deviate from its demonstrated starting states and affect execution; and task-level metrics hinder skill-specific diagnosis, while early failures leave later skills untested. We therefore...

</details>

<details>
<summary>Share</summary>

```
ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction.

arXiv: https://arxiv.org/abs/2610.12089

#VLA #robotics
```

</details>

---

### [Humanoid World Action Model With Joint State--Action Generation](https://arxiv.org/abs/2610.12026)

**Authors:** Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu et al. (10 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12026) | [PDF](https://arxiv.org/pdf/2610.12026)

<details>
<summary>Abstract</summary>

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robo...

</details>

<details>
<summary>Share</summary>

```
Humanoid World Action Model With Joint State--Action Generation

Humanoid robots are a promising platform for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2610.12026

#VLA #robotics
```

</details>

---

### [VioLA: Learning Generalist Humanoid Control Policies from Human Data](https://arxiv.org/abs/2610.12435)

**Authors:** Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12435) | [PDF](https://arxiv.org/pdf/2610.12435)

<details>
<summary>Abstract</summary>

Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing...

</details>

<details>
<summary>Share</summary>

```
VioLA: Learning Generalist Humanoid Control Policies from Human Data

Teaching a humanoid to follow instructions with its whole body runs into two obstacles.

arXiv: https://arxiv.org/abs/2610.12435

#VLA #robotics
```

</details>

---

### [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](https://arxiv.org/abs/2610.12369)

**Authors:** Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12369) | [PDF](https://arxiv.org/pdf/2610.12369)

<details>
<summary>Abstract</summary>

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code measures and tracks the robot, environment, and task state from camera images and proprioception, a...

</details>

<details>
<summary>Share</summary>

```
Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time.

arXiv: https://arxiv.org/abs/2610.12369

#VLA #robotics
```

</details>

---

### [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](https://arxiv.org/abs/2610.12107)

**Authors:** Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou, Shuhan Yang, Junchao Huang et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12107) | [PDF](https://arxiv.org/pdf/2610.12107)

<details>
<summary>Abstract</summary>

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise boundary delineation. This requirement challenges existing cascaded vision-language architectures, which typically rely on static feature interfaces and single-pass mask prediction, limiting adaptive perception and geometric correction. We introduce ContourVLA, a vision-language-action policy that recasts GRES as a closed-loop visuomotor process, in which editable contours serve a...

</details>

<details>
<summary>Share</summary>

```
ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise...

arXiv: https://arxiv.org/abs/2610.12107

#VLA #robotics
```

</details>

---

## World Models (11)

### [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/abs/2610.12468)

**Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★★

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12468) | [PDF](https://arxiv.org/pdf/2610.12468) | [Project Page](https://brave-eai.github.io/DreamTrue) | [Code](https://github.com/brave-eai/DreamTrue)

<details>
<summary>Abstract</summary>

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render action trajectories into image-space conditions and introduce offline geometric calibration to align these conditions with the target videos. To broaden interaction coverage, we introduc...

</details>

<details>
<summary>Share</summary>

```
DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction.

arXiv: https://arxiv.org/abs/2610.12468
Project page: https://brave-eai.github.io/DreamTrue
Code: https://github.com/brave-eai/DreamTrue

#worldmodels #robotics
```

</details>

---

### [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](https://arxiv.org/abs/2610.12368)

**Authors:** Linkai Liu, Yuntian Zhang, Zhenshan Bing, Chen Chen, Lingjuan Lyu et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12368) | [PDF](https://arxiv.org/pdf/2610.12368)

<details>
<summary>Abstract</summary>

Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences. Generative navigation world models provide this foresight through visual rollouts, which are costly when evaluating multiple candidates. We present LiteNWM, a latent navigation world model that shares visual encoding across candidates and jointly predicts their action-conditioned future representations at multiple horizons, while a learned scorer uses these predictions to select trajectories. In offline evaluations on RECON, SCAND, and SACSoN, LiteNWM reduces macro-aver...

</details>

<details>
<summary>Share</summary>

```
LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild

Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences.

arXiv: https://arxiv.org/abs/2610.12368

#worldmodels #robotics
```

</details>

---

### [Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction](https://arxiv.org/abs/2610.12299)

**Authors:** Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12299) | [PDF](https://arxiv.org/pdf/2610.12299)

<details>
<summary>Abstract</summary>

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate multi-agent egocentric world modeling as synchronized ego-stream generation for multiple agents interacting through fine-grained actions in a shared world. This requires cross-view actio...

</details>

<details>
<summary>Share</summary>

```
Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent.

arXiv: https://arxiv.org/abs/2610.12299

#worldmodels #robotics
```

</details>

---

### [LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC](https://arxiv.org/abs/2610.12407)

**Authors:** Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12407) | [PDF](https://arxiv.org/pdf/2610.12407)

<details>
<summary>Abstract</summary>

World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions. We introduce LeWAM, a bidirectional transformer for forward, backward, inverse dynamics and policy prediction, on a decoder-free JEPA latent trained end-to-end through all four modes. We see the following benefits: 1) Alignment: linear probes read robot and object state from LeWAM's latent better than from a regular Le World Model (a forward-only JEPA world model), while the latent ignores...

</details>

<details>
<summary>Share</summary>

```
LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC

World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions.

arXiv: https://arxiv.org/abs/2610.12407

#worldmodels #robotics
```

</details>

---

### [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](https://arxiv.org/abs/2610.12459)

**Authors:** Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12459) | [PDF](https://arxiv.org/pdf/2610.12459)

<details>
<summary>Abstract</summary>

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as \emph{clos...

</details>

<details>
<summary>Share</summary>

```
WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced.

arXiv: https://arxiv.org/abs/2610.12459

#worldmodels #robotics
```

</details>

---

### [RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning](https://arxiv.org/abs/2610.12333)

**Authors:** Ruixiang Ouyang, Guanren Qiao, Fansen Meng, Yueci Deng, Ruixing Jin et al. (7 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.AI, cs.GR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12333) | [PDF](https://arxiv.org/pdf/2610.12333)

<details>
<summary>Abstract</summary>

Accurate simulation of rigid-body interactions is essential for predictive physical world models. Despite recent progress in modeling object dynamics, capturing how local contacts between surfaces shape object motion remains challenging. While end-to-end world models predict interactions across entire scenes or objects, in practice, rigid-body contact is inherently local, and only nearby surfaces can directly exchange contact forces. Motivated by this observation, we introduce Rigid-body Contact Reasoning (RiCo), which represents interactions between objects through sparse neighborhoods of con...

</details>

<details>
<summary>Share</summary>

```
RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning

Accurate simulation of rigid-body interactions is essential for predictive physical world models.

arXiv: https://arxiv.org/abs/2610.12333

#worldmodels #robotics
```

</details>

---

### [CausalDreamer: Learning Predictive World Models with Latent Disentanglement](https://arxiv.org/abs/2610.12016)

**Authors:** Prince Jha, Nils Lukas, Kun Zhang, Salem Lahlou

**Published:** 2026-10-08 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12016) | [PDF](https://arxiv.org/pdf/2610.12016)

<details>
<summary>Abstract</summary>

World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward. Generative world models such as Dreamer 4 consist of a video tokenizer, which encodes each frame into a latent, and a dynamics model, which is pretrained to predict future latents from past latents and actions. Yet the tokenizer is trained with a reconstruction objective, without action or reward supervision, so its latent provides no explicit mechanism to separate controllable, uncontrollable, reward-relevant, and reward-irrelevant information. We propose \te...

</details>

<details>
<summary>Share</summary>

```
CausalDreamer: Learning Predictive World Models with Latent Disentanglement

World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward.

arXiv: https://arxiv.org/abs/2610.12016

#worldmodels #robotics
```

</details>

---

### [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942)

**Authors:** Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu et al. (6 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11942) | [PDF](https://arxiv.org/pdf/2610.11942)

<details>
<summary>Abstract</summary>

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the observed screen requires a second model to judge the two. We argue that a world model meant for verificat...

</details>

<details>
<summary>Share</summary>

```
Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack.

arXiv: https://arxiv.org/abs/2610.11942

#worldmodels #robotics
```

</details>

---

### [What 30,000 Hours of Ego-centric Video Does Not Teach](https://arxiv.org/abs/2610.12464)

**Authors:** Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov et al. (10 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12464) | [PDF](https://arxiv.org/pdf/2610.12464)

<details>
<summary>Abstract</summary>

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains ne...

</details>

<details>
<summary>Share</summary>

```
What 30,000 Hours of Ego-centric Video Does Not Teach

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment.

arXiv: https://arxiv.org/abs/2610.12464

#worldmodels #robotics
```

</details>

---

### [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417)

**Authors:** Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang et al. (12 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12417) | [PDF](https://arxiv.org/pdf/2610.12417)

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a traini...

</details>

<details>
<summary>Share</summary>

```
WOVEN: Weaving Visual World Modeling into Multimodal LLMs

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning.

arXiv: https://arxiv.org/abs/2610.12417

#worldmodels #robotics
```

</details>

---

### [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](https://arxiv.org/abs/2610.11794)

**Authors:** Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.AI, cs.CL, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11794) | [PDF](https://arxiv.org/pdf/2610.11794)

<details>
<summary>Abstract</summary>

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects...

</details>

<details>
<summary>Share</summary>

```
Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives.

arXiv: https://arxiv.org/abs/2610.11794

#worldmodels #robotics
```

</details>

---
