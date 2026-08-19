# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-19 16:30 UTC

**Papers found:** 20

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.18035v1)

**Authors:** Zongzheng Zhang, Jijun Wang, Saining Zhang, Shuo Wang, Yiru Wang et al. (11 authors)

**Published:** 2026-08-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.18035v1) | [PDF](https://arxiv.org/pdf/2608.18035v1.pdf) | [Project Page](https://zzongzheng0918.github.io/TE-Aware-E2E-AD/)

<details>
<summary>Abstract</summary>

Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end driving research predominantly focuses on dynamic road participants (e.g., vehicles and pedestrians), while the role of traffic elements remains largely unexplored. The community still lacks a systematic study quantifying their impact, largely because public datasets rarely provide structured traffic-...

</details>

---

### [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885v1)

**Authors:** Xiaowei Cai, Yunuo Cai, Bingao Chen, Jingxiao Chen, Zhi Chen et al. (39 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16885v1) | [PDF](https://arxiv.org/pdf/2608.16885v1.pdf) | [Project Page](https://tau0-vla.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_0$-VLA, a hierarchical robot foundation model that formulates high-level subtask generation as a compute-scalable inference problem through w...

</details>

---

### [HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](https://arxiv.org/abs/2608.16837v1)

**Authors:** Langzhe Gu, Chengkai Hou, Meng Li, Xinhua Wang, Jiaming Liu et al. (17 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16837v1) | [PDF](https://arxiv.org/pdf/2608.16837v1.pdf) | [Project Page](https://grange007.github.io/HAF)

<details>
<summary>Abstract</summary>

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate locomotion, waist posture, and dual-arm manipulation effectively. Moreover, policies trained through offline behavior cloning can ...

</details>

---

### [US-VLA: An Ultrasound Vision-Language-Action Model for Embodied Abdomina](https://arxiv.org/abs/2608.16074v1)

**Authors:** Cheng Zhang, Xingzheng Wu, Guihao Yan, Xifeng Hu, Zhi Liu et al. (7 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16074v1) | [PDF](https://arxiv.org/pdf/2608.16074v1.pdf) | [GitHub](https://github.com/VMVLab/US-VLA)

<details>
<summary>Abstract</summary>

Artificial intelligence-assisted ultrasound scanning enhances diagnostic reliability and efficiency by providing real-time guidance for standardized image acquisition and reducing operator dependence. However, existing reinforcement learning and learning-assisted ultrasound scanning methods typically rely on carefully designed reward functions or extensive interaction data, which limits their generalization ability and stability across different devices, patient populations, and complex clinical...

</details>

---

## Other Recent Papers

### [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600v1)

**Authors:** Zhengyan Qian, Rui Yan, Alex Jinpeng Wang, Jinhui Tang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17600v1) | [PDF](https://arxiv.org/pdf/2608.17600v1.pdf)

<details>
<summary>Abstract</summary>

Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear. Existing work covers only a narrow range of cue forms and focuses on final task success, providing only a coarse assessment of cue-following capability. Treating all visual cues as authorized also leaves safety risks of unauthorized following unexplored. To address these gaps, we introduce LIBERO-VI...

</details>

---

### [Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies](https://arxiv.org/abs/2608.17484v1)

**Authors:** Yuhwan Jeong, Kuk-Jin Yoon

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17484v1) | [PDF](https://arxiv.org/pdf/2608.17484v1.pdf)

<details>
<summary>Abstract</summary>

Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations. Yet there is little guidance for deciding which intervention a deployed policy actually needs. Additional sampling is useful only when better behavior already exists within the policy's stochastic rollouts and can be identified, whereas retrieval is most useful when the relevant action prior is not reliably represented by the policy. ...

</details>

---

### [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453v1)

**Authors:** Songwei Wu, Rui Zhao, Fan Yang, Zhongqiang Nie, Zhiduo Jiang et al. (9 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17453v1) | [PDF](https://arxiv.org/pdf/2608.17453v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...

</details>

---

### [Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](https://arxiv.org/abs/2608.17423v1)

**Authors:** Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping et al. (9 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.17423v1) | [PDF](https://arxiv.org/pdf/2608.17423v1.pdf)

<details>
<summary>Abstract</summary>

GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose rollouts all succeed or all fail have zero advantage and are discarded by dynamic sampling. These groups are especially common early in training, when most rollouts fail, wasting much of...

</details>

---

### [MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](https://arxiv.org/abs/2608.17386v1)

**Authors:** Yiyan Peng, Philip Wang, Simon Sinong Zhan, Yiqi Lyu, Zhenyang Ni et al. (14 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17386v1) | [PDF](https://arxiv.org/pdf/2608.17386v1.pdf)

<details>
<summary>Abstract</summary>

Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along ...

</details>

---

### [CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation](https://arxiv.org/abs/2608.17717v1)

**Authors:** Zhen Zhang, Ahmad Hafez, Peng Xie, Yanliang Huang, Wenyuan Wu et al. (6 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17717v1) | [PDF](https://arxiv.org/pdf/2608.17717v1.pdf)

<details>
<summary>Abstract</summary>

A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction. This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty. We...

</details>

---

### [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](https://arxiv.org/abs/2608.17496v1)

**Authors:** Kaiming Zhong, Tianhua Liu, Yue Wang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17496v1) | [PDF](https://arxiv.org/pdf/2608.17496v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pip...

</details>

---

### [Teach and Grow: An Agent-Centered Architecture for General Robot Learning](https://arxiv.org/abs/2608.17209v1)

**Authors:** Chang Nie, Zhe Liu, Hesheng Wang

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.17209v1) | [PDF](https://arxiv.org/pdf/2608.17209v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end vision-language-action (VLA) and world-action models offer an elegant route to general-purpose robotics, but their reliability is bounded by validated physical coverage. When an unfamiliar object, sensor, embodiment, or contact falls outside that coverage and no validated fallback exists, correcting the failure requires new robot data, a policy update, and regression testing. This recurring burden is the retraining tax. Unlike text, embodied data must often be created by operating mac...

</details>

---

### [Inference-Time Attention Steering for Vision-Language-Action Driving Models](https://arxiv.org/abs/2608.17095v1)

**Authors:** Darshan Nagendra Prasad, Lars Ullrich, Knut Graichen

**Published:** 2026-08-17 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.17095v1) | [PDF](https://arxiv.org/pdf/2608.17095v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining. We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone. It is applied as a fail open forward pre-hook with no weight changes. On 50 lane-change scenarios from the Physical AI...

</details>

---

### [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](https://arxiv.org/abs/2608.16889v1)

**Authors:** Bingxin Xu, Yuzhang Shang, Emilio Ferrara

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.16889v1) | [PDF](https://arxiv.org/pdf/2608.16889v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation chains many contact-rich skills into one multi-stage task. Vision-language-action (VLA) models increasingly master the individual skills, yet the chain still fails: errors compound beyond the policy's ability to correct, and one subtask silently constrains the next. A promising recipe freezes the VLA and puts an LLM agent in charge: it plans in language, moves in free space with analytic primitives, invokes the VLA only for contact-rich segments, and writes adapta...

</details>

---

### [FabriMAE I Trust Myself? Self-Evaluating VLA Action Generation with Markov Attention Entropy](https://arxiv.org/abs/2608.16697v1)

**Authors:**  Aniri, Chen Yilin, Jinhe Bi, Junfei Guo, Donglai Ran et al. (13 authors)

**Published:** 2026-08-17 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16697v1) | [PDF](https://arxiv.org/pdf/2608.16697v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) integrate visual perception, language instruction, and action generation into end-to-end policies across heterogeneous architectures. However, enabling VLAs to self-evaluate their action generation reliability without external supervision remains a major challenge. Existing methods either rely on expert annotations or estimate uncertainty only from output statistics, largely ignoring internal signals. In this work, we observe that internal visual modality ent...

</details>

---

### [NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](https://arxiv.org/abs/2608.16503v1)

**Authors:** Cong Zhao, Shuai Tian, Xu Zhang, Baocheng Ni, Xinguo Song et al. (14 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16503v1) | [PDF](https://arxiv.org/pdf/2608.16503v1.pdf)

<details>
<summary>Abstract</summary>

Real-world deployment of Vision-Language-Action (VLA) models is often bottlenecked by efficiency-performance trade-offs, cross-embodiment generalization, and execution smoothness. We present NebulaVLA, an asynchronous dual-frequency architecture that decouples high-level semantic reasoning from low-level action control, optimizing computational resources and modularity. To bridge semantic gaps across heterogeneous robots, we introduce GESTURE-7, a unified language-grounded action representation....

</details>

---

### [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172v1)

**Authors:** Xunyao Lei, Renjun Wu, Tianlin Huo, Xuesong Li

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16172v1) | [PDF](https://arxiv.org/pdf/2608.16172v1.pdf)

<details>
<summary>Abstract</summary>

At every re-observation point in a hierarchical Vision-Language-Action (VLA) system, two interface decisions must be made: when to terminate the current subtask and how far to execute the proposed action chunk. These decisions are mutually dependent---the optimal stopping point depends on what the executor plans to do, while the optimal execution length depends on where the subtask boundary lies---yet existing architectures evaluate them in isolation, an asymmetry neither module can overcome alo...

</details>

---

### [Q-Learning With World Models](https://arxiv.org/abs/2608.17163v1)

**Authors:** Perry Dong, Yueru Jia, Chelsea Finn, Dorsa Sadigh

**Published:** 2026-08-17 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.17163v1) | [PDF](https://arxiv.org/pdf/2608.17163v1.pdf)

<details>
<summary>Abstract</summary>

Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which ...

</details>

---

### [When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents](https://arxiv.org/abs/2608.16806v1)

**Authors:** Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang et al. (10 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.16806v1) | [PDF](https://arxiv.org/pdf/2608.16806v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated capabilities in in-context learning, task decomposition, step-by-step reasoning, and code generation, driving their gradual evolution from text generation models into the core of agents capable of perceiving environments, invoking tools, and executing tasks. Traditional LLM Agents typically obtain information through webpages, documents, databases, or external tools and generate corresponding invocation sequences according to user goals; when this t...

</details>

---

### [Exposing the Long-tail in Embodied Urban Navigation via Scalable Learning from In-the-Wild Videos](https://arxiv.org/abs/2608.16476v1)

**Authors:** Bingyi Xia, Han Bao, Zhewei Chen, Hanjing Ye, Jingwen Yu et al. (8 authors)

**Published:** 2026-08-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.16476v1) | [PDF](https://arxiv.org/pdf/2608.16476v1.pdf)

<details>
<summary>Abstract</summary>

Learning embodied urban navigation policies from real-world data is constrained by the cost of task-specific data collection and the limited coverage of rare yet safety-critical scenarios. To address these challenges, we present a scalable framework for learning point-goal urban navigation from web-scale in-the-wild egocentric videos while systematically exposing its long tail. The framework automatically annotates uncurated web videos with metric trajectories and structured navigation semantics...

</details>

---
