# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-03 17:25 UTC

**Papers found:** 23

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/abs/2607.02517v1)

**Authors:** Hanlin Wang, Hao Ouyang, Qiuyu Wang, Wen Wang, Qingyan Bai et al. (13 authors)

**Published:** 2026-07-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.02517v1) | [PDF](https://arxiv.org/pdf/2607.02517v1.pdf) | [Project Page](https://worlddirector.github.io/)

<details>
<summary>Abstract</summary>

We present WorldDirector, a highly controllable video world model framework designed for persistent dynamic object memory and unrestricted viewpoint exploration. Unlike existing world models that entangle physical dynamics with pixel rendering and rely on continuous visual observation to sustain motion, our framework explicitly decouples semantic motion orchestration from visual generation. By leveraging an LLM to coordinate 3D trajectories with camera movements and subsequently employing these ...

</details>

---

### [ACID: Action Consistency via Inverse Dynamics for Planning with World Models](https://arxiv.org/abs/2607.02403v1)

**Authors:** Gawon Seo, Dongwon Kim, Suha Kwak

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.02403v1) | [PDF](https://arxiv.org/pdf/2607.02403v1.pdf) | [Project Page]([this)

<details>
<summary>Abstract</summary>

Decision-time planning with action-conditioned world models has become a popular paradigm for embodied control. However, the standard planning cost judges a candidate solely by how close its predicted terminal state lies to the goal, leaving the realizability of the intermediate transitions unchecked -- a predicted trajectory can look convincing while the environment rollout drifts away from it. In this paper, we propose ACID, a decision-time planning framework that introduces cycle action consi...

</details>

---

### [Bridge-WA: Predicting Where and How the World Changes for Robotic Action](https://arxiv.org/abs/2607.02195v1)

**Authors:** Yongjie Bai, Hanting Wang, Mingtong Dai, Qijun Zhong, Yang Liu et al. (6 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.02195v1) | [PDF](https://arxiv.org/pdf/2607.02195v1.pdf) | [Project Page](https://hcplab-sysu.github.io/BRIDGE-WA)

<details>
<summary>Abstract</summary>

General-purpose vision-language-action models benefit from large vision-language priors, but effective manipulation also requires anticipating action-relevant scene changes. Existing world-action models often rely on large generative world models or dense future rollouts, which are expensive and spend capacity on visual details weakly coupled to control. We present Bridge-WA, a lightweight world-action framework that distills a frozen future-change teacher into three compact priors: future token...

</details>

---

### [PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2607.01938v1)

**Authors:** Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang et al. (6 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.01938v1) | [PDF](https://arxiv.org/pdf/2607.01938v1.pdf) | [GitHub](https://github.com/vLAR-group/PhysMani)

<details>
<summary>Abstract</summary>

Manipulating fast and dynamically moving targets in unstructured 3D environments remains challenging for embodied AI. Existing visual-language-action models and world models struggle with accurate 3D geometry and physically meaningful forecasting. We propose PhysMani, a framework that couples a physics-principled 3D Gaussian world model with a future-aware action policy model. The world model learns a divergence-free Gaussian velocity field via online optimization for fast and physically grounde...

</details>

---

### [Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander](https://arxiv.org/abs/2607.01736v1)

**Authors:** Nikolai Smolyanskiy

**Published:** 2026-07-02 | **Categories:** cs.LG, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2607.01736v1) | [PDF](https://arxiv.org/pdf/2607.01736v1.pdf) | [GitHub](https://github.com/nsmoly/LunarLander_RSSM)

<details>
<summary>Abstract</summary>

We study how to predict the downstream closed-loop performance of a learned latent world model from validation-time diagnostics alone. Choosing the right checkpoint from a world-model training run is difficult: validation loss and multi-step prediction RMSE keep improving long after closed-loop performance has collapsed. We present a suite of structural validation-time diagnostics drawn from optimal-control theory and apply them to Gymnasium's LunarLander v3, which features shaped rewards. We tr...

</details>

---

### [Valdi: Value Diffusion World Models](https://arxiv.org/abs/2607.00917v1)

**Authors:** Christopher Lindenberg, Kashyap Chitta

**Published:** 2026-07-01 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00917v1) | [PDF](https://arxiv.org/pdf/2607.00917v1.pdf) | [GitHub](https://github.com/Kit115/ValueDiffusionWorldModels)

<details>
<summary>Abstract</summary>

World models can enable Model Predictive Control (MPC), but this requires dynamics prediction that is both fast enough for online use and expressive enough to represent uncertain futures. Diffusion models offer a natural mechanism for modeling uncertain dynamics, yet their iterative inference procedure makes them difficult to use for low-latency latent planning. We bridge this gap with Value Diffusion World Models (Valdi), combining end-to-end online training for MPC with a latent diffusion dyna...

</details>

---

### [From World Models to World Action Models: A Concise Tutorial for Robotics](https://arxiv.org/abs/2607.00836v2)

**Authors:** Xiaoxiong Zhang, Xiong Zeng, Wei Zhang

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2607.00836v2) | [PDF](https://arxiv.org/pdf/2607.00836v2.pdf) | [Project Page](https://clearlab-sustech.github.io/WorldModelSurvey/)

<details>
<summary>Abstract</summary>

World models are increasingly used in embodied intelligence and generative simulation, yet their scope remains ambiguous across communities. This tutorial presents a design-space view of world models as action-conditioned predictive models that estimate the future evolution of task-relevant observations or states. We categorize existing methods into observation-space and state-space world models, comparing their trade-offs in visual fidelity, spatial structure, physical interpretability, and con...

</details>

---

### [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678v1)

**Authors:** Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin et al. (21 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00678v1) | [PDF](https://arxiv.org/pdf/2607.00678v1.pdf) | [GitHub](https://github.com/amap-cvlab/ABot-Manipulation)

<details>
<summary>Abstract</summary>

Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...

</details>

---

## Other Recent Papers

### [WorldSample: Closed-loop Real-robot RL with World Modelling](https://arxiv.org/abs/2607.02431v1)

**Authors:** Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu et al. (8 authors)

**Published:** 2026-07-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.02431v1) | [PDF](https://arxiv.org/pdf/2607.02431v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations. However, deploying RL on real robots remains constrained by high interaction costs, since each physical rollout is costly and reflects only one realized action-outcome path. To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for rea...

</details>

---

### [DecompRL: Solving Harder Problems by Learning Modular Code Generation](https://arxiv.org/abs/2607.02390v1)

**Authors:** Juliette Decugis, Fabian Gloeckle, Francis Bach, Taco Cohen, Gabriel Synnaeve

**Published:** 2026-07-02 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.02390v1) | [PDF](https://arxiv.org/pdf/2607.02390v1.pdf)

<details>
<summary>Abstract</summary>

How can Large Language Models (LLMs) solve problems they currently cannot? Repeated sampling scales test-time compute but GPU cost grows linearly with attempts, while reinforcement learning (RL) with verifiable rewards improves single-attempt accuracy at the expense of sample diversity. Both strategies ultimately fail when the base policy has near-zero probability of producing a correct solution: no amount of sampling or gradient signal can overcome a search space that is simply too large. We ta...

</details>

---

### [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](https://arxiv.org/abs/2607.02376v1)

**Authors:** Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi

**Published:** 2026-07-02 | **Categories:** cs.AI, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2607.02376v1) | [PDF](https://arxiv.org/pdf/2607.02376v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination p...

</details>

---

### [PWM-ArtGen: Part World Model for Articulated Object Generation](https://arxiv.org/abs/2607.02045v1)

**Authors:** Wentao Zheng, Ancong Wu

**Published:** 2026-07-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.02045v1) | [PDF](https://arxiv.org/pdf/2607.02045v1.pdf)

<details>
<summary>Abstract</summary>

The key challenge in articulated 3D object generation from a single image is accurately predicting the underlying kinematic structure. Existing methods either infer kinematic parameters directly from a static image that lacks dynamic part-level kinematic relationships, or estimate parameters from visual dynamics generated from a single image, which is prone to accumulated errors of two steps. Moreover, the limited scale and diversity of existing annotated datasets further hinder generalization t...

</details>

---

### [Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling](https://arxiv.org/abs/2607.01986v1)

**Authors:** Weizhi Nie, Weijie Wang, Yuting Su

**Published:** 2026-07-02 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.01986v1) | [PDF](https://arxiv.org/pdf/2607.01986v1.pdf)

<details>
<summary>Abstract</summary>

Multivariate time-series models for prognostics are often evaluated by point prediction accuracy, yet their internal states rarely expose a coherent degradation process. We study liquid neural networks as latent dynamics models for aircraft engine health monitoring on the C-MAPSS benchmark. The proposed model encodes a history window into a latent state, evolves that state with a liquid transition model, and decodes future sensor observations. To separate health evolution from operating-conditio...

</details>

---

### [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](https://arxiv.org/abs/2607.01767v1)

**Authors:** Xinyuan Song, Zekun Cai

**Published:** 2026-07-02 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.01767v1) | [PDF](https://arxiv.org/pdf/2607.01767v1.pdf)

<details>
<summary>Abstract</summary>

As agent planning moves from short tool chains toward persistent workflows with thousands or tens of thousands of steps, failures will occur inside large planning graphs rather than in isolated predictions. Replanning the entire graph after every mistake is neither computationally realistic nor desirable: full-graph replay consumes large context budgets, exposes the LLM to many irrelevant symptoms, and can degrade long-context retrieval. This paper studies the missing component in such systems: ...

</details>

---

### [Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model](https://arxiv.org/abs/2607.01595v1)

**Authors:** Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo et al. (7 authors)

**Published:** 2026-07-02 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.01595v1) | [PDF](https://arxiv.org/pdf/2607.01595v1.pdf)

<details>
<summary>Abstract</summary>

As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge. While existing approaches integrate Large Language Models (LLMs) for semantic understanding and Deep Reinforcement Learning (DRL) for policy optimization, they often rely on sequential, loosely coupled architectures that underutilize the generative and reasoning capabilities of LLMs. In this paper, we propose...

</details>

---

### [Certified World Models as Sensing Clocks: Drift-Aware Deadlines for Active Perception](https://arxiv.org/abs/2607.01537v1)

**Authors:** Hongbo Wang

**Published:** 2026-07-01 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.01537v1) | [PDF](https://arxiv.org/pdf/2607.01537v1.pdf)

<details>
<summary>Abstract</summary>

Certified world models estimate how long their predictions remain valid. We turn this validity horizon into an operational sensing clock: a rule for when an agent should stop coasting and re-sense. Starting from an audited equivariant world model, we derive a deadline for no-sensing intervals and show that deployable deadlines in learned world models must be drift-aware: on-manifold Lyapunov rates alone overestimate coasting validity, while calibrated native rollout-drift envelopes carry the dep...

</details>

---

### [OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration](https://arxiv.org/abs/2607.01531v1)

**Authors:** David Courtis, Wenhao Li, Scott Sanner

**Published:** 2026-07-01 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.01531v1) | [PDF](https://arxiv.org/pdf/2607.01531v1.pdf)

<details>
<summary>Abstract</summary>

Learning how an environment behaves from interaction is central to building agents that adapt to unfamiliar tasks. World models learned with deep networks are flexible but data-hungry and transfer poorly beyond their training distribution. Program-synthesized world models, written as source code by LLMs and refined through counterexample-guided inductive synthesis (CEGIS), are instead data-efficient and reusable, yet they have been demonstrated mainly on structured-state worlds with a given obje...

</details>

---

### [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](https://arxiv.org/abs/2607.01060v1)

**Authors:** Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo, Sungdong Kim, Minjoon Seo et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.01060v1) | [PDF](https://arxiv.org/pdf/2607.01060v1.pdf)

<details>
<summary>Abstract</summary>

Video world models are emerging as a scalable alternative for evaluating generalist robot policies, bypassing the physical constraints and engineering burdens of real-world deployment. However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-a...

</details>

---

### [DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889v1)

**Authors:** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00889v1) | [PDF](https://arxiv.org/pdf/2607.00889v1.pdf)

<details>
<summary>Abstract</summary>

We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single p...

</details>

---

### [Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)

**Authors:** Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu et al. (6 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00673v1) | [PDF](https://arxiv.org/pdf/2607.00673v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in unstructured outdoor environments often plan from scene reconstructions collected before deployment because operators cannot remap large or remote sites before every mission. As a result, robots must make long-horizon planning decisions using stale maps that assume the terrain remains unchanged, even though physical changes to the environment may render previously feasible routes unsafe or unreachable at execution time. We present a physically viable world model for evaluating...

</details>

---

### [AGI Maze as a Benchmark Framework for World-Modeling Agents](https://arxiv.org/abs/2607.00627v1)

**Authors:** Alexey Potapov

**Published:** 2026-07-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00627v1) | [PDF](https://arxiv.org/pdf/2607.00627v1.pdf)

<details>
<summary>Abstract</summary>

Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environ...

</details>

---

### [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457v1)

**Authors:** Jinwoo Jang, Daniel J. Rho, Sihyung Yoon, Hyunsuk Cho, Honguk Woo

**Published:** 2026-07-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00457v1) | [PDF](https://arxiv.org/pdf/2607.00457v1.pdf)

<details>
<summary>Abstract</summary>

Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a uniform update policy cannot accommodate the different rates at which knowledge at each scale becomes outdated. We present MuSix, a framework that addresses both challenges through scale-aware world mo...

</details>

---

### [RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail](https://arxiv.org/abs/2607.00310v1)

**Authors:** Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar, Anoop M. Namboodiri, Sashi P. Reddi

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00310v1) | [PDF](https://arxiv.org/pdf/2607.00310v1.pdf)

<details>
<summary>Abstract</summary>

Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocentric video of the same activity are available, which viewpoint of training data produces the strongest adapted model? We introduce RetailSMV (...

</details>

---
