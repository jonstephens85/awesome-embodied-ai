# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-17 22:38 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models](https://arxiv.org/abs/2607.14739v1)

**Authors:** Wei Li, Peijin Jia, Yuan Ma, Xuefeng Jiang, Titong Jiang et al. (12 authors)

**Published:** 2026-07-16 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.14739v1) | [PDF](https://arxiv.org/pdf/2607.14739v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics. Existing visual foresight methods predict future visual states but lack explicit motion guidance: they show where to go but not how to get there. We argue that future feature prediction and sparse point tracking are naturally complementary: the former provi...

</details>

---

### [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275v1)

**Authors:** Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge et al. (11 authors)

**Published:** 2026-07-16 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.15275v1) | [PDF](https://arxiv.org/pdf/2607.15275v1.pdf) | [Project Page](http://research.nvidia.com/labs/gear/robottt/)

<details>
<summary>Abstract</summary>

Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturb...

</details>

---

### [DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/abs/2607.14280v1)

**Authors:** Pegah Khayatan, Sara Meziane, Jayneel Parekh, Matthieu Cord

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.14280v1) | [PDF](https://arxiv.org/pdf/2607.14280v1.pdf) | [Project Page](https://pegah-kh.github.io/dimas/) | [GitHub](https://github.com/pegah-kh/dimas)

<details>
<summary>Abstract</summary>

Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations. Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these cl...

</details>

---

### [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](https://arxiv.org/abs/2607.14236v1)

**Authors:** Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li et al. (11 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.14236v1) | [PDF](https://arxiv.org/pdf/2607.14236v1.pdf) | [Project Page](https://lift-policy.github.io/)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA polic...

</details>

---

### [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429v1)

**Authors:** Dwip Dalal, Shivansh Patel, Chahit Jain, Jeonghwan Kim, Utkarsh Mishra et al. (10 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13429v1) | [PDF](https://arxiv.org/pdf/2607.13429v1.pdf) | [Project Page](anchoralignvla.github.io) | [GitHub](https://github.com/dwipddalal/Anchor-Align)

<details>
<summary>Abstract</summary>

Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that stan...

</details>

---

## Other Recent Papers

### [CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking](https://arxiv.org/abs/2607.15004v1)

**Authors:** Ruilong Ren, Songsheng Cheng, Yunpeng Zhou, Hanxuan Chen, Xiangyue Wang et al. (12 authors)

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.15004v1) | [PDF](https://arxiv.org/pdf/2607.15004v1.pdf)

<details>
<summary>Abstract</summary>

Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track visible targets effectively, but their performance often degrades when buildings, vegetation, or roadside objects block the line of sight. During sustained occlusion, a policy may lose the target state, execute actions toward an incorrect region, and amplify th...

</details>

---

### [Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation](https://arxiv.org/abs/2607.14852v1)

**Authors:** Yao He, Gan Sun, Wenqi Liang, Fazeng Li, Yang Cong

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14852v1) | [PDF](https://arxiv.org/pdf/2607.14852v1.pdf)

<details>
<summary>Abstract</summary>

Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models. To ...

</details>

---

### [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](https://arxiv.org/abs/2607.14698v1)

**Authors:** Marino Watanabe, Takami Sato, Kentaro Yoshioka

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14698v1) | [PDF](https://arxiv.org/pdf/2607.14698v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals. While adversarial training is the standard countermeasure,...

</details>

---

### [Reflex: Real-Time VLA Control through Streaming Inference](https://arxiv.org/abs/2607.14695v1)

**Authors:** Yuanchun Guo, Bingyan Liu

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14695v1) | [PDF](https://arxiv.org/pdf/2607.14695v1.pdf)

<details>
<summary>Abstract</summary>

Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance P...

</details>

---

### [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](https://arxiv.org/abs/2607.14635v1)

**Authors:** Yufeng Ji, Wenhao Tang, Haoyi Niu, Koushil Sreenath, Yi Wu et al. (6 authors)

**Published:** 2026-07-16 | **Categories:** cs.AI, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14635v1) | [PDF](https://arxiv.org/pdf/2607.14635v1.pdf)

<details>
<summary>Abstract</summary>

Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side process...

</details>

---

### [Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2607.14609v1)

**Authors:** Ruilin Chen, Jingkai Jia, Tong Yang, Xinyu Zhou, Qiao Sun et al. (11 authors)

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14609v1) | [PDF](https://arxiv.org/pdf/2607.14609v1.pdf)

<details>
<summary>Abstract</summary>

Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations with different roles, from perceptual encoding to motor prediction, making it unclear where this supervision should be applied. We study this ...

</details>

---

### [Video = World + Event Stream](https://arxiv.org/abs/2607.15038v1)

**Authors:** Lianghua Huang, Zhi-Fan Wu, Yupeng Shi, Wei Wang, Mengyang Feng et al. (27 authors)

**Published:** 2026-07-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.15038v1) | [PDF](https://arxiv.org/pdf/2607.15038v1.pdf)

<details>
<summary>Abstract</summary>

We present Wan-Streamer v0.3, which reframes our native-streaming interaction model under a single organizing view: a video is a world plus an event stream. The world is the persistent context in which a video unfolds, including the environment, scene, subjects, ambient acoustic conditions, voice characteristics, and other relatively stable conditions. The event stream is everything that changes over time within that world, including scene or environmental changes, subject behavior, speech, and ...

</details>

---

### [AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)

**Authors:** Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang et al. (11 authors)

**Published:** 2026-07-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14997v1) | [PDF](https://arxiv.org/pdf/2607.14997v1.pdf)

<details>
<summary>Abstract</summary>

Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observati...

</details>

---

### [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2607.13926v1)

**Authors:** Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng et al. (6 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13926v1) | [PDF](https://arxiv.org/pdf/2607.13926v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglemen...

</details>

---

### [Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning](https://arxiv.org/abs/2607.14183v1)

**Authors:** Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen et al. (32 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.14183v1) | [PDF](https://arxiv.org/pdf/2607.14183v1.pdf)

<details>
<summary>Abstract</summary>

Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in na...

</details>

---

### [Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning](https://arxiv.org/abs/2607.13818v1)

**Authors:** Xiaopeng Zhang, Yueyang Weng, Qi Liu, Yongjin Mu, Yanjie Li

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13818v1) | [PDF](https://arxiv.org/pdf/2607.13818v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution deviates from its nominal behavior. In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, a...

</details>

---

### [UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following](https://arxiv.org/abs/2607.13621v1)

**Authors:** Kun Yu, Jianhua Yang, Yixiang Chen, Changwei Wang, Hongyuan Yu et al. (10 authors)

**Published:** 2026-07-15 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.13621v1) | [PDF](https://arxiv.org/pdf/2607.13621v1.pdf)

<details>
<summary>Abstract</summary>

Language-guided human following is an important capability for embodied agents, but existing benchmarks typically assume that the target person is visible at the start of an episode. This setting simplifies the problem and overlooks a more realistic requirement: an agent often needs to first find a language-described target and then persistently follow that target in a dynamic environment. While recent work has started to study human search, existing settings are typically evaluated in task-spec...

</details>

---

### [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](https://arxiv.org/abs/2607.13605v1)

**Authors:** Yingwei Ji

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13605v1) | [PDF](https://arxiv.org/pdf/2607.13605v1.pdf)

<details>
<summary>Abstract</summary>

One high-level instruction in long-horizon manipulation can cover several action stages. We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks. A progress module tracks the active stage, while the action policy receives stage information either as current-stage text or as a normalized ordinal stage index in robot state. We compare these interfaces with GR00T N1.6 on LIBERO-10 under direct fine-tuning and continuation fine-tu...

</details>

---

### [Semantic Anchoring for Robotic Action Representations](https://arxiv.org/abs/2607.13597v1)

**Authors:** Yuan Xu, Youheng Shi, Chengyang Li, Wentao Zhu, Yizhou Wang

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13597v1) | [PDF](https://arxiv.org/pdf/2607.13597v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit rich semantic representations from pretrained Vision-Language Models, yet fine-tuning on limited robot demonstrations degrades this structure and undermines generalization. A fundamental question therefore arises: what constitutes a good action representation? Inspired by the mirror neuron theory's insight that observation and execution share an intention-level encoding, we examine whether a robot's action representations preserve the semantic structur...

</details>

---
