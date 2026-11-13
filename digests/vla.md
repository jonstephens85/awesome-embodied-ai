# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-13 02:16 UTC

**Papers shown:** 45 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Scaling VLA Serving Under Robotic Execution Constraints](https://arxiv.org/abs/2611.14969)

**Authors:** Yue Zhang, Zicong Ye, Lufang Chen, Dance Yang, Mingyang Li et al. (17 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14969) | [PDF](https://arxiv.org/pdf/2611.14969) | [Code](https://github.com/X-Square-Robot/xinfer)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation. In our production setting, hundreds of VLA-powered robots are already operating in real-world environments, creating an immediate need for efficient fleet serving. We present XInfer, a production-deployed VLA serving system designed to reduce the inference infrastructure cost of large-scale robotic deployments. XInfer jointly coordinates heterogeneous VLA computation with the evolving response requirements of robotic execution. By exploiting computational parallelism while managin...

</details>

<details>
<summary>Share</summary>

```
Scaling VLA Serving Under Robotic Execution Constraints

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation.

arXiv: https://arxiv.org/abs/2611.14969
Code: https://github.com/X-Square-Robot/xinfer

#VLA #robotics
```

</details>

---

### [One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](https://arxiv.org/abs/2611.14432)

**Authors:** Ilia Larchenko, Gleb Zarin, Atindra Nair, Keerti Manney, Vitaly Kleban et al. (7 authors)

**Published:** 2026-11-10 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14432) | [PDF](https://arxiv.org/pdf/2611.14432) | [Project Page](https://robot-learning-collective.github.io/behavior-1k-2026/) | [Code](https://github.com/Robot-Learning-Collective/behavior-1k-solution-2026)

<details>
<summary>Abstract</summary>

We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion from 2025 was that the model was undertrained, so most of the 2026 work went into training the model...

</details>

<details>
<summary>Share</summary>

```
One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge

We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator.

arXiv: https://arxiv.org/abs/2611.14432
Project page: https://robot-learning-collective.github.io/behavior-1k-2026/
Code: https://github.com/Robot-Learning-Collective/behavior-1k-solution-2026

#VLA #robotics
```

</details>

---

### [Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation](https://arxiv.org/abs/2611.11981)

**Authors:** Jingxuan Chen, Junshi Luo, Chencheng Dong, Xiaojian Nie, Tongge Huang et al. (6 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11981) | [PDF](https://arxiv.org/pdf/2611.11981) | [Project Page](https://j-x-chen.github.io/Thermo-VLA-web/)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal images into cold and hot attribute representations and injects them into the RGB token through language-conditioned residual modulation, enabling temperature-driven target selection and continuous manipulation. We further construct six real-world...

</details>

<details>
<summary>Share</summary>

```
Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation

Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware re...

arXiv: https://arxiv.org/abs/2611.11981
Project page: https://j-x-chen.github.io/Thermo-VLA-web/

#VLA #robotics
```

</details>

---

### [Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models](https://arxiv.org/abs/2611.10443)

**Authors:** Jungin Park, Chaoran Zhu, Changjae Oh, Kwanghoon Sohn

**Published:** 2026-11-07 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.10443) | [PDF](https://arxiv.org/pdf/2611.10443) | [Code](https://github.com/park-jungin/spark-vla)

<details>
<summary>Abstract</summary>

Understanding three-dimensional physical structure has become essential for vision-language-action models (VLAs). However, existing approaches either rely on explicit geometric inputs at inference time or adopt a single visual pathway, potentially compromising the visual-semantic knowledge inherited from pre-trained models. We present SPARK-VLA, Spatial Representation distillation and Knowledge routing for VLAs, a preserve-specialize-route framework for spatially adapting VLAs without requiring external 3D inputs or experts at inference. SPARK-VLA consists of two key components: (1) spatial re...

</details>

<details>
<summary>Share</summary>

```
Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models

Understanding three-dimensional physical structure has become essential for vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.10443
Code: https://github.com/park-jungin/spark-vla

#VLA #robotics
```

</details>

---

### [How Much of Your VLA Is kNN](https://arxiv.org/abs/2611.13160)

**Authors:** Denis Grachev, Damien LaRocque, Omar Moured

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.13160) | [PDF](https://arxiv.org/pdf/2611.13160) | [Code](https://github.com/sereact/lerobot_knn)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models now exceed 95% success on the LIBERO simulation benchmark, yet it remains unclear how much of this performance requires generalization beyond the training demonstrations. In this work, we show that retrieving nearby demonstrations and reusing their action chunks achieves a success rate of 91.7 % on LIBERO without policy training. Under LIBERO-Plus perturbations, retrieval shows the smallest drop of all evaluated policies. Across nine publicly available VLAs, fine-tuning mostly makes the vision-language backbone a better retrieval key, and the actions of the...

</details>

<details>
<summary>Share</summary>

```
How Much of Your VLA Is kNN

Vision-language-action (VLA) models now exceed 95% success on the LIBERO simulation benchmark, yet it remains unclear how much of this performance requires generalization beyond the training demonstrations.

arXiv: https://arxiv.org/abs/2611.13160
Code: https://github.com/sereact/lerobot_knn

#VLA #robotics
```

</details>

---

### [Streaming Failure Forecasting: VLA Failure Monitors That Keep Learning After Deployment](https://arxiv.org/abs/2611.11688)

**Authors:** Amit Jadhav, Shaurya Beriwala, David Q. Liu, Yanfei Liu

**Published:** 2026-11-08 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11688) | [PDF](https://arxiv.org/pdf/2611.11688) | [Project Page](https://sff-research.org)

<details>
<summary>Abstract</summary>

Failure monitors for vision-language-action (VLA) policies are trained offline and then frozen. After deployment, lighting, objects and cameras drift, and the policy itself is updated or moved to new tasks. On recorded real-robot runs, after a switch of task or policy version, a frozen monitor fit on the old task ranks failures little better than chance. We present Streaming Failure Forecasting (SFF), a monitor that keeps learning from the one label every episode provides: whether it succeeded. SFF keeps the offline monitor's network fixed and refits only its last linear layer after each episo...

</details>

<details>
<summary>Share</summary>

```
Streaming Failure Forecasting: VLA Failure Monitors That Keep Learning After Deployment

Failure monitors for vision-language-action (VLA) policies are trained offline and then frozen.

arXiv: https://arxiv.org/abs/2611.11688
Project page: https://sff-research.org

#VLA #robotics
```

</details>

---

### [On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)

**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi et al. (13 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.09892) | [PDF](https://arxiv.org/pdf/2611.09892) | [Project Page](https://apple-aiml-research.github.io/ml-amp/)

<details>
<summary>Abstract</summary>

Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the...

</details>

<details>
<summary>Share</summary>

```
On Agentic Manipulation Policies

Recent work on robot manipulation has focused on specialist policies trained on demonstrations.

arXiv: https://arxiv.org/abs/2611.09892
Project page: https://apple-aiml-research.github.io/ml-amp/

#VLA #robotics
```

</details>

---

### [DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking](https://arxiv.org/abs/2611.09041)

**Authors:** Shengjun Deng, Yinghan Zhang, Chengrui Wei, Liu Liang, Songyuan Liu et al. (11 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.09041) | [PDF](https://arxiv.org/pdf/2611.09041) | [Code](https://github.com/Dobot-Team/dobot_track)

<details>
<summary>Abstract</summary>

Language-guided embodied person tracking requires a mobile agent to identify a target from a referring description and consistently follow the target under egocentric observations. We present DobotTrack, a target-grounded vision-language-action (VLA) framework that integrates auxiliary grounding supervision with efficient temporal modeling. We systematically investigate five auxiliary tasks---person segmentation, bounding-box grounding, visual-spatial classification (VSC), future DINO feature prediction, and future-frame prediction---and adopt complementary mask and bounding-box supervision to...

</details>

<details>
<summary>Share</summary>

```
DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking

Language-guided embodied person tracking requires a mobile agent to identify a target from a referring description and consistently follow the target under egocentric observations.

arXiv: https://arxiv.org/abs/2611.09041
Code: https://github.com/Dobot-Team/dobot_track

#VLA #robotics
```

</details>

---

### [Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models](https://arxiv.org/abs/2611.14834)

**Authors:** Wen-Han Hsieh, Ken Jiankun Zheng, Chia-Chien Chen, David M. Chan, Trevor Darrell

**Published:** 2026-11-10 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.14834) | [PDF](https://arxiv.org/pdf/2611.14834)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating alternatives with computationally expensive verifiers adds latency at each policy query. In this work, we propose HDH, a lightweight framework that uses hindsight from a frozen VLA's own deployments to improve action verification. The framework has three stages. First, we deploy the policy and collect its autonomous rollouts. We then train a compact action verifier to assign each action chunk a predicted task-success...

</details>

<details>
<summary>Share</summary>

```
Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models

Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation.

arXiv: https://arxiv.org/abs/2611.14834

#VLA #robotics
```

</details>

---

### [DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning](https://arxiv.org/abs/2611.14092)

**Authors:** Huaijin Pi, Zehong Shen, Yong Wang, Kechun Xu, Changpeng Wang et al. (11 authors)

**Published:** 2026-11-10 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14092) | [PDF](https://arxiv.org/pdf/2611.14092) | [Project Page](https://robbyant-research.github.io/DexSeed/)

<details>
<summary>Abstract</summary>

We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration-generation methods typically rely on costly teleoperated examples. Meanwhile, human hand--object datasets provide a reusable source, but existing transfer methods mainly reproduce given interactions. Turning these interactions into VLA training data further requires coverage of different objects and manipulation locations, together with executable arm and finger actions, and visual observations. To achieve this, we present DexSeed, a framework...

</details>

<details>
<summary>Share</summary>

```
DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning

We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning.

arXiv: https://arxiv.org/abs/2611.14092
Project page: https://robbyant-research.github.io/DexSeed/

#VLA #robotics
```

</details>

---

### [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)

**Authors:** Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi et al. (12 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.12382) | [PDF](https://arxiv.org/pdf/2611.12382) | [Code](https://github.com/ShivaTeam/AutoVLA-D)

<details>
<summary>Abstract</summary>

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous trajectory. We address this gap with TrajCond, which introduces a discrete trajectory-geometric condition for VLA planning. Specifically, we represent TrajCond as a 1D-Brohan differential action trajectory and learn it with a two-stage training framework before final continuous trajectory prediction. With the simultaneous autoregressive generation of discrete and numeric trajec...

</details>

<details>
<summary>Share</summary>

```
AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuo...

arXiv: https://arxiv.org/abs/2611.12382
Code: https://github.com/ShivaTeam/AutoVLA-D

#VLA #robotics
```

</details>

---

### [Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](https://arxiv.org/abs/2611.11854)

**Authors:** Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiajin Zheng, Yin Zhang et al. (7 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11854) | [PDF](https://arxiv.org/pdf/2611.11854)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy into a slow vision-language model (System 2) and a fast flow-matching action head (System 1) that r...

</details>

<details>
<summary>Share</summary>

```
Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation

Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each ex...

arXiv: https://arxiv.org/abs/2611.11854

#VLA #robotics
```

</details>

---

### [SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking](https://arxiv.org/abs/2611.11697)

**Authors:** Jiaxin Guo, Wenzhen Dong, Taoyu Wu, Haomin Kuang, Mengya Xu et al. (12 authors)

**Published:** 2026-11-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11697) | [PDF](https://arxiv.org/pdf/2611.11697) | [Project Page](https://wrld.github.io/surgtap-3d/)

<details>
<summary>Abstract</summary>

Understanding 3D scene dynamics in minimally invasive surgery (MIS) is a fundamental step toward physically intelligent and autonomous surgical systems. However, existing public datasets offer limited scalability and diversity in real-world clinical scenarios. Moreover, annotations typically focus on either tissue or instruments alone, overlooking tool-tissue interactions. This gap limits applications such as augmented reality guidance and autonomous surgery driven by vision-language-action (VLA) models or world models, which demand large-scale, high-quality 3D supervision. In this work, we co...

</details>

<details>
<summary>Share</summary>

```
SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking

Understanding 3D scene dynamics in minimally invasive surgery (MIS) is a fundamental step toward physically intelligent and autonomous surgical systems.

arXiv: https://arxiv.org/abs/2611.11697
Project page: https://wrld.github.io/surgtap-3d/

#VLA #robotics
```

</details>

---

### [Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.11554)

**Authors:** Yunheng Wang, Jiaxi Zhang, Wei Lu, Yuetong Fang, Taowen Wang et al. (15 authors)

**Published:** 2026-11-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11554) | [PDF](https://arxiv.org/pdf/2611.11554) | [Project Page](https://kimodo-policy.github.io/)

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation requires continuous coordination of high-dimensional whole-body motion to realize task objectives. While vision-language-action models and world action models transfer semantic and visual-dynamics priors to robot control, these priors do not necessarily capture the structure of robot motion. We introduce Kinematic Action Models (KAMs), a paradigm that treats whole-body motion as a direct pretraining target and uses a pretrained motion generator as the primary action-generation backbone. KAMs ground learned temporal and cross-body coordination priors through task cond...

</details>

<details>
<summary>Share</summary>

```
Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation

Humanoid loco-manipulation requires continuous coordination of high-dimensional whole-body motion to realize task objectives.

arXiv: https://arxiv.org/abs/2611.11554
Project page: https://kimodo-policy.github.io/

#VLA #robotics
```

</details>

---

### [ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.08827)

**Authors:** Sungwon Moon, Minji Kim, Hyemin Boo, Daeun Song, Jiyoung Lee

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08827) | [PDF](https://arxiv.org/pdf/2611.08827)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control. Visual token pruning reduces this cost; however, prior methods estimate token redundancy from encoded visual embeddings or attention, only after the visual encoder has processed the entire observation. We propose \ours, a training-free token pruning method that moves the pruning decision ahead of the vision encoder by grounding it in a geometric prior derived from the robot's own action. The action chunk predic...

</details>

<details>
<summary>Share</summary>

```
ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models

Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control.

arXiv: https://arxiv.org/abs/2611.08827

#VLA #robotics
```

</details>

---

### [APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.13030)

**Authors:** Xiaoyang Xing, Chun-Mei Feng, Anthony Cohn, Xiaoliang Gong, Asoke Nandi

**Published:** 2026-11-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.13030) | [PDF](https://arxiv.org/pdf/2611.13030)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have demonstrated strong generalization in robotic manipulation, yet processing dense visual tokens often incurs high inference latency. Visual token pruning offers a practical way to reduce this cost, but identifying a compact set of tokens that preserves reliable action generation remains challenging. Existing methods largely rely on static or immediate heuristic cues to estimate token importance. We introduce APS-VLA, a framework that learns visual token selection from robot demonstrations while keeping the pretrained VLA backbone frozen. A lightweight...

</details>

<details>
<summary>Share</summary>

```
APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models

Vision-language-action (VLA) policies have demonstrated strong generalization in robotic manipulation, yet processing dense visual tokens often incurs high inference latency.

arXiv: https://arxiv.org/abs/2611.13030

#VLA #robotics
```

</details>

---

### [From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models](https://arxiv.org/abs/2611.11136)

**Authors:** Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang

**Published:** 2026-11-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11136) | [PDF](https://arxiv.org/pdf/2611.11136)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We introduce a framework that automatically generates game environments and expert demonstrations. An LLM-powered agent uses game-building tools to construct executable environments and tasks targeting specified skills. Programmatic experts then use privileged simulator state to generate aligned instructions, rendered observations, and keyboard and mouse actions. We train our game policy, Script2Play, by post-training a 4B vision-language model...

</details>

<details>
<summary>Share</summary>

```
From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models

Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations.

arXiv: https://arxiv.org/abs/2611.11136

#VLA #robotics
```

</details>

---

### [HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes](https://arxiv.org/abs/2611.09355)

**Authors:** Boran Zhao, Yanbin Hu, Jun Ye, Zhenxian Hu, Yuxin Zhai et al. (7 authors)

**Published:** 2026-11-06 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09355) | [PDF](https://arxiv.org/pdf/2611.09355)

<details>
<summary>Abstract</summary>

Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this challenge, we first introduce a hippocampus-inspired memory consolidation mechanism that synthesizes ex...

</details>

<details>
<summary>Share</summary>

```
HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes

Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes.

arXiv: https://arxiv.org/abs/2611.09355

#VLA #robotics
```

</details>

---

### [Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies](https://arxiv.org/abs/2611.14488)

**Authors:** Chubin Zhang, Bo An

**Published:** 2026-11-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.14488) | [PDF](https://arxiv.org/pdf/2611.14488)

<details>
<summary>Abstract</summary>

Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample frames uniformly across the episode and stamp each frame with its time step. Because time passes even when nothing happens, such a memory may not tell waiting from working. We show that it does not. On the counting tasks of RoboMME, we make the robot briefly pause or fidget its wrist. Such a null event changes nothing the task depends on, yet a released memory VLA counts the interval as work done and stops early. We call this failure phantom progre...

</details>

<details>
<summary>Share</summary>

```
Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

Memory-augmented vision-language-action (VLA) policies are meant to remember what happened.

arXiv: https://arxiv.org/abs/2611.14488

#VLA #robotics
```

</details>

---

### [VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess](https://arxiv.org/abs/2611.12676)

**Authors:** Matěj Kripner, Milan Straka

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.12676) | [PDF](https://arxiv.org/pdf/2611.12676)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are trained as general-purpose foundation models for robot learning, and require fine-tuning for each downstream task and robot. This raises practical questions such as how much data and training updates are needed, how checkpoints should be selected, and whether simulation can be leveraged to alleviate the cost of real data collection. We study these questions on a task that requires both precise manipulation and spatial understanding of the scene. In this task, an SO-101 arm moves a chess king between two squares that are given only by their names, such as...

</details>

<details>
<summary>Share</summary>

```
VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess

Vision-language-action (VLA) models are trained as general-purpose foundation models for robot learning, and require fine-tuning for each downstream task and robot.

arXiv: https://arxiv.org/abs/2611.12676

#VLA #robotics
```

</details>

---

### [VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation](https://arxiv.org/abs/2611.12286)

**Authors:** Yongxuan Lv, Zhen Fang, Lichen Man, Hao Li, Pu Li et al. (13 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.12286) | [PDF](https://arxiv.org/pdf/2611.12286)

<details>
<summary>Abstract</summary>

Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills. Vision-language-action (VLA) policies offer a shared interface, but task-specific post-training often produces separate specialists. Consolidation is difficult: mixed-task reinforcement learning provides sparse trajectory-level credit, while offline distillation may miss student-visited observations and endpoint distillation does not supervise intermediate action-generation states. We introduce VLA Multi-teacher On-Policy Distillation (VLA-MOPD), a protocol for c...

</details>

<details>
<summary>Share</summary>

```
VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation

Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills.

arXiv: https://arxiv.org/abs/2611.12286

#VLA #robotics
```

</details>

---

### [LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data](https://arxiv.org/abs/2611.12136)

**Authors:** Xueyang Wang, Zehong Shen, Dingkun Wei, Huaijin Pi, Changpeng Wang et al. (9 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.12136) | [PDF](https://arxiv.org/pdf/2611.12136) | [Project Page](https://robbyant-research.github.io/LHNav/)

<details>
<summary>Abstract</summary>

We study humanoid navigation across multiple destinations under long-horizon language instructions. This task is challenging because robots must maintain progress across successive goals while continuously producing natural, stable whole-body motion through confined spaces. However, task decomposition in existing methods does not by itself ensure progress throughout execution, while waypoint-based navigation does not guarantee natural, route-faithful whole-body motion. Our key idea is to organize navigation into three complementary roles operating at different time scales: a Brain for task rea...

</details>

<details>
<summary>Share</summary>

```
LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data

We study humanoid navigation across multiple destinations under long-horizon language instructions.

arXiv: https://arxiv.org/abs/2611.12136
Project page: https://robbyant-research.github.io/LHNav/

#VLA #robotics
```

</details>

---

### [DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving](https://arxiv.org/abs/2611.11856)

**Authors:** Bingzhang Wang, Mo Poorsartep, Yasaman Esfandiari

**Published:** 2026-11-09 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11856) | [PDF](https://arxiv.org/pdf/2611.11856)

<details>
<summary>Abstract</summary>

Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into a single model. Weight merging loses accuracy as heterogeneous domains accumulate, and dense mixture-of-experts routing is prohibitively expensive to combine them. We present DeltaForge, to our knowledge the first post-hoc mixture-of-experts VLA for driving, which consolidates N independently finetuned per-domain models into a single multi-domain model from their weights and a sma...

</details>

<details>
<summary>Share</summary>

```
DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving

Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into...

arXiv: https://arxiv.org/abs/2611.11856

#VLA #robotics
```

</details>

---

### [Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading](https://arxiv.org/abs/2611.11894)

**Authors:** Ali-Adeeb Abbas, Esmaeil Seraj

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11894) | [PDF](https://arxiv.org/pdf/2611.11894) | [Code](https://github.com/adeeb10abbas/weightsmith)

<details>
<summary>Abstract</summary>

Generalist robot policies often fail at one step of a task they can otherwise perform. We ask whether such a failure can be repaired by editing the policy's weights directly, without gradients, training data, or a change to the instruction. Told to put the cube then the banana in the bowl, a zero-shot $π_{0.5}$ vision-language-action policy in RoboLab releases the cube before it reaches the bowl. Replaying 21 of these decisions under rewordings shows that it binds "in the bowl" to the wrong object. Closed-form instruction distillation copies the per-layer effect of an explicit rewording into t...

</details>

<details>
<summary>Share</summary>

```
Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading

Generalist robot policies often fail at one step of a task they can otherwise perform.

arXiv: https://arxiv.org/abs/2611.11894
Code: https://github.com/adeeb10abbas/weightsmith

#VLA #robotics
```

</details>

---

### [HARP-Bench: Benchmarking Robot Manipulation Around Active Humans](https://arxiv.org/abs/2611.11123)

**Authors:** Qinhong Zhou, Riley Zong, Chunru Lin, Diyi Hu, Shivraj Singh Bhatti et al. (9 authors)

**Published:** 2026-11-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.11123) | [PDF](https://arxiv.org/pdf/2611.11123) | [Code](https://github.com/UMass-Embodied-AGI/harp)

<details>
<summary>Abstract</summary>

Recent robot manipulation benchmarks have enabled systematic evaluation of general-purpose robot policies across diverse objects, scenes, instructions, and embodiments. However, most existing benchmarks still assume that the robot is the only active agent and that task semantics are determined primarily by the instruction and object state. This assumption overlooks a common source of real-world variation: humans actively sharing the workspace. In such settings, humans may reveal an implicit goal, complete part of the task, temporarily change object availability, or constrain safe robot motion...

</details>

<details>
<summary>Share</summary>

```
HARP-Bench: Benchmarking Robot Manipulation Around Active Humans

Recent robot manipulation benchmarks have enabled systematic evaluation of general-purpose robot policies across diverse objects, scenes, instructions, and embodiments.

arXiv: https://arxiv.org/abs/2611.11123
Code: https://github.com/UMass-Embodied-AGI/harp

#VLA #robotics
```

</details>

---

### [Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration](https://arxiv.org/abs/2611.11098)

**Authors:** Zhengyang Cheng, He Zhu, Zeyu Guo, Zihan Liu, Anbang Wu et al. (9 authors)

**Published:** 2026-11-08 | **Categories:** cs.AR, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11098) | [PDF](https://arxiv.org/pdf/2611.11098)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to understand and execute complex instructions, but their autoregressive (AR) action generation introduces significant latency on resource-constrained robotic platforms. Speculative decoding can accelerate AR-based inference by parallelizing action generation and verification; however, existing approaches rely on costly draft models, which are inefficient on edge platforms. In this paper, we propose Zora, a hardware-software co-design framework for accelerating AR-based VLA inference. Specifically, Zora introduces a lightweight retrieval-augmen...

</details>

<details>
<summary>Share</summary>

```
Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration

Vision-language-action (VLA) models enable robots to understand and execute complex instructions, but their autoregressive (AR) action generation introduces significant latency on resource-constrained robotic platforms.

arXiv: https://arxiv.org/abs/2611.11098

#VLA #robotics
```

</details>

---

### [Zero-Shot VLA Adaptation with Retrieved Guidance](https://arxiv.org/abs/2611.10894)

**Authors:** Subin Kim, Anh-Quan Pham, Dinesh Jayaraman

**Published:** 2026-11-07 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10894) | [PDF](https://arxiv.org/pdf/2611.10894)

<details>
<summary>Abstract</summary>

Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation. However, these models still struggle under even small domain shifts relative to the training data, such as changes in camera viewpoint, background, object identity, or robot morphology. Motivated by the success of Retrieval-Augmented Generation (RAG) in language models, we pursue retrieval to boost VLA performance. Specifically, we seek to leverage retrieval from domain-mismatched, "in-the-wild" demonstration datasets like...

</details>

<details>
<summary>Share</summary>

```
Zero-Shot VLA Adaptation with Retrieved Guidance

Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2611.10894

#VLA #robotics
```

</details>

---

### [DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies](https://arxiv.org/abs/2611.10872)

**Authors:** Kevin Park, Izat Rasyad, Dvij Kalaria, Shankar Sastry

**Published:** 2026-11-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10872) | [PDF](https://arxiv.org/pdf/2611.10872)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies typically depends on substantial robot demonstration data, making human teleoperation a costly and cumbersome bottleneck, particularly for whole-body humanoid interaction. Reinforcement learning in simulation offers an alternative for scaling this data, but designing task-specific rewards remains challenging. To address this, we propose DreamVLA, which uses generated motion trajectories to guide reinforcement learning (RL) in simulation, converting them into reliable task execution trajectories. These trajectories train VLA models in simulation wi...

</details>

<details>
<summary>Share</summary>

```
DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies

Training vision-language-action (VLA) policies typically depends on substantial robot demonstration data, making human teleoperation a costly and cumbersome bottleneck, particularly for whole-body humanoid interaction.

arXiv: https://arxiv.org/abs/2611.10872

#VLA #robotics
```

</details>

---

### [SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning](https://arxiv.org/abs/2611.09684)

**Authors:** Jingye Zhang, Choo Sin Wai, Dake Zhong, Zhifang Liu, Yuhong Zhang et al. (11 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09684) | [PDF](https://arxiv.org/pdf/2611.09684)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data. In manipulation tasks, this dependence is compounded by structured spatiotemporal uncertainty in the action space: multiple nearby actions or trajectories may successfully solve the same task, while semantically equivalent demonstrations often unfold at different speeds. Standard pointwise supervision treats each demonstrated action as an exact target, imposing an unnecessary learning burden under such uncerta...

</details>

<details>
<summary>Share</summary>

```
SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning

Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data.

arXiv: https://arxiv.org/abs/2611.09684

#VLA #robotics
```

</details>

---

### [VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models](https://arxiv.org/abs/2611.08987)

**Authors:** Takayuki Nishio

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.LG, cs.NI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08987) | [PDF](https://arxiv.org/pdf/2611.08987)

<details>
<summary>Abstract</summary>

Large vision-language-action (VLA) models generalize well but are difficult to run in real time on a robot, and small VLAs that run there fail more often. Remote inference over beyond-5G and 6G networks lets a robot use a large VLA on a server, but querying the server for every action chunk limits the number of robots per server. We propose VLA handover: the robot runs a small VLA (S-VLA) and switches to a large VLA (L-VLA) on a server only when the S-VLA is likely to fail. We formulate the switching as minimizing the request cost under a required success probability and, since this problem ca...

</details>

<details>
<summary>Share</summary>

```
VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models

Large vision-language-action (VLA) models generalize well but are difficult to run in real time on a robot, and small VLAs that run there fail more often.

arXiv: https://arxiv.org/abs/2611.08987

#VLA #robotics
```

</details>

---

### [PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation](https://arxiv.org/abs/2611.08917)

**Authors:** Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08917) | [PDF](https://arxiv.org/pdf/2611.08917)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy must retain previously acquired skills and reuse them inside composite tasks whose behavior changes across phases. The standard recipe absorbs every new task into one shared update, which provides neither a parameter-level locus for reusable skills nor a mechanism for invoking each skill along the trajectory. We observe that this missing structure is latent rather than absent: per-s...

</details>

<details>
<summary>Share</summary>

```
PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation

Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy mu...

arXiv: https://arxiv.org/abs/2611.08917

#VLA #robotics
```

</details>

---

### [Localizing and Editing the Goal Representation of a Vision-Language-Action Model](https://arxiv.org/abs/2611.08895)

**Authors:** Sudhanshu Srivastava, Faisal Aqlan

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08895) | [PDF](https://arxiv.org/pdf/2611.08895)

<details>
<summary>Abstract</summary>

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove". We study whether OpenVLA follows such prohibitions and where it represents the goal it executes. The 10 tasks of LIBEROGoal share one scene, so we can label the goal that each rollout executes. We combine closed-loop rollouts with activation patching, linear probes, activation steering and runtime monitors. On LIBERO-Goal, negation had no detectable effect on which task OpenVLA executed. The model executed the forbidden task in 79% of negated rollouts and completed 78% of plain tasks....

</details>

<details>
<summary>Share</summary>

```
Localizing and Editing the Goal Representation of a Vision-Language-Action Model

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove".

arXiv: https://arxiv.org/abs/2611.08895

#VLA #robotics
```

</details>

---

### [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://arxiv.org/abs/2611.12806)

**Authors:** Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu, Yongyi Jia et al. (19 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.12806) | [PDF](https://arxiv.org/pdf/2611.12806)

<details>
<summary>Abstract</summary>

Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from sensor-specific physics, so that embodied models can effectively leverage heterogeneous tactile data. To this end, we develop LingBot-Touch, a tactile foundation model characterized by the f...

</details>

<details>
<summary>Share</summary>

```
Learning Heterogeneous Tactile Representation for General Dexterous Manipulation

Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence.

arXiv: https://arxiv.org/abs/2611.12806

#VLA #robotics
```

</details>

---

### [Be My Eye: Learning to See Beyond a Robot's Own Perspective](https://arxiv.org/abs/2611.12295)

**Authors:** Baifu Huang, Shilin Fang, Jianan Wang

**Published:** 2026-11-09 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.12295) | [PDF](https://arxiv.org/pdf/2611.12295)

<details>
<summary>Abstract</summary>

Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution. A key challenge is leveraging complementary observations from partner robots to support collaborative decision-making. We argue that information sharing should go beyond passively transmitting raw observations or generic visual features. Instead, robots should selectively encode task-relevant information according to task objectives and execution progress. To this end, we propose a task-ori...

</details>

<details>
<summary>Share</summary>

```
Be My Eye: Learning to See Beyond a Robot's Own Perspective

Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution.

arXiv: https://arxiv.org/abs/2611.12295

#VLA #robotics
```

</details>

---

### [PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation](https://arxiv.org/abs/2611.11798)

**Authors:** Sung-Wook Lee, Xuhui Kang, Dylan Losey, Yen-Ling Kuo

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11798) | [PDF](https://arxiv.org/pdf/2611.11798)

<details>
<summary>Abstract</summary>

While imitation learning has made substantial progress toward generalizable robot manipulation through scaling, viewpoint robustness remains a major bottleneck. Visuomotor policies rely heavily on visual inputs, yet images provide an inherently ambiguous signal under viewpoint change: similar scenes may appear markedly different across viewpoints, while distinct states may share certain visual overlaps. A policy must therefore infer not only the task-relevant state, but also how it is visually projected under a particular camera configuration. This entanglement of viewpoint-dependent appearanc...

</details>

<details>
<summary>Share</summary>

```
PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation

While imitation learning has made substantial progress toward generalizable robot manipulation through scaling, viewpoint robustness remains a major bottleneck.

arXiv: https://arxiv.org/abs/2611.11798

#VLA #robotics
```

</details>

---

### [Motion Belief Action: From a Visual Scene Map to Physical Decisions](https://arxiv.org/abs/2611.12113)

**Authors:** Dibyendu Ghosh

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.12113) | [PDF](https://arxiv.org/pdf/2611.12113)

<details>
<summary>Abstract</summary>

A robot that works among people must judge what it cannot see: whether an object is still where it was last seen, and whether a pull on a door or drawer is worth its risk. Maps that track object change hold nothing about force, maps of physical properties answer a risk question at a fixed risk level, and vision-language-action models keep no explicit estimate of hidden physics. We propose Motion Belief Action (MBA), a decision layer on the scene map. From how often people move an object and how much force it needs, how much load it holds and whether it is blocked, MBA chooses under a force lim...

</details>

<details>
<summary>Share</summary>

```
Motion Belief Action: From a Visual Scene Map to Physical Decisions

A robot that works among people must judge what it cannot see: whether an object is still where it was last seen, and whether a pull on a door or drawer is worth its risk.

arXiv: https://arxiv.org/abs/2611.12113

#VLA #robotics
```

</details>

---

### [Control-Aware Command Generation for Asynchronous Control and Action Inference with Vision-Based Policies towards Fast Execution](https://arxiv.org/abs/2611.11089)

**Authors:** Takayuki Osa, Kazuki Ota

**Published:** 2026-11-08 (updated 2026-11-10) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11089) | [PDF](https://arxiv.org/pdf/2611.11089)

<details>
<summary>Abstract</summary>

Vision-based control policies, including vision-language-action models, have enabled robots to perform increasingly complex tasks. However, their execution speed is often limited by the high computational cost of action inference. In this work, we investigate what can be achieved at the control level without modifying the underlying policy learning process. We introduce an asynchronous inference and control framework that enables fast task execution while maintaining smooth and stable robot motions. By formulating the generation of continuous target positions from discontinuous model predictio...

</details>

<details>
<summary>Share</summary>

```
Control-Aware Command Generation for Asynchronous Control and Action Inference with Vision-Based Policies towards Fast Execution

Vision-based control policies, including vision-language-action models, have enabled robots to perform increasingly complex tasks.

arXiv: https://arxiv.org/abs/2611.11089

#VLA #robotics
```

</details>

---

### [ODEAction: From Predicting Chunks to Evolving Actions](https://arxiv.org/abs/2611.09672)

**Authors:** Qishen Wang, Pengxiang Ding, Shifeng Bao, Mingyang Sun, Hengtao Li et al. (17 authors)

**Published:** 2026-11-06 (updated 2026-11-10) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09672) | [PDF](https://arxiv.org/pdf/2611.09672)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically generate actions in chunks, dividing continuous robot execution into separately predicted action chunks, which can introduce discontinuities at chunk boundaries. We propose ODEAction, a chunk-free action generation paradigm that replaces action chunk prediction with Continuous Action Evolution. We use an ordinary differential equation (ODE) to describe the continuous evolution of actions, and define the vector field of this ODE as the Action Transition Field to characterize how actions evolve with respect to evolution time. During inference, the mo...

</details>

<details>
<summary>Share</summary>

```
ODEAction: From Predicting Chunks to Evolving Actions

Vision-language-action (VLA) models typically generate actions in chunks, dividing continuous robot execution into separately predicted action chunks, which can introduce discontinuities at chunk boundaries.

arXiv: https://arxiv.org/abs/2611.09672

#VLA #robotics
```

</details>

---

### [Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G](https://arxiv.org/abs/2611.11023)

**Authors:** Wanlu Sun, Zhenhui Yuan, Xiang Ji, Yi Han, Qing Li et al. (6 authors)

**Published:** 2026-11-07 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.11023) | [PDF](https://arxiv.org/pdf/2611.11023)

<details>
<summary>Abstract</summary>

Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have significantly enhanced the capabilities of embodied agents in complex environments. However, deploying these models remains challenging due to the limited computational resources and energy budgets of robotic platforms. A fundamental question is where inference should be executed. Collaborative inference, which partitions m...

</details>

<details>
<summary>Share</summary>

```
Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G

Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control.

arXiv: https://arxiv.org/abs/2611.11023

#VLA #robotics
```

</details>

---

### [Look Ahead: Search-Driven Reasoning in Embodied AI](https://arxiv.org/abs/2611.10769)

**Authors:** Ahmed Zeer, Osama Shbib, Muzaffer Kaan Yuce, Himmet Toprak Kesgin, Mehmet Fatih Amasyali

**Published:** 2026-11-07 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10769) | [PDF](https://arxiv.org/pdf/2611.10769)

<details>
<summary>Abstract</summary>

Search allows a robotic policy to evaluate candidate futures before committing to an action. Motivated by test-time planning for vision-language action (VLA) models, we study selective search over action chunks in PushT using a frozen Action Chunking with Transformers (ACT) policy. Beam search generates perturbed alternatives around the policy prediction and scores them through rollouts from cloned simulator states. Across 50 evaluation episodes, beam search raises task success from 0% to 18% and increases average cumulative reward from 39.44 to 103.2. We introduce One Step Ahead (OSA), a gate...

</details>

<details>
<summary>Share</summary>

```
Look Ahead: Search-Driven Reasoning in Embodied AI

Search allows a robotic policy to evaluate candidate futures before committing to an action.

arXiv: https://arxiv.org/abs/2611.10769

#VLA #robotics
```

</details>

---

### [RoboACE: Adversarial Co-Evolution for Robot Self-Improvement](https://arxiv.org/abs/2611.13034)

**Authors:** Delin Zhao, Zhengrong Yue, Junlin He, Yali Wang

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.13034) | [PDF](https://arxiv.org/pdf/2611.13034)

<details>
<summary>Abstract</summary>

Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged. Useful practice depends on the agent's current capabilities, so the procedure that chooses practice must also be revisable. We present RoboACE (Robot Adversarial Co-Evolution), a framework that jointly evolves curriculum and execution harnesses around frozen foundation models. The curriculum harness uses accumulated capability evidence to propose informative challenges, while the execution harness responds wi...

</details>

<details>
<summary>Share</summary>

```
RoboACE: Adversarial Co-Evolution for Robot Self-Improvement

Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged.

arXiv: https://arxiv.org/abs/2611.13034

#VLA #robotics
```

</details>

---

### [Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks](https://arxiv.org/abs/2611.13039)

**Authors:** Zequan Zeng, Kai Wang, Delvin Ce Zhang, Huaping Liu, Zhipeng Yuan et al. (7 authors)

**Published:** 2026-11-09 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.13039) | [PDF](https://arxiv.org/pdf/2611.13039)

<details>
<summary>Abstract</summary>

Reliable medical laboratory automation requires robots to complete entire workflows in protocol order while handling changes during execution. A robot may execute each motion correctly yet fail the workflow by confusing visually similar stages or stalling after human intervention. We present Robo-MLT, a dual-system framework that couples explicit workflow monitoring with learned action generation. A vision--language planner composes an ordered atomic-skill sequence from the protocol and the initial workspace observation. A multiframe execution monitor detects when the active skill has complete...

</details>

<details>
<summary>Share</summary>

```
Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks

Reliable medical laboratory automation requires robots to complete entire workflows in protocol order while handling changes during execution.

arXiv: https://arxiv.org/abs/2611.13039

#VLA #robotics
```

</details>

---

### [When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary](https://arxiv.org/abs/2611.11438)

**Authors:** Yiming Sun, Mi Zhang

**Published:** 2026-11-08 | **Categories:** cs.RO, cs.CR, cs.MM | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.11438) | [PDF](https://arxiv.org/pdf/2611.11438)

<details>
<summary>Abstract</summary>

Advances in spatial understanding have enabled frontier models to power coding agents that control a real robot arm zero-shot and end-to-end, without task-specific demonstrations or retraining. This brings two new safety challenges. First, the extensive knowledge of frontier models lets these agents perform tasks that earlier VLA and WAM paradigms could not, opening the door to new forms of capability misuse. Second, coding agents can access digital resources such as web pages and emails. Threats in these resources, such as indirect prompt injection, can carry over into the physical world when...

</details>

<details>
<summary>Share</summary>

```
When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary

Advances in spatial understanding have enabled frontier models to power coding agents that control a real robot arm zero-shot and end-to-end, without task-specific demonstrations or retraining.

arXiv: https://arxiv.org/abs/2611.11438

#VLA #robotics
```

</details>

---

### [Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376)

**Authors:** Jusheng Zhang, Keze Wang, Liang Lin

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.09376) | [PDF](https://arxiv.org/pdf/2611.09376)

<details>
<summary>Abstract</summary>

A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows. We bring weight-space programming to robot foundation policies: GPT-6 Astra reads weights and uses a CPU workspace and budgeted simulator feedback, without gradient updates or new demonstrations. Three independent sessions on $π_{0.5}$ all improve success on 765 held-out paraphrases; the best raises success from 86.3\% to 92.0\% (48 repairs, four regressions; exact paired $p=1.31\times10^{-10}$). Among the 335 instructions containing edited tokens, success rises from 74.3\% to 87...

</details>

<details>
<summary>Share</summary>

```
Can LLMs Debug Robots by Editing Their Weights?

A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows.

arXiv: https://arxiv.org/abs/2611.09376

#VLA #robotics
```

</details>

---

### [QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction](https://arxiv.org/abs/2611.12353)

**Authors:** Zhizhong Fu, Wei Zhou, Zhaoyang Jiang, Yudong Lin, Songlun Li et al. (10 authors)

**Published:** 2026-11-09 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.12353) | [PDF](https://arxiv.org/pdf/2611.12353)

<details>
<summary>Abstract</summary>

A key challenge in action-conditioned world modeling is to construct macro-states from high-dimensional observations that support recursive prediction under actions, while keeping their predicted evolution consistent with visual changes in generated observations. We propose QCC-WM, a visual world model based on Quotient-based Causal Construction. QCC-WM uses action responses to guide macro-variable construction for recursive action-conditioned prediction. A shared reference quotient measurement constrains the consistency between predicted states and observed changes, allowing macro-level predi...

</details>

<details>
<summary>Share</summary>

```
QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction

A key challenge in action-conditioned world modeling is to construct macro-states from high-dimensional observations that support recursive prediction under actions, while keeping their predicted evolution consistent...

arXiv: https://arxiv.org/abs/2611.12353

#VLA #robotics
```

</details>

---
