# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-29 18:32 UTC

**Papers found:** 24

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation](https://arxiv.org/abs/2605.30350v1)

**Authors:** Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim et al. (9 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.30350v1) | [PDF](https://arxiv.org/pdf/2605.30350v1.pdf) | [Project Page](https://dynaflip-robotics.github.io)

<details>
<summary>Abstract</summary>

Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and rob...

</details>

---

### [RoboWits: Unexpected Challenges for Robotic Creative Problem Solving](https://arxiv.org/abs/2605.30326v1)

**Authors:** Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths et al. (8 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.30326v1) | [PDF](https://arxiv.org/pdf/2605.30326v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable constructio...

</details>

---

### [Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation](https://arxiv.org/abs/2605.30282v1)

**Authors:** Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma et al. (12 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.30282v1) | [PDF](https://arxiv.org/pdf/2605.30282v1.pdf) | [Project Page](https://zuo-kuangji.github.io/Gaze2Act/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and ...

</details>

---

### [PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology](https://arxiv.org/abs/2605.29710v1)

**Authors:** Sergey Arkhangelskiy

**Published:** 2026-05-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.29710v1) | [PDF](https://arxiv.org/pdf/2605.29710v1.pdf) | [GitHub](https://github.com/Positronic-Robotics/phail-paper)

<details>
<summary>Abstract</summary>

Real-world evaluation of vision-language-action (VLA) policies still rests on binary success rate at a fixed timeout with $N \le 25$ rollouts per condition, almost always without confidence intervals or paired statistical comparison; these cohort sizes struggle to resolve close comparisons reliably. We introduce PhAIL (Physical AI Leaderboard, https://phail.ai), an open real-robot benchmark on a Franka FR3 (dataset, per-rollout artifacts, and end-to-end reference implementation) of a distributio...

</details>

---

### [Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling](https://arxiv.org/abs/2605.28803v1)

**Authors:** Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang et al. (9 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28803v1) | [PDF](https://arxiv.org/pdf/2605.28803v1.pdf) | [GitHub](https://github.com/UCMP13753/Omega-QVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We c...

</details>

---

### [How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures](https://arxiv.org/abs/2605.28726v1)

**Authors:** Krishnam Gupta

**Published:** 2026-05-27 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28726v1) | [PDF](https://arxiv.org/pdf/2605.28726v1.pdf) | [GitHub](https://github.com/krishnam94/vla-edge)

<details>
<summary>Abstract</summary>

We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level. Running VQ-BeT, Diffusion Policy, and ACT on identical evaluation protocols (n=450 episodes across PushT and ALOHA 14-DOF bimanual manipulation), we find: (1) direction reversal rate is a universal failure predictor across all three architectures (AUROC=0.93, 0.79, 0.91; p<0.001); (2) jerk monitoring is predictive only for discrete-token architectures, following a discrete-to-continuo...

</details>

---

### [GEM: Generative Supervision Helps Embodied Intelligence](https://arxiv.org/abs/2605.28548v1)

**Authors:** Ruowen Zhao, Bangguo Li, Zuyan Liu, Yinan Liang, Junliang Ye et al. (12 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28548v1) | [PDF](https://arxiv.org/pdf/2605.28548v1.pdf) | [Project Page](https://zhaorw02.github.io/GEM/)

<details>
<summary>Abstract</summary>

Embodied Vision-Language Models (VLMs) have demonstrated impressive performance and generalization in robotics, particularly within Vision-Language-Action frameworks. However, a significant gap remains between the high-level semantic focus of standard text-guided pre-training paradigms and the low-level spatial and physical knowledge critical for execution in embodied environments. In this paper, we introduce GEM, a Generative-supervised Embodied vision-language Model designed to bridge this div...

</details>

---

### [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](https://arxiv.org/abs/2605.27886v1)

**Authors:** Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.27886v1) | [PDF](https://arxiv.org/pdf/2605.27886v1.pdf) | [GitHub](https://github.com/NathanWu7/Tabero)

<details>
<summary>Abstract</summary>

Tactile sensing is essential for robots to achieve human-like gentle manipulation. However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop force feedback mechanisms. To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception. Fi...

</details>

---

## Other Recent Papers

### [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280v1)

**Authors:** Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie et al. (40 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.30280v1) | [PDF](https://arxiv.org/pdf/2605.30280v1.pdf)

<details>
<summary>Abstract</summary>

Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perceptio...

</details>

---

### [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/abs/2605.30226v1)

**Authors:** Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu et al. (8 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.30226v1) | [PDF](https://arxiv.org/pdf/2605.30226v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for grounding visual-language understanding into real-world robotic manipulation. However, dexterous manipulation remains challenging for VLA policies due to high-dimensional hand control and compounding execution errors, which makes real-world RL post-training essential for bridging the gap between visually grounded action generation and physically reliable dexterous execution. However, high-dimensional dexterous explorati...

</details>

---

### [VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing](https://arxiv.org/abs/2605.30117v1)

**Authors:** Haoyuan Shi, Xiancong Ren, Yingji Zhang, Qinfan Zhang, Jiayu Hu et al. (12 authors)

**Published:** 2026-05-28 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.30117v1) | [PDF](https://arxiv.org/pdf/2605.30117v1.pdf)

<details>
<summary>Abstract</summary>

Understanding how Vision-Language-Action (VLA) models transform multimodal knowledge into embodied control remains an open challenge. We present VLA-Trace, a progressive diagnostic framework that analyzes VLA models through a unified evidence chain from representation dynamics to causal control attribution and behavioral manifestation. It specifically combines cross-modal and checkpoint-drift centered kernel alignment (CKA) to trace representation evolution, attention knockout interventions to i...

</details>

---

### [VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies](https://arxiv.org/abs/2605.30011v1)

**Authors:** Mingjian Gao, Wenqiao Zhang, Yuqian Yuan, Yang Dai, Binhe Yu et al. (12 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.30011v1) | [PDF](https://arxiv.org/pdf/2605.30011v1.pdf)

<details>
<summary>Abstract</summary>

Recent work has begun to equip vision-language-action (VLA) policies with explicit intermediate reasoning. In embodied control, however, textual chain-of-thought is a poor fit: irrelevant or weakly textual information can interfere with action prediction, while autoregressive text decoding adds too much latency for real-time closed-loop execution. We present VISUALTHINK-VLA, a visual intermediate-reasoning framework for accurate, low-latency VLA policies. Our bootstrapping philosophy is to guide...

</details>

---

### [SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation](https://arxiv.org/abs/2605.29662v1)

**Authors:** Shilin Ma, Chubin Zhang, Changyuan Wang, Yuji Wang, Yue Wu et al. (9 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.29662v1) | [PDF](https://arxiv.org/pdf/2605.29662v1.pdf)

<details>
<summary>Abstract</summary>

Real-time inference of vision-language-action (VLA) models is essential for robotic control. While visual token pruning has shown strong potential for accelerating inference, most existing methods mainly base pruning decisions on shallow-layer cues and risk discarding visual information required by deep layers. To address this issue, we propose SAFE-Pruner, a plug-and-play pruning framework that incorporates attention cues of future layers into pruning decisions. Specifically, we identify semant...

</details>

---

### [VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models](https://arxiv.org/abs/2605.29605v1)

**Authors:** Dehao Huang, Aoxiang Gu, Chengjie Zhang, Bolin Zou, Wenlong Dong et al. (8 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.29605v1) | [PDF](https://arxiv.org/pdf/2605.29605v1.pdf)

<details>
<summary>Abstract</summary>

Confidence estimation for Vision-Language-Action (VLA) models is essential for robots to perform manipulation tasks in the open world, providing crucial signals for risk-sensitive decision-making and failure anticipation. Existing confidence estimation methods typically rely on ensemble-based paradigms or action-token probabilities to predict the likelihood of task success. However, they still encounter challenges in computational efficiency and cross-architecture generalizability. These methods...

</details>

---

### [Mitigating State Aliasing in Vision-Language-Action Models via Inverse Dynamics Learning](https://arxiv.org/abs/2605.29577v1)

**Authors:** Kyujin Lee, Injae Kim, Jihwan Park, Yejun Ju, Minseok Joo et al. (6 authors)

**Published:** 2026-05-28 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.29577v1) | [PDF](https://arxiv.org/pdf/2605.29577v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising framework that unifies perception, reasoning, and control for robot manipulation by adapting pretrained vision-language models (VLMs) to action prediction. However, VLM-derived representations are often insensitive to subtle visual distinctions required for low-level control, causing state aliasing between visually similar states that require substantially different actions. Prior VLA studies improve visual understanding by generati...

</details>

---

### [VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models](https://arxiv.org/abs/2605.29562v1)

**Authors:** Shengyu Si, Yuanzhuo Lu, Ruimeng Yang, Ziyi Ye, Zuxuan Wu et al. (6 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.29562v1) | [PDF](https://arxiv.org/pdf/2605.29562v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action~(VLA) models have shown strong potential for general-purpose robotic manipulation, yet they still struggle to generalize to unseen tasks that necessitate transferring relevant experience across objects, scenes, and action patterns. This paper proposes VLA-Pro, a plug-and-play framework designed to enhance cross-task generalization by storing task-relevant procedural memories at training time and transferring these memories during inference. Specifically, VLA-Pro stores tas...

</details>

---

### [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2605.29438v1)

**Authors:** Ye Li, Huanan Liu, Kangye Ji, Yuan Meng, Jiajun Fan et al. (10 authors)

**Published:** 2026-05-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.29438v1) | [PDF](https://arxiv.org/pdf/2605.29438v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are a powerful paradigm for generalist robotic control. However, their high computational cost and limited control frequency hinder real-time robotic manipulation, especially when large vision-language backbones and iterative action heads run at every control step. Existing VLA acceleration methods often optimize individual components or rely on fixed acceleration rules, treating different control steps with largely fixed computation and overlooking the non-un...

</details>

---

### [3DVLA: Enhancing Vision-Language-Action Models via 3D Spatial and Instance Understanding](https://arxiv.org/abs/2605.29416v1)

**Authors:** Zhongyu Xia, Yousen Tang, Bingqing Wei, Yongtao Wang

**Published:** 2026-05-28 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.29416v1) | [PDF](https://arxiv.org/pdf/2605.29416v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have achieved remarkable progress in robotic manipulation, yet they suffer from a critical limitation: a lack of 3D scene understanding. This deficiency manifests as three intertwined challenges: weak extraction of 3D spatial positions without enforcing multi-view consistency, inadequate 3D instance understanding, and fragile reasoning under occlusion. Although mature 3D perception methods exist, their direct integration into VLA pipelines is hindered by architectur...

</details>

---

### [ReasonBreak: Probing Vulnerabilities in Reasoning-Enabled Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2605.29114v1)

**Authors:** Mohammadreza Teymoorianfard, Jean-Philippe Monteuuis, Jonathan Petit, Amir Houmansadr

**Published:** 2026-05-27 | **Categories:** cs.CR, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.29114v1) | [PDF](https://arxiv.org/pdf/2605.29114v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models with integrated reasoning have been proposed for end-to-end autonomous driving, assuming a tight coupling between reasoning and trajectory generation. However, the robustness of such systems under realistic input perturbations remains largely unexplored. We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, ...

</details>

---

### [PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation](https://arxiv.org/abs/2605.28634v1)

**Authors:** Yutai Li, Shaohui Peng, Jiaming Guo, Di Huang, Zihao Zhang et al. (11 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28634v1) | [PDF](https://arxiv.org/pdf/2605.28634v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for generalist robotic policies, yet their adaptation is hindered by data inefficiency and poor generalization. We argue that these bottlenecks stem from the prevailing Direct Instruction-to-Control Mapping, which forces models to memorize monolithic trajectories rather than reusable motion patterns, i.e., primitives. We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble & Assemble para...

</details>

---

### [What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies](https://arxiv.org/abs/2605.28527v1)

**Authors:** Jiachen Zhang, Junnan Nie, Junyi Lao, Wei Cheng, Chenghao Liu et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28527v1) | [PDF](https://arxiv.org/pdf/2605.28527v1.pdf)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) policies are trained to imitate actions; their loss never asks them to estimate reward, progress, or future success. Their frozen representations nevertheless carry such information, and it can be read out and used to guide action choice without retraining the policy. From mixed successful and failed manipulation trajectories on LIBERO-Goal, we recover Monte-Carlo outcome targets using lightweight linear probes on frozen features. The targets are consistently predi...

</details>

---

### [Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation](https://arxiv.org/abs/2605.28486v1)

**Authors:** Yongchen Wang, Kangyi Lu, Lan Wei, Dandan Zhang

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28486v1) | [PDF](https://arxiv.org/pdf/2605.28486v1.pdf)

<details>
<summary>Abstract</summary>

Magnetically actuated microrobots have been used as wireless, non-contact manipulation tools at microscales, making them promising for minimally invasive applications. However, their control remains challenging due to indirect actuation, limited sensing, and nonlinear magnetic interactions. In this work, we propose Mag-VLA, a vision-language-action (VLA) model for dexterous magnetic microrobot manipulation using two robotic arms with mounted magnets for dynamic magnetic-field construction. Biman...

</details>

---

### [ProgVLA: Progress-Aware Robot Manipulation Skill Learning](https://arxiv.org/abs/2605.28231v1)

**Authors:** Seungsu Kim, Jinyoung Choi, Seungmin Baek, Jean-Michel Renders

**Published:** 2026-05-27 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28231v1) | [PDF](https://arxiv.org/pdf/2605.28231v1.pdf)

<details>
<summary>Abstract</summary>

We present ProgVLA, a compact vision-language-action (VLA) model designed for reliable robot manipulation under tight compute and memory budgets. The model specifically focuses on efficiently processing long multi-modal sequences by maintaining an explicit representation of task progress over extended horizons. To this end, ProgVLA integrates two key components. First, a multi-modal encoder with a two-stage Perceiver resampling scheme compresses variable-length visual, language, and propriocepti...

</details>

---

### [VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking](https://arxiv.org/abs/2605.28083v1)

**Authors:** Jiyuan Fu, Kaixun Jiang, Jingkai Jia, Zhaoyu Chen, Xueyao Chen et al. (10 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28083v1) | [PDF](https://arxiv.org/pdf/2605.28083v1.pdf)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have emerged as powerful generalist policies, their severe vulnerability to adversarial patches significantly hinders their deployment in safety-critical domains. Moreover, existing patch attacks primarily focus on white-box settings, heavily overfitting to the specific action output space of the target model, which results in poor cross-architecture transferability. To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that...

</details>

---
