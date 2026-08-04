# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-04 22:51 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation](https://arxiv.org/abs/2608.02326v1)

**Authors:** Yuzhi Huang, Weijue Bu, Ziyi Xiong, Jie Wu, Fanding Huang et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02326v1) | [PDF](https://arxiv.org/pdf/2608.02326v1.pdf) | [Project Page](https://muqy1818.github.io/chainvla-web/)

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

### [Hermite Curves as Trajectory Priors for Vision-Language-Action Models](https://arxiv.org/abs/2608.01265v1)

**Authors:** Qi Lv, Jianming Xing, Zhao Yang, Mingyuan Yao, Yinan Shi et al. (8 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.01265v1) | [PDF](https://arxiv.org/pdf/2608.01265v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Despite recent progress in Vision-Language-Action (VLA) models for robotic manipulation, the action chunk remains a weakly structured interface. Existing work typically flatten each chunk into per-timestep controls, relying on implicit data learning that manifests as jagged motion and boundary discontinuities during physical execution. To address these limitations, we introduce Hermite trajectory priors, parameterizing the chunk trajectory as a piecewise cubic Hermite curve defined by endpoint p...

</details>

---

## Other Recent Papers

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

### [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](https://arxiv.org/abs/2608.01755v1)

**Authors:** Zixuan Huang, Yang Zhou, Kaixuan Wang, Guli Zhang, Hongyan Xie et al. (9 authors)

**Published:** 2026-08-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01755v1) | [PDF](https://arxiv.org/pdf/2608.01755v1.pdf)

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

### [Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them](https://arxiv.org/abs/2608.01402v1)

**Authors:** Carlota Parés-Morlans, Nils Kuhn, Isabel Liu, Alberta Longhini, Jeannette Bohg

**Published:** 2026-08-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01402v1) | [PDF](https://arxiv.org/pdf/2608.01402v1.pdf)

<details>
<summary>Abstract</summary>

We address the problem of understanding when and why Vision-Language-Action models struggle with contact-rich manipulation tasks that require precise physical interaction. Prior work has primarily focused on addressing contact failures through force-augmented architectures and training-time regularizers, yet the root causes of these failures remain underexplored. We identify two distinct failure modes underlying this gap. Precision failures are rooted in a flow-matching policy training mismatch,...

</details>

---

### [DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation](https://arxiv.org/abs/2608.01381v1)

**Authors:** Zheng Yang, Wenjie Zhang, Xiangyu Chen, Wenxuan Song, Xianpeng Wang et al. (10 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01381v1) | [PDF](https://arxiv.org/pdf/2608.01381v1.pdf)

<details>
<summary>Abstract</summary>

Mobile manipulation requires a robot to coordinate base and arm motion under continuously changing viewpoints and contact conditions, within an action space far larger than that of fixed-base manipulation. Existing Vision-Language-Action (VLA) policies are limited in two respects. (i)They map observations directly to whole-body action chunks, searching this large action space without an explicit task-space motion plan, which makes coordinated base--arm prediction imprecise. (ii)They execute the ...

</details>

---

### [OC-VLA++: Monocular Geometry-Guided Cross-View Consistency for Viewpoint-Robust Robotic Manipulation](https://arxiv.org/abs/2608.01066v1)

**Authors:** Tianyi Zhang, Ziyang Gong, Zhenjie Yang, Zhe Qian, Haonan Duan

**Published:** 2026-08-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01066v1) | [PDF](https://arxiv.org/pdf/2608.01066v1.pdf)

<details>
<summary>Abstract</summary>

We propose OC-VLA++, an extension of OC-VLA for viewpoint generalization under limited camera coverage. While OC-VLA grounds robot actions in the camera coordinate system to align action supervision with visual observations, camera-space grounding alone can still overfit to the few viewpoints observed during training. OC-VLA++ addresses this limitation by introducing geometry-guided paired-view supervision and an explicit cross-view action-equivariance objective. Given paired observations of the...

</details>

---

### [WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA](https://arxiv.org/abs/2608.01035v1)

**Authors:** Zhihao Zhu, Hanlin Shang, Mingwang Xu, Feipeng Cai, Zhuolin He et al. (9 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.01035v1) | [PDF](https://arxiv.org/pdf/2608.01035v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however, their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training them from scratch typically yields narrow, single-task architectures that lack holistic visual-linguistic reasoning. Successfully transfo...

</details>

---

### [VLAGuard: A Framework for Evaluating and Mitigating Physical Attention Hijacking in Vision-Language-Action Robots within Wireless Sensor Networks](https://arxiv.org/abs/2608.01028v1)

**Authors:** Dongfu Yin, Jinquan Zhang

**Published:** 2026-08-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01028v1) | [PDF](https://arxiv.org/pdf/2608.01028v1.pdf)

<details>
<summary>Abstract</summary>

Deploying Vision-Language-Action (VLA) robots as mobile edge nodes within wireless sensor networks (WSNs) requires robust protection against physical adversarial threats. We present VLAGuard, a framework to assess and mitigate a critical vulnerability: policy-critical action-to-vision attention hijacking. We first introduce a stress-test module, Visuomotor Attention-guided Semantic Attack (VASA), using printable patches to severely distract the robot's action-conditioned cross-attention. To coun...

</details>

---

### [RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment](https://arxiv.org/abs/2608.01013v1)

**Authors:** Damir Nurtdinov, Alexei Kornaev, Alexander Maloletov

**Published:** 2026-08-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01013v1) | [PDF](https://arxiv.org/pdf/2608.01013v1.pdf)

<details>
<summary>Abstract</summary>

Adapting a pretrained vision-language-action (VLA) policy to a new robot usually assumes embodiment-specific demonstrations. This assumption is especially restrictive for custom robots whose morphology differs strongly from the manipulators seen in large robot datasets. We study a harder setting: zero-demo embodiment alignment of OpenVLA-OFT on a cable-driven parallel robot (CDPR) with a simple gripper and a previously unseen control interface. Instead of supervised fine-tuning, we use reinforce...

</details>

---
