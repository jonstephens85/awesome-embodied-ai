# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-12 23:07 UTC

**Papers found:** 22

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories](https://arxiv.org/abs/2606.13578v1)

**Authors:** Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li et al. (18 authors)

**Published:** 2026-06-11 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.13578v1) | [PDF](https://arxiv.org/pdf/2606.13578v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Scientific laboratories increasingly rely on AI systems to reason about experiments, but the physical act of doing science remains largely outside their reach. AI can help read literature, generate hypotheses, and plan protocols, yet the execution of those protocols at the bench still requires a human operator. Vision-Language-Action (VLA) models provide one possible interface between written protocols and robot execution, but existing policies are trained mostly on household and tabletop demons...

</details>

---

### [GIVE: Grounding Human Gestures in Vision-Language-Action Models](https://arxiv.org/abs/2606.13435v1)

**Authors:** Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia et al. (7 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.13435v1) | [PDF](https://arxiv.org/pdf/2606.13435v1.pdf) | [Project Page](https://luis-cloud-sg.github.io/GIVE-project/)

<details>
<summary>Abstract</summary>

Human communication is inherently multimodal, where language is often accompanied by non-verbal cues such as gestures to convey intentions. However, current Vision-Language-Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking the important role of gestures in Human-Robot Interaction (HRI). This often leads to inaccurate intent grounding and unreliable manipulation when language instructions are ambiguous or underspecified. To address this challenge, we propose G...

</details>

---

### [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2606.12978v1)

**Authors:** Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür et al. (6 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.CV, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2606.12978v1) | [PDF](https://arxiv.org/pdf/2606.12978v1.pdf) | [Project Page](https://vla-redirection-attack.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies bring natural language into closed-loop robot control, enabling robots to execute manipulation tasks directly from text instructions. The same interface gives text a recurring role in control because the prompt is reused at every replanning step, and each prompt-conditioned action changes the future observations on which the policy acts. Existing VLA attacks study adversarial prompts that elicit targeted low-level actions or make such actions persist across ...

</details>

---

### [SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2606.12956v1)

**Authors:** Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12956v1) | [PDF](https://arxiv.org/pdf/2606.12956v1.pdf) | [Project Page](https://existentialrobotics.org/serf/)

<details>
<summary>Abstract</summary>

Long-horizon robot mobile manipulation requires continual reasoning about localization, environment changes, and task progress, all of which are challenging to infer from image observations alone. In this paper, we show that conditioning a mobile manipulation policy on a spatiotemporal feature map improves reasoning over long horizons. The map represents the environment and the articulated robot body as neural points in a shared latent space and is updated online from egocentric observations and...

</details>

---

### [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](https://arxiv.org/abs/2606.12403v1)

**Authors:** Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li et al. (7 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12403v1) | [PDF](https://arxiv.org/pdf/2606.12403v1.pdf) | [Project Page](https://world-pilot.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit semantic grounding from large-scale pretraining and perform competently across in-distribution manipulation tasks. This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture. We present World Pilot, a VLA framework that augments the policy with priors from a World-Action Model (WAM), routed into the decision chain through two complementary pathw...

</details>

---

### [VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.12396v1)

**Authors:** Jin Yao, Dhruva Dixith Kurra, Tom Lampo, Zezhou Cheng, Danhua Guo et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12396v1) | [PDF](https://arxiv.org/pdf/2606.12396v1.pdf) | [Project Page](https://yaojin17.github.io/VLGA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that provide no dense spatial signal. We introduce VLGA, the first vision-language-action model supervised to reconstruct the dense 3D world it d...

</details>

---

### [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/abs/2606.12366v1)

**Authors:** Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12366v1) | [PDF](https://arxiv.org/pdf/2606.12366v1.pdf) | [Project Page](https://xukechun.github.io/papers/APT/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs) with continuous action experts have achieved strong manipulation performance, yet generalization to out-of-distribution (OOD) language instructions remains poor. A known challenge is the structural imbalance in VLA data, where language is far less diverse than visual and action content, making policies prone to visual shortcuts. While discrete-action methods mitigate this through vision-language co-training,...

</details>

---

### [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](https://arxiv.org/abs/2606.12352v1)

**Authors:** Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12352v1) | [PDF](https://arxiv.org/pdf/2606.12352v1.pdf) | [Project Page](https://chorus-model.github.io)

<details>
<summary>Abstract</summary>

Multi-robot collaboration allows robots to efficiently take on a wide range of tasks, from moving a couch through a doorway to assembling structures on a construction site. However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team size, and decentralized methods that train one policy per robot often require explicit alignment procedures or information sharing at inference ...

</details>

---

### [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](https://arxiv.org/abs/2606.12105v1)

**Authors:** Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, Moritz Reuss, Gianluca Geraci et al. (7 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12105v1) | [PDF](https://arxiv.org/pdf/2606.12105v1.pdf) | [Project Page](\href{https://intuitive-robots.github.io/DAM-VLA/}{intuitive-robots.github.io/DAM-VLA/})

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models inherit a shared synchronous clock from vision-language pretraining, processing every input at one rate. This is misaligned with physical interaction, where a high-frequency modality changes at hundreds of hertz, vision evolves more slowly, and language stays constant across an episode. A synchronous VLA oversamples slow modalities, undersamples fast ones, and caps action generation at the lowest effective frequency. We hypothesize that decoupling temporal pro...

</details>

---

### [$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models](https://arxiv.org/abs/2606.12497v1)

**Authors:** Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn et al. (9 authors)

**Published:** 2026-06-10 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12497v1) | [PDF](https://arxiv.org/pdf/2606.12497v1.pdf) | [Project Page](https://avanturist322.github.io/mu-vla/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a control...

</details>

---

### [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](https://arxiv.org/abs/2606.11743v1)

**Authors:** Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su et al. (8 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.GR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.11743v1) | [PDF](https://arxiv.org/pdf/2606.11743v1.pdf) | [Project Page](https://tac-corl.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide strong visual, language, and action priors for robot manipulation, but visual observations alone often miss the local contact state required for contact-rich tasks. We present TacCoRL, a scalable framework that injects Tactile feedback into VLA policies and improves them through sim-real Co-training and simulation-based reinforcement learning (RL), without requiring large-scale tactile pretraining or extensive real-world contact exploration. The key id...

</details>

---

### [DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World](https://arxiv.org/abs/2606.11901v1)

**Authors:** Tobias Jülg, Seongjin Bien, Simon Hilber, Yannik Blei, Pierre Krack et al. (10 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.11901v1) | [PDF](https://arxiv.org/pdf/2606.11901v1.pdf) | [Project Page](https://duobench.github.io/)

<details>
<summary>Abstract</summary>

Bimanual robot systems substantially expand manipulation capabilities, but coordinating two arms introduces additional control complexity and failure modes that are not well captured by existing benchmarks. We introduce DuoBench, an extensible benchmarking framework for bimanual manipulation policies on the FR3 Duo platform. DuoBench comprises eleven tasks spanning four coordination categories, implemented in simulation and partially reproduced in the real world through reproducible task recipes...

</details>

---

## Other Recent Papers

### [See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation](https://arxiv.org/abs/2606.13279v1)

**Authors:** Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.13279v1) | [PDF](https://arxiv.org/pdf/2606.13279v1.pdf)

<details>
<summary>Abstract</summary>

In bimanual robotic manipulation, task-relevant visual information varies with the task stage and context, while the interaction of the two arms shifts between independent and coordinated modes, making policy learning challenging. However, existing monolithic Vision-Language-Action (VLA) policies process diverse visual inputs and interaction patterns through a single shared representation and action generation pathway, often failing to separately account for visual relevance and bimanual interac...

</details>

---

### [An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics](https://arxiv.org/abs/2606.12936v1)

**Authors:** Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu et al. (11 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12936v1) | [PDF](https://arxiv.org/pdf/2606.12936v1.pdf)

<details>
<summary>Abstract</summary>

Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical experiments, but scaling their learning requires customizable simulators for safe and reproducible task generation, open editable laboratory assets, and efficient pipelines that turn limited demonstrations into usable training data. We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning. Pipette releases over 43 open-source and re-edit...

</details>

---

### [AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots](https://arxiv.org/abs/2606.12859v1)

**Authors:** Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang et al. (9 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12859v1) | [PDF](https://arxiv.org/pdf/2606.12859v1.pdf)

<details>
<summary>Abstract</summary>

Aerial manipulation systems have long suffered from representation coupling in end-to-end control, as platform-level Unmanned Aerial Vehicle (UAV) movement and end-effector-level arm manipulation differ substantially in action scale, dynamics, and control objectives. In this paper, we propose AIR-VLA+, a flow matching action generation architecture specifically designed for aerial manipulation, featuring cascaded dual-action decoders and an asymmetric feature-level Mixture of Experts (MoE). We c...

</details>

---

### [Real-Time Execution with Autoregressive Policies](https://arxiv.org/abs/2606.13355v1)

**Authors:** Sangkyu Lee, Seohyeon Park, Tackgeun You, Avi Caciularu, Idan Szpektor et al. (7 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.13355v1) | [PDF](https://arxiv.org/pdf/2606.13355v1.pdf)

<details>
<summary>Abstract</summary>

Real-time execution, enabled by asynchronous inference that ensures both smooth action trajectories and fast reactivity, is critical for realistic deployments of large-scale Vision-Language-Action models. However, recent work on real-time execution primarily focuses on variants of diffusion policies, even though it is more critical for autoregressive policies given their slower rollout speed in synchronous inference. In contrast, we demonstrate that autoregressive policies can achieve real-time ...

</details>

---

### [VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving](https://arxiv.org/abs/2606.12706v1)

**Authors:** Thach Nguyen, Danhua Guo, Tom Lampo, Fei Wu, Burhan Yaman

**Published:** 2026-06-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.12706v1) | [PDF](https://arxiv.org/pdf/2606.12706v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside driving trajectories, but existing benchmarks evaluate only trajectory quality and do not assess whether the CoT is relevant, consistent, or causally connected to the driving action. We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationsh...

</details>

---

### [PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation](https://arxiv.org/abs/2606.12616v1)

**Authors:** Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki

**Published:** 2026-06-10 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.12616v1) | [PDF](https://arxiv.org/pdf/2606.12616v1.pdf)

<details>
<summary>Abstract</summary>

Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode. Recent work introduces style variation through post-hoc labels on observational data or LLM-inferred reward weights, but these signals act as proxies for what a style should reward rather than demonstrations of humans explicitly asked to drive in that style. W...

</details>

---

### [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/abs/2606.12299v1)

**Authors:** Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12299v1) | [PDF](https://arxiv.org/pdf/2606.12299v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a natural language interface to robot control, but the mapping from language to behavior is often brittle and unintuitive: semantically similar instructions can induce drastically different behaviors, while some capabilities may not be elicitable through prompting alone. As a result, both human instructions and zero-shot language models can fail to reliably steer VLAs toward successful task execution. In this work, we propose a framework that interacti...

</details>

---

### [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/abs/2606.12109v1)

**Authors:** Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12109v1) | [PDF](https://arxiv.org/pdf/2606.12109v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and acute action manifold collapse due to data scarcity. In this paper, we present I...

</details>

---

### [Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration](https://arxiv.org/abs/2606.12475v1)

**Authors:** Leo Xu, Letian Li, Alex Cuellar, Michael Hagenow

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12475v1) | [PDF](https://arxiv.org/pdf/2606.12475v1.pdf)

<details>
<summary>Abstract</summary>

Human-robot collaboration (HRC) combines the complementary strengths of humans and robots to improve task efficiency. However, many existing collaborative systems rely on hand-engineered pipelines, limiting their scalability and flexibility for new tasks. In this work, we show that models trained end-to-end with imitation learning, specifically vision-language-action (VLA) models, can support collaborative manipulation, and characterize the key factors affecting their real-world performance. We ...

</details>

---

### [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688v1)

**Authors:** Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin, Rohan Sanda et al. (12 authors)

**Published:** 2026-06-10 | **Categories:** cs.LG, cs.AI, cs.DC

**Links:** [arXiv](https://arxiv.org/abs/2606.12688v1) | [PDF](https://arxiv.org/pdf/2606.12688v1.pdf)

<details>
<summary>Abstract</summary>

We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about mode...

</details>

---
