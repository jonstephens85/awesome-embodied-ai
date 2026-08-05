# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-05 22:48 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies](https://arxiv.org/abs/2608.03727v1)

**Authors:** Chenyi Wang, Xinkai Wang, Bokai Lin, Jialin Tian, Fucheng Zhang et al. (7 authors)

**Published:** 2026-08-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.03727v1) | [PDF](https://arxiv.org/pdf/2608.03727v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Action labels tell a vision-language-action (VLA) policy which robot commands to imitate, but not how those commands change the 3D world. The aligned demonstration clip contains this missing supervision because its $K$ frame transitions record the geometry, motion, visibility, and camera change produced during the corresponding $K$ actions. We introduce Track4Action, a framework that distills this realized transition from a frozen world-centric 3D tracker into a current-observation VLA policy. D...

</details>

---

### [PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud](https://arxiv.org/abs/2608.03682v1)

**Authors:** Chenghua Wang, Daliang Xu, Dongqi Cai, Duojin Sun, Hao Zhang et al. (22 authors)

**Published:** 2026-08-04 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.03682v1) | [PDF](https://arxiv.org/pdf/2608.03682v1.pdf) | [GitHub](https://github.com/mingti-org/phyai)

<details>
<summary>Abstract</summary>

Physical AI policies require inference throughout their lifecycle, including model evaluation, cloud reinforcement learning rollout, edge GPU serving, and onboard deployment. Although these settings share the same checkpoint and action semantics, they often rely on separate inference programs. To unify them, we build PhyAI, a Physical AI inference engine with a single runtime that keeps architecture-specific conditioning, solver, cache, and output logic in model adapters while sharing graph exec...

</details>

---

### [Unified Visuomotor Targets: Supervising VLAs Beyond Physical Actions](https://arxiv.org/abs/2608.03563v1)

**Authors:** Zhenyang Feng, Unnat Jain

**Published:** 2026-08-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.03563v1) | [PDF](https://arxiv.org/pdf/2608.03563v1.pdf) | [Project Page](https://unified-visuomotor-targets.github.io/)

<details>
<summary>Abstract</summary>

VLA models are trained to predict robot actions from visual and language observations. This is a natural choice, but it creates a mismatch: VLMs encode rich, high-level representations of scenes and goals, while robot actions are low-level signals with limited task structure. We ask whether changing what the policy is trained to predict, rather than how it is architecturally designed, can yield better and more efficiently trained policies. We propose UVT (Unified Visuomotor Target), a unified la...

</details>

---

### [Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution](https://arxiv.org/abs/2608.03483v1)

**Authors:** Weichen Xu, Zhenhua Liu, Lin Luo, Yaobo Liang, Chengtang Yao et al. (11 authors)

**Published:** 2026-08-04 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.03483v1) | [PDF](https://arxiv.org/pdf/2608.03483v1.pdf) | [Project Page](https://fleetfootwork.github.io/BCP/)

<details>
<summary>Abstract</summary>

Existing chunk-based Vision-Language-Action (VLA) models execute a fixed number of actions (i.e., execution horizon) before replanning, turning replanning into a task-agnostic periodic schedule that is independent of task progress. As a result, when no replanning boundary falls before a critical manipulation stage, it is executed from a stale chunk rather than a freshly replanned one. To address this limitation, we propose Bernoulli-Continuation Policy (BCP), a lightweight, plug-and-play framewo...

</details>

---

### [ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation](https://arxiv.org/abs/2608.02326v2)

**Authors:** Yuzhi Huang, Weijue Bu, Ziyi Xiong, Jie Wu, Fanding Huang et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02326v2) | [PDF](https://arxiv.org/pdf/2608.02326v2.pdf) | [Project Page](https://muqy1818.github.io/chainvla-web/)

<details>
<summary>Abstract</summary>

Humans perform long-horizon manipulation by retaining knowledge of what earlier actions have established while continuously adapting the motion underway. By contrast, action-chunked vision-language-action (VLA) policies repeatedly replan from the current input at each query. Existing methods preserve either long-term task evidence through memory or short-term motion through action reuse and ensembling, leaving the cross-query handoff incomplete. We introduce ChainVLA, a 1.2B-parameter VLA policy...

</details>

---

### [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580v1)

**Authors:** Ye Wang, Pei Lin, Xiong-Hui Chen, Haoqi Yuan, Zhixuan Liang et al. (15 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02580v1) | [PDF](https://arxiv.org/pdf/2608.02580v1.pdf) | [Project Page](https://www-ye.github.io/ego2robot_blog/)

<details>
<summary>Abstract</summary>

Learning generalizable robot manipulation policies requires large-scale and diverse demonstration data. Egocentric human manipulation videos offer rich scene and task diversity, and prior work has shown that retargeting and rendering such videos into robot-format data can yield effective per-task policies at small scale. However, whether this approach can provide pretraining benefits for vision-language-action models at scale remains unexplored. We present \textbf{Ego2Robot}, a scalable pipeline...

</details>

---

## Other Recent Papers

### [Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking](https://arxiv.org/abs/2608.03231v1)

**Authors:** Jinquan Zhang, Dongfu Yin, Run Yang, Yufeng Yan, Zhen Tian et al. (6 authors)

**Published:** 2026-08-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.03231v1) | [PDF](https://arxiv.org/pdf/2608.03231v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch. To demonstrate the threat, we propose Attention-Guided Semantic Disrupti...

</details>

---

### [DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack](https://arxiv.org/abs/2608.03207v1)

**Authors:** Hoseong Tae, Jong-Seok Lee

**Published:** 2026-08-04 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.03207v1) | [PDF](https://arxiv.org/pdf/2608.03207v1.pdf)

<details>
<summary>Abstract</summary>

Flow-matching vision-language-action (VLA) models such as pi0 generate robot actions by integrating a learned denoising velocity field, and have been reported to resist adversarial perturbations that readily fool autoregressive VLAs. We show that this robustness is largely illusory: it stems from prior attacks ignoring the multi-step denoising ODE. We introduce DRIFT (Denoising Redirection via Input perturbation of the Flow-matching Trajectory), a test-time universal adversarial patch placed on ...

</details>

---

### [How Should Vision-Language-Action Models Use Proprioceptive State?](https://arxiv.org/abs/2608.03052v1)

**Authors:** Yiren Zhao, Ziyang Chen, Ziyang Rao, Pengteng Li, He Zhang et al. (8 authors)

**Published:** 2026-08-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.03052v1) | [PDF](https://arxiv.org/pdf/2608.03052v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models almost universally take robot proprioceptive state as input, yet wire it in incompatible ways -- serialized into text prompts, projected into the vision-language prefix, or fed directly to the action expert -- and almost always as a single current frame. Three questions remain open: (1) whether, and on which tasks, current state actually improves closed-loop control; (2) how much state history helps, and whether its benefit reflects genuine temporal var...

</details>

---

### [ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies](https://arxiv.org/abs/2608.02958v1)

**Authors:** Inkyu Sa, Konstantin Stulov, Rajat Bhageria

**Published:** 2026-08-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.02958v1) | [PDF](https://arxiv.org/pdf/2608.02958v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies trained by behavior cloning fail silently: from the action stream alone, a collapsing rollout looks much like one making clean progress, because imitation supplies no notion of progress. Reinforcement learning would supply one, but it is impractical here, where real-robot experience is costly and deformable food resists simulation. The cheap alternative, a terminal success / failure bit, is learnable in principle yet far too sparse to say when a rollout went...

</details>

---

### [Grounded Semantic Re-Binding for Robust Instruction Generalization in Vision-Language-Action Models](https://arxiv.org/abs/2608.02497v1)

**Authors:** Zhaokai Yin, Zhipeng Zhang

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02497v1) | [PDF](https://arxiv.org/pdf/2608.02497v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel in robotic manipulation but suffer catastrophic performance drops when canonical instructions are simply paraphrased. Although this brittleness is typically addressed through costly data scaling, our probing reveals that the root cause is architectural rather than a lack of semantic understanding. Specifically, we demonstrate that current VLAs successfully retain the correct task identity internally. The failure actually stems from the joint encoding of ...

</details>

---

### [Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation](https://arxiv.org/abs/2608.02257v1)

**Authors:** Donglin Yang, Haoran Chen, Xingyu Chen, Lixing Liu, Manyi Li et al. (9 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02257v1) | [PDF](https://arxiv.org/pdf/2608.02257v1.pdf)

<details>
<summary>Abstract</summary>

Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA) policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated control of both the mobile base and the robotic arms; at the model level, existing VLA models predominantly rely on local camera observations,...

</details>

---

### [Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models](https://arxiv.org/abs/2608.02197v1)

**Authors:** Jin Cui, Yanbin Hu, Xinyue Long, Linkai Li, Boran Zhao et al. (6 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02197v1) | [PDF](https://arxiv.org/pdf/2608.02197v1.pdf)

<details>
<summary>Abstract</summary>

Visual representations of VLA models remain unreliable for spatially precise robotic manipulation. We uncover that vision encoders in VLAs also exhibit attention artifacts previously documented in generic Vision Transformers, and further show that, in embodied policies, these artifacts are closely associated with spatial perception capabilities acquired during post-training. As the encoder learns task-relevant information such as object location, depth ordering, and local geometry, limited globa...

</details>

---

### [Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851v1)

**Authors:** Gaytri Jena, Kapil Wanaskar, Vinija Jain, Aman Chadha, Vasu Sharma et al. (6 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01851v1) | [PDF](https://arxiv.org/pdf/2608.01851v1.pdf)

<details>
<summary>Abstract</summary>

Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action, or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy methods by their degree of self-improvement, from zero-shot program synthesis, through closed-loop self-repair and persistent skill memory, ...

</details>

---

### [Multi-View Unified Camera Fields: Geometry-Shaped Action-Facing Representations for RGB-Only Multi-Camera VLA Policies](https://arxiv.org/abs/2608.01826v1)

**Authors:** Jiarui Yang, Yehao Lu, Yuning Su, Yufeng Xie, Yu Zhong et al. (12 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01826v1) | [PDF](https://arxiv.org/pdf/2608.01826v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation, yet complex contact-rich tasks often benefit from multi-camera observations that jointly capture the end effector, objects, and targets under occlusion. Existing multi-camera VLAs usually concatenate view tokens, leaving action representations weak in metric depth and inconsistent across cameras. We introduce Multi-View Unified Camera Fields (MVUCF), a training-only framework that forms a shared action-...

</details>

---

### [ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction](https://arxiv.org/abs/2608.01824v1)

**Authors:** Shiqi Zhang, Xin Zhang, Yedong Shen, Jiajun Deng, Yuxuan Gao et al. (12 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01824v1) | [PDF](https://arxiv.org/pdf/2608.01824v1.pdf)

<details>
<summary>Abstract</summary>

Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports contact-rich dexterous manipulation through tactile predictions continually refined online using execution-time feedback. ReTouch builds on two ma...

</details>

---

### [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](https://arxiv.org/abs/2608.01755v2)

**Authors:** Zixuan Huang, Yang Zhou, Kaixuan Wang, Guli Zhang, Hongyan Xie et al. (10 authors)

**Published:** 2026-08-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01755v2) | [PDF](https://arxiv.org/pdf/2608.01755v2.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, prod...

</details>

---

### [ProtoAct: Turning Wet-Lab Protocols into Embodied Robotic Actions](https://arxiv.org/abs/2608.01690v1)

**Authors:** Zhe Liu, Jiaming Gu, Zhaohui Du, Zhe Wang, Huanbo Jin et al. (10 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01690v1) | [PDF](https://arxiv.org/pdf/2608.01690v1.pdf)

<details>
<summary>Abstract</summary>

Biological wet-lab protocols are written for trained researchers and often leave routine operations, state-dependent conditions, and contextual parameters implicit, making them difficult to translate into robot-executable actions. We present ProtoAct, a structured protocol-grounding framework that converts free-form biological procedures into state-aware, embodiment-ready action sequences. ProtoAct uses ProtoRAG to retrieve manually annotated examples for context-sensitive parsing, employs Refin...

</details>

---

### [Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models](https://arxiv.org/abs/2608.01573v1)

**Authors:** Dongdong An, Pengjie Zhao, Yihao Huang, Wenbing Tang, Ziming He et al. (8 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01573v1) | [PDF](https://arxiv.org/pdf/2608.01573v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene factor held fixed, merely relocating a task-irrelevant distractor can sharply raise the failure probability within localized, spatially coh...

</details>

---
