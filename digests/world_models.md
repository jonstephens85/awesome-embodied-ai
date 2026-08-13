# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-13 22:30 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video](https://arxiv.org/abs/2608.11017v1)

**Authors:** Ke Ma, Yamin Mao, Weiming Li, Shuai Tan, Yijie Zhong et al. (8 authors)

**Published:** 2026-08-11 | **Categories:** cs.CV, cs.AI, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2608.11017v1) | [PDF](https://arxiv.org/pdf/2608.11017v1.pdf) | [Project Page](https://dualtransparency.github.io/R4DSG/)

<details>
<summary>Abstract</summary>

Long-horizon egocentric video is a rich substrate for wearable AI assistants, but object-centric questions such as where an item was moved, when it last changed state, or why it was relocated remain difficult because caption- and transcript-based memories rarely preserve persistent object identity or structured spatial change. Existing long-video QA methods mainly emphasize temporal grounding and clip retrieval, while prior 3D scene-graph methods typically assume stronger geometry than free-moti...

</details>

---

### [PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots](https://arxiv.org/abs/2608.10449v2)

**Authors:** Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang et al. (11 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10449v2) | [PDF](https://arxiv.org/pdf/2608.10449v2.pdf) | [Project Page](of)

<details>
<summary>Abstract</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples ...

</details>

---

## Other Recent Papers

### [Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models](https://arxiv.org/abs/2608.12078v1)

**Authors:** Shukrullo Nazirjonov, Sai Prasanna, Anna Manasyan, Georg Martius

**Published:** 2026-08-12 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.12078v1) | [PDF](https://arxiv.org/pdf/2608.12078v1.pdf)

<details>
<summary>Abstract</summary>

Learning world models from offline trajectories enables agents to accomplish different tasks through planning. Object-centric (OC) representations, which decompose a scene into a set of slots that bind to its objects, have been proposed as an inductive bias for world models that are more sample-efficient and generalize better. Yet prior object-centric world models (OCWMs) take the slot encoder as given and evaluate only in-distribution, leaving open whether the object-centric bias actually deliv...

</details>

---

### [How Can Driving World Models Do Counterfactual Prediction?](https://arxiv.org/abs/2608.11601v1)

**Authors:** Jiaru Zhang, Can Cui, Yi Xu, Xin Ye, Ruqi Zhang et al. (6 authors)

**Published:** 2026-08-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.11601v1) | [PDF](https://arxiv.org/pdf/2608.11601v1.pdf)

<details>
<summary>Abstract</summary>

Driving world models are often interpreted as counterfactual simulators for observed driving episodes: given a factual driving log, they are asked what would have happened under an alternative ego action. In this paper, we identify a fundamental mismatch between this goal and direct action-conditioned prediction. The direct prediction uses the shared history and the alternative action but not the factual continuation observed after that history. It can therefore generate a plausible future witho...

</details>

---

### [Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning](https://arxiv.org/abs/2608.11204v1)

**Authors:** Wenrui Bao, Tianyun Jiang, Zhiben Chen, Ser-Nam Lim, Peter D. Peng et al. (6 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.11204v1) | [PDF](https://arxiv.org/pdf/2608.11204v1.pdf)

<details>
<summary>Abstract</summary>

Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is comparatively inexpensive and abundant relative to synchronized video--kinematics trajectories, and a natural way to exploit it is to learn world models o...

</details>

---

### [VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174v2)

**Authors:** Haiyu Wu, Randall Balestriero, Morgan Levine

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11174v2) | [PDF](https://arxiv.org/pdf/2608.11174v2.pdf)

<details>
<summary>Abstract</summary>

Regulating the latent space to an isotropic Gaussian distribution provides a stable and information-maximized landscape for world model planning. However, the latent space property and successful planning remain disconnected. We first study this by comparing SIGReg and VISReg, two regularization loss functions with the same distribution target but different properties. Compared with SIGReg, VISReg has more flexibility in controlling the weights of center, scale, and shape regularization, and a l...

</details>

---

### [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915v2)

**Authors:** Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Yao et al. (22 authors)

**Published:** 2026-08-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.10915v2) | [PDF](https://arxiv.org/pdf/2608.10915v2.pdf)

<details>
<summary>Abstract</summary>

After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeli...

</details>

---

### [Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618v1)

**Authors:** Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He et al. (11 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10618v1) | [PDF](https://arxiv.org/pdf/2608.10618v1.pdf)

<details>
<summary>Abstract</summary>

Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicl...

</details>

---

### [Stream Forcing: Constructing Unified Training Trajectory for Robust Streaming Video Generation](https://arxiv.org/abs/2608.10439v1)

**Authors:** Yueting Zhu, Yuehao Song, Kaicheng Zhang, Bao Tang, Shaoyu Chen et al. (8 authors)

**Published:** 2026-08-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10439v1) | [PDF](https://arxiv.org/pdf/2608.10439v1.pdf)

<details>
<summary>Abstract</summary>

Streaming video generation holds strong potential for world modeling, where future frames must be inferred online sequentially to form a continuous video stream. However, streaming video diffusion models introduce a fundamental train-inference mismatch: inference follows a specialized denoising order, whereas advanced training strategies typically require diverse noise-level configurations. To address this trade-off between train-inference consistency and training coverage, we reformulate the vi...

</details>

---

### [Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving](https://arxiv.org/abs/2608.10386v1)

**Authors:** Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong

**Published:** 2026-08-11 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10386v1) | [PDF](https://arxiv.org/pdf/2608.10386v1.pdf)

<details>
<summary>Abstract</summary>

Sample-efficient reinforcement learning for autonomous driving is often limited by the trade-off between data efficiency and model bias. While world models reduce the reliance on costly environment interactions, policy optimization over learned dynamics remains sensitive to prediction errors. This paper proposes the Dreamer-SAC framework, which integrates a recurrent state-space world model with an off-policy soft actor-critic algorithm trained directly in latent space. The framework uses a comb...

</details>

---
