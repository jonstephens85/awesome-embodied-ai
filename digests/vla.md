# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-25 04:41 UTC

**Papers shown:** 121 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2611.32206)

**Authors:** Qing Zhang, Xuesong Li, Zhaoyuan Yang, Changlin Song, Xinyu Tian et al. (6 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32206) | [PDF](https://arxiv.org/pdf/2611.32206) | [Code](https://github.com/QZhang2111/psg)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are expected to inherit visual grounding from vision-language models, yet often reach for an object's training location after it has been moved. Across six VLAs, we identify two shortcuts: a scene shortcut, where the arm follows the scene's original task despite a new instruction, and an instruction shortcut, where the instruction retrieves the requested object's training location. In $π_{0.5}$, the instruction shortcut persists even though object-name attention follows the moved target. We call this Seeing Is Not Reaching. To determine whether this groundi...

</details>

<details>
<summary>Share</summary>

```
Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models

Vision-language-action models (VLAs) are expected to inherit visual grounding from vision-language models, yet often reach for an object's training location after it has been moved.

arXiv: https://arxiv.org/abs/2611.32206
Code: https://github.com/QZhang2111/psg

#VLA #robotics
```

</details>

---

### [Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for Vision-Language-Action Models](https://arxiv.org/abs/2611.31954)

**Authors:** Yifeng Lin, Liuxiang Qiu, Yunfeng Chen, Tiesong Zhao

**Published:** 2026-11-24 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31954) | [PDF](https://arxiv.org/pdf/2611.31954) | [Project Page](https://lin0e0.github.io/TauPrune-VLA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models must process continuous streams of visual observations, and the resulting computational cost limits real-time robotic control. Token pruning reduces this cost, but a fixed semantic scale of perceptual representation can overlook information needed at different stages of manipulation. We show that perceptual semantics can guide effective token selection without relying on internal attention when the selection scale adapts to the scene's evolving semantic structure. Based on this observation, we introduce TauPrune-VLA, a training-free method that controls the...

</details>

<details>
<summary>Share</summary>

```
Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for Vision-Language-Action Models

Vision-language-action (VLA) models must process continuous streams of visual observations, and the resulting computational cost limits real-time robotic control.

arXiv: https://arxiv.org/abs/2611.31954
Project page: https://lin0e0.github.io/TauPrune-VLA/

#VLA #robotics
```

</details>

---

### [EgoStudy: How Does Scaling Egocentric Data Affect VLA and WAM Pretraining?](https://arxiv.org/abs/2611.30490)

**Authors:** Puzhen Yuan, Yanjiang Guo, Yichen Liu, Xiang Zhu, Qingzhou Lu et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30490) | [PDF](https://arxiv.org/pdf/2611.30490) | [Project Page](https://puzhenyuan.github.io/EgoStudy-website)

<details>
<summary>Abstract</summary>

Egocentric human manipulation data offer a scalable resource for training dexterous robot policies. However, how effectively robots can learn and benefit from these data remains unclear due to the embodiment gap between humans and robots. We present EgoStudy, a systematic, controlled study of egocentric data for robot learning. Holding the robot dataset fixed, we vary the scale and diversity of egocentric data, data processing strategies, and co-training configurations. We investigate three questions: (1) Which data processing and pretraining choices most effectively exploit egocentric data? (...

</details>

<details>
<summary>Share</summary>

```
EgoStudy: How Does Scaling Egocentric Data Affect VLA and WAM Pretraining?

Egocentric human manipulation data offer a scalable resource for training dexterous robot policies.

arXiv: https://arxiv.org/abs/2611.30490
Project page: https://puzhenyuan.github.io/EgoStudy-website

#VLA #robotics
```

</details>

---

### [Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2611.30178)

**Authors:** Yanlong Chen, Thongthornpatch Chamadol, Yichen Guo, Yunfei Gao, Mohan Liu et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30178) | [PDF](https://arxiv.org/pdf/2611.30178) | [Code](https://github.com/ForeverBlue816/LoopQ)

<details>
<summary>Abstract</summary>

Deploying large vision-language-action (VLA) models on resource-constrained robots demands extreme compression, yet existing post-training quantization (PTQ) methods frequently collapse at ultra-low bit-widths ($\le$ 2 bits). We trace this failure to two mismatches in standard pipelines. First, calibrating on static offline demonstrations induces distribution shift: minor quantization perturbations drive the policy into unseen states where uncalibrated errors compound. Second, minimizing the layer-wise weight reconstruction error is a flawed proxy, as action generation depends only on the repr...

</details>

<details>
<summary>Share</summary>

```
Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models

Deploying large vision-language-action (VLA) models on resource-constrained robots demands extreme compression, yet existing post-training quantization (PTQ) methods frequently collapse at ultra-low bit-widths ($\le$...

arXiv: https://arxiv.org/abs/2611.30178
Code: https://github.com/ForeverBlue816/LoopQ

#VLA #robotics
```

</details>

---

### [Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning](https://arxiv.org/abs/2611.32304)

**Authors:** Simin Huang, Jiawei Chen, Shaolong Zhu, Qiwei Liang, Zhaoxia Yin

**Published:** 2026-11-24 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32304) | [PDF](https://arxiv.org/pdf/2611.32304) | [Code](https://github.com/vla-attack/Sparse_Poison_Strong_Hijack)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats. Among these threats, trajectory-level targeted backdoors are particularly challenging and may pose greater safety risks than behavior-disrupting attacks: rather than merely causing task failures or local action deviations, they must sustain closed-loop redirection to complete an attacker-specified multi-step task. To reliably induce such behaviors, existing methods typically rely on high poisoning rates to obtain sufficient target-trajectory supervision. Howe...

</details>

<details>
<summary>Share</summary>

```
Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning

Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats.

arXiv: https://arxiv.org/abs/2611.32304
Code: https://github.com/vla-attack/Sparse_Poison_Strong_Hijack

#VLA #robotics
```

</details>

---

### [Hi3R-VLA: Grounding Semantics and Actions in 3D](https://arxiv.org/abs/2611.31535)

**Authors:** Shizhe Chen, Paul Pacaud, Cordelia Schmid

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31535) | [PDF](https://arxiv.org/pdf/2611.31535) | [Project Page](https://cshizhe.github.io/projects/hi3r_vla.html)

<details>
<summary>Abstract</summary>

While recent vision-language-action (VLA) models increasingly incorporate 3D geometry, how to effectively exploit it for precise and generalizable action prediction remains a central challenge. We introduce Hi3R-VLA, a 3D policy that grounds heterogeneous modalities - vision, language, and action - in explicit 3D geometry for robotic manipulation. Our model integrates spatially-aligned visual features and language conditioning into point cloud representations, enriching scene geometry with fine-grained, task-relevant semantics. It then anchors low-level control commands in the same 3D coordina...

</details>

<details>
<summary>Share</summary>

```
Hi3R-VLA: Grounding Semantics and Actions in 3D

While recent vision-language-action (VLA) models increasingly incorporate 3D geometry, how to effectively exploit it for precise and generalizable action prediction remains a central challenge.

arXiv: https://arxiv.org/abs/2611.31535
Project page: https://cshizhe.github.io/projects/hi3r_vla.html

#VLA #robotics
```

</details>

---

### [Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs](https://arxiv.org/abs/2611.31511)

**Authors:** Adrià Ruiz, Bartłomiej Twardowski, Tinne Tuytelaars, Sergi Masip

**Published:** 2026-11-23 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31511) | [PDF](https://arxiv.org/pdf/2611.31511) | [Project Page](https://adrrp.github.io/vla-ood-robustness)

<details>
<summary>Abstract</summary>

Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay. However, robustness to domain shift of learned tasks remains unexplored. In this work, we study the robustness of Pi0 fine-tuned with experience replay under out-of-distribution (OOD) data using the LIBERO and LIBERO-Plus benchmarks. While the in-domain (ID) setup achieves near-zero catastrophic forgetting, OOD performance on previous tasks quickly collapses. Specifically, we show that during the continual learning process, the OOD c...

</details>

<details>
<summary>Share</summary>

```
Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs

Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay.

arXiv: https://arxiv.org/abs/2611.31511
Project page: https://adrrp.github.io/vla-ood-robustness

#VLA #robotics
```

</details>

---

### [Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action](https://arxiv.org/abs/2611.31240)

**Authors:** Seongchan Kim, Soowon Son, Sangoh Kim, Hyunah Ko, Eunbeen Hong et al. (12 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31240) | [PDF](https://arxiv.org/pdf/2611.31240) | [Project Page](https://cvlab-kaist.github.io/MoOP)

<details>
<summary>Abstract</summary>

Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction. Our analysis of Taylor importance in Alpamayo-1.5-10B shows that reasoning and trajectory objectives assign different importance to the same vision-language model (VLM) structures. In the action expert, MLP channels exhibit more stable importance rankings across denoising steps than query h...

</details>

<details>
<summary>Share</summary>

```
Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action

Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs.

arXiv: https://arxiv.org/abs/2611.31240
Project page: https://cvlab-kaist.github.io/MoOP

#VLA #robotics
```

</details>

---

### [WorldLeague: Benchmarking Physical Agency](https://arxiv.org/abs/2611.30989)

**Authors:** Xinyang Zhou, Qi Li, Xinchao Wang

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30989) | [PDF](https://arxiv.org/pdf/2611.30989) | [Project Page](https://xyangzhou.github.io/WorldLeague)

<details>
<summary>Abstract</summary>

AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce \textbf{WorldLeague}, a benchmark that compares AI systems on a common set of \textbf{60 simulated robot tasks} by measuring progress toward each task's physical goal from the robot's trajectory. Robots explore scenes to gather evidence in \textbf{WorldSe...

</details>

<details>
<summary>Share</summary>

```
WorldLeague: Benchmarking Physical Agency

AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms.

arXiv: https://arxiv.org/abs/2611.30989
Project page: https://xyangzhou.github.io/WorldLeague

#VLA #robotics
```

</details>

---

### [JEPA-Tuner: From Predictive Fine-Tuning to Asynchronous Execution of Vision-Language-Action Models](https://arxiv.org/abs/2611.29096)

**Authors:** Jingxiang Qu, Tian Xie, Youngjin Hong, Changhyun Choi, Yang Katie Zhao et al. (6 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29096) | [PDF](https://arxiv.org/pdf/2611.29096) | [Project Page](https://qujx.github.io/JEPA-Tuner-Website)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generate sequences of actions from visual observations, proprioceptive states, and language instructions. In embodied interaction, executing these actions influences subsequent observations and robot states, providing a natural predictive signal for policy learning. However, standard action-supervised fine-tuning does not explicitly capture these action-conditioned temporal dependencies in the guidance consumed by the action predictor. We introduce JEPA-Tuner, a predictive fine-tuning framework that regularizes the VLA's native policy guidance through action...

</details>

<details>
<summary>Share</summary>

```
JEPA-Tuner: From Predictive Fine-Tuning to Asynchronous Execution of Vision-Language-Action Models

Vision-Language-Action (VLA) models generate sequences of actions from visual observations, proprioceptive states, and language instructions.

arXiv: https://arxiv.org/abs/2611.29096
Project page: https://qujx.github.io/JEPA-Tuner-Website

#VLA #robotics
```

</details>

---

### [TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action](https://arxiv.org/abs/2611.26405)

**Authors:** Weile Li, Yunfan Lou, Muqing Shi, Zihao Zhang, Zhenbiao Huang et al. (8 authors)

**Published:** 2026-11-19 (updated 2026-11-21) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26405) | [PDF](https://arxiv.org/pdf/2611.26405) | [Project Page](https://tacinno.github.io)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich manipulation. However, adding tactile input yields inconsistent gains, and some visuo-tactile VLA models rely little on tactile input, because much of the tactile change, such as the gel deformation during gripper closure, is predictable from visual observations and executed actions. To address this problem, we introduce TacInno, which isolates the contact dynamics that vision and executed actions cannot explain, termed tactile innovation, and uses tac...

</details>

<details>
<summary>Share</summary>

```
TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action

Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.26405
Project page: https://tacinno.github.io

#VLA #robotics
```

</details>

---

### [Towards Pose-Robust Few-Shot Vision-Language-Action Models](https://arxiv.org/abs/2611.24360)

**Authors:** Wenhao Li, Zhongyi Han, Yuhao Wei, Liang Han, Yilong Yin et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24360) | [PDF](https://arxiv.org/pdf/2611.24360) | [Project Page](https://peacelwh.github.io/WACO/)

<details>
<summary>Abstract</summary>

Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-docked a few centimetres away makes it reach for the wrong place. We show that both failures are one phenomenon, a change of the camera-to-base extrinsic that the policy has memorised, and that the robot carries everything needed to undo it. We introduce WACO, a world-anchored canonicalization framew...

</details>

<details>
<summary>Share</summary>

```
Towards Pose-Robust Few-Shot Vision-Language-Action Models

Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base...

arXiv: https://arxiv.org/abs/2611.24360
Project page: https://peacelwh.github.io/WACO/

#VLA #robotics
```

</details>

---

### [AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation](https://arxiv.org/abs/2611.24077)

**Authors:** Shiwei Wu, Yuwen Pan, Zhi Li, Yaowen Li, Yan Zhou et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24077) | [PDF](https://arxiv.org/pdf/2611.24077) | [Project Page](https://starsholic.github.io/AeroRSI/) | [Code](https://github.com/starsholic/AeroRSI)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight. Correcting these failures requires repairs, i.e., actions that avoid them at the states the policy itself reaches, which human pilots cannot label at scale and rule-based planners cannot supply reliably. In this paper, we present AeroRSI, a recursive self-improvement framework in which an aerial navigation policy iteratively learns from its own failures. Our key insight is that a failing policy should judge its own repairs by flyin...

</details>

<details>
<summary>Share</summary>

```
AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight.

arXiv: https://arxiv.org/abs/2611.24077
Project page: https://starsholic.github.io/AeroRSI/
Code: https://github.com/starsholic/AeroRSI

#VLA #robotics
```

</details>

---

### [Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models](https://arxiv.org/abs/2611.31452)

**Authors:** Guangting Zheng, Shaoxuan Wang, Yu Yuan, Zhipeng Tang, Jiajun Deng et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31452) | [PDF](https://arxiv.org/pdf/2611.31452) | [Project Page](https://tom-zgt.github.io/MFM-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models effectively learn action policies from robot demonstrations, but struggle to generalize to changes in object positions and task goals. General multimodal foundation models (MFMs) offer complementary scene understanding and spatial reasoning, but remain slow and unreliable for direct fine-grained control. To understand how MFMs can improve VLA spatial generalization, we conduct a systematic capability analysis across multiple VLA architectures using atomic-stage interventions, revealing that many failures stem from poor target grounding and global spatial rou...

</details>

<details>
<summary>Share</summary>

```
Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models

Vision-Language-Action (VLA) models effectively learn action policies from robot demonstrations, but struggle to generalize to changes in object positions and task goals.

arXiv: https://arxiv.org/abs/2611.31452
Project page: https://tom-zgt.github.io/MFM-VLA

#VLA #robotics
```

</details>

---

### [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](https://arxiv.org/abs/2611.32665)

**Authors:** Sichen Wu, Qian Sun, Mengfan Liu, Weikai Qin, Bike Zhu et al. (6 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.32665) | [PDF](https://arxiv.org/pdf/2611.32665)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination. Existing hierarchical humanoid VLAs typically decouple motion generation from physical execution, leaving tracking and balance errors unable to directly optimize the VLA generator. We propose DiffGR00T, an end-to-end differentiable training framework that couples GR00T N1.7 with SONIC, a pretrained whole-body behavior foundation model. To enable execution-aware differentiable training, we replace...

</details>

<details>
<summary>Share</summary>

```
DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models

Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination.

arXiv: https://arxiv.org/abs/2611.32665

#VLA #robotics
```

</details>

---

### [LeanWAM: Learning Latent World Action Models from Frozen Video Models](https://arxiv.org/abs/2611.31740)

**Authors:** Shaolong Li, Hongze Fu, Joyce Chai, Yinpei Dai

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31740) | [PDF](https://arxiv.org/pdf/2611.31740) | [Project Page](https://shaolonl-16.github.io/leanwam/)

<details>
<summary>Abstract</summary>

World action models (WAMs) typically adapt large pretrained video generators to jointly predict future observations and robot actions, incurring substantial training and deployment costs. However, it remains unclear which future representations a policy actually needs and how compactly they can be represented. Our probing study shows that complementary future representations can be compressed into a few tokens while retaining most of their action-decoding performance. Motivated by this finding, we introduce LeanWAM, a latent WAM that transfers video priors from a frozen video generator to a li...

</details>

<details>
<summary>Share</summary>

```
LeanWAM: Learning Latent World Action Models from Frozen Video Models

World action models (WAMs) typically adapt large pretrained video generators to jointly predict future observations and robot actions, incurring substantial training and deployment costs.

arXiv: https://arxiv.org/abs/2611.31740
Project page: https://shaolonl-16.github.io/leanwam/

#VLA #robotics
```

</details>

---

### [What Does a Skill Vocabulary Cost? A Closed-Loop Decomposition over Demonstrated Motions](https://arxiv.org/abs/2611.32858)

**Authors:** Maximilian Xiling Li, Nils Blank, Paul Mattes, Pankhuri Vanjani, Rudolf Lioutikov

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32858) | [PDF](https://arxiv.org/pdf/2611.32858) | [Project Page](https://intuitive-robots.github.io/mpq)

<details>
<summary>Abstract</summary>

Discrete skill policies execute motions drawn from a finite vocabulary. In most current methods, this vocabulary is a latent codebook learned jointly with a selector and a decoder. When such a policy fails in closed loop, the failure cannot be traced to the vocabulary, to the choice of skill or to its execution. We present Movement Prototype Quantization (MPQ), which places a library of demonstrated motions after a trained policy instead of inside it. MPQ replaces each predicted action chunk with its nearest library element, corrects that element toward the prediction within a bound, and train...

</details>

<details>
<summary>Share</summary>

```
What Does a Skill Vocabulary Cost? A Closed-Loop Decomposition over Demonstrated Motions

Discrete skill policies execute motions drawn from a finite vocabulary.

arXiv: https://arxiv.org/abs/2611.32858
Project page: https://intuitive-robots.github.io/mpq

#VLA #robotics
```

</details>

---

### [RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation](https://arxiv.org/abs/2611.32016)

**Authors:** Liyang Li, Mingyu Liu, Xiaoman Li, Zhiyue Zhao, Jin-Chuan Shi et al. (11 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32016) | [PDF](https://arxiv.org/pdf/2611.32016) | [Project Page](https://aim-uofa.github.io/RoboHarness-RL/)

<details>
<summary>Abstract</summary>

Agentic harnesses enable frontier vision-language models (VLMs) to manipulate robots through perception, planning, and control tools, yet achieving comparable performance with compact open-weight VLMs remains challenging. We present RoboHarness-RL, an agentic reinforcement learning framework for improving VLM-based robot manipulation through tool calls. Starting from supervised fine-tuning on successful teacher demonstrations, the VLM further improves through multi-turn reinforcement learning with task-outcome rewards, without relying on vision-language-action models or world action models. To...

</details>

<details>
<summary>Share</summary>

```
RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation

Agentic harnesses enable frontier vision-language models (VLMs) to manipulate robots through perception, planning, and control tools, yet achieving comparable performance with compact open-weight VLMs remains challeng...

arXiv: https://arxiv.org/abs/2611.32016
Project page: https://aim-uofa.github.io/RoboHarness-RL/

#VLA #robotics
```

</details>

---

### [WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2611.31126)

**Authors:** Zien Wang, Yuhao Pan, Yunfeng Fan, Nan Cheng, Xin Xia et al. (6 authors)

**Published:** 2026-11-23 (updated 2026-11-24) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31126) | [PDF](https://arxiv.org/pdf/2611.31126)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models leverage pretrained vision-language representations for instruction-conditioned robot control, yet their understanding of task-relevant 3D relations and how these relations evolve during manipulation remains largely implicit. To address this challenge, we introduce WeaveVLA, a framework that enhances VLA action generation by explicitly modeling task-relevant relative 3D relations and maintaining relational context across observations. WeaveVLA employs a task-conditioned sparse graph neural network to encode relative 3D relations among objects, the gripper, a...

</details>

<details>
<summary>Share</summary>

```
WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models

Vision-language-action (VLA) models leverage pretrained vision-language representations for instruction-conditioned robot control, yet their understanding of task-relevant 3D relations and how these relations evolve d...

arXiv: https://arxiv.org/abs/2611.31126

#VLA #robotics
```

</details>

---

### [GeoMerge-OPD: Balanced Skill Integration in Vision-Language-Action Models](https://arxiv.org/abs/2611.30632)

**Authors:** Le Yang, Haoyang Lyu, Honglei Jin, Wenshuo Chen, Jiawei Liang et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30632) | [PDF](https://arxiv.org/pdf/2611.30632)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models excel at individual robotic skills, yet integrating heterogeneous skills into a single policy remains a key challenge for general-purpose robotic control, especially in whole-body tasks with differing manipulation and locomotion requirements. Common multi-skill integration strategies, such as joint fine-tuning and parameter merging, can induce unintended actions during closed-loop execution, severely degrading individual skills. Task-conditioned analysis of expert updates reveals response energy concentrated in a few dominant directions and opposing expert r...

</details>

<details>
<summary>Share</summary>

```
GeoMerge-OPD: Balanced Skill Integration in Vision-Language-Action Models

Vision-language-action (VLA) models excel at individual robotic skills, yet integrating heterogeneous skills into a single policy remains a key challenge for general-purpose robotic control, especially in whole-body t...

arXiv: https://arxiv.org/abs/2611.30632

#VLA #robotics
```

</details>

---

### [DelayOPSD: On-Policy Self-Distillation from a Synchronous Teacher for Real-time Asynchronous Policies](https://arxiv.org/abs/2611.30534)

**Authors:** Hyeonjae Kim, Jeongsol Kim, Sunwoo Park, Chanyu Moon, Yoojin Oh et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30534) | [PDF](https://arxiv.org/pdf/2611.30534) | [Code](https://github.com/present091/DelayOPSD)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) policies incur substantial inference latency due to their large vision-language backbones and iterative denoising. Asynchronous execution reduces this latency by generating the next action chunk while executing the current one, but the new chunk is conditioned on a stale observation, degrading performance as the delay increases. We investigate this mismatch by comparing actions predicted from observations at planning and execution times. We find that these predictions differ little on expert demonstrations but diverge substantially on the policy's own de...

</details>

<details>
<summary>Share</summary>

```
DelayOPSD: On-Policy Self-Distillation from a Synchronous Teacher for Real-time Asynchronous Policies

Flow-based vision-language-action (VLA) policies incur substantial inference latency due to their large vision-language backbones and iterative denoising.

arXiv: https://arxiv.org/abs/2611.30534
Code: https://github.com/present091/DelayOPSD

#VLA #robotics
```

</details>

---

### [OVOGO: Offline Value-Guided On-Policy Generative Optimization for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2611.30477)

**Authors:** Rongzheng Yang, Jiaming Guo, Yuxuan Guo, Zihao Zhang, Yunkai Gao et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30477) | [PDF](https://arxiv.org/pdf/2611.30477)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action models can benefit from robot experience collected during deployment, but repeatedly acquiring new physical interactions for policy improvement is costly. Offline reinforcement learning provides a natural way to reuse collected experience, while flow-based policies offer an additional opportunity because fresh generation trajectories can be cheaply resampled from the current policy at replay observations. This motivates separating offline value learning from on-policy optimization of the generative process. We propose OVOGO, an offline reinforcement learning f...

</details>

<details>
<summary>Share</summary>

```
OVOGO: Offline Value-Guided On-Policy Generative Optimization for Flow-Based Vision-Language-Action Models

Flow-based vision-language-action models can benefit from robot experience collected during deployment, but repeatedly acquiring new physical interactions for policy improvement is costly.

arXiv: https://arxiv.org/abs/2611.30477

#VLA #robotics
```

</details>

---

### [ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models](https://arxiv.org/abs/2611.30308)

**Authors:** Yunhe Zhang, Long Gao, Yuedong Fu, Gang He, Li Xu et al. (8 authors)

**Published:** 2026-11-23 (updated 2026-11-24) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30308) | [PDF](https://arxiv.org/pdf/2611.30308)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation. Although multi-view observations provide complementary scene information, VLMs model cross-view interactions based on 2D feature similarity, which can lead to physical inconsistency in the form of cross-view incorrect association between distinct entities and cross-view information fragmentation about the same entity. To address these challenges, we propose ConsisX, a novel VLA framework that integrates cross-view associa...

</details>

<details>
<summary>Share</summary>

```
ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models

Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation.

arXiv: https://arxiv.org/abs/2611.30308

#VLA #robotics
```

</details>

---

### [Beyond Which: Where, How, and When in Vision-Language-Action Models](https://arxiv.org/abs/2611.30291)

**Authors:** Yunhe Zhang, Long Gao, Yuedong Fu, Gang He, Li Xu et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30291) | [PDF](https://arxiv.org/pdf/2611.30291)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization across diverse robotic manipulation tasks. Although VLM features can identify which entities are relevant to action prediction, precise manipulation also requires understanding where task-relevant entities are located within the spatial layout, how their geometric structure constrains physical interaction, and when spatial or geometric information should make a greater contribution to action prediction. To this end, we...

</details>

<details>
<summary>Share</summary>

```
Beyond Which: Where, How, and When in Vision-Language-Action Models

Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization across diverse robotic manipulation tasks.

arXiv: https://arxiv.org/abs/2611.30291

#VLA #robotics
```

</details>

---

### [RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2611.30145)

**Authors:** Yiheng Du, Jingqi Tian, Xu Jiang, Jiexuan Zhang, Shuyu Wang et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30145) | [PDF](https://arxiv.org/pdf/2611.30145)

<details>
<summary>Abstract</summary>

Long-horizon, history-dependent robotic manipulation often requires acting on visual cues that have disappeared, such as an object indicated earlier or a target hidden under a moving cup. The key challenge is to maintain what past evidence means for the next action as the scene changes. We introduce Recurrent Memory Reasoning (RMR), an explicit reasoning step that connects memory to action inside a vision-language-action model (VLA), with no external reasoning model. At each update, the VLA first infers an event from visual evidence, then revises the task state and grounds a subgoal in the cur...

</details>

<details>
<summary>Share</summary>

```
RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models

Long-horizon, history-dependent robotic manipulation often requires acting on visual cues that have disappeared, such as an object indicated earlier or a target hidden under a moving cup.

arXiv: https://arxiv.org/abs/2611.30145

#VLA #robotics
```

</details>

---

### [FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator](https://arxiv.org/abs/2611.31577)

**Authors:** Wenkang Hu, Haoran Wang, Liu Liu, Wenchao Huang, Yiji Chen et al. (14 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.31577) | [PDF](https://arxiv.org/pdf/2611.31577) | [Project Page](https://fabricbench.github.io/)

<details>
<summary>Abstract</summary>

Fabric manipulation challenges robot policies with changing geometry, self-occlusion, and contact, yet standardized evaluation remains focused on rigid objects. We introduce FabricBench, a benchmark for bimanual fabric manipulation with six tasks spanning garments, silk, and bags, 10,000 simulation-ready assets, and controlled tests of configuration and appearance generalization. Built on an open-source solver in Newton, our simulator enables stable bimanual grasping, holding, and release through contact forces, without artificial attachment. Redesigned cloth-rigid contact and bidirectional fo...

</details>

<details>
<summary>Share</summary>

```
FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator

Fabric manipulation challenges robot policies with changing geometry, self-occlusion, and contact, yet standardized evaluation remains focused on rigid objects.

arXiv: https://arxiv.org/abs/2611.31577
Project page: https://fabricbench.github.io/

#VLA #robotics
```

</details>

---

### [RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)

**Authors:** Yunbei Zhang, Zijian Jin, Shuaicheng Niu, Baian Chen, Weirui Ye et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30209) | [PDF](https://arxiv.org/pdf/2611.30209) | [Project Page](https://RoboAda.github.io/)

<details>
<summary>Abstract</summary>

Pretrained robot policies decide what to do from camera images, yet some of the physics that decides whether their plans succeed is not visible. An object may look light but be 100 times heavier, and a weakened joint or a lagging controller leaves no trace in the image. When the physics at deployment differs from training, the plan is often still right but is executed as if nothing had changed. Training on such variations in advance cannot handle unseen changes, while adapting once deployed either changes the plan, leaving the miscalibrated commands in place, or updates a robot model by gradie...

</details>

<details>
<summary>Share</summary>

```
RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See

Pretrained robot policies decide what to do from camera images, yet some of the physics that decides whether their plans succeed is not visible.

arXiv: https://arxiv.org/abs/2611.30209
Project page: https://RoboAda.github.io/

#VLA #robotics
```

</details>

---

### [RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)

**Authors:** Yunbei Zhang, Zijian Jin, Janet Wang, Xingchen Zhao, Zhenyu Zhang et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30111) | [PDF](https://arxiv.org/pdf/2611.30111) | [Project Page](https://robo-think.github.io/)

<details>
<summary>Abstract</summary>

Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong. Existing systems either hand the agent control, which takes minutes per episode, or let it send instructions. Yet a policy follows a new instruction only from a fresh start, since a half-finished task leaves it in states outside its training data. Nor can an instruction fix how the robot moves. If a drift keeps pulling the hand to the left, "push right, slightly" is not a task the policy has learned. We propose RoboThink, in which the agent thinks and t...

</details>

<details>
<summary>Share</summary>

```
RoboThink: Let the Agent Think, Let the Policy Act

Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong.

arXiv: https://arxiv.org/abs/2611.30111
Project page: https://robo-think.github.io/

#VLA #robotics
```

</details>

---

### [$ζ_0$: A Framework for World Action Models with Joint Scene and Body Foresight in Humanoid Control](https://arxiv.org/abs/2611.29277)

**Authors:** Yizhi Chen, Zhanxiang Cao, Yitong Wang, Junyu Liu, Hongchu Zeng et al. (22 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29277) | [PDF](https://arxiv.org/pdf/2611.29277) | [Project Page](https://chenyizhi123.github.io/zeta0-project/) | [Code](https://github.com/chenyizhi123/Zeta0)

<details>
<summary>Abstract</summary>

World Action Models anticipate visual outcomes to guide robot actions, yet humanoid interaction also depends on how the robot's body responds. Visual foresight alone can miss body motion, while latent-distance losses do not directly supervise action responses. We present $ζ_0$, a framework that turns vision-language-action policies into World Action Models by foreseeing future visual features and measured joint trajectories in a shared latent representation. During training, a teacher conditioned on recorded futures provides a reference action response, and dual-response transfer trains the ca...

</details>

<details>
<summary>Share</summary>

```
$ζ_0$: A Framework for World Action Models with Joint Scene and Body Foresight in Humanoid Control

World Action Models anticipate visual outcomes to guide robot actions, yet humanoid interaction also depends on how the robot's body responds.

arXiv: https://arxiv.org/abs/2611.29277
Project page: https://chenyizhi123.github.io/zeta0-project/
Code: https://github.com/chenyizhi123/Zeta0

#VLA #robotics
```

</details>

---

### [FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing](https://arxiv.org/abs/2611.26744)

**Authors:** Junde Li, Wei-Han Yu, Xiangyi Chu, Yaoxin Li, Jiawei Xu et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26744) | [PDF](https://arxiv.org/pdf/2611.26744) | [Code](https://github.com/Jordanlllll/FORTH)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are widely credited with force control, operating on the unverified assumption that proxy loss minimization implies physical force grounding. In this work, we demonstrate that this assumption breaks down at three core deployment levels: frozen visual backbones discard contact geometry, downstream losses mask token-level gradient alignment, and discrete indicators trigger optimization collapse. To address these disconnections, we present FORTH, a forward-only measurement harness and execution framework that explicitly pairs the optimization objective at eac...

</details>

<details>
<summary>Share</summary>

```
FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing

Vision-Language-Action (VLA) policies are widely credited with force control, operating on the unverified assumption that proxy loss minimization implies physical force grounding.

arXiv: https://arxiv.org/abs/2611.26744
Code: https://github.com/Jordanlllll/FORTH

#VLA #robotics
```

</details>

---

### [FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving](https://arxiv.org/abs/2611.26242)

**Authors:** Changtao Zhao, Yingxue Guan, Li Wang, Shijie Zhao, Yuhang Zhang et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26242) | [PDF](https://arxiv.org/pdf/2611.26242) | [Code](https://github.com/ADEPT-ORG/FastRoverVLA)

<details>
<summary>Abstract</summary>

Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference. Reusing a prediction reduces this demand while leaving its commands exposed to changes in vehicle motion. FastRoverVLA addresses this mismatch by decoupling visual plan generation from motion-conditioned execution. Its training-free interface maintains decoded plans between visual predictions. A speed-curvature action buffer is aligned with measured motion at each update, integrated into a local trajectory, and advanced by consumin...

</details>

<details>
<summary>Share</summary>

```
FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving

Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference.

arXiv: https://arxiv.org/abs/2611.26242
Code: https://github.com/ADEPT-ORG/FastRoverVLA

#VLA #robotics
```

</details>

---

### [$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling](https://arxiv.org/abs/2611.24940)

**Authors:** Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong et al. (15 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24940) | [PDF](https://arxiv.org/pdf/2611.24940) | [Project Page](https://junjieye.com/Z-sight/)

<details>
<summary>Abstract</summary>

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight instead predicts the future directly in the visual token space in which its VLM perceives the present. C...

</details>

<details>
<summary>Share</summary>

```
$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling.

arXiv: https://arxiv.org/abs/2611.24940
Project page: https://junjieye.com/Z-sight/

#VLA #robotics
```

</details>

---

### [Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs](https://arxiv.org/abs/2611.32705)

**Authors:** Dan Zlotnikov, Nadav Alali, Ohad Ben-Shahar

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.32705) | [PDF](https://arxiv.org/pdf/2611.32705)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) enable simultaneous processing of egocentric video and textual target descriptions to produce action commands for embodied tracking platforms. However, these platforms rarely move exactly as commanded, in part due to unexpected environmental disturbances such as wind, unleveled terrain, and road bumps. Here we study how such models handle uncommanded egomotion. First, we explore performance across diverse disturbances by benchmarking three tracking VLAs on three datasets. We find that models differ in which environmental disturbances hurt them most, but all...

</details>

<details>
<summary>Share</summary>

```
Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs

Vision-Language-Action models (VLAs) enable simultaneous processing of egocentric video and textual target descriptions to produce action commands for embodied tracking platforms.

arXiv: https://arxiv.org/abs/2611.32705

#VLA #robotics
```

</details>

---

### [Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations](https://arxiv.org/abs/2611.32353)

**Authors:** Ziang Ren, Zifan Wang, Zhuoyang Li, Benhao Qin, Haoyang Li et al. (11 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32353) | [PDF](https://arxiv.org/pdf/2611.32353) | [Project Page](https://any2act.github.io/)

<details>
<summary>Abstract</summary>

Robot in-context learning (ICL) enables a policy to perform unseen tasks by following contextual demonstrations, without task-specific fine-tuning. This is increasingly valuable as large language models reasoning at low frequency can specify tasks through demonstrations and delegate high-frequency execution to such a policy. However, methods conditioned on human videos are bounded by scarce human-robot pairs, while those conditioned on robot demonstrations accept only one or two source types at limited scale. We present Any2Act, a foundation model for robot ICL. Our key insight is that a demon...

</details>

<details>
<summary>Share</summary>

```
Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations

Robot in-context learning (ICL) enables a policy to perform unseen tasks by following contextual demonstrations, without task-specific fine-tuning.

arXiv: https://arxiv.org/abs/2611.32353
Project page: https://any2act.github.io/

#VLA #robotics
```

</details>

---

### [VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation](https://arxiv.org/abs/2611.32245)

**Authors:** Jiajie Zhang, Yankai Xiang, Changhao Chen

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32245) | [PDF](https://arxiv.org/pdf/2611.32245)

<details>
<summary>Abstract</summary>

Composing frozen Vision-Language-Action (VLA) skills under an agentic planner promises scalable long-horizon manipulation without long-horizon demonstrations, yet strong atomic skills routinely fail at seams even under a correct plan. Standard remedies reset the robot's pose or draft entry conditions in language, missing the physical cause we uncover via causal interventions: even after re-homing, a frozen VLA rigidly retraces its habitual trajectory and collides with displaced scene residue, whether or not it can see it. We propose the Skill Envelope, a policy-measured 3D geometric preconditi...

</details>

<details>
<summary>Share</summary>

```
VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation

Composing frozen Vision-Language-Action (VLA) skills under an agentic planner promises scalable long-horizon manipulation without long-horizon demonstrations, yet strong atomic skills routinely fail at seams even unde...

arXiv: https://arxiv.org/abs/2611.32245

#VLA #robotics
```

</details>

---

### [Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning](https://arxiv.org/abs/2611.31903)

**Authors:** Ziyang Chen, Dehua Chen, Shaoguang Wang, Xu Yan, Hao Huang et al. (6 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31903) | [PDF](https://arxiv.org/pdf/2611.31903)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models need to continually acquire new manipulation skills while retaining the ability to follow previously learned instructions. Experience replay (ER) can mitigate catastrophic forgetting, but retaining only a small number of historical expert frames per task leaves many old-instruction responses without direct supervision. Under limited replay, we observe a structured failure mode in which an earlier instruction can trigger a subsequently learned, competing goal. To address this gap, we propose Cross-Instruction Anchoring (XIA), which supplements expert replay w...

</details>

<details>
<summary>Share</summary>

```
Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning

Vision-language-action (VLA) models need to continually acquire new manipulation skills while retaining the ability to follow previously learned instructions.

arXiv: https://arxiv.org/abs/2611.31903

#VLA #robotics
```

</details>

---

### [ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning](https://arxiv.org/abs/2611.32639)

**Authors:** Haoyuan Li, Wei Huang, Jiehong Lin, Shengrong Zhang, Chenzhi Liu et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.32639) | [PDF](https://arxiv.org/pdf/2611.32639) | [Project Page](https://refocus-robotics.github.io)

<details>
<summary>Abstract</summary>

Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encounter bottlenecks. Moreover, repeated full-task rollouts also leave these bottlenecks weakly analyzed and insufficiently practiced. To this end, we introduce ReFocus, a progress-guided multi-round RL framework that alternates between Global and Local RL to identify task-specific bottlenecks and allocate additional practice to them. Specifically, during...

</details>

<details>
<summary>Share</summary>

```
ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning

Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction.

arXiv: https://arxiv.org/abs/2611.32639
Project page: https://refocus-robotics.github.io

#VLA #robotics
```

</details>

---

### [NoveltyGate: Novelty, Not Error, Decides Which VLA Prefix Tokens to Compute Exactly](https://arxiv.org/abs/2611.31099)

**Authors:** Lemeng Qi

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31099) | [PDF](https://arxiv.org/pdf/2611.31099)

<details>
<summary>Abstract</summary>

Flow-matching vision-language-action (VLA) models such as $π_{0.5}$ re-encode the camera images and the instruction with a 2B-parameter backbone at every control step, and the feed-forward layers of this prefix account for most of its compute. A natural way to save this compute is to send most tokens through a low-rank MLP and compute exactly only the tokens whose approximation error is large. We find that this intuition is wrong. Even a verifier that knows every token's exact error picks the wrong tokens, producing 1.3--1.7$\times$ larger action deviation than a simple test of whether a token...

</details>

<details>
<summary>Share</summary>

```
NoveltyGate: Novelty, Not Error, Decides Which VLA Prefix Tokens to Compute Exactly

Flow-matching vision-language-action (VLA) models such as $π_{0.5}$ re-encode the camera images and the instruction with a 2B-parameter backbone at every control step, and the feed-forward layers of this prefix accoun...

arXiv: https://arxiv.org/abs/2611.31099

#VLA #robotics
```

</details>

---

### [SWEEP-Bench: Do Embodied Policies Act on the Speed They See?](https://arxiv.org/abs/2611.30637)

**Authors:** Hiroaki Honda, Koya Sakamoto, Shu Morikuni, Yusuke Iwasawa, Taiki Miyanishi

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30637) | [PDF](https://arxiv.org/pdf/2611.30637) | [Project Page](https://damin3927.github.io/SWEEP-Bench)

<details>
<summary>Abstract</summary>

Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds. We introduce SWEEP-Bench, a simulation benchmark with 80 conveyor-belt manipulation tasks spanning 16 skill categories, each evaluated at 13 belt speeds (0.10-0.40 m/s). Objects are transported through physical contact with a visibly moving belt. Each task has a static counterpart, and each evaluation episode uses the same randomized scene at all 13 speeds. We fine-tune eight vision-language-action and world-action models on demonstrations spanning the...

</details>

<details>
<summary>Share</summary>

```
SWEEP-Bench: Do Embodied Policies Act on the Speed They See?

Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds.

arXiv: https://arxiv.org/abs/2611.30637
Project page: https://damin3927.github.io/SWEEP-Bench

#VLA #robotics
```

</details>

---

### [Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models](https://arxiv.org/abs/2611.29813)

**Authors:** Aditya Makineni, Amitesh Sahoo, Qing Tian

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29813) | [PDF](https://arxiv.org/pdf/2611.29813)

<details>
<summary>Abstract</summary>

Real-time onboard robot control calls for a lightweight vision-language-action (VLA) model, yet shrinking the backbone leaves less capacity for deliberation at inference time. Chain-of-thought decoding, dual-system architectures, and larger backbones can restore deliberation but reintroduce the latency and memory costs that motivated going small. Recurrent action heads offer a lighter alternative by iterating in latent space before committing to an action, but existing designs refine a single undifferentiated state that must simultaneously encode slowly evolving task context and rapidly changi...

</details>

<details>
<summary>Share</summary>

```
Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models

Real-time onboard robot control calls for a lightweight vision-language-action (VLA) model, yet shrinking the backbone leaves less capacity for deliberation at inference time.

arXiv: https://arxiv.org/abs/2611.29813

#VLA #robotics
```

</details>

---

### [A2I-VLA: A Two-Stage Vision-Language-Action model with Semantic-Physical Alignment and Integration](https://arxiv.org/abs/2611.29279)

**Authors:** Kun Dai, Tianqi Wang, Haibo Lei, Chaoyang Li, Kai Zhang et al. (11 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29279) | [PDF](https://arxiv.org/pdf/2611.29279)

<details>
<summary>Abstract</summary>

Force and tactile feedback provide essential information about physical interactions in contact-rich manipulation that visual observations alone cannot reliably capture.However, integrating these signals into vision-language-action (VLA) models remains challenging owing to the representational gap between visual-language semantics and physical measurements.To address this challenge, we propose A2I-VLA, a two-stage VLA framework that first learns semantically Aligned force-tactile representations and then Integrates them into a VLA model.In Stage I, a cross-modal alignment loss is introduced to...

</details>

<details>
<summary>Share</summary>

```
A2I-VLA: A Two-Stage Vision-Language-Action model with Semantic-Physical Alignment and Integration

Force and tactile feedback provide essential information about physical interactions in contact-rich manipulation that visual observations alone cannot reliably capture.However, integrating these signals into vision-l...

arXiv: https://arxiv.org/abs/2611.29279

#VLA #robotics
```

</details>

---

### [Spatially Grounded Latent Lookahead for Vision-Language-Action Models](https://arxiv.org/abs/2611.28839)

**Authors:** Qihang Chen, Tengjie Li, Hongwei Lu, Jason Wu, Chyna Qu et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28839) | [PDF](https://arxiv.org/pdf/2611.28839)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models benefit from strong semantic representations that support object recognition and instruction understanding. However, precise manipulation also depends on resolving object locations and workspace relations, and on selecting actions with an estimate of how the scene will evolve. Existing geometry-aware methods make the current scene more explicit, while predictive methods model future observations or representations. Yet future information is often neither grounded in a control-relevant spatial state nor directly used to guide action generation. We introduce S...

</details>

<details>
<summary>Share</summary>

```
Spatially Grounded Latent Lookahead for Vision-Language-Action Models

Vision-language-action (VLA) models benefit from strong semantic representations that support object recognition and instruction understanding.

arXiv: https://arxiv.org/abs/2611.28839

#VLA #robotics
```

</details>

---

### [AlpaSafe: Risk-Aware Trajectory Selection for Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2611.28509)

**Authors:** Qiren Wang, Mingyu Guo, Weisong Shi

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.28509) | [PDF](https://arxiv.org/pdf/2611.28509)

<details>
<summary>Abstract</summary>

Reasoning-based driving vision-language-action (VLA) models propose multiple candidate trajectories at each decision, yet only one is executed. Standard evaluation scores the best candidate, assuming an oracle selector that deployment lacks, and leaves the risk of the executed candidate unexamined. Existing online evaluators typically close this gap with a purpose-trained scene or world model, often rolling out each candidate through it at inference time. We introduce AlpaSafe, a risk-aware trajectory selector that reuses the scene representation a frozen driving VLA computes while proposing i...

</details>

<details>
<summary>Share</summary>

```
AlpaSafe: Risk-Aware Trajectory Selection for Vision-Language-Action Models in Autonomous Driving

Reasoning-based driving vision-language-action (VLA) models propose multiple candidate trajectories at each decision, yet only one is executed.

arXiv: https://arxiv.org/abs/2611.28509

#VLA #robotics
```

</details>

---

### [Defending Vision-Language-Action Models against Transferable Attacks via Visual-Proprioceptive Consistency](https://arxiv.org/abs/2611.28346)

**Authors:** Jiahao Wang, Ming F. Li, Han Xu

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28346) | [PDF](https://arxiv.org/pdf/2611.28346)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in a wide range of robotic tasks. However, adversarial attacks in VLA models have shown strong transferability across robotic tasks, posing significant threats to robotic systems. Despite their different attack strategies, we observe that these transferable attacks share a common consequence: they disrupt the VLA model's perception towards the robot itself. Motivated by this observation, we propose a proprioception-grounded defense framework that leverages trusted proprioceptive information to detect and mitigate transfe...

</details>

<details>
<summary>Share</summary>

```
Defending Vision-Language-Action Models against Transferable Attacks via Visual-Proprioceptive Consistency

Vision-Language-Action (VLA) models have demonstrated strong capabilities in a wide range of robotic tasks.

arXiv: https://arxiv.org/abs/2611.28346

#VLA #robotics
```

</details>

---

### [Intervention-Robust VLA: Diverse Demonstrations for Robot Deployment with Safety Filters](https://arxiv.org/abs/2611.28289)

**Authors:** Tzu-Yuan Huang, Shao-Hsuan Chang, Dai-Jie Wu, Ralf Römer, Yung-Hui Li et al. (9 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.LG, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28289) | [PDF](https://arxiv.org/pdf/2611.28289)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) have shown strong potential for learning complex robotic behaviors from demonstrations. However, learning safe behavior directly from data requires extensive coverage of safety-critical situations, which is often impractical in real-world settings. Test-time safety filters provide an alternative by correcting unsafe actions during deployment, but these interventions can drive the robot into states poorly covered by the training data, thereby degrading task performance. We introduce InteR-VLA, an intervention-robust framework for VLAs that leverages diverse...

</details>

<details>
<summary>Share</summary>

```
Intervention-Robust VLA: Diverse Demonstrations for Robot Deployment with Safety Filters

Vision-Language-Action models (VLAs) have shown strong potential for learning complex robotic behaviors from demonstrations.

arXiv: https://arxiv.org/abs/2611.28289

#VLA #robotics
```

</details>

---

### [FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models](https://arxiv.org/abs/2611.27011)

**Authors:** Shuai Peng, Yongkai Liao, Yuxin Cheng, Haoyuan Wang, Jian Huang

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.27011) | [PDF](https://arxiv.org/pdf/2611.27011)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have demonstrated strong performance in grasp-based manipulation, yet reliable recovery from local grasping failures remains challenging. Specifically, in pick-and-place tasks, policies may continue transport after a failed grasp instead of retrying, potentially reflecting overreliance on proprioceptive cues for stage progression and limited retry supervision. Existing recovery approaches typically rely on deployment-time guidance or demonstration augmentation. We introduce Force-guided Recovery (FoRe), a framework for autonomous recovery from local grasping...

</details>

<details>
<summary>Share</summary>

```
FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models

Vision-language-action (VLA) models have demonstrated strong performance in grasp-based manipulation, yet reliable recovery from local grasping failures remains challenging.

arXiv: https://arxiv.org/abs/2611.27011

#VLA #robotics
```

</details>

---

### [Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models](https://arxiv.org/abs/2611.26944)

**Authors:** Stefan de Lasa, Mohammadreza Mofayezi, Gennady Pekhimenko, Nandita Vijaykumar

**Published:** 2026-11-20 | **Categories:** cs.DC, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26944) | [PDF](https://arxiv.org/pdf/2611.26944)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control. While they enable robots to perform complex tasks in unseen environments, serving VLAs leaves hardware idle between inference passes and under-utilized during inference. Serving multiple clients at once can improve utilization, but fundamental multi-client techniques such as batching and co-execution have not been characterized for VLAs. We therefore characterize the trade-offs these known techniques impose across latency, throughput, power, and hardware utilization. Our findings inf...

</details>

<details>
<summary>Share</summary>

```
Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models

Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control.

arXiv: https://arxiv.org/abs/2611.26944

#VLA #robotics
```

</details>

---

### [RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics](https://arxiv.org/abs/2611.26969)

**Authors:** Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Amir Rasouli

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26969) | [PDF](https://arxiv.org/pdf/2611.26969) | [Project Page](https://robodyna.github.io/robodyna/)

<details>
<summary>Abstract</summary>

Object manipulation in the dynamic real world requires understanding how the environment functions and evolves, and acting accordingly. Existing benchmarks, however, do not adequately address these needs. Physics-oriented benchmarks evaluate predictive fidelity but not closed-loop action. Dynamic robotic manipulation benchmarks often use simplified, physically implausible object motions, limiting evaluation of reasoning and action under realistic dynamics. Evaluation is also typically synchronized, freezing the environment during inference and making computation time irrelevant to task outcome...

</details>

<details>
<summary>Share</summary>

```
RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics

Object manipulation in the dynamic real world requires understanding how the environment functions and evolves, and acting accordingly.

arXiv: https://arxiv.org/abs/2611.26969
Project page: https://robodyna.github.io/robodyna/

#VLA #robotics
```

</details>

---

### [Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience](https://arxiv.org/abs/2611.26420)

**Authors:** EngineAI

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26420) | [PDF](https://arxiv.org/pdf/2611.26420) | [Project Page](https://engineai-robotics.github.io/Awaken-HI)

<details>
<summary>Abstract</summary>

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with synchronized whole-body human motion and covers more than 100 skills. Building on this, we also introduce Awaken-HI (Humanoid Intelligence), a vision-language-action model for humanoid loco-manipulation that jointly predicts origi...

</details>

<details>
<summary>Share</summary>

```
Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces.

arXiv: https://arxiv.org/abs/2611.26420
Project page: https://engineai-robotics.github.io/Awaken-HI

#VLA #robotics
```

</details>

---

### [PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.26596)

**Authors:** Kai Lu, Chenyang Ma, Ioannis Havoutis

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26596) | [PDF](https://arxiv.org/pdf/2611.26596) | [Project Page](https://kl-research.github.io/pgx)

<details>
<summary>Abstract</summary>

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using p...

</details>

<details>
<summary>Share</summary>

```
PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are ti...

arXiv: https://arxiv.org/abs/2611.26596
Project page: https://kl-research.github.io/pgx

#VLA #robotics
```

</details>

---

### [PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity](https://arxiv.org/abs/2611.26565)

**Authors:** Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi et al. (11 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26565) | [PDF](https://arxiv.org/pdf/2611.26565)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. As a result, it remains unclear whether current policies truly understand physics or merely interpolate from their training data. We address this gap through the lens of dynamic extrinsic dexterity and introduce PhyDEX, a throwing benchmark in which a robot must infer an object's mass, center of mass, and frict...

</details>

<details>
<summary>Share</summary>

```
PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity

Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the...

arXiv: https://arxiv.org/abs/2611.26565

#VLA #robotics
```

</details>

---

### [Teaching Vision-Language-Action Models to Stop Safely](https://arxiv.org/abs/2611.26239)

**Authors:** Zheyuan Liu, Chuhan Wang, Jinduo Guo, Yue Huang, Xiangchi Yuan et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26239) | [PDF](https://arxiv.org/pdf/2611.26239)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to perform diverse tasks from visual observations and language instructions. While prior work has explored task suppression and refusal, stopping prohibited behavior once execution is underway and controlling the resulting physical response remain challenging. Our evaluation reveals that policies which suppress a task from its initial state can still complete it when taking over partway through execution. Even when the task remains unfinished, the robot may drop a held object, making non-completion an incomplete measure of safety. To address th...

</details>

<details>
<summary>Share</summary>

```
Teaching Vision-Language-Action Models to Stop Safely

Vision-language-action (VLA) models enable robots to perform diverse tasks from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.26239

#VLA #robotics
```

</details>

---

### [CoachSI: Self-Improvement of Robot Policies with a Language Coach](https://arxiv.org/abs/2611.25529)

**Authors:** Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25529) | [PDF](https://arxiv.org/pdf/2611.25529) | [Project Page](https://tlxhlll.github.io/CoachSI/)

<details>
<summary>Abstract</summary>

Generalist robot policies execute atomic skills reliably but fail when the same skills are composed into long-horizon tasks. Self-improvement from the policy's own experience does not close this gap: experience collected by the policy alone stays within its own distribution and reproduces what it can already do. We show that what the policy lacks is not a skill but the next step. We present CoachSI, a self-improvement method in which a frozen, off-the-shelf vision-language model (VLM) coaches the policy in language: it watches the robot and names the next step in the format of the policy's ato...

</details>

<details>
<summary>Share</summary>

```
CoachSI: Self-Improvement of Robot Policies with a Language Coach

Generalist robot policies execute atomic skills reliably but fail when the same skills are composed into long-horizon tasks.

arXiv: https://arxiv.org/abs/2611.25529
Project page: https://tlxhlll.github.io/CoachSI/

#VLA #robotics
```

</details>

---

### [Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation](https://arxiv.org/abs/2611.24247)

**Authors:** Haotian Xu, Yue Hu, Zhengqiu Zhu, Tuo Feng, Wenguan Wang et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.24247) | [PDF](https://arxiv.org/pdf/2611.24247)

<details>
<summary>Abstract</summary>

Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight. A key challenge is linking changing egocentric perception with spatial evidence anchored to stable locations for long-range navigation. We propose CityNav-VLA, a dual-frame vision-language-action model for urban navigation integrating dynamic egocentric context with persistent allocentric spatial memory. The UAV incrementally accumulates visual observations on a fixed north-up map initialized with geographic and landmark priors, preserving evidence acr...

</details>

<details>
<summary>Share</summary>

```
Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation

Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight.

arXiv: https://arxiv.org/abs/2611.24247

#VLA #robotics
```

</details>

---

### [CoRA-VTLA: Contact-Guided Attention and Queryable Response Memory for Tactile Post-Training](https://arxiv.org/abs/2611.23963)

**Authors:** Chengye Song, Rui Song, Shengqi Wang, Jiawei Zhang, Hongzhou Wang et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.23963) | [PDF](https://arxiv.org/pdf/2611.23963) | [Project Page](https://cora-vtla.github.io/)

<details>
<summary>Abstract</summary>

In precision manipulation, small errors in alignment or force can cause jamming or deformation, making contact feedback essential for adapting pretrained vision-language-action (VLA) models to these tasks. A single tactile observation leaves the response to recent actions ambiguous. Direct tactile fusion during post-training can also disperse the action expert's visual attention and reduce the share it allocates to contact regions. To address these challenges, CoRA-VTLA augments pretrained VLAs with lightweight tactile modules. A queryable action-response memory retrieves recent contact respon...

</details>

<details>
<summary>Share</summary>

```
CoRA-VTLA: Contact-Guided Attention and Queryable Response Memory for Tactile Post-Training

In precision manipulation, small errors in alignment or force can cause jamming or deformation, making contact feedback essential for adapting pretrained vision-language-action (VLA) models to these tasks.

arXiv: https://arxiv.org/abs/2611.23963
Project page: https://cora-vtla.github.io/

#VLA #robotics
```

</details>

---

### [RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models](https://arxiv.org/abs/2611.23843)

**Authors:** Apoorva Vashisth, Manav Kulshrestha, Damon Conover, Zachary Kingston, Aniket Bera

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23843) | [PDF](https://arxiv.org/pdf/2611.23843)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipulations. Instead of burdening the VLA policies with long-horizon reasoning, memory, action generation, progress tracking, and error recovery, we argue for leveraging their short-horizon manipulation capabilities within an execution-aware framework. To this end, we introduce \textnormal{\textbf{RePlan-VLA}}, a VLA-agnostic framework that translates a VLA's short-horizon capabilitie...

</details>

<details>
<summary>Share</summary>

```
RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipu...

arXiv: https://arxiv.org/abs/2611.23843

#VLA #robotics
```

</details>

---

### [ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2611.23714)

**Authors:** Keke Tang, Guolin Qiu, Tianyu Hao, Daizong Liu, Yikai Zhang et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23714) | [PDF](https://arxiv.org/pdf/2611.23714)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a powerful paradigm for robotic manipulation and show strong promise for real-world deployment, making adversarial robustness critical for reliable robot operation. Existing adversarial attacks on VLA-controlled robots mainly optimize prediction-level discrepancies or rollout-level deviations to disrupt manipulation. However, they rarely account for the fact that VLA-predicted commands are not executed directly, but must be realized through downstream control and robot embodiment. In this paper, we propose ExecGap, an adversarial patch attack fra...

</details>

<details>
<summary>Share</summary>

```
ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models

Vision-Language-Action (VLA) models have become a powerful paradigm for robotic manipulation and show strong promise for real-world deployment, making adversarial robustness critical for reliable robot operation.

arXiv: https://arxiv.org/abs/2611.23714

#VLA #robotics
```

</details>

---

### [Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need](https://arxiv.org/abs/2611.23676)

**Authors:** Artur Kuramshin, Charlotte Cloutier, Michael Przystupa, Kirsty Ellis, Mohammad S. Akhter et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23676) | [PDF](https://arxiv.org/pdf/2611.23676)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best adapt VLAs to dexterous hands by pairing supervised fine-tuning (SFT) with diffusion-steering reinforcement learning (DSRL). Using $π_{0.5}$ and a LEAP hand, we evaluate five fine-tuning recipes across two simulation tasks using only a handfu...

</details>

<details>
<summary>Share</summary>

```
Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need

Vision-Language-Action models have demonstrated strong manipulation capabilities.

arXiv: https://arxiv.org/abs/2611.23676

#VLA #robotics
```

</details>

---

### [NativeDrive: Native Multimodal Foundations for Autonomous Driving](https://arxiv.org/abs/2611.32216)

**Authors:** Zehua Fan, Qi Jiang, Wei Li, Kai Tang, Yue Jiang et al. (10 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32216) | [PDF](https://arxiv.org/pdf/2611.32216)

<details>
<summary>Abstract</summary>

Autonomous driving requires semantic understanding and fine-grained scene perception for precise action prediction. Vision-language-action models (VLAs) inherit semantic priors, but low-dimensional action labels provide limited structural supervision. Some studies extend VLAs with visual generation tasks or adopt video-based world-action models (WAMs), but both approaches introduce appearance-reconstruction overhead, which is less relevant to planning. Native multimodal models offer an alternative to unify understanding and generation within one backbone. On this basis, we propose NativeDrive,...

</details>

<details>
<summary>Share</summary>

```
NativeDrive: Native Multimodal Foundations for Autonomous Driving

Autonomous driving requires semantic understanding and fine-grained scene perception for precise action prediction.

arXiv: https://arxiv.org/abs/2611.32216

#VLA #robotics
```

</details>

---

### [Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2611.26438)

**Authors:** Zixuan Liu, Hashem Haghbayan, Zizhan Zheng, Siavash Khajavi

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26438) | [PDF](https://arxiv.org/pdf/2611.26438)

<details>
<summary>Abstract</summary>

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters. However, even when retrieved demonstrations are relevant to the current task, the VLA may fail to effectively utilize the retrieved information, ultimately leading to task failure. To address this challenge, we propose R2-VLA, a risk-controlled retrieval-augmented VLA framework that enables reliable test-time adaptation by satisfying a user-specified task success rate requirement with minimal expert assistance...

</details>

<details>
<summary>Share</summary>

```
Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters.

arXiv: https://arxiv.org/abs/2611.26438

#VLA #robotics
```

</details>

---

### [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](https://arxiv.org/abs/2611.25461)

**Authors:** Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25461) | [PDF](https://arxiv.org/pdf/2611.25461) | [Code](https://github.com/LigphiDonk/ActMem)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual...

</details>

<details>
<summary>Share</summary>

```
ActMem: From Latent Memory Reasoning to Grounded Robotic Action

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.

arXiv: https://arxiv.org/abs/2611.25461
Code: https://github.com/LigphiDonk/ActMem

#VLA #robotics
```

</details>

---

### [MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory](https://arxiv.org/abs/2611.32564)

**Authors:** Jialong Peng, Shihao Zhou, Feng Yan, Wen Xiao, Haozheng Wang et al. (11 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32564) | [PDF](https://arxiv.org/pdf/2611.32564)

<details>
<summary>Abstract</summary>

In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates. However, existing robotic ICL methods either rely on large-scale pretraining constrained by scarce, costly robot interaction data or require additional annotations yet struggle to generalize across tasks. To bridge this gap, we propose MXI-MemICL, a framework for memory-guided ICL in vision-language-action (VLA) models. By treating demonstrations as retrievable memory, MXI-MemICL enables in-context manipulation without additional large-scale pretraining or specialized anno...

</details>

<details>
<summary>Share</summary>

```
MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory

In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates.

arXiv: https://arxiv.org/abs/2611.32564

#VLA #robotics
```

</details>

---

### [KeyMemVLA: Subtask-Guided Key Memory for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2611.32081)

**Authors:** Yongwei Zhang, Tao Chen, Sicheng Ma, Yuanzhe Xing, Pengwei Zhang et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32081) | [PDF](https://arxiv.org/pdf/2611.32081)

<details>
<summary>Abstract</summary>

Memory-dependent long-horizon manipulation requires vision-language-action (VLA) policies to infer task progress and recall evidence absent from current observations. Under a limited memory budget, the challenge is to retain history that resolves stage ambiguity and supports subsequent decisions. We present KeyMemVLA, a subtask-guided key memory framework based on progress indication and decision-evidence retention. A two-level annotation process selects subtasks satisfying either criterion and labels their final frames as keyframes to supervise online memory writes. A shared vision-language b...

</details>

<details>
<summary>Share</summary>

```
KeyMemVLA: Subtask-Guided Key Memory for Long-Horizon Robotic Manipulation

Memory-dependent long-horizon manipulation requires vision-language-action (VLA) policies to infer task progress and recall evidence absent from current observations.

arXiv: https://arxiv.org/abs/2611.32081

#VLA #robotics
```

</details>

---

### [Embodied Neuro-symbolic AI: Making Robot Behavior Auditable, Safe, and Scalable](https://arxiv.org/abs/2611.31488)

**Authors:** Ruwan Wickramarachchi, Jonathan Francis, Alessandro Oltramari

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31488) | [PDF](https://arxiv.org/pdf/2611.31488)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) end-to-end systems have driven major progress in robot learning, yet they still face persistent barriers to dependable real-world deployment. In practice, these models often exhibit brittle generalization under distribution shift (i.e., novel objects, layouts, lighting, or contact conditions), limited physical and causal reasoning, and inconsistent fine-grained motor control. Critically, many VLA pipelines offer limited ways to express and audit what a robot must not do, making it difficult to provide assurance in safety-critical settings. These limitations...

</details>

<details>
<summary>Share</summary>

```
Embodied Neuro-symbolic AI: Making Robot Behavior Auditable, Safe, and Scalable

Current Vision-Language-Action (VLA) end-to-end systems have driven major progress in robot learning, yet they still face persistent barriers to dependable real-world deployment.

arXiv: https://arxiv.org/abs/2611.31488

#VLA #robotics
```

</details>

---

### [Body and Soul: Decoupling Robotic Brain and Policy with RoboHarness-Zero](https://arxiv.org/abs/2611.30550)

**Authors:** Yihao Shen, Yuxuan Chen, Xuantong Liu, Jun Gao, Weijian Luo et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30550) | [PDF](https://arxiv.org/pdf/2611.30550)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can execute individual skills but fail to complete tasks that require combining several of them. In our audit of Xiaomi-Robotics-1, an estimated 43\% of failures involve choosing the wrong target or losing track of task progress. Wrapping a frozen VLA in a vision-language model (VLM) harness is a natural remedy. Existing harnesses can gain substantially from task- and policy-specific preparation, raising the question of how much of that gain transfers to a new task or policy. An ideal harness should (i) need minimal preparation for a new task, (ii) need no...

</details>

<details>
<summary>Share</summary>

```
Body and Soul: Decoupling Robotic Brain and Policy with RoboHarness-Zero

Vision-language-action (VLA) policies can execute individual skills but fail to complete tasks that require combining several of them.

arXiv: https://arxiv.org/abs/2611.30550

#VLA #robotics
```

</details>

---

### [JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation](https://arxiv.org/abs/2611.30516)

**Authors:** Tingjun Dai, Jianxiang He, Mingfei Han, Qihao Yu, Longtao Jiang et al. (9 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30516) | [PDF](https://arxiv.org/pdf/2611.30516)

<details>
<summary>Abstract</summary>

Demonstrations show how a task can be completed, but differences in embodiment, appearance, and execution speed make it difficult to identify the guidance relevant to the robot's current progress. We introduce JEPA-ICL, a vision-language-action framework that couples predictive planning with demonstration learning. The policy learns to plan by predicting ordered future states in JEPA feature space up to subtask completion, capturing what remains to be accomplished. These plans guide action generation and locate relevant stages in demonstrations, whose JEPA-supervised content features provide p...

</details>

<details>
<summary>Share</summary>

```
JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation

Demonstrations show how a task can be completed, but differences in embodiment, appearance, and execution speed make it difficult to identify the guidance relevant to the robot's current progress.

arXiv: https://arxiv.org/abs/2611.30516

#VLA #robotics
```

</details>

---

### [MotionServe: Efficient Multi-Robot Serving by Exploiting Robot Execution Slack](https://arxiv.org/abs/2611.30083)

**Authors:** Zikang Wen, Yuning Zhang, Dong Yuan

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30083) | [PDF](https://arxiv.org/pdf/2611.30083)

<details>
<summary>Abstract</summary>

As robotic arms undertake diverse manipulation tasks, a deployment may need to serve many task-specific vision-language-action (VLA) policies concurrently. Dedicating a GPU to each robot is costly, motivating shared-GPU inference. Low-rank adaptation (LoRA) allows compatible policies to share a frozen backbone with lightweight policy-specific adapters, reducing model-weight memory and enabling cross-policy batching. However, robot inference must keep pace with physical execution. With action chunking, robots continue executing buffered actions while awaiting new predictions, and the remaining...

</details>

<details>
<summary>Share</summary>

```
MotionServe: Efficient Multi-Robot Serving by Exploiting Robot Execution Slack

As robotic arms undertake diverse manipulation tasks, a deployment may need to serve many task-specific vision-language-action (VLA) policies concurrently.

arXiv: https://arxiv.org/abs/2611.30083

#VLA #robotics
```

</details>

---

### [ProMix: Efficient Data Mixture Optimization for Robotic Imitation via Proxy-Reference DRO](https://arxiv.org/abs/2611.29873)

**Authors:** Qie Sima, Wei Xue, Yike Guo

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29873) | [PDF](https://arxiv.org/pdf/2611.29873)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel in open-world manipulation, yet their performance often saturates when training data are naively pooled across heterogeneous robots, tasks, and environments. Distributionally robust data mixture optimization, exemplified by Re-Mix, can recover much of this performance, but its weight search requires training full-scale policies twice on the entire corpus, placing it out of reach for most laboratories. We present ProMix, a compute-efficient instantiation of the proxy-reference DRO recipe for robotic imitation learning: a 15M-parameter proxy learns per-d...

</details>

<details>
<summary>Share</summary>

```
ProMix: Efficient Data Mixture Optimization for Robotic Imitation via Proxy-Reference DRO

Vision-Language-Action (VLA) models excel in open-world manipulation, yet their performance often saturates when training data are naively pooled across heterogeneous robots, tasks, and environments.

arXiv: https://arxiv.org/abs/2611.29873

#VLA #robotics
```

</details>

---

### [JKO-GRPO: Augmenting GRPO with Wasserstein Proximal Steps for Flow-Matching VLAs](https://arxiv.org/abs/2611.29646)

**Authors:** Jiyong Kwon, Yikun Bai, Amirhossein Mollaali, Guang Lin

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29646) | [PDF](https://arxiv.org/pdf/2611.29646)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models such as $π_0,π_{0.5}$ generate continuous action chunks by flow matching, and online reinforcement learning (RL) can improve them beyond supervised fine-tuning. Existing methods, such as Flow-GRPO and $π_{\mathrm{RL}}$, optimize likelihood ratios of stochastic denoising transitions, which reweight the sampled actions by their advantages but do not use the distances between them. We propose JKO-GRPO, which augments Flow-GRPO with Wasserstein proximal steps, with two contributions: (1) At each state, we treat the group of sampled actions as an empir...

</details>

<details>
<summary>Share</summary>

```
JKO-GRPO: Augmenting GRPO with Wasserstein Proximal Steps for Flow-Matching VLAs

Flow-based vision-language-action (VLA) models such as $π_0,π_{0.5}$ generate continuous action chunks by flow matching, and online reinforcement learning (RL) can improve them beyond supervised fine-tuning.

arXiv: https://arxiv.org/abs/2611.29646

#VLA #robotics
```

</details>

---

### [Detecting Is Not Choosing: What a World Model Needs to Keep a VLA Policy Safe](https://arxiv.org/abs/2611.29553)

**Authors:** Thanish Bolla

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.29553) | [PDF](https://arxiv.org/pdf/2611.29553)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies complete most benchmark tasks but often violate safety constraints. Since they are stochastic, one remedy is to sample several candidate action chunks and execute one that a world model predicts is safe. We ask what such a model must do. In simulation, a lookahead safety filter with the simulator as an exact world model raises the safety rate of three VLA policies on LIBERO and of pi0.5 on LIBERO-Plus by 11.5 to 25.7 points. It also helps pi0.5 on three RoboCasa tasks. Learned critics trained on one policy's data detect dangerous states (pooled AUROC up to...

</details>

<details>
<summary>Share</summary>

```
Detecting Is Not Choosing: What a World Model Needs to Keep a VLA Policy Safe

Vision-language-action (VLA) policies complete most benchmark tasks but often violate safety constraints.

arXiv: https://arxiv.org/abs/2611.29553

#VLA #robotics
```

</details>

---

### [MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model](https://arxiv.org/abs/2611.29501)

**Authors:** Rongze Tang, Chenyu Zhou, Jianjie Fang, Ziming Liu, Zhaolu Wang et al. (11 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29501) | [PDF](https://arxiv.org/pdf/2611.29501) | [Project Page](https://embodiedcity.github.io/MAWAM/)

<details>
<summary>Abstract</summary>

World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timing, and heterogeneous embodiments. Such coordination demands both spatiotemporal alignment of future interactions and awareness of individual embodiment and role identities, whereas existing decentralized per-robot policies, flat centralized models, and multi-robot VLAs fail to unite both. To bridge this gap, we presen...

</details>

<details>
<summary>Share</summary>

```
MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model

World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent.

arXiv: https://arxiv.org/abs/2611.29501
Project page: https://embodiedcity.github.io/MAWAM/

#VLA #robotics
```

</details>

---

### [Self-Refining VLA Sampling](https://arxiv.org/abs/2611.29383)

**Authors:** Jeff Duan, Arjun Sharma, Jennifer Cruden, Vansh Tibrewal

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29383) | [PDF](https://arxiv.org/pdf/2611.29383)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models typically use flow-based generative modeling to learn a rich, often multimodal, distribution of robot actions. Generating samples from flow-based methods involves iteratively updating random noise, and distinct noise samples from the same state can result in distinct trajectories and task outcomes. Existing test-time scaling methods improve action chunk generation via selection, aggregation, or correction, but commonly require the generation of large ensembles of candidates or the training of an external corrector. We adapt Predict-and-Perturb (P&P), a self-...

</details>

<details>
<summary>Share</summary>

```
Self-Refining VLA Sampling

Vision-Language-Action (VLA) models typically use flow-based generative modeling to learn a rich, often multimodal, distribution of robot actions.

arXiv: https://arxiv.org/abs/2611.29383

#VLA #robotics
```

</details>

---

### [LIBERO-MOR: A Multimodal Robustness Benchmark Across the Vision-Language-Action Pipeline](https://arxiv.org/abs/2611.28867)

**Authors:** Qihang Chen, Tengjie Li, Hongwei Lu, Jason Wu, Chyna Qu et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28867) | [PDF](https://arxiv.org/pdf/2611.28867)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong performance on robot manipulation benchmarks. Translating this progress into reliable deployment calls for systematic evaluation of how policies respond to variations throughout the robot interaction loop. We introduce LIBERO-MOR, a multimodal robustness benchmark across the vision-language-action pipeline. Built on standard LIBERO, it covers five deployment-facing domains: vision, language, proprioception, action execution, and environment. The benchmark comprises 22 deployment-inspired perturbations, each evaluated at three severity le...

</details>

<details>
<summary>Share</summary>

```
LIBERO-MOR: A Multimodal Robustness Benchmark Across the Vision-Language-Action Pipeline

Vision-language-action (VLA) models have achieved strong performance on robot manipulation benchmarks.

arXiv: https://arxiv.org/abs/2611.28867

#VLA #robotics
```

</details>

---

### [Probing Invisible Actuation Shifts for Test-time Calibration of Visuomotor Policies](https://arxiv.org/abs/2611.28308)

**Authors:** Jie Liu, Hui Xie, Qinfeng Feng, Joaquin Vanschoren

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28308) | [PDF](https://arxiv.org/pdf/2611.28308)

<details>
<summary>Abstract</summary>

Visuomotor policies such as vision-language-action models (VLAs) and world action models (WAMs) are increasingly deployed on robots whose cameras and controllers differ from those used to collect their training data. Such deployment introduces two kinds of shifts. Visual shifts, such as a moved camera, change the observed images; actuation shifts, such as a retuned controller, latency or an added payload, change only how commanded actions translate into robot motion. Invisible to the policy, actuation shifts sharply degrade its success, even under domain randomization. In this work, we propose...

</details>

<details>
<summary>Share</summary>

```
Probing Invisible Actuation Shifts for Test-time Calibration of Visuomotor Policies

Visuomotor policies such as vision-language-action models (VLAs) and world action models (WAMs) are increasingly deployed on robots whose cameras and controllers differ from those used to collect their training data.

arXiv: https://arxiv.org/abs/2611.28308

#VLA #robotics
```

</details>

---

### [FlowPAC: Flow-Guided Visual Pruning and Action Caching for Efficient VLA Inference](https://arxiv.org/abs/2611.28256)

**Authors:** Jintao Cheng, Yipu Zhang, Haozhe Wang, Lin Jiang, Jiang Xu et al. (6 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28256) | [PDF](https://arxiv.org/pdf/2611.28256)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied AI, yet their high inference latency and memory footprint remain major barriers to edge deployment. Existing training-free acceleration techniques, such as visual token pruning and action caching, typically rely on static resource allocation. This mismatch with dynamic robotic interactions not only degrades control performance but also causes severe hardware inefficiencies, including fragmented KV-cache layouts and wasted compute on non-critical regions. To address this, we propose FlowPAC, a locality-aware fr...

</details>

<details>
<summary>Share</summary>

```
FlowPAC: Flow-Guided Visual Pruning and Action Caching for Efficient VLA Inference

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied AI, yet their high inference latency and memory footprint remain major barriers to edge deployment.

arXiv: https://arxiv.org/abs/2611.28256

#VLA #robotics
```

</details>

---

### [GenPA: Image Generators as Efficient Robot Policies](https://arxiv.org/abs/2611.27446)

**Authors:** Zian Deng, Tianyi Zhang, Zilong Zheng, Ziyu Liu, Tao Zhang et al. (7 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27446) | [PDF](https://arxiv.org/pdf/2611.27446) | [Project Page](https://deng-zian.github.io/GenPA-website/)

<details>
<summary>Abstract</summary>

Pretrained visual generation models have shown great promise in robotic manipulation. However, a representative line of work still treats future visual prediction as the central link between visual generative pretraining and action learning, retaining it as a training objective even when future scenes are no longer generated at inference time. We argue that the instruction-following, spatial understanding, and visual imagination capabilities acquired through image generation pretraining can support control without future visual prediction: image generation models themselves can be directly ada...

</details>

<details>
<summary>Share</summary>

```
GenPA: Image Generators as Efficient Robot Policies

Pretrained visual generation models have shown great promise in robotic manipulation.

arXiv: https://arxiv.org/abs/2611.27446
Project page: https://deng-zian.github.io/GenPA-website/

#VLA #robotics
```

</details>

---

### [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444)

**Authors:** Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang et al. (43 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26444) | [PDF](https://arxiv.org/pdf/2611.26444)

<details>
<summary>Abstract</summary>

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a failure comes from reasoning, execution, or their composition. We introduce Mind2Act World, a diagnosti...

</details>

<details>
<summary>Share</summary>

```
Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and tim...

arXiv: https://arxiv.org/abs/2611.26444

#VLA #robotics
```

</details>

---

### [One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency](https://arxiv.org/abs/2611.26161)

**Authors:** Jinxi Liu, Ruifeng Zhai, Hao Liu, Guangrun Wang

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.26161) | [PDF](https://arxiv.org/pdf/2611.26161)

<details>
<summary>Abstract</summary>

Multi-view vision-language-action (VLA) models still face challenges in spatial generalization, particularly under changes in camera viewpoints and robot initial states. These models typically receive action supervision only in the robot base frame, requiring them to implicitly learn the spatial correspondence between observations from each view and base-frame actions. We propose One View, One Action (OVOA-VLA), which learns to predict actions in each view's camera frame, allowing the same physical motion to provide diverse, observation-aligned supervision across views. OVOA-VLA jointly trains...

</details>

<details>
<summary>Share</summary>

```
One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency

Multi-view vision-language-action (VLA) models still face challenges in spatial generalization, particularly under changes in camera viewpoints and robot initial states.

arXiv: https://arxiv.org/abs/2611.26161

#VLA #robotics
```

</details>

---

### [A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery](https://arxiv.org/abs/2611.25656)

**Authors:** Chenyuan Zhou, Chaoyi Huang, Zibo Wang, Zhiyuan Li, Yong-Lu Li

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.25656) | [PDF](https://arxiv.org/pdf/2611.25656)

<details>
<summary>Abstract</summary>

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with a VLA policy. It treats tool affordances as hypotheses the agent can construct, test, and revise. Gi...

</details>

<details>
<summary>Share</summary>

```
A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy a...

arXiv: https://arxiv.org/abs/2611.25656

#VLA #robotics
```

</details>

---

### [Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation](https://arxiv.org/abs/2611.25400)

**Authors:** Chengyang Dong, Ze Chen, Kai Ye, Chutian Wang, Heng Xu et al. (14 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.25400) | [PDF](https://arxiv.org/pdf/2611.25400)

<details>
<summary>Abstract</summary>

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining. However, backpropagation-based adaptation incurs heavy memory overhead on resource-constrained robots, whereas zeroth-order (ZO) methods suffer from high estimation variance under limited perturbation budgets. We observe that while ZO estimation enables low-memory adaptation with rapid initial gains, it often stalls or degrades over long-horizon updates due to noisy gradient estimates. To address these limitations, we propose Dune, a zeroth-or...

</details>

<details>
<summary>Share</summary>

```
Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining.

arXiv: https://arxiv.org/abs/2611.25400

#VLA #robotics
```

</details>

---

### [3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation](https://arxiv.org/abs/2611.23961)

**Authors:** Xin Zhang, Shiqi Zhang, Siyuan Cao, Juncheng Cai, Yedong Shen et al. (12 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23961) | [PDF](https://arxiv.org/pdf/2611.23961)

<details>
<summary>Abstract</summary>

In contact-rich dexterous manipulation, occlusion by the fingers and interacting objects obscures local geometry, preventing visual observations from fully capturing contact locations. Visually similar scenes may also differ subtly in the relative positions of interacting objects, leading to different contact states. We propose 3DTouch, a tactile-geometric conditioning approach for vision-language-action (VLA) models. 3DTouch constructs a shared 3D visuo-tactile representation by expressing RGB-D scene points and dense five-finger tactile measurements in the robot-base frame, preserving each t...

</details>

<details>
<summary>Share</summary>

```
3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation

In contact-rich dexterous manipulation, occlusion by the fingers and interacting objects obscures local geometry, preventing visual observations from fully capturing contact locations.

arXiv: https://arxiv.org/abs/2611.23961

#VLA #robotics
```

</details>

---

### [GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation](https://arxiv.org/abs/2611.23926)

**Authors:** Tianqi Gong, Haochen Niu, Yusheng Zhao, Lantao Zhang, Haoyu Liu et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23926) | [PDF](https://arxiv.org/pdf/2611.23926)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generate local actions from visual observations, language, and robot state, but long-horizon manipulation requires the global task intent to remain grounded in the currently executable context. We propose GTI (Grounding Task Intent), which uses the current observation and execution history to localize the active subtask and its execution phase. For the same local subtask, GTI generates two phase-dependent visual targets: an interaction/contact state and a local completion state. The local language instruction and the corresponding phase-specific visual targe...

</details>

<details>
<summary>Share</summary>

```
GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation

Vision-language-action (VLA) models generate local actions from visual observations, language, and robot state, but long-horizon manipulation requires the global task intent to remain grounded in the currently executa...

arXiv: https://arxiv.org/abs/2611.23926

#VLA #robotics
```

</details>

---

### [RoboMorpher: Scaling Robot Morphology Representations for Cross-Embodiment Action Prediction](https://arxiv.org/abs/2611.24816)

**Authors:** Wenwei Lin, Yan Qin, Weiliang Deng, Zixuan Li, Kaixuan Wang et al. (15 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24816) | [PDF](https://arxiv.org/pdf/2611.24816) | [Project Page](https://robomorpher.github.io/)

<details>
<summary>Abstract</summary>

Learning shared action representations is central to cross-embodiment manipulation. However, identical joint values can produce different spatial configurations across robots, limiting representations learned from joint values alone. We introduce RoboMorpher, a morphology-conditioned action tokenizer that jointly reconstructs joint angles and link poses to associate control coordinates with their kinematic effects. MorphGen supplies scalable kinematic supervision by generating serial-arm descriptions from survey-derived geometric priors. We pretrain RoboMorpher on 40 million morphology-state p...

</details>

<details>
<summary>Share</summary>

```
RoboMorpher: Scaling Robot Morphology Representations for Cross-Embodiment Action Prediction

Learning shared action representations is central to cross-embodiment manipulation.

arXiv: https://arxiv.org/abs/2611.24816
Project page: https://robomorpher.github.io/

#VLA #robotics
```

</details>

---

### [GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving](https://arxiv.org/abs/2611.32510)

**Authors:** JiaHui Huang, Songyan Zhang, Hanbing Li, Hanchao Leng, Kuiyuan Yang et al. (8 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32510) | [PDF](https://arxiv.org/pdf/2611.32510)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) planners inherit semantic knowledge from pretrained vision-language models, but their reasoning is rarely grounded in 3D scene structure and its evolution over time. We introduce GeoVLDrive, a geometry-grounded VLA framework for 3D spatiotemporal reasoning and planning. Multi-layer features from a 3D foundation model augment the vision-language backbone through gated cross-attention. A structured latent chain of thought (CoT) organizes future scene geometry, key-agent motion, and meta-actions into ordered, separately supervised latent states. An action expert gener...

</details>

<details>
<summary>Share</summary>

```
GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving

Vision-language-action (VLA) planners inherit semantic knowledge from pretrained vision-language models, but their reasoning is rarely grounded in 3D scene structure and its evolution over time.

arXiv: https://arxiv.org/abs/2611.32510

#VLA #robotics
```

</details>

---

### [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](https://arxiv.org/abs/2611.27645)

**Authors:** Nan Tang, Han-Tao Zhang, Jing-Cheng Pang, Hao-Nan Wang, Hao-Xiang Ren et al. (11 authors)

**Published:** 2026-11-20 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.27645) | [PDF](https://arxiv.org/pdf/2611.27645)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences. However, existing VLA-MBRL methods primarily rely on large-scale image or video generation world models, incurring large computational overhead. Latent world models offer a more efficient alternative but face two challenges: compounding errors during recursive prediction and incompatibility with VLAs' visual input interfaces. In this work, we propose LS-MBPO, a lightweight residual MBRL framework that leverages latent world models to improve upon pretrained VLAs....

</details>

<details>
<summary>Share</summary>

```
Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models

Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences.

arXiv: https://arxiv.org/abs/2611.27645

#VLA #robotics
```

</details>

---

### [Beyond a Single Human Demonstration: Learning from Scored Trajectory Alternatives for End-to-End Driving](https://arxiv.org/abs/2611.27515)

**Authors:** Xinyao Rao, Zecheng Tang, Liuxuan Sun, Zheyuan Lai, Minjun Yu et al. (7 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.27515) | [PDF](https://arxiv.org/pdf/2611.27515) | [Project Page](https://rtwotwo.github.io/DriveSTA)

<details>
<summary>Abstract</summary>

Human driving logs record only one trajectory per scene, leaving other feasible driving choices without explicit trajectory targets or quality labels. This limits supervision for end-to-end planners that generate and refine multiple candidate trajectories. Meanwhile, conditioning refinement on a large vision-language model adds substantial online inference cost. We propose DriveSTA, which extends autoregressive proposal generation and proposal-conditioned residual flow refinement with scored trajectory alternatives. For each training scene, we generate alternatives offline through smooth defor...

</details>

<details>
<summary>Share</summary>

```
Beyond a Single Human Demonstration: Learning from Scored Trajectory Alternatives for End-to-End Driving

Human driving logs record only one trajectory per scene, leaving other feasible driving choices without explicit trajectory targets or quality labels.

arXiv: https://arxiv.org/abs/2611.27515
Project page: https://rtwotwo.github.io/DriveSTA

#VLA #robotics
```

</details>

---

### [DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies](https://arxiv.org/abs/2611.25695)

**Authors:** Jun Xia, Shangwen Wang, Jun Ma, Ruichao Ren, Zhouyang Jia et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.25695) | [PDF](https://arxiv.org/pdf/2611.25695)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks. However, optimized patterns can stand out from their surroundings, making an attack easier to notice and its carrier more likely to be inspected or removed. To address this limitation, our key insight is to search the structured image distribution of a diffusion model for natural-looking textures while using closed-loop feedback to identify task-disruptive candidates. Based on this idea, we propose DMT-Attack, a gradient-free gray-box attack that generate...

</details>

<details>
<summary>Share</summary>

```
DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies

Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks.

arXiv: https://arxiv.org/abs/2611.25695

#VLA #robotics
```

</details>

---

### [Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence](https://arxiv.org/abs/2611.32233)

**Authors:** Yujie Zhao, Anthony L. Hu, Zimeng Huang, Zhijing Wu, Luobin Wang et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.32233) | [PDF](https://arxiv.org/pdf/2611.32233)

<details>
<summary>Abstract</summary>

Time is a fundamental dimension of robotic intelligence: a robot may fail despite physically correct actions if it acts outside a valid time window, responds too slowly to an event, or fails to meet required throughput. Yet existing robotic benchmarks primarily emphasize spatial correctness and logical task completion, largely overlooking the temporal constraints of real-world applications. We present RoboClock, a unified benchmark for time-aware robotic manipulation featuring 60 tasks across five application domains. Mirroring these failure modes, RoboClock structures tasks around three types...

</details>

<details>
<summary>Share</summary>

```
Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence

Time is a fundamental dimension of robotic intelligence: a robot may fail despite physically correct actions if it acts outside a valid time window, responds too slowly to an event, or fails to meet required throughput.

arXiv: https://arxiv.org/abs/2611.32233

#VLA #robotics
```

</details>

---

### [Sparks of Weight-Space Programming for Robot Foundation Models](https://arxiv.org/abs/2611.31715)

**Authors:** Kyle Coelho, Eugen Solowjow

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31715) | [PDF](https://arxiv.org/pdf/2611.31715)

<details>
<summary>Abstract</summary>

This paper demonstrates an approach for correcting failures of robot foundation models (RFMs) without additional data collection, demonstrations, or training. We apply weight-space programming (WSP), in which a language-model agent directly reads and writes a neural network's parameters, to a large, pre-trained vision-language-action policy. The idea is simple: many policy failures are not random but repeatedly land in the same recognizable stuck state, so if that state is visible in the model's internal activations, a small edit could trigger a corrective movement while leaving the rest of th...

</details>

<details>
<summary>Share</summary>

```
Sparks of Weight-Space Programming for Robot Foundation Models

This paper demonstrates an approach for correcting failures of robot foundation models (RFMs) without additional data collection, demonstrations, or training.

arXiv: https://arxiv.org/abs/2611.31715

#VLA #robotics
```

</details>

---

### [SOAR: temporal Structure-guided One-step Action generation for Robotic manipulation](https://arxiv.org/abs/2611.30363)

**Authors:** Di Xin, Mingfei Han, Genming Cui, Yuanxiang Chen, Xiaolong Wu et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30363) | [PDF](https://arxiv.org/pdf/2611.30363)

<details>
<summary>Abstract</summary>

Efficient robotic manipulation requires temporally coordinated actions with low inference latency. Multi-step diffusion and flow policies progressively refine action trajectories but require costly iterative inference, whereas one-step policies eliminate iterative trajectory refinement to reduce inference cost. We introduce **SOAR**, a structure-guided one-step generative policy that improves action quality while preserving one-step efficiency. SOAR predicts an observation-conditioned discrete cosine transform (DCT) representation of future actions, capturing temporal variations across multipl...

</details>

<details>
<summary>Share</summary>

```
SOAR: temporal Structure-guided One-step Action generation for Robotic manipulation

Efficient robotic manipulation requires temporally coordinated actions with low inference latency.

arXiv: https://arxiv.org/abs/2611.30363

#VLA #robotics
```

</details>

---

### [AgentMoT: An Agentic Mixture-of-Transformers for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.30389)

**Authors:** Qihang Huang, Collister Chua, YuJie Yan, Shiyu Fang, Zhan Chen et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30389) | [PDF](https://arxiv.org/pdf/2611.30389)

<details>
<summary>Abstract</summary>

Driving models need to choose which capabilities to use and when to reconsider their decisions. We introduce AgentMoT, a Mixture-of-Transformers with built-in agent reasoning and system scheduling. Combinations of agent, world, and action experts form three jointly trained pathways for direct-action, vision-language-action, and world-action computation. The Router selects a native pathway, while the agent expert supplies reasoning and selects skills. Execution feedback raises wake-up requests, and the agent self-scheduler learns whether to reconsider the task decision or keep it. Mandatory req...

</details>

<details>
<summary>Share</summary>

```
AgentMoT: An Agentic Mixture-of-Transformers for End-to-End Autonomous Driving

Driving models need to choose which capabilities to use and when to reconsider their decisions.

arXiv: https://arxiv.org/abs/2611.30389

#VLA #robotics
```

</details>

---

### [Representation Alignment Is Only as Good as the Teacher's Behavioral Structure](https://arxiv.org/abs/2611.29483)

**Authors:** Zhengfeiyang Zhang, Haoyuan Chen, Hexin Wang, Hanyu Zhou, Zhenglin Wan et al. (7 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29483) | [PDF](https://arxiv.org/pdf/2611.29483)

<details>
<summary>Abstract</summary>

Recent works align the intermediate features of vision-language-action (VLA) models with frozen vision encoders during fine-tuning, hoping to inject additional priors such as 3D awareness or affordances. Unlike in image generation, where teachers for representation alignment (REPA) are assessed with encoder-intrinsic metrics, teachers for VLAs are still chosen largely by heuristics. We show that this practice is unreliable: across 14 teachers and 16 manipulation tasks, under matched training budgets, no off-the-shelf vision encoder improves the clean success rate of $π_{0.5}$ by more than 1 po...

</details>

<details>
<summary>Share</summary>

```
Representation Alignment Is Only as Good as the Teacher's Behavioral Structure

Recent works align the intermediate features of vision-language-action (VLA) models with frozen vision encoders during fine-tuning, hoping to inject additional priors such as 3D awareness or affordances.

arXiv: https://arxiv.org/abs/2611.29483

#VLA #robotics
```

</details>

---

### [More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation](https://arxiv.org/abs/2611.29339)

**Authors:** Xin Zhang, Yushuo Hou, Anqi Zhao, Moyun Liu, Xingwei Zhao et al. (8 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29339) | [PDF](https://arxiv.org/pdf/2611.29339)

<details>
<summary>Abstract</summary>

Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting actions. Yet this paradigm is inherited from Vision-Language Models, where it serves understanding rather than action: each latent is aligned with an isolated future frame, often enriched with further modalities of that frame. We find that this binds the policy to the appearance of its training scenes, so that it degrades sharply once the scene changes. We argue that visual latents fo...

</details>

<details>
<summary>Share</summary>

```
More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation

Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting acti...

arXiv: https://arxiv.org/abs/2611.29339

#VLA #robotics
```

</details>

---

### [InfoField3D: Differentiable Information Field for Embodied Task-Oriented View Planning](https://arxiv.org/abs/2611.29230)

**Authors:** Huan Lyu, Yawei Luo

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.29230) | [PDF](https://arxiv.org/pdf/2611.29230)

<details>
<summary>Abstract</summary>

Effective task execution requires embodied agents to select observation positions that provide sufficient task-relevant information. Existing approaches typically predict viewpoints with learned models or score discrete candidates, but they either struggle to incorporate new constraints such as reachability or require extensive candidate evaluation to search. We introduce InfoField3D, which lifts geometry-bound information into a differentiable analytic field, whose value at each 3D observation position represents the task-required information accessible there. It uses low-order spherical harm...

</details>

<details>
<summary>Share</summary>

```
InfoField3D: Differentiable Information Field for Embodied Task-Oriented View Planning

Effective task execution requires embodied agents to select observation positions that provide sufficient task-relevant information.

arXiv: https://arxiv.org/abs/2611.29230

#VLA #robotics
```

</details>

---

### [DeRail: Escaping Trajectory Priors via Counterfactual Action Steering for Mid-Execution Instruction Switching](https://arxiv.org/abs/2611.28803)

**Authors:** Yitong Hong, Xiangdong Feng, Xiaoxi Sun, Senqiao Yang, Boyao Han et al. (12 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28803) | [PDF](https://arxiv.org/pdf/2611.28803)

<details>
<summary>Abstract</summary>

Robots operating in the real world must often adapt when user instructions change mid-execution, yet current instruction-conditioned robot policies, including Vision-Language-Action (VLA) models and World-Action Models (WAMs), are largely evaluated under fixed-instruction episodes. We study mid-execution instruction switching and identify trajectory hijacking as a key failure mode, where the policy fails to redirect sufficiently toward the switched target, with its post-switch behavior remaining fully or partially drawn toward trajectories associated with non-target tasks. We propose Counterfa...

</details>

<details>
<summary>Share</summary>

```
DeRail: Escaping Trajectory Priors via Counterfactual Action Steering for Mid-Execution Instruction Switching

Robots operating in the real world must often adapt when user instructions change mid-execution, yet current instruction-conditioned robot policies, including Vision-Language-Action (VLA) models and World-Action Model...

arXiv: https://arxiv.org/abs/2611.28803

#VLA #robotics
```

</details>

---

### [AsyncMixVLA: Runtime Asynchronous Robot Policy Switching for Adaptation to Dynamic Environments](https://arxiv.org/abs/2611.28585)

**Authors:** Tamoghno Das, Keyon Jazayeri, Yerin Cho, Nazmul Takbir, Arshia Aravinthan et al. (6 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28585) | [PDF](https://arxiv.org/pdf/2611.28585)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models translate visual observations and language instructions into robot actions, enabling general-purpose robotic control. However, environmental perturbations, such as objects moving during execution, can undermine their reliability. Different policies exhibit complementary failures under mid-rollout perturbations, motivating selective switching between policies for recovery. Such switching can stall the robot during inference of the newly invoked policy or, if performed asynchronously, act on stale observations. We present AsyncMixVLA, an adaptive inference fra...

</details>

<details>
<summary>Share</summary>

```
AsyncMixVLA: Runtime Asynchronous Robot Policy Switching for Adaptation to Dynamic Environments

Vision-language-action (VLA) models translate visual observations and language instructions into robot actions, enabling general-purpose robotic control.

arXiv: https://arxiv.org/abs/2611.28585

#VLA #robotics
```

</details>

---

### [NAT: Scaling Causal Neural Action Tokenizers Across Embodiments](https://arxiv.org/abs/2611.28873)

**Authors:** Ahad Jawaid, Alexander Swerdlow, Yu Xiang

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28873) | [PDF](https://arxiv.org/pdf/2611.28873)

<details>
<summary>Abstract</summary>

Action tokenizers let robot policies treat control as autoregressive next-token prediction. As these policies are trained on larger and more diverse datasets, they will need a universal tokenizer that can encode actions from many embodiments and data sources, including ones it has not seen. We study action tokenization at scale, training on 49k hours of action data from real-world robots, handheld grippers, simulation, and humans. We introduce Neural Action Tokenizer (NAT), a causal tokenizer whose decoder lets actions be executed as their tokens are generated. Across four simulation benchmark...

</details>

<details>
<summary>Share</summary>

```
NAT: Scaling Causal Neural Action Tokenizers Across Embodiments

Action tokenizers let robot policies treat control as autoregressive next-token prediction.

arXiv: https://arxiv.org/abs/2611.28873

#VLA #robotics
```

</details>

---

### [Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies](https://arxiv.org/abs/2611.27171)

**Authors:** Yunpeng Mei, Chenyu Wang, Xiaowen Zhu, Chenbo Xin, Hongjie Cao et al. (9 authors)

**Published:** 2026-11-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.27171) | [PDF](https://arxiv.org/pdf/2611.27171)

<details>
<summary>Abstract</summary>

Visual labeling of egocentric demonstrations often leaves contiguous gaps in action supervision. Reliable poses around a gap still provide its net translation and rotation. We use this information to train vision-language-action policies while preserving ordinary flow matching on reliable local actions. A composition objective constrains the aggregate motion of missing-action estimates, combining multiple fixed windows when a gap exceeds the policy horizon. A shared interval branch learns from reliable endpoints and supplies the composition target. On LIBERO with 20% of demonstrations and 70.5...

</details>

<details>
<summary>Share</summary>

```
Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies

Visual labeling of egocentric demonstrations often leaves contiguous gaps in action supervision.

arXiv: https://arxiv.org/abs/2611.27171

#VLA #robotics
```

</details>

---

### [SCAP: Stochastic Context for Action Expert Pretraining](https://arxiv.org/abs/2611.27187)

**Authors:** Xiao Lin, Yaoxu Lyu, Ronghao Dang, Zhili Liu, Kaijing Ma et al. (12 authors)

**Published:** 2026-11-20 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.27187) | [PDF](https://arxiv.org/pdf/2611.27187)

<details>
<summary>Abstract</summary>

Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation. Yet single-modality pretraining can impair the vision--language interactions needed for subsequent joint prediction. We construct a diagnostic model in which VA or LA pretraining can disable an initially active pathway for joint vision--language modeling. In this model, subsequent training with complete visual and language inputs cannot restore the pathway, even with unlimited adaptation. We therefore introduce Stochastic Context for Action Expert Pretraining (...

</details>

<details>
<summary>Share</summary>

```
SCAP: Stochastic Context for Action Expert Pretraining

Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation.

arXiv: https://arxiv.org/abs/2611.27187

#VLA #robotics
```

</details>

---

### [Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance](https://arxiv.org/abs/2611.27182)

**Authors:** Sunli Chen, Yun Zong, Qinhong Zhou, Xiaowen Qiu, Jiaben Chen et al. (7 authors)

**Published:** 2026-11-20 (updated 2026-11-23) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.27182) | [PDF](https://arxiv.org/pdf/2611.27182)

<details>
<summary>Abstract</summary>

Agent harnesses are turn-based: the agent acts, waits for the result, then reasons. When the action invokes a pretrained robot policy, such as a vision-language-action (VLA) or world action model (WAM), the policy may react continuously to observations, but the agent cannot revisit its decision until the call returns. Meanwhile, a person may step into the robot's path or move the object it is about to grasp. Invoking the agent more often narrows this blind interval, but a reasoning model takes seconds per decision and most control steps need no new one. We propose TRIP, a training-free, event-...

</details>

<details>
<summary>Share</summary>

```
Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance

Agent harnesses are turn-based: the agent acts, waits for the result, then reasons.

arXiv: https://arxiv.org/abs/2611.27182

#VLA #robotics
```

</details>

---

### [Beyond the Sink Interpretation: Radial Attention in Flow-Based VLA Policies](https://arxiv.org/abs/2611.26385)

**Authors:** Yuxi Zheng, Yueqian Lin, Yudong Liu, Zijia Tang, Junyu Pan et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.26385) | [PDF](https://arxiv.org/pdf/2611.26385)

<details>
<summary>Abstract</summary>

Prior work calls the high attention on the first and last action tokens of a flow-based VLA policy a radial action sink, and uses these tokens to set the execution horizon. In language models, a sink is a token with high incoming attention, a small value, and little effect on the output. We test whether that profile holds, not the horizon rule, in one $π_{0.5}$ checkpoint on five RoboCasa tasks. The two endpoints receive 5.4% of action-key mass, 1.4 percentage points above their uniform share, and rotary positional encoding produces this excess: directly in shallow layers and through upstream...

</details>

<details>
<summary>Share</summary>

```
Beyond the Sink Interpretation: Radial Attention in Flow-Based VLA Policies

Prior work calls the high attention on the first and last action tokens of a flow-based VLA policy a radial action sink, and uses these tokens to set the execution horizon.

arXiv: https://arxiv.org/abs/2611.26385

#VLA #robotics
```

</details>

---

### [CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control](https://arxiv.org/abs/2611.25667)

**Authors:** Xu Pan, Chubin Zhang, Xingrui Yu, Runmin Lan, Zihao Wang et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.25667) | [PDF](https://arxiv.org/pdf/2611.25667)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies must react while visual inference is still running. Overlapping computation and execution reduces waiting, yet leaves perceptual memory stale and successive action chunks disconnected. We present CauSyncVLA, an asynchronous dual-system controller that aligns perceptual-memory prediction and trajectory correction with actual robot execution. Rather than forecasting pixels or physical states, a Causal Latent World Model predicts current perceptual memory from delayed visual anchors and executed state-action history, supervised through action-sensitive distil...

</details>

<details>
<summary>Share</summary>

```
CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control

Vision-Language-Action (VLA) policies must react while visual inference is still running.

arXiv: https://arxiv.org/abs/2611.25667

#VLA #robotics
```

</details>

---

### [FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash](https://arxiv.org/abs/2611.25580)

**Authors:** Yuseon Choi, Sanghyeon Park, Eunjong Lee, Hanseo Lee, Sangjin Kim

**Published:** 2026-11-19 | **Categories:** cs.AR, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.25580) | [PDF](https://arxiv.org/pdf/2611.25580)

<details>
<summary>Abstract</summary>

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computational overhead. This creates a new opportunity to improve task accuracy and inference efficiency simu...

</details>

<details>
<summary>Share</summary>

```
FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iter...

arXiv: https://arxiv.org/abs/2611.25580

#VLA #robotics
```

</details>

---

### [RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning](https://arxiv.org/abs/2611.25398)

**Authors:** Dijia Zhan, Jinyi Li, Xuemiao Xu, Yan Zhou, Yu Liu et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.25398) | [PDF](https://arxiv.org/pdf/2611.25398)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training. However, we find that demonstration data vary sharply in supervision value across temporal windows, and that each window's value to the policy evolves substantially during training rather than being fixed or captured by raw loss alone. Motivated by this finding, we propose RefreshGrad, an online adaptive data-sampling framework that periodically scores temporal windows from the evolving policy using five policy-native sign...

</details>

<details>
<summary>Share</summary>

```
RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training.

arXiv: https://arxiv.org/abs/2611.25398

#VLA #robotics
```

</details>

---

### [RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback](https://arxiv.org/abs/2611.24494)

**Authors:** Jiayou Zhu, Peng Guo, Litian Zhang, Xinze Shi, Yuting Zhang et al. (9 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CR, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.24494) | [PDF](https://arxiv.org/pdf/2611.24494)

<details>
<summary>Abstract</summary>

Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observations. To mitigate these threats, many existing defenses rely on policy adaptation or auxiliary models, but require additional training or inference. We introduce RECLAIM, a training-free, inference-time defense that uses a frozen VLA's own attention response to local visual interventions to guide purification during closed-loop embodied manipulation. Our key insight is that attent...

</details>

<details>
<summary>Share</summary>

```
RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback

Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observat...

arXiv: https://arxiv.org/abs/2611.24494

#VLA #robotics
```

</details>

---

### [Homeward: No Place Like the Training View](https://arxiv.org/abs/2611.24455)

**Authors:** Mingyang Lyu, Yinqian Sun, Gongce Cao, Guobin Shen, Yuhao Zhang et al. (11 authors)

**Published:** 2026-11-18 (updated 2026-11-19) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.24455) | [PDF](https://arxiv.org/pdf/2611.24455)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems from a closed-loop diagnostic paradox in simulation: while re-rendering perturbed views into the train...

</details>

<details>
<summary>Share</summary>

```
Homeward: No Place Like the Training View

Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precip...

arXiv: https://arxiv.org/abs/2611.24455

#VLA #robotics
```

</details>

---

### [Adaptive Action Horizon Selection via Flow-Field Uncertainty](https://arxiv.org/abs/2611.24178)

**Authors:** Idan Ben-Ami, Arnon Netzer, Sarah Keren, Idit Diamant

**Published:** 2026-11-18 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.24178) | [PDF](https://arxiv.org/pdf/2611.24178)

<details>
<summary>Abstract</summary>

Reliable uncertainty estimates are important for adaptive execution in vision-language-action (VLA) models. Existing approaches such as Adaptive Action Chunking (AAC) estimate action entropy from multiple sampled action chunks, introducing additional inference cost and capturing both uncertainty within an action trajectory and diversity across alternative strategies. We introduce Divergence-based Uncertainty-aware Adaptive Action Chunking (DUAC), a post-hoc method that extracts trajectory-conditioned predictive uncertainty from the vector field of a pretrained VLA. Building on a closed-form fl...

</details>

<details>
<summary>Share</summary>

```
Adaptive Action Horizon Selection via Flow-Field Uncertainty

Reliable uncertainty estimates are important for adaptive execution in vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2611.24178

#VLA #robotics
```

</details>

---

### [Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?](https://arxiv.org/abs/2611.24076)

**Authors:** Ryoichi Kurihara, Kota Sunamoto

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.24076) | [PDF](https://arxiv.org/pdf/2611.24076)

<details>
<summary>Abstract</summary>

VLA policies are fragile to rewording. Success rates alone cannot say whether a policy fails to choose the object or to complete the task, nor where in the policy to intervene. We study the released GR00T N1.7 on two LIBERO-Spatial tasks differing only in the landmark word telling which of two bowls to take. Synonyms absent from the training instructions send the policy to the bowl they name, unlike made-up words, yet complete 67.6% of one task's closed-loop episodes, against the original word's 100%. Before the connector between the vision-language model and the action generator, replacing on...

</details>

<details>
<summary>Share</summary>

```
Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?

VLA policies are fragile to rewording.

arXiv: https://arxiv.org/abs/2611.24076

#VLA #robotics
```

</details>

---

### [NereidVLA: Learning to Understand and Navigate the Underwater World](https://arxiv.org/abs/2611.24864)

**Authors:** Chenjie Zhao, Zhiliang Zhu, Quan Chen, Yuquan Xue, Xingxue Shi et al. (11 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.24864) | [PDF](https://arxiv.org/pdf/2611.24864)

<details>
<summary>Abstract</summary>

Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories. We present NereidVLA, a vision-language-action model that transfers marine spatial knowledge to language-conditioned 3D navigation. We first train Sea2Know on approximately two million marine examples to learn target grounding, spatial relations, and scene structure without paired robot-motion supervision. We then adapt it using expert trajectories executed under simulated underwater vehicle dynamics. Given RGB histories and a language instru...

</details>

<details>
<summary>Share</summary>

```
NereidVLA: Learning to Understand and Navigate the Underwater World

Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories.

arXiv: https://arxiv.org/abs/2611.24864

#VLA #robotics
```

</details>

---

### [Urban State Representation for Autonomous Mobility: A Survey of Multimodal Perception, Architectures, Datasets, and Benchmarks](https://arxiv.org/abs/2611.28129)

**Authors:** Binay Kumar Singh, Niels Da Vitoria Lobo

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.28129) | [PDF](https://arxiv.org/pdf/2611.28129)

<details>
<summary>Abstract</summary>

Cities are sensed by many platforms at once: on-board cameras, LiDAR and radar on autonomous vehicles, roadside units at intersections, drones and satellites overhead, and the GNSS traces of millions of trips. Yet most learned representations are built for one platform, one city, and one task. We survey this fragmented landscape through a single lens, the Urban State Representation (USR): a georeferenced, layered, time-varying, uncertainty-aware state that any sensing platform can write to and any downstream task can read from. We (i) formalize USR and five desiderata for it, and relate it to...

</details>

<details>
<summary>Share</summary>

```
Urban State Representation for Autonomous Mobility: A Survey of Multimodal Perception, Architectures, Datasets, and Benchmarks

Cities are sensed by many platforms at once: on-board cameras, LiDAR and radar on autonomous vehicles, roadside units at intersections, drones and satellites overhead, and the GNSS traces of millions of trips.

arXiv: https://arxiv.org/abs/2611.28129

#VLA #robotics
```

</details>

---

### [Boltz-Flow: Generating High-Quality Robot Action from Boltzmann Machine](https://arxiv.org/abs/2611.31038)

**Authors:** Hengzhi Jiang, Haixu Liu, Jindou Jia, Tinglan Wang, Shaobo Chen et al. (30 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31038) | [PDF](https://arxiv.org/pdf/2611.31038)

<details>
<summary>Abstract</summary>

Flow-matching policies integrate a velocity field from a fixed, observation-independent Gaussian source. However, since the source is unimodal and identical across all tasks, the limited representational capacity of Gaussian distributions constrains how far a policy can scale with growing task diversity. Moreover, the source factorizes over time steps and control dimensions, discarding the coordination that manipulation requires. We introduce Boltz-Flow, which replaces Gaussian initialization with a more powerful, observation- and instruction-conditioned Boltzmann source while leaving the base...

</details>

<details>
<summary>Share</summary>

```
Boltz-Flow: Generating High-Quality Robot Action from Boltzmann Machine

Flow-matching policies integrate a velocity field from a fixed, observation-independent Gaussian source.

arXiv: https://arxiv.org/abs/2611.31038

#VLA #robotics
```

</details>

---

### [FATCAT: Fault Injection Attacks Targeting Chip-level Alignment](https://arxiv.org/abs/2611.31129)

**Authors:** Peter Horvath, Ilia Shumailov, Zhuoran Liu, Lukasz Chmielewski, Lejla Batina

**Published:** 2026-11-23 | **Categories:** cs.CR, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31129) | [PDF](https://arxiv.org/pdf/2611.31129)

<details>
<summary>Abstract</summary>

Model alignment is the primary safety and security mechanism for enforcing refusal of malicious prompts in modern foundation models; yet, existing adversarial evaluations implicitly assume underlying hardware integrity. In this paper, we present FATCAT, the first physical fault-injection attacks capable of eliminating refusal in modern large language and vision-language models. Specifically, we present a non-invasive electromagnetic (EM) fault injection attack targeting GPU-accelerated Systems-on-Chip with physical access, requiring neither software execution privileges nor model-layer access....

</details>

<details>
<summary>Share</summary>

```
FATCAT: Fault Injection Attacks Targeting Chip-level Alignment

Model alignment is the primary safety and security mechanism for enforcing refusal of malicious prompts in modern foundation models; yet, existing adversarial evaluations implicitly assume underlying hardware integrity.

arXiv: https://arxiv.org/abs/2611.31129

#VLA #robotics
```

</details>

---

### [LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models](https://arxiv.org/abs/2611.25460)

**Authors:** LoongForge Team

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.25460) | [PDF](https://arxiv.org/pdf/2611.25460)

<details>
<summary>Abstract</summary>

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraini...

</details>

<details>
<summary>Share</summary>

```
LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to r...

arXiv: https://arxiv.org/abs/2611.25460

#VLA #robotics
```

</details>

---

### [Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation](https://arxiv.org/abs/2611.29377)

**Authors:** Shilin Shan, Yuxuan Hu, Chuhao Zhou, Yimeng Dong, Bohan Hou et al. (9 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.29377) | [PDF](https://arxiv.org/pdf/2611.29377)

<details>
<summary>Abstract</summary>

Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation. Force and tactile feedback provide complementary information, but their semantic ambiguity makes them difficult for agents to use directly. These signals must be interpreted according to their physical meaning, together with task phase and visual evidence. We propose Contact Harness, which uses reusable, optimized skills to guide a VLM agent in assessing contact states from multimodal feedback and selectin...

</details>

<details>
<summary>Share</summary>

```
Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation

Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.29377

#VLA #robotics
```

</details>

---

### [A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation](https://arxiv.org/abs/2611.29338)

**Authors:** Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang, Jia-Jun Wang et al. (14 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.29338) | [PDF](https://arxiv.org/pdf/2611.29338)

<details>
<summary>Abstract</summary>

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as semantic steps composed of reusable, parameterized action primitives, guided by explicit progress descriptions. Meanwhile, CP-SFT uses an explicit robot-specific system prompt to constra...

</details>

<details>
<summary>Share</summary>

```
A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced.

arXiv: https://arxiv.org/abs/2611.29338

#VLA #robotics
```

</details>

---

### [VTLA-RL: Learning Visuotactile Policies for Load-Adaptive Grasping](https://arxiv.org/abs/2611.28752)

**Authors:** Qiwei Wu, Qixuan Li, Xin Xiang, Xiangyu Chen, Xiang Xiao et al. (8 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.28752) | [PDF](https://arxiv.org/pdf/2611.28752)

<details>
<summary>Abstract</summary>

Vision-language-action foundation models learn general manipulation priors, but object mass and local slip are difficult to infer from vision alone. Changing loads require contact-driven grasp adjustments that demonstrations collected under fixed conditions may not adequately cover. We present VTLA-RL to study visuotactile grasping policies and their reinforcement learning (RL) post-training under varying loads. Our main approach shares a visual encoder between tactile-image histories and RGB inputs to jointly generate and execute motion and bilateral force targets in a unified action space. M...

</details>

<details>
<summary>Share</summary>

```
VTLA-RL: Learning Visuotactile Policies for Load-Adaptive Grasping

Vision-language-action foundation models learn general manipulation priors, but object mass and local slip are difficult to infer from vision alone.

arXiv: https://arxiv.org/abs/2611.28752

#VLA #robotics
```

</details>

---

### [RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](https://arxiv.org/abs/2611.27042)

**Authors:** Chenghao Yin, Da Huang, Di Yang, Jichao Wang, Junhui Wu et al. (34 authors)

**Published:** 2026-11-20 (updated 2026-11-23) | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.27042) | [PDF](https://arxiv.org/pdf/2611.27042)

<details>
<summary>Abstract</summary>

Simulation-based evaluation of embodied models requires calibrated interactions, diverse tasks, and explicit execution constraints. We present RoboColiseum, a platform combining system identification, composable physics and rendering, and multidimensional benchmarking. Recorded-command replay characterizes robot dynamics and object interactions, while a shared interface connects rigid and deformable simulation to rendering. Across 22 paired real--simulation robot--task configurations, task scores have a reported Pearson correlation of 0.9686. Eight evaluation tracks span instruction following,...

</details>

<details>
<summary>Share</summary>

```
RoboColiseum: Co-evolution of Simulation, Evaluation, and Models

Simulation-based evaluation of embodied models requires calibrated interactions, diverse tasks, and explicit execution constraints.

arXiv: https://arxiv.org/abs/2611.27042

#VLA #robotics
```

</details>

---

### [GraF-VTA: Neuro-Symbolic Trajectory Generation from Vision and Temporal Logic via Graph-Based Fusion](https://arxiv.org/abs/2611.25589)

**Authors:** Zezhi Liu, Zhiwei Zheng, Hanqian Luo, Deyun Qin, Shizhen Wu et al. (6 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25589) | [PDF](https://arxiv.org/pdf/2611.25589)

<details>
<summary>Abstract</summary>

Robotic planning from visual observations and signal temporal logic (STL) requires grounding task requirements in scene evidence while adapting plans to execution feedback. We present GraF-VTA, a graph-based framework that extends Vision-TL-Action with structured task representations, causal observation history, and closed-loop trajectory generation. Bidirectional cross-attention fuses STL syntax tokens with visual features, while an optional frozen automaton embedding supplies complementary untimed task structure. A temporal pyramid preserves detailed current observations and compresses older...

</details>

<details>
<summary>Share</summary>

```
GraF-VTA: Neuro-Symbolic Trajectory Generation from Vision and Temporal Logic via Graph-Based Fusion

Robotic planning from visual observations and signal temporal logic (STL) requires grounding task requirements in scene evidence while adapting plans to execution feedback.

arXiv: https://arxiv.org/abs/2611.25589

#VLA #robotics
```

</details>

---

### [TuringPAI: A Foundation for On-Device Physical AI](https://arxiv.org/abs/2611.25474)

**Authors:** Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang et al. (28 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25474) | [PDF](https://arxiv.org/pdf/2611.25474)

<details>
<summary>Abstract</summary>

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation histo...

</details>

<details>
<summary>Share</summary>

```
TuringPAI: A Foundation for On-Device Physical AI

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute.

arXiv: https://arxiv.org/abs/2611.25474

#VLA #robotics
```

</details>

---

### [MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation](https://arxiv.org/abs/2611.25105)

**Authors:** Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu et al. (13 authors)

**Published:** 2026-11-18 (updated 2026-11-20) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25105) | [PDF](https://arxiv.org/pdf/2611.25105)

<details>
<summary>Abstract</summary>

Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the high...

</details>

<details>
<summary>Share</summary>

```
MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

Every move in a robot team changes the world in which its teammates must act.

arXiv: https://arxiv.org/abs/2611.25105

#VLA #robotics
```

</details>

---

### [Full Rank and Stable Sampling of $\tanh$ Networks](https://arxiv.org/abs/2611.25867)

**Authors:** Philipp Grohs, Matěj Trödler

**Published:** 2026-11-19 | **Categories:** math.NA, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.25867) | [PDF](https://arxiv.org/pdf/2611.25867)

<details>
<summary>Abstract</summary>

We study the recovery of feedforward $\tanh$ networks of fixed architecture with $P$ parameters from finitely many point evaluations. First, we characterize the set of parameters where the differential of the realization map has full rank and show that it coincides with the regular parameters in the sense of Vla{č}i{ć} and B{ö}lcskei (2021). Second, we make use of this characterization to prove that almost every tuple of $2P+1$ sampling points yields uniform-norm Lipschitz stability on compact subsets of this parameter set. Third, we prove that for exact observations, projected gradient descen...

</details>

<details>
<summary>Share</summary>

```
Full Rank and Stable Sampling of $\tanh$ Networks

We study the recovery of feedforward $\tanh$ networks of fixed architecture with $P$ parameters from finitely many point evaluations.

arXiv: https://arxiv.org/abs/2611.25867

#VLA #robotics
```

</details>

---
