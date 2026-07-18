# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-18 22:38 UTC

**Papers found:** 10

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
