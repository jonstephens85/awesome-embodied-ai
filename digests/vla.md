# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-10 23:18 UTC

**Papers found:** 21

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination](https://arxiv.org/abs/2606.10862v1)

**Authors:** Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei

**Published:** 2026-06-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10862v1) | [PDF](https://arxiv.org/pdf/2606.10862v1.pdf) | [GitHub](https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VL...

</details>

---

### [SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation](https://arxiv.org/abs/2606.10305v1)

**Authors:** Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun et al. (11 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10305v1) | [PDF](https://arxiv.org/pdf/2606.10305v1.pdf) | [Project Page](https://qianzhong-chen.github.io/sarm2.github.io/)

<details>
<summary>Abstract</summary>

Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still relies heavily on behavior cloning, which requires costly high-quality demonstrations and keeps policies near the demonstration distribution. Reward models can reduce this dependence by reweighting demonstrations and providing dense supervision for on-robot reinforcement learning (RL), but they must be dense, accurate, and general. Existing methods fall short: task-specific stage-aware models are accurate but r...

</details>

---

### [MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](https://arxiv.org/abs/2606.09827v1)

**Authors:** Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou et al. (9 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09827v1) | [PDF](https://arxiv.org/pdf/2606.09827v1.pdf) | [Project Page](https://shihao1895.github.io/MemoryVLA-PP-Web)

<details>
<summary>Abstract</summary>

Temporal modeling is essential for robotic manipulation, as effective control requires both memory of past interactions and imagination of future states. However, most VLA models rely primarily on the current observation and therefore struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived context, the hippocampal system to preserve episodic memory of past experience, and internal models to imagine possible futur...

</details>

---

### [Scaling by Diversified Experience for Vision-Language-Action Models](https://arxiv.org/abs/2606.09009v1)

**Authors:** Leiyu Wang, Zhaofengnian Wang, Xueqi Li, Luoyi Fan, Cewu Lu et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09009v1) | [PDF](https://arxiv.org/pdf/2606.09009v1.pdf) | [Project Page](https://sy-vla.github.io/}{project)

<details>
<summary>Abstract</summary>

Vision-Language-Action models face significant challenges in real-world deployment due to the entanglement of high-level reasoning with low-level control, and the instability of policy optimization. In this paper, we introduce SyVLA, a robust VLA model trained with diversified experiences. We propose an Intention Decoupling algorithm to isolate control-relevant features from reasoning contexts and a similar-sample guided RL pipeline to stabilize policy updates and mitigate distribution shift. Ex...

</details>

---

## Other Recent Papers

### [Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations](https://arxiv.org/abs/2606.10614v1)

**Authors:** Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee et al. (6 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.10614v1) | [PDF](https://arxiv.org/pdf/2606.10614v1.pdf)

<details>
<summary>Abstract</summary>

Robotic foundation models pre-trained on human demonstration videos have shown promise, but a significant embodiment gap remains when the resulting policies are deployed on real robots. A common remedy is to fine-tune these models on robot-specific demonstrations. However, robot data collection can be prohibitively expensive and time-consuming, which is particularly acute in dexterous manipulation, e.g., teleoperating a multi-fingered hand for even a single atomic task can take days. To address ...

</details>

---

### [VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models](https://arxiv.org/abs/2606.10568v1)

**Authors:** Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei et al. (9 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10568v1) | [PDF](https://arxiv.org/pdf/2606.10568v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong promise for robotic manipulation, but their reliability at test time remains limited by one-shot action prediction, where even small action errors can cause grasp failure, collision, or incorrect task progression. A natural alternative is to equip VLA systems with test-time verification, allowing multiple candidate actions to be proposed and evaluated before execution. However, reliable action verification is challenging because it requires n...

</details>

---

### [Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults](https://arxiv.org/abs/2606.10501v1)

**Authors:** Minsoo Jo, Taeju Kwon, Junha Chun, Youngjoon Jeong, Taesup Kim

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10501v1) | [PDF](https://arxiv.org/pdf/2606.10501v1.pdf)

<details>
<summary>Abstract</summary>

Deploying Vision-Language-Action (VLA) models in real robotic systems requires robustness not only to semantic and perceptual variations, but also to embodiment-side faults that change how actions are physically realized. Real robots can experience joint-level changes caused by actuator degradation, hardware faults, safety limits, collision damage, or wear-induced friction. These faults are critical because they alter the action-to-motion interface of a policy, disrupting the learned closed-loop...

</details>

---

### [Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models](https://arxiv.org/abs/2606.10495v1)

**Authors:** Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang et al. (6 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10495v1) | [PDF](https://arxiv.org/pdf/2606.10495v1.pdf)

<details>
<summary>Abstract</summary>

Safe social navigation requires robots to distinguish people from ordinary obstacles and to react before danger becomes imminent. We show that pretrained Vision-Language-Action (VLA) models already encode pedestrian-object distinctions and future collision signals in their internal representations, but behavior cloning fails to translate these signals into socially appropriate actions. To address this mismatch, we propose SALSA, a two-stage annotation-free post-training framework: (1) social beh...

</details>

---

### [A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation](https://arxiv.org/abs/2606.10366v1)

**Authors:** Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10366v1) | [PDF](https://arxiv.org/pdf/2606.10366v1.pdf)

<details>
<summary>Abstract</summary>

Simulation has become an essential tool for evaluating and improving vision-language-action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation. Recent simulation benchmarks have made substantial progress on realism and diversity, yet these platforms have not been widely adopted as reliable proxies for real-world policy evaluation. In this work, we investigate this issue through the lens of sim-and-real correlation. We conduct a sy...

</details>

---

### [What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents](https://arxiv.org/abs/2606.10267v1)

**Authors:** Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang et al. (7 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.10267v1) | [PDF](https://arxiv.org/pdf/2606.10267v1.pdf)

<details>
<summary>Abstract</summary>

Hierarchical vision-language-action (Hi-VLA) systems have emerged as a promising paradigm for complex robot manipulation, by using high-level VLM planners to decompose tasks into language subgoals executed by low-level VLA controllers. Despite recent empirical progress, there is a lack of unified design principles for these systems: existing Hi-VLA systems differ in how they choose and connect planners, controllers, mechanisms to switch between the two, and how observations and memory are repres...

</details>

---

### [Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs](https://arxiv.org/abs/2606.10180v1)

**Authors:** Jonathan C. Kao, Jason Chan, Andy Wang

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2606.10180v1) | [PDF](https://arxiv.org/pdf/2606.10180v1.pdf)

<details>
<summary>Abstract</summary>

We introduce flow control of vision-language-action (VLA) models, a simple and effective way to steer VLA actions in real-time through generic inputs, such as a keyboard. This method can be used out-of-the-box and does not require retraining or fine-tuning VLAs. It enables relatively crude user inputs to steer a VLA to align with user intent. The VLA transforms these inputs into action samples drawn from the VLA expert action distribution learned during training, so that the generated actions ar...

</details>

---

### [Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models](https://arxiv.org/abs/2606.09749v1)

**Authors:** Seongbin Park, Fan Zhang, Baharan Mirzasoleiman, Shahriar Talebi, Nader Sehatbakhsh

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.09749v1) | [PDF](https://arxiv.org/pdf/2606.09749v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated impressive end-to-end performance across a variety of robotic manipulation tasks. However, these policies offer no guarantees against collisions with task-irrelevant objects in the scene. Existing safety filters sidestep this problem by querying a vision-language model (VLM) to identify obstacles and their locations. This, however, is too slow to run in the control loop and can only be invoked at episode initialization, leaving the filter una...

</details>

---

### [ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models](https://arxiv.org/abs/2606.09740v1)

**Authors:** Fan Zhang, Seongbin Park, Baharan Mirzasoleiman, Shariar Talebi, Nader Sehatbakhsh

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09740v1) | [PDF](https://arxiv.org/pdf/2606.09740v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate strong perfor-1 mance on language-conditioned robotic manipulation within their training dis-2 tribution, yet their generalization capabilities remain fundamentally limited. They3 lack the robustness required to handle perturbations, frequently failing when con-4 fronted with lighting changes, altered camera viewpoints, or small initial-state5 variations. We propose PROBEACT, a training-free runtime intervention frame-6 work that detects and recove...

</details>

---

### [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](https://arxiv.org/abs/2606.09630v1)

**Authors:** Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki et al. (7 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.09630v1) | [PDF](https://arxiv.org/pdf/2606.09630v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards dire...

</details>

---

### [CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control](https://arxiv.org/abs/2606.09572v1)

**Authors:** Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.09572v1) | [PDF](https://arxiv.org/pdf/2606.09572v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models have shown strong promise for robot manipulation, yet raw language is primarily needed to specify task intent rather than to be repeatedly processed during high-frequency low-level execution. Motivated by this separation, we propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-conditioned visuomotor control. CT-VAM acts as a compact local execution policy that predicts action chunks from dualview visual observations, proprioception, ...

</details>

---

### [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499v1)

**Authors:** Ethan Rathbun, Ahmed Agha, Saaduddin Mahmud, Christopher Amato, Alina Oprea et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2606.09499v1) | [PDF](https://arxiv.org/pdf/2606.09499v1.pdf)

<details>
<summary>Abstract</summary>

World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing their integration into the robot learning pipeline. While highly practical, in this work we demonstrate that world models introduce a uniquely stealthy and effective data poisoning entry point into the robot learning supply chain that can result in the deployment of unsafe or otherwi...

</details>

---

### [Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer](https://arxiv.org/abs/2606.09416v1)

**Authors:** Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.SE

**Links:** [arXiv](https://arxiv.org/abs/2606.09416v1) | [PDF](https://arxiv.org/pdf/2606.09416v1.pdf)

<details>
<summary>Abstract</summary>

Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing...

</details>

---

### [TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation](https://arxiv.org/abs/2606.09337v1)

**Authors:** Huaihang Zheng, Yi Yang, Kai Ma, Shenglin Xu, Tian Xie et al. (11 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09337v1) | [PDF](https://arxiv.org/pdf/2606.09337v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a powerful framework for robotic manipulation, and recent studies have introduced tactile or force feedback into VLAs to address contact-rich tasks. However, these models are typically deployed as offline policies. When contact conditions shift from the training distribution, the policy cannot perform online adaptation, leading to problems such as inappropriate contact forces and inefficient retries. Therefore, we propose TORL-VLA, a tactile-guided...

</details>

---

### [Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection](https://arxiv.org/abs/2606.09258v1)

**Authors:** Suyeon Shin, Juwon Kim, Hyeonbin Park, Hyunseo Kim, Hyundo Lee et al. (7 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09258v1) | [PDF](https://arxiv.org/pdf/2606.09258v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can deviate from nominal trajectories during manipulation, even when tasks remain physically feasible. Recovering from these deviations is challenging, as they push the policy into unfamiliar state spaces where direct re-planning frequently destabilizes action sequences. We propose Back to the Familiar Future (B2FF), a recovery framework for foresight-driven VLAs that leverages future visual conditioning as a recovery interface. Before execution, the VLA gen...

</details>

---

### [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215v1)

**Authors:** Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09215v1) | [PDF](https://arxiv.org/pdf/2606.09215v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple a video dynamics prior to the policy and have shown encouraging results on tabletop manipulation, but iterative denoising over high-dimensional video-action latents leaves them too slow for real-time humanoid loco-manipulation. The problem is compounded by the dominant hierarchical paradigm, in which a high-level manipulation policy controls only the upper body while a low-level controller tracks coarse base commands -- placing upper and lower body in inconsiste...

</details>

---

### [C$^3$ache: Accelerating World Action Models with Cross Inference Chunk Cache](https://arxiv.org/abs/2606.08962v1)

**Authors:** Weisen Zhao, Lam Nguyen, Zhicong Lu, Yuzhang Shang

**Published:** 2026-06-08 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.08962v1) | [PDF](https://arxiv.org/pdf/2606.08962v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) generalize better than standard Vision-Language-Action (VLA) policies to novel motions and environments, because a video-modeling objective lets them learn from abundant unlabeled video rather than scarce labeled robot demonstrations. This generalization is computationally expensive. To complete a task, a WAM runs over multiple inference chunks, and each chunk requires a costly denoising process. Existing acceleration methods reduce this cost by caching and reusing com...

</details>

---
