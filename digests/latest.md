# What's New

Papers discovered in the run at **2026-10-26 20:53 UTC**.

**New this run:** 22

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](https://arxiv.org/abs/2610.31845)

**Authors:** Chubin Zhang, Changyuan Wang, Yirui Wang, Ao Li, Shilin Ma et al. (10 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31845) | [PDF](https://arxiv.org/pdf/2610.31845) | [Project Page](https://lin-shan.com/EgoForesight)

<details>
<summary>Abstract</summary>

Scaling policy learning requires broad experience and reliable supervision. Robot demonstrations provide high-quality trajectory supervision but are costly to collect. Egocentric videos broaden task and environment coverage, yet motion reconstruction and retargeting introduce noisy action labels. To address this challenge, we introduce EgoForesight, a vision-language-action framework that learns jointly from both sources by reducing the influence of unreliable action labels and exploiting demonstrated outcomes as complementary supervision. A joint vision-action flow couples future visual repre...

</details>

<details>
<summary>Share</summary>

```
EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

Scaling policy learning requires broad experience and reliable supervision.

arXiv: https://arxiv.org/abs/2610.31845
Project page: https://lin-shan.com/EgoForesight

#egocentric #robotlearning
```

</details>

---

### [KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations](https://arxiv.org/abs/2610.31801)

**Authors:** Shuangyu Xie, Kaiyuan Chen, Muhammad Zubair Irshad, Richard Cheng, Sergey Zakharov et al. (6 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric human" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31801) | [PDF](https://arxiv.org/pdf/2610.31801) | [Project Page](https://berkeleyautomation.github.io/kirose/)

<details>
<summary>Abstract</summary>

Segmenting robot demonstration data into disjoint temporal and semantic subsegments is valuable for learning, cleaning, retrieval, and analysis. Segmentation is often performed manually in a tedious and error prone process. Multimodal Large Language Models (MLLMs) have the potential for automating this process, but directly ingesting raw multi camera video streams into MLLMs can be costly and can quickly exhaust context windows. In this paper, we introduce KiRoSe (Kinematics for Robot Segmentation), a novel framework that focuses on the companion stream of robot kinematic data. Inspired by the...

</details>

<details>
<summary>Share</summary>

```
KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations

Segmenting robot demonstration data into disjoint temporal and semantic subsegments is valuable for learning, cleaning, retrieval, and analysis.

arXiv: https://arxiv.org/abs/2610.31801
Project page: https://berkeleyautomation.github.io/kirose/

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (12)

### [Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies](https://arxiv.org/abs/2610.32102)

**Authors:** Jiabing Yang, Yuan Xu, Yixiang Chen, Qisen Ma, Peiyan Li et al. (16 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32102) | [PDF](https://arxiv.org/pdf/2610.32102) | [Project Page](https://jiabingyang01.github.io/Horizon-Depth-VLA/)

<details>
<summary>Abstract</summary>

Flow-matching Vision-Language-Action (VLA) models generate expressive continuous trajectories for robotic manipulation, yet balancing real-time responsiveness with execution stability remains a persistent challenge. Standard deployment workflows typically treat numerical solver depth and execution horizon as decoupled choices. The horizon amortizes inference latency, while solver depth is kept high to preserve integration fidelity. In this paper, we reveal a fundamental compute-execution coupling in flow-matching VLAs governed by a systematic sign reversal. While coarse numerical integration d...

</details>

<details>
<summary>Share</summary>

```
Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies

Flow-matching Vision-Language-Action (VLA) models generate expressive continuous trajectories for robotic manipulation, yet balancing real-time responsiveness with execution stability remains a persistent challenge.

arXiv: https://arxiv.org/abs/2610.32102
Project page: https://jiabingyang01.github.io/Horizon-Depth-VLA/

#VLA #robotics
```

</details>

---

### [If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs](https://arxiv.org/abs/2610.32941)

**Authors:** Thomas Landeg, Thierry Tambe

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32941) | [PDF](https://arxiv.org/pdf/2610.32941)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models perform well on robotic manipulation, yet remain brittle once their own actions carry them into states their training data barely covers. Recovering from such failures usually requires recovery demonstrations, policy retraining, or a separate model at inference time. We introduce Backtrack, a lightweight failure detection and recovery mechanism for frozen VLAs that needs none of these. A small failure prediction head, trained only on outcome-labeled rollouts of the frozen policy, reads the VLA's existing internal representations to estimate whether the curre...

</details>

<details>
<summary>Share</summary>

```
If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

Vision-Language-Action (VLA) models perform well on robotic manipulation, yet remain brittle once their own actions carry them into states their training data barely covers.

arXiv: https://arxiv.org/abs/2610.32941

#VLA #robotics
```

</details>

---

### [When Human Corrections Travel: Safety in Federated VLA Adaptation](https://arxiv.org/abs/2610.32888)

**Authors:** Vigneshwaran Subbaraju, Obaidullah Zaland, Monowar Bhuyan

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32888) | [PDF](https://arxiv.org/pdf/2610.32888)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can adapt to local human intervention, while federated learning can combine distributed robot experience without pooling raw records. We examine their prospective intersection: sharing adaptations derived from diverse human corrections across tasks, environments, people, and robot embodiments. Corrections differ in modality, safety semantics(urgency, behavioral scope, etc.), and privacy sensitivity. A shared update that improves mean task success may suppress a rare safety intervention or produce an unsafe response on another robot. We argue for three requ...

</details>

<details>
<summary>Share</summary>

```
When Human Corrections Travel: Safety in Federated VLA Adaptation

Vision-language-action (VLA) policies can adapt to local human intervention, while federated learning can combine distributed robot experience without pooling raw records.

arXiv: https://arxiv.org/abs/2610.32888

#VLA #robotics
```

</details>

---

### [MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation](https://arxiv.org/abs/2610.32312)

**Authors:** Jiachi Yang, Zhiyi Xu, Hongquan Zhang, Xin Tan, Zhizhong Zhang et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32312) | [PDF](https://arxiv.org/pdf/2610.32312)

<details>
<summary>Abstract</summary>

Generalist robot manipulation requires a single vision-language-action (VLA) policy to execute diverse skills across scenes and instructions. However, current multi-skill VLA policies often leave two aspects of an instruction insufficiently modeled: which primitive skill to execute and where/how to contact and move objects. We propose MAST-VLA (Multi-skill Adaptation with Skill-conditioned experts and Trajectory-affordance priors), a dual-conditioning framework for robot manipulation. MAST-VLA introduces skill-conditioned LoRA Mixture-of-Experts (LoRA-MoE) adapters in the LLM backbone, where s...

</details>

<details>
<summary>Share</summary>

```
MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

Generalist robot manipulation requires a single vision-language-action (VLA) policy to execute diverse skills across scenes and instructions.

arXiv: https://arxiv.org/abs/2610.32312

#VLA #robotics
```

</details>

---

### [From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot](https://arxiv.org/abs/2610.32271)

**Authors:** Giovanni Minelli, Antonio Langella, Giovanni B. Dessy, Lorenzo Amatucci, Giulio Turrisi et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32271) | [PDF](https://arxiv.org/pdf/2610.32271)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Mounting the same arm on a quadruped extends the workspace to the entire floor, but fundamentally changes the embodiment: rather than controlling the arm in isolation, the policy must jointly coordinate base navigation, body posture, and end-eff...

</details>

<details>
<summary>Share</summary>

```
From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot.

arXiv: https://arxiv.org/abs/2610.32271

#VLA #robotics
```

</details>

---

### [Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems](https://arxiv.org/abs/2610.32208)

**Authors:** Christian A. Rogers, Qian Lin, Daniel S. Brown

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32208) | [PDF](https://arxiv.org/pdf/2610.32208)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as powerful general-purpose robot policies, but their successes and failures remain difficult to diagnose and understand. In this work, we show that sparse autoencoder (SAE) representations of OpenVLA activations contain outcome-predictive information and can be used to predict task failure before the robot reaches an unrecoverable state. Moreover, to provide insights into what common behaviors may contribute to these outcomes, we identify individual SAE features whose strong activations are associated with specific stages of success or failure,...

</details>

<details>
<summary>Share</summary>

```
Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

Vision-Language-Action (VLA) models have emerged as powerful general-purpose robot policies, but their successes and failures remain difficult to diagnose and understand.

arXiv: https://arxiv.org/abs/2610.32208

#VLA #robotics
```

</details>

---

### [DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning](https://arxiv.org/abs/2610.32093)

**Authors:** Minho Park, Kinam Kim, Donghu Kim, Byungkun Lee, Dongyoon Hwang et al. (9 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32093) | [PDF](https://arxiv.org/pdf/2610.32093) | [Project Page](https://davian-robotics.github.io/DiscoDemo)

<details>
<summary>Abstract</summary>

Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly. We study reinforcement learning (RL) not as a deployable controller, but as a data generator for downstream visuomotor imitation learning. Our key premise is that multiple successful solution modes cover a broader range of successful trajectories than repeatedly collecting a single narrow solution. We introduce DiscoDemo, which trains a privileged latent-conditioned RL generator with a parallel reverse curriculum and a success-gate...

</details>

<details>
<summary>Share</summary>

```
DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly.

arXiv: https://arxiv.org/abs/2610.32093
Project page: https://davian-robotics.github.io/DiscoDemo

#VLA #robotics
```

</details>

---

### [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)

**Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, Jiaying Xu, Shangding Gu et al. (8 authors)

**Published:** 2026-10-23 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32971) | [PDF](https://arxiv.org/pdf/2610.32971) | [Project Page](https://robustrl-lib.github.io/)

<details>
<summary>Abstract</summary>

Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, offline, and safe RL algorithms under a unified interface for substantially improved reusability, to...

</details>

<details>
<summary>Share</summary>

```
RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions.

arXiv: https://arxiv.org/abs/2610.32971
Project page: https://robustrl-lib.github.io/

#VLA #robotics
```

</details>

---

### [Retiming Robot Demonstrations with a Learned Speed Prior](https://arxiv.org/abs/2610.32676)

**Authors:** Seungyong Moon, Deokjae Lee, Hansang Lee, Munkhtselmeg Battsengel, Youngin Kim et al. (10 authors)

**Published:** 2026-10-23 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32676) | [PDF](https://arxiv.org/pdf/2610.32676) | [Project Page](https://mllab.snu.ac.kr/projects/learned_speed_prior)

<details>
<summary>Abstract</summary>

The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself. As a result, the same motion can appear at widely different speeds across demonstrations, and policies trained on such data may inherit operator-specific timing along with task behavior. We propose to learn a speed prior directly from large-scale demonstration data. Given a task instruction, a motion path and the images along it, it predicts a distribution over execution speed along the path, from which a chosen quantile defines a consistent clock for retiming each demonstration. Existing...

</details>

<details>
<summary>Share</summary>

```
Retiming Robot Demonstrations with a Learned Speed Prior

The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself.

arXiv: https://arxiv.org/abs/2610.32676
Project page: https://mllab.snu.ac.kr/projects/learned_speed_prior

#VLA #robotics
```

</details>

---

### [Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](https://arxiv.org/abs/2610.31859)

**Authors:** Shubham Singh

**Published:** 2026-10-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.31859) | [PDF](https://arxiv.org/pdf/2610.31859)

<details>
<summary>Abstract</summary>

When a vision-language-action (VLA) model is fine-tuned with its trainable weights in bfloat16 (bf16) and no fp32 master copy, AdamW writes each update straight into bf16, silently rounding away any update smaller than 1/512 of a weight. In 9 of 12 open VLA codebases a default or documented recipe trains this way, 4 on full weight matrices, including LeRobot's SmolVLA default and its $π_0$/$π_{0.5}$ guides. In our LIBERO runs without the copy, a probe every 100 steps finds at least 79% of updates to bf16 weights erased. On the Hugging Face Hub, 99% of sampled full-weight SmolVLA fine-tunes sto...

</details>

<details>
<summary>Share</summary>

```
Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates

When a vision-language-action (VLA) model is fine-tuned with its trainable weights in bfloat16 (bf16) and no fp32 master copy, AdamW writes each update straight into bf16, silently rounding away any update smaller tha...

arXiv: https://arxiv.org/abs/2610.31859

#VLA #robotics
```

</details>

---

### [When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning](https://arxiv.org/abs/2610.32431)

**Authors:** Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang, Bing Zheng, Zhaolin Wang et al. (6 authors)

**Published:** 2026-10-23 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.32431) | [PDF](https://arxiv.org/pdf/2610.32431)

<details>
<summary>Abstract</summary>

A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside the errors they aim to correct. Ideal stopping conditions for failure feedback are characterized using success-probability and policy-score martingales. At these stops, the removed gradient contribution has zero conditional expectation given the retained information. Truncation therefore preserves th...

</details>

<details>
<summary>Share</summary>

```
When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure.

arXiv: https://arxiv.org/abs/2610.32431

#VLA #robotics
```

</details>

---

### [TTT in VLA Models: Exploring Training with Human Demonstrations](https://arxiv.org/abs/2610.32094)

**Authors:** Qiangong Zhou, Jiafeng Liang, Yimin Dong, Yang He, Hongxiang Li

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.32094) | [PDF](https://arxiv.org/pdf/2610.32094)

<details>
<summary>Abstract</summary>

Long-horizon robot tasks require retaining and using past information. We integrate Test-Time Training (TTT), which stores context in fast weights, into InternVLA-A1 and Pi0.5 to study action generation conditioned on human demonstrations through training on paired demonstrations and robot trajectories. We implement memory transfer between the two phases and truncated backpropagation, and examine training objectives, gradient coverage, and contrastive regularization across video, short-video, and single-frame cue tasks. In our experiments, adding TTT and training on paired data at the current...

</details>

<details>
<summary>Share</summary>

```
TTT in VLA Models: Exploring Training with Human Demonstrations

Long-horizon robot tasks require retaining and using past information.

arXiv: https://arxiv.org/abs/2610.32094

#VLA #robotics
```

</details>

---

## World Models (8)

### [See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762)

**Authors:** Jiawei Chen, Yinxi Wang, Zihan Yang, Meijun Gao, Yaowei Liu et al. (15 authors)

**Published:** 2026-10-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.31762) | [PDF](https://arxiv.org/pdf/2610.31762) | [Project Page](https://wang-yinxi.github.io/representnav/)

<details>
<summary>Abstract</summary>

What visual representation should a navigation policy act on? Navigation policies built on vision foundation models largely leave representation design to the encoders' pretraining objectives. We present RepresentNav, a navigation foundation model built on a self-constructed representation space: a visual representation constructed by the policy's own objectives from vision foundation models. RepresentNav builds this space with Representation Residuals, a compact three-layer transformer that attends over features spanning the full depth of multiple complementary vision foundation models, so th...

</details>

<details>
<summary>Share</summary>

```
See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

What visual representation should a navigation policy act on?

arXiv: https://arxiv.org/abs/2610.31762
Project page: https://wang-yinxi.github.io/representnav/

#worldmodels #robotics
```

</details>

---

### [UniAction: Unified Action Conditioning for World Models](https://arxiv.org/abs/2610.32977)

**Authors:** Bowen Xue, Zizhang Li, Hong-Xing Yu, Jiajun Wu

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.32977) | [PDF](https://arxiv.org/pdf/2610.32977) | [Project Page](https://uniaction.github.io/)

<details>
<summary>Abstract</summary>

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity and a continuous spatiotemporal grounding coordinate. By mapping these coordinates directly into the pretrained video model's native positional space, UniAction allows heterogeneous actions to condit...

</details>

<details>
<summary>Share</summary>

```
UniAction: Unified Action Conditioning for World Models

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across...

arXiv: https://arxiv.org/abs/2610.32977
Project page: https://uniaction.github.io/

#worldmodels #robotics
```

</details>

---

### [Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection](https://arxiv.org/abs/2610.32742)

**Authors:** Luke Beddow, George Mavroghenis, Rodrigo Chacon Quesada, Kamil Dreczkowski, Cong Sun et al. (8 authors)

**Published:** 2026-10-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.32742) | [PDF](https://arxiv.org/pdf/2610.32742)

<details>
<summary>Abstract</summary>

Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures. Current anomaly detection approaches often rely on direct access to the monitored system by utilizing onboard sensors, such as motor encoders, to detect anomalous states. However, legacy hardware often lacks these sensors, or strict security protocols may prohibit access altogether. We therefore present AWARE, a world model framework that is capable of anomaly detection using only external camera monitoring via system dynamics estimation and state prediction. Evaluated acro...

</details>

<details>
<summary>Share</summary>

```
Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection

Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures.

arXiv: https://arxiv.org/abs/2610.32742

#worldmodels #robotics
```

</details>

---

### [UniWorld: A Unified World Model for Real-Time Visual World Simulation](https://arxiv.org/abs/2610.32381)

**Authors:** Xin Zhang, Yabo Chen, Shuaiwei Wang, Zixuan Duan, Haibin Huang et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.32381) | [PDF](https://arxiv.org/pdf/2610.32381)

<details>
<summary>Abstract</summary>

Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance. We present UniWorld, a unified framework that integrates depth trajectories and reference appearance within a shared video generation model. The central design maintains visual and geometric histories on a common timeline. Noise-aligned overlapping continuation places generated history at the prescribed sampling noise level and commits only newly generated latents. Rolling depth latent state preserves the corresponding geometric controls, incrementally reads newly available geome...

</details>

<details>
<summary>Share</summary>

```
UniWorld: A Unified World Model for Real-Time Visual World Simulation

Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance.

arXiv: https://arxiv.org/abs/2610.32381

#worldmodels #robotics
```

</details>

---

### [DT-JEPA: Learning to Predict Future Representations for Decision-Making](https://arxiv.org/abs/2610.32657)

**Authors:** Changxu Ni, Yiyang Ni, Jun Li, Feiran You, Hongyang Du et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.32657) | [PDF](https://arxiv.org/pdf/2610.32657)

<details>
<summary>Abstract</summary>

Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories. However, treating expected future returns as the condition provides an incomplete description of the future, as trajectories with different state transitions and behaviors may share similar returns. Moreover, expected future returns inherently depend on task-specific reward functions, which makes policy learning reliant on reward-labeled datasets and restricts its scalability to tasks with si...

</details>

<details>
<summary>Share</summary>

```
DT-JEPA: Learning to Predict Future Representations for Decision-Making

Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories.

arXiv: https://arxiv.org/abs/2610.32657

#worldmodels #robotics
```

</details>

---

### [$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model](https://arxiv.org/abs/2610.32177)

**Authors:** Khai Loong Aw, Klemen Kotar, Baihan Zhang, Yifan Liu, Lilian Chen et al. (8 authors)

**Published:** 2026-10-23 | **Categories:** cs.AI, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.32177) | [PDF](https://arxiv.org/pdf/2610.32177)

<details>
<summary>Abstract</summary>

Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds. Achieving this flexibility is a major open challenge in AI: capabilities often remain separated across specialized models, limiting how they can be composed and jointly adapted to a task. We introduce $Ψ$-0.6, a unified vision-language world model that adaptively composes perception, language, geometry, and simulation within a shared reasoning process we call streams of thought. These streams interleave images, text, and explicit representations of geometry and motion, all of which t...

</details>

<details>
<summary>Share</summary>

```
$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model

Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds.

arXiv: https://arxiv.org/abs/2610.32177

#worldmodels #robotics
```

</details>

---

### [ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences](https://arxiv.org/abs/2610.32222)

**Authors:** Shibo Hong, Siyu Ren, FengJiao Chen, Zhongyuan Peng, Wei Shi et al. (6 authors)

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.32222) | [PDF](https://arxiv.org/pdf/2610.32222)

<details>
<summary>Abstract</summary>

Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matching optimization. Realizing this potential requires reward signals that reliably rank videos by both VQ and AF. However, existing rewards capture only one dimension: metric-based rewards assess VQ but require ground-truth videos and do not directly assess AF, while inverse dynamics model (IDM) rewards assess AF without references but do not guarantee VQ. Moreover, IDMs, typically tr...

</details>

<details>
<summary>Share</summary>

```
ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences

Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matchin...

arXiv: https://arxiv.org/abs/2610.32222

#worldmodels #robotics
```

</details>

---

### [Interpreting Physics in Video Encoders using Multi-Object Interaction Videos](https://arxiv.org/abs/2610.31983)

**Authors:** Ayushi Mehrotra, Sai Vidyaranya Nuthalapati

**Published:** 2026-10-22 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.31983) | [PDF](https://arxiv.org/pdf/2610.31983)

<details>
<summary>Abstract</summary>

Video encoder models are increasingly used as world models for physical AI, where a policy plans by rolling out the latent, so what physics the latent holds bounds what the agent can plan over. Moreover, existing interpretability work probes quantities belonging to a single object; the quantities that make physics relational, such as momentum transfer, restitution, and friction, are defined between bodies and have not been examined. We probe relational physics attributes in two frozen self-supervised video encoders (V-JEPA2 and VideoMAE) under two-body settings and test if they transfer across...

</details>

<details>
<summary>Share</summary>

```
Interpreting Physics in Video Encoders using Multi-Object Interaction Videos

Video encoder models are increasingly used as world models for physical AI, where a policy plans by rolling out the latent, so what physics the latent holds bounds what the agent can plan over.

arXiv: https://arxiv.org/abs/2610.31983

#worldmodels #robotics
```

</details>

---
