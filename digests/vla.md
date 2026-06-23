# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-23 22:59 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686v1)

**Authors:** Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo et al. (14 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23686v1) | [PDF](https://arxiv.org/pdf/2606.23686v1.pdf) | [Project Page](https://libero-safety.github.io/)

<details>
<summary>Abstract</summary>

Despite the impressive manipulation capabilities of Vision-Language-Action (VLA) models, their operational safety under strict constraints remains largely unverified. To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. Leveraging this infrastructure, we curate a large-scale dataset ...

</details>

---

### [Flatness Preserves Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2606.23641v1)

**Authors:** Haochen Zhang, Yonatan Bisk

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23641v1) | [PDF](https://arxiv.org/pdf/2606.23641v1.pdf) | [Project Page](can)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have the potential for open-world generalization by leveraging pretrained vision-language representations, yet downstream finetuning on limited robot data often degrades these representations, leading to brittle policies that ignore language instructions in favor of visual shortcuts, a failure mode we term instruction blindness. We hypothesize that standard finetuning with limited data applies gradients to a sparse set of points, which manifests as a sharp los...

</details>

---

### [Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models](https://arxiv.org/abs/2606.23147v1)

**Authors:** Pinhao Song, Ze Fu, Yutong Hu, Renaud Detry

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23147v1) | [PDF](https://arxiv.org/pdf/2606.23147v1.pdf) | [GitHub](https://github.com/mousecpn/Assistron.git)

<details>
<summary>Abstract</summary>

We propose Assistron, a shared autonomy model that leverages Vision-Language-Action (VLA) models to assist the user in daily activities. Our approach is grounded in two core principles: (1)~minimizing human cognitive and physical effort by leveraging VLA-driven autonomy for macro-movements, and (2)~prioritizing human intervention specifically at critical failure points. Driven by the user's verbal language commands, Assistron utilizes the VLA to autonomously execute macro-reaching trajectories, ...

</details>

---

### [UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models](https://arxiv.org/abs/2606.22794v1)

**Authors:** Lin Sun, Zhiwei Guan, Conglin Wang, Zihong Chen, Jianhai Yu et al. (10 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.22794v1) | [PDF](https://arxiv.org/pdf/2606.22794v1.pdf) | [GitHub](https://github.com/linsun449/UniFS)

<details>
<summary>Abstract</summary>

Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. Moreover, because the action expert receives only the VLM's final-layer representation at a single fixed frequency, rich intermediate features are discarded, limiting both i...

</details>

---

### [PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models](https://arxiv.org/abs/2606.22540v1)

**Authors:** Xianghui Wang, Feng Chen, Wenbo Zhang, Hua Yan, Zixuan Wang et al. (7 authors)

**Published:** 2026-06-21 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.22540v1) | [PDF](https://arxiv.org/pdf/2606.22540v1.pdf) | [Project Page](https://inceptionwang.github.io/PolicyTrim/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency. While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic \textbf{policy efficiency} of these models remains largely unexplored. Policy efficiency is fundamentally affected by two factors, namely the effective executable length of predicted action chunks and the to...

</details>

---

## Other Recent Papers

### [LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation](https://arxiv.org/abs/2606.23685v1)

**Authors:** Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi et al. (18 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23685v1) | [PDF](https://arxiv.org/pdf/2606.23685v1.pdf)

<details>
<summary>Abstract</summary>

Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting ...

</details>

---

### [dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models](https://arxiv.org/abs/2606.23623v1)

**Authors:** Yuhao Wu, Yitian Liu, Weijie Shen, Mishuo Han, Wenjie Xu et al. (16 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23623v1) | [PDF](https://arxiv.org/pdf/2606.23623v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have established a powerful paradigm for generalist robotic manipulation by grounding control into the semantic reasoning of VLMs. Prevailing architectures typically model actions continuously via diffusion or flow processes, or discretely through either autoregressive generation or parallel decoding. Recently, Discrete Diffusion VLAs (dVLAs) have emerged as a distinct alternative, unifying vision, language, and action into a single discrete token space via ma...

</details>

---

### [RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models](https://arxiv.org/abs/2606.23617v1)

**Authors:** Ulas Berk Karli, Tesca Fitzgerald

**Published:** 2026-06-22 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.23617v1) | [PDF](https://arxiv.org/pdf/2606.23617v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation learning, where additional demonstrations are collected for tasks where the policy performs poorly. This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. In this paper, we propose an active, con...

</details>

---

### [KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies](https://arxiv.org/abs/2606.23589v1)

**Authors:** Yihan Zeng, Minghao Ye, Yiyuan Chen, Yide Shentu, Philipp Wu et al. (7 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23589v1) | [PDF](https://arxiv.org/pdf/2606.23589v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation remains challenging because similar observations may occur at different execution stages, while the appropriate action depends on previously completed operations. Memory can address this ambiguity by enabling policies to infer task progress from execution history. However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. In this work,...

</details>

---

### [A Watermark for Vision-Language-Action and World Action Models](https://arxiv.org/abs/2606.23574v1)

**Authors:** Yule Liu, Shuai Liu, Jiaheng Wei, Xinlei He

**Published:** 2026-06-22 | **Categories:** cs.CR, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23574v1) | [PDF](https://arxiv.org/pdf/2606.23574v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models and world-action models (WAM) are the generative models now driving general-purpose robot control, turning raw camera input directly into motor commands. They are increasingly deployed as black-box services, where a partner runs the policy through an interface while the owner keeps the weights private. Training such a model takes proprietary data and heavy computational power, making the deployed model itself a valuable intellectual property. To address this, ...

</details>

---

### [BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation](https://arxiv.org/abs/2606.23531v1)

**Authors:** Jinsong Lin, Chi kit Ng, Zhiyong Xiong, Zikang Pan, Yihan Hu et al. (11 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23531v1) | [PDF](https://arxiv.org/pdf/2606.23531v1.pdf)

<details>
<summary>Abstract</summary>

Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable a...

</details>

---

### [Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models](https://arxiv.org/abs/2606.22966v1)

**Authors:** Linghan Chen, Kaiyan Ji, Minyu Guo

**Published:** 2026-06-22 | **Categories:** cs.LG, cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2606.22966v1) | [PDF](https://arxiv.org/pdf/2606.22966v1.pdf)

<details>
<summary>Abstract</summary>

Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. A downstream oracle, such as a safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check verifier, consumes z~ as a prediction of the future. The robustness of ...

</details>

---

### [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913v1)

**Authors:** Zisheng Chen, Yuping Qiu, Jianhua Han, Tao Tang, Xiuwei Chen et al. (9 authors)

**Published:** 2026-06-22 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.22913v1) | [PDF](https://arxiv.org/pdf/2606.22913v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving by incorporating reasoning for better interpretability and planning quality. However, most existing approaches directly generate the final trajectory without explicitly examining its future consequences, which limits their reliability in complex and dynamic environments. To address this limitation, we propose IRR-Drive (Intend, Reflect, Refine), an adaptive multimodal reflection framework for autonomous drivin...

</details>

---

### [HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning](https://arxiv.org/abs/2606.22860v1)

**Authors:** Jingyi Liu, Zhaohong Mai, ShunSen He, Hang Ren, Chao Wang et al. (8 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.22860v1) | [PDF](https://arxiv.org/pdf/2606.22860v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in generative imitation learning have significantly propelled the field of robotic manipulation. However, the majority of existing models rely heavily on Behavior Cloning (BC), a paradigm that suffers from compounding errors and distributional shift. Consequently, the efficacy of these models in practical industrial deployments remains limited. To address these challenges, we introduce a novel, plug-and-play fine-tuning pipeline designed to facilitate the robust deployment of...

</details>

---

### [Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA](https://arxiv.org/abs/2606.22836v1)

**Authors:** Michael Piseno, Guy Tevet, C. Karen Liu

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.22836v1) | [PDF](https://arxiv.org/pdf/2606.22836v1.pdf)

<details>
<summary>Abstract</summary>

We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera. The end-effector occupies a large and consistent region of the wrist view and masking it allows for embodiment-agnostic visual reasoning. Cloak renders a mask in simulation from the robot's known geometry, accurately and in real time, with no segmentation or generative models. During training, we augment the mask so ...

</details>

---

### [Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation](https://arxiv.org/abs/2606.23420v1)

**Authors:** Bruno Machado, Alexandre Chapin, Emmanuel Dellandrea, Liming Chen

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23420v1) | [PDF](https://arxiv.org/pdf/2606.23420v1.pdf)

<details>
<summary>Abstract</summary>

Flow matching has recently become a new standard for behavior cloning in robotic manipulation. However, state-of-the-art flow matching policies suffer from a systematic structural mismatch: they rely on a globally fixed isotropic source distribution despite the strongly fragmented and heteroscedastic structure of robotic action spaces. This agnostic initialization forces the model to learn highly entangled vector fields, bottlenecking training efficiency and limiting overall policy performance. ...

</details>

---

### [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085v1)

**Authors:** Haoran Zhang, Yifu Lu, Boyang Wang, Xuhui Kang, Yen-Ling Kuo et al. (8 authors)

**Published:** 2026-06-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.23085v1) | [PDF](https://arxiv.org/pdf/2606.23085v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks is particularly challenging because failure onset is often ambiguous and dense temporal annotations are typically unavailable. We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model. Foresight is trained using only final ...

</details>

---

### [Reference-Free Assessment of Physical Consistency in World Model-based Video Generation](https://arxiv.org/abs/2606.22363v1)

**Authors:** Yun Oh, Sukmin Yun

**Published:** 2026-06-21 | **Categories:** cs.AI, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.22363v1) | [PDF](https://arxiv.org/pdf/2606.22363v1.pdf)

<details>
<summary>Abstract</summary>

We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD)...

</details>

---

### [Benchmarking Robot Memory Under Interference](https://arxiv.org/abs/2606.22338v1)

**Authors:** Soumil Rathi

**Published:** 2026-06-21 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.22338v1) | [PDF](https://arxiv.org/pdf/2606.22338v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment. The robot's tasks may often require it to remember information from multiple sessions ago, making long-context robot memory important for real-world deployments. However, most robot-memory benchmarks today are based on single episodes or a short context. To measure how current robot memory systems perform on longer sessions with more distractions, we introduce RoboMME-Interferen...

</details>

---
