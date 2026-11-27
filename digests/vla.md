# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-27 23:54 UTC

**Papers shown:** 110 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers](https://arxiv.org/abs/2611.33769)

**Authors:** Zirui Li, Yujie Yan, Jingxuan Qian, Yangang Ren, Haizhou Yin et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★★★

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33769) | [PDF](https://arxiv.org/pdf/2611.33769) | [Project Page](https://lzrbit.github.io/FailPoint_X/) | [Code](https://github.com/yujieyan81/failpoint-x)

<details>
<summary>Abstract</summary>

Human takeovers offer corrective supervision for vision-language-action (VLA) policies, but their contribution to offline post-training must be separated from that of continued optimization. We introduce FailPoint-X, a benchmark for offline VLA post-training with human takeovers. To represent uncertainty in failure onset, an annotator marks an interval for each failure, and training takeovers start at seeded frames sampled within it. From one fixed $π_{0.5}$ checkpoint, which also initializes post-training, we assemble 629 natural failures across 10 LIBERO-X task families at up to five difficu...

</details>

<details>
<summary>Share</summary>

```
FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers

Human takeovers offer corrective supervision for vision-language-action (VLA) policies, but their contribution to offline post-training must be separated from that of continued optimization.

arXiv: https://arxiv.org/abs/2611.33769
Project page: https://lzrbit.github.io/FailPoint_X/
Code: https://github.com/yujieyan81/failpoint-x

#VLA #robotics
```

</details>

---

### [$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?](https://arxiv.org/abs/2611.33816)

**Authors:** Junmyeong Lee, Dongmin Shin, Wooseok Jeon, JunGyu Lee, Seunghyun Shin et al. (6 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33816) | [PDF](https://arxiv.org/pdf/2611.33816) | [Project Page](https://june65.github.io/Epsilon-Tilde)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) have widely adopted diffusion-based action generation for continuous robot motions, enabling fine-grained control across diverse tasks. However, recent studies have shown that their performance is highly sensitive to initial noise, with resulting action errors that make recovery difficult during execution. Existing approaches search for favorable noise initializations to improve performance, yet the action expert itself remains sensitive to noise. In this work, we reveal that initial noise induces a consistent directional bias in action space that closely a...

</details>

<details>
<summary>Share</summary>

```
$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?

Vision-language-action models (VLAs) have widely adopted diffusion-based action generation for continuous robot motions, enabling fine-grained control across diverse tasks.

arXiv: https://arxiv.org/abs/2611.33816
Project page: https://june65.github.io/Epsilon-Tilde

#VLA #robotics
```

</details>

---

### [FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models](https://arxiv.org/abs/2611.33635)

**Authors:** Jiaming Liang, Yifeng Zhan, Rongyi He, Mu Li, Jiaqi Fan et al. (12 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33635) | [PDF](https://arxiv.org/pdf/2611.33635) | [Project Page](https://freshvla.github.io/)

<details>
<summary>Abstract</summary>

Learning reusable latent actions from action-free videos offers an effective route to improving Vision-Language-Action (VLA) policies. However, reconstruction-oriented latent actions do not necessarily benefit policy learning: as they may encode task-irrelevant static appearance with scene identity, or entangle slowly varying task progress with fine-grained execution dynamics in limited discrete code. We propose FreshVLA, a VLA framework built on a frequency-guided, dynamics-sensitive learning paradigm for acquiring temporally hierarchical continuous latent actions. FreshVLA uses a high-pass p...

</details>

<details>
<summary>Share</summary>

```
FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models

Learning reusable latent actions from action-free videos offers an effective route to improving Vision-Language-Action (VLA) policies.

arXiv: https://arxiv.org/abs/2611.33635
Project page: https://freshvla.github.io/

#VLA #robotics
```

</details>

---

### [M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation](https://arxiv.org/abs/2611.34560)

**Authors:** Liufan Tan, Tong Wang, Yuehao Yin, Jian Chen, Yihang Yin et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34560) | [PDF](https://arxiv.org/pdf/2611.34560) | [Project Page](https://tlf-tlf.github.io/M2AdaptVLAPage/)

<details>
<summary>Abstract</summary>

Effective robotic manipulation calls for multimodal memory and rapid adaptation to shifts in contact dynamics. However, many existing policies, which retain either visual or wrench history, may miss key cues from the other modality. Moreover, even with wrench memory, fixed policies can struggle when contact conditions shift at deployment. To this end, we introduce M$^{2}$AdaptVLA, a vision-language-action model that integrates visual and wrench memories with predictive test-time adaptation. For visual memory, the model uses test-time training (TTT) to encode observation history in fast weights...

</details>

<details>
<summary>Share</summary>

```
M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation

Effective robotic manipulation calls for multimodal memory and rapid adaptation to shifts in contact dynamics.

arXiv: https://arxiv.org/abs/2611.34560
Project page: https://tlf-tlf.github.io/M2AdaptVLAPage/

#VLA #robotics
```

</details>

---

### [Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2611.32206)

**Authors:** Qing Zhang, Xuesong Li, Zhaoyuan Yang, Changlin Song, Xinyu Tian et al. (6 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

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

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

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

### [Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning](https://arxiv.org/abs/2611.32304)

**Authors:** Simin Huang, Jiawei Chen, Shaolong Zhu, Qiwei Liang, Zhaoxia Yin

**Published:** 2026-11-24 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

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

### [Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs](https://arxiv.org/abs/2611.34914)

**Authors:** Agelos Kratimenos, Kostas Daniilidis, Evangelos Chatzipantazis

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34914) | [PDF](https://arxiv.org/pdf/2611.34914)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wrong place or into collisions. Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has. We introduce Cairn, which keeps the VLA frozen and steers it at test time along learned 3D trajectories of the object in its gripper. A small prior reads point clouds of the scene and the held object, along with its pose when grasped and the instruction, an...

</details>

<details>
<summary>Share</summary>

```
Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs

Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wron...

arXiv: https://arxiv.org/abs/2611.34914

#VLA #robotics
```

</details>

---

### [Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation](https://arxiv.org/abs/2611.34538)

**Authors:** Yanran Jiang, Cécile Paris, Dana Kulić, Leimin Tian

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34538) | [PDF](https://arxiv.org/pdf/2611.34538) | [Project Page](https://dtu-bench.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies perform well on fixed-instruction robotic manipulation benchmarks, but their ability to adapt to instruction changes during execution remains understudied. We introduce the Dynamic Task Update Benchmark (DTU-Bench), evaluating 40 task revisions across seven update types and three execution stages using LIBERO, a simulated robotic manipulation benchmark. We compare performance when a new instruction is given before execution starts versus during execution, and examine whether the new task instructions are followed. Across 13 representative VLA configuration...

</details>

<details>
<summary>Share</summary>

```
Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation

Vision-language-action (VLA) policies perform well on fixed-instruction robotic manipulation benchmarks, but their ability to adapt to instruction changes during execution remains understudied.

arXiv: https://arxiv.org/abs/2611.34538
Project page: https://dtu-bench.github.io/

#VLA #robotics
```

</details>

---

### [HoloBrain-0.5 Technical Report](https://arxiv.org/abs/2611.34449)

**Authors:** Xuewu Lin, Jiahao Wang, Jiawei Li, Mengdi Li, Zhengmao Sun et al. (13 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34449) | [PDF](https://arxiv.org/pdf/2611.34449) | [Project Page](https://horizonrobotics.github.io/robot_lab/holobrain_0_5/)

<details>
<summary>Abstract</summary>

We present HoloBrain-0.5, a family of vision-language-action (VLA) models for manipulation across robot embodiments. The policies plan in a shared action space using robot state, kinematic structure, and calibrated camera observations. We standardize joint axes, coordinate frames, and tool-center points in robot descriptions (URDFs) and encode their kinematic graphs in a shared 3D representation. HoloBrain-0.5-Continuous generates action chunks by diffusion, while HoloBrain-0.5-Discrete uses residual finite scalar quantization (FSQ) and delayed autoregression. We pretrain both policies on over...

</details>

<details>
<summary>Share</summary>

```
HoloBrain-0.5 Technical Report

We present HoloBrain-0.5, a family of vision-language-action (VLA) models for manipulation across robot embodiments.

arXiv: https://arxiv.org/abs/2611.34449
Project page: https://horizonrobotics.github.io/robot_lab/holobrain_0_5/

#VLA #robotics
```

</details>

---

### [Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies](https://arxiv.org/abs/2611.33794)

**Authors:** Zilin Huang, Zhengyang Wan, Kangan Qian, Zihao Sheng, Sikai Chen

**Published:** 2026-11-25 | **Categories:** cs.AI, cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33794) | [PDF](https://arxiv.org/pdf/2611.33794) | [Project Page](https://zilin-huang.github.io/SealedLoop/)

<details>
<summary>Abstract</summary>

Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher. However, the judge is usually trained or chosen inside the same loop, so its evidence is not independent of the policy. We introduce SealedLoop, an evaluation framework that adds a sealed judge: an evaluator outside the loop that the improver cannot see or optimize against. A new policy is kept only when a sequential test on the sealed judge confirms the gain, with a bounded probability of keeping a worse one. Running the same loop under each j...

</details>

<details>
<summary>Share</summary>

```
Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies

Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher.

arXiv: https://arxiv.org/abs/2611.33794
Project page: https://zilin-huang.github.io/SealedLoop/

#VLA #robotics
```

</details>

---

### [Hi3R-VLA: Grounding Semantics and Actions in 3D](https://arxiv.org/abs/2611.31535)

**Authors:** Shizhe Chen, Paul Pacaud, Cordelia Schmid

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

**Published:** 2026-11-23 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

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

### [A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models](https://arxiv.org/abs/2611.34698)

**Authors:** Yuhao Luo, Zihao Sheng, Zilin Huang, Zhengyang Wan, Boyue Wang et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34698) | [PDF](https://arxiv.org/pdf/2611.34698)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action (VLA) models rarely satisfy all behavioral requirements of a new platform, and teams without a large deployed fleet lack the data to address the resulting failures. We propose a failure-driven data flywheel for post-training such models. It constructs target scenarios absent from the available data by inserting task-relevant entities into reconstructed real-world scenes, and evaluates the model against each behavioral requirement of the target task. Failure rates form a failure map across task conditions and difficulty levels, which is re-evaluated after each...

</details>

<details>
<summary>Share</summary>

```
A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models

Pretrained vision-language-action (VLA) models rarely satisfy all behavioral requirements of a new platform, and teams without a large deployed fleet lack the data to address the resulting failures.

arXiv: https://arxiv.org/abs/2611.34698

#VLA #robotics
```

</details>

---

### [Towards 360$^\circ$ Embodied UAV Tracking Without Turning](https://arxiv.org/abs/2611.33934)

**Authors:** Bingyu Li, Wu Du, Zhiyuan Zhao, Junyu Gao, Xuelong Li

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33934) | [PDF](https://arxiv.org/pdf/2611.33934) | [Project Page](https://libingyu01.github.io/360UAV-ETrack_360UAV-TVLA/)

<details>
<summary>Abstract</summary>

Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras. We investigate a complementary paradigm that uses full-spherical perception to follow designated targets without active heading adjustment. To support this setting, we introduce 360UAV-ETrack, a simulation benchmark comprising 2,652 sequences, over 1.73 million synchronized observations, eight tracking tasks, and 150 held-out closed-loop scenarios. We propose 360UAV-TVLA, a panoramic vision--language--action (VLA) framework integrating pers...

</details>

<details>
<summary>Share</summary>

```
Towards 360$^\circ$ Embodied UAV Tracking Without Turning

Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras.

arXiv: https://arxiv.org/abs/2611.33934
Project page: https://libingyu01.github.io/360UAV-ETrack_360UAV-TVLA/

#VLA #robotics
```

</details>

---

### [Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models](https://arxiv.org/abs/2611.31452)

**Authors:** Guangting Zheng, Shaoxuan Wang, Yu Yuan, Zhipeng Tang, Jiajun Deng et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

### [RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies](https://arxiv.org/abs/2611.34864)

**Authors:** Insup Lee, Hojin Jeon, Sunguk Shin, Seoungbin Bae, Taekwan Kim et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34864) | [PDF](https://arxiv.org/pdf/2611.34864)

<details>
<summary>Abstract</summary>

Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. However, even within a single segment, a speedup factor suitable for steady motion may be too high when precise alignment is required. To this end, this paper presents RePace, an offline reasoning framewor...

</details>

<details>
<summary>Share</summary>

```
RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies

Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection...

arXiv: https://arxiv.org/abs/2611.34864

#VLA #robotics
```

</details>

---

### [ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking](https://arxiv.org/abs/2611.34741)

**Authors:** Jasper Gerigk, Yang Xu, Nicholas Rhinehart, Igor Gilitschenski

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34741) | [PDF](https://arxiv.org/pdf/2611.34741) | [Project Page](https://uoft-isl.github.io/elmo.github.io/)

<details>
<summary>Abstract</summary>

Robot trajectories naturally decompose into variable-length phases with distinct semantic intents, such as reaching, grasping, and lifting. However, training policies to minimize MSE treats all actions as equal, obscuring their semantic structure. While latent action models attempt to create a structured prediction target by compressing action chunks into latent representations, existing approaches rely on two-stage training and context-blind decoders. Consequently, their representations are context-agnostic motion codes (e.g., "move down") which fail to capture behavioural intent (e.g., "pick...

</details>

<details>
<summary>Share</summary>

```
ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking

Robot trajectories naturally decompose into variable-length phases with distinct semantic intents, such as reaching, grasping, and lifting.

arXiv: https://arxiv.org/abs/2611.34741
Project page: https://uoft-isl.github.io/elmo.github.io/

#VLA #robotics
```

</details>

---

### [Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion](https://arxiv.org/abs/2611.34352)

**Authors:** Zezhi Liu, Jingwen Sun, Hongjin Chen, Shaojie Ren, Peiyan Tu et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34352) | [PDF](https://arxiv.org/pdf/2611.34352)

<details>
<summary>Abstract</summary>

Robotic tasks combine object relations, logical dependencies, and temporal requirements, which robot planning and industrial control commonly specify in temporal logic (TL). We introduce TL-VLA, a vision--language--action framework that replaces natural-language task instructions with temporal logic, making this spatiotemporal structure explicit. A typed graph encoder and visual--logical fusion condition continuous actions on the task specification and the current observations. To prepare a general vision--language backbone for this interface, we develop TL-aware robot pretraining with separat...

</details>

<details>
<summary>Share</summary>

```
Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion

Robotic tasks combine object relations, logical dependencies, and temporal requirements, which robot planning and industrial control commonly specify in temporal logic (TL).

arXiv: https://arxiv.org/abs/2611.34352

#VLA #robotics
```

</details>

---

### [DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training](https://arxiv.org/abs/2611.34287)

**Authors:** Sergei Kurchev, Iaroslav Kolomiets, Filipp Maksimov, Elizaveta Semenyakina, Miguel Altamirano Cabrera et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34287) | [PDF](https://arxiv.org/pdf/2611.34287)

<details>
<summary>Abstract</summary>

We present a dataset of 340 fully synthetic manipulation demonstrations generated from real seed data for Vision-Language-Action (VLA) training. The corpus contains 32,340 frames with synchronized RGB and actions across eight object categories, represented as LeRobot v2.1 episodes with H.264 video, per-frame robot states and pose-valued action labels, language task annotations, summary statistics and quality decisions. Each synthetic demonstration is produced without additional teleoperation: a LoRA-fine-tuned Cosmos-3 model generates a manipulation video, and RoboHaMeR recovers the correspond...

</details>

<details>
<summary>Share</summary>

```
DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training

We present a dataset of 340 fully synthetic manipulation demonstrations generated from real seed data for Vision-Language-Action (VLA) training.

arXiv: https://arxiv.org/abs/2611.34287

#VLA #robotics
```

</details>

---

### [Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes](https://arxiv.org/abs/2611.34280)

**Authors:** Xuetao Li, Chen Liu, Jing Wu, Sheng Liu, Miao Li

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34280) | [PDF](https://arxiv.org/pdf/2611.34280)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are trained to follow a fixed instruction, yet people change their minds while the robot acts. We identify the instruction black hole: once a VLA policy commits to a task, new instructions are absorbed and the robot completes the old task or freezes. We quantify it with a transmission ratio and an event horizon and prove it is a blind spot of static imitation, which cannot distinguish a policy that listens from a deaf one once the execution state reveals the task. We propose Wormhole, a training-free plug-in that relocates the robot instead of re-instructi...

</details>

<details>
<summary>Share</summary>

```
Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes

Vision-language-action (VLA) policies are trained to follow a fixed instruction, yet people change their minds while the robot acts.

arXiv: https://arxiv.org/abs/2611.34280

#VLA #robotics
```

</details>

---

### [Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data](https://arxiv.org/abs/2611.33880)

**Authors:** Koshi Oishi, Seigo Ito

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33880) | [PDF](https://arxiv.org/pdf/2611.33880)

<details>
<summary>Abstract</summary>

Forklifts play a critical role in warehousing and distribution, but existing automation systems remain limited in handling complex tasks that require sequential decision-making. Recently, vision--language--action (VLA) models have emerged as a promising approach for multi-step decision-making by directly generating control actions from visual observations and language prompts. Although VLA-based control has been extensively researched for manipulators, to the best of our knowledge, its application to forklifts remains unexplored. Therefore, this study demonstrates the integration of VLA contro...

</details>

<details>
<summary>Share</summary>

```
Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data

Forklifts play a critical role in warehousing and distribution, but existing automation systems remain limited in handling complex tasks that require sequential decision-making.

arXiv: https://arxiv.org/abs/2611.33880

#VLA #robotics
```

</details>

---

### [RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)

**Authors:** Chenzhi Liu, Jiehong Lin, Wei Huang, Xuzhao Huang, Haoyuan Li et al. (12 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34675) | [PDF](https://arxiv.org/pdf/2611.34675) | [Project Page](https://kaiknower.github.io/RoboEvo2/)

<details>
<summary>Abstract</summary>

Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings; reasoning agents can discover solutions using broad prior knowledge and robot-control APIs, but repeated deliberation and repair are costly. Inspired by human learning through reasoning and practice, we propose RoboEvo$^2$, a framework for recursive harness-policy co-evolution. In Policy-to-Harness (P2H) evolution, po...

</details>

<details>
<summary>Share</summary>

```
RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution

Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice.

arXiv: https://arxiv.org/abs/2611.34675
Project page: https://kaiknower.github.io/RoboEvo2/

#VLA #robotics
```

</details>

---

### [Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](https://arxiv.org/abs/2611.33398)

**Authors:** Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ming Jin, Ye Wang

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.33398) | [PDF](https://arxiv.org/pdf/2611.33398)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still remains challenging. Recent test-time steering methods have shown promise in enabling adaptive VLA policies by utilizing additional computation during deployment. In this paper, we consider best-of-$N$ test-time steering for VLA models, where multiple action candidates are sampled from a fixed policy and a verifier is used to select the best one during deployment. We show that increasing $N$ does not always improve performance when the verifie...

</details>

<details>
<summary>Share</summary>

```
Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models

Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still remains challenging.

arXiv: https://arxiv.org/abs/2611.33398

#VLA #robotics
```

</details>

---

### [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](https://arxiv.org/abs/2611.32665)

**Authors:** Sichen Wu, Qian Sun, Mengfan Liu, Weikai Qin, Bike Zhu et al. (6 authors)

**Published:** 2026-11-24 (updated 2026-11-25) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

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

### [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](https://arxiv.org/abs/2611.33010)

**Authors:** Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li et al. (8 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33010) | [PDF](https://arxiv.org/pdf/2611.33010) | [Code](https://github.com/iPPLab/robodojo-mirror)

<details>
<summary>Abstract</summary>

Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions. Across five policies spanning Vision-Language-Action models, World Action Models, and agent...

</details>

<details>
<summary>Share</summary>

```
Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies

Can a simple mirror expose the limitations of today's robotic manipulation policies?

arXiv: https://arxiv.org/abs/2611.33010
Code: https://github.com/iPPLab/robodojo-mirror

#VLA #robotics
```

</details>

---

### [What Does a Skill Vocabulary Cost? A Closed-Loop Decomposition over Demonstrated Motions](https://arxiv.org/abs/2611.32858)

**Authors:** Maximilian Xiling Li, Nils Blank, Paul Mattes, Pankhuri Vanjani, Rudolf Lioutikov

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

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

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

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

### [Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models](https://arxiv.org/abs/2611.34614)

**Authors:** Zikai Zhang, Hubert P. Shum, Toby Breckon

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34614) | [PDF](https://arxiv.org/pdf/2611.34614)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models introduce language reasoning into end-to-end autonomous driving. They output a language decision together with a trajectory, which makes the planner more interpretable. However, in existing methods the language decision is either an independent output or an index that selects among similar candidate trajectories, and its annotations are not verified against the trajectory. As a result, the language decision and the trajectory are often inconsistent in closed-loop driving. To address this, we propose Commit2Drive, a framework that imposes the language decisio...

</details>

<details>
<summary>Share</summary>

```
Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models

Vision-Language-Action (VLA) models introduce language reasoning into end-to-end autonomous driving.

arXiv: https://arxiv.org/abs/2611.34614

#VLA #robotics
```

</details>

---

### [FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips](https://arxiv.org/abs/2611.33810)

**Authors:** Zexi Zhao, Zizhen Liu, Jing Justin Ye, Huawei Li

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33810) | [PDF](https://arxiv.org/pdf/2611.33810)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generate robot actions from visual observations and language instructions in real-world environments, making malicious model tampering a potential threat to physical safety. We study whether object-triggered backdoors can be implanted through a small, fixed set of parameter bit flips without retraining. The central challenge is to make persistent weight modifications disrupt trigger-present behavior while preserving performance on non-trigger inputs. We propose FlipVLA, a two-stage selector-amplifier method that exploits existing visual features within an FC...

</details>

<details>
<summary>Share</summary>

```
FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips

Vision-language-action (VLA) models generate robot actions from visual observations and language instructions in real-world environments, making malicious model tampering a potential threat to physical safety.

arXiv: https://arxiv.org/abs/2611.33810

#VLA #robotics
```

</details>

---

### [Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs](https://arxiv.org/abs/2611.32705)

**Authors:** Dan Zlotnikov, Nadav Alali, Ohad Ben-Shahar

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

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

### [Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action](https://arxiv.org/abs/2611.33137)

**Authors:** Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner, Angela Dai

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33137) | [PDF](https://arxiv.org/pdf/2611.33137) | [Project Page](https://liu115.github.io/physicl)

<details>
<summary>Abstract</summary>

We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves perfor...

</details>

<details>
<summary>Share</summary>

```
Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action

We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces.

arXiv: https://arxiv.org/abs/2611.33137
Project page: https://liu115.github.io/physicl

#VLA #robotics
```

</details>

---

### [CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion](https://arxiv.org/abs/2611.34257)

**Authors:** Haoming Gu, Yunpeng Qing, Zhi Hou, Weinan Zhang

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.34257) | [PDF](https://arxiv.org/pdf/2611.34257)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models benefit from large, diverse datasets for robotic manipulation, yet collecting robot demonstrations remains costly. Recent work has explored egocentric videos as a source of supervision, primarily drawing on demonstrations of human-object interaction. We show that in-the-wild videos can improve robotic manipulation even when they contain no demonstrations of object manipulation. Specifically, camera motion recovered from these videos provides an additional source of motion supervision that complements robot demonstrations. Building on this finding, we introdu...

</details>

<details>
<summary>Share</summary>

```
CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion

Vision-Language-Action (VLA) models benefit from large, diverse datasets for robotic manipulation, yet collecting robot demonstrations remains costly.

arXiv: https://arxiv.org/abs/2611.34257

#VLA #robotics
```

</details>

---

### [Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents](https://arxiv.org/abs/2611.34778)

**Authors:** Yuxiang Lai, Jike Zhong, Yu-Jhe Li, Lan Wang, Chengzhi Liu et al. (12 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34778) | [PDF](https://arxiv.org/pdf/2611.34778)

<details>
<summary>Abstract</summary>

Recent vision-language models (VLMs) can act as robot-use agents that understand diverse scenes and control robots through policy code and tools. However, they predict 3D gripper poses poorly even with extended reasoning, struggling with precise manipulation. Vision-language-action (VLA) and world-action (WAM) models are the opposite: they execute fast, smooth control on trained tasks, yet fail under domain shifts or when tasks require long-horizon memory and reasoning. Agentic robots therefore combine VLM reasoning and perception with precise VLA/WAM control through a policy harness. Yet harn...

</details>

<details>
<summary>Share</summary>

```
Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents

Recent vision-language models (VLMs) can act as robot-use agents that understand diverse scenes and control robots through policy code and tools.

arXiv: https://arxiv.org/abs/2611.34778

#VLA #robotics
```

</details>

---

### [RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills](https://arxiv.org/abs/2611.33739)

**Authors:** Shengming Liu, Yunyi Gao, Xinyi Wang, Jianyong Sun, Shuai Wang et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33739) | [PDF](https://arxiv.org/pdf/2611.33739)

<details>
<summary>Abstract</summary>

Code-as-Policy agents generate, execute, and revise robot programs, but often lack explicit mechanisms to govern what persists across executions: which actions are retained within a trial and which code modifications carry over to subsequent runs. This leaves two critical aspects of agent behavior insufficiently controlled: step-level execution and cross-run adaptation. We present RegHarness, a two-level harness that governs both forms of persistence for the RATs agent team, without relying on a vision-language-action (VLA) policy or demonstrations. Within each trial, run-time governance evalu...

</details>

<details>
<summary>Share</summary>

```
RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills

Code-as-Policy agents generate, execute, and revise robot programs, but often lack explicit mechanisms to govern what persists across executions: which actions are retained within a trial and which code modifications...

arXiv: https://arxiv.org/abs/2611.33739

#VLA #robotics
```

</details>

---

### [Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations](https://arxiv.org/abs/2611.32353)

**Authors:** Ziang Ren, Zifan Wang, Zhuoyang Li, Benhao Qin, Haoyang Li et al. (11 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

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

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

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

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

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

### [One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation](https://arxiv.org/abs/2611.34360)

**Authors:** Yiqian Liu, Yuqi Lin, Hui Lu, Jiaming He, Qi Zhu et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34360) | [PDF](https://arxiv.org/pdf/2611.34360)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) and World Action Models (WAMs) are vulnerable to adversarial visual interference, motivating the study of universal and transferable physical patch attacks. We propose Object-Associated Patch Attack (OAPA), a universal and transferable physical patch framework that enables an attacker to select which task object's manipulation to disrupt through patch placement, without re-optimizing the patch. Our framework combines object-associated placement, differentiable physical compositing, and final action-expert representation divergence. Physical compositing accounts for...

</details>

<details>
<summary>Share</summary>

```
One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation

Vision-Language-Action (VLA) and World Action Models (WAMs) are vulnerable to adversarial visual interference, motivating the study of universal and transferable physical patch attacks.

arXiv: https://arxiv.org/abs/2611.34360

#VLA #robotics
```

</details>

---

### [Off the Driven Path: Transferable Road Understanding in Driving VLAs](https://arxiv.org/abs/2611.33878)

**Authors:** Lena Wild, Christian Helten, Katie Z Luo, Jakob Thumm, Rafael Valencia et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33878) | [PDF](https://arxiv.org/pdf/2611.33878)

<details>
<summary>Abstract</summary>

End-to-end driving policies increasingly operate without explicit HD maps at inference, raising the question of what road knowledge they actually internalize. To probe this knowledge through model outputs, we introduce Road-KSU, a framework that automatically converts HD maps and actor annotations into a road-centric scene graph. From this, we derive road-focused question answering and reasoning targets, complemented by map-based trajectory compliance metrics. Pairing Road-KSU with geographically disjoint splits yields a $2 \times 2$ evaluation crossing output modality (language vs. action) wi...

</details>

<details>
<summary>Share</summary>

```
Off the Driven Path: Transferable Road Understanding in Driving VLAs

End-to-end driving policies increasingly operate without explicit HD maps at inference, raising the question of what road knowledge they actually internalize.

arXiv: https://arxiv.org/abs/2611.33878

#VLA #robotics
```

</details>

---

### [NativeDrive: Native Multimodal Foundations for Autonomous Driving](https://arxiv.org/abs/2611.32216)

**Authors:** Zehua Fan, Qi Jiang, Wei Li, Kai Tang, Yue Jiang et al. (10 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

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

### [Hetero-Associative Visuomotor Memory: Soft Recall as a Base for Learned Residuals in Few-Demonstration Imitation](https://arxiv.org/abs/2611.34014)

**Authors:** Runcong Wang

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34014) | [PDF](https://arxiv.org/pdf/2611.34014)

<details>
<summary>Abstract</summary>

Retrieve-and-correct policies typically refine the nearest retrieved demonstration chunk, the readout that works best when executed directly. We study what a demonstration memory should supply to the corrector instead and find that a smooth, softmax-weighted recall over the whole memory is a much better base. On ALOHA cube transfer (40 human demonstrations), soft recall is no better to execute alone than the nearest chunk; however, with keys, candidates, and training fixed, correcting it raises success by 22.4 points on fresh resets with new encoders and by 7.4 against a closed-loop-tuned top-...

</details>

<details>
<summary>Share</summary>

```
Hetero-Associative Visuomotor Memory: Soft Recall as a Base for Learned Residuals in Few-Demonstration Imitation

Retrieve-and-correct policies typically refine the nearest retrieved demonstration chunk, the readout that works best when executed directly.

arXiv: https://arxiv.org/abs/2611.34014

#VLA #robotics
```

</details>

---

### [Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT](https://arxiv.org/abs/2611.33352)

**Authors:** Inayat Rasool, Chulwoo Pack, Shabbir Ahmed

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.33352) | [PDF](https://arxiv.org/pdf/2611.33352)

<details>
<summary>Abstract</summary>

Learned manipulation policies, from task-specific imitation policies to vision-language-action (VLA) models, rely primarily on RGB images. While some studies report gains from sensor depth, others avoid depth cameras because of measurement noise. Depth cameras introduce both noise and missing depth values (holes), whose relative effects remain unclear. In this study, we calibrate a sensor model using a real wrist-mounted stereo camera and separately evaluate noise and holes on RGB-D imitation policies with three visual encoders in simulation. We found that complete depth improves success by ap...

</details>

<details>
<summary>Share</summary>

```
Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT

Learned manipulation policies, from task-specific imitation policies to vision-language-action (VLA) models, rely primarily on RGB images.

arXiv: https://arxiv.org/abs/2611.33352

#VLA #robotics
```

</details>

---

### [MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory](https://arxiv.org/abs/2611.32564)

**Authors:** Jialong Peng, Shihao Zhou, Feng Yan, Wen Xiao, Haozheng Wang et al. (11 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

### [RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)

**Authors:** Yunbei Zhang, Zijian Jin, Shuaicheng Niu, Baian Chen, Weirui Ye et al. (7 authors)

**Published:** 2026-11-23 (updated 2026-11-24) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.30209) | [PDF](https://arxiv.org/pdf/2611.30209)

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

#VLA #robotics
```

</details>

---

### [RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)

**Authors:** Yunbei Zhang, Zijian Jin, Janet Wang, Xingchen Zhao, Zhenyu Zhang et al. (7 authors)

**Published:** 2026-11-23 (updated 2026-11-24) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.30111) | [PDF](https://arxiv.org/pdf/2611.30111)

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

### [GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving](https://arxiv.org/abs/2611.32510)

**Authors:** JiaHui Huang, Songyan Zhang, Hanbing Li, Hanchao Leng, Kuiyuan Yang et al. (8 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

### [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](https://arxiv.org/abs/2611.33390)

**Authors:** Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan, Xiaoyu Huang et al. (12 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.33390) | [PDF](https://arxiv.org/pdf/2611.33390)

<details>
<summary>Abstract</summary>

Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skills recorded elsewhere rarely transfer. We therefore ask: when manipulation hinges on spatial constraints, can robots reason out the right motions? We introduce RoboARC, a benchmark of 90 tasks in six constraint types over rigid and soft materials, on three robots in MuJoCo. Every task is a frozen scene with a physics-ba...

</details>

<details>
<summary>Share</summary>

```
RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints

Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts.

arXiv: https://arxiv.org/abs/2611.33390

#VLA #robotics
```

</details>

---

### [Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence](https://arxiv.org/abs/2611.32233)

**Authors:** Yujie Zhao, Anthony L. Hu, Zimeng Huang, Zhijing Wu, Luobin Wang et al. (9 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

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

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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

**Published:** 2026-11-23 (updated 2026-11-25) | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.30363) | [PDF](https://arxiv.org/pdf/2611.30363)

<details>
<summary>Abstract</summary>

Efficient robotic manipulation requires temporally coordinated actions with low inference latency. Multi-step diffusion and flow policies progressively refine action trajectories but require costly iterative inference, whereas one-step policies eliminate iterative trajectory refinement to reduce inference cost. We introduce SOAR, a structure-guided one-step generative policy that improves action quality while preserving one-step efficiency. SOAR predicts an observation-conditioned discrete cosine transform (DCT) representation of future actions, capturing temporal variations across multiple fr...

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

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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

### [Boltz-Flow: Generating High-Quality Robot Action from Boltzmann Machine](https://arxiv.org/abs/2611.31038)

**Authors:** Hengzhi Jiang, Haixu Liu, Jindou Jia, Tinglan Wang, Shaobo Chen et al. (30 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

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

**Published:** 2026-11-23 | **Categories:** cs.CR, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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
