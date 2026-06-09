# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-09 18:05 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.08684v1)

**Authors:** George Ling, Lijin Yang, Hao Yang, Zhongzhan Huang

**Published:** 2026-06-07 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.08684v1) | [PDF](https://arxiv.org/pdf/2606.08684v1.pdf) | [GitHub](https://github.com/George-Ling3/BLUE)

<details>
<summary>Abstract</summary>

We present BLUE, a minimal method for better language use in vision-language-action (VLA) models for autonomous driving (AD). Through extensive analysis, we reveal that language matters on only a small fraction of routes, but on those routes it can greatly improve or degrade performance. Generating language at every frame is therefore inefficient, since most computation is spent on frames that do not benefit from language. We further show that pretrained VLA hidden states potentially already enc...

</details>

---

### [FiberTune: Preserving Action-Fiber Visual Residuals in Vision-Language-Action Fine-Tuning](https://arxiv.org/abs/2606.08653v1)

**Authors:** Haihao Lin, Xiangsheng Huang, Xiao Yang, Weibang Zhou, Yiqi Zhang et al. (10 authors)

**Published:** 2026-06-07 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.08653v1) | [PDF](https://arxiv.org/pdf/2606.08653v1.pdf) | [Project Page](https://fibertune.github.io/)

<details>
<summary>Abstract</summary>

Action-supervised fine-tuning of vision-language-action (VLA) policies fits demonstrations effectively but constrains only the directions that change predicted actions, leaving visual structure consistent across action-equivalent states free to collapse. We formalize this as residual visual collapse along local action fibers and propose FiberTune, a training-time objective that preserves teacher-structured visual residuals without adding inference-time overhead. FiberTune uses an online action p...

</details>

---

### [GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation](https://arxiv.org/abs/2606.08530v1)

**Authors:** Yuan Zhang, Shiqi Zhang, Yedong Shen, Shuai Dong, Jiajun Deng et al. (14 authors)

**Published:** 2026-06-07 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.08530v1) | [PDF](https://arxiv.org/pdf/2606.08530v1.pdf) | [GitHub](https://github.com/babynabeauty/GEAR-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong benchmark performance but still struggle in real-world deployment with unseen objects, background shifts, and different robot embodiments. We argue that this stems from the lack of a unified geometry-aware manipulation representation, leaving existing VLAs vulnerable to low-level trajectory supervision, misaligned 3D features, and embodiment differences. To address this, we propose GEAR-VLA, a VLA framework for learning unified geometry-aware ac...

</details>

---

## Other Recent Papers

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

### [Benchmarking Vision-Language-Action Models on SO-101: Failure and Recovery Analysis](https://arxiv.org/abs/2606.08881v1)

**Authors:** Yi Yu, Xinchuan Qiu

**Published:** 2026-06-07 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.08881v1) | [PDF](https://arxiv.org/pdf/2606.08881v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong generalization in robotic manipulation, yet existing evaluations are primarily conducted in simulation or on expensive robotic platforms, leaving their robustness on affordable real-world robots largely unexplored. We present a standardized real-world benchmark for evaluating representative VLA and imitation learning policies on the low-cost SO-101 robotic platform. The benchmark comprises four representative manipulation tasks togethe...

</details>

---

### [Language as a Sensor: Calibrated Spatial Belief Estimation in 3D Scenes from Natural Language](https://arxiv.org/abs/2606.08666v1)

**Authors:** Aryan Naveen, Jason Xinyu Liu, Luca Carlone, Andreea Bobu

**Published:** 2026-06-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.08666v1) | [PDF](https://arxiv.org/pdf/2606.08666v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in human-centric environments routinely receive natural-language descriptions of spatial information ("I left my backpack on the table") that reference parts of the world beyond their perceptual field of view. Traditional metric-semantic mapping ignores this signal, while off-the-shelf multimodal models remain limited in 3D spatial reasoning and are not directly amenable to fusion with other sensor modalities. To convert language observations into a calibrated spatial distributio...

</details>

---

### [Two Bridges, One Pathway: From VLMs to Generalizable VLAs with Embodied Trajectory-Coupled Data](https://arxiv.org/abs/2606.08520v1)

**Authors:** Linqi Yin, Shiduo Zhang, Shenling Qiu, Chenxin Li, Zhaoyang Fu et al. (14 authors)

**Published:** 2026-06-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.08520v1) | [PDF](https://arxiv.org/pdf/2606.08520v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) are powerful general-purpose reasoners, yet converting them into robot control policies (VLAs) is surprisingly difficult. The root cause is a two-fold gap: VLMs are trained on internet-scale images with language-understanding objectives, while VLAs must perceive robot scenes and predict motor actions. Fine-tuning a VLM directly on robot action data forces the model to cross both gaps at once -- the learning curve is steep and the rich generalizations learned during ...

</details>

---

### [EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control](https://arxiv.org/abs/2606.08495v1)

**Authors:** Haoyang Ge, Peng Ren, Yukun Shi, Cong Huang, Kun Li et al. (6 authors)

**Published:** 2026-06-07 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.08495v1) | [PDF](https://arxiv.org/pdf/2606.08495v1.pdf)

<details>
<summary>Abstract</summary>

Humanoid robots require whole-body motions that adapt to scene context, task requirements, and user intent. Motion tracking reproduces specified trajectories, and humanoid vision-language-action systems provide semantic interfaces, but neither offers a scalable and interactive prior for broad full-body behavior. We introduce EgoPriMo (Egocentric Motion Prior for Humanoid Robots), a unified framework that learns such priors from egocentric human demonstrations. Given egocentric observations and a...

</details>

---
