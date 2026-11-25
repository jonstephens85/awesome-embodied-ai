# What's New

Papers discovered in the run at **2026-11-25 00:22 UTC**.

**New this run:** 24

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [World Models as Native Latent Action Models](https://arxiv.org/abs/2611.30898)

**Authors:** Qinyue Li, Weijie Qiao, Qingyi Tao, Zerui Gong, Zhe Yang et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models, World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30898) | [PDF](https://arxiv.org/pdf/2611.30898) | [Project Page](https://pawteam-eai.github.io/native-lam/)

<details>
<summary>Abstract</summary>

Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forward-dynamics models (IDM, FDM) from scratch, trading off pixel reconstruction against latent capacity and accuracy. Pretrained video world models natively generate high-fidelity dynamics, yet represent them densely, entangled across all layers. Viewing the world model as a LAM, we show that these dynamics can be extrac...

</details>

<details>
<summary>Share</summary>

```
World Models as Native Latent Action Models

Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space.

arXiv: https://arxiv.org/abs/2611.30898
Project page: https://pawteam-eai.github.io/native-lam/

#egocentric #robotlearning
```

</details>

---

### [ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild](https://arxiv.org/abs/2611.30597)

**Authors:** Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric human" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30597) | [PDF](https://arxiv.org/pdf/2611.30597) | [Code](https://github.com/NTUYWANG103/ViDiHand)

<details>
<summary>Abstract</summary>

Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion. Recent methods leverage pretrained video diffusion model (VDM) priors to recover occluded hands directly from full-frame videos, but their appearance-based depth regression generalizes poorly to unseen cameras. In this work, we propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth estimation from direct regression into fine-grained geometric constraint solving. Specifically, we introduce Fine-Grained Geometric Lifting and Clip-Level Ray Fitting, which recover metric...

</details>

<details>
<summary>Share</summary>

```
ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild

Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion.

arXiv: https://arxiv.org/abs/2611.30597
Code: https://github.com/NTUYWANG103/ViDiHand

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (15)

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

### [WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2611.31126)

**Authors:** Zien Wang, Yuhao Pan, Yunfeng Fan, Nan Cheng, Xin Xia et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.31126) | [PDF](https://arxiv.org/pdf/2611.31126)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models leverage pretrained vision-language representations for instruction-conditioned robot control, yet their understanding of task-relevant 3D relations and how these relations evolve during manipulation remains largely implicit. To address this challenge, we introduce \textbf{WeaveVLA}, a framework that enhances VLA action generation by explicitly modeling task-relevant relative 3D relations and maintaining relational context across observations. WeaveVLA employs a task-conditioned sparse graph neural network to encode relative 3D relations among objects, the g...

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

## World Models (7)

### [Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting](https://arxiv.org/abs/2611.30573)

**Authors:** ZiAn Wang, Tianyi Wang, Zhihao Chen, Manni Cui, Junkai Chen et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30573) | [PDF](https://arxiv.org/pdf/2611.30573) | [Project Page](https://wangzian828.github.io/PersistWorld) | [Code](https://github.com/wangzian828/PersistWorld)

<details>
<summary>Abstract</summary>

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather than to forecast what will change. We therefore make what the model has seen its state. PersistWorld streams camera frames into a persistent 3D world state anchored in the scene, writ...

</details>

<details>
<summary>Share</summary>

```
Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead.

arXiv: https://arxiv.org/abs/2611.30573
Project page: https://wangzian828.github.io/PersistWorld
Code: https://github.com/wangzian828/PersistWorld

#worldmodels #robotics
```

</details>

---

### [DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2611.30907)

**Authors:** Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30907) | [PDF](https://arxiv.org/pdf/2611.30907) | [Project Page](https://vinaymohan0409.github.io/DexLatentWorld/)

<details>
<summary>Abstract</summary>

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability to previously unseen robot morphologies. We introduce a 3D latent-action world model that learns continuous action representations directly from point-cloud observations of retargeted human manipulation demonstrations. A contrastive objectiv...

</details>

<details>
<summary>Share</summary>

```
DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions.

arXiv: https://arxiv.org/abs/2611.30907
Project page: https://vinaymohan0409.github.io/DexLatentWorld/

#worldmodels #robotics
```

</details>

---

### [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](https://arxiv.org/abs/2611.30714)

**Authors:** Yuxuan Jiang, Zehua Chen, Yusheng Dai, Andong Wang, Weibei Dou et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.SD, cs.CV, cs.MM | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30714) | [PDF](https://arxiv.org/pdf/2611.30714) | [Project Page](https://streamaudio.github.io)

<details>
<summary>Abstract</summary>

Video-to-audio generation synthesizes sound that matches a video in content and timing, with applications ranging from film post-production to live streaming, games and interactive world models. Interactive applications receive video continuously and need the sound to follow it in real time, yet most existing video-to-audio models are bidirectional and must observe an entire clip before producing any sound. We propose LiveAudio, a streaming video-to-audio framework that generates high-quality and synchronized audio in real time while the video is playing. In contrast to prior streaming models...

</details>

<details>
<summary>Share</summary>

```
LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation

Video-to-audio generation synthesizes sound that matches a video in content and timing, with applications ranging from film post-production to live streaming, games and interactive world models.

arXiv: https://arxiv.org/abs/2611.30714
Project page: https://streamaudio.github.io

#worldmodels #robotics
```

</details>

---

### [VeriTouch: Verified Visuo-Tactile World Models that Improve Robot Policy Learning](https://arxiv.org/abs/2611.30572)

**Authors:** Shuxun Wang, Xiaonan Jiang, Zhaoyu Wang, Ziyuan Chu, Xihang Yue et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30572) | [PDF](https://arxiv.org/pdf/2611.30572)

<details>
<summary>Abstract</summary>

Scaling visuo-tactile policy learning is constrained by the high cost of real-world data collection and the difficulty of building realistic simulations. Generative models offer a scalable source of training data, yet useful demonstrations require plausible tactile feedback, temporal alignment with visual contact, and accurate actions. To this end, we present VeriTouch, a framework for generating and verifying synthetic visuo-tactile trajectories for policy learning. Conditioned on initial images and task instructions, our world model, VeriGen, jointly generates high-fidelity dual-view videos...

</details>

<details>
<summary>Share</summary>

```
VeriTouch: Verified Visuo-Tactile World Models that Improve Robot Policy Learning

Scaling visuo-tactile policy learning is constrained by the high cost of real-world data collection and the difficulty of building realistic simulations.

arXiv: https://arxiv.org/abs/2611.30572

#worldmodels #robotics
```

</details>

---

### [Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning](https://arxiv.org/abs/2611.30666)

**Authors:** Yu Zhang, Jingrui Li, Congyu Wang, Yuhang Cheng, Wenbo Chen et al. (8 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30666) | [PDF](https://arxiv.org/pdf/2611.30666)

<details>
<summary>Abstract</summary>

Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified. We introduce Zhengrong (Zhengrong-PoleWM), a world model that decomposes a latent trajectory into an initial-condition anchor, a free response, and delayed responses to action innovations. Nonlinear networks map visual history and causal action prefixes to response coefficients. A shared bank of stable conjugate poles determines how each response evolves with elapsed time. This factorization preserves nonlinear inter...

</details>

<details>
<summary>Share</summary>

```
Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning

Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified.

arXiv: https://arxiv.org/abs/2611.30666

#worldmodels #robotics
```

</details>

---

### [Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?](https://arxiv.org/abs/2611.30836)

**Authors:** Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang, Shou-Po Tsai, Jing-Zhe Huang et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30836) | [PDF](https://arxiv.org/pdf/2611.30836)

<details>
<summary>Abstract</summary>

Embodied vision systems rely on complementary sensors to perceive and act as conditions change. Even models that accept arbitrary sensor subsets can exhibit negative fusion: adding a sensor increases prediction error. We propose MakeSense, a multimodal fusion framework that preserves sensor-specific evidence in private streams and combines information through shared bottleneck tokens. Training pairs full and subset views of the same degraded observations, penalizing higher error with more sensors. Where geometry permits, the distance readout uses range measurements alone, while the rest of the...

</details>

<details>
<summary>Share</summary>

```
Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?

Embodied vision systems rely on complementary sensors to perceive and act as conditions change.

arXiv: https://arxiv.org/abs/2611.30836

#worldmodels #robotics
```

</details>

---

### [ActField: Learning Action Effects as Continuous-Time Latent Dynamics](https://arxiv.org/abs/2611.30659)

**Authors:** Yunpeng Qing, Yuheng Huang, Changxu Wei, Yilun Kong, Yichen Shi et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30659) | [PDF](https://arxiv.org/pdf/2611.30659)

<details>
<summary>Abstract</summary>

Learning how actions change visual states is essential for prediction and decision-making in embodied tasks. Existing action-conditioned JEPA world models typically predict future representations at discrete observation intervals, leaving the temporal evolution of action effects implicit. We introduce ActField, a continuous-time JEPA world model that explicitly models latent state evolution through an action-conditioned vector field integrated over physical time. ActField separates action-independent evolution from action-induced changes, with the latter modulated by the latent context. A refe...

</details>

<details>
<summary>Share</summary>

```
ActField: Learning Action Effects as Continuous-Time Latent Dynamics

Learning how actions change visual states is essential for prediction and decision-making in embodied tasks.

arXiv: https://arxiv.org/abs/2611.30659

#worldmodels #robotics
```

</details>

---
