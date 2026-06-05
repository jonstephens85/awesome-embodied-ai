# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-05 22:57 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators](https://arxiv.org/abs/2606.06476v1)

**Authors:** Chenming Zhu, Jingli Lin, Yilin Long, Peizhou Cao, Tai Wang et al. (7 authors)

**Published:** 2026-06-04 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.06476v1) | [PDF](https://arxiv.org/pdf/2606.06476v1.pdf) | [Project Page](https://zcmax.github.io/projects/Thinking-With-Imagination)

<details>
<summary>Abstract</summary>

While Vision-Language Models (VLMs) have shown strong visual reasoning capabilities, their spatial reasoning abilities remain largely constrained to the observed images and text-oriented chain-of-thought. They often struggle to infer unobserved layouts, maintain cross-view consistency, and reason from alternative viewpoints when only limited egocentric observations are available. In this work, we study this problem as thinking with imagination, where a VLM actively acquires imagined visual evide...

</details>

---

### [OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics](https://arxiv.org/abs/2606.04463v2)

**Authors:** Zhuoyuan Wu, Jun Gao

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04463v2) | [PDF](https://arxiv.org/pdf/2606.04463v2.pdf) | [Project Page](https://wuzy2115.github.io/oscar-project-page/)

<details>
<summary>Abstract</summary>

We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments and enables robot policy evaluation. Existing video world models face three main challenges for real-world robot evaluation: limited scenario diversity in current robot training datasets, imprecise action following, and poor generalization across embodiments for broad adoption. We tackle these challenges from two perspectives. At its core is a large-scale standardized data pipelin...

</details>

---

## Other Recent Papers

### [MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action](https://arxiv.org/abs/2606.06245v1)

**Authors:** Boyang Zhang, Lianlei Shan

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.06245v1) | [PDF](https://arxiv.org/pdf/2606.06245v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies remain brittle in long-horizon and high-uncertainty control, where one-pass action decoding provides limited inference-time deliberation. Explicit chain-of-thought can increase reasoning depth, but introduces token latency and an indirect text-to-action interface. We propose MPCoT, a reward-guided multi-path latent reasoning framework that initializes $M$ hypotheses, refines them for K weight-tied steps, and softly aggregates them before action decoding. A t...

</details>

---

### [WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation](https://arxiv.org/abs/2606.06147v1)

**Authors:** Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao et al. (8 authors)

**Published:** 2026-06-04 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.06147v1) | [PDF](https://arxiv.org/pdf/2606.06147v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation. However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions. We argue that the ability to "imagine" future states -- inherent in World Models -- is critical for robust decision-making under such partial observability. To address this, we construct a ...

</details>

---

### [PLAN-S: Bridging Planning with Latent Style Dynamics for Autonomous Driving World Models](https://arxiv.org/abs/2606.06014v1)

**Authors:** Xiaoyun Qiu, Jingtao He, Yijie Chen, Yusong Huang, Haotian Wang et al. (7 authors)

**Published:** 2026-06-04 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.06014v1) | [PDF](https://arxiv.org/pdf/2606.06014v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models (LWMs) have strengthened end-to-end autonomous driving by forecasting compact scene dynamics for downstream planning. However, existing LWM-based planners usually generate trajectories directly from entangled latent representations. This compact latent-to-planner pathway lacks explicit modeling of risk, drivability, and diverse style preferences, making driving-style dynamics difficult to supervise, inspect, or modulate before a final trajectory is selected. We propose PLAN-S...

</details>

---

### [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979v1)

**Authors:** Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu et al. (12 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.05979v1) | [PDF](https://arxiv.org/pdf/2606.05979v1.pdf)

<details>
<summary>Abstract</summary>

We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions, conjoining the \emph{world modeling interface} to learn from extensive egocentric videos as in the world-action model (WAM) and the \emph{language reasoning} capacities to solve complex long-horizon tasks as in vision-language-action (VLA) models. At the core of WLA li...

</details>

---

### [Towards a Data Flywheel for Embodied Intelligence in Logistics](https://arxiv.org/abs/2606.05960v1)

**Authors:** Anlan Yu, Zaishu Chen, Zhiqing Hong, Daqing Zhang

**Published:** 2026-06-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05960v1) | [PDF](https://arxiv.org/pdf/2606.05960v1.pdf)

<details>
<summary>Abstract</summary>

Embodied intelligence is moving from laboratory demonstrations toward industrial deployment, with the logistics industry serving as a key application scenario. Learning-based policies offer a promising path beyond traditional perception-planning-control pipelines, but their scalability depends on how embodied data can be collected, organized, and reused. This research studies a data-centric framework for industrial embodied intelligence by constructing a logistics data flywheel. Our framework co...

</details>

---

### [Towards World Models in Biomedical Research](https://arxiv.org/abs/2606.05925v1)

**Authors:** Guangyu Wang, Jingkun Yue, Siqi Zhang, Yu Liu, Xiaoyu Wang et al. (22 authors)

**Published:** 2026-06-04 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.05925v1) | [PDF](https://arxiv.org/pdf/2606.05925v1.pdf)

<details>
<summary>Abstract</summary>

A central goal of biomedicine is to understand, predict and ultimately control the dynamic mechanisms by which biological systems respond to perturbations, disease progression and therapeutic intervention. Although foundation models and large language models have accelerated biomedical data interpretation, most current systems remain focused on static pattern recognition rather than prospective simulation of biological futures. Here we propose biomedical world models as a paradigm for AI-driven ...

</details>

---

### [PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773v1)

**Authors:** Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang et al. (7 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05773v1) | [PDF](https://arxiv.org/pdf/2606.05773v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies operate in a closed loop in real-world robot tasks: a robot observes the scene, executes an action chunk, and conditions its next decision on the resulting observation. However, most existing world models for robot action evaluation are limited to open-loop prediction along pre-collected action trajectories. This prevents them from supporting closed-loop VLA evaluation, where each action chunk must be conditioned on the observation generated by the previous ...

</details>

---

### [DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699v1)

**Authors:** Runfa Blark Li, Kuang-Ting Tu, Nikola Raicevic, Dwait Bhatt, Xinshuang Liu et al. (9 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05699v1) | [PDF](https://arxiv.org/pdf/2606.05699v1.pdf)

<details>
<summary>Abstract</summary>

Bimanual dexterous tool use remains challenging for robots due to high-dimensional hand configurations and complex hand-tool-object dynamics and contact. Most existing control policies depend on future configuration references provided from demonstrations, while future action-conditioned world models require slow online planning over high-dimensional action sequences. A significant challenge is generating a dynamically consistent future reference trajectory without relying on privileged states f...

</details>

---

### [Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645v1)

**Authors:** Ziyang Yao, Haochen Liu, Yuncheng Jiang, Zeyu Zhu, Zibin Guo et al. (13 authors)

**Published:** 2026-06-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05645v1) | [PDF](https://arxiv.org/pdf/2606.05645v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving requires reasoning about how ego actions shape the evolution of the surrounding world. However, most end-to-end methods rely on direct state-to-action mappings, capturing correlations without explicitly modeling action-conditioned dynamics. Conversely, continuous-latent world models often lack compositional structure for causal reasoning across counterfactual futures. We introduce Discrete-WAM, a unified latent vision-action world policy that represents future visual states an...

</details>

---

### [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558v1)

**Authors:** Kaixuan Liu, Guojun Xiong, Weinan Zhang, Shengpu Tang

**Published:** 2026-06-04 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.05558v1) | [PDF](https://arxiv.org/pdf/2606.05558v1.pdf)

<details>
<summary>Abstract</summary>

Evaluating large language model (LLM) agents in multi-turn interactive environments is expensive and risky, as it requires online environment interaction. We propose ADWM (Autoregressive Diffusion World Model), an evaluation framework that estimates the performance of a new LLM agent policy purely from pre-collected trajectories. The core idea is to learn a latent diffusion world model that simulates how the environment responds to the evaluation policy, without ever executing it in the real env...

</details>

---

### [Representation Learning Enables Scalable Multitask Deep Reinforcement Learning](https://arxiv.org/abs/2606.05555v1)

**Authors:** Johan Obando-Ceron, Lu Li, Scott Fujimoto, Pierre-Luc Bacon, Aaron Courville et al. (6 authors)

**Published:** 2026-06-04 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.05555v1) | [PDF](https://arxiv.org/pdf/2606.05555v1.pdf)

<details>
<summary>Abstract</summary>

Scaling reinforcement learning (RL) to diverse multitask settings remains a central challenge. While recent advances in model-based RL achieve strong performance, they rely on planning and complex training pipelines, making it unclear which components are essential for scalability. We revisit this question and argue that the primary driver of scalable multitask RL is not model-based control, but \emph{representation learning}. In particular, we show that combining predictive, model-based represe...

</details>

---

### [Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation](https://arxiv.org/abs/2606.05015v1)

**Authors:** Luca Zanatta, Grzegorz Malczyk, Kostas Alexis

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.05015v1) | [PDF](https://arxiv.org/pdf/2606.05015v1.pdf)

<details>
<summary>Abstract</summary>

World models, learned generative models that predict how an environment evolves, have become a promising tool for sample-efficient robot learning. Yet how robust they are to environmental variability remains poorly understood. To address this, we conduct a systematic study using vision-based quadrotor navigation as a testbed problem, training DreamerV3-based world models under varying levels of environmental randomness and evaluating them across all levels through cross-environment validation, s...

</details>

---

### [Explainably Safe Reinforcement Learning](https://arxiv.org/abs/2606.04634v1)

**Authors:** Sabine Rieder, Stefan Pranger, Debraj Chakraborty, Jan Křetínský, Bettina Könighofer

**Published:** 2026-06-03 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.04634v1) | [PDF](https://arxiv.org/pdf/2606.04634v1.pdf)

<details>
<summary>Abstract</summary>

Trust in a decision-making system requires both safety guarantees and the ability to interpret and understand its behavior. This is particularly important for learned systems, whose decision-making processes are often highly opaque. Shielding is a prominent model-based technique for enforcing safety in reinforcement learning. However, because shields are automatically synthesized using rigorous formal methods, their decisions are often similarly difficult for humans to interpret. Recently, decis...

</details>

---

### [MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models](https://arxiv.org/abs/2606.04627v1)

**Authors:** Zhichao Yang, Yuanze Hu, Haojie Hao, Longkun Hao, Dongshuo Huang et al. (10 authors)

**Published:** 2026-06-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.04627v1) | [PDF](https://arxiv.org/pdf/2606.04627v1.pdf)

<details>
<summary>Abstract</summary>

Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains of thought, which slows interaction, increases supervision cost, and complicates deployment. We introduce MIRAGE, a framework that learns continuous latent reasoning representations from visible textua...

</details>

---

### [MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534v1)

**Authors:** Xinhong Zhang, Runqing Wang, Yunfan Ren, Ding Yu, Boyu Zhou et al. (9 authors)

**Published:** 2026-06-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.04534v1) | [PDF](https://arxiv.org/pdf/2606.04534v1.pdf)

<details>
<summary>Abstract</summary>

Agile quadrotor flight in cluttered scenes requires more than a reactive mapping from a depth image to a control command: the vehicle must remember which regions have been observed, infer nearby occupied space, and act under partial visibility and tight latency. In this paper, we present Mapping-Aware Dreamer (MAD), a geometry-aware world model for vision-based quadrotor flight. Instead of using raw-image reconstruction as the main self-supervised objective, MAD learns recurrent latent dynamics ...

</details>

---
