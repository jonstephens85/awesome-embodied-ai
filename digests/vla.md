# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-17 04:14 UTC

**Papers shown:** 31 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [SuperGlance: Driving at a Glance with a Vision-Language Model](https://arxiv.org/abs/2611.19138)

**Authors:** Jieyuan Pei, Xin Yan, Mingwei Xu, Haiyi Zhang, Siyu Zou et al. (12 authors)

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19138) | [PDF](https://arxiv.org/pdf/2611.19138) | [Project Page](https://guobapei.github.io/SuperGlance/) | [Code](https://github.com/GuobaPei/SuperGlance)

<details>
<summary>Abstract</summary>

Autonomous driving is turning to vision-language-action models (VLAs). They answer and plan by decoding, one step at a time. Each step is another forward pass, so a plan can take over a second of GPU time. Embodied AI often pairs such a slow, reasoning System 2 with a fast System 1 that acts. Human drivers plan at a glance, with System 1. Faster designs usually put System 1 outside the vision-language model (VLM), in a planner without its abilities. Yet before a VLM writes its first token, it has already read the scene into one hidden state. We show that, once trained, this hidden state is eno...

</details>

<details>
<summary>Share</summary>

```
SuperGlance: Driving at a Glance with a Vision-Language Model

Autonomous driving is turning to vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.19138
Project page: https://guobapei.github.io/SuperGlance/
Code: https://github.com/GuobaPei/SuperGlance

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

### [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](https://arxiv.org/abs/2611.20011)

**Authors:** Nikos Theodoridis, Reenu Mohandas, Sushil Sharma, Ciarán Hogan, Ganesh Sistu et al. (8 authors)

**Published:** 2026-11-15 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.20011) | [PDF](https://arxiv.org/pdf/2611.20011)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios. Although these models achieve state-of-the-art results on autonomous driving benchmarks, most existing benchmarks are dominated by nominal scenarios and therefore cannot test this promise. To test one such long-tail capability that is critical for safety, we introduce ReactBench-AD, a benchmark that measures how driving models react to objects that appear in the ego vehicle's path. Built on real NAVSIM and PhysicalAI-Autonomous...

</details>

<details>
<summary>Share</summary>

```
ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?

Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios.

arXiv: https://arxiv.org/abs/2611.20011

#VLA #robotics
```

</details>

---

### [PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models](https://arxiv.org/abs/2611.20010)

**Authors:** Hanbo Zhang, Lianlei Shan, Liuhaichen Yang, Zezhi Tang

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.20010) | [PDF](https://arxiv.org/pdf/2611.20010)

<details>
<summary>Abstract</summary>

Test-time scaling improves vision-language-action (VLA) policies by drawing several action candidates and executing the best one. We find that its returns diminish quickly when the candidates are resampled from one decoder: they differ by noise rather than by plan, and for each of three resampling sources, going from four to eight candidates adds only 0.06-0.07 to the average number of completed tasks on CALVIN. We introduce PlanDiv, an action head that makes the candidates differ by plan: a lightweight planner proposes K latent plan hypotheses, a shared masked-diffusion executor decodes one a...

</details>

<details>
<summary>Share</summary>

```
PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models

Test-time scaling improves vision-language-action (VLA) policies by drawing several action candidates and executing the best one.

arXiv: https://arxiv.org/abs/2611.20010

#VLA #robotics
```

</details>

---

### [ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents](https://arxiv.org/abs/2611.18176)

**Authors:** Yundi Cai, Zihan Wang, Chenxi Han, Yi Cheng, Houde Liu et al. (6 authors)

**Published:** 2026-11-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.18176) | [PDF](https://arxiv.org/pdf/2611.18176) | [Code](https://github.com/Embodied-Self-Improvement/ESI)

<details>
<summary>Abstract</summary>

Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior. The VLA may generate actions that diverge from the LLM's intended subtask and, upon regaining control after a correction, undo the promising state restored by the LLM. We introduce ESI (Embodied Self-Improvement), an automated flywheel that uses environmental interaction to align reasoning and action. ESI treats the modular agent as the unit of post-training, repeatedly refining the...

</details>

<details>
<summary>Share</summary>

```
ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents

Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior.

arXiv: https://arxiv.org/abs/2611.18176
Code: https://github.com/Embodied-Self-Improvement/ESI

#VLA #robotics
```

</details>

---

### [Scaling VLA Serving Under Robotic Execution Constraints](https://arxiv.org/abs/2611.14969)

**Authors:** Yue Zhang, Zicong Ye, Lufang Chen, Dance Yang, Mingyang Li et al. (17 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

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

### [When Backdoors Can Be Switched Off: Suppression-Aware Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2611.19774)

**Authors:** Nur Afsa Syeda, Mohamed Elmahallawy

**Published:** 2026-11-15 | **Categories:** cs.CV, cs.CR | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.19774) | [PDF](https://arxiv.org/pdf/2611.19774)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map visual observations, robot states, and natural-language instructions to robotic actions, but their multimodal interfaces introduce new security risks. Existing VLA backdoor attacks primarily study trigger-based activation and stealthy action manipulation, leaving conditional suppression of malicious behavior underexplored. We investigate suppression-aware backdoors, which combine conjunctive trigger activation with instruction-conditioned suppression. We instantiate this design through three variants: Cross-Modal Trigger, combining robot-state and spatia...

</details>

<details>
<summary>Share</summary>

```
When Backdoors Can Be Switched Off: Suppression-Aware Backdoor Attacks on Vision-Language-Action Models

Vision-Language-Action (VLA) models map visual observations, robot states, and natural-language instructions to robotic actions, but their multimodal interfaces introduce new security risks.

arXiv: https://arxiv.org/abs/2611.19774

#VLA #robotics
```

</details>

---

### [Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations](https://arxiv.org/abs/2611.19196)

**Authors:** Chen Liu, Nikolaus Correll

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19196) | [PDF](https://arxiv.org/pdf/2611.19196) | [Project Page](https://robonana.github.io/ego2sim2humanoid/)

<details>
<summary>Abstract</summary>

Imitation learning for visuomotor policies typically relies on teleoperated robot demonstrations, which are costly because every episode requires a trained operator controlling a physical robot in real time through teleoperation interfaces and wearable body-tracking hardware. Egocentric glasses capture human demonstrations without a robot or handheld grippers, yet they track only the head and in-view human hands, and directly copying human motion to a robot with different stature, arm reach and hand morphology fails to produce feasible contacts. \method{} converts egocentric glasses recordings...

</details>

<details>
<summary>Share</summary>

```
Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations

Imitation learning for visuomotor policies typically relies on teleoperated robot demonstrations, which are costly because every episode requires a trained operator controlling a physical robot in real time through te...

arXiv: https://arxiv.org/abs/2611.19196
Project page: https://robonana.github.io/ego2sim2humanoid/

#VLA #robotics
```

</details>

---

### [Wireless Edge-Assisted Adaptive Latent Reasoning for Vision-Language-Action Models in Physical AI](https://arxiv.org/abs/2611.19131)

**Authors:** Fatih Temiz, Melike Erol-Kantarci

**Published:** 2026-11-14 | **Categories:** cs.RO, cs.NI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19131) | [PDF](https://arxiv.org/pdf/2611.19131)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable embodied artificial intelligence (AI) by translating visual observations and language instructions into robotic actions. Emerging use cases in physical AI are expected to drive the need for efficient inference and communication, as the computational demands of the VLA models pose challenges for real-time control with limited onboard resources. Test-time scaling through latent reasoning allows these models to refine hidden representations without generating explicit chain-of-thought (CoT) tokens, but introduces a trade-off between task success, inferen...

</details>

<details>
<summary>Share</summary>

```
Wireless Edge-Assisted Adaptive Latent Reasoning for Vision-Language-Action Models in Physical AI

Vision-language-action (VLA) models enable embodied artificial intelligence (AI) by translating visual observations and language instructions into robotic actions.

arXiv: https://arxiv.org/abs/2611.19131

#VLA #robotics
```

</details>

---

### [Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment](https://arxiv.org/abs/2611.18372)

**Authors:** Suvarna Kadam, Soran Parsa

**Published:** 2026-11-13 | **Categories:** cs.RO, cs.AI, cs.ET | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.18372) | [PDF](https://arxiv.org/pdf/2611.18372)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control. In under 4 years the field has moved from RT-2, the first VLA, to open models that fine-tune on a single consumer GPU and to proprietary generalists that clean unseen homes. This survey reviews 88 works from December 2022 to October 2026, mainly on manipulation and navigation, plus humanoid control, world-action models and evaluation. We follow a VLA through its life cycle, from model design to training and deployment, along seven axes...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control.

arXiv: https://arxiv.org/abs/2611.18372

#VLA #robotics
```

</details>

---

### [STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models](https://arxiv.org/abs/2611.16589)

**Authors:** Zhuo Han, Yeqiang Wang, Xinran Wang, Hongwei Han, Yi Xiong et al. (11 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16589) | [PDF](https://arxiv.org/pdf/2611.16589) | [Project Page](https://stvla.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires both spatial scene understanding and task history. However, many vision-language-action (VLA) policies rely primarily on current observations, without explicitly integrating spatial structure and task history. Appearance-based memories can be sensitive to occlusion and viewpoint changes, while spatial representations of the current scene alone do not preserve how the scene has changed during task execution. We introduce STVLA, a framework that incorporates features from a pretrained visual geometry foundation model into temporal memory alongside visual repre...

</details>

<details>
<summary>Share</summary>

```
STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models

Robotic manipulation often requires both spatial scene understanding and task history.

arXiv: https://arxiv.org/abs/2611.16589
Project page: https://stvla.github.io/

#VLA #robotics
```

</details>

---

### [I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History](https://arxiv.org/abs/2611.16419)

**Authors:** Xiangyi Jia, Kaixian Qu, Shengzhi Wang, Chenyu Yang, Robert Katzschmann et al. (6 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16419) | [PDF](https://arxiv.org/pdf/2611.16419) | [Project Page](https://see-want.github.io/)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly inferring the ongoing atomic action and the broader mission it serves from a short visual teleoperation history. To study this, we introduce VI AMO (Vision Intention Action and Mission Ongoing), a dataset of 6,600 episodes from eleven robot so...

</details>

<details>
<summary>Share</summary>

```
I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control.

arXiv: https://arxiv.org/abs/2611.16419
Project page: https://see-want.github.io/

#VLA #robotics
```

</details>

---

### [MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes](https://arxiv.org/abs/2611.15937)

**Authors:** Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15937) | [PDF](https://arxiv.org/pdf/2611.15937) | [Project Page](https://mmahdavian.github.io/MOSAIC/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relationships to be inferred implicitly. This limitation is particularly problematic in cluttered environments, where small spatial errors can lead to unintended contacts or collisions. We propose MOSAIC, a modular spatial- and obstacle-aware framework that can be integrated with pretrained VLA policies to improve object-level scene understanding and action generation. Our method augmen...

</details>

<details>
<summary>Share</summary>

```
MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relati...

arXiv: https://arxiv.org/abs/2611.15937
Project page: https://mmahdavian.github.io/MOSAIC/

#VLA #robotics
```

</details>

---

### [ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490)

**Authors:** Zibin Dong, Yicheng Liu, Shiduo Zhang, Tianyuan Yuan, Baijun Ye et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15490) | [PDF](https://arxiv.org/pdf/2611.15490) | [Project Page](https://zibindong.github.io/actioncodec2-page/)

<details>
<summary>Abstract</summary>

Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We introduce ActionCodec2, a non-neural streaming tokenizer that releases actions incrementally while keeping trajectory reconstruction error within a prescribed tolerance. Its encoder quantizes each step relative to the decoder's reconstructed state, so the selected motion primitive corrects residual error rather than allowing errors from independently quantized increments to accumulate. Finding the smallest such primiti...

</details>

<details>
<summary>Share</summary>

```
ActionCodec2: A Streaming Action Tokenizer

Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable.

arXiv: https://arxiv.org/abs/2611.15490
Project page: https://zibindong.github.io/actioncodec2-page/

#VLA #robotics
```

</details>

---

### [Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning](https://arxiv.org/abs/2611.15381)

**Authors:** Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer, Yung-Hui Li, Donglin Chen et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15381) | [PDF](https://arxiv.org/pdf/2611.15381) | [Project Page](https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored. We present a low-cost and reproducible mobile bimanual platform integrating two LeRobot SO-101 manipulators with a TurtleBot 4 and a LeRobot-ROS 2 software stack. Using long-horizon toilet cleaning as a case study, we collect 250 real-world demonstrations and evaluate $π_0$, $π_{0.5}$, SmolVLA, and GR00T under the same embodiment and task conditions. We further evaluate variants using SARM-derived task-progress signal...

</details>

<details>
<summary>Share</summary>

```
Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning

Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored.

arXiv: https://arxiv.org/abs/2611.15381
Project page: https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/

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

### [Bring Back Language to Actions: Restoring VLM capabilities in VLA Models via Parameter Merging](https://arxiv.org/abs/2611.18891)

**Authors:** Mohamed Salim Aissi, Olivier Sigaud, Laure Soulier, Nicolas Thome

**Published:** 2026-11-13 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.18891) | [PDF](https://arxiv.org/pdf/2611.18891)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) are obtained by fine-tuning pre-trained Vision-Language Models (VLMs) on robot demonstration data, enabling action prediction from visual observations and language instructions. However, this fine-tuning induces catastrophic forgetting, substantially degrading the semantic and visual grounding capabilities of the original VLM. We address this by merging the parameters of a VLM and its VLA derivative without retraining either model. Concretely, we extract the task vector (the difference between VLA and VLM weights) and decompose it via Singular Value Decompo...

</details>

<details>
<summary>Share</summary>

```
Bring Back Language to Actions: Restoring VLM capabilities in VLA Models via Parameter Merging

Vision-Language-Action models (VLAs) are obtained by fine-tuning pre-trained Vision-Language Models (VLMs) on robot demonstration data, enabling action prediction from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.18891

#VLA #robotics
```

</details>

---

### [Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning](https://arxiv.org/abs/2611.19198)

**Authors:** Jae Hun Hwang, Yechan Seo, Hong-In Won

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19198) | [PDF](https://arxiv.org/pdf/2611.19198)

<details>
<summary>Abstract</summary>

In simulation, Vision-Agent-Action (VAA) performs pick-and-place in robot cells with gripper or base-frame changes without robot demonstrations or fine-tuning. It uses pre-trained vision-language and language models for interpretation, measures the command map and camera geometry from its own motion and fingertips, estimates lens distortion, and plans grasps from measured object depth. A controlled study of eight public LIBERO-fine-tuned vision-language-action models (VLAs) varies robot hardware, camera geometry, appearance, and base frame. Gripper and frame changes dominate their losses in th...

</details>

<details>
<summary>Share</summary>

```
Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning

In simulation, Vision-Agent-Action (VAA) performs pick-and-place in robot cells with gripper or base-frame changes without robot demonstrations or fine-tuning.

arXiv: https://arxiv.org/abs/2611.19198

#VLA #robotics
```

</details>

---

### [Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training](https://arxiv.org/abs/2611.17394)

**Authors:** Gongyue Teng, Yuqing Xie, Yixian Zhang, Feng Gao, Shu'ang Yu et al. (13 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.17394) | [PDF](https://arxiv.org/pdf/2611.17394)

<details>
<summary>Abstract</summary>

Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning. Coding agents can autonomously generate demonstrations through environment interaction, yet successful execution alone does not ensure effective supervision for VLA learning. We introduce Agentic-Teacher, an autonomous data engine for failure-driven VLA post-training. Given a VLA checkpoint, a task specification, and configured environment tools, the engine analyzes failed rollouts, selects intervention states, and iteratively develops cl...

</details>

<details>
<summary>Share</summary>

```
Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training

Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning.

arXiv: https://arxiv.org/abs/2611.17394

#VLA #robotics
```

</details>

---

### [What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation](https://arxiv.org/abs/2611.16246)

**Authors:** Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu et al. (7 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.16246) | [PDF](https://arxiv.org/pdf/2611.16246)

<details>
<summary>Abstract</summary>

Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test time. Agent sessions are not VLA demonstrations. They include motions driven by planner tools and sub-instructions, along with detours. We present H2E, a task-level experience distillation method that converts these sessions into VLA training data. Every motion becomes a VLA action under the original task instruction,...

</details>

<details>
<summary>Share</summary>

```
What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation

Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model.

arXiv: https://arxiv.org/abs/2611.16246

#VLA #robotics
```

</details>

---

### [What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491)

**Authors:** Zhuoyue Li, Zhendong Han, Pankhuri Vanjani, Wenting Li, Rudolf Lioutikov

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15491) | [PDF](https://arxiv.org/pdf/2611.15491)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA reactive, using \pihalf{} on two dynamic simulation benchmarks and three real-robot tasks. We vary the prediction and execution horizons, compare synchronous and asynchronous inference, test methods that deliver actions sooner or keep successive chunks continuous, and adapt the policy with motion cues and latent-space reinforcement learning. The best prediction horizon is about one second, and the best execution horizo...

</details>

<details>
<summary>Share</summary>

```
What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation

Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed.

arXiv: https://arxiv.org/abs/2611.15491

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

### [ResWAM: Learning What Changes, Not What Stays, for World-Action Models](https://arxiv.org/abs/2611.19559)

**Authors:** Chongyu Fan, Gaowen Liu, Ramana Rao Kompella, Jason Corso, Sijia Liu

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.19559) | [PDF](https://arxiv.org/pdf/2611.19559)

<details>
<summary>Abstract</summary>

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world. Existing WAMs supervise complete future observations. However, observations typically change little over an action chunk, so the future loss is dominated by copying static background content rather than learning task-relevant robot and object motion, limiting policy learning. Moreover, existing WAMs rely on large video generation models or separate world models, incurring heavy training and inference compute that hind...

</details>

<details>
<summary>Share</summary>

```
ResWAM: Learning What Changes, Not What Stays, for World-Action Models

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world.

arXiv: https://arxiv.org/abs/2611.19559

#VLA #robotics
```

</details>

---

### [MARS: Dynamic Routing of Reinforcement-Learned Atomic Skills for Multi-Stage Robotic Manipulation](https://arxiv.org/abs/2611.19324)

**Authors:** Zequan Zeng, Junqin Yang, Kai Wang

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19324) | [PDF](https://arxiv.org/pdf/2611.19324)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in multi-task robotic manipulation. However, they still face limitations in control precision and execution stability during critical manipulation stages, such as object grasping, alignment and insertion. To combine general-purpose manipulation capabilities with task-specific fine-grained control, while enabling effective coordination between generalist and specialized policies throughout multi-stage manipulation tasks, this paper proposes MARS (Modular Atomic-skill Routing System), a dynamic routing framework for reinfo...

</details>

<details>
<summary>Share</summary>

```
MARS: Dynamic Routing of Reinforcement-Learned Atomic Skills for Multi-Stage Robotic Manipulation

Vision-Language-Action (VLA) models have demonstrated strong capabilities in multi-task robotic manipulation.

arXiv: https://arxiv.org/abs/2611.19324

#VLA #robotics
```

</details>

---

### [RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution](https://arxiv.org/abs/2611.19081)

**Authors:** Ran Qi, Yixin Xiao, Dawei Wang, Zhiyuan Li, Jinbang Huang et al. (10 authors)

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19081) | [PDF](https://arxiv.org/pdf/2611.19081)

<details>
<summary>Abstract</summary>

Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities. However, the improvement of such integrated systems remains largely decoupled across their agent and model components, with advances in one component not necessarily benefiting the other, substantially limiting the capabilities of the combined system. As both MLLMs and robotic foundation models become increasingly capable, fully realizing their combined potential calls for co-evolution, an iterative process in which improvements in agents and robotic fou...

</details>

<details>
<summary>Share</summary>

```
RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution

Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities.

arXiv: https://arxiv.org/abs/2611.19081

#VLA #robotics
```

</details>

---

### [Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)

**Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao et al. (11 authors)

**Published:** 2026-11-13 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.18562) | [PDF](https://arxiv.org/pdf/2611.18562)

<details>
<summary>Abstract</summary>

Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the model observes the environment, reasons in a chain of thought, and generates the next end-effector po...

</details>

<details>
<summary>Share</summary>

```
Training Reasoning Models in Simulation to Natively Use Real Robots

Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control.

arXiv: https://arxiv.org/abs/2611.18562

#VLA #robotics
```

</details>

---

### [PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach](https://arxiv.org/abs/2611.15117)

**Authors:** Heng Li, Yang Li, Yifan Duan, Ren Fang, Matao Duan et al. (9 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15117) | [PDF](https://arxiv.org/pdf/2611.15117)

<details>
<summary>Abstract</summary>

Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectories remains challenging because the controller must determine when and how the base should move, and this decision depends on the mounted-arm morphology. We therefore present PolyMorphWBC, a hierarchical controller that takes an EE trajectory...

</details>

<details>
<summary>Share</summary>

```
PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach

Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base.

arXiv: https://arxiv.org/abs/2611.15117

#VLA #robotics
```

</details>

---

### [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397)

**Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang et al. (27 authors)

**Published:** 2026-11-13 | **Categories:** cs.CL, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.18397) | [PDF](https://arxiv.org/pdf/2611.18397)

<details>
<summary>Abstract</summary>

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens of thousands of hours of device-level keyboard and mouse interaction. These trajectories span simulated games and embodied environments, allowing the model to learn environmental dyn...

</details>

<details>
<summary>Share</summary>

```
Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments.

arXiv: https://arxiv.org/abs/2611.18397

#VLA #robotics
```

</details>

---

### [CARE-Drive: Coupled Alternating Refinement for Ego-trajectories](https://arxiv.org/abs/2611.15360)

**Authors:** Xiao Ma, Yijun Chen, Zhiquan Hu, Jicheng Zhao, Ran Ji et al. (7 authors)

**Published:** 2026-11-11 (updated 2026-11-13) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15360) | [PDF](https://arxiv.org/pdf/2611.15360)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving. To further improve the quality of predicted trajectories, existing studies introduce candidate refinement, residual denoising, and token correction. However, these methods typically focus on unified refinement of the entire trajectory, paying limited attention to the distinct physical quantities and their interactions. We further investigate physical specialization and coordination in trajectory refinement, centering on position and heading for simpler and more intuitive cor...

</details>

<details>
<summary>Share</summary>

```
CARE-Drive: Coupled Alternating Refinement for Ego-trajectories

Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving.

arXiv: https://arxiv.org/abs/2611.15360

#VLA #robotics
```

</details>

---

### [Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction](https://arxiv.org/abs/2611.15651)

**Authors:** Miao Pan, Kaixiang Yao, Xiaohe Zhou, Xu Wang, Qinfeng Li et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.15651) | [PDF](https://arxiv.org/pdf/2611.15651)

<details>
<summary>Abstract</summary>

Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable. During execution, actions deviate from intended effects, constrained by the embodiment and environment. An embodied brain must understand why execution deviates, identify what can be reliably realized, and revise decisions using interaction experience. These correspond to causal failure localization, capability-constrained adaptation, and experience-driven revision. Current embodied foundation models largely lack these capabilities....

</details>

<details>
<summary>Share</summary>

```
Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction

Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable.

arXiv: https://arxiv.org/abs/2611.15651

#VLA #robotics
```

</details>

---
