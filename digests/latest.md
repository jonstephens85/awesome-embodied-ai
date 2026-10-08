# What's New

Papers discovered in the run at **2026-10-08 01:26 UTC**.

**New this run:** 25

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (1)

### [RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning](https://arxiv.org/abs/2610.09455)

**Authors:** Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin

**Published:** 2026-10-07 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09455) | [PDF](https://arxiv.org/pdf/2610.09455) | [Project Page](https://seungjun-moon.github.io/rlhnd/)

<details>
<summary>Abstract</summary>

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy training. To this end, we propose RLHND, a video foundation model-based hand tracking model that jointly estimates hand pose and realistic tactile information from monocular egocen...

</details>

<details>
<summary>Share</summary>

```
RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent.

arXiv: https://arxiv.org/abs/2610.09455
Project page: https://seungjun-moon.github.io/rlhnd/

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (12)

### [Juno: Taming Predictive Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.09940)

**Authors:** Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09940) | [PDF](https://arxiv.org/pdf/2610.09940) | [Project Page](https://juno-policy.github.io/)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predict...

</details>

<details>
<summary>Share</summary>

```
Juno: Taming Predictive Latents for Vision-Language-Action Models

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2610.09940
Project page: https://juno-policy.github.io/

#VLA #robotics
```

</details>

---

### [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](https://arxiv.org/abs/2610.09718)

**Authors:** Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu, Hanlong Li, Tatsuya Matsushima et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09718) | [PDF](https://arxiv.org/pdf/2610.09718) | [Project Page](https://yubi-stag.airoa.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grounding that automatically enriches manipulation demonstrations with interaction-rich semantics to ali...

</details>

<details>
<summary>Share</summary>

```
YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions.

arXiv: https://arxiv.org/abs/2610.09718
Project page: https://yubi-stag.airoa.io/

#VLA #robotics
```

</details>

---

### [TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks](https://arxiv.org/abs/2610.09462)

**Authors:** Zirun Zhou, Jingfeng Zhang, HaoChuan Xu, Xizhe Zhang, Elliott Wen et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09462) | [PDF](https://arxiv.org/pdf/2610.09462) | [Project Page](https://zzr42.github.io/tmt/)

<details>
<summary>Abstract</summary>

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears. Detecting such activation is difficult because malicious behavior can comprise individually plausible actions, while unfamiliar tasks introduce legitimate changes in observations and behavior. We introduce TMT, a runtime backdoor detector based on Token Manifold and latent Transition modeling. Trained on benign rollouts, its two branches assess input-token structure and prediction errors in adjacent-layer latent dynamics. A suspicious rollout identifie...

</details>

<details>
<summary>Share</summary>

```
TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears.

arXiv: https://arxiv.org/abs/2610.09462
Project page: https://zzr42.github.io/tmt/

#VLA #robotics
```

</details>

---

### [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09451)

**Authors:** Yeonseo Lee, Hyosup Shin, Guebin Hwang, Sungho Jo

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09451) | [PDF](https://arxiv.org/pdf/2610.09451) | [Project Page](https://lysees.github.io/tempobridge-page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextual VLM representations, aligns them with task progress through a causal phase router, and modulates n...

</details>

<details>
<summary>Share</summary>

```
TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly.

arXiv: https://arxiv.org/abs/2610.09451
Project page: https://lysees.github.io/tempobridge-page/

#VLA #robotics
```

</details>

---

### [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](https://arxiv.org/abs/2610.09496)

**Authors:** Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09496) | [PDF](https://arxiv.org/pdf/2610.09496)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened attention to task-relevant visual regions, and a mechanistic interpretation via sparse autoencoders...

</details>

<details>
<summary>Share</summary>

```
Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models.

arXiv: https://arxiv.org/abs/2610.09496

#VLA #robotics
```

</details>

---

### [Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228)

**Authors:** Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang et al. (7 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09228) | [PDF](https://arxiv.org/pdf/2610.09228) | [Project Page](https://robo-cop.pages.dev/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bo...

</details>

<details>
<summary>Share</summary>

```
Co-Evolving Robot Orchestrators and Policies through Deployment

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment.

arXiv: https://arxiv.org/abs/2610.09228
Project page: https://robo-cop.pages.dev/

#VLA #robotics
```

</details>

---

### [PAIR: Bridging Perception and Action in Vision-Language-Action Models](https://arxiv.org/abs/2610.09016)

**Authors:** Kaixi Feng, Guoheng Sun, Ang li

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09016) | [PDF](https://arxiv.org/pdf/2610.09016)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Lat...

</details>

<details>
<summary>Share</summary>

```
PAIR: Bridging Perception and Action in Vision-Language-Action Models

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions.

arXiv: https://arxiv.org/abs/2610.09016

#VLA #robotics
```

</details>

---

### [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](https://arxiv.org/abs/2610.09943)

**Authors:** Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun et al. (8 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09943) | [PDF](https://arxiv.org/pdf/2610.09943)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternative strategies under distribution shifts. Inspired by this, we introduce DRIVE (Diversity-driven RL fI...

</details>

<details>
<summary>Share</summary>

```
Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited.

arXiv: https://arxiv.org/abs/2610.09943

#VLA #robotics
```

</details>

---

### [DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09144)

**Authors:** Kaixi Feng, Guoheng Sun, Ziyao Wang, Yexiao He, Zheyu Shen et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09144) | [PDF](https://arxiv.org/pdf/2610.09144)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tokens influence policy computation. We introduce DIVA, a Dual-Space Intent-Aware Visual Attenuation module with an anchor-then-attenuate design. DIVA combines high-level task intent with low-level visual evidence to estimate patch-wise relevance anchors, then applies them in two complementary spaces: it reweights projected visual tokens before backbone entry and persistently attenua...

</details>

<details>
<summary>Share</summary>

```
DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tok...

arXiv: https://arxiv.org/abs/2610.09144

#VLA #robotics
```

</details>

---

### [CARE: Certifying Acceleration for Vision-Language-Action Inference](https://arxiv.org/abs/2610.08917)

**Authors:** Rui Liu, Tong Zheng, Jindong Gu, Zhipeng Wang

**Published:** 2026-10-06 | **Categories:** cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08917) | [PDF](https://arxiv.org/pdf/2610.08917)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive. Prior work accelerates VLA inference using techniques like action chunking and visual-token pruning, typically evaluating based on latency and average task success. However, acceleration may discard information and break tasks the original policy would solve, a risk hidden by average metrics. Measuring these failures is challenging because action deviations compound over closed-loop trajectories, meaning task failure is only observable across full episodes. We therefore define...

</details>

<details>
<summary>Share</summary>

```
CARE: Certifying Acceleration for Vision-Language-Action Inference

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive.

arXiv: https://arxiv.org/abs/2610.08917

#VLA #robotics
```

</details>

---

### [RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies](https://arxiv.org/abs/2610.09696)

**Authors:** Mimo Shirasaka, Takehiko Ohkawa, Takuya Okubo, Nicola Scianca, Tatsuya Matsushima et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09696) | [PDF](https://arxiv.org/pdf/2610.09696)

<details>
<summary>Abstract</summary>

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands. Vision-Language-Action (VLA) policies trained on such data inherit the demonstrator's timing. Yet human timing does not directly transfer to robots: compliant hands tolerate fast contact, whereas robots may overshoot due to actuator and tracking limitations; conversely, robots can move faster in free space. This motivates a unified approach that reconciles execution speed with contact safety...

</details>

<details>
<summary>Share</summary>

```
RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands.

arXiv: https://arxiv.org/abs/2610.09696

#VLA #robotics
```

</details>

---

### [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)

**Authors:** Haoran Chen, Jingtian Ji, Samuel Wheeler, Kaylene Caswell Stocking, Matthew Walter

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09170) | [PDF](https://arxiv.org/pdf/2610.09170)

<details>
<summary>Abstract</summary>

Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space. Many action tokenizers learn the mapping between tokens and actions via a reconstruction objective. However, as we show through extensive analysis, sufficiently accurate action reconstruction is only one part of what makes a downstream robot policy successful. It is also critical that the policy is able to predict the right tokens for new observations, and that unseen policy token predictions still decode in...

</details>

<details>
<summary>Share</summary>

```
Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space.

arXiv: https://arxiv.org/abs/2610.09170

#VLA #robotics
```

</details>

---

## World Models (12)

### [Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation](https://arxiv.org/abs/2610.09309)

**Authors:** Tzu-Yu Chuang, Ching-Hsiang Chang, Yi-Hsiu Lee, Yi-Ting Chen, Min Sun et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★★★

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09309) | [PDF](https://arxiv.org/pdf/2610.09309) | [Project Page](https://claire0730.github.io/executable-goals/) | [Code](https://github.com/Claire0730/executable-goals)

<details>
<summary>Abstract</summary>

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control. When training supervises future prediction alone, terminal goal accuracy is not an explicit learning objective, even when geometric recovery is available. We present Entity-Level Goal Readout, a learned prediction-to-execution interface that makes the executable terminal goal an explicit output of a 3D trace world model. It combines object-centric pose prediction with translation grounded in obser...

</details>

<details>
<summary>Share</summary>

```
Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control.

arXiv: https://arxiv.org/abs/2610.09309
Project page: https://claire0730.github.io/executable-goals/
Code: https://github.com/Claire0730/executable-goals

#worldmodels #robotics
```

</details>

---

### [SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation](https://arxiv.org/abs/2610.08941)

**Authors:** Yunheng Liu, Ziqi Cai, Siqi Yang, Yimu Wang, Minggui Teng et al. (10 authors)

**Published:** 2026-10-06 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08941) | [PDF](https://arxiv.org/pdf/2610.08941) | [Project Page](https://alaya-lab.github.io/SPW-Nav)

<details>
<summary>Abstract</summary>

Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement instructions and streams one minute of 2K 360-degree video in real time from a single panorama. SPW-Nav interprets each instruction in the previously generated panorama as camera motion. Spher...

</details>

<details>
<summary>Share</summary>

```
SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation

Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training.

arXiv: https://arxiv.org/abs/2610.08941
Project page: https://alaya-lab.github.io/SPW-Nav

#worldmodels #robotics
```

</details>

---

### [World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models](https://arxiv.org/abs/2610.09134)

**Authors:** Jiuyi Xu, Xiao Hu, Meida Chen, Peng Gao, Yang Ye et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09134) | [PDF](https://arxiv.org/pdf/2610.09134) | [Code](https://github.com/jiuyixu25/CureWM)

<details>
<summary>Abstract</summary>

Robot world models support policy evaluation, planning, and synthetic data generation, but these applications require predictions that distinguish successful actions from failures. Across four released checkpoints from two architecture families, we observe weak sensitivity to action changes and success-like predictions on verified failures. Although recent work incorporates failures into model training, which data can repair released checkpoints without changing their architecture or training objective still remains underexplored. To this end, we introduce CureWM, which constructs alternative...

</details>

<details>
<summary>Share</summary>

```
World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models

Robot world models support policy evaluation, planning, and synthetic data generation, but these applications require predictions that distinguish successful actions from failures.

arXiv: https://arxiv.org/abs/2610.09134
Code: https://github.com/jiuyixu25/CureWM

#worldmodels #robotics
```

</details>

---

### [Controllable Crowd Generation through World-Model Planning](https://arxiv.org/abs/2610.09438)

**Authors:** JunGyu Lee, Jisu Shin, Seunghyun Shin, Hae-Gon Jeon

**Published:** 2026-10-07 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09438) | [PDF](https://arxiv.org/pdf/2610.09438) | [Project Page](https://jungyu0413.github.io/Ctrl-CWM)

<details>
<summary>Abstract</summary>

Crowd simulation plays a central role in robot navigation, autonomous driving, and urban planning. For these applications, realistic simulation requires crowds to adapt their behavior to environmental changes and user objectives. However, existing methods that rely on predefined control settings have limited flexibility in accommodating new user-specified objectives. To address this limitation, we propose Ctrl-CWM, a multi-agent Controllable Crowd World Model that integrates crowd generation and run-time control. Our key idea is to adapt the world-model principle of planning using imagined fut...

</details>

<details>
<summary>Share</summary>

```
Controllable Crowd Generation through World-Model Planning

Crowd simulation plays a central role in robot navigation, autonomous driving, and urban planning.

arXiv: https://arxiv.org/abs/2610.09438
Project page: https://jungyu0413.github.io/Ctrl-CWM

#worldmodels #robotics
```

</details>

---

### [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2610.09763)

**Authors:** Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09763) | [PDF](https://arxiv.org/pdf/2610.09763) | [Project Page](https://mahmoud-selim.github.io/ICDP/)

<details>
<summary>Abstract</summary>

Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous driving, this can be insufficient: a candidate ego trajectory may remain well supported under the marg...

</details>

<details>
<summary>Share</summary>

```
Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving

Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains.

arXiv: https://arxiv.org/abs/2610.09763
Project page: https://mahmoud-selim.github.io/ICDP/

#worldmodels #robotics
```

</details>

---

### [DSReg: Provably Recovering Individual World Latents without Reconstruction](https://arxiv.org/abs/2610.09457)

**Authors:** Yujia Zheng, David Klindt, Randall Balestriero, Bernhard Schölkopf

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09457) | [PDF](https://arxiv.org/pdf/2610.09457) | [Project Page](https://dsreg.github.io/)

<details>
<summary>Abstract</summary>

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear transformation, so individual latents remain mixed. We close this gap: individual world latents can be provably recovered with no reconstruction, no decoder, and no labels. The key cond...

</details>

<details>
<summary>Share</summary>

```
DSReg: Provably Recovering Individual World Latents without Reconstruction

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervi...

arXiv: https://arxiv.org/abs/2610.09457
Project page: https://dsreg.github.io/

#worldmodels #robotics
```

</details>

---

### [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](https://arxiv.org/abs/2610.09285)

**Authors:** Mayank Sengupta, Nirmit Desai, Eric Song, Kunal Sawarkar

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09285) | [PDF](https://arxiv.org/pdf/2610.09285)

<details>
<summary>Abstract</summary>

Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a separate, larger downstream model. To build this model, we choose LeWorldModel (LeWM)as our latent...

</details>

<details>
<summary>Share</summary>

```
LeCuration: A Tiny World Model as a Data Curation Multi-Tool

Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior.

arXiv: https://arxiv.org/abs/2610.09285

#worldmodels #robotics
```

</details>

---

### [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](https://arxiv.org/abs/2610.09335)

**Authors:** Yatai Ji, Zhengqiu Zhu, Yong Zhao, Yue Hu, Fanglong Yao et al. (8 authors)

**Published:** 2026-10-07 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09335) | [PDF](https://arxiv.org/pdf/2610.09335)

<details>
<summary>Abstract</summary>

Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain largely reactive, reasoning over past observations without explicitly predicting future states. World m...

</details>

<details>
<summary>Share</summary>

```
SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models

Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability.

arXiv: https://arxiv.org/abs/2610.09335

#worldmodels #robotics
```

</details>

---

### [ΔWAM: Distilling Action Tangent Fields into World Action Models](https://arxiv.org/abs/2610.09734)

**Authors:** Ke Wu, Hanwen Huang, Bo Gu, Kaizhao Zhang, Xiangting Meng et al. (9 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09734) | [PDF](https://arxiv.org/pdf/2610.09734)

<details>
<summary>Abstract</summary>

World Action Models (WAM) improve robot policies by augmenting sparse action supervision with dense future prediction. However, much of the predictable future is dominated by appearance and scene persistence rather than action-dependent dynamics. We observe that several recent WAM designs, including optical flow, motion-centric representations, and latent actions, can be understood from a common perspective in which world supervision becomes more efficient as it contains a higher proportion of action-relevant variation. Based on this insight, we introduce Action Tangent Fields, which reformula...

</details>

<details>
<summary>Share</summary>

```
ΔWAM: Distilling Action Tangent Fields into World Action Models

World Action Models (WAM) improve robot policies by augmenting sparse action supervision with dense future prediction.

arXiv: https://arxiv.org/abs/2610.09734

#worldmodels #robotics
```

</details>

---

### [Kuration SDK: Addressing the Virtual2Real Gap via Data Curation](https://arxiv.org/abs/2610.09305)

**Authors:** Nirmit Desai, Eric Song, Mayank Sengupta, Tejal Bedmutha, Siri Reddy et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09305) | [PDF](https://arxiv.org/pdf/2610.09305)

<details>
<summary>Abstract</summary>

Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically-grounded metrics. However, for domain and task-agnostic action-conditioned world model training, existing benchmarks provide a limited signal. By training and evaluating diffusion world models on CounterStrike gameplay data, we confirm that qualitative playability does not correspond with metrics such as FVD, LPIPS, and JEDi. We term this the Virtual2Real gap. We posit that, in lieu of reliable benchmarks, curating r...

</details>

<details>
<summary>Share</summary>

```
Kuration SDK: Addressing the Virtual2Real Gap via Data Curation

Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically-grounded metrics.

arXiv: https://arxiv.org/abs/2610.09305

#worldmodels #robotics
```

</details>

---

### [Towards Financial World Modeling](https://arxiv.org/abs/2610.09048)

**Authors:** Humzah Merchant, Alec Guthrie, Simon Mahns, Randall Balestriero, Bradford Levy

**Published:** 2026-10-06 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.09048) | [PDF](https://arxiv.org/pdf/2610.09048)

<details>
<summary>Abstract</summary>

Building a world model requires a state representation useful for planning and decision-making---potentially over tasks unknown at training time. In the context of financial markets, planning and decision-making may require a model to reason about market-wide conditions, asset-specific expected returns, liquidity, volatility, and cross-asset relationships. Yet financial representation learning has largely been evaluated on individual predictive tasks, oftentimes on a single time period using comparatively narrow datasets. We address this through three primary contributions. First, we introduce...

</details>

<details>
<summary>Share</summary>

```
Towards Financial World Modeling

Building a world model requires a state representation useful for planning and decision-making---potentially over tasks unknown at training time.

arXiv: https://arxiv.org/abs/2610.09048

#worldmodels #robotics
```

</details>

---

### [Directed Temporal Representations for Offline Visual Control](https://arxiv.org/abs/2610.08960)

**Authors:** Chenyang Yuan, Haoyu Wang, Zhuo Sun, Xiaoyuan Cheng

**Published:** 2026-10-06 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.08960) | [PDF](https://arxiv.org/pdf/2610.08960)

<details>
<summary>Abstract</summary>

Predictive world models provide compact visual representations for control. Control requires a latent geometry aligned with temporal reachability rather than predictive similarity alone. We introduce Directed Temporal Representations for Control (DTRC), which learns such a geometry from offline visual trajectories on top of frozen LeWorldModel (LeWM) features. DTRC constructs a directed temporal quasimetric over the learned control representation. Short-range temporal offsets calibrate the distance scale. Bootstrapped targets extend temporal reachability across longer horizons. Action-conditio...

</details>

<details>
<summary>Share</summary>

```
Directed Temporal Representations for Offline Visual Control

Predictive world models provide compact visual representations for control.

arXiv: https://arxiv.org/abs/2610.08960

#worldmodels #robotics
```

</details>

---
