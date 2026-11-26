# What's New

Papers discovered in the run at **2026-11-26 03:50 UTC**.

**New this run:** 36

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [EgoMyo: Physical Hand State Estimation from Egocentric Video and Wrist Electromyography](https://arxiv.org/abs/2611.34224)

**Authors:** Guanglong Sun, Kanglei Zhou, Ziteng Wang, Nana Wang, Hengkai Tan et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.34224) | [PDF](https://arxiv.org/pdf/2611.34224) | [Project Page](https://egomyo.github.io/)

<details>
<summary>Abstract</summary>

Physical hand interaction depends on configuration, contact, and force, yet nearly identical appearances can conceal different contact states and exerted forces. We therefore formulate physical hand state estimation from egocentric video and wrist surface electromyography (sEMG), combining visual geometry with neuromuscular evidence to jointly recover these coupled components. To support this task, we introduce EgoMyo, a benchmark spanning 5.75M video frames, 50 participants, 34 contact configurations, and repeated donnings, synchronizing these inputs with 3D hand pose and with contact and nor...

</details>

<details>
<summary>Share</summary>

```
EgoMyo: Physical Hand State Estimation from Egocentric Video and Wrist Electromyography

Physical hand interaction depends on configuration, contact, and force, yet nearly identical appearances can conceal different contact states and exerted forces.

arXiv: https://arxiv.org/abs/2611.34224
Project page: https://egomyo.github.io/

#egocentric #robotlearning
```

</details>

---

### [EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding](https://arxiv.org/abs/2611.33565)

**Authors:** Saif Mahmud, Vineet Parikh, Bharath Hariharan, Cheng Zhang

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.HC | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33565) | [PDF](https://arxiv.org/pdf/2611.33565) | [Project Page](https://saif-mahmud.github.io/projects/ego-carbs)

<details>
<summary>Abstract</summary>

Egocentric video records what a person looks at, but often misses what their body does: the hands leave the frame, and arm motion goes unseen. An exocentric camera recovers this context, but it must be installed wherever the activity happens. Active acoustic sensing can recover it from the wearables themselves: a device's speaker emits inaudible chirps, and its microphone senses the motion of the hands, arms, and nearby objects from their echoes. Yet no public dataset pairs it with egocentric video. We present EgoCARBS, with two deliverables. The first is a multimodal dataset and benchmark: 15...

</details>

<details>
<summary>Share</summary>

```
EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding

Egocentric video records what a person looks at, but often misses what their body does: the hands leave the frame, and arm motion goes unseen.

arXiv: https://arxiv.org/abs/2611.33565
Project page: https://saif-mahmud.github.io/projects/ego-carbs

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (16)

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

### [Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](https://arxiv.org/abs/2611.33398)

**Authors:** Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ming Jin, Ye Wang

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

### [Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT](https://arxiv.org/abs/2611.33352)

**Authors:** Inayat Rasool, Chulwoo Pack, Shabbir Ahmed

**Published:** 2026-11-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

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

### [RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](https://arxiv.org/abs/2611.33390)

**Authors:** Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan, Xiaoyu Huang et al. (12 authors)

**Published:** 2026-11-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

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

## World Models (18)

### [Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2611.33993)

**Authors:** Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang, Jianhua Han et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.33993) | [PDF](https://arxiv.org/pdf/2611.33993)

<details>
<summary>Abstract</summary>

Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution. Although future prediction can inform action correction, an accurate forecast does not establish whether modifying an existing action would be beneficial. We present Aegis-VLA, a world-model-guided vision-language-action (VLA) framework that generates predictive action corrections and separately determines whether and how strongly to apply them. A Trajectory World Model combines kinematic extrapolation with learned residual dynamics to predict objec...

</details>

<details>
<summary>Share</summary>

```
Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation

Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution.

arXiv: https://arxiv.org/abs/2611.33993

#worldmodels #robotics
```

</details>

---

### [DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model](https://arxiv.org/abs/2611.33779)

**Authors:** Zixuan Li, Kangyao Huang, Meng Xu, Wan Tian, Xiaoyu Tang et al. (11 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33779) | [PDF](https://arxiv.org/pdf/2611.33779)

<details>
<summary>Abstract</summary>

Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformations to ground the induced scene motion. We further introduce transform-aware pretraining, which pair...

</details>

<details>
<summary>Share</summary>

```
DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model

Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformati...

arXiv: https://arxiv.org/abs/2611.33779

#worldmodels #robotics
```

</details>

---

### [WorldUAV: Scaling UAV Data Synthesis via World Models](https://arxiv.org/abs/2611.33682)

**Authors:** Xuewen Liu, Mengjuan Chen, Jing Zhang, Mengzhe Shen, Zekun Xu et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33682) | [PDF](https://arxiv.org/pdf/2611.33682) | [Project Page](https://bienluky.github.io/WorldUAV/)

<details>
<summary>Abstract</summary>

UAV detection and tracking remain constrained by the scarcity of high-quality training data. Existing game-engine-based synthetic UAV data suffer from a substantial synthetic-to-real gap, while the high cost of manually collected real-world UAV data limits dataset scale. Therefore, we introduce WorldUAV, a high-quality UAV dataset constructed through an efficient framework powered by world models. Specifically, WorldUAV directly integrates UAVs into readily available real-world videos, naturally preserving realistic backgrounds, illumination, and scene dynamics. Leveraging the spatiotemporal p...

</details>

<details>
<summary>Share</summary>

```
WorldUAV: Scaling UAV Data Synthesis via World Models

UAV detection and tracking remain constrained by the scarcity of high-quality training data.

arXiv: https://arxiv.org/abs/2611.33682
Project page: https://bienluky.github.io/WorldUAV/

#worldmodels #robotics
```

</details>

---

### [VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors](https://arxiv.org/abs/2611.33591)

**Authors:** Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.33591) | [PDF](https://arxiv.org/pdf/2611.33591) | [Project Page](https://research.nvidia.com/labs/sil/projects/vivaworld/)

<details>
<summary>Abstract</summary>

Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D grounding. We introduce \textbf{VivaWorld}, a framework for generating geometry- and view-consistent long videos from an image. We first construct a compositional hybrid 3D representation that combines reconstructed point clouds, which preserve observed scene geometry and appearance, with generated textured meshes, which provide complete object geometry across $360^\circ$ novel views. W...

</details>

<details>
<summary>Share</summary>

```
VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors

Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D ground...

arXiv: https://arxiv.org/abs/2611.33591
Project page: https://research.nvidia.com/labs/sil/projects/vivaworld/

#worldmodels #robotics
```

</details>

---

### [Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics](https://arxiv.org/abs/2611.34302)

**Authors:** Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34302) | [PDF](https://arxiv.org/pdf/2611.34302)

<details>
<summary>Abstract</summary>

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning. Existing methods, however, either retarget human-specific geometry or match only static visual goals, and thus stumble over the cross-embodiment dynamics mismatch and the ungrounded action execution. We present the Co-World Model (CoWM), a predictive framework jointly optimized from paired yet unsynchronized human and robot streams. To bridge the cross-embodiment dynamics gap, CoWM di...

</details>

<details>
<summary>Share</summary>

```
Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning.

arXiv: https://arxiv.org/abs/2611.34302

#worldmodels #robotics
```

</details>

---

### [Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models](https://arxiv.org/abs/2611.34288)

**Authors:** Guangyu Liu, Hanzhang Wang, Huijia Zhang, Hanbei Zhan, Linjie Hu et al. (9 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34288) | [PDF](https://arxiv.org/pdf/2611.34288)

<details>
<summary>Abstract</summary>

Embodied world models aim to predict future interactions that are both visually realistic and physically consistent. Yet explicit 3D motion prediction alone does not guarantee that object structure and contact relationships are preserved. Beyond motion prediction, 3D representations provide an explicit state space for imposing structural and physical constraints. Building on this insight, we introduce RehearsalWorld, an editable robot world model driven by 3D Interaction Rehearsal (3DIR). Given an initial RGB-D observation and robot actions, Interaction-Consistent Rehearsal (ICR) uses a pretra...

</details>

<details>
<summary>Share</summary>

```
Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models

Embodied world models aim to predict future interactions that are both visually realistic and physically consistent.

arXiv: https://arxiv.org/abs/2611.34288

#worldmodels #robotics
```

</details>

---

### [WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](https://arxiv.org/abs/2611.34130)

**Authors:** Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang, Jinan Zhang, Linchao Zhu

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34130) | [PDF](https://arxiv.org/pdf/2611.34130)

<details>
<summary>Abstract</summary>

World models are increasingly used in robotics to improve the performance of embodied models. Compared with general-purpose video generation, robotics places more stringent requirements on world models. Generated videos must satisfy fine-grained physical constraints on robot motion and object interactions. However, existing world model benchmarks can overlook robotics specific physical details and struggle to assess them accurately. To address this problem, we introduce WorldPhy, a world model benchmark for accurate, fine-grained evaluation of physical plausibility in robotics. Our benchmark c...

</details>

<details>
<summary>Share</summary>

```
WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics

World models are increasingly used in robotics to improve the performance of embodied models.

arXiv: https://arxiv.org/abs/2611.34130

#worldmodels #robotics
```

</details>

---

### [Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures](https://arxiv.org/abs/2611.33925)

**Authors:** Zhiyue Zhao, Mingyu Liu, Bolin Zhang, Liyang Li, Guangyu Huang et al. (10 authors)

**Published:** 2026-11-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33925) | [PDF](https://arxiv.org/pdf/2611.33925)

<details>
<summary>Abstract</summary>

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, their predictions break down. Across five pretrained action-conditioned models, object-motion error is at most 10.4% lower than that of a static baseline that copies the first frame, and two models are worse than this baseline. We present WorldReforge, which teaches world models what happens when manipulation goes wrong. We construct the Reforge dataset o...

</details>

<details>
<summary>Share</summary>

```
Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations.

arXiv: https://arxiv.org/abs/2611.33925

#worldmodels #robotics
```

</details>

---

### [WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation](https://arxiv.org/abs/2611.33745)

**Authors:** Xu Yang, Kailai Sun, Qianchuan Zhao

**Published:** 2026-11-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33745) | [PDF](https://arxiv.org/pdf/2611.33745)

<details>
<summary>Abstract</summary>

World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation. Factual transitions alone determine action-wise marginal futures and average effects, but not individual effects or the probability that switching actions causes harm. We introduce WhatIf, a counterfactual world model for manipulation that couples candidate futures through shared latent physics and transition noise inferred from factual history. Each candidate action induces a sparse object-factor causal graph describing the physical pathways it acti...

</details>

<details>
<summary>Share</summary>

```
WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation

World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation.

arXiv: https://arxiv.org/abs/2611.33745

#worldmodels #robotics
```

</details>

---

### [CARE-WM: Same-Horizon Self-Conditioning with Constraint-Adaptive Regularization for Latent World Models](https://arxiv.org/abs/2611.34054)

**Authors:** Yuchen Lin, Kai Zhao

**Published:** 2026-11-25 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34054) | [PDF](https://arxiv.org/pdf/2611.34054)

<details>
<summary>Abstract</summary>

Planning with latent world models requires both accurate multi-step predictions and latent distances that reflect physical proximity to the goal. However, models are typically trained on ground-truth observations but must rely on their own imaginations during planning, while closer latent distances do not necessarily correspond to better task outcomes. Existing methods resort to auxiliary training objectives or additional task-cost readouts, which respectively incur extra training overhead or leave the latent geometry itself misaligned with task cost. We introduce CARE-WM, a drop-in training m...

</details>

<details>
<summary>Share</summary>

```
CARE-WM: Same-Horizon Self-Conditioning with Constraint-Adaptive Regularization for Latent World Models

Planning with latent world models requires both accurate multi-step predictions and latent distances that reflect physical proximity to the goal.

arXiv: https://arxiv.org/abs/2611.34054

#worldmodels #robotics
```

</details>

---

### [Normalizing Flows are Capable World Models](https://arxiv.org/abs/2611.33872)

**Authors:** Zijia Li, Yong-Hyun Park, Shusheng Yang, Jiatao Gu

**Published:** 2026-11-25 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33872) | [PDF](https://arxiv.org/pdf/2611.33872)

<details>
<summary>Abstract</summary>

A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encoder is invertible, the predicted distribution over latent states defines a distribution over future observations. Maximizing the exact conditional likelihood of those observations therefore trains the representation and dynamics jointly. An agent can plan directly in the learned latent space and decode sampled trajector...

</details>

<details>
<summary>Share</summary>

```
Normalizing Flows are Capable World Models

A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions.

arXiv: https://arxiv.org/abs/2611.33872

#worldmodels #robotics
```

</details>

---

### [Improving Building Energy Efficiency with an Indoor Environmental World Model and Counterfactual Adaptive Learning](https://arxiv.org/abs/2611.33764)

**Authors:** Xu Yang, Kailai Sun, Dianyu Zhong, Irfan Qaisar, Yu Yang et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33764) | [PDF](https://arxiv.org/pdf/2611.33764)

<details>
<summary>Abstract</summary>

Optimizing indoor climate systems plays a critical role in achieving the United Nations' Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing reinforcement learning (RL) methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors during long-horizon rollouts. Thus, we propose a novel occupant-centric indoor climate control framework. It develops indoor environmental world models to predict future physical thermal baselines and dynamic occup...

</details>

<details>
<summary>Share</summary>

```
Improving Building Energy Efficiency with an Indoor Environmental World Model and Counterfactual Adaptive Learning

Optimizing indoor climate systems plays a critical role in achieving the United Nations' Sustainable Development Goals 11 and 13.

arXiv: https://arxiv.org/abs/2611.33764

#worldmodels #robotics
```

</details>

---

### [DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.33734)

**Authors:** Lifan Jiang, Yifan Huang, Jixuan Zhang, Peifeng Wang, Yuying Ma et al. (8 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33734) | [PDF](https://arxiv.org/pdf/2611.33734)

<details>
<summary>Abstract</summary>

Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories. However, capturing synchronized camera trajectories often requires game-specific pipelines, limiting scalability. We therefore propose GameWeaver, a unified diffusion framework that automatically produces paired video--camera data through three complementary tasks: camera pose estimation from observed video, video generation along a prescribed camera trajectory, and joint video--camera generation from a reference image and text. First, each...

</details>

<details>
<summary>Share</summary>

```
DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation

Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories.

arXiv: https://arxiv.org/abs/2611.33734

#worldmodels #robotics
```

</details>

---

### [GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting](https://arxiv.org/abs/2611.33693)

**Authors:** Shijun Guo, Yaming Yang, Haoran Xu, Wei Zhao, Ziyu Guan et al. (7 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33693) | [PDF](https://arxiv.org/pdf/2611.33693)

<details>
<summary>Abstract</summary>

4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models. Semantic occupancy abstracts image color and texture into discrete labels, leaving 3D voxel arrangements as the primary cues for distinguishing local shapes within each class. Existing methods borrow image-encoding frameworks to obtain compact latent representations through height channelization or plane factorization, but do not sufficiently model within-column height patterns and cross-column relations jointly before compression, weakening these geometri...

</details>

<details>
<summary>Share</summary>

```
GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting

4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models.

arXiv: https://arxiv.org/abs/2611.33693

#worldmodels #robotics
```

</details>

---

### [A Simple Yet Effective Agent for Open-World Aerial Object Search](https://arxiv.org/abs/2611.34115)

**Authors:** Jitai Hao, Liangxing Yang, Zhenyang Li, Fan Liu, Qiang Huang et al. (6 authors)

**Published:** 2026-11-25 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.34115) | [PDF](https://arxiv.org/pdf/2611.34115)

<details>
<summary>Abstract</summary>

Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how far a minimal, training-free design can go, we introduce SimpleUAV, an agent built around a frozen, off-the-shelf vision-language model (VLM). SimpleUAV separates current-view target assessment from history-conditioned action selection, combining fresh candidate evidence with lightweight search context. Local geometry converts visual selections into bounded straight-line movements, depth-based checks halt blocked segments, and measured execution...

</details>

<details>
<summary>Share</summary>

```
A Simple Yet Effective Agent for Open-World Aerial Object Search

Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training.

arXiv: https://arxiv.org/abs/2611.34115

#worldmodels #robotics
```

</details>

---

### [SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467)

**Authors:** Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield

**Published:** 2026-11-24 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33467) | [PDF](https://arxiv.org/pdf/2611.33467)

<details>
<summary>Abstract</summary>

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We present SplatWAM (Splatting World Action Model), a generative world model that learns action-conditioned dynamics directly over compact 3D Gaussian primitives. A tokenizer SplatWAM-T first encodes a variable number of unposed views into a fixed budget of Gaussian tokens. A dynamics model SplatWAM-D then predicts future Gaussian states in a single forward pass per action, using log-Euclidean covariance coordinates and differentiable rendering supe...

</details>

<details>
<summary>Share</summary>

```
SplatWAM: Splatting World Action Models for Real-Time 3D Imagination

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution.

arXiv: https://arxiv.org/abs/2611.33467

#worldmodels #robotics
```

</details>

---

### [CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching](https://arxiv.org/abs/2611.33939)

**Authors:** Shizhuang Wang, Tianhao Wang, Xingqun Zhan

**Published:** 2026-11-25 | **Categories:** cs.LG, stat.ML | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33939) | [PDF](https://arxiv.org/pdf/2611.33939)

<details>
<summary>Abstract</summary>

Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems. The errors of such systems often vary with factors such as input quality and operating conditions, and thus cannot be accurately described by a single Gaussian model. Although Gaussian mixture models and calibrated quantiles can approximate such error distributions, their unconditional forms do not capture how the error behavior depends on these factors. Hence, we propose condUQ, an approach...

</details>

<details>
<summary>Share</summary>

```
CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching

Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems.

arXiv: https://arxiv.org/abs/2611.33939

#worldmodels #robotics
```

</details>

---

### [DreamTour: Layout Steering for Training-Free World Exploration](https://arxiv.org/abs/2611.33378)

**Authors:** Srikumar Sastry, Meher Gitika Karumuri, Chenqi Li, Sarosij Bose, Mellon Zhang et al. (10 authors)

**Published:** 2026-11-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.33378) | [PDF](https://arxiv.org/pdf/2611.33378)

<details>
<summary>Abstract</summary>

Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance. We present DreamTour, a training-free framework that generates camera tours from a single image with more accurate control over camera motion. DreamTour first uses a frozen image inpainting prior to extend the photograph beyond its original field of view while preserving the input pixels. Depth-based rendering of this extended scene along the requested camera path produces approximate target views that serve as spatial guidance. We introduce Layout Steering,...

</details>

<details>
<summary>Share</summary>

```
DreamTour: Layout Steering for Training-Free World Exploration

Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance.

arXiv: https://arxiv.org/abs/2611.33378

#worldmodels #robotics
```

</details>

---
