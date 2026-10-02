# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-02 20:22 UTC

**Papers shown:** 136 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation](https://arxiv.org/abs/2609.39822)

**Authors:** Di Wu, Rongtian Shen, Ping Liu, Yan Shen, Zhenhan Yin et al. (11 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★★★

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39822) | [PDF](https://arxiv.org/pdf/2609.39822) | [Project Page](https://embodied.magiclab.top/works/inference/index.html) | [Code](https://github.com/MagiclabRobotics/Inference)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution. We characterize this gap through end-to-end latency measurements of model inference and the robot execution chain. Repeated Flow Matching denoising contributes substantially to inference cost, while robot-side delays mainly arise from perception acquisition, communication scheduling, and physical response. Analysis of the velocity field shows relatively stable magnitude and direction in early integration, followed by stronger directional correction near the terminal steps. Based on t...

</details>

<details>
<summary>Share</summary>

```
Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution.

arXiv: https://arxiv.org/abs/2609.39822
Project page: https://embodied.magiclab.top/works/inference/index.html
Code: https://github.com/MagiclabRobotics/Inference

#VLA #robotics
```

</details>

---

### [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)

**Authors:** Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding et al. (26 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39601) | [PDF](https://arxiv.org/pdf/2609.39601) | [Project Page](https://groundingpi.github.io/) | [Code](https://github.com/groundingpi/GroundingPI)

<details>
<summary>Abstract</summary>

Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding foundation model that generates points and boxes as quantized coordinates in a shared vocabulary. Training combines multimodal and spatial pretraining, supervised fine-tuning, and reinforce...

</details>

<details>
<summary>Share</summary>

```
GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

Precise grounding matters.

arXiv: https://arxiv.org/abs/2609.39601
Project page: https://groundingpi.github.io/
Code: https://github.com/groundingpi/GroundingPI

#VLA #robotics
```

</details>

---

### [ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection](https://arxiv.org/abs/2610.01741)

**Authors:** Yijie Zhu, Rui Shao, Jie He, Wei Li, Bo Zhao et al. (11 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01741) | [PDF](https://arxiv.org/pdf/2610.01741) | [Project Page](https://jiutian-vl.github.io/ATI-VLA-page/)

<details>
<summary>Abstract</summary>

Predictive Vision-Language-Action (VLA) models aim to improve robotic manipulation via future observation or world dynamics forecasting. However, existing approaches often fail to realize this potential and underperform direct action prediction models. We argue that these limitations stem from modality misalignment between observations and actions, together with joint optimization conflicts that drive learning away from an action-centric objective. To this end, we introduce ATI-VLA, an Action-Centric Predictive Vision-Language-Action framework via Actionable Alignment Then Adaptive Injection....

</details>

<details>
<summary>Share</summary>

```
ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection

Predictive Vision-Language-Action (VLA) models aim to improve robotic manipulation via future observation or world dynamics forecasting.

arXiv: https://arxiv.org/abs/2610.01741
Project page: https://jiutian-vl.github.io/ATI-VLA-page/

#VLA #robotics
```

</details>

---

### [Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies](https://arxiv.org/abs/2610.00982)

**Authors:** Xuehui Yu, Eason Yu, Meiyi Wang, Haozhe Du, Stefano V. Albrecht et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00982) | [PDF](https://arxiv.org/pdf/2610.00982) | [Project Page](https://dnr-memory.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models struggle on history-dependent manipulation tasks, where the current observation alone does not determine the action, and the policy needs a memory of the history. Existing memory methods decide what to remember by design, for example, keeping frames with large pixel changes, and show inconsistent gains across tasks. We view what to remember as an optimisation problem. From the POMDP formulation of imitation learning, we show that the optimal memory maximises the conditional mutual information $I(a_t; m_t \mid o_t)$ between the action and the memory given the...

</details>

<details>
<summary>Share</summary>

```
Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies

Vision-language-action (VLA) models struggle on history-dependent manipulation tasks, where the current observation alone does not determine the action, and the policy needs a memory of the history.

arXiv: https://arxiv.org/abs/2610.00982
Project page: https://dnr-memory.github.io/

#VLA #robotics
```

</details>

---

### [NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields](https://arxiv.org/abs/2610.00981)

**Authors:** Shota Kobayashi, Koki Seno, Daichi Yashima, Komei Sugiura

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00981) | [PDF](https://arxiv.org/pdf/2610.00981) | [Project Page](https://shota0520.github.io/NarrativeFlow-project-page/)

<details>
<summary>Abstract</summary>

We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation models remains limited by the labor-intensive collection of embodiment-specific data. Existing methods either coarsely approximate robot flows with sparse keypoint displacements, or cannot handle language-conditioned manipulation. To address...

</details>

<details>
<summary>Share</summary>

```
NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platfo...

arXiv: https://arxiv.org/abs/2610.00981
Project page: https://shota0520.github.io/NarrativeFlow-project-page/

#VLA #robotics
```

</details>

---

### [TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2610.00899)

**Authors:** Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryoichi Nakajo, Roman Mykhailyshyn et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00899) | [PDF](https://arxiv.org/pdf/2610.00899) | [Project Page](https://kskshr.github.io/toast/)

<details>
<summary>Abstract</summary>

Autoregressive Vision-Language-Action models often represent continuous robot actions as discrete token sequences, enabling action prediction with standard next-token objectives. FAST has substantially improved this representation by compactly encoding action containing diverse temporal frequencies into relatively few tokens. However, while such compression reduces the number of action tokens required for autoregressive prediction, it does not necessarily improve the efficiency of policy learning from limited demonstrations. In particular, FAST typically assigns a single deterministic tokeniza...

</details>

<details>
<summary>Share</summary>

```
TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models

Autoregressive Vision-Language-Action models often represent continuous robot actions as discrete token sequences, enabling action prediction with standard next-token objectives.

arXiv: https://arxiv.org/abs/2610.00899
Project page: https://kskshr.github.io/toast/

#VLA #robotics
```

</details>

---

### [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://arxiv.org/abs/2610.00604)

**Authors:** Egor Cherepanov, Nikita Kachaev, Aleksandr I. Panov, Alexey K. Kovalev

**Published:** 2026-09-30 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00604) | [PDF](https://arxiv.org/pdf/2610.00604) | [Project Page](https://mikasarobo.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task. We introduce MIKASA-Robo-VLA, a benchmark of 90 language-conditioned manipulation tasks. All but 10 hide the cue an action depends on. Those 10 are reactive controls. MIKASA-Robo, the suite it rebuilds, has 32 tasks and uses language only in a representative VLA subset. Here every task provides an instruction, while memory-dependent tasks hide a task-relevant cue and reactive controls keep it available. For 70 tasks, environment...

</details>

<details>
<summary>Share</summary>

```
MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation

Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task.

arXiv: https://arxiv.org/abs/2610.00604
Project page: https://mikasarobo.github.io/

#VLA #robotics
```

</details>

---

### [Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs](https://arxiv.org/abs/2610.00524)

**Authors:** Taegeun Yang, Youngju Na, Yoonki Cho, Sung-Eui Yoon

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00524) | [PDF](https://arxiv.org/pdf/2610.00524) | [Project Page](https://taegeunyang.github.io/craft/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models often struggle to generalize to skill combinations absent from their fine-tuning demonstrations, even when every constituent skill has been demonstrated. We focus on a vision shortcut as one failure mode: during fine-tuning, visual observations can serve as a proxy for the instruction, so a policy may execute a demonstrated combination associated with similar observations rather than the instructed combination. This motivates training with counterfactual pairs formed by holding a demonstration observation fixed while changing the instruction to specify an un...

</details>

<details>
<summary>Share</summary>

```
Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs

Vision-language-action (VLA) models often struggle to generalize to skill combinations absent from their fine-tuning demonstrations, even when every constituent skill has been demonstrated.

arXiv: https://arxiv.org/abs/2610.00524
Project page: https://taegeunyang.github.io/craft/

#VLA #robotics
```

</details>

---

### [Multi-Link Safety Filtering for VLA Policies Around Moving Hazards](https://arxiv.org/abs/2609.40007)

**Authors:** Yatharth Agarwal, Vijay Raghunathan

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.40007) | [PDF](https://arxiv.org/pdf/2609.40007) | [Project Page](https://yathag.github.io/multilink-safety-filter/)

<details>
<summary>Abstract</summary>

A vision-language-action (VLA) policy can finish a manipulation task while knocking over objects unrelated to it, so task success alone does not show that the policy is safe to deploy in clutter. We study how to keep a pretrained VLA policy clear of such hazards at run time without retraining it, which requires guarding more of the arm than the end effector, following the hazard as it moves, and sharing onboard compute with the policy. Our training-free shield covers the gripper, wrist, and forearm with five ellipsoids and filters every commanded motion through one barrier program against a ke...

</details>

<details>
<summary>Share</summary>

```
Multi-Link Safety Filtering for VLA Policies Around Moving Hazards

A vision-language-action (VLA) policy can finish a manipulation task while knocking over objects unrelated to it, so task success alone does not show that the policy is safe to deploy in clutter.

arXiv: https://arxiv.org/abs/2609.40007
Project page: https://yathag.github.io/multilink-safety-filter/

#VLA #robotics
```

</details>

---

### [MotionWeave: Learning Motion-Centered Future Dynamics for Vision-Language-Action Policies](https://arxiv.org/abs/2609.39324)

**Authors:** Jingqiu Wang, Yan Wang

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39324) | [PDF](https://arxiv.org/pdf/2609.39324) | [Code](https://github.com/autu-mn/MotionWeave)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently incorporated world models to provide richer dynamic supervision beyond sparse action labels. However, explicitly predicting future images or videos may include control-irrelevant appearance, while guidance derived from holistic future visual representations and shared global action features may fail to establish timestep-specific correspondence between actions and local visual changes. To address this issue, we propose MotionWeave, a motion-centric future-dynamics framework for action-chunk prediction with two modules: the Action-Induced Motion...

</details>

<details>
<summary>Share</summary>

```
MotionWeave: Learning Motion-Centered Future Dynamics for Vision-Language-Action Policies

Vision-Language-Action (VLA) models have recently incorporated world models to provide richer dynamic supervision beyond sparse action labels.

arXiv: https://arxiv.org/abs/2609.39324
Code: https://github.com/autu-mn/MotionWeave

#VLA #robotics
```

</details>

---

### [Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation](https://arxiv.org/abs/2609.38989)

**Authors:** Haoxuan Wang, Griffin Galimi, Junhua Huang, Selina Song, Wayne Wu et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38989) | [PDF](https://arxiv.org/pdf/2609.38989) | [Project Page](https://hatchetproject.github.io/delivery_steer/)

<details>
<summary>Abstract</summary>

Open-world goods delivery requires mobile manipulators to follow free-form user instructions and manipulate potentially novel objects. Existing dual-system approaches use high-level grounding models to convert language into grounded visual prompts, but their low-level controllers can remain brittle under noisy perception, dynamic scenes, and contact-rich interactions. We instead use a pretrained flow-matching vision-language-action model as the low-level control interface, leveraging its reactivity and robustness to environmental changes while treating the grounding output as a spatial cue for...

</details>

<details>
<summary>Share</summary>

```
Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation

Open-world goods delivery requires mobile manipulators to follow free-form user instructions and manipulate potentially novel objects.

arXiv: https://arxiv.org/abs/2609.38989
Project page: https://hatchetproject.github.io/delivery_steer/

#VLA #robotics
```

</details>

---

### [Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead](https://arxiv.org/abs/2609.37165)

**Authors:** Junghyun Kim, Ngseo Kim, ChungWoo Lee, Seoyeon Lee, Woo-Jeong Baek et al. (10 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37165) | [PDF](https://arxiv.org/pdf/2609.37165) | [Project Page](https://dill-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure. We propose Domain-Invariant Latent Lookahead (DILL), a representation-learning framework that mitigates shortcut learning in VLA policies. Our key idea is to supervise policies with domain-invariant future latents learned from domain-transformed trajectory data. A Task-Domain Encoder is trained with contrastive objectives and Gaussian disentanglement regularization to separate task-relevant structure fro...

</details>

<details>
<summary>Share</summary>

```
Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure.

arXiv: https://arxiv.org/abs/2609.37165
Project page: https://dill-vla.github.io/

#VLA #robotics
```

</details>

---

### [FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation](https://arxiv.org/abs/2609.36416)

**Authors:** Jade Choghari, Pepijn Kooijmans, Mansi Agarwal, Yusuf Umut Ciftci, Aseem Doriwala et al. (11 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36416) | [PDF](https://arxiv.org/pdf/2609.36416) | [Code](https://github.com/huggingface/lerobot)

<details>
<summary>Abstract</summary>

Robots operating in real-world environments must often execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions. Current manipulation datasets struggle to support this capability: although single-arm datasets reach hundreds of thousands of trajectories, they typically provide only one high-level instruction per episode, while existing bimanual datasets with subtask labels annotate only part of their recorded hours. We present FineART, a densely annotated bimanual manipulation dataset comprising 40,543 episodes (1,718 hours) and 533,913 subtasks across...

</details>

<details>
<summary>Share</summary>

```
FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation

Robots operating in real-world environments must often execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions.

arXiv: https://arxiv.org/abs/2609.36416
Code: https://github.com/huggingface/lerobot

#VLA #robotics
```

</details>

---

### [Learning to Act under Visual Interruptions with Vision-Language-Action Models](https://arxiv.org/abs/2609.35003)

**Authors:** Mingle Jiang, Rui Xu, Yunke Wang, Chang Xu

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.35003) | [PDF](https://arxiv.org/pdf/2609.35003) | [Project Page](https://minglejiang.github.io/Mail-Bench/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, but they are typically developed and evaluated with all camera streams available throughout task execution. When a camera stops delivering frames during task execution, the policy must continue acting without access to subsequent observations from the missing view. Despite its practical importance, how such interruptions affect closed-loop manipulation remains insufficiently understood. To investigate this problem, we introduce MAIL-Bench, a benchmark that evaluates visual interruptions with VLA...

</details>

<details>
<summary>Share</summary>

```
Learning to Act under Visual Interruptions with Vision-Language-Action Models

Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, but they are typically developed and evaluated with all camera streams available throughout task execution.

arXiv: https://arxiv.org/abs/2609.35003
Project page: https://minglejiang.github.io/Mail-Bench/

#VLA #robotics
```

</details>

---

### [RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2609.34384)

**Authors:** Aernaer Akelijiang, Jiannan Li, Zhineng Chen, Jingjing Chen, Bin Zhu

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34384) | [PDF](https://arxiv.org/pdf/2609.34384) | [Project Page](https://aernar.github.io/RoboIRGBench/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong capabilities in robotic manipulation, yet existing benchmarks typically assume that task-relevant information is explicitly specified in the instruction. In practice, however, humans frequently refer to objects, quantities, and relations implicitly, requiring robots to recover the intended target from linguistic and perceptual context. We study this capability as Implicit Referential Grounding (IRG) and introduce RoboIRG-Bench, a manipulation benchmark designed to systematically evaluate it. Built upon RoboMME, RoboIRG-Bench contains 40 var...

</details>

<details>
<summary>Share</summary>

```
RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models

Vision-Language-Action (VLA) models have shown strong capabilities in robotic manipulation, yet existing benchmarks typically assume that task-relevant information is explicitly specified in the instruction.

arXiv: https://arxiv.org/abs/2609.34384
Project page: https://aernar.github.io/RoboIRGBench/

#VLA #robotics
```

</details>

---

### [FailPatch: Failure Residual Patching for Vision-Language-Action Models](https://arxiv.org/abs/2609.34175)

**Authors:** Peng Yu, Jiacheng Wang, Ziheng Zhang, Xuchong Zhang, Baoting Li et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34175) | [PDF](https://arxiv.org/pdf/2609.34175) | [Code](https://github.com/yupeng-2003/FailPatch)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are typically adapted using successful demonstrations, which provide direct action supervision but rarely cover failure-prone states. Deployment failures expose these states, yet lack the corrective actions needed for conventional supervised learning. We propose FailPatch, a failure-driven residual patching framework that decouples action supervision from execution-reliability supervision. Successful demonstrations ground how the policy should act, while deployment trajectories indicate when its behavior becomes unreliable. We further observe that action h...

</details>

<details>
<summary>Share</summary>

```
FailPatch: Failure Residual Patching for Vision-Language-Action Models

Vision-Language-Action (VLA) policies are typically adapted using successful demonstrations, which provide direct action supervision but rarely cover failure-prone states.

arXiv: https://arxiv.org/abs/2609.34175
Code: https://github.com/yupeng-2003/FailPatch

#VLA #robotics
```

</details>

---

### [Quantile Head for Vision-Language-Action Models](https://arxiv.org/abs/2609.34061)

**Authors:** Xuan Wang, Yinan Wu, Haoran Duan, Jungong Han

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34061) | [PDF](https://arxiv.org/pdf/2609.34061) | [Code](https://github.com/xwangrs/Quantile-Head-for-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models integrate pretrained Vision-Language Models (VLMs) with action heads for robot control. Common action heads have distinct limitations: point regression provides only a point estimate of the action distribution, while standard flow-matching samplers require costly iterative sampling. To address these limitations, we unify regression and flow matching under a shared objective and extend it to derive a quantile objective. This quantile objective guides the design of our Quantile Head, which predicts a median and positive gaps to form ordered marginal action qua...

</details>

<details>
<summary>Share</summary>

```
Quantile Head for Vision-Language-Action Models

Vision-Language-Action (VLA) models integrate pretrained Vision-Language Models (VLMs) with action heads for robot control.

arXiv: https://arxiv.org/abs/2609.34061
Code: https://github.com/xwangrs/Quantile-Head-for-VLA

#VLA #robotics
```

</details>

---

### [SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models](https://arxiv.org/abs/2609.33575)

**Authors:** Tianfu Li, Haoxuan Xu, Wenbo Chen, Haitian Li, Changchuan Yang et al. (10 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.33575) | [PDF](https://arxiv.org/pdf/2609.33575) | [Project Page](https://haoxuanxu1024.github.io/SLIP_VLA/)

<details>
<summary>Abstract</summary>

Vision-Language-Action models are increasingly effective for robotic manipulation, yet most predict actions directly from current observations without explicitly modeling future scene evolution. Recent methods introduce future prediction to improve action generation, but dense future modeling often requires expensive iterative denoising, while one-step alternatives can underperform their multi-step counterparts. To reconcile efficient future modeling with strong action performance, we present SLIP-VLA, a policy learning framework that equips VLA models with a Single-Step Latent Imagination for...

</details>

<details>
<summary>Share</summary>

```
SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models

Vision-Language-Action models are increasingly effective for robotic manipulation, yet most predict actions directly from current observations without explicitly modeling future scene evolution.

arXiv: https://arxiv.org/abs/2609.33575
Project page: https://haoxuanxu1024.github.io/SLIP_VLA/

#VLA #robotics
```

</details>

---

### [VLALight: A Vision-Language-Action Model for Traffic Signal Control](https://arxiv.org/abs/2609.36934)

**Authors:** Pan Zhang, Siqi Lai, Kemu Dong, Hao Liu

**Published:** 2026-09-29 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36934) | [PDF](https://arxiv.org/pdf/2609.36934) | [Code](https://github.com/usail-hkust/VLALight.git)

<details>
<summary>Abstract</summary>

Traffic signal control (TSC) is essential for improving urban mobility and reducing congestion. Although roadside cameras are widely deployed at signalized intersections and provide rich visual observations of evolving traffic, existing TSC methods typically rely on manually engineered traffic states or separate perception modules, creating a gap between physical observations and control decisions. We present VLALight, the first vision-language-action (VLA) model for end-to-end traffic signal control from multi-view roadside videos. VLALight directly maps visual observations to coordinated sig...

</details>

<details>
<summary>Share</summary>

```
VLALight: A Vision-Language-Action Model for Traffic Signal Control

Traffic signal control (TSC) is essential for improving urban mobility and reducing congestion.

arXiv: https://arxiv.org/abs/2609.36934
Code: https://github.com/usail-hkust/VLALight.git

#VLA #robotics
```

</details>

---

### [ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control](https://arxiv.org/abs/2610.00801)

**Authors:** Yize Liu, Ke Wang, Mac Schwager, Yiqing Xu, Jiajun Wu

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00801) | [PDF](https://arxiv.org/pdf/2610.00801) | [Project Page](https://ecomem.github.io/)

<details>
<summary>Abstract</summary>

A robot may lose sight of an object it must later retrieve, need to recall what a person demonstrated earlier, or track which steps of a task it has already completed. Current vision-language-action (VLA) policies often fail once the information needed for action disappears from the current observation, making memory critical for long-horizon robot behavior. Existing approaches typically provide longer histories or learn implicit memory from observation-action trajectories. But action supervision tells a policy how to act, not what to remember: it does not specify which past facts should persi...

</details>

<details>
<summary>Share</summary>

```
ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control

A robot may lose sight of an object it must later retrieve, need to recall what a person demonstrated earlier, or track which steps of a task it has already completed.

arXiv: https://arxiv.org/abs/2610.00801
Project page: https://ecomem.github.io/

#VLA #robotics
```

</details>

---

### [Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models](https://arxiv.org/abs/2609.39820)

**Authors:** Mingyue Cui, Zheyuan Liu, Yihan Zhu, Zheyuan Zhang, Meng Jiang

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39820) | [PDF](https://arxiv.org/pdf/2609.39820)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only te...

</details>

<details>
<summary>Share</summary>

```
Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact.

arXiv: https://arxiv.org/abs/2609.39820

#VLA #robotics
```

</details>

---

### [Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model](https://arxiv.org/abs/2609.39794)

**Authors:** Zaijing Li, Rui Shao, Bing Hu, Haoyu Zhang, Dongmei Jiang et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39794) | [PDF](https://arxiv.org/pdf/2609.39794)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, yet adapting them to new tasks and domains remains inefficient: existing methods often rely on parameter tuning, incurring substantial costs and risking catastrophic forgetting of previously learned tasks. To address this, we propose \textbf{Optimus-R}, a memory-centric VLA framework that formulates robotic adaptation as explicit query-skill memory tuning. Optimus-R introduces: (i) An \textbf{Inline Memory Interface for skill extraction}. It inserts learnable memory tokens into the VLA prefi...

</details>

<details>
<summary>Share</summary>

```
Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model

Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, yet adapting them to new tasks and domains remains inefficient: existing methods often rely on parameter tuning,...

arXiv: https://arxiv.org/abs/2609.39794

#VLA #robotics
```

</details>

---

### [Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2609.39178)

**Authors:** Songhua Yang, Ziyu Liu, Yuanwei Liu, Xuetao Li, Xuanye Fei et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CR, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39178) | [PDF](https://arxiv.org/pdf/2609.39178)

<details>
<summary>Abstract</summary>

Recently, Vision-Language-Action (VLA) models have revolutionized robotic manipulation by seamlessly integrating visual perception, language understanding, and action generation in an end-to-end learning framework. However, since these models are designed to interact directly with the physical world and humans, their security is critical, and even small vulnerabilities can lead to catastrophic failures. In this work, we propose the Universal Adversarial Object, a sphere with optimized surface texture that significantly degrades task success rates when placed within the robot's field of view. S...

</details>

<details>
<summary>Share</summary>

```
Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics

Recently, Vision-Language-Action (VLA) models have revolutionized robotic manipulation by seamlessly integrating visual perception, language understanding, and action generation in an end-to-end learning framework.

arXiv: https://arxiv.org/abs/2609.39178

#VLA #robotics
```

</details>

---

### [Data-Efficient Adaptation of a Driving VLA to Class 8 Trucks](https://arxiv.org/abs/2609.38570)

**Authors:** Satyajeet Das, Aaron Buxbaum, Niels Joubert, Gaurav S. Sukhatme

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38570) | [PDF](https://arxiv.org/pdf/2609.38570) | [Project Page](https://truckvla.github.io)

<details>
<summary>Abstract</summary>

Class 8 trucks differ from passenger cars in geometry, dynamics, and maneuvering requirements. As a result, vision-language-action (VLA) models trained for passenger vehicles do not readily transfer to Class 8 trucks, particularly in unstructured scenarios such as accident scenes and construction zones. Rather than training a truck-driving VLA from scratch, we propose an adapt-then-steer strategy that adapts an off-the-shelf VLA to generate trajectories for Class-8 trucks in these challenging scenarios. In the adapt stage, we use NVIDIA's Alpamayo 1.5 as the base model, fine-tuning only its ac...

</details>

<details>
<summary>Share</summary>

```
Data-Efficient Adaptation of a Driving VLA to Class 8 Trucks

Class 8 trucks differ from passenger cars in geometry, dynamics, and maneuvering requirements.

arXiv: https://arxiv.org/abs/2609.38570
Project page: https://truckvla.github.io

#VLA #robotics
```

</details>

---

### [AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations](https://arxiv.org/abs/2609.36915)

**Authors:** Rui Huang, Yanlin Mu, Lidong Li, Yucong Wang, Zichen Yan et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36915) | [PDF](https://arxiv.org/pdf/2609.36915) | [Project Page](https://ruihuangnus.github.io/AeroManip-VLA-page/)

<details>
<summary>Abstract</summary>

Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation. However, extending Vision-Language-Action (VLA) models to aerial robots introduces distinct challenges due to the tight coupling between manipulation and flight, continuously changing observations, and safety-critical physical interactions. These challenges demand diverse training data and systematic policy evaluation, yet collecting demonstrations and evaluating policies directly on physical aerial platforms are c...

</details>

<details>
<summary>Share</summary>

```
AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations

Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2609.36915
Project page: https://ruihuangnus.github.io/AeroManip-VLA-page/

#VLA #robotics
```

</details>

---

### [StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks](https://arxiv.org/abs/2609.36352)

**Authors:** Ziyi Yin, Sangmin Woo, Kang Zhou, Sungyeon Kim, Aosong Feng et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36352) | [PDF](https://arxiv.org/pdf/2609.36352) | [Code](https://github.com/amazon-science/StructRL)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models perform well on shorter-horizon manipulation tasks but still struggle with long-horizon tasks that require multiple dependent manipulations from a single command. Online reinforcement learning (RL) can improve these policies through environment interaction, yet many existing methods provide reward only after the complete task succeeds. However, such terminal supervision is sparse and does not distinguish early failures from rollouts that make substantial partial progress. We propose StructRL, an online RL framework that constructs structured intermediate sup...

</details>

<details>
<summary>Share</summary>

```
StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks

Vision-language-action (VLA) models perform well on shorter-horizon manipulation tasks but still struggle with long-horizon tasks that require multiple dependent manipulations from a single command.

arXiv: https://arxiv.org/abs/2609.36352
Code: https://github.com/amazon-science/StructRL

#VLA #robotics
```

</details>

---

### [ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning](https://arxiv.org/abs/2609.34982)

**Authors:** Di Zhu, Ziheng Yan, Fang Wan

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34982) | [PDF](https://arxiv.org/pdf/2609.34982) | [Code](https://github.com/Di-Zhu123/ActionUNet)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown great promise for robotic manipulation by mapping multi-modal semantics to physical actions. However, this mapping inherently struggles to align these coarse-grained semantics with fine-grained temporal execution. It leaves VLA models with limited generalization and insufficient robustness in cluttered environments. To overcome this issue, we propose ActionUNet, an efficient multi-scale fine-tuning framework that enhances pre-trained VLA models with minimal computational cost. ActionUNet first constructs a lightweight temporal U-Net within the tem...

</details>

<details>
<summary>Share</summary>

```
ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning

Vision-Language-Action (VLA) models have shown great promise for robotic manipulation by mapping multi-modal semantics to physical actions.

arXiv: https://arxiv.org/abs/2609.34982
Code: https://github.com/Di-Zhu123/ActionUNet

#VLA #robotics
```

</details>

---

### [Don't Throw Away the Tail: Action Upcycling for Policy Acceleration](https://arxiv.org/abs/2609.34911)

**Authors:** Taesung Kwon, Jangho Park, Sunwoo Park, Youngmin Kim, Seonghyun Jin et al. (8 authors)

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34911) | [PDF](https://arxiv.org/pdf/2609.34911) | [Project Page](https://acupcycling.github.io/)

<details>
<summary>Abstract</summary>

Modern robot policies predict a chunk of future actions from a single observation, execute only a prefix, and discard the rest before replanning. Choosing the length of this prefix, the execution horizon, poses a trade-off between reactivity and efficiency. A short horizon keeps the policy reactive to the environment, but requires frequent policy calls. Recent test-time methods adaptively select the horizon for each chunk, but they either read model internals, where the signal must be chosen for each architecture, or draw extra samples, which adds cost. We propose Action Upcycling, a training-...

</details>

<details>
<summary>Share</summary>

```
Don't Throw Away the Tail: Action Upcycling for Policy Acceleration

Modern robot policies predict a chunk of future actions from a single observation, execute only a prefix, and discard the rest before replanning.

arXiv: https://arxiv.org/abs/2609.34911
Project page: https://acupcycling.github.io/

#VLA #robotics
```

</details>

---

### [GT-VLA: Target-Conditioned Trace Guidance for Generalizable Robotic Manipulation](https://arxiv.org/abs/2609.31904)

**Authors:** Ninghan Zhong, Jing-Chen Peng, Sriram Vishwanath

**Published:** 2026-09-25 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.31904) | [PDF](https://arxiv.org/pdf/2609.31904) | [Project Page](https://ivaniz.github.io/gt-vla/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong performance on robotic manipulation, but they often struggle to generalize to unseen tasks, configurations, and long-horizon settings. A key challenge is that VLAs overfit to training scenes and fail to follow novel language instructions. Off-the-shelf vision-language models (VLMs) often provide stronger generalization, but cannot directly control robot actions. To combine the common sense of VLMs with VLA control, we propose Guided Trace VLA (GT-VLA), a steerable framework that accepts guidance from an external generalist VLM through trace...

</details>

<details>
<summary>Share</summary>

```
GT-VLA: Target-Conditioned Trace Guidance for Generalizable Robotic Manipulation

Vision-Language-Action (VLA) models have shown strong performance on robotic manipulation, but they often struggle to generalize to unseen tasks, configurations, and long-horizon settings.

arXiv: https://arxiv.org/abs/2609.31904
Project page: https://ivaniz.github.io/gt-vla/

#VLA #robotics
```

</details>

---

### [CAR-VLA: Complexity-Aware and Risk-Adaptive Reasoning for Autonomous Driving](https://arxiv.org/abs/2609.34387)

**Authors:** Xiaolei Chen, Zhuolin He, Yuxuan Liang, Xu Li, Haotian Chen et al. (16 authors)

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34387) | [PDF](https://arxiv.org/pdf/2609.34387) | [Code](https://github.com/chenxl124578/CAR-VLA.git)

<details>
<summary>Abstract</summary>

Existing adaptive reasoning methods for driving Vision-Language-Action (VLA) models primarily focus on whether to reason, overlooking how reasoning should differ across driving situations. Our key insight is that while scene complexity informs reasoning depth, dynamic risk is equally critical for deciding how to reason in time-critical situations. We therefore propose CAR-VLA, a unified driving VLA model that jointly considers scene complexity and dynamic risk to guide reasoning depth, urgency, and focus. CAR-VLA maps four complexity--risk categories to three reasoning modes: \textit{Fast Intu...

</details>

<details>
<summary>Share</summary>

```
CAR-VLA: Complexity-Aware and Risk-Adaptive Reasoning for Autonomous Driving

Existing adaptive reasoning methods for driving Vision-Language-Action (VLA) models primarily focus on whether to reason, overlooking how reasoning should differ across driving situations.

arXiv: https://arxiv.org/abs/2609.34387
Code: https://github.com/chenxl124578/CAR-VLA.git

#VLA #robotics
```

</details>

---

### [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](https://arxiv.org/abs/2610.02161)

**Authors:** Hanchu Zhou, Dechen Gao, Hang Wang, Brendan Lynch, Boqi Zhao et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.02161) | [PDF](https://arxiv.org/pdf/2610.02161)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings. Extending these capabilities to multi-robot systems remains challenging because robots must coordinate long-horizon behaviors while maintaining reliable, fine-grained execution. We introduce DuoMind, a distributed hierarchical framework for multi-robot coordination through semantic communication. Each robot uses a VLA-based action model for low-level execution and a VLM-based orchestrator for high-level rea...

</details>

<details>
<summary>Share</summary>

```
DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication

Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings.

arXiv: https://arxiv.org/abs/2610.02161

#VLA #robotics
```

</details>

---

### [ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing](https://arxiv.org/abs/2610.01856)

**Authors:** Zhugang Liu, Kaichuang Zhang, Jinman Zhang, Pu Sun, Martha Asare et al. (10 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.01856) | [PDF](https://arxiv.org/pdf/2610.01856)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering new opportunities for automation in additive manufacturing (AM). However, deployment in AM remains challenging because adapting these models to unseen robot embodiments is costly, and performance can degrade under environment changes. In this work, we present a framework for deploying OpenVLA-OFT on a FAIRINO FR3 robot in a fixed AM workcell. A data pipeline converts monocular real-world demonstrations into OpenVLA-compatible TFDS/RLDS datasets to support adaptation to the FR3 e...

</details>

<details>
<summary>Share</summary>

```
ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing

Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering new opportunities for automation in additive manufacturing (AM).

arXiv: https://arxiv.org/abs/2610.01856

#VLA #robotics
```

</details>

---

### [Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors](https://arxiv.org/abs/2610.01794)

**Authors:** Edward W. Staley, Connor O. Pyles, Rahul Hingorani, Frank Camargo, Griffin Milsap et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.01794) | [PDF](https://arxiv.org/pdf/2610.01794)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models rely strongly on language for describing task information, despite having multimodal inputs. We hypothesize that other modalities in the state space may present opportunities for supplemental task conditioning, which may be particularly relevant in cluttered or otherwise ambiguous scenes. We introduce two tuned models to test this hypothesis: (1) an electrophysiology-conditioned VLA (EC-VLA) that incorporates 8-channel electromyography envelopes as continuous conditioning input concatenated to the proprioceptive vector, and (2) a visually-annotated VLA (VA-V...

</details>

<details>
<summary>Share</summary>

```
Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors

Vision-Language-Action (VLA) models rely strongly on language for describing task information, despite having multimodal inputs.

arXiv: https://arxiv.org/abs/2610.01794

#VLA #robotics
```

</details>

---

### [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351)

**Authors:** Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci, Alessandro Suglia

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.01351) | [PDF](https://arxiv.org/pdf/2610.01351)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks. More recently, there has been an emphasis on evaluating the robustness of VLA models to perturbations. However, this robustness is still predominantly measured through Task Success Rate (TSR). In this work, we propose a benchmark-agnostic evaluation framework to measure the behavioural robustness of models by characterising how successful trajectories are executed under perturbation. We implement this methodology by extending the widely-used LIBERO and LIBERO-Plus benchmarks. Across...

</details>

<details>
<summary>Share</summary>

```
Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks

Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks.

arXiv: https://arxiv.org/abs/2610.01351

#VLA #robotics
```

</details>

---

### [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](https://arxiv.org/abs/2610.01083)

**Authors:** Samuel Zhen, Siwon Jo, Yanze Zhang, Wenhao Luo

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.01083) | [PDF](https://arxiv.org/pdf/2610.01083)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have demonstrated impressive capabilities in generalizable robotic manipulation, but their deployment in the real world remains challenging due to potential collisions involving different parts of the robot, manipulated objects, and the surrounding environment. Existing inference-time VLA safety frameworks typically rely on simplified end-effector-centered representations that do not explicitly model the full articulated robot and attached-object geometry. In this paper, we present WBAG, a safety framework that models the robot's whole-body and grasp-depen...

</details>

<details>
<summary>Share</summary>

```
WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation

Vision-language-action (VLA) policies have demonstrated impressive capabilities in generalizable robotic manipulation, but their deployment in the real world remains challenging due to potential collisions involving d...

arXiv: https://arxiv.org/abs/2610.01083

#VLA #robotics
```

</details>

---

### [eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing](https://arxiv.org/abs/2610.00913)

**Authors:** Dehao Huang, Jianbang Liu, Jianpan Gao, Chao Tang, Zilang Cen et al. (10 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.00913) | [PDF](https://arxiv.org/pdf/2610.00913)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide strong behavioral priors for robotic manipulation, yet efficiently adapting them to downstream tasks remains challenging. Recent work addresses this challenge by adapting frozen VLAs through online reinforcement learning (RL), whose sample efficiency depends on the quality of the state representation used by the actor and critic. Existing methods construct such representations either with VLA-independent visual encoders or through fixed compression of internal VLA representations. Neither design explicitly extracts the task-specific action-relevant V...

</details>

<details>
<summary>Share</summary>

```
eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing

Vision-Language-Action (VLA) models provide strong behavioral priors for robotic manipulation, yet efficiently adapting them to downstream tasks remains challenging.

arXiv: https://arxiv.org/abs/2610.00913

#VLA #robotics
```

</details>

---

### [When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies](https://arxiv.org/abs/2610.00601)

**Authors:** Sathwik Karnik, Joseph JR. Lee, Aryaman Gupta, Somil Bansal

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.00601) | [PDF](https://arxiv.org/pdf/2610.00601)

<details>
<summary>Abstract</summary>

Reasoning-enabled VLA policies expose chain-of-thought (CoT) traces that appear to explain and guide their actions, creating a potential interface for runtime safety through reasoning monitoring and correction. In this work, we define and operationalize two evaluation axes for assessing when this interface can improve embodied behavior: correctability, which measures whether unreliable reasoning can be detected and improved during generation, and actionability, which measures whether reasoning corrections produce behaviorally meaningful changes in the intended direction. To enable correctabili...

</details>

<details>
<summary>Share</summary>

```
When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies

Reasoning-enabled VLA policies expose chain-of-thought (CoT) traces that appear to explain and guide their actions, creating a potential interface for runtime safety through reasoning monitoring and correction.

arXiv: https://arxiv.org/abs/2610.00601

#VLA #robotics
```

</details>

---

### [DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents](https://arxiv.org/abs/2609.40306)

**Authors:** Haoyuan Deng, Jiebin Liu, Tengxiao Zhang, Langning Yan, Hongye Cao et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.40306) | [PDF](https://arxiv.org/pdf/2609.40306) | [Project Page](https://denghaoyuan123.github.io/Dynaharness_page/)

<details>
<summary>Abstract</summary>

Pretrained robot policies provide useful action priors, but long-horizon manipulation still requires coordination between semantic reasoning and physical execution. Semantic reasoning operates at a coarser timescale than physical interaction, while episode-level failures provide limited guidance on which system component should be revised. We propose DynaHarness, a dynamic physical harness that couples semantic reasoning with physical governance through a shared execution contract and turns failure evidence into validated capability revisions. To be more specific, the slow brain proposes capab...

</details>

<details>
<summary>Share</summary>

```
DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents

Pretrained robot policies provide useful action priors, but long-horizon manipulation still requires coordination between semantic reasoning and physical execution.

arXiv: https://arxiv.org/abs/2609.40306
Project page: https://denghaoyuan123.github.io/Dynaharness_page/

#VLA #robotics
```

</details>

---

### [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](https://arxiv.org/abs/2609.39971)

**Authors:** Hung-Jen Chen, Yu-Hsun Hou, Yan-Hong Chen, Yan-Fu Chen, Binghua Cai et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39971) | [PDF](https://arxiv.org/pdf/2609.39971)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action. Aggregate robustness scores can therefore conceal a more specific failure, in which a policy responds to both language and vision yet does not combine them to select the action the task requires. We call this failure instruction-action binding. Instructions cue familiar trajectory families, and visual feedback adjusts their execution. Behavioral analyses of fine-tuned $π_{0.5}$...

</details>

<details>
<summary>Share</summary>

```
When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models

Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action.

arXiv: https://arxiv.org/abs/2609.39971

#VLA #robotics
```

</details>

---

### [From Local Whole-Body VLA Behaviors to Scene-Scale Aerial Manipulation](https://arxiv.org/abs/2609.39670)

**Authors:** Weixiang Guo, Rui Jin, Haotian Jin, Xinhang Xu, Ruiyang Liu et al. (10 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39670) | [PDF](https://arxiv.org/pdf/2609.39670)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable task-conditioned interaction, but extending them to scene-scale aerial manipulation remains challenging due to costly whole-body demonstrations, latency-induced action-state misalignment, and cross-site behavior composition. We present a unified framework for synthetic policy training and scene-scale execution on articulated uncrewed aerial manipulators (UAMs). A scene-reconfigurable pipeline synthesizes task-conditioned, kinodynamically feasible trajectories and synchronized multiview observations for VLA training without physical-platform demonstrat...

</details>

<details>
<summary>Share</summary>

```
From Local Whole-Body VLA Behaviors to Scene-Scale Aerial Manipulation

Vision-language-action (VLA) models enable task-conditioned interaction, but extending them to scene-scale aerial manipulation remains challenging due to costly whole-body demonstrations, latency-induced action-state...

arXiv: https://arxiv.org/abs/2609.39670

#VLA #robotics
```

</details>

---

### [DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction](https://arxiv.org/abs/2609.39198)

**Authors:** Wenhao Li, Xiu Su, Yu Han, Yichao Cao, Shan You et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39198) | [PDF](https://arxiv.org/pdf/2609.39198)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation). We identify three fundamental limitations hindering current VLAs in these scenarios: the \textbf{perception gap}, where static visual inputs lack temporal motion cues; the \textbf{latency gap}, where inference delays render actions obsolete; and the \textbf{control gap}, caused by the open-loop action chunk execution without real-time adjustment. In this work, we propose \textbf{DSDyn-VLA}, a Slow-Fast \textbf{D}ual-\textbf{S}tre...

</details>

<details>
<summary>Share</summary>

```
DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction

While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation).

arXiv: https://arxiv.org/abs/2609.39198

#VLA #robotics
```

</details>

---

### [Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults](https://arxiv.org/abs/2609.39145)

**Authors:** Heejae Suh, Jongwook Han, Zahra Gholami, Yohan Jo

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39145) | [PDF](https://arxiv.org/pdf/2609.39145)

<details>
<summary>Abstract</summary>

Unreliable visual inputs can harm task performance and cause potential physical safety risks for vision-language-action (VLA) models. We analyze how $π0.5$ and GR00T models act under input faults such as image blackouts and freezing. We find that blackout and freezing produce distinct physical failure modes even when task-success rates are similarly low: freezing causes more extreme joint behavior, whereas blackout after gripper closure can cause more object drops, most markedly without proprioception. Selective intervention studies reveal that proprioception (current robot state) partly compe...

</details>

<details>
<summary>Share</summary>

```
Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults

Unreliable visual inputs can harm task performance and cause potential physical safety risks for vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2609.39145

#VLA #robotics
```

</details>

---

### [Looking Back to Move Forward: Temporal Verification for Generative Robot Policies](https://arxiv.org/abs/2609.39038)

**Authors:** Haoxuan Wang, Wayne Wu, Yan Yan, Bolei Zhou

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39038) | [PDF](https://arxiv.org/pdf/2609.39038) | [Project Page](https://hatchetproject.github.io/tev/)

<details>
<summary>Abstract</summary>

Generative policies have emerged as a promising paradigm for robot learning, combining expressive generative action modeling with scalable imitation learning from large demonstration corpora. However, heterogeneous demonstrations can induce suboptimal action chunks whose errors compound over time, eventually driving the robot into out-of-distribution states from which recovery is difficult. Action verification offers a test-time scaling strategy for mitigating this failure mode by sampling multiple candidate actions and using a verifier to select one for execution. Existing approaches, however...

</details>

<details>
<summary>Share</summary>

```
Looking Back to Move Forward: Temporal Verification for Generative Robot Policies

Generative policies have emerged as a promising paradigm for robot learning, combining expressive generative action modeling with scalable imitation learning from large demonstration corpora.

arXiv: https://arxiv.org/abs/2609.39038
Project page: https://hatchetproject.github.io/tev/

#VLA #robotics
```

</details>

---

### [Online Evolution Strategy for Flow-Matching VLA Policies via Self-Supervised Trajectory Distribution Optimization](https://arxiv.org/abs/2609.38855)

**Authors:** Gongxin Yao, Yongsheng Zhao, Jiayin Deng, Deng Liang, Han Gao et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.38855) | [PDF](https://arxiv.org/pdf/2609.38855)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models based on generative frameworks, such as Flow Matching, have recently achieved impressive performance in robotic manipulation. Unlike deterministic policies, Flow Matching enables VLA models to learn conditional action trajectory distributions, where latent noise vectors induce different actions under the same task scenario. However, we observe that these distributions are often ill-formed, with successful and failed behaviors coexisting while considerable probability mass remains in unfavorable regions. To this end, we propose Online-ES, an online adaptation...

</details>

<details>
<summary>Share</summary>

```
Online Evolution Strategy for Flow-Matching VLA Policies via Self-Supervised Trajectory Distribution Optimization

Vision-Language-Action (VLA) models based on generative frameworks, such as Flow Matching, have recently achieved impressive performance in robotic manipulation.

arXiv: https://arxiv.org/abs/2609.38855

#VLA #robotics
```

</details>

---

### [EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation](https://arxiv.org/abs/2609.38046)

**Authors:** Yiming Jiang, Jin Chen, Chongyang Xu, Yilun Chen, Aimin Hao et al. (6 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38046) | [PDF](https://arxiv.org/pdf/2609.38046) | [Project Page](https://lambdahumanoid.github.io/EgoAlign/)

<details>
<summary>Abstract</summary>

Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose, continuous whole-body controller, without collecting physical-robot demonstrations. Using the target-robot model and simulator, EgoAlign guides demonstration collection through execution feedback. It preserves locomotion re...

</details>

<details>
<summary>Share</summary>

```
EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation

Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervis...

arXiv: https://arxiv.org/abs/2609.38046
Project page: https://lambdahumanoid.github.io/EgoAlign/

#VLA #robotics
```

</details>

---

### [Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance](https://arxiv.org/abs/2609.38616)

**Authors:** Yanyan Zhang, Disheng Liu, Xinpeng Li, Chaoda Song, Mohsen Hariri et al. (11 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38616) | [PDF](https://arxiv.org/pdf/2609.38616)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models enable flexible action generation, their generalization across diverse environmental elements, including manipulated objects, destinations, and backgrounds, is limited by the lack of diversity in robotic training data. Trained end-to-end on such data, VLAs tend to exploit visual shortcuts, associating actions with task-irrelevant visual features rather than the intended task semantics. These shortcuts block recomposition of elements already seen by the policy, that is, compositional generalization. Existing approaches mitigate such entanglement through...

</details>

<details>
<summary>Share</summary>

```
Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance

While Vision-Language-Action (VLA) models enable flexible action generation, their generalization across diverse environmental elements, including manipulated objects, destinations, and backgrounds, is limited by the...

arXiv: https://arxiv.org/abs/2609.38616

#VLA #robotics
```

</details>

---

### [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](https://arxiv.org/abs/2609.36588)

**Authors:** Ruixiao Xu, Wong Lik Hang Kenny, Zhiqian Liu, Jianing Guo, Hanxiao Li et al. (15 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36588) | [PDF](https://arxiv.org/pdf/2609.36588)

<details>
<summary>Abstract</summary>

We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models. This problem is challenging because VLAs are pretrained on large-scale single-agent data and therefore lack the fine-grained coordination skills required for inter-robot collaboration. Supervised fine-tuning (SFT) on multi-robot demonstrations partially bridges this gap, but its performance is bounded by the demonstration data and cannot improve from its own experience. We present a three-stage reinforced fine-tuning (RFT) pipeline for multi-agent VLAs. First, initialization-aware data...

</details>

<details>
<summary>Share</summary>

```
Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2609.36588

#VLA #robotics
```

</details>

---

### [RAVEL: Asynchronous Rolling Inference for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2609.34170)

**Authors:** Yuhan Chen, Ke Yu, Pengfei Liu, Shuxun Wang, Yi Yang et al. (6 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34170) | [PDF](https://arxiv.org/pdf/2609.34170)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models are highly effective for generalist robot manipulation, yet their reliance on computationally expensive VLM encoding and multi-step iterative action generation imposes a significant latency bottleneck. The resulting inference latency makes it difficult for robots to respond quickly, especially in dynamic environments. We address this limitation with RAVEL (Rolling Asynchronous VLA Enabling Low-Latency Control), an asynchronous inference framework that addresses the computational bottlenecks of both the VLM backbone and the action expert. To reduce...

</details>

<details>
<summary>Share</summary>

```
RAVEL: Asynchronous Rolling Inference for Flow-Based Vision-Language-Action Models

Flow-based vision-language-action (VLA) models are highly effective for generalist robot manipulation, yet their reliance on computationally expensive VLM encoding and multi-step iterative action generation imposes a...

arXiv: https://arxiv.org/abs/2609.34170

#VLA #robotics
```

</details>

---

### [TAO-DA: Towards Autonomous Operation--A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation](https://arxiv.org/abs/2609.33197)

**Authors:** Yongsheng Zhao, Han Gao, Baoping Cheng, Jingyao Tang, Dian Zhou et al. (10 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33197) | [PDF](https://arxiv.org/pdf/2609.33197)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a unified framework for grounding high-level semantic information into low-level robot actions, enabling scalable robotic manipulation across diverse tasks. However, existing VLA models lack explicit mechanisms to disentangle the states and intents of the two arms, leading to unintended cross-arm interference that degrades task execution success. To address this issue, we propose a symmetric Dual-Arm Expert (DAE) architecture built upon a shared Vision-Language Model (VLM) backbone with decoupled, arm-specific expert towers. Expert selection is carri...

</details>

<details>
<summary>Share</summary>

```
TAO-DA: Towards Autonomous Operation--A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation

Vision-Language-Action (VLA) models provide a unified framework for grounding high-level semantic information into low-level robot actions, enabling scalable robotic manipulation across diverse tasks.

arXiv: https://arxiv.org/abs/2609.33197

#VLA #robotics
```

</details>

---

### [Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement](https://arxiv.org/abs/2609.38216)

**Authors:** Pavel Bushuyeu, Yujin Chen, Anton Nikolaev, Brian Shu, Igor Molybog

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38216) | [PDF](https://arxiv.org/pdf/2609.38216) | [Project Page](https://fiatlux-bench.github.io)

<details>
<summary>Abstract</summary>

Existing benchmarks evaluate tabletop manipulation, flat-floor household activity, or humanoid locomotion and manipulation as separate task groups; none scores vertical mobility and dexterous work on a fragile payload in one long-horizon episode. We present Fiatlux, a light-bulb replacement benchmark built on NVIDIA Isaac Lab. In one episode, a Unitree G1 humanoid positions a step ladder under a ceiling or wall fixture, climbs it, exchanges a spent bulb in a socket for a fresh one, and leaves the spent one in a disposal crate. We decompose the episode into twelve subtask environments scored on...

</details>

<details>
<summary>Share</summary>

```
Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement

Existing benchmarks evaluate tabletop manipulation, flat-floor household activity, or humanoid locomotion and manipulation as separate task groups; none scores vertical mobility and dexterous work on a fragile payload...

arXiv: https://arxiv.org/abs/2609.38216
Project page: https://fiatlux-bench.github.io

#VLA #robotics
```

</details>

---

### [PF-RL: Progress Field Reinforcement Learning via Goal-Conditioned Value Geometry for Vision-Language-Action Models](https://arxiv.org/abs/2609.32634)

**Authors:** Yunpeng Qing, Yilun Kong, Sixu Lin, Ming Zhou, Yiming Fei et al. (12 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32634) | [PDF](https://arxiv.org/pdf/2609.32634)

<details>
<summary>Abstract</summary>

Reinforcement Fine-Tuning~(RFT) has emerged as a promising paradigm for improving Vision-Language-Action~(VLA) policies, yet sparse task-level outcomes provide limited credit for intermediate transitions, especially in long-horizon manipulation. A natural approach is to model intermediate task progress and use it as dense feedback for policy improvement. Despite their architectural differences, existing progress-aware methods commonly formulate task progress as an explicit scalar prediction, providing limited structure for modeling how intermediate observations relate to the task goal, which m...

</details>

<details>
<summary>Share</summary>

```
PF-RL: Progress Field Reinforcement Learning via Goal-Conditioned Value Geometry for Vision-Language-Action Models

Reinforcement Fine-Tuning~(RFT) has emerged as a promising paradigm for improving Vision-Language-Action~(VLA) policies, yet sparse task-level outcomes provide limited credit for intermediate transitions, especially i...

arXiv: https://arxiv.org/abs/2609.32634

#VLA #robotics
```

</details>

---

### [Are Vision-Language-Action Models Robust to One-Step Observation Perturbations?](https://arxiv.org/abs/2609.32550)

**Authors:** Shojiro Yamabe, Jun Sakuma

**Published:** 2026-09-26 | **Categories:** cs.AI, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32550) | [PDF](https://arxiv.org/pdf/2609.32550)

<details>
<summary>Abstract</summary>

Understanding the safety risks of vision-language-action (VLA) models is essential for their deployment in the physical world. Existing safety research has mainly considered persistent perturbations that are applied continuously to observations throughout an episode. However, momentary observation corruption, in which observations are severely perturbed only briefly within an episode, remains an underexplored safety threat. To address this gap, this work investigates robustness to one-step perturbations applied at a single time step per episode. Our experiments reveal that these perturbations...

</details>

<details>
<summary>Share</summary>

```
Are Vision-Language-Action Models Robust to One-Step Observation Perturbations?

Understanding the safety risks of vision-language-action (VLA) models is essential for their deployment in the physical world.

arXiv: https://arxiv.org/abs/2609.32550

#VLA #robotics
```

</details>

---

### [DS-VLA: A Dendritic-inspired Vision-Language-Action Model for Robust Action Control](https://arxiv.org/abs/2609.32253)

**Authors:** Yaxing Lyu, Jingyi Li, Mingkun Xu, Yujie Wu

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.AI, cs.NE | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32253) | [PDF](https://arxiv.org/pdf/2609.32253)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong performance in language-conditioned manipulation, yet success under nominal evaluation does not necessarily translate into robust closed-loop behavior when executed actions are transiently corrupted. We introduce DS-VLA, a dendritic-inspired action architecture that incorporates dendritic spiking dynamics into VLA control to address this limitation. Specifically, to enable modularized feature processing and temporal information integration, DS-VLA equips action neurons with multiple sparsely connected dendritic branches, each featuring h...

</details>

<details>
<summary>Share</summary>

```
DS-VLA: A Dendritic-inspired Vision-Language-Action Model for Robust Action Control

Vision-language-action (VLA) models have achieved strong performance in language-conditioned manipulation, yet success under nominal evaluation does not necessarily translate into robust closed-loop behavior when exec...

arXiv: https://arxiv.org/abs/2609.32253

#VLA #robotics
```

</details>

---

### [CausalDriveBench: Evaluating Causal Reasoning in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2609.32157)

**Authors:** Narendiran Chembu, Navvrat Rao, Shreedhar Shreeshail Kodate, Gayatri Srujana Banda, Arko Sarkar et al. (13 authors)

**Published:** 2026-09-26 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32157) | [PDF](https://arxiv.org/pdf/2609.32157)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models for autonomous driving produce natural-language reasoning alongside predicted trajectories, but whether this reasoning reflects the causal structure of the scene remains untested. We introduce CausalDriveBench, an evaluation framework grounded in Pearl's Causal Hierarchy (PCH) that tests causal reasoning in driving-specific VLAs through structured visual question answering (QA) and alternative-trajectory prediction. To this end, we construct causal scene graphs over nuScenes that distinguish causally active, dormant, and distractor entities, separating perce...

</details>

<details>
<summary>Share</summary>

```
CausalDriveBench: Evaluating Causal Reasoning in Vision-Language-Action Models for Autonomous Driving

Vision-Language-Action (VLA) models for autonomous driving produce natural-language reasoning alongside predicted trajectories, but whether this reasoning reflects the causal structure of the scene remains untested.

arXiv: https://arxiv.org/abs/2609.32157

#VLA #robotics
```

</details>

---

### [SAMBAR: Selective Anchoring via Method of Multipliers for Balanced Knowledge Acquisition and Retention in Vision-Language-Action Models](https://arxiv.org/abs/2609.32108)

**Authors:** Aayushi Shrivastava, Xunlan Zhou, Hongrui Zhao, Ziyu Chen, Negar Mehr

**Published:** 2026-09-26 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32108) | [PDF](https://arxiv.org/pdf/2609.32108)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models leverage large-scale pretraining to ultimately achieve generalist manipulation. Deployed VLA policies must support continual learning to acquire new tasks over time. Teaching a VLA a new task generally requires finetuning it on demonstrations of that task. However, naively finetuning on downstream tasks causes the policy to forget earlier tasks and degrades generalist capabilities. This failure is known as catastrophic forgetting. Most continual learning methods counter it by replaying data from earlier tasks. However, the old task demonstrations are not alw...

</details>

<details>
<summary>Share</summary>

```
SAMBAR: Selective Anchoring via Method of Multipliers for Balanced Knowledge Acquisition and Retention in Vision-Language-Action Models

Vision-Language-Action (VLA) models leverage large-scale pretraining to ultimately achieve generalist manipulation.

arXiv: https://arxiv.org/abs/2609.32108

#VLA #robotics
```

</details>

---

### [Towards VLA-Dreamer: Refining VLA Behavior Using World Models](https://arxiv.org/abs/2609.31313)

**Authors:** Parsa Mastouri Kashani, Jan-Gerrit Habekost, Stefan Wermter

**Published:** 2026-09-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2609.31313) | [PDF](https://arxiv.org/pdf/2609.31313)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data. Moreover, the absence of an explicit world model casts further doubt on their control capabilities. In this concept paper, we propose a novel architecture that addresses sample efficiency in VLAs by training a predictive world model on the embedding space of the VLA's vision encoder. We hypothesize that these embeddings are action-relevant and usable for future prediction. To this end, we propose using the suggested architecture to investigate...

</details>

<details>
<summary>Share</summary>

```
Towards VLA-Dreamer: Refining VLA Behavior Using World Models

Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data.

arXiv: https://arxiv.org/abs/2609.31313

#VLA #robotics
```

</details>

---

### [VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL](https://arxiv.org/abs/2609.30868)

**Authors:** Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30868) | [PDF](https://arxiv.org/pdf/2609.30868)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction. Residual reinforcement learning (RL) can correct such errors while keeping the VLA frozen, but real-robot RL is costly and safety-critical. We propose VLA Latent-Conditioned RL (VLaRL), which enables residual RL for frozen VLAs to be trained in simulation and deployed on real robots without real-world RL or online adaptation. The key challenge is transferring the learned residual policy despite the visual gap betwe...

</details>

<details>
<summary>Share</summary>

```
VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction.

arXiv: https://arxiv.org/abs/2609.30868

#VLA #robotics
```

</details>

---

### [Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2609.30833)

**Authors:** Chuanliang Xie, Boyu Ma, Gen Li, Yizhou Liu, Houwang Chen et al. (7 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30833) | [PDF](https://arxiv.org/pdf/2609.30833)

<details>
<summary>Abstract</summary>

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions. This hierarchical design has practical value only if the planner can generate plans fast enough to meet real-time control requirements, and the resulting plans actually contribute to the generation of action. We study one such system, a waypoint hierarchy pipeline adapted from $π_{0.5}$, and find that neither requirement is satisfied. This baseline relies on token-level autoregressive decoding (Token-AR) to generate a waypoint plan,...

</details>

<details>
<summary>Share</summary>

```
Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions.

arXiv: https://arxiv.org/abs/2609.30833

#VLA #robotics
```

</details>

---

### [ConflictVLA-Bench: Benchmarking Behavioral Responses of Vision-Language-Action Models to Premise Conflicts](https://arxiv.org/abs/2609.31792)

**Authors:** Liyu Hou, Yuan Wu, Yi Chang

**Published:** 2026-09-25 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.31792) | [PDF](https://arxiv.org/pdf/2609.31792)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models perform strongly on manipulation tasks, their responses to invalid task premises remain underexplored. Existing evaluations of premise conflicts often focus on terminal task outcomes, yet task failure alone cannot distinguish behavioral disengagement from continued pursuit followed by an execution error. We call the latter pattern Failed Persistence. To study this phenomenon, we introduce ConflictVLA-Bench, which pairs conflict rollouts with premise-consistent reference rollouts and evaluates both outcomes and execution processes. Built on LIBERO, the...

</details>

<details>
<summary>Share</summary>

```
ConflictVLA-Bench: Benchmarking Behavioral Responses of Vision-Language-Action Models to Premise Conflicts

While Vision-Language-Action (VLA) models perform strongly on manipulation tasks, their responses to invalid task premises remain underexplored.

arXiv: https://arxiv.org/abs/2609.31792

#VLA #robotics
```

</details>

---

### [WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325)

**Authors:** Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.40325) | [PDF](https://arxiv.org/pdf/2609.40325)

<details>
<summary>Abstract</summary>

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close coupling of two distinct capabilities: action, to navigate the 3D world and search for anomalies system...

</details>

<details>
<summary>Share</summary>

```
WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, tr...

arXiv: https://arxiv.org/abs/2609.40325

#VLA #robotics
```

</details>

---

### [D$^2$-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation](https://arxiv.org/abs/2609.34792)

**Authors:** Zijian Ye, Chengqi Wei, Wei Huang, Anlin Zheng, Chunyu Zou et al. (12 authors)

**Published:** 2026-09-28 (updated 2026-09-30) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34792) | [PDF](https://arxiv.org/pdf/2609.34792)

<details>
<summary>Abstract</summary>

Long-horizon manipulation requires robots to remember cues that are no longer in view while responding to moving objects. Yet vision-language-action (VLA) policies often rely on the latest observation, and refreshing their visual context typically requires another costly vision-language model (VLM) pass. We present D$^2$-VLA, which combines dual memory and dual-frequency control at the KV-cache interface of a pretrained VLA. D$^2$-VLA uses block-wise causal KV caching to encode observations incrementally and, guided by distinct temporal attention patterns, constructs separate historical KV rea...

</details>

<details>
<summary>Share</summary>

```
D$^2$-VLA: Dual-Memory Dual-Frequency Vision-Language-Action Model For Long Dynamic Manipulation

Long-horizon manipulation requires robots to remember cues that are no longer in view while responding to moving objects.

arXiv: https://arxiv.org/abs/2609.34792

#VLA #robotics
```

</details>

---

### [The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996)

**Authors:** Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto, SooJean Han

**Published:** 2026-09-25 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30996) | [PDF](https://arxiv.org/pdf/2609.30996)

<details>
<summary>Abstract</summary>

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an additional challenge. Unlike semantic attributes commonly studied in LLMs, such as gender or language, a physical quantity of interest (QoI) in a VLA evolves jointly with the system dynamics: the representation influences the actions selected...

</details>

<details>
<summary>Share</summary>

```
The Linear Representation Hypothesis for Vision-Language-Action Models

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs).

arXiv: https://arxiv.org/abs/2609.30996

#VLA #robotics
```

</details>

---

### [UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054)

**Authors:** Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong et al. (16 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.02054) | [PDF](https://arxiv.org/pdf/2610.02054)

<details>
<summary>Abstract</summary>

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified architecture that integrates a physical reasoner, a world generator, and an action predictor to jointly learn semantic understanding of the physical world, visual generation, and action predi...

</details>

<details>
<summary>Share</summary>

```
UniWAM: Unified World-Action Model

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics.

arXiv: https://arxiv.org/abs/2610.02054

#VLA #robotics
```

</details>

---

### [Tactile Curiosity Drives Robot Interaction](https://arxiv.org/abs/2609.40134)

**Authors:** Klemens Iten, Alexander Proshkin, Bhavya Sukhija, Stelian Coros, Andreas Krause et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.40134) | [PDF](https://arxiv.org/pdf/2609.40134)

<details>
<summary>Abstract</summary>

Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient. The most common RL algorithms rely on random action sampling to discover new strategies, resulting in agents that allocate most of their training budget to motions in free space, away from the contacts from which manipulation skills emerge. Existing intrinsic motivation methods based on model disagreement or epistemic uncertainty improve on isotropic noise, but they can also reward uncertainty in functionally irrelevant transitions, such as erratic motions in free space. In this work, we arg...

</details>

<details>
<summary>Share</summary>

```
Tactile Curiosity Drives Robot Interaction

Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient.

arXiv: https://arxiv.org/abs/2609.40134

#VLA #robotics
```

</details>

---

### [Discrete Forcing: Infusing Discrete Guidance into Continuous Denoising for Few-Step Action Experts](https://arxiv.org/abs/2609.39526)

**Authors:** Jingbo Wang, Wenxuan Song, Wenhao Yu, Han Zhao, Xi Wang et al. (9 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.39526) | [PDF](https://arxiv.org/pdf/2609.39526)

<details>
<summary>Abstract</summary>

Efficient action generation in vision-language-action (VLA) models requires capturing both coarse action structure and fine-grained details. Discrete action tokens provide compact structural representations but sacrifice precision, while continuous action tokens offer high precision but often require multiple denoising steps. We introduce Discrete Forcing, a flow-matching framework that combines these representations through an explicit coarse-to-fine generation process. It first predicts discrete action tokens to establish a coarse action structure, then uses them to guide continuous action r...

</details>

<details>
<summary>Share</summary>

```
Discrete Forcing: Infusing Discrete Guidance into Continuous Denoising for Few-Step Action Experts

Efficient action generation in vision-language-action (VLA) models requires capturing both coarse action structure and fine-grained details.

arXiv: https://arxiv.org/abs/2609.39526

#VLA #robotics
```

</details>

---

### [Vision-Language-Action Autonomous Driving Agent with Language-based Memory](https://arxiv.org/abs/2609.38641)

**Authors:** Kai Yan, Xiangyu Chen, Yulong Cao, Alex Naumann, Peter Karkus et al. (12 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38641) | [PDF](https://arxiv.org/pdf/2609.38641)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate and interpretable driving. However, VLAs can take only a limited number of frames as visual input due to the high token cost of an image, which is problematic for memory-dependent tasks such as determining the arrival order at all-way stops and long-horizon driving scene understanding. Existing solutions use latent vector memories accessed through cross-attention, which are neither...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Action Autonomous Driving Agent with Language-based Memory

Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate an...

arXiv: https://arxiv.org/abs/2609.38641

#VLA #robotics
```

</details>

---

### [Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control](https://arxiv.org/abs/2609.37772)

**Authors:** Zibo Wang, Haochen Han, Pengzhen Ren, Mingtong Dai, Fangming Liu

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37772) | [PDF](https://arxiv.org/pdf/2609.37772)

<details>
<summary>Abstract</summary>

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control. Existing acceleration methods treat an action chunk as a monolithic computational unit, ignoring a crucial physical reality of receding-horizon control: actions are generated jointly but consumed sequentially, resulting in inherently heterogeneous execution urgencies. We exploit this asymmetry to introduce Urgency-Aware Denoising (UAD), a novel inference-time framework that allocates denoisi...

</details>

<details>
<summary>Share</summary>

```
Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control.

arXiv: https://arxiv.org/abs/2609.37772

#VLA #robotics
```

</details>

---

### [Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration](https://arxiv.org/abs/2609.37771)

**Authors:** Qiwei Chen, Kaijun Zhou, Nuohui Shi, Zhiyang Li, Yuxuan Feng et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37771) | [PDF](https://arxiv.org/pdf/2609.37771)

<details>
<summary>Abstract</summary>

Simulated manipulation benchmarks are the standard tool for evaluating vision-language-action (VLA) policies and the acceleration methods that reduce their inference latency for on-robot deployment. On these benchmarks, we observe that some training-free acceleration methods, which approximate the baseline policy's computation, achieve higher measured success rates than the baseline itself. Success rates alone cannot establish whether such gains come from better task execution or from evaluation flaws. We therefore investigate two kinds of benchmark flaws behind these gains: bugs, where the im...

</details>

<details>
<summary>Share</summary>

```
Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration

Simulated manipulation benchmarks are the standard tool for evaluating vision-language-action (VLA) policies and the acceleration methods that reduce their inference latency for on-robot deployment.

arXiv: https://arxiv.org/abs/2609.37771

#VLA #robotics
```

</details>

---

### [Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing](https://arxiv.org/abs/2609.37334)

**Authors:** Sohyun Lee, Yoonjae Baek, Jaesang Won, Jinnyeong Kim, Kang Hyunwoo et al. (8 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37334) | [PDF](https://arxiv.org/pdf/2609.37334)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action. Such execution errors arise from the robot's mechanics and operating conditions, such as wear and payload changes. We propose self-compensating VLA, a deployment-time adaptation method that enables a VLA policy to pre-compensate for the robot's execution errors when generating commands. Without task rewards or labels, it updates the policy online using the residual between the action commanded by a VLA and the motion executed by the robot. To stress-test VLA robustness across e...

</details>

<details>
<summary>Share</summary>

```
Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action.

arXiv: https://arxiv.org/abs/2609.37334

#VLA #robotics
```

</details>

---

### [Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2609.37307)

**Authors:** Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37307) | [PDF](https://arxiv.org/pdf/2609.37307)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks. However, many existing VLAs lack explicit access to interaction history, making them vulnerable to perceptual aliasing: similar current observations and robot states at different task stages may induce action ambiguity and lower success rate. Existing methods incorporate temporal or progress cues through feature conditioning, action-prior modification, or sampling guidance. However, methods that jointly fine-tune memo...

</details>

<details>
<summary>Share</summary>

```
Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks.

arXiv: https://arxiv.org/abs/2609.37307

#VLA #robotics
```

</details>

---

### [Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2609.36967)

**Authors:** Jiayu Chen, Shuyong Gao, Jingkai Jia, Xiaosheng Bu, Jiyuan Fu et al. (9 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36967) | [PDF](https://arxiv.org/pdf/2609.36967)

<details>
<summary>Abstract</summary>

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a purely geometric pruning strategy. Surprisingly, Stride outperforms semantic pruning and random pruning at certain pruning ratios, but collapses when the token budget is only slightly reduced. We characterize this phenomenon through the spat...

</details>

<details>
<summary>Share</summary>

```
Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation.

arXiv: https://arxiv.org/abs/2609.36967

#VLA #robotics
```

</details>

---

### [Where Predictive Supervision Goes Shapes What VLA Policies Learn](https://arxiv.org/abs/2609.36645)

**Authors:** Hanseul Kim, Jewon Yeom, Youngjoon Jeong, Minsoo Jo, Taesup Kim

**Published:** 2026-09-29 (updated 2026-10-01) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36645) | [PDF](https://arxiv.org/pdf/2609.36645)

<details>
<summary>Abstract</summary>

Future prediction is increasingly used to improve vision-language-action (VLA) policies, based on the premise that anticipating scene evolution encourages representations useful for control. However, forecast quality alone does not establish that a policy has learned a better representation for action. This distinction matters under distribution shift, where successful control depends on preserving spatial state and likely scene change beyond familiar configurations. We study what determines whether predictive supervision improves the visual representation used by a VLA policy. Through control...

</details>

<details>
<summary>Share</summary>

```
Where Predictive Supervision Goes Shapes What VLA Policies Learn

Future prediction is increasingly used to improve vision-language-action (VLA) policies, based on the premise that anticipating scene evolution encourages representations useful for control.

arXiv: https://arxiv.org/abs/2609.36645

#VLA #robotics
```

</details>

---

### [DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies](https://arxiv.org/abs/2610.00317)

**Authors:** Youngjun Jun, Kyumin Choi, Youngmin Kim, Seonghyun Jin, Sunwoo Park et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.00317) | [PDF](https://arxiv.org/pdf/2610.00317)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models increasingly rely on action experts that generate short action chunks under receding-horizon control. While chunk-level training is convenient across robot embodiments, it optimizes local action likelihood without explicitly accounting for long-horizon task success. Sequence-level reinforcement learning can address this limitation, but typically requires policy rollouts and closed-loop interaction, which are costly for real-robot manipulation. We introduce DriftOPD, a teacher-free, rollout-free framework for sequence-level on-policy distillation of continuou...

</details>

<details>
<summary>Share</summary>

```
DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies

Vision-Language-Action (VLA) models increasingly rely on action experts that generate short action chunks under receding-horizon control.

arXiv: https://arxiv.org/abs/2610.00317

#VLA #robotics
```

</details>

---

### [Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment](https://arxiv.org/abs/2609.36540)

**Authors:** Moritz Zoellner, Reece O'Mahoney, Ioannis Havoutis, Rohan Paleja

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36540) | [PDF](https://arxiv.org/pdf/2609.36540)

<details>
<summary>Abstract</summary>

Generalist robot policies such as vision-language-action models (VLAs) have achieved remarkable generalization, but their inference delays can conflict with the demands of real-time control. Asynchronous execution avoids pauses between action chunks by predicting the next sequence of actions while the robot carries out the previous one. In this paper, we study whether asynchronous execution produces the same action distribution as the original VLA. We find that, for non-Markovian demonstrations, asynchronous execution can produce a fundamentally different action distribution, which can limit t...

</details>

<details>
<summary>Share</summary>

```
Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment

Generalist robot policies such as vision-language-action models (VLAs) have achieved remarkable generalization, but their inference delays can conflict with the demands of real-time control.

arXiv: https://arxiv.org/abs/2609.36540

#VLA #robotics
```

</details>

---

### [LIBERO-MAX: Do Robot Policies Adapt When the World Changes?](https://arxiv.org/abs/2609.36518)

**Authors:** Yunbei Zhang, Zijian Jin, Yuanzhe Liu, Janet Wang, Xilun Zhang et al. (17 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36518) | [PDF](https://arxiv.org/pdf/2609.36518) | [Project Page](https://liberomax.github.io)

<details>
<summary>Abstract</summary>

Robots must often continue a task after a target moves, the viewpoint shifts, or an obstacle appears, even though their earlier observations and committed actions reflect the previous scene. Many simulation robustness benchmarks fix external conditions at reset, leaving this temporal challenge underexamined. We introduce LIBERO-MAX, a benchmark of 8,000 paired cases spanning eight types of changes to geometry, observations, appearance, clutter, and paths. Each pair compares task execution with and without a mid-task event, holding the task, initial state, policy seed, and pre-event action sequ...

</details>

<details>
<summary>Share</summary>

```
LIBERO-MAX: Do Robot Policies Adapt When the World Changes?

Robots must often continue a task after a target moves, the viewpoint shifts, or an obstacle appears, even though their earlier observations and committed actions reflect the previous scene.

arXiv: https://arxiv.org/abs/2609.36518
Project page: https://liberomax.github.io

#VLA #robotics
```

</details>

---

### [V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents](https://arxiv.org/abs/2609.37250)

**Authors:** Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Jiayu Hu, Xiu Yuan et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37250) | [PDF](https://arxiv.org/pdf/2609.37250) | [Code](https://github.com/breez3young/VJEPA-Policy)

<details>
<summary>Abstract</summary>

World-action models (WAMs) couple future visual-state prediction with action generation. By adapting video generators or image-editing models pretrained at scale, a prominent line of recent WAMs inherits both predictive knowledge and the models in which it was learned. We ask whether a predictive visual latent space induced by large-scale predictive pretraining can instead provide a sufficient foundation for effective WAM learning without inheriting a complete pretrained visual generative model. To answer this question, we introduce V-JEPA Policy, a simple framework that builds a WAM on the la...

</details>

<details>
<summary>Share</summary>

```
V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents

World-action models (WAMs) couple future visual-state prediction with action generation.

arXiv: https://arxiv.org/abs/2609.37250
Code: https://github.com/breez3young/VJEPA-Policy

#VLA #robotics
```

</details>

---

### [T$^2$Mem: Learning Test-Time Memory for Robotics](https://arxiv.org/abs/2609.36720)

**Authors:** Yize Liu, Huang Huang, Yining Hong, Zijian Du, Zhi Cao et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36720) | [PDF](https://arxiv.org/pdf/2609.36720) | [Project Page](https://yzliu84.github.io/T2MEM-project/)

<details>
<summary>Abstract</summary>

Memory-dependent robotic manipulation requires policies to use information that is no longer available in the current observation. Retaining history alone is insufficient: memory must preserve information that supports future actions. One challenge is whether a memory-free foundation model can learn to retain and use historical information from action demonstrations alone, without external memory support. We introduce T$^2$Mem, a framework that develops this capability within a pretrained vision-language-action policy, without external reasoning models or memory-specific annotations. T$^2$Mem...

</details>

<details>
<summary>Share</summary>

```
T$^2$Mem: Learning Test-Time Memory for Robotics

Memory-dependent robotic manipulation requires policies to use information that is no longer available in the current observation.

arXiv: https://arxiv.org/abs/2609.36720
Project page: https://yzliu84.github.io/T2MEM-project/

#VLA #robotics
```

</details>

---

### [Humanoid Loco-Manipulation With Discrete VLA Model](https://arxiv.org/abs/2609.35709)

**Authors:** Wenxin Shao, Siqi Chai, Kun Li, Kerou Zhang, Xinzhou Jiang et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35709) | [PDF](https://arxiv.org/pdf/2609.35709)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do not address. We present Holo-M, to our knowledge the first discrete VLA model for humanoid loco-manipulation that intrinsically exploits the language model by extending its vocabulary with action tokens. In this model, we devise a...

</details>

<details>
<summary>Share</summary>

```
Humanoid Loco-Manipulation With Discrete VLA Model

Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on manipulation tasks.

arXiv: https://arxiv.org/abs/2609.35709

#VLA #robotics
```

</details>

---

### [Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.35450)

**Authors:** Zihao Wang, Shutong Liu, Siqi Zheng, Liu Cao, Ruoqu Chen et al. (8 authors)

**Published:** 2026-09-28 (updated 2026-09-30) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35450) | [PDF](https://arxiv.org/pdf/2609.35450)

<details>
<summary>Abstract</summary>

Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception alone are often insufficient to characterize physical interaction, especially when the contact region is occluded. Unlike sparse force or torque measurements at predefined regions, distributed tactile sensing preserves spatially resolved contact patterns across the robot body. We therefore study how to integrate such whole-body tactile information into vision-language-action (VLA) policies for contact-rich control. Our approach, Uni-VLaT, introduces a tactile pathway whose la...

</details>

<details>
<summary>Share</summary>

```
Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation

Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception alone are often insufficient to characterize physical interaction, especially when the contact re...

arXiv: https://arxiv.org/abs/2609.35450

#VLA #robotics
```

</details>

---

### [Spatial Grafting: Grounding 3D Features for Flow-Matching Robot Policies](https://arxiv.org/abs/2609.35249)

**Authors:** Dingsheng Liu, Yangzheng Wu, Mahboubeh Asadi, Zhiyuan Li, Jinbang Huang et al. (8 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35249) | [PDF](https://arxiv.org/pdf/2609.35249)

<details>
<summary>Abstract</summary>

Pretrained robot manipulation policies such as vision-language-action models (VLAs) or world-action models (WAMs) leave interaction-relevant metric geometry implicit. Recent breakthroughs in spatial reconstruction can supply the necessary geometry reliably, but their features describe local shape without stating where it lies with respect to the robot. How best to deliver these features to a pretrained policy remains unresolved. We propose Spatial Grafting, a versatile, lightweight spatial module that binds frozen reconstruction features to metric, robot-relative geometry. Spatial Grafting con...

</details>

<details>
<summary>Share</summary>

```
Spatial Grafting: Grounding 3D Features for Flow-Matching Robot Policies

Pretrained robot manipulation policies such as vision-language-action models (VLAs) or world-action models (WAMs) leave interaction-relevant metric geometry implicit.

arXiv: https://arxiv.org/abs/2609.35249

#VLA #robotics
```

</details>

---

### [Do Not Cut When Uncertain: Rejectable and Calibrated Decision Heads for VLA Policies in Robotic Harvesting](https://arxiv.org/abs/2609.35039)

**Authors:** Heng Zhang

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35039) | [PDF](https://arxiv.org/pdf/2609.35039)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies trained with behavior cloning or flow matching are optimized to output an action trajectory, but they cannot express "I don't know" or "I should not act." In robotic harvesting, occlusion makes single-frame decisions fundamentally ambiguous: identical pixels can correspond either to a cuttable stem or to no stem at all. Existing VLAs are forced to commit, leading to high-confidence errors with irreversible consequences. We argue that the failure mode of a VLA is determined not by backbone scale but by its output interface. We propose Rejectable and Calibra...

</details>

<details>
<summary>Share</summary>

```
Do Not Cut When Uncertain: Rejectable and Calibrated Decision Heads for VLA Policies in Robotic Harvesting

Vision-Language-Action (VLA) policies trained with behavior cloning or flow matching are optimized to output an action trajectory, but they cannot express "I don't know" or "I should not act." In robotic harvesting, o...

arXiv: https://arxiv.org/abs/2609.35039

#VLA #robotics
```

</details>

---

### [Adjoint Guidance Flow: Amortized Critic Guidance for VLA Policies](https://arxiv.org/abs/2609.34944)

**Authors:** Jeongsol Kim, Youngjun Jun, Kyumin Choi, Youngmin Kim, Seonghyun Jin et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.LG, cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34944) | [PDF](https://arxiv.org/pdf/2609.34944)

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies are typically trained by behavior cloning and thus do not explicitly optimize long-term task return. Critic guidance steers generation toward higher-value actions, but existing methods differentiate the critic through a one-step surrogate of the sampler and back-propagate a critic ensemble at every flow step. In contrast, here we propose Adjoint Guidance Flow (AGF), which amortizes trajectory-aware critic guidance into a lightweight guidance network while preserving the pretrained VLA policy. Specifically, we formulate critic-guided flow generat...

</details>

<details>
<summary>Share</summary>

```
Adjoint Guidance Flow: Amortized Critic Guidance for VLA Policies

Flow-based Vision-Language-Action (VLA) policies are typically trained by behavior cloning and thus do not explicitly optimize long-term task return.

arXiv: https://arxiv.org/abs/2609.34944

#VLA #robotics
```

</details>

---

### [Natural State-Prediction Accuracy can Hide Weak Controlled Responsiveness in VLA Readouts](https://arxiv.org/abs/2609.34684)

**Authors:** Hyungjoon Kim, Wonbin Son, Mi Young Lee, Jun Young Lee, Seungmin Rho

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34684) | [PDF](https://arxiv.org/pdf/2609.34684)

<details>
<summary>Abstract</summary>

Accurately decoding object states from the internal representations of vision-language-action (VLA) models does not establish that the predictions respond faithfully to changes in the target physical state. In natural observations, object state, robot configuration, occlusion, and task progress vary together, allowing contextual cues to contribute to prediction. In this paper, we introduce an evaluation framework that separates prediction accuracy, target-state responsiveness, and context stability using physically validated observations that cross target coordinates with robot contexts. We de...

</details>

<details>
<summary>Share</summary>

```
Natural State-Prediction Accuracy can Hide Weak Controlled Responsiveness in VLA Readouts

Accurately decoding object states from the internal representations of vision-language-action (VLA) models does not establish that the predictions respond faithfully to changes in the target physical state.

arXiv: https://arxiv.org/abs/2609.34684

#VLA #robotics
```

</details>

---

### [Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs](https://arxiv.org/abs/2609.34554)

**Authors:** Tanguy Dieudonné, Jack B. Jedlicki, Heng Yang

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34554) | [PDF](https://arxiv.org/pdf/2609.34554)

<details>
<summary>Abstract</summary>

Memory is essential for long-horizon, partially observed robotic manipulation: a robot must remember which object was placed in a drawer, whose cup it moved, or how many action cycles have elapsed. Recent vision-language-action (VLA) models embed memory directly inside the policy, but benchmarks show no single in-policy mechanism covers all spatio-temporal dimensions, trailing oracle methods by a wide margin. We argue that memory type dictates where memory should reside: short-term perceptual memory (repetition, timing, retracing) belongs inside the policy, while long-term object memory (persi...

</details>

<details>
<summary>Share</summary>

```
Where Memory Belongs: Ledger, an Object Ledger for Memory-Augmented VLAs

Memory is essential for long-horizon, partially observed robotic manipulation: a robot must remember which object was placed in a drawer, whose cup it moved, or how many action cycles have elapsed.

arXiv: https://arxiv.org/abs/2609.34554

#VLA #robotics
```

</details>

---

### [Gaze Prompts: Temporally Dense Human Attention for Vision-Language-Action Fine-Tuning](https://arxiv.org/abs/2609.34550)

**Authors:** Yihan Zhou, Rui Yan, Mingcong Li, Zheyuan Huang, Xu Yang et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34550) | [PDF](https://arxiv.org/pdf/2609.34550)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) fine-tuning pairs images with actions at every step, yet typically provides only a task-level language instruction, leaving moment-to-moment visual relevance implicit. We introduce \emph{eye-tracker-supervised gaze prompting}, which uses gaze recorded during VR teleoperation to provide frame-level visual guidance for VLA fine-tuning. During training, recorded gaze locations are rendered as crosshairs on the robot's head-camera images. At deployment, a lightweight predictor estimates gaze locations from recent images and the instruction, supplying the same type of v...

</details>

<details>
<summary>Share</summary>

```
Gaze Prompts: Temporally Dense Human Attention for Vision-Language-Action Fine-Tuning

Vision-Language-Action (VLA) fine-tuning pairs images with actions at every step, yet typically provides only a task-level language instruction, leaving moment-to-moment visual relevance implicit.

arXiv: https://arxiv.org/abs/2609.34550

#VLA #robotics
```

</details>

---

### [Text-Vision Synergistic Token Caching: A Training-Free Framework for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2609.34319)

**Authors:** Qianer Li, Chengjie Zhang, Jingwen Chen, Zanjia Tong, Jiyuan Zhang et al. (6 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34319) | [PDF](https://arxiv.org/pdf/2609.34319)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable generalizable robotic control but remain computationally expensive. Token caching provides a training-free, plug-and-play acceleration alternative. However, existing VLA caching does not fully exploit a key inductive bias of VLA models: text-vision synergy, wherein textual semantics guide the precise visual grounding of task-relevant regions. In particular, existing designs insufficiently account for head-wise reliability in attention aggregation and layer-wise stability in cache reuse. To address this, we propose Text-Vision Synergistic Token Caching...

</details>

<details>
<summary>Share</summary>

```
Text-Vision Synergistic Token Caching: A Training-Free Framework for Efficient Vision-Language-Action Inference

Vision-Language-Action (VLA) models enable generalizable robotic control but remain computationally expensive.

arXiv: https://arxiv.org/abs/2609.34319

#VLA #robotics
```

</details>

---

### [RoboICL: Embodied In-Context Learning with GPT-6 Astra](https://arxiv.org/abs/2609.34261)

**Authors:** Fangcheng Liu, Yeqing Shen, Anda Cheng, Weishi Mi, Chao Tang et al. (10 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34261) | [PDF](https://arxiv.org/pdf/2609.34261) | [Code](https://github.com/Mosi-AI/RoboICL)

<details>
<summary>Abstract</summary>

General-purpose vision-language models offer a promising way to zero-shot robot control: \gptastra{} excels at open-ended and language- or image-conditioned manipulation but remains substantially weaker on high-precision and long-horizon tasks. We introduce \emph{RoboICL}, an in-context robot-control framework that narrows these gaps without robot-specific parameter updates or a learned VLA. RoboICL separates \emph{demonstration context}, which provides recorded examples when available, from \emph{interaction memory}, which accumulates the model's own actions and observed outcomes. Both use a...

</details>

<details>
<summary>Share</summary>

```
RoboICL: Embodied In-Context Learning with GPT-6 Astra

General-purpose vision-language models offer a promising way to zero-shot robot control: \gptastra{} excels at open-ended and language- or image-conditioned manipulation but remains substantially weaker on high-precis...

arXiv: https://arxiv.org/abs/2609.34261
Code: https://github.com/Mosi-AI/RoboICL

#VLA #robotics
```

</details>

---

### [UMR: Universal Manipulation Representation](https://arxiv.org/abs/2609.34256)

**Authors:** Song Liu, Linyi Li, Yanshun Zhao, Rxuan Li, Xinrui Xu et al. (14 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.34256) | [PDF](https://arxiv.org/pdf/2609.34256) | [Project Page](https://umr-wepvla.github.io/)

<details>
<summary>Abstract</summary>

General-purpose embodied manipulation hinges on a unified action representation that generalizes across embodiments and scales readily. Yet existing policies rely on embodiment-specific action spaces, making cross-embodiment demonstrations difficult to leverage at scale and limiting transfer to new embodiments and spatial variations. To this end, we introduce Universal Manipulation Representation (UMR), a unified action representation that enables zero-shot skill transfer from human demonstrations to heterogeneous robots. UMR decomposes manipulation into two functionally distinct yet geometric...

</details>

<details>
<summary>Share</summary>

```
UMR: Universal Manipulation Representation

General-purpose embodied manipulation hinges on a unified action representation that generalizes across embodiments and scales readily.

arXiv: https://arxiv.org/abs/2609.34256
Project page: https://umr-wepvla.github.io/

#VLA #robotics
```

</details>

---

### [Does Adversarial Training Improve Generalization in Multi-View VLAs? Revealing and Mitigating View Collapse](https://arxiv.org/abs/2609.33707)

**Authors:** Futa Waseda, Shuhei Kurita, Isao Echizen

**Published:** 2026-09-27 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33707) | [PDF](https://arxiv.org/pdf/2609.33707)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models adapt pretrained vision-language models (VLMs) for closed-loop robot control, transferring their perceptual and semantic capabilities to action prediction. Despite strong in-distribution performance, however, VLAs often degrade under deployment shifts. Adversarial training (AT) offers a model-adaptive approach to robustness without explicitly anticipating individual shifts, but its effect on natural distribution-shift generalization in multi-view VLAs remains unclear. We study this question using a multi-view VLA directly adapted from a pretrained VLM and ev...

</details>

<details>
<summary>Share</summary>

```
Does Adversarial Training Improve Generalization in Multi-View VLAs? Revealing and Mitigating View Collapse

Vision-language-action (VLA) models adapt pretrained vision-language models (VLMs) for closed-loop robot control, transferring their perceptual and semantic capabilities to action prediction.

arXiv: https://arxiv.org/abs/2609.33707

#VLA #robotics
```

</details>

---

### [InfraVLA: Extending Vision-Language-Action Navigation with Infrastructure Cameras](https://arxiv.org/abs/2609.33647)

**Authors:** Lukas Vierling, Benjamin Ramtoula, Luke Robinson, Ronald Clark, Daniele De Martini

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33647) | [PDF](https://arxiv.org/pdf/2609.33647)

<details>
<summary>Abstract</summary>

Many indoor environments in which robots operate, such as warehouses, offices, and hospitals, already have cameras installed. They observe parts of the building that the robot cannot see from where it stands, yet navigation policies, including recent vision-language-action (VLA) models, do not use them. We propose InfraVLA, an end-to-end method that adapts a pretrained navigation VLA to such static infrastructure views: a closed-circuit television (CCTV) encoder turns each external view into tokens of the input sequence. Because the views matter only at rare decision points, fine-tuning alone...

</details>

<details>
<summary>Share</summary>

```
InfraVLA: Extending Vision-Language-Action Navigation with Infrastructure Cameras

Many indoor environments in which robots operate, such as warehouses, offices, and hospitals, already have cameras installed.

arXiv: https://arxiv.org/abs/2609.33647

#VLA #robotics
```

</details>

---

### [ActionGround: Training-Free Runtime Refinement of Frozen VLA Policies](https://arxiv.org/abs/2609.33256)

**Authors:** Namai Chandra, Madhur Thareja, Shriram Damodaran, Addison Lin Wang

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33256) | [PDF](https://arxiv.org/pdf/2609.33256)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map visual observations and language instructions directly to robot actions, but they do not explicitly represent the phase structure of manipulation tasks or the rigid-body dynamics governing execution. We present ActionGround, a neuro-symbolic, training-free runtime layer that wraps a frozen VLA policy without retraining, fine-tuning, or weight access, adding less than 1 ms of overhead per control step. A symbolic phase-aware finite-state machine identifies the manipulation phase (approach, grasp, transport, or place) and applies a phase-specific rule-base...

</details>

<details>
<summary>Share</summary>

```
ActionGround: Training-Free Runtime Refinement of Frozen VLA Policies

Vision-Language-Action (VLA) models map visual observations and language instructions directly to robot actions, but they do not explicitly represent the phase structure of manipulation tasks or the rigid-body dynamic...

arXiv: https://arxiv.org/abs/2609.33256

#VLA #robotics
```

</details>

---

### [TimelyDAgger: Timing-Aware Expert Querying for VLA Policy Improvement](https://arxiv.org/abs/2609.33157)

**Authors:** Zhixuan Zhao, Peiyan Li, Enhao Zhang, Yueran Tao, Hao Wang et al. (13 authors)

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33157) | [PDF](https://arxiv.org/pdf/2609.33157)

<details>
<summary>Abstract</summary>

DAgger improves robot policies by aggregating expert supervision from states visited during policy execution. Robot-gated DAgger automates expert queries, allowing the robot to decide when to request expert takeover. While existing gates emphasize detecting the need for assistance, takeover timing also shapes the content of these demonstrations and their value for policy learning. We propose TimelyDAgger, combining Bridge-PCA monitoring of internal vision-language-action (VLA) features with Feedback-guided Threshold Adaptation based on expert behavior to improve takeover timing. We introduce a...

</details>

<details>
<summary>Share</summary>

```
TimelyDAgger: Timing-Aware Expert Querying for VLA Policy Improvement

DAgger improves robot policies by aggregating expert supervision from states visited during policy execution.

arXiv: https://arxiv.org/abs/2609.33157

#VLA #robotics
```

</details>

---

### [Train Together or Merge Later? Unifying VLA Experts via a Shared Action Interface](https://arxiv.org/abs/2609.33125)

**Authors:** Zhizhen Zhang, Yuxia Fu, Zijian Wang, Helen Huang, Yadan Luo

**Published:** 2026-09-27 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33125) | [PDF](https://arxiv.org/pdf/2609.33125)

<details>
<summary>Abstract</summary>

Co-training offers a straightforward way to build a multi-task vision-language-action (VLA) policy, but can fall short of the performance achieved by training each task independently. The challenge is to retain these task-specific gains in a multi-task policy without joint post-training. Combining independently trained experts through model merging is a natural approach, yet strong individual experts do not necessarily yield a strong merged policy. We identify one source of this incompatibility: task-specific changes to the action interface, comprising action normalization and the action encod...

</details>

<details>
<summary>Share</summary>

```
Train Together or Merge Later? Unifying VLA Experts via a Shared Action Interface

Co-training offers a straightforward way to build a multi-task vision-language-action (VLA) policy, but can fall short of the performance achieved by training each task independently.

arXiv: https://arxiv.org/abs/2609.33125

#VLA #robotics
```

</details>

---

### [Copper-Policy: Focus on the Representation for Robust Robot Manipulation](https://arxiv.org/abs/2609.32779)

**Authors:** Zexin Feng, Yixu Feng, Lingyu Xiao, Shang Su, Kexin Zheng et al. (9 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.32779) | [PDF](https://arxiv.org/pdf/2609.32779) | [Project Page](https://zexinfeng-cn.github.io/works/copper-policy/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) acquire behavioral priors by modeling future scene evolution, but predicting detailed futures in pixel or latent space incurs substantial cost. Recent evidence that co-training gains persist without test-time generation raises a question: what must a WAM learn to improve control? We introduce Copper-Policy, which learns a compact World representation with the policy rather than relying on a predefined target space. Through temporal joint-embedding prediction, it predicts future observation embeddings conditioned on task intention without reconstructing pixels. This p...

</details>

<details>
<summary>Share</summary>

```
Copper-Policy: Focus on the Representation for Robust Robot Manipulation

World Action Models (WAMs) acquire behavioral priors by modeling future scene evolution, but predicting detailed futures in pixel or latent space incurs substantial cost.

arXiv: https://arxiv.org/abs/2609.32779
Project page: https://zexinfeng-cn.github.io/works/copper-policy/

#VLA #robotics
```

</details>

---

### [SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation](https://arxiv.org/abs/2609.32698)

**Authors:** Ziwen Li, Hanlue Zhang, Zhenyang Ren, Tianyu Huang, Runqi Lin et al. (12 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32698) | [PDF](https://arxiv.org/pdf/2609.32698)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) policies demonstrate promising generalization across diverse short-horizon tasks. However, they remain unreliable on long-horizon tasks, partly because the large-scale training data is biased toward single-stage manipulation tasks that are cheaper to demonstrate. A single weak atomic skill can cause failures across multiple multi-stage tasks. To address such failures, existing methods often require experts to identify the bottleneck and provide additional demonstrations, making the improvement costly and potentially impractical after deployment. To this end,...

</details>

<details>
<summary>Share</summary>

```
SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation

Recent vision-language-action (VLA) policies demonstrate promising generalization across diverse short-horizon tasks.

arXiv: https://arxiv.org/abs/2609.32698

#VLA #robotics
```

</details>

---

### [Find Something You Can't Do: Agentic Real-World Reinforcement Learning for Self-Improving VLA Models](https://arxiv.org/abs/2609.32069)

**Authors:** Yuan Fang, Zechu Li, Haolei Tong, Puze Liu, Georgia Chalvatzaki

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32069) | [PDF](https://arxiv.org/pdf/2609.32069)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) models provide strong priors for robotic manipulation but are typically deployed as frozen policies, unable to improve from their own failures. Real-world reinforcement learning (RL) offers a path to continued improvement, yet manual environment resets and task-success supervision hinder autonomous learning. We introduce \textbf{FIND}, an agentic real-world RL framework that closes the loop between scene understanding, weakness-aware practice, self-evaluation, and policy improvement in a persistent workspace. FIND reframes autonomous practice as a scene-condition...

</details>

<details>
<summary>Share</summary>

```
Find Something You Can't Do: Agentic Real-World Reinforcement Learning for Self-Improving VLA Models

Vision--language--action (VLA) models provide strong priors for robotic manipulation but are typically deployed as frozen policies, unable to improve from their own failures.

arXiv: https://arxiv.org/abs/2609.32069

#VLA #robotics
```

</details>

---

### [Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048)

**Authors:** Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.31048) | [PDF](https://arxiv.org/pdf/2609.31048)

<details>
<summary>Abstract</summary>

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation. However, such pipelines typically retain successful demonstrations while failed rollouts are discarded, even though they expose precisely the off-nominal states from which recovery must be learned. We introduce Kintsugi-VLA, a framework for converting failed rollouts into targeted synthetic recovery data by exploiting exact state restoration and branching in simulation. For a fixed...

</details>

<details>
<summary>Share</summary>

```
Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation.

arXiv: https://arxiv.org/abs/2609.31048

#VLA #robotics
```

</details>

---

### [Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies](https://arxiv.org/abs/2609.30913)

**Authors:** Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30913) | [PDF](https://arxiv.org/pdf/2609.30913)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state. We study instruction switching, where a new task is issued during or after the execution of a different one. We observe that a target task that is reliably completed from its standard initial states can become inaccessible from states produced by a preceding task. We call such states task islands. We propose Causeway, a training-free inference-time intervention. Given the current state and a re-entry pose for the ta...

</details>

<details>
<summary>Share</summary>

```
Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state.

arXiv: https://arxiv.org/abs/2609.30913

#VLA #robotics
```

</details>

---

### [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939)

**Authors:** Ruiyang Si, Jianxin Bi, Shunyu Yang, Rui Ni, Wenbo Huang et al. (12 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.01939) | [PDF](https://arxiv.org/pdf/2610.01939)

<details>
<summary>Abstract</summary>

Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead. We introduce PyRUA-Lean, an interactive code-execution framework that couples feedback-driven primitive composition with selective observation: the agent composes classical robot primitives and learned vision-language-action (VLA) policies into Python cells that perform conditional checks and local retries, returning only explicitly requested images and state feedback for replanning. Across 700 simulated...

</details>

<details>
<summary>Share</summary>

```
Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead.

arXiv: https://arxiv.org/abs/2610.01939

#VLA #robotics
```

</details>

---

### [The Layer Mystery of VLA: An Information-Theoretical Analysis of VLA Latent Interface](https://arxiv.org/abs/2609.36118)

**Authors:** Yuxiang Liu, Lizhi Yang, Fengze Xie, Aaron Ames, Yisong Yue

**Published:** 2026-09-28 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36118) | [PDF](https://arxiv.org/pdf/2609.36118)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies connect a pretrained vision-language backbone to an action head through a latent interface, but which backbone layers this interface should expose remains unclear. We study single-layer selection and multi-layer fusion for frozen backbones across three pretrained models and two manipulation benchmarks, LIBERO and CALVIN, with three policy-training seeds per configuration. Across three fusion mechanisms and three layer-subset strategies, 47 of 54 configurations underperform the best observed single-layer policy. Our stastical analysis further confirms that...

</details>

<details>
<summary>Share</summary>

```
The Layer Mystery of VLA: An Information-Theoretical Analysis of VLA Latent Interface

Vision-language-action (VLA) policies connect a pretrained vision-language backbone to an action head through a latent interface, but which backbone layers this interface should expose remains unclear.

arXiv: https://arxiv.org/abs/2609.36118

#VLA #robotics
```

</details>

---

### [RefineDrive: Reliable Failure-Guided Learning for Vision-Language-Action Driving](https://arxiv.org/abs/2609.35078)

**Authors:** Zhe Sun, Ziyi Luo, Yehao Lu, Lei Zhou, Xi Li

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35078) | [PDF](https://arxiv.org/pdf/2609.35078)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models for autonomous driving rely heavily on successful expert demonstrations, leaving model-specific failures underexploited. Learning from these failures is hindered by unreliable diagnoses, poorly matched correction targets, and coarse rewards. We propose RefineDrive, a failure-guided post-training framework that learns from self-generated failures through targeted supervision and safety-aware reinforcement learning. Reliable Diagnosis derives structured, verifiable feedback on collisions and drivable-area violations directly from simulator states. Minimum-Corr...

</details>

<details>
<summary>Share</summary>

```
RefineDrive: Reliable Failure-Guided Learning for Vision-Language-Action Driving

Vision-Language-Action (VLA) models for autonomous driving rely heavily on successful expert demonstrations, leaving model-specific failures underexploited.

arXiv: https://arxiv.org/abs/2609.35078

#VLA #robotics
```

</details>

---

### [Unified Trajectory Matching Policy Optimization: Diverse T2I Generation and VLA Generalization](https://arxiv.org/abs/2609.34688)

**Authors:** Zhiyuan Ma, Jiaming Li, Lingzhen Li, Yu Liu, Xuekai Zhu et al. (10 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34688) | [PDF](https://arxiv.org/pdf/2609.34688)

<details>
<summary>Abstract</summary>

Reward-maximizing reinforcement learning (RL) is widely used to post-train stochastic diffusion and flow policies for text-to-image (T2I) generation. However, reward-maximizing RL causes policy mode collapse even under reference KL or entropy regularization, reducing the policy to a single high-reward mode. In T2I, this produces similar images and reward hacking. When extended to vision-language-action (VLA) models, the same collapse removes alternative successful strategies and weakens task and scene generalization. To address this limitation, we introduce Unified Trajectory Matching Policy O...

</details>

<details>
<summary>Share</summary>

```
Unified Trajectory Matching Policy Optimization: Diverse T2I Generation and VLA Generalization

Reward-maximizing reinforcement learning (RL) is widely used to post-train stochastic diffusion and flow policies for text-to-image (T2I) generation.

arXiv: https://arxiv.org/abs/2609.34688

#VLA #robotics
```

</details>

---

### [The Low-Rank Structure of VLA Reinforcement Learning](https://arxiv.org/abs/2609.34599)

**Authors:** Minjae Oh, Yoonah Park, Jongwon Lim, Yohan Jo

**Published:** 2026-09-28 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34599) | [PDF](https://arxiv.org/pdf/2609.34599)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, yet how RL reshapes these policies remains poorly understood. We find that RL across widely used flow-based VLA models, including $π_{0.5}$ and GR00T~N1.5/N1.6, on LIBERO, ManiSkill, MetaWorld, and CALVIN induces substantially lower-rank parameter updates that are highly concentrated in the action expert's Timestep Modules, a small and previously overlooked component. Through systematic module-replacement experiments, we further show that these modules capture a disproportionate share of the per...

</details>

<details>
<summary>Share</summary>

```
The Low-Rank Structure of VLA Reinforcement Learning

Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, yet how RL reshapes these policies remains poorly understood.

arXiv: https://arxiv.org/abs/2609.34599

#VLA #robotics
```

</details>

---

### [Alignment-Guided Flow Transformer for Efficient Vision-Language-Action Policy Learning](https://arxiv.org/abs/2609.34467)

**Authors:** Shengchao Hu, Peng Wang, Qiyang Zhou, Guodong Zheng, Yuqi Huang et al. (8 authors)

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34467) | [PDF](https://arxiv.org/pdf/2609.34467)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models point toward general-purpose robotic intelligence by unifying perception, instruction, and control. Despite impressive progress, existing VLA models often adapt poorly due to \emph{tri-modal misalignment} among vision, language, and action, which weakens action grounding and hurts generalization and fine-tuning efficiency. In this work, we present Alignment-Guided Flow Transformer (AGFT), a novel framework that explicitly enforces tri-modal alignment through a dedicated alignment loss, bridging the representational gap across modalities an...

</details>

<details>
<summary>Share</summary>

```
Alignment-Guided Flow Transformer for Efficient Vision-Language-Action Policy Learning

Recent advances in Vision-Language-Action (VLA) models point toward general-purpose robotic intelligence by unifying perception, instruction, and control.

arXiv: https://arxiv.org/abs/2609.34467

#VLA #robotics
```

</details>

---

### [WorldGuide: Learning Success-Failure Boundaries in Latent World Models for Vision-Language-Action Policies](https://arxiv.org/abs/2609.34206)

**Authors:** Lin Liu, Lu Zhang, Ziying Song, Wu Yang, Yuzheng Zhuang et al. (9 authors)

**Published:** 2026-09-28 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34206) | [PDF](https://arxiv.org/pdf/2609.34206)

<details>
<summary>Abstract</summary>

Latent world models offer a promising way to improve Vision-Language-Action policies by capturing the consequences of actions. However, models trained primarily on expert demonstrations have limited exposure to failure outcomes and may struggle to distinguish visually similar successful and failed interactions. We propose \textbf{WorldGuide}, a framework that learns these distinctions in latent space and uses them to guide policy training. WorldGuide combines predictive pretraining on successful and failed trajectories with contrastive learning on matched success--failure pairs. The learned pr...

</details>

<details>
<summary>Share</summary>

```
WorldGuide: Learning Success-Failure Boundaries in Latent World Models for Vision-Language-Action Policies

Latent world models offer a promising way to improve Vision-Language-Action policies by capturing the consequences of actions.

arXiv: https://arxiv.org/abs/2609.34206

#VLA #robotics
```

</details>

---

### [Resolving State-Representation Mismatch: State-Space Visual Reasoning for Open-Loop VLA Planning](https://arxiv.org/abs/2609.33412)

**Authors:** Junhao Xiao, Haoxiang Zhao, Menghao Fang, Jinkui Zhang, Jinghan Yu et al. (11 authors)

**Published:** 2026-09-27 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33412) | [PDF](https://arxiv.org/pdf/2609.33412)

<details>
<summary>Abstract</summary>

Despite rapid progress in vision-language-action (VLA) models, existing reasoning paradigms still face a fundamental \emph{state-representation mismatch} in open-loop planning. Given only an initial observation, models must internally simulate action-conditioned state transitions, whereas text-, pixel-, and latent-space reasoning can suffer from lossy spatial compression, error-accumulating visual generation, and bypass of intermediate latent tokens, respectively, undermining reliable long-horizon planning. We propose \textbf{State-Space Visual Reasoning} (SSVR), which decouples static visual...

</details>

<details>
<summary>Share</summary>

```
Resolving State-Representation Mismatch: State-Space Visual Reasoning for Open-Loop VLA Planning

Despite rapid progress in vision-language-action (VLA) models, existing reasoning paradigms still face a fundamental \emph{state-representation mismatch} in open-loop planning.

arXiv: https://arxiv.org/abs/2609.33412

#VLA #robotics
```

</details>

---

### [Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling](https://arxiv.org/abs/2609.32193)

**Authors:** Hongyi Cai, Yi Herng Ong, Tingshiuan C. Wu, Chiew Hui Lim, Hanxia Li et al. (7 authors)

**Published:** 2026-09-26 (updated 2026-10-01) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32193) | [PDF](https://arxiv.org/pdf/2609.32193)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models condition actions directly on current visual and language context, without an explicit account of how the scene evolves under candidate actions. World Action Models (WAM) attempt to address this limitation by predicting future states, but existing designs keep prediction and policy learning architecturally separate, connecting them only through the predicted output, whether through pixel space video generation or a latent forecasting module trained independently of the policy. We present Devol-ONE, a Mixture of Transformers architecture that unifies vision l...

</details>

<details>
<summary>Share</summary>

```
Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling

Vision Language Action (VLA) models condition actions directly on current visual and language context, without an explicit account of how the scene evolves under candidate actions.

arXiv: https://arxiv.org/abs/2609.32193

#VLA #robotics
```

</details>

---

### [VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control](https://arxiv.org/abs/2609.30709)

**Authors:** Kemou Jiang, Maonan Wang, Xingchen Zou, Jiayue Zhu, Yuhang Fu et al. (9 authors)

**Published:** 2026-09-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30709) | [PDF](https://arxiv.org/pdf/2609.30709)

<details>
<summary>Abstract</summary>

Traffic signal control (TSC) is essential for mitigating urban congestion. Recent advances in vision-language models (VLMs) enable richer interpretation of intersection scenes, opening new opportunities for visual-context-aware TSC. However, the loose coupling and repeated information conversion between modules can lead to the loss of fine-grained visual details, while sequential inference introduces substantial latency. To address these limitations, we propose VLALight, a lightweight end-to-end vision-language-action framework that directly maps intersection observations and signal-phase info...

</details>

<details>
<summary>Share</summary>

```
VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control

Traffic signal control (TSC) is essential for mitigating urban congestion.

arXiv: https://arxiv.org/abs/2609.30709

#VLA #robotics
```

</details>

---

### [PrefPI: Preference-Guided Steering into Out-of-Distribution Behaviors](https://arxiv.org/abs/2609.40165)

**Authors:** Seungeun Rho, Wontaek Kim, Danfei Xu, Sehoon Ha

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.40165) | [PDF](https://arxiv.org/pdf/2609.40165)

<details>
<summary>Abstract</summary>

We present PrefPI (Preference-Guided Policy Iteration), an iterative framework for steering pretrained generative robot policies using only relative preferences over self-generated trajectories. Unlike prior preference-learning methods that primarily sharpen modes already represented by the policy, we study steering beyond the initial effective support, where desired behaviors are rarely or never observed under the initial policy. Our key idea is to formulate preference learning as preference-conditioned generative modeling: preferred trajectories define a conditional distribution, whose densi...

</details>

<details>
<summary>Share</summary>

```
PrefPI: Preference-Guided Steering into Out-of-Distribution Behaviors

We present PrefPI (Preference-Guided Policy Iteration), an iterative framework for steering pretrained generative robot policies using only relative preferences over self-generated trajectories.

arXiv: https://arxiv.org/abs/2609.40165

#VLA #robotics
```

</details>

---

### [PRICE the Action Chunks: Physical Relational Credit Assignment for Embodied Reinforcement Learning](https://arxiv.org/abs/2609.38890)

**Authors:** Yangang Zou, Jiajun Lu, Weitao Zhou, Haibao Yu, Bozhou Zhang et al. (9 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.38890) | [PDF](https://arxiv.org/pdf/2609.38890)

<details>
<summary>Abstract</summary>

Outcome-based reinforcement learning (RL) post-trains vision--language--action policies using terminal success signals, but assigns the same trajectory-level advantage to every action chunk. A failed episode can thus penalize useful early actions as if they caused the failure. Existing approaches seek finer-grained feedback through learned evaluators, adding task-specific supervision or additional model training. We explore, for the first time to our knowledge, whether physical relations across trajectories can provide action-chunk credit in embodied RL from terminal outcomes alone, without an...

</details>

<details>
<summary>Share</summary>

```
PRICE the Action Chunks: Physical Relational Credit Assignment for Embodied Reinforcement Learning

Outcome-based reinforcement learning (RL) post-trains vision--language--action policies using terminal success signals, but assigns the same trajectory-level advantage to every action chunk.

arXiv: https://arxiv.org/abs/2609.38890

#VLA #robotics
```

</details>

---

### [EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation](https://arxiv.org/abs/2609.37181)

**Authors:** Jin Chen, Yiming Jiang, Chongyang Xu, Modi Shi, Shijia Peng et al. (11 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2609.37181) | [PDF](https://arxiv.org/pdf/2609.37181)

<details>
<summary>Abstract</summary>

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid skill transfer framework for coordinated whole-body loco-manipulation. At its core, coarse-to-fine action alignment combines kinematic reference correction with dynamics-aware refinement. It improves end-effector pose accuracy while pre...

</details>

<details>
<summary>Share</summary>

```
EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation.

arXiv: https://arxiv.org/abs/2609.37181

#VLA #robotics
```

</details>

---

### [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)

**Authors:** Ke Zhang, Danica J. Sutherland, Chao Liu

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38401) | [PDF](https://arxiv.org/pdf/2609.38401)

<details>
<summary>Abstract</summary>

Training data variation, whether through designing a domain randomization (DR) scheme in simulation or curating demonstrations for imitation learning, is a primary lever for improving the robustness of robotic manipulation policies. Yet its underlying mechanisms remain poorly understood, and practitioners typically select randomization parameters through expensive trial and error. We investigate these mechanisms through a series of case studies, randomizing object size, color, and type as well as scene lighting and linguistic prompts across settings including pick-and-place RL in ManiSkill and...

</details>

<details>
<summary>Share</summary>

```
Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation

Training data variation, whether through designing a domain randomization (DR) scheme in simulation or curating demonstrations for imitation learning, is a primary lever for improving the robustness of robotic manipul...

arXiv: https://arxiv.org/abs/2609.38401

#VLA #robotics
```

</details>

---

### [Rho: A Foundation for Efficiently Adaptable VLA Models](https://arxiv.org/abs/2609.38164)

**Authors:** Rho Team, Simran Bagaria, Daphne Chen, Dean Fortier, Jianlong Fu et al. (14 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.38164) | [PDF](https://arxiv.org/pdf/2609.38164)

<details>
<summary>Abstract</summary>

General-purpose physical AI models must combine broad visual and linguistic capabilities with precise control across robot embodiments and efficient adaptation to downstream tasks. We introduce Rho, a family of open-weights VLA models for bimanual manipulation designed for data-light task adaptation on 3 embodiments representative of dual-arm robots across research labs and the industry -- YAM Box, UR AI Trainer, and FR3 Duo. We systematically ablate Rho's action-expert architecture and training recipe, and show in controlled simulation and physical-robot experiments that embodiment midtrainin...

</details>

<details>
<summary>Share</summary>

```
Rho: A Foundation for Efficiently Adaptable VLA Models

General-purpose physical AI models must combine broad visual and linguistic capabilities with precise control across robot embodiments and efficient adaptation to downstream tasks.

arXiv: https://arxiv.org/abs/2609.38164

#VLA #robotics
```

</details>

---

### [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078)

**Authors:** Bingxuan Li, Siqi Song, Yizhuo Wu, Jiarui Yao, Tong Zhang et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38078) | [PDF](https://arxiv.org/pdf/2609.38078)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from benefiting directly from rapidly advancing general-purpose vision-language models (VLMs). In parallel, recent agentic robotic systems leverage VLMs for high-level reasoning or coding agents for robot control, but often depend on extensive external models and tools, introducing additional complexity and cost. This motivates us to ask: Can a general-purpose VLM itself operate a robot mo...

</details>

<details>
<summary>Share</summary>

```
MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation

Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from bene...

arXiv: https://arxiv.org/abs/2609.38078

#VLA #robotics
```

</details>

---

### [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation](https://arxiv.org/abs/2609.37530)

**Authors:** Shuhong Liu, Heng Zhou, Lingfeng Qian, Yuhao Fang, Xianbao Hou et al. (10 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37530) | [PDF](https://arxiv.org/pdf/2609.37530)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop. We systematically examine the consequences of this overlooked design choice across five fundamental ISP dimensions: gain, sensor noise, chromatic response, tonal response, and bit depth. Our analysis reveals that RAW-to-RGB processing materially shapes both action prediction and manipulation success, with different ISP dimensions exerting substantially different effects. Guided by these findings, we i...

</details>

<details>
<summary>Share</summary>

```
RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop.

arXiv: https://arxiv.org/abs/2609.37530

#VLA #robotics
```

</details>

---

### [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](https://arxiv.org/abs/2609.37150)

**Authors:** Tianhang Pan, Xuanhao Wang, Yiwen Pang, Bo Zhou, Jun Yang et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.37150) | [PDF](https://arxiv.org/pdf/2609.37150)

<details>
<summary>Abstract</summary>

VLAs combine pretrained vision-language representations with action generation to enable language-guided control across diverse tasks, becoming a mainstream paradigm in embodied intelligence. However, multiple studies have reported VLA's substantial declines in task success under camera shifts, revealing a key vulnerability that limits reliable deployment. To address this vulnerability, existing methods collect paired observations of the same scene from different viewpoints to fine-tune the VLA or train visual adaptation modules. Unfortunately, they require additional data collection and VLA t...

</details>

<details>
<summary>Share</summary>

```
CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

VLAs combine pretrained vision-language representations with action generation to enable language-guided control across diverse tasks, becoming a mainstream paradigm in embodied intelligence.

arXiv: https://arxiv.org/abs/2609.37150

#VLA #robotics
```

</details>

---

### [LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks](https://arxiv.org/abs/2609.36774)

**Authors:** Zeming Wei, Jianheng Ye, Xinshuai Song, Sirui Chen, Yang Liu et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36774) | [PDF](https://arxiv.org/pdf/2609.36774)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models struggle to reuse recurring interactions in unseen tasks. Our diagnostic study reveals that reliable task completion does not imply consistent execution of constituent atomic actions across task contexts. We present LexiconVLA, a retrievable atomic-action lexicon for cross-task reuse. Global and detail codebooks capture shared interaction structure and fine-grained execution variation, respectively, preserving both reusable patterns and execution details. Visual-Atomic Action Alignment couples trajectory reconstruction from visual state changes with visual o...

</details>

<details>
<summary>Share</summary>

```
LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks

Vision-language-action (VLA) models struggle to reuse recurring interactions in unseen tasks.

arXiv: https://arxiv.org/abs/2609.36774

#VLA #robotics
```

</details>

---

### [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching](https://arxiv.org/abs/2609.35469)

**Authors:** Chenyu Zhang, Yuhang Cao, Daru Du, Yingxi Lu, Jing Shao et al. (11 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35469) | [PDF](https://arxiv.org/pdf/2609.35469)

<details>
<summary>Abstract</summary>

Autoregressive Vision-Language-Action (VLA) models offer a scalable path to robot learning, yet existing action tokenizers treat tokenization as a compression problem, producing representations that are semantically misaligned with the autoregressive backbone. We propose CATok, a causal action tokenizer that reframes tokenization as a causally structured generative process. CATok introduces a conditional annealing mechanism that extracts action tokens by progressively annealing a flow-matching process: each token is conditioned on all preceding tokens and encodes the residual reconstruction si...

</details>

<details>
<summary>Share</summary>

```
Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching

Autoregressive Vision-Language-Action (VLA) models offer a scalable path to robot learning, yet existing action tokenizers treat tokenization as a compression problem, producing representations that are semantically m...

arXiv: https://arxiv.org/abs/2609.35469

#VLA #robotics
```

</details>

---

### [Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432)

**Authors:** Hongcheng Gao, Jingjing Zhou, Zelin Zheng, Shijia Ge, Jay Zhu et al. (13 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35432) | [PDF](https://arxiv.org/pdf/2609.35432)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) and world-action (WAM) models map observations and instructions directly to robot actions. This directness ties a policy to training: minor layout or viewpoint changes cause failure, and instructions generalize poorly. The root cause lies in representation: task requirements, conditions, progress, and failure recovery are implicitly encoded in action sequences, making them difficult to inspect or revise. Digital coding agents offer a precedent: LLMs call tools, verify results, and revise from feedback as executable code. The same working pattern of explicit state,...

</details>

<details>
<summary>Share</summary>

```
Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence

Vision-language-action (VLA) and world-action (WAM) models map observations and instructions directly to robot actions.

arXiv: https://arxiv.org/abs/2609.35432

#VLA #robotics
```

</details>

---

### [RoboFL: Federated Expert Assembly for World Action Models](https://arxiv.org/abs/2609.34968)

**Authors:** Rongyu Zhang, Ruizhi Fan, Yunfan Lou, Hengyu Fang, Shenli Zheng et al. (11 authors)

**Published:** 2026-09-28 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34968) | [PDF](https://arxiv.org/pdf/2609.34968)

<details>
<summary>Abstract</summary>

Vision-language-action and world-action models are increasingly popular, yet remain bottlenecked by physical interaction data that is scarce, institutionally siloed, and task-heterogeneous. A natural federated solution is to let each client adapt a shared foundation model through parameter-efficient fine-tuning, avoiding the exchange of full-model updates. However, federating these adapters is nontrivial, as naive aggregation can entangle incompatible updates, while incorporating MoE-style routing into federated aggregation may dilute specialization and destabilize expert selection. We present...

</details>

<details>
<summary>Share</summary>

```
RoboFL: Federated Expert Assembly for World Action Models

Vision-language-action and world-action models are increasingly popular, yet remain bottlenecked by physical interaction data that is scarce, institutionally siloed, and task-heterogeneous.

arXiv: https://arxiv.org/abs/2609.34968

#VLA #robotics
```

</details>

---

### [mmHRI: Towards Privacy-Preserving Human-Robot Interaction with Millimeter-Wave Radar](https://arxiv.org/abs/2609.34220)

**Authors:** Junqiao Fan, Yuxuan Hu, Bofan Lyu, Yanshuo Lu, Pengfei Liu et al. (10 authors)

**Published:** 2026-09-28 (updated 2026-09-30) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34220) | [PDF](https://arxiv.org/pdf/2609.34220)

<details>
<summary>Abstract</summary>

Assistive robots increasingly operate in many human-centered environments and perform various human-robot interaction (HRI) tasks, such as object delivery. However, most existing HRI systems rely on RGB cameras that continuously observe humans to respond to non-verbal commands, such as hand gestures. This raises privacy concerns in privacy- critical environments, such as hospital wards or restaurants, where direct camera observation of humans is restricted. To develop privacy-preserving HRI, we leverage millimeter-wave (mmWave) radar, which can sense human motion through privacy barriers witho...

</details>

<details>
<summary>Share</summary>

```
mmHRI: Towards Privacy-Preserving Human-Robot Interaction with Millimeter-Wave Radar

Assistive robots increasingly operate in many human-centered environments and perform various human-robot interaction (HRI) tasks, such as object delivery.

arXiv: https://arxiv.org/abs/2609.34220

#VLA #robotics
```

</details>

---

### [F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement](https://arxiv.org/abs/2609.35575)

**Authors:** Zhuoyuan Yu, Jiacheng Wang, Tianle Liu, Yihua Ren, Peng Yu et al. (16 authors)

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35575) | [PDF](https://arxiv.org/pdf/2609.35575)

<details>
<summary>Abstract</summary>

The real-world performance of current vision-language-action models is fundamentally constrained by the limited coverage of expert demonstrations and their insufficient understanding of physical interactions. A common remedy is to collect additional real-world demonstrations of newly encountered failures. However, this process is costly, inefficient, potentially unsafe, and difficult to scale. To address this challenge, we propose Failure for Rising (F4R), a failure-driven real-to-sim-to-real closed-loop learning framework that converts real-world failures into targeted policy improvement. F4R...

</details>

<details>
<summary>Share</summary>

```
F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement

The real-world performance of current vision-language-action models is fundamentally constrained by the limited coverage of expert demonstrations and their insufficient understanding of physical interactions.

arXiv: https://arxiv.org/abs/2609.35575

#VLA #robotics
```

</details>

---

### [Zero-Shot Reactive Obstacle Avoidance for Generative Robot Policies](https://arxiv.org/abs/2609.35231)

**Authors:** Weihang Guo, Lydia E. Kavraki

**Published:** 2026-09-28 (updated 2026-09-29) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.35231) | [PDF](https://arxiv.org/pdf/2609.35231)

<details>
<summary>Abstract</summary>

We propose NUDGE (Nudge Update via Differentiable GEometry), a training-free obstacle-avoidance procedure that can be incorporated in any robot policy based on diffusion or flow matching, including diffusion policies and vision-language-action models. Our work injects gradients from a signed distance field, a function returning each point's distance to the nearest obstacle, into the policy at inference time to steer it away from obstacles. It supports any common action parameterization, from absolute or relative joint poses to end-effector poses, through a differentiable joint-trajectory decod...

</details>

<details>
<summary>Share</summary>

```
Zero-Shot Reactive Obstacle Avoidance for Generative Robot Policies

We propose NUDGE (Nudge Update via Differentiable GEometry), a training-free obstacle-avoidance procedure that can be incorporated in any robot policy based on diffusion or flow matching, including diffusion policies...

arXiv: https://arxiv.org/abs/2609.35231

#VLA #robotics
```

</details>

---

### [Principal Steering Subspaces for Online Adaptation of Frozen Generative Robot Policies](https://arxiv.org/abs/2609.33765)

**Authors:** Jialeng Ni, Nathan Zhao, Kunpeng Song

**Published:** 2026-09-27 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33765) | [PDF](https://arxiv.org/pdf/2609.33765)

<details>
<summary>Abstract</summary>

Generative robot policies provide expressive behavior priors, but updating a large diffusion or flow-matching model through online interaction is costly. Latent-space reinforcement learning avoids updating the pretrained generator by controlling its initial sampling noise, yet high-dimensional noise can have strongly anisotropic effects on decoded actions. We introduce Principal Steering Subspaces (PSS), a forward-query interface that constructs a fixed low-dimensional control basis from finite-difference decoder responses. Soft Actor-Critic controls the leading response directions, while the...

</details>

<details>
<summary>Share</summary>

```
Principal Steering Subspaces for Online Adaptation of Frozen Generative Robot Policies

Generative robot policies provide expressive behavior priors, but updating a large diffusion or flow-matching model through online interaction is costly.

arXiv: https://arxiv.org/abs/2609.33765

#VLA #robotics
```

</details>

---

### [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378)

**Authors:** Seungyeon Kim, Junhoo Lee, Minkyu Kim, Baekseung Kim, Nojun Kwak

**Published:** 2026-09-27 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.33378) | [PDF](https://arxiv.org/pdf/2609.33378)

<details>
<summary>Abstract</summary>

A central goal in robotics is to enable manipulation across changing tasks and environments. Vision-language-action (VLA) models provide broad manipulation capabilities but can struggle when execution requires diagnosing failures and adapting behavior. Strong agents can discover effective interventions through interaction with these policies. We propose Recursive Harness Distillation to accumulate this experience as reusable guidance across agents. A strong agent distills its experience into a playbook for a light agent, then recursively refines the playbook using the light agent's execution f...

</details>

<details>
<summary>Share</summary>

```
Recursive Harness Distillation across Agents for Robot Manipulation

A central goal in robotics is to enable manipulation across changing tasks and environments.

arXiv: https://arxiv.org/abs/2609.33378

#VLA #robotics
```

</details>

---

### [CLAP: Closed-Loop Alignment with Pressure for Precise Suction Manipulation](https://arxiv.org/abs/2609.32767)

**Authors:** Yixian Zou, Chongyang Xu, Yuling Xin, Ziliang Feng, Fanman Meng et al. (6 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32767) | [PDF](https://arxiv.org/pdf/2609.32767)

<details>
<summary>Abstract</summary>

Stacking and palletising demand precise placement: error left in one layer is inherited by the next, and a flat pad offers no feature to funnel a wrong pose into the right one. Top-down suction suits such dense arrangements, and suction has already been brought into vision-language-action (VLA) policies. What that work does not report, however, is a policy conditioned on a measured vacuum signal, or one that uses it to abandon an action already under way. Vision does not settle the question here, because at the moment it matters the cup and the face it holds occlude each other. We present CLAP...

</details>

<details>
<summary>Share</summary>

```
CLAP: Closed-Loop Alignment with Pressure for Precise Suction Manipulation

Stacking and palletising demand precise placement: error left in one layer is inherited by the next, and a flat pad offers no feature to funnel a wrong pose into the right one.

arXiv: https://arxiv.org/abs/2609.32767

#VLA #robotics
```

</details>

---

### [Federated Subspace Guided Vision-Language-Action Policy Distillation for Non-IID Multi-Robot Manipulation](https://arxiv.org/abs/2609.32239)

**Authors:** Biprodip Pal, Kaushik Roy, Yanming Zhu, Brendan Tidd, Alan Wee-Chung Liew et al. (6 authors)

**Published:** 2026-09-26 | **Categories:** cs.RO, cs.CV, cs.DC | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.32239) | [PDF](https://arxiv.org/pdf/2609.32239)

<details>
<summary>Abstract</summary>

Federated learning offers a natural way for multiple robots to jointly improve manipulation policies without requiring centralized access to training demonstrations. However, non-IID task and environment distributions can induce representation drift and mutually incompatible robot-policy updates, making naive parameter aggregation destructive. We present FedDRMan, a federated subspace-guided distillation framework for heterogeneous robot manipulation. At each communication round, the server model provides a frozen teacher for local behavior cloning, while low-rank multimodal subspace and actio...

</details>

<details>
<summary>Share</summary>

```
Federated Subspace Guided Vision-Language-Action Policy Distillation for Non-IID Multi-Robot Manipulation

Federated learning offers a natural way for multiple robots to jointly improve manipulation policies without requiring centralized access to training demonstrations.

arXiv: https://arxiv.org/abs/2609.32239

#VLA #robotics
```

</details>

---

### [FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.30965)

**Authors:** Hiroshi Ito, Hyogo Hiruma, Yoshiki Kanai, Takahiro Yoshida, Akira Kanazawa et al. (6 authors)

**Published:** 2026-09-25 (updated 2026-10-01) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30965) | [PDF](https://arxiv.org/pdf/2609.30965)

<details>
<summary>Abstract</summary>

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters. In this work, we propose the Future Representation Action Model (FRAM), a small policy that explicitly links the future end-effector trajectory to the current visual input. FRAM uses the image coordinates of the predicted trajectory as spatial pointers and reads local visual features related to the motion from the current image. This organizes the information for action generation into the reference position (Where), the visual state (What), and the future motion (Futu...

</details>

<details>
<summary>Share</summary>

```
FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters.

arXiv: https://arxiv.org/abs/2609.30965

#VLA #robotics
```

</details>

---

### [Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving](https://arxiv.org/abs/2609.37046)

**Authors:** Katharina Winter, Stefan Englmeier, Fabian B. Flohr

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37046) | [PDF](https://arxiv.org/pdf/2609.37046)

<details>
<summary>Abstract</summary>

Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized. We study velocity understanding as a controlled diagnostic across three tasks: surrounding-agent speed, current ego speed, and short-horizon future ego-speed proposal. On nuScenes, we evaluate open-weight general-purpose and PhysicalAI VLMs, together with the driving-oriented Alpamayo-1.5 Vision-Language-Action model, using multiple input and output formulations. We combine verbal evaluation with temporal perturb...

</details>

<details>
<summary>Share</summary>

```
Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving

Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized.

arXiv: https://arxiv.org/abs/2609.37046

#VLA #robotics
```

</details>

---

### [Brain-Conditioned Action Policies for Neural Motor Decoding](https://arxiv.org/abs/2609.34561)

**Authors:** Luyao Jin, Running Zhao, Huan Zhao, Vincent C. K. Cheung, Wei-Hsin Liao

**Published:** 2026-09-28 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.34561) | [PDF](https://arxiv.org/pdf/2609.34561)

<details>
<summary>Abstract</summary>

Motor brain-computer interfaces (BCIs) aim to decode motor intention, enabling people with paralysis to control external devices. Neural motor decoding typically learns task-specific mappings from neural activity to kinematics, yet remains constrained by scarce paired neural-action data. We propose BrainVLA, a framework that enables neural motor decoding by drawing on a pretrained vision-language-action (VLA) model through language-mediated alignment. BrainVLA mitigates reliance on scarce paired neural-action data by leveraging VLA policies. We first construct VLA-compatible datasets including...

</details>

<details>
<summary>Share</summary>

```
Brain-Conditioned Action Policies for Neural Motor Decoding

Motor brain-computer interfaces (BCIs) aim to decode motor intention, enabling people with paralysis to control external devices.

arXiv: https://arxiv.org/abs/2609.34561

#VLA #robotics
```

</details>

---

### [RCVLA: 4D Radar-Grounded Semantic Reasoning and Trajectory Arbitration for Autonomous Driving](https://arxiv.org/abs/2609.32681)

**Authors:** Lianqing Zheng, Xiaokai Bai, Yixuan Luo, Runwei Guan, Minghao Liu et al. (9 authors)

**Published:** 2026-09-26 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.32681) | [PDF](https://arxiv.org/pdf/2609.32681)

<details>
<summary>Abstract</summary>

4D radar provides geometric and motion cues that complement visual semantics, but integrating it into vision-language-action (VLA) models requires both radar--language alignment for semantic reasoning and explicit use of radar measurements for trajectory refinement and selection. To support these capabilities, we construct Cap4DR with 86,016 radar-image-text samples for alignment pretraining and OmniHD-QA with 520,161 question-answer pairs for instruction tuning across scene description, key-object reasoning, occupancy understanding, and trajectory planning. Building on these datasets, we prop...

</details>

<details>
<summary>Share</summary>

```
RCVLA: 4D Radar-Grounded Semantic Reasoning and Trajectory Arbitration for Autonomous Driving

4D radar provides geometric and motion cues that complement visual semantics, but integrating it into vision-language-action (VLA) models requires both radar--language alignment for semantic reasoning and explicit use...

arXiv: https://arxiv.org/abs/2609.32681

#VLA #robotics
```

</details>

---

### [WayFinder: Hierarchical Visual-Language-Action for Zero-Shot Waypoint Generation and Low-Level Kinematic Control](https://arxiv.org/abs/2609.37922)

**Authors:** Timothy K Johnsen, Marco Levorato

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.37922) | [PDF](https://arxiv.org/pdf/2609.37922)

<details>
<summary>Abstract</summary>

Visual Language Action (VLA) models offer unprecedented generalization for autonomous robots; however, their real-world deployment is frequently bottlenecked by unreliable execution and the prohibitive computational cost of fine-tuning for specific robot embodiments and tasks. To bridge this gap, we propose WayFinder, an end-to-end, closed-loop hierarchical VLA framework that circumvents the need for fine-tuning by decoupling high-level task reasoning from low-level kinematic control. WayFinder utilizes a zero-shot, offboard Multimodal Large Language Model (MLLM) policy to process linguistic c...

</details>

<details>
<summary>Share</summary>

```
WayFinder: Hierarchical Visual-Language-Action for Zero-Shot Waypoint Generation and Low-Level Kinematic Control

Visual Language Action (VLA) models offer unprecedented generalization for autonomous robots; however, their real-world deployment is frequently bottlenecked by unreliable execution and the prohibitive computational c...

arXiv: https://arxiv.org/abs/2609.37922

#VLA #robotics
```

</details>

---

### [Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks](https://arxiv.org/abs/2609.36471)

**Authors:** Guoheng Sun, Chen Chen, Jin Wang, Ang Li, Teresa Lv

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.36471) | [PDF](https://arxiv.org/pdf/2609.36471)

<details>
<summary>Abstract</summary>

World-Action Models (WAMs) improve robotic manipulation by conditioning action generation on predicted future observations, but future prediction adds further inference overhead to already expensive iterative action generation. Action chunking can amortize this cost over multiple actions, yet performance degrades over long execution horizons because later actions remain conditioned on stale observations. We introduce STAIRCASE POLICY, a streaming inference and training framework that turns a flow-matching VLA into a JEPA-style WAM and partitions a large action chunk into sub-chunks at staggere...

</details>

<details>
<summary>Share</summary>

```
Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks

World-Action Models (WAMs) improve robotic manipulation by conditioning action generation on predicted future observations, but future prediction adds further inference overhead to already expensive iterative action g...

arXiv: https://arxiv.org/abs/2609.36471

#VLA #robotics
```

</details>

---

### [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](https://arxiv.org/abs/2609.37810)

**Authors:** Sicheng Xie, Yitong Chen, Haidong Cao, Shunlin Lu, Zuxuan Wu et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.37810) | [PDF](https://arxiv.org/pdf/2609.37810)

<details>
<summary>Abstract</summary>

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging. More recently, general-purpose multimodal agents have shown great potential for zero-shot robotic task solving. However, they often incur high execution costs by reasoning and exploring the physical world from scratch. To reduce these costs, we introduce RoboSkill, a framework that connects skill acquisition and reuse through an Explore, Execute, Evolve loop. Within this loop, the agent explores to gather task-relevant information, execut...

</details>

<details>
<summary>Share</summary>

```
Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging.

arXiv: https://arxiv.org/abs/2609.37810

#VLA #robotics
```

</details>

---

### [RecastVLA: From Past Interaction to Future Control with Adaptive Policy States](https://arxiv.org/abs/2609.32155)

**Authors:** Wenbo Li, Jun Yang, Yiteng Chen, Wei Zhang, Qingyao Wu

**Published:** 2026-09-26 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.32155) | [PDF](https://arxiv.org/pdf/2609.32155)

<details>
<summary>Abstract</summary>

Sequential manipulation requires a robot to track what has already happened, even when the current scene no longer reveals it. Policies with explicit history representations make past interactions available as context for current decisions. We ask how action generation itself can form a persistent state for subsequent control. Building on action-side test-time training, RecastVLA maintains an adaptive policy state within a flow-matching vision-language-action policy. The state is represented by shared fast weights and remains fixed throughout action generation. Depth-specific interfaces read t...

</details>

<details>
<summary>Share</summary>

```
RecastVLA: From Past Interaction to Future Control with Adaptive Policy States

Sequential manipulation requires a robot to track what has already happened, even when the current scene no longer reveals it.

arXiv: https://arxiv.org/abs/2609.32155

#VLA #robotics
```

</details>

---

### [LLMs are General Asynchronous Agents](https://arxiv.org/abs/2609.35427)

**Authors:** George Yakushev, Denis Mazur, Vladimir Bartenev, Vyacheslav Zhdanovskiy, Timofey Byzov et al. (7 authors)

**Published:** 2026-09-28 | **Categories:** cs.LG, cs.CL | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.35427) | [PDF](https://arxiv.org/pdf/2609.35427)

<details>
<summary>Abstract</summary>

Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat. Many real-world use cases are not sequential: voice assistants, embodied agents, and monitoring systems receive new inputs while they think or perform another task. Modern LLMs address this with specialized architectures for voice interaction and video streams, VLAs for robot control, asynchronous tool calling for API usage, and others. In this work, we generalize from different asynchronous tasks to general asynchronous agents that can adapt to di...

</details>

<details>
<summary>Share</summary>

```
LLMs are General Asynchronous Agents

Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat.

arXiv: https://arxiv.org/abs/2609.35427

#VLA #robotics
```

</details>

---
