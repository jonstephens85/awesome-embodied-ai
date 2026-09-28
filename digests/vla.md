# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-09-28 21:35 UTC

**Papers shown:** 55 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models](https://arxiv.org/abs/2609.28865)

**Authors:** Yufei Duan, Hang Yin, Alberta Longhini, Chao Tang, Danica Kragic

**Published:** 2026-09-24 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28865) | [PDF](https://arxiv.org/pdf/2609.28865) | [Project Page](https://vla-dsd.github.io/)

<details>
<summary>Abstract</summary>

Action representation plays a central role in discrete-token vision-language-action (VLA) learning but remains underexamined. Under conventional pose-increment representations, action tokens are sensitive to execution speed and dataset-specific normalization, potentially obscuring geometric structure shared across demonstrations and datasets. We introduce Direction-Scale Decomposition (DSD), an action representation that decomposes translation and rotation increments into direction and scale components before tokenization. DSD isolates motion direction while retaining magnitudes in separate sc...

</details>

<details>
<summary>Share</summary>

```
Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models

Action representation plays a central role in discrete-token vision-language-action (VLA) learning but remains underexamined.

arXiv: https://arxiv.org/abs/2609.28865
Project page: https://vla-dsd.github.io/

#VLA #robotics
```

</details>

---

### [TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](https://arxiv.org/abs/2609.28314)

**Authors:** Samrat Sahoo, Liang Ji, Tom Silver, Yixuan Huang

**Published:** 2026-09-23 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28314) | [PDF](https://arxiv.org/pdf/2609.28314) | [Project Page](https://prpl-group.com/tandem/)

<details>
<summary>Abstract</summary>

Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present TANDEM (Tamp with As-Needed Demonstrations for Efficient Model fine-tuning), a system that combines TAMP with selective human teleoperation to collect demonstrations for tasks beyond the planner's capabilities. Our key idea is to represent...

</details>

<details>
<summary>Share</summary>

```
TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models.

arXiv: https://arxiv.org/abs/2609.28314
Project page: https://prpl-group.com/tandem/

#VLA #robotics
```

</details>

---

### [MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence](https://arxiv.org/abs/2609.25627)

**Authors:** Haoran Wen, Wenfu Wang, Kunsong Shi, Jingke Wang, Wancheng Feng et al. (18 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; code repo

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25627) | [PDF](https://arxiv.org/pdf/2609.25627) | [Project Page](https://machembodied.com/ME-U/ME-U0.html) | [Code](https://github.com/MachEmbodied/ME-U0)

<details>
<summary>Abstract</summary>

General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unified embodied foundation model connecting understanding and generation experts through a Mixture-of-Tr...

</details>

<details>
<summary>Share</summary>

```
MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence

General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions.

arXiv: https://arxiv.org/abs/2609.25627
Project page: https://machembodied.com/ME-U/ME-U0.html
Code: https://github.com/MachEmbodied/ME-U0

#VLA #robotics
```

</details>

---

### [VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2609.25376)

**Authors:** Jiuyi Xu, Qing Jin, Meida Chen, Song Wang, Yang Sui et al. (6 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25376) | [PDF](https://arxiv.org/pdf/2609.25376) | [Code](https://github.com/jiuyixu25/VLAQuantBench)

<details>
<summary>Abstract</summary>

Post-training quantization reduces the memory requirements of vision-language-action (VLA) models, but precision selection must account for the interaction between layer scope, numerical format, and calibration. We introduce \textbf{VLAQuantBench}, a controlled evaluation with 409 runs and 94,574 simulation episodes: four models on LIBERO, with X-VLA additionally evaluated on three simulation benchmark families. Under uncalibrated W4A4 round-to-nearest quantization, expanding a $π_{0.5}$ action-head subset from 126 to 167 layers raises success from 7.0\% to 70.5\%. Fixed-observation replay con...

</details>

<details>
<summary>Share</summary>

```
VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models

Post-training quantization reduces the memory requirements of vision-language-action (VLA) models, but precision selection must account for the interaction between layer scope, numerical format, and calibration.

arXiv: https://arxiv.org/abs/2609.25376
Code: https://github.com/jiuyixu25/VLAQuantBench

#VLA #robotics
```

</details>

---

### [Self-Adaptive VLA for Robust Robot Deployment](https://arxiv.org/abs/2609.30092)

**Authors:** Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang, Zhenjia Xu, Chuang Gan

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.30092) | [PDF](https://arxiv.org/pdf/2609.30092) | [Project Page](https://icefoxzhx.github.io/self-adaptive-vla)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models demonstrate impressive capabilities in robotic manipulation, their memoryless nature renders them brittle to test-time environment shifts, particularly hardware shifts caused by wear or imperfect calibration. Enabling these models to self-adapt during deployment without requiring continuous on-site recalibration remains a critical bottleneck for real-world scalability. In this work, we introduce Self-Adaptive VLA, a novel post-training recipe that enables the policy to iteratively adapt to deployment-time hardware shifts leveraging its own rollouts as...

</details>

<details>
<summary>Share</summary>

```
Self-Adaptive VLA for Robust Robot Deployment

While Vision-Language-Action (VLA) models demonstrate impressive capabilities in robotic manipulation, their memoryless nature renders them brittle to test-time environment shifts, particularly hardware shifts caused...

arXiv: https://arxiv.org/abs/2609.30092
Project page: https://icefoxzhx.github.io/self-adaptive-vla

#VLA #robotics
```

</details>

---

### [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](https://arxiv.org/abs/2609.26313)

**Authors:** Zeyu Lou, Tianran Zhang, Xinquan Yue, Ya Jing, Chenyang Si

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.26313) | [PDF](https://arxiv.org/pdf/2609.26313) | [Code](https://github.com/Loule0-0/SafeLoop)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models are promising for general-purpose manipulation, but long-horizon execution remains fragile. Small state-estimation or control errors can lead to irreversible failures (e.g., collisions and object drops). Avoiding these risks requires a proactive safety mechanism capable of anticipating hazards. In this paper, we introduce SafeLoop, a non-invasive external wrapper that adds hazard prediction and rollback-based recovery to a VLA model without changing its parameters. SafeLoop trains a risk predictor from vision and proprioception to output four values:...

</details>

<details>
<summary>Share</summary>

```
SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

Recent vision-language-action (VLA) models are promising for general-purpose manipulation, but long-horizon execution remains fragile.

arXiv: https://arxiv.org/abs/2609.26313
Code: https://github.com/Loule0-0/SafeLoop

#VLA #robotics
```

</details>

---

### [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)

**Authors:** Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, Xiaoyang Li, Zhangkai Wu et al. (10 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25562) | [PDF](https://arxiv.org/pdf/2609.25562) | [Code](https://github.com/xiaoqi-7/IndustrialVLA-Bench)

<details>
<summary>Abstract</summary>

Open robot policies increasingly follow two paradigms: vision-language-action models (VLAs) directly map observations and instructions to actions, whereas world-action models (WAMs) incorporate learned video or world dynamics into policy learning or action generation. Although both target the same manipulation tasks and represent alternative design choices, they are commonly reported under different evaluation protocols, leaving their capability, robustness, language sensitivity, and deployment-cost trade-offs unclear. We present IndustrialVLA-Bench, an evidence-aware evaluation of six release...

</details>

<details>
<summary>Share</summary>

```
IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models

Open robot policies increasingly follow two paradigms: vision-language-action models (VLAs) directly map observations and instructions to actions, whereas world-action models (WAMs) incorporate learned video or world...

arXiv: https://arxiv.org/abs/2609.25562
Code: https://github.com/xiaoqi-7/IndustrialVLA-Bench

#VLA #robotics
```

</details>

---

### [Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies](https://arxiv.org/abs/2609.24682)

**Authors:** Trung Dao, Sankalp Yamsani, Jaden Park, Joohyung Kim, Yong Jae Lee

**Published:** 2026-09-21 (updated 2026-09-22) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24682) | [PDF](https://arxiv.org/pdf/2609.24682) | [Project Page](https://thaw-vla.trung-dt.com/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map observations to actions with no objective that accounts for how the world responds, so their robustness is bounded primarily by data coverage. World models carry precisely that missing objective and are better grounded for it, yet rolling the future forward costs seconds per decision and rules them out of the control loop. We show the two can be separated. What a world model knows about physical scenes lives in its internal features; generating the future is merely the objective that produced them, so the grounding can be inherited while the generative m...

</details>

<details>
<summary>Share</summary>

```
Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies

Vision-Language-Action (VLA) models map observations to actions with no objective that accounts for how the world responds, so their robustness is bounded primarily by data coverage.

arXiv: https://arxiv.org/abs/2609.24682
Project page: https://thaw-vla.trung-dt.com/

#VLA #robotics
```

</details>

---

### [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](https://arxiv.org/abs/2609.24350)

**Authors:** Huiqiong Li, Zhiting Mei, Anirudha Majumdar, Jingjing Chen, Yu-Gang Jiang et al. (6 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24350) | [PDF](https://arxiv.org/pdf/2609.24350) | [Project Page](https://huiqiongli.github.io/LIBERO-VPro/)

<details>
<summary>Abstract</summary>

Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution. We introduce LIBERO-VPro, a benchmark for systematically evaluating the closed-loop visual robustness of robotic foundation models by perturbing the visual evidence available during execution. LIBERO-VPro covers four complementary dimensions, including Visual Evidence Degradation, Camera Staleness, Visual Source Consistency, and Task-Relevant Scene Variation, spanning 12 challenge categories,...

</details>

<details>
<summary>Share</summary>

```
LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models

Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution.

arXiv: https://arxiv.org/abs/2609.24350
Project page: https://huiqiongli.github.io/LIBERO-VPro/

#VLA #robotics
```

</details>

---

### [CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies](https://arxiv.org/abs/2609.24118)

**Authors:** Junlan Xiao, Junwei Jiang, Zaibin Zhang, Yifan Wang, Zhongbo Zhang et al. (7 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24118) | [PDF](https://arxiv.org/pdf/2609.24118) | [Code](https://github.com/xiaojunlan/care)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies achieve strong performance in robotic manipulation but remain brittle once execution deviates from nominal trajectories. We propose CARE (Corrective Atomic Robotic Execution), a framework that improves recovery by learning from failures encountered during execution. Instead of generating corrective data from manually designed or random perturbations, CARE collects failed rollouts, models stage-conditioned post-failure deviations, and uses the resulting empirical distributions to synthesize representative failure states and corrective demonstrations. At inf...

</details>

<details>
<summary>Share</summary>

```
CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies

Vision-Language-Action (VLA) policies achieve strong performance in robotic manipulation but remain brittle once execution deviates from nominal trajectories.

arXiv: https://arxiv.org/abs/2609.24118
Code: https://github.com/xiaojunlan/care

#VLA #robotics
```

</details>

---

### [FoldQuantVLA: Native Low-Bit Quantization of Vision-Language-Action Models via Consistent Folding](https://arxiv.org/abs/2609.24433)

**Authors:** Hung T. Ho, Khanh D. Nguyen, Quang D. Nguyen, Thanh Q. Duong, Ngan Le et al. (8 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24433) | [PDF](https://arxiv.org/pdf/2609.24433) | [Code](https://github.com/cair-vinuni/FoldQuantVLA)

<details>
<summary>Abstract</summary>

Low-bit vision-language-action inference must reduce observation-to-action latency while preserving robot behavior. We present FoldQuantVLA, a post-training quantization framework that carries a consistent activation representation through calibration, weight rounding, and native integer execution. It combines channel scaling and block Hadamard transforms with dynamic per-token quantization, without policy retraining. Custom TensorRT plugins execute projections in both the language backbone and iterative action expert with four-bit weights and activations (W4A4) on Ada GPUs and Jetson AGX Orin...

</details>

<details>
<summary>Share</summary>

```
FoldQuantVLA: Native Low-Bit Quantization of Vision-Language-Action Models via Consistent Folding

Low-bit vision-language-action inference must reduce observation-to-action latency while preserving robot behavior.

arXiv: https://arxiv.org/abs/2609.24433
Code: https://github.com/cair-vinuni/FoldQuantVLA

#VLA #robotics
```

</details>

---

### [Towards VLA-Dreamer: Refining VLA Behavior Using World Models](https://arxiv.org/abs/2609.31313)

**Authors:** Parsa Mastouri Kashani, Jan-Gerrit Habekost, Stefan Wermter

**Published:** 2026-09-25 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2609.31313) | [PDF](https://arxiv.org/pdf/2609.31313)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data. Moreover, the absence of an explicit world model casts further doubt on their control capabilities. In this concept paper, we propose a novel architecture that addresses sample efficiency in VLAs by training a predictive world model on the embedding space of the VLA's vision encoder. We hypothesize that these embeddings are action-relevant and usable for future prediction. To this end, we propose using the suggested architecture to investigate...

</details>

<details>
<summary>Share</summary>

```
Towards VLA-Dreamer: Refining VLA Behavior Using World Models

Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data.

arXiv: https://arxiv.org/abs/2609.31313

#VLA #robotics
```

</details>

---

### [VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL](https://arxiv.org/abs/2609.30868)

**Authors:** Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30868) | [PDF](https://arxiv.org/pdf/2609.30868)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction. Residual reinforcement learning (RL) can correct such errors while keeping the VLA frozen, but real-robot RL is costly and safety-critical. We propose VLA Latent-Conditioned RL (VLaRL), which enables residual RL for frozen VLAs to be trained in simulation and deployed on real robots without real-world RL or online adaptation. The key challenge is transferring the learned residual policy despite the visual gap betwe...

</details>

<details>
<summary>Share</summary>

```
VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction.

arXiv: https://arxiv.org/abs/2609.30868

#VLA #robotics
```

</details>

---

### [Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2609.30833)

**Authors:** Chuanliang Xie, Boyu Ma, Gen Li, Yizhou Liu, Houwang Chen et al. (7 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30833) | [PDF](https://arxiv.org/pdf/2609.30833)

<details>
<summary>Abstract</summary>

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions. This hierarchical design has practical value only if the planner can generate plans fast enough to meet real-time control requirements, and the resulting plans actually contribute to the generation of action. We study one such system, a waypoint hierarchy pipeline adapted from $π_{0.5}$, and find that neither requirement is satisfied. This baseline relies on token-level autoregressive decoding (Token-AR) to generate a waypoint plan,...

</details>

<details>
<summary>Share</summary>

```
Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions.

arXiv: https://arxiv.org/abs/2609.30833

#VLA #robotics
```

</details>

---

### [LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion](https://arxiv.org/abs/2609.28431)

**Authors:** Ning Chen, Yankai Fu, Junkai Zhao, Qianpu Sun, Guocai Yao et al. (8 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.28431) | [PDF](https://arxiv.org/pdf/2609.28431) | [Project Page](https://ccdcs.github.io/LiMA_repo/)

<details>
<summary>Abstract</summary>

Dexterous manipulation demands long-term foresight and rapid reactive control. Vision-Language-Action (VLA) models, while proficient in high-level reasoning, often lack a fine-grained understanding of physical dynamics and spatial perception. Conversely, World-Action Models (WAMs) typically suffer from high inference latency due to iterative generation. These deficiencies result in a critical temporal misalignment where the model's intent fails to adapt to rapid physical contact changes. To overcome this fundamental bottleneck, we propose LiMA, an asynchronous dual-system generative framework...

</details>

<details>
<summary>Share</summary>

```
LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion

Dexterous manipulation demands long-term foresight and rapid reactive control.

arXiv: https://arxiv.org/abs/2609.28431
Project page: https://ccdcs.github.io/LiMA_repo/

#VLA #robotics
```

</details>

---

### [Less Language, More Latents: Annotation-Efficient VLAs for Driving](https://arxiv.org/abs/2609.27747)

**Authors:** Alexey Zakharov, Kemal Oksuz, Puneet K. Dokania

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.27747) | [PDF](https://arxiv.org/pdf/2609.27747)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLA) promise human-steerable autonomous driving, but their training is bottlenecked by the scarcity of frames paired with natural-language instructions: while camera streams and expert trajectories are logged at scale, language annotations (e.g., turn left at the intersection) remain scarce and expensive to acquire. To address this challenge, we introduce Latent Action Driving Annotations (LADA), a three-stage pipeline that transforms abundant unlabelled observation-trajectory pairs into a substrate for language-conditioned control. First, we train a latent actio...

</details>

<details>
<summary>Share</summary>

```
Less Language, More Latents: Annotation-Efficient VLAs for Driving

Vision-language-action models (VLA) promise human-steerable autonomous driving, but their training is bottlenecked by the scarcity of frames paired with natural-language instructions: while camera streams and expert t...

arXiv: https://arxiv.org/abs/2609.27747

#VLA #robotics
```

</details>

---

### [BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models](https://arxiv.org/abs/2609.27450)

**Authors:** Weihui Zhao, Xiaohan Yan, Zunian Wan, Xuan Du, Zhaozhan Chi et al. (17 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.27450) | [PDF](https://arxiv.org/pdf/2609.27450)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models handle long-horizon manipulation, yet success hinges on a few precision-critical phases where millimeter-scale errors undo all prior progress. Online reinforcement learning (RL) can optimize exactly these actions, but free exploration is far too costly on real robots, which makes human corrections indispensable. However, existing online RL methods for VLAs either cannot incorporate such corrections or fold them into undifferentiated supervision. Yet human corrections are not uniformly noisy but reliable along some action dimensions and variable along others....

</details>

<details>
<summary>Share</summary>

```
BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models

Vision-language-action (VLA) models handle long-horizon manipulation, yet success hinges on a few precision-critical phases where millimeter-scale errors undo all prior progress.

arXiv: https://arxiv.org/abs/2609.27450

#VLA #robotics
```

</details>

---

### [Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation](https://arxiv.org/abs/2609.26672)

**Authors:** Hao Wei, Yang Liu, Chao Tang, Shengbao Li, Jiangtao Chen et al. (10 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.26672) | [PDF](https://arxiv.org/pdf/2609.26672) | [Project Page](https://varepsilon4p.github.io/)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) models for high-precision manipulation typically requires task-specific, high-quality data (e.g., teleoperation), which is slow and expensive to collect. To reduce this burden without compromising manipulation precision, we propose $\varepsilon$4P (Imperfection for Precision), a simple yet effective method that "upcycles" two otherwise discarded data sources: (1) low-precision data from the target task and (2) high-precision data from mismatched tasks. Rather than naively mixing these imperfect data sources throughout co-training, $\varepsilon$4P controls...

</details>

<details>
<summary>Share</summary>

```
Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation

Training vision-language-action (VLA) models for high-precision manipulation typically requires task-specific, high-quality data (e.g., teleoperation), which is slow and expensive to collect.

arXiv: https://arxiv.org/abs/2609.26672
Project page: https://varepsilon4p.github.io/

#VLA #robotics
```

</details>

---

### [Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2609.25820)

**Authors:** Yuxin Yang, Gaohan He, Changxue Guan, Hangming Liu

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.25820) | [PDF](https://arxiv.org/pdf/2609.25820)

<details>
<summary>Abstract</summary>

Discrete action tokenization is central to autoregressive vision-language-action (VLA) models, yet action representations are often evaluated primarily through reconstruction fidelity. We ask which representation properties actually matter for closed-loop control by comparing fixed analytical, data-driven linear, and nonlinear neural representations under a unified tokenization interface. Across rate-distortion analysis, sequence-modeling diagnostics, and 3,500 LIBERO rollouts, representation rankings change with the evaluation criterion. PCA achieves lower nominal reconstruction error than Te...

</details>

<details>
<summary>Share</summary>

```
Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models

Discrete action tokenization is central to autoregressive vision-language-action (VLA) models, yet action representations are often evaluated primarily through reconstruction fidelity.

arXiv: https://arxiv.org/abs/2609.25820

#VLA #robotics
```

</details>

---

### [Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D](https://arxiv.org/abs/2609.24525)

**Authors:** Haoxuan Li, Sixu Yan, Lianghui Zhu, Xuanlai Tang, Shikang Wang et al. (6 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.24525) | [PDF](https://arxiv.org/pdf/2609.24525)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated remarkable generalization in robotic manipulation via large-scale multimodal pretraining. However, VLA models are mainly trained on 2D-centric observations, which inherently constrains their capacity for precise spatial manipulation. Previous methods enhance 3D awareness by introducing implicit spatial priors, but still lack explicit geometry guidance. In this paper, we propose Bridge3D that integrates both implicit and explicit 3D geometry guidance into pre-trained 2D VLA models, enabling them to ''see'' and ''act'' in 3D. Bridge3D introdu...

</details>

<details>
<summary>Share</summary>

```
Bridge3D: Enabling Vision-Language-Action Models to See and Act in 3D

Vision-Language-Action (VLA) models have demonstrated remarkable generalization in robotic manipulation via large-scale multimodal pretraining.

arXiv: https://arxiv.org/abs/2609.24525

#VLA #robotics
```

</details>

---

### [ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation](https://arxiv.org/abs/2609.24124)

**Authors:** Yibo Li, Enshen Zhou, Rui Chen, Yanjun Ding, Mengzhen Liu et al. (10 authors)

**Published:** 2026-09-21 (updated 2026-09-23) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.24124) | [PDF](https://arxiv.org/pdf/2609.24124) | [Project Page](https://leeibo.github.io/ActiveArena)

<details>
<summary>Abstract</summary>

Active perception and manipulation are crucial for robots to interact with complex scenes. Existing benchmarks struggle to evaluate how robots effectively acquire and maintain information in memory in an active manner. To this end, we introduce ActiveArena-Sim, an active-perception simulator with controllable viewpoints and large-scale workspaces as the foundation. Built on this, we propose ActiveArena-Bench, which comprises 35 tasks across 5 fine-grained categories, covering visual exploration and interactive information acquisition. Each task is difficult to solve from passive observations a...

</details>

<details>
<summary>Share</summary>

```
ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation

Active perception and manipulation are crucial for robots to interact with complex scenes.

arXiv: https://arxiv.org/abs/2609.24124
Project page: https://leeibo.github.io/ActiveArena

#VLA #robotics
```

</details>

---

### [The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996)

**Authors:** Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto, SooJean Han

**Published:** 2026-09-25 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30996) | [PDF](https://arxiv.org/pdf/2609.30996)

<details>
<summary>Abstract</summary>

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an additional challenge. Unlike semantic attributes commonly studied in LLMs, such as gender or language, a physical quantity of interest (QoI) in a VLA evolves jointly with the system dynamics: the representation influences the actions selected...

</details>

<details>
<summary>Share</summary>

```
The Linear Representation Hypothesis for Vision-Language-Action Models

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs).

arXiv: https://arxiv.org/abs/2609.30996

#VLA #robotics
```

</details>

---

### [X-Planner: Event-Structured Task Planning for Embodied Intelligence](https://arxiv.org/abs/2609.25187)

**Authors:** Howard Lu, Shalfun Li, Porter Pan, Cris, Lumen et al. (32 authors)

**Published:** 2026-09-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25187) | [PDF](https://arxiv.org/pdf/2609.25187) | [Code](https://github.com/X-Square-Robot/Xplanner)

<details>
<summary>Abstract</summary>

Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, and teleoperation under a hierarchy granularity with source-dependent annotation depth. Takeover-time...

</details>

<details>
<summary>Share</summary>

```
X-Planner: Event-Structured Task Planning for Embodied Intelligence

Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit.

arXiv: https://arxiv.org/abs/2609.25187
Code: https://github.com/X-Square-Robot/Xplanner

#VLA #robotics
```

</details>

---

### [Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048)

**Authors:** Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.31048) | [PDF](https://arxiv.org/pdf/2609.31048)

<details>
<summary>Abstract</summary>

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation. However, such pipelines typically retain successful demonstrations while failed rollouts are discarded, even though they expose precisely the off-nominal states from which recovery must be learned. We introduce Kintsugi-VLA, a framework for converting failed rollouts into targeted synthetic recovery data by exploiting exact state restoration and branching in simulation. For a fixed...

</details>

<details>
<summary>Share</summary>

```
Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation.

arXiv: https://arxiv.org/abs/2609.31048

#VLA #robotics
```

</details>

---

### [Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies](https://arxiv.org/abs/2609.30913)

**Authors:** Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30913) | [PDF](https://arxiv.org/pdf/2609.30913)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state. We study instruction switching, where a new task is issued during or after the execution of a different one. We observe that a target task that is reliably completed from its standard initial states can become inaccessible from states produced by a preceding task. We call such states task islands. We propose Causeway, a training-free inference-time intervention. Given the current state and a re-entry pose for the ta...

</details>

<details>
<summary>Share</summary>

```
Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state.

arXiv: https://arxiv.org/abs/2609.30913

#VLA #robotics
```

</details>

---

### [Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs](https://arxiv.org/abs/2609.29382)

**Authors:** Riccardo Andrea Izzo, Rimvydas Rubavicius, Gianluca Bardaro, Subramanian Ramamoorthy, Matteo Matteucci et al. (6 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.29382) | [PDF](https://arxiv.org/pdf/2609.29382)

<details>
<summary>Abstract</summary>

Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions. While these models exhibit impressive capabilities, due to their very high number of parameters, their computational requirements are often prohibitive for robotics control. To mitigate these inefficiencies, existing methods predominantly skip VLM backbone layers with early exits or reduce denoising steps, while leaving action expert depth untouc...

</details>

<details>
<summary>Share</summary>

```
Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs

Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that g...

arXiv: https://arxiv.org/abs/2609.29382

#VLA #robotics
```

</details>

---

### [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](https://arxiv.org/abs/2609.29204)

**Authors:** Junyi Tang, Jie Peng, Zezhen Ding, Yuan Shen, Tianlong Chen

**Published:** 2026-09-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.29204) | [PDF](https://arxiv.org/pdf/2609.29204)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models offer strong local control and instruction following but often struggle with long-horizon tasks requiring persistent memory and planning. Task harnesses provide persistent context for agent reasoning by retaining task history and tracking progress across execution stages. To bring these complementary capabilities together, we introduce AdaHVLA, an adaptive harness that refines code-based coordination policies through robot experience to better align agent reasoning and memory with VLA execution. Its decoupled multiagent adaptation process separates evidence...

</details>

<details>
<summary>Share</summary>

```
AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution

Vision-language-action (VLA) models offer strong local control and instruction following but often struggle with long-horizon tasks requiring persistent memory and planning.

arXiv: https://arxiv.org/abs/2609.29204

#VLA #robotics
```

</details>

---

### [Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy](https://arxiv.org/abs/2609.28838)

**Authors:** Mehmet Turan Yardımcı, Yunus Emre Çoğurcu

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.28838) | [PDF](https://arxiv.org/pdf/2609.28838)

<details>
<summary>Abstract</summary>

Online reinforcement learning fine-tuning of pretrained flow-matching vision-language-action (VLA) policies promises robots that keep learning after deployment, but continued updates often destroy competence on individual tasks while the aggregate still looks healthy. We study this failure mode, which we call task collapse, under a matched small-compute budget on LIBERO-10 with a 450M-parameter SmolVLA policy trained by PPO with stochastic (SDE) sampling. Three exploration-noise policies differ in one live variable: a fixed noise scale, a ReinFlow-style learned noise network, and an uncertaint...

</details>

<details>
<summary>Share</summary>

```
Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy

Online reinforcement learning fine-tuning of pretrained flow-matching vision-language-action (VLA) policies promises robots that keep learning after deployment, but continued updates often destroy competence on indivi...

arXiv: https://arxiv.org/abs/2609.28838

#VLA #robotics
```

</details>

---

### [Dissecting Advantage-Guided Post-Training for Vision-Language-Action Policies](https://arxiv.org/abs/2609.28161)

**Authors:** Jiahang Cao, Hanye Zhao, Hang Lai, Shenyu Zhang, Xiaoshen Han et al. (13 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.28161) | [PDF](https://arxiv.org/pdf/2609.28161)

<details>
<summary>Abstract</summary>

Advantage-guided reinforcement learning provides a practical way to post-train vision-language-action (VLA) policies using limited robot data. However, its performance depends on several coupled choices, including how critic-derived advantages are constructed, calibrated, and used for policy training. Existing recipes often combine these choices into a single end-to-end procedure, making their individual effects difficult to identify. In this work, we dissect advantage-guided VLA post-training through a controlled empirical study that separates these design choices while accounting for their d...

</details>

<details>
<summary>Share</summary>

```
Dissecting Advantage-Guided Post-Training for Vision-Language-Action Policies

Advantage-guided reinforcement learning provides a practical way to post-train vision-language-action (VLA) policies using limited robot data.

arXiv: https://arxiv.org/abs/2609.28161

#VLA #robotics
```

</details>

---

### [Latent evolving World Action Model](https://arxiv.org/abs/2609.27455)

**Authors:** Xueji Fang, Boqiang Duan, Hua Wu, Jingdong Wang, Guo-Jun Qi

**Published:** 2026-09-23 (updated 2026-09-24) | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.27455) | [PDF](https://arxiv.org/pdf/2609.27455) | [Code](https://github.com/XuejiFang/LeWAM)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) jointly model action generation and environment dynamics and are mostly built on pretrained Video Diffusion Models (VDMs). In VDM-based WAMs, observations are first encoded by a VAE, and the resulting compressed latents are then processed by large video diffusion backbones to extract effective features for action generation. However, this paradigm ties WAM performance and training cost to large-scale video generation pretraining, limiting WAM efficiency and scalability. In this paper, we theoretically and empirically investigate how visual representations affect acti...

</details>

<details>
<summary>Share</summary>

```
Latent evolving World Action Model

World Action Models (WAMs) jointly model action generation and environment dynamics and are mostly built on pretrained Video Diffusion Models (VDMs).

arXiv: https://arxiv.org/abs/2609.27455
Code: https://github.com/XuejiFang/LeWAM

#VLA #robotics
```

</details>

---

### [MemBodied: Recurrent Associative Memory for Vision-Language-Action Models](https://arxiv.org/abs/2609.28256)

**Authors:** Tej Deep Pala, Navonil Majumder, Bryce Goh, Raphael Yee, Jianfei Yang et al. (7 authors)

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.28256) | [PDF](https://arxiv.org/pdf/2609.28256)

<details>
<summary>Abstract</summary>

Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation. This limitation is consequential in history-dependent manipulation tasks that depend on information available only in past observations. Retaining past observations in context can aid in recovering this information, but at the significant cost of ever-growing, bloated context and inference latency. We thus introduce MemBodied, a fixed-size episodic memory with two complementary compone...

</details>

<details>
<summary>Share</summary>

```
MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation.

arXiv: https://arxiv.org/abs/2609.28256

#VLA #robotics
```

</details>

---

### [HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery](https://arxiv.org/abs/2609.25558)

**Authors:** Jinu Pahk, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm et al. (7 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2609.25558) | [PDF](https://arxiv.org/pdf/2609.25558)

<details>
<summary>Abstract</summary>

Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. Offline frame pairs define a nominal 0.5-second prediction horizon; future observations are used onl...

</details>

<details>
<summary>Share</summary>

```
HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery

Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation.

arXiv: https://arxiv.org/abs/2609.25558

#VLA #robotics
```

</details>

---

### [RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy](https://arxiv.org/abs/2609.26467)

**Authors:** Chongyu Zhu, Jaden Hinds, Hyegang Kim, Juan Sebastian Rojas, Ramy Elmallah et al. (6 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.26467) | [PDF](https://arxiv.org/pdf/2609.26467)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide broad manipulation competence, but often struggle during the precision-critical stages that dominate contact-rich industrial tasks such as connector insertion and cable management. A common remedy is to refine a pretrained VLA with reinforcement learning (RL), enabling task-specific improvement beyond behavior cloning. However, how to preserve its generalist behavior while deciding when RL refinement is needed and which specialized policy should act remains an open question. In this work, we present RouteRLT, a routing framework that learns when and...

</details>

<details>
<summary>Share</summary>

```
RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy

Vision-language-action (VLA) models provide broad manipulation competence, but often struggle during the precision-critical stages that dominate contact-rich industrial tasks such as connector insertion and cable mana...

arXiv: https://arxiv.org/abs/2609.26467

#VLA #robotics
```

</details>

---

### [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](https://arxiv.org/abs/2609.25756)

**Authors:** Junjie Xie, Chuxuan He, Angen Ye, Yujia Song, Dapeng Zhang

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.25756) | [PDF](https://arxiv.org/pdf/2609.25756)

<details>
<summary>Abstract</summary>

Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-age...

</details>

<details>
<summary>Share</summary>

```
MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation

Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints.

arXiv: https://arxiv.org/abs/2609.25756

#VLA #robotics
```

</details>

---

### [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](https://arxiv.org/abs/2609.25636)

**Authors:** Chang Guo, Yukun Xie, Bohan Tan, Zheng Chang, Zhaokai Yin et al. (9 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.25636) | [PDF](https://arxiv.org/pdf/2609.25636) | [Code](https://github.com/AutoLab-SAI-SJTU/RoboFollow)

<details>
<summary>Abstract</summary>

Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically distinct task branches, making vision alone insufficient and forcing reliance on language. (2) Hierarchi...

</details>

<details>
<summary>Share</summary>

```
RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest.

arXiv: https://arxiv.org/abs/2609.25636
Code: https://github.com/AutoLab-SAI-SJTU/RoboFollow

#VLA #robotics
```

</details>

---

### [MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection](https://arxiv.org/abs/2609.26520)

**Authors:** Yichuan Yu, Youzhuo Wang, Yiming Ren, Di Feng, Yexuan Yang et al. (9 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.26520) | [PDF](https://arxiv.org/pdf/2609.26520) | [Project Page](https://yerik-yu.github.io/MATE/)

<details>
<summary>Abstract</summary>

Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed operators to simultaneously control whole-body humanoids in a shared physics-based environment. MATE re...

</details>

<details>
<summary>Share</summary>

```
MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection

Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills.

arXiv: https://arxiv.org/abs/2609.26520
Project page: https://yerik-yu.github.io/MATE/

#VLA #robotics
```

</details>

---

### [StenoVLA-3D: 3D-Aware Reasoning VLA for Navigation Through Gastrointestinal Stenoses](https://arxiv.org/abs/2609.24187)

**Authors:** Tamima Tabassum, Yiming Huang, Tianchun Wu, Changjing Liu, Zhiqing Tang et al. (10 authors)

**Published:** 2026-09-21 (updated 2026-09-22) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.24187) | [PDF](https://arxiv.org/pdf/2609.24187)

<details>
<summary>Abstract</summary>

Autonomous endoscopic navigation requires the policy model to predict actions from texture-poor monocular observations, make safe control decisions, and retain evidence of lesions after they leave the field of view. Existing vision-language-action (VLA) models primarily rely on visual appearance and short-term context, limiting geometric grounding and episode-level reporting. We introduce StenoVLA-3D, a 3D-aware VLA framework for navigating through stenotic regions. We integrate point-maps into the Cosmos-Reason 2 backbone through learned geometry-gated fusion, and also propose a temporal stat...

</details>

<details>
<summary>Share</summary>

```
StenoVLA-3D: 3D-Aware Reasoning VLA for Navigation Through Gastrointestinal Stenoses

Autonomous endoscopic navigation requires the policy model to predict actions from texture-poor monocular observations, make safe control decisions, and retain evidence of lesions after they leave the field of view.

arXiv: https://arxiv.org/abs/2609.24187

#VLA #robotics
```

</details>

---

### [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](https://arxiv.org/abs/2609.24033)

**Authors:** Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang

**Published:** 2026-09-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2609.24033) | [PDF](https://arxiv.org/pdf/2609.24033)

<details>
<summary>Abstract</summary>

Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences. Existing noise-space reinforcement learning efficiently steers a frozen Vision-Language-Action (VLA) policy, but its critics largely ignore these consequences. We present Imagine-RL, which augments noise-space VLA post-training with action-conditioned visual-torque imagination. For each candidate action chunk, a frozen visual-torque latent world model (VTLWM) autoregressively predicts compact future representations without pixel reconstruction. A cu...

</details>

<details>
<summary>Share</summary>

```
Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning

Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences.

arXiv: https://arxiv.org/abs/2609.24033

#VLA #robotics
```

</details>

---

### [Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2609.23968)

**Authors:** Fukang Liu, Yipu Chen, Jaehwi Jang, Danfei Xu, Zsolt Kira et al. (6 authors)

**Published:** 2026-09-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.23968) | [PDF](https://arxiv.org/pdf/2609.23968)

<details>
<summary>Abstract</summary>

Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely on whole-body controllers focused on motion tracking, with limited explicit reasoning or control of interaction forces. This limitation is particularly relevant in contact-rich tasks, where geometrically similar motions may require differe...

</details>

<details>
<summary>Share</summary>

```
Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces.

arXiv: https://arxiv.org/abs/2609.23968

#VLA #robotics
```

</details>

---

### [VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control](https://arxiv.org/abs/2609.30709)

**Authors:** Kemou Jiang, Maonan Wang, Xingchen Zou, Jiayue Zhu, Yuhang Fu et al. (9 authors)

**Published:** 2026-09-25 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30709) | [PDF](https://arxiv.org/pdf/2609.30709)

<details>
<summary>Abstract</summary>

Traffic signal control (TSC) is essential for mitigating urban congestion. Recent advances in vision-language models (VLMs) enable richer interpretation of intersection scenes, opening new opportunities for visual-context-aware TSC. However, the loose coupling and repeated information conversion between modules can lead to the loss of fine-grained visual details, while sequential inference introduces substantial latency. To address these limitations, we propose VLALight, a lightweight end-to-end vision-language-action framework that directly maps intersection observations and signal-phase info...

</details>

<details>
<summary>Share</summary>

```
VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control

Traffic signal control (TSC) is essential for mitigating urban congestion.

arXiv: https://arxiv.org/abs/2609.30709

#VLA #robotics
```

</details>

---

### [CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution](https://arxiv.org/abs/2609.27468)

**Authors:** Shuai Zeng, Yuxuan Liang, Hangmiao Hu, Fobao Zhou, Zixiang Wang et al. (7 authors)

**Published:** 2026-09-23 | **Categories:** cs.CV, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.27468) | [PDF](https://arxiv.org/pdf/2609.27468)

<details>
<summary>Abstract</summary>

Action-chunked vision-language-action (VLA) policies improve inference efficiency, but limited feedback within committed action chunks can lead to accumulated execution errors. Residual adaptation can correct such deviations without retraining the VLA; however, existing corrections are typically optimized for reference-action consistency without explicitly considering their downstream consequences. To address this limitation, we present Cerebellum-Inspired Consequence-Aware Residual Governance (CereVLA), a unified framework that integrates lightweight residual refinement and predictive consequ...

</details>

<details>
<summary>Share</summary>

```
CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution

Action-chunked vision-language-action (VLA) policies improve inference efficiency, but limited feedback within committed action chunks can lead to accumulated execution errors.

arXiv: https://arxiv.org/abs/2609.27468

#VLA #robotics
```

</details>

---

### [FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.30965)

**Authors:** Hiroshi Ito, Hyogo Hiruma, Yoshiki Kanai, Takahiro Yoshida, Akira Kanazawa et al. (6 authors)

**Published:** 2026-09-25 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.30965) | [PDF](https://arxiv.org/pdf/2609.30965)

<details>
<summary>Abstract</summary>

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters. In this work, we propose the Future Representation Action Model (FRAM), a small policy that explicitly links the future end-effector trajectory to the current visual input. FRAM uses the image coordinates of the predicted trajectory as spatial pointers and reads local visual features related to the motion from the current image. This organizes the information for action generation into the reference position (Where), the visual state (What), and the future motion (Futu...

</details>

<details>
<summary>Share</summary>

```
FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters.

arXiv: https://arxiv.org/abs/2609.30965

#VLA #robotics
```

</details>

---

### [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389)

**Authors:** Zexi Li, Yehang Zhang, Wenqian Li, Haojian Huang, Chenxu Wang et al. (15 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.29389) | [PDF](https://arxiv.org/pdf/2609.29389)

<details>
<summary>Abstract</summary>

Foundation vision-language models (VLMs) understand objects, instructions, and spatial relations, yet translating this capability into robotic manipulation remains difficult. Vision-language-action (VLA) models require extensive demonstrations and may compromise pretrained understanding, while direct RGB-only VLM control is costly and strongly dependent on model capability. We introduce Robo-Harness K1, a robot-use agent (RUA) framework that exposes perception as tools. The agent queries calibrated depth, persistent visual anchors, spatial measurements, and grasp hypotheses, then selects gener...

</details>

<details>
<summary>Share</summary>

```
Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation

Foundation vision-language models (VLMs) understand objects, instructions, and spatial relations, yet translating this capability into robotic manipulation remains difficult.

arXiv: https://arxiv.org/abs/2609.29389

#VLA #robotics
```

</details>

---

### [CrossSafe: Towards Cross-Embodiment Latent Safety Filters](https://arxiv.org/abs/2609.28984)

**Authors:** Ihab Tabbara, Yuxuan Yang, Hussein Sibai

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.28984) | [PDF](https://arxiv.org/pdf/2609.28984)

<details>
<summary>Abstract</summary>

Cross-embodiment learning has shown that a single model, such as a vision-language-action (VLA) model, can learn state representations and manipulation skills that can be applied across heterogeneous robots to accomplish various tasks. We hypothesize that the same holds for safety enforcement. The reasoning required to satisfy a safety constraint, such as detecting an obstacle, recognizing that it should be avoided, and selecting a safe abstract action, is largely shared across robots. What differs across embodiments is how the abstract safe action is realized: morphology, kinematics, and dyna...

</details>

<details>
<summary>Share</summary>

```
CrossSafe: Towards Cross-Embodiment Latent Safety Filters

Cross-embodiment learning has shown that a single model, such as a vision-language-action (VLA) model, can learn state representations and manipulation skills that can be applied across heterogeneous robots to accompl...

arXiv: https://arxiv.org/abs/2609.28984

#VLA #robotics
```

</details>

---

### [ActGaze: Learning Action-Grounded Gaze through Counterfactual Visual Interventions for High-Precision Manipulation](https://arxiv.org/abs/2609.28955)

**Authors:** Jinxuan Zhu, Jiaheng Wang, Chao Tang, Mengfan Wang, Hao Wei et al. (10 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.28955) | [PDF](https://arxiv.org/pdf/2609.28955)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models often struggle with high-precision robotic manipulation. We attribute this limitation primarily to their visual attention being dispersed across task-irrelevant regions. To address this issue, we propose ActGaze, a training approach that guides VLA policies to gaze on task-relevant regions, much like humans gaze on critical visual cues while executing precise movements. Unlike prior methods that rely on external labels for gaze supervision, ActGaze derives spatial supervision directly from the VLA's own action objective by using counterfactual visual...

</details>

<details>
<summary>Share</summary>

```
ActGaze: Learning Action-Grounded Gaze through Counterfactual Visual Interventions for High-Precision Manipulation

Current Vision-Language-Action (VLA) models often struggle with high-precision robotic manipulation.

arXiv: https://arxiv.org/abs/2609.28955

#VLA #robotics
```

</details>

---

### [InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies](https://arxiv.org/abs/2609.27734)

**Authors:** Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave

**Published:** 2026-09-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.27734) | [PDF](https://arxiv.org/pdf/2609.27734)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies often rely strongly on the camera viewpoints seen during training, causing substantial performance degradation when deployed from unseen perspectives. Collecting demonstrations from sufficiently diverse physical viewpoints is expensive and still provides only sparse coverage of the viewpoint space. We introduce InfiNoVA, a data-augmentation framework that converts synchronized multi-camera demonstrations into a dense distribution of geometrically consistent training views. InfiNoVA reconstructs each manipulation trajectory as a time-varying 3D Gaussian rep...

</details>

<details>
<summary>Share</summary>

```
InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies

Vision-Language-Action (VLA) policies often rely strongly on the camera viewpoints seen during training, causing substantial performance degradation when deployed from unseen perspectives.

arXiv: https://arxiv.org/abs/2609.27734

#VLA #robotics
```

</details>

---

### [Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study](https://arxiv.org/abs/2609.26868)

**Authors:** Zijian Zhang, Zhen Zeng, Zhongshu Gu, Sandeep Pisharody

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.26868) | [PDF](https://arxiv.org/pdf/2609.26868)

<details>
<summary>Abstract</summary>

Learning-based models (e.g., visuomotor and Vision-Language-Action (VLA)) are increasingly explored for industrial robotic manipulation, where model predictions are directly translated into physical actions. This tight coupling between model behavior and physical execution makes hidden security vulnerabilities particularly consequential. While backdoor attacks have been widely studied in conventional AI models, their effects on deployed learning-based robotic arm manipulation systems remain less understood: a backdoored robot can behave normally during benign operation while inducing attacker-...

</details>

<details>
<summary>Share</summary>

```
Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study

Learning-based models (e.g., visuomotor and Vision-Language-Action (VLA)) are increasingly explored for industrial robotic manipulation, where model predictions are directly translated into physical actions.

arXiv: https://arxiv.org/abs/2609.26868

#VLA #robotics
```

</details>

---

### [RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?](https://arxiv.org/abs/2609.26292)

**Authors:** Jiaqi Zhang, Feng Ye, Mingjia Yang, Zhihong Chen, Mingkang Xiang et al. (9 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.26292) | [PDF](https://arxiv.org/pdf/2609.26292)

<details>
<summary>Abstract</summary>

Physical-condition diversity is largely missing from current benchmarks for robot manipulation. While large-scale simulation benchmarks increasingly incorporate variations in object appearance, scene layout, and visual observations, they typically keep the underlying physical parameters fixed. As a result, important sources of real-world variability, such as changes in mass, friction, and joint dynamics, remain largely untested. We introduce RoboTwin-Phys, a physics-diverse benchmark that treats physical-condition diversity as an explicit dimension of robot manipulation evaluation. The benchma...

</details>

<details>
<summary>Share</summary>

```
RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?

Physical-condition diversity is largely missing from current benchmarks for robot manipulation.

arXiv: https://arxiv.org/abs/2609.26292

#VLA #robotics
```

</details>

---

### [VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](https://arxiv.org/abs/2609.25785)

**Authors:** Jung-Woo Lee, Soo-Chul Lim

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.25785) | [PDF](https://arxiv.org/pdf/2609.25785)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies. However, in dexterous hand manipulation, contact forces are typically provided as separate states or force-specific representations, making it difficult to explicitly represent the spatial correspondence between force and their corresponding visual locations. In this work, we propose VisForce, which visually grounds the current and desired forces at their corresponding fingertip locations. VisForce renders current and desired visual force cues on the current wrist image and a task-specific goal i...

</details>

<details>
<summary>Share</summary>

```
VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation

Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies.

arXiv: https://arxiv.org/abs/2609.25785

#VLA #robotics
```

</details>

---

### [Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera](https://arxiv.org/abs/2609.25750)

**Authors:** Ziang Ren, Zike Yan, Raymond Zhang, Xuguo He, Zhongyu Li

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.25750) | [PDF](https://arxiv.org/pdf/2609.25750)

<details>
<summary>Abstract</summary>

Manipulation requires both broad scene awareness and detailed local feedback, yet conventional camera rigs provide them through separate front and wrist cameras. We present Fisheye-VLA, a visual interface that brings these capabilities together using a single passive fisheye. A global view preserves the workspace, while local perspective crops direct detail toward the interaction. The key design question is where this local visual budget should go. We answer it through a controlled re-rendering study, comparing alternative crop directions on the same recorded observations. The study finds that...

</details>

<details>
<summary>Share</summary>

```
Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera

Manipulation requires both broad scene awareness and detailed local feedback, yet conventional camera rigs provide them through separate front and wrist cameras.

arXiv: https://arxiv.org/abs/2609.25750

#VLA #robotics
```

</details>

---

### [Capability-Aware Arbitration for Semantic Intent-Based Shared Control](https://arxiv.org/abs/2609.25369)

**Authors:** Zhaoda Du, Michael Bowman, Xiaoli Zhang

**Published:** 2026-09-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.25369) | [PDF](https://arxiv.org/pdf/2609.25369)

<details>
<summary>Abstract</summary>

Shared control often allocates robot authority based on confidence in inferred human intent, assuming reliable autonomous execution. When this assumption fails, high intent confidence can cause over-helping. We present a capability-aware shared-control framework in which a vision-language model (VLM) infers human intent and provides semantic-intent confidence, while a vision-language-action (VLA) policy generates autonomous actions. VLA capability confidence is estimated online from the dispersion and local instability of stochastic action trajectories. We design a nonlinear arbitration policy...

</details>

<details>
<summary>Share</summary>

```
Capability-Aware Arbitration for Semantic Intent-Based Shared Control

Shared control often allocates robot authority based on confidence in inferred human intent, assuming reliable autonomous execution.

arXiv: https://arxiv.org/abs/2609.25369

#VLA #robotics
```

</details>

---

### [Full-Covariance Smoothing of Bayesian Neural Networks for Online Adaptation](https://arxiv.org/abs/2609.27244)

**Authors:** Oren Wright, Haoming Jing, Qiaoan Shen, Koichiro Niinuma, Yorie Nakahira et al. (6 authors)

**Published:** 2026-09-23 | **Categories:** cs.LG, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.27244) | [PDF](https://arxiv.org/pdf/2609.27244)

<details>
<summary>Abstract</summary>

A neural network's layers can be treated as time steps of a state-space model, turning Bayesian training into a smoothing problem: a forward pass propagates Gaussian moments through the network, and a backward Rauch--Tung--Striebel pass updates the weight posteriors in closed form. Such methods learn from each observation in a single pass, in an uncertainty-aware manner, and without gradient-based iterations or replay, which makes them well suited for online adaptation and data-efficient learning. Existing smoothing-based methods, however, are restricted to diagonal covariances across activati...

</details>

<details>
<summary>Share</summary>

```
Full-Covariance Smoothing of Bayesian Neural Networks for Online Adaptation

A neural network's layers can be treated as time steps of a state-space model, turning Bayesian training into a smoothing problem: a forward pass propagates Gaussian moments through the network, and a backward Rauch--...

arXiv: https://arxiv.org/abs/2609.27244

#VLA #robotics
```

</details>

---

### [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964)

**Authors:** Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou et al. (16 authors)

**Published:** 2026-09-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.29964) | [PDF](https://arxiv.org/pdf/2609.29964)

<details>
<summary>Abstract</summary>

General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehea...

</details>

<details>
<summary>Share</summary>

```
World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal

General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them...

arXiv: https://arxiv.org/abs/2609.29964

#VLA #robotics
```

</details>

---

### [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308)

**Authors:** Zeyu Shen, Haoxiang You, Yilang Liu, Zhicheng Zheng, Lihan Zha et al. (19 authors)

**Published:** 2026-09-23 (updated 2026-09-25) | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.27308) | [PDF](https://arxiv.org/pdf/2609.27308)

<details>
<summary>Abstract</summary>

We study coding agents for long-horizon, dexterous robotics and ask whether their solutions can provide scalable supervision for learning general robot policies. To test this, we develop EMBODIEDSWE-BENCH, a simulation benchmark for coding agents spanning contact-rich manipulation, deformable objects, and long-horizon tasks requiring up to half an hour of continuous interaction. We find that frontier coding agents can solve complex long-horizon tasks and transfer prior solutions across both tasks and embodiments. We also design supporting tools that help agents more effectively solve these tas...

</details>

<details>
<summary>Share</summary>

```
EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics

We study coding agents for long-horizon, dexterous robotics and ask whether their solutions can provide scalable supervision for learning general robot policies.

arXiv: https://arxiv.org/abs/2609.27308

#VLA #robotics
```

</details>

---

### [CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing](https://arxiv.org/abs/2609.25606)

**Authors:** Zhifei Teng, Bo Feng, Xiang Zou, Jinpeng Xiao, Min Li et al. (7 authors)

**Published:** 2026-09-22 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.25606) | [PDF](https://arxiv.org/pdf/2609.25606)

<details>
<summary>Abstract</summary>

Cable routing requires coordinated control of global cable topology and changing local contacts. We present CableVLA, an end-to-end multimodal vision-language-action framework that converts simulation-privileged supervision into deployable cable-topology and tactile representations. TopoHead distills node-level physics and current and future cable-topology information into causal visual context for the action expert. TacSense uses complementary frame and taxel branches to learn contact dynamics from resistive arrays, with simulator-derived kinematics and contact events providing supervision be...

</details>

<details>
<summary>Share</summary>

```
CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing

Cable routing requires coordinated control of global cable topology and changing local contacts.

arXiv: https://arxiv.org/abs/2609.25606

#VLA #robotics
```

</details>

---
