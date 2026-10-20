# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-20 19:49 UTC

**Papers shown:** 94 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](https://arxiv.org/abs/2610.25961)

**Authors:** Hojin Jeon, Jimin Lee, Taekwan Kim, Nayoung Oh, Taeyoung Kim et al. (9 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25961) | [PDF](https://arxiv.org/pdf/2610.25961) | [Project Page](https://pacevla.github.io/)

<details>
<summary>Abstract</summary>

Fast and reliable manipulation is crucial for practical robot deployment. Although Vision-Language-Action (VLA) models have recently shown remarkable progress as generalist robot policies, their execution often remains temporally inefficient. A key source of this inefficiency is that policies learn fine-grained temporal patterns from teleoperated demonstrations, requiring many low-level action steps. Temporal action quantization offers a simple way to accelerate execution by aggregating consecutive low-level actions into temporally coarser actions. However, applying action quantization without...

</details>

<details>
<summary>Share</summary>

```
PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

Fast and reliable manipulation is crucial for practical robot deployment.

arXiv: https://arxiv.org/abs/2610.25961
Project page: https://pacevla.github.io/

#VLA #robotics
```

</details>

---

### [VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse](https://arxiv.org/abs/2610.25043)

**Authors:** Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu et al. (13 authors)

**Published:** 2026-10-18 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25043) | [PDF](https://arxiv.org/pdf/2610.25043) | [Project Page](https://chenbao123ww.github.io/VLA-Rolling/)

<details>
<summary>Abstract</summary>

Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising progress: action-tail initialization can match or outperform a native 10-step Gaussian baseline using fewer denoising steps. However, the optimal denoising budget varies substantially...

</details>

<details>
<summary>Share</summary>

```
VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse

Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations.

arXiv: https://arxiv.org/abs/2610.25043
Project page: https://chenbao123ww.github.io/VLA-Rolling/

#VLA #robotics
```

</details>

---

### [NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](https://arxiv.org/abs/2610.23271)

**Authors:** Guodong Du, Wanyu Lin

**Published:** 2026-10-16 (updated 2026-10-19) | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.23271) | [PDF](https://arxiv.org/pdf/2610.23271) | [Code](https://github.com/WanyuGroup/NeurIPS2026-NestedVLA)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc. To this end, we propose NestedVLA, which replaces parameter aggregation with parameter generation: a nested hypernetwork, conditio...

</details>

<details>
<summary>Share</summary>

```
NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, jo...

arXiv: https://arxiv.org/abs/2610.23271
Code: https://github.com/WanyuGroup/NeurIPS2026-NestedVLA

#VLA #robotics
```

</details>

---

### [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](https://arxiv.org/abs/2610.22951)

**Authors:** Khuyen Pham, Tran Nguyen Le, Edoardo Fazzari, Cesare Stefanini

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22951) | [PDF](https://arxiv.org/pdf/2610.22951) | [Code](https://github.com/giakhuyendihoc/MambaAct)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control. This limitation is especially pronounced in flow-matching VLAs such as $π_{0.5}$, where the action expert is evaluated repeatedly during iterative denoising. We introduce MambaAct, an efficient Mamba action expert for flow-matching VLA policies. MambaAct retains the pretrained visual-language prefix encoder of $π_{0.5}$, while replacing its transformer-based action expert with a compact Mamba-based action expert. Within th...

</details>

<details>
<summary>Share</summary>

```
MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models

Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control.

arXiv: https://arxiv.org/abs/2610.22951
Code: https://github.com/giakhuyendihoc/MambaAct

#VLA #robotics
```

</details>

---

### [REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178)

**Authors:** Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary, Shizhe Chen, Moritz Böhle

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22178) | [PDF](https://arxiv.org/pdf/2610.22178) | [Code](https://github.com/kyutai-labs/reki)

<details>
<summary>Abstract</summary>

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in th...

</details>

<details>
<summary>Share</summary>

```
REKI: Registering Knowledge in VLAs

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa36...

arXiv: https://arxiv.org/abs/2610.22178
Code: https://github.com/kyutai-labs/reki

#VLA #robotics
```

</details>

---

### [When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.22556)

**Authors:** Victoria Smelova, Daniil Kazachkov, Georgiy Kazantsev, Iuliia Tsvetkova, Egor Cherepanov et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22556) | [PDF](https://arxiv.org/pdf/2610.22556) | [Project Page](https://vika787.github.io/RePlanMem/)

<details>
<summary>Abstract</summary>

Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation. Retaining the complete observation history is computationally expensive and highly redundant, motivating selective visual memory. We introduce RePlanMem-VLA (Replanning-Guided Keyframe Memory for VLA), which turns a policy's own plan revisions into an online memory-write signal. Under receding-horizon execution, consecutive action chunks predict some of the same future actions. RePlanMem-VLA treats unusually large disagreement between these temp...

</details>

<details>
<summary>Share</summary>

```
When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models

Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation.

arXiv: https://arxiv.org/abs/2610.22556
Project page: https://vika787.github.io/RePlanMem/

#VLA #robotics
```

</details>

---

### [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146)

**Authors:** Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu, Yang Sui, Yangming Shi

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22146) | [PDF](https://arxiv.org/pdf/2610.22146) | [Code](https://github.com/jiuyixu25/FastVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets...

</details>

<details>
<summary>Share</summary>

```
FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often mu...

arXiv: https://arxiv.org/abs/2610.22146
Code: https://github.com/jiuyixu25/FastVLA

#VLA #robotics
```

</details>

---

### [ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction](https://arxiv.org/abs/2610.20223)

**Authors:** Huailiang Ma, Yuxuan Li, Ziyi Zhao, Xinkai Wang, Mingyu Li et al. (10 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20223) | [PDF](https://arxiv.org/pdf/2610.20223) | [Project Page](https://huailiangma.github.io/objdream/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions. However, most existing VLA models still operate on image-level visual representations inherited from pretrained vision-language backbones, while lacking fine-grained object understanding for manipulation. As a result, their robustness can degrade under out-of-distribution object layouts, clutter, and background variations. To address these limitations, we introduce ObjDream, an object-centric VLA framework cent...

</details>

<details>
<summary>Share</summary>

```
ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction

Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2610.20223
Project page: https://huailiangma.github.io/objdream/

#VLA #robotics
```

</details>

---

### [What Matters for World Modeling in Vision-Language-Action Models?](https://arxiv.org/abs/2610.19825)

**Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang et al. (13 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19825) | [PDF](https://arxiv.org/pdf/2610.19825) | [Project Page](https://dylanmqs.github.io/WM-in-VLAs/)

<details>
<summary>Abstract</summary>

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping. However, existing approaches vary simultaneously in their world representations, integration paradigms, and policy backbones, making it difficult to determine what truly matters for effective world model integration. To disentangle these factors, we categorize existing efforts into four representative paradigms, namely Implicit Future Alignment, Explicit Future Query, MoT Future Expert, and Extern...

</details>

<details>
<summary>Share</summary>

```
What Matters for World Modeling in Vision-Language-Action Models?

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping.

arXiv: https://arxiv.org/abs/2610.19825
Project page: https://dylanmqs.github.io/WM-in-VLAs/

#VLA #robotics
```

</details>

---

### [WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL](https://arxiv.org/abs/2610.17922)

**Authors:** Shangqing Zhou, Zhennan Jiang, Ning Ma, Xin Fu, Yupeng Zheng et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17922) | [PDF](https://arxiv.org/pdf/2610.17922) | [Project Page](https://youmo445.github.io/WoVR_Plus.github.io/)

<details>
<summary>Abstract</summary>

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization. Extending them to richer VLA interfaces and long-horizon tasks raises challenges in spatiotemporal and cross-modal consistency, exploration-reliability balance in RL, and compounding rollout errors. We present WoVR+, extending WoVR's hallucination-aware WM-RL framework by redesigning the learned environment and imagined interaction protocol: A VLA-interface-aligned world model provides multi-view predi...

</details>

<details>
<summary>Share</summary>

```
WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization.

arXiv: https://arxiv.org/abs/2610.17922
Project page: https://youmo445.github.io/WoVR_Plus.github.io/

#VLA #robotics
```

</details>

---

### [TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency](https://arxiv.org/abs/2610.17540)

**Authors:** Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17540) | [PDF](https://arxiv.org/pdf/2610.17540) | [Project Page](https://tacitvla.github.io)

<details>
<summary>Abstract</summary>

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate...

</details>

<details>
<summary>Share</summary>

```
TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding.

arXiv: https://arxiv.org/abs/2610.17540
Project page: https://tacitvla.github.io

#VLA #robotics
```

</details>

---

### [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)

**Authors:** Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21306) | [PDF](https://arxiv.org/pdf/2610.21306) | [Code](https://github.com/ZJU-OmniAI/VLA-Delta)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. W...

</details>

<details>
<summary>Share</summary>

```
VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks.

arXiv: https://arxiv.org/abs/2610.21306
Code: https://github.com/ZJU-OmniAI/VLA-Delta

#VLA #robotics
```

</details>

---

### [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](https://arxiv.org/abs/2610.26717)

**Authors:** Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26717) | [PDF](https://arxiv.org/pdf/2610.26717)

<details>
<summary>Abstract</summary>

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to collect on physical robots. In this work, we develop a simulation-to-real robot-learning framework for ag...

</details>

<details>
<summary>Share</summary>

```
Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints.

arXiv: https://arxiv.org/abs/2610.26717

#VLA #robotics
```

</details>

---

### [SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models](https://arxiv.org/abs/2610.26487)

**Authors:** Shenli Zheng, Zhou Fang, Yuan Du, Yijiang Liu, Li Du

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26487) | [PDF](https://arxiv.org/pdf/2610.26487)

<details>
<summary>Abstract</summary>

The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simultaneously prunes the hidden and feed-forward intermediate dimensions of the large language model (LLM) backbone through pruning-aware tuning, then applies reinforcement learning (RL) to recover policy performance. Applied to $π_{0.5}$, SPAR...

</details>

<details>
<summary>Share</summary>

```
SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models

The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate.

arXiv: https://arxiv.org/abs/2610.26487

#VLA #robotics
```

</details>

---

### [Robotic Photography System based on Vision-Language-Action Model](https://arxiv.org/abs/2610.26287)

**Authors:** Song-Li Wu, Chubin Zhang, Wenbo Ding, Yansong Tang

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26287) | [PDF](https://arxiv.org/pdf/2610.26287)

<details>
<summary>Abstract</summary>

Modern robotic photography requires understanding photographic intent, planning camera motions, and producing aesthetically pleasing images in complex environments. We present RoboPhoto-VLA, a unified Vision-Language-Action framework that jointly models perception, reasoning, and camera control for autonomous robotic photography. RoboPhoto-VLA incorporates PhotoCoT for structured action planning and Aesthetic Direct Preference Optimization (ADPO) to align camera behaviors with human aesthetic preferences. To facilitate training and evaluation, we construct OpenPhotography, a robotic photograph...

</details>

<details>
<summary>Share</summary>

```
Robotic Photography System based on Vision-Language-Action Model

Modern robotic photography requires understanding photographic intent, planning camera motions, and producing aesthetically pleasing images in complex environments.

arXiv: https://arxiv.org/abs/2610.26287

#VLA #robotics
```

</details>

---

### [CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA](https://arxiv.org/abs/2610.25927)

**Authors:** Feiyang Hong, Yujie Wei, Bo Zhao, Xiu Su, Hongxun Yao et al. (6 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25927) | [PDF](https://arxiv.org/pdf/2610.25927) | [Code](https://github.com/FeiyangHong/CondenseVLA)

<details>
<summary>Abstract</summary>

Robot manipulation often depends on short-term cues - such as brief contacts, temporary occlusions, and intermediate object states - that are ambiguous in a single frame and can only be resolved by integrating observations over time. However, injecting historical information solely by enlarging the history window is computationally costly and frequently yields limited gains due to substantial redundancy and task-agnostic, inflexible sampling of observations. We propose CondenseVLA, a multi-frame VLA policy with a learnable decoder-side history condensation module for using short-term visual co...

</details>

<details>
<summary>Share</summary>

```
CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA

Robot manipulation often depends on short-term cues - such as brief contacts, temporary occlusions, and intermediate object states - that are ambiguous in a single frame and can only be resolved by integrating observa...

arXiv: https://arxiv.org/abs/2610.25927
Code: https://github.com/FeiyangHong/CondenseVLA

#VLA #robotics
```

</details>

---

### [Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation](https://arxiv.org/abs/2610.25874)

**Authors:** Lingsen Zhang, Wei Li, Jie He, Henghua Zhang, Kai Mo et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25874) | [PDF](https://arxiv.org/pdf/2610.25874) | [Code](https://github.com/baidu-baige/LoongForge)

<details>
<summary>Abstract</summary>

Robotic manipulation is not merely observation-to-action generation, but the realization of task-specified state changes in the physical world. Existing vision-language-action (VLA) methods directly learn observation-to-action mappings, imposing a substantial learning burden due to the gap between semantic understanding and action execution. Although world-action models (WAMs) improve control through future prediction, modeling complete future states wastes capacity on static appearance and action-irrelevant changes. We propose Vision-Language-Delta-Action (VLDA), a paradigm that reformulates...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation

Robotic manipulation is not merely observation-to-action generation, but the realization of task-specified state changes in the physical world.

arXiv: https://arxiv.org/abs/2610.25874
Code: https://github.com/baidu-baige/LoongForge

#VLA #robotics
```

</details>

---

### [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459)

**Authors:** Yong Wang, Kecheng Zheng, Xing Zhu, Chao Xu, Yujun Shen et al. (6 authors)

**Published:** 2026-10-18 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.25459) | [PDF](https://arxiv.org/pdf/2610.25459) | [Project Page](https://BiDex-100.github.io/BiDex-100/)

<details>
<summary>Abstract</summary>

Bimanual manipulation with dexterous hands has attracted growing attention in research on robotic action models. However, few studies have developed benchmarks specifically tailored for dexterous manipulation, leaving the dexterous manipulation capabilities of existing models insufficiently characterized. In this paper, we present BiDex-100, a simulation benchmark for bimanual dexterous manipulation that combines broad task coverage, multi-dimensional evaluation, and high-DoF hand embodiments. Concretely, the benchmark comprises 106 tasks organized along five capability axes: generalization, i...

</details>

<details>
<summary>Share</summary>

```
BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks

Bimanual manipulation with dexterous hands has attracted growing attention in research on robotic action models.

arXiv: https://arxiv.org/abs/2610.25459
Project page: https://BiDex-100.github.io/BiDex-100/

#VLA #robotics
```

</details>

---

### [VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents](https://arxiv.org/abs/2610.23018)

**Authors:** Chenglong Zhang, Shuaijun Liu, Feiyang You, Shuyang Hao, Chengyu Wu et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.23018) | [PDF](https://arxiv.org/pdf/2610.23018) | [Project Page](https://nebulis-lab.com/VLA-Fabric/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are rapidly expanding what individual robots can accomplish, yet many real-world manipulation settings require multiple arms to operate as a coordinated system. Existing approaches organize multi-arm coordination in different ways, including centralized joint policies, high-level task or role assignment, and locally executed policies that react to teammates. However, how complete action-producing VLAs should explicitly interact with one another during action generation remains largely unexplored. We introduce VLA-Fabric, which organizes one complete VLA per...

</details>

<details>
<summary>Share</summary>

```
VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents

Vision-language-action (VLA) models are rapidly expanding what individual robots can accomplish, yet many real-world manipulation settings require multiple arms to operate as a coordinated system.

arXiv: https://arxiv.org/abs/2610.23018
Project page: https://nebulis-lab.com/VLA-Fabric/

#VLA #robotics
```

</details>

---

### [Fast-VLA: You Only Think Once for Robot Manipulation](https://arxiv.org/abs/2610.21389)

**Authors:** Kehong Gong, Guanli Hou, Xiaoxu Zheng, Qi Wang, Mingxi Xu et al. (9 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21389) | [PDF](https://arxiv.org/pdf/2610.21389) | [Project Page](https://garfield-kh.github.io/FastVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk. Yet task understanding changes far more slowly than the robot state. We introduce Fast-VLA, which invokes a frozen 4B VLM once per episode to contextualize the instruction and initial views as fixed, multi-layer key-value task memory. During execution, a lightweight online actor fuses learned time- and arm-indexed queries with current visual and proprioceptive feedback to form action queries. These queries r...

</details>

<details>
<summary>Share</summary>

```
Fast-VLA: You Only Think Once for Robot Manipulation

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk.

arXiv: https://arxiv.org/abs/2610.21389
Project page: https://garfield-kh.github.io/FastVLA

#VLA #robotics
```

</details>

---

### [LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.21362)

**Authors:** Qixin Sun, WenLong Gao, Xiansheng Chen, Zhongyuan Wang, Si Liu et al. (6 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21362) | [PDF](https://arxiv.org/pdf/2610.21362) | [Code](https://github.com/buaa-colalab/LTM-pi)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires remembering interactions that are no longer visible. We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations. Instantiated on $π_{0.5}$ as LTM-$π$, our method uses a frozen latent action encoder, a lightweight adapter, and causal KV caching for incremental inference without memory-specific semantic annotations or external reasoning-model calls. With DreamDojo transitions, LTM-$π$ achieves 58.54% success on RoboMME and 80.5% on LIBERO-Mem, performing best among baselines without external...

</details>

<details>
<summary>Share</summary>

```
LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models

Robotic manipulation often requires remembering interactions that are no longer visible.

arXiv: https://arxiv.org/abs/2610.21362
Code: https://github.com/buaa-colalab/LTM-pi

#VLA #robotics
```

</details>

---

### [FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs](https://arxiv.org/abs/2610.20064)

**Authors:** Bingao Chen, Lihan Zha, C. Karen Liu, Guy Tevet

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20064) | [PDF](https://arxiv.org/pdf/2610.20064) | [Project Page](https://tml.stanford.edu/FoveaVLA/)

<details>
<summary>Abstract</summary>

We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions. Wrist cameras provide close-up detail but restrict the view to the end-effector's surroundings. External cameras see the whole scene, but the policy receives them at low resolution, so the fine detail needed for manipulation is lost. FoveaVLA recovers this detail by predicting, alongside each action chunk, the interaction region to observe at the next policy query. The policy then receives crops of these regions, taken from the original-resolution images, together with the f...

</details>

<details>
<summary>Share</summary>

```
FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs

We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions.

arXiv: https://arxiv.org/abs/2610.20064
Project page: https://tml.stanford.edu/FoveaVLA/

#VLA #robotics
```

</details>

---

### [Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](https://arxiv.org/abs/2610.19495)

**Authors:** Yunze Liu, Jing Wang, Shenrui Wu, Wenkun He, Guanqi Zhan et al. (19 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19495) | [PDF](https://arxiv.org/pdf/2610.19495) | [Project Page](https://robota-ai.github.io/robota-embed/)

<details>
<summary>Abstract</summary>

Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first vision-language-action (VLA) embedding model to jointly encode all three modalities in both current-state queries and recorded future continuations. Predictive retrieval training aligns these endpoints, enabling historical continuations to serve as context at inference time. We construct a multi-source corpus of 1,695,684 cleaned training anchors and introduce Robota-Embed-Bench, with 4,000 queries and a shared 8,000-e...

</details>

<details>
<summary>Share</summary>

```
Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution

Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow.

arXiv: https://arxiv.org/abs/2610.19495
Project page: https://robota-ai.github.io/robota-embed/

#VLA #robotics
```

</details>

---

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869)

**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang et al. (22 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18869) | [PDF](https://arxiv.org/pdf/2610.18869) | [Project Page](https://axis-bench.github.io/)

<details>
<summary>Abstract</summary>

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain b...

</details>

<details>
<summary>Share</summary>

```
What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning?

arXiv: https://arxiv.org/abs/2610.18869
Project page: https://axis-bench.github.io/

#VLA #robotics
```

</details>

---

### [Interaction Latents as Actions for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18855)

**Authors:** Yuhang Zheng, Yujie Zang, Yuchen Liu, Yupeng Zheng, Zhennan Jiang et al. (12 authors)

**Published:** 2026-10-13 (updated 2026-10-14) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18855) | [PDF](https://arxiv.org/pdf/2610.18855) | [Project Page](https://mrsecant.github.io/ILA/)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction. Yet most robot policies represent actions primarily as motion trajectories, using tactile signals as inputs or auxiliary prediction targets without explicitly encoding contact dynamics in the action representation. We propose ILA (Interaction Latents as Actions), which uses decodable interaction latents that jointly capture the evolution of motion, contact, and force application as policy action units, providing a shared representation for acti...

</details>

<details>
<summary>Share</summary>

```
Interaction Latents as Actions for Contact-Rich Manipulation

Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction.

arXiv: https://arxiv.org/abs/2610.18855
Project page: https://mrsecant.github.io/ILA/

#VLA #robotics
```

</details>

---

### [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2610.26584)

**Authors:** Langzhe Gu, Chengkai Hou, Meng Li, Xinhua Wang, Xinyuan Lv et al. (15 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26584) | [PDF](https://arxiv.org/pdf/2610.26584)

<details>
<summary>Abstract</summary>

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional whole-body action space, where inaccurate base or waist motions can easily induce unstable and aggressive upper-body compensation. We propose HAF-VLA, a hierarchical action-flow framework for humanoid VLA control. Built upon a pretrained...

</details>

<details>
<summary>Share</summary>

```
HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging.

arXiv: https://arxiv.org/abs/2610.26584

#VLA #robotics
```

</details>

---

### [FR-VLA: Implicit Force Reasoning VLA for Contact-Rich Manipulation](https://arxiv.org/abs/2610.25981)

**Authors:** Jiaju He, Zhiyuan Yang, Ruyang Han, Jiahong Tang, Zhiping Lin et al. (6 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.25981) | [PDF](https://arxiv.org/pdf/2610.25981)

<details>
<summary>Abstract</summary>

Integrating force awareness into Vision-Language-Action (VLA) models involves not merely encoding wrench measurements as an additional modality, but determining when and how strongly physical interaction should influence robot action generation. Existing VLAs that use force typically inject it through a fixed pathway, without explicitly determining when it is relevant to the current action. This calls for an intermediate force relevance mechanism inside the VLA, in which visual-language context estimates the relevance of physical feedback to the current task before force enters the action path...

</details>

<details>
<summary>Share</summary>

```
FR-VLA: Implicit Force Reasoning VLA for Contact-Rich Manipulation

Integrating force awareness into Vision-Language-Action (VLA) models involves not merely encoding wrench measurements as an additional modality, but determining when and how strongly physical interaction should influe...

arXiv: https://arxiv.org/abs/2610.25981

#VLA #robotics
```

</details>

---

### [Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving](https://arxiv.org/abs/2610.25734)

**Authors:** Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang et al. (8 authors)

**Published:** 2026-10-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.25734) | [PDF](https://arxiv.org/pdf/2610.25734)

<details>
<summary>Abstract</summary>

Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as language instructions or trajectory signals. This direct mapping from dense visual observations to sparse representations forces the model to compress or even discard critical scene information essential for safe driving. We argue that this limitation does not stem from insufficient model capacity, but from the lack of explicit mechanisms that encourage the formation of dense world rep...

</details>

<details>
<summary>Share</summary>

```
Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving

Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as langu...

arXiv: https://arxiv.org/abs/2610.25734

#VLA #robotics
```

</details>

---

### [AeroDASH: Asynchronous Vision-Language-Action Control for Continuous UAV Flight](https://arxiv.org/abs/2610.25407)

**Authors:** Zhe Liu, Yuxuan Zheng, Jinzhe Qin, Ziqi Gao, Boyu Zhou

**Published:** 2026-10-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.25407) | [PDF](https://arxiv.org/pdf/2610.25407)

<details>
<summary>Abstract</summary>

Onboard inference latency creates a mismatch between the trajectories predicted by vision-language-action (VLA) policies and the ongoing motion of unmanned aerial vehicles (UAVs). We present AeroDASH, an asynchronous VLA framework for continuous language-conditioned flight. A B-spline policy is initialized through supervised fine-tuning on expert demonstrations, providing continuous trajectory references in position and yaw. During execution, trajectory fusion removes the expired prediction prefix and connects the remaining segment to the active reference with derivative continuity while limit...

</details>

<details>
<summary>Share</summary>

```
AeroDASH: Asynchronous Vision-Language-Action Control for Continuous UAV Flight

Onboard inference latency creates a mismatch between the trajectories predicted by vision-language-action (VLA) policies and the ongoing motion of unmanned aerial vehicles (UAVs).

arXiv: https://arxiv.org/abs/2610.25407

#VLA #robotics
```

</details>

---

### [Relational Spatial Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2610.24705)

**Authors:** Chaoran Zhu, Hengyi Wang, Chenglin Cui, Yazhe Wan, Taein Kwon et al. (6 authors)

**Published:** 2026-10-17 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24705) | [PDF](https://arxiv.org/pdf/2610.24705)

<details>
<summary>Abstract</summary>

Spatial understanding is essential for robots to perceive their surrounding environments and execute actions. Existing approaches typically encode 3D awareness into vision-language-action (VLA) models by directly aligning their representations with pre-trained 3D foundation models. However, we observe that such direct geometric feature alignment essentially exploits 3D foundation priors as a form of low-rank regularization in the feature space, resulting in severe rank collapse of the pre-trained VLA representations. In contrast, we shift the focus from enforcing point-wise equality to alignin...

</details>

<details>
<summary>Share</summary>

```
Relational Spatial Alignment for Vision-Language-Action Models

Spatial understanding is essential for robots to perceive their surrounding environments and execute actions.

arXiv: https://arxiv.org/abs/2610.24705

#VLA #robotics
```

</details>

---

### [Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization](https://arxiv.org/abs/2610.23566)

**Authors:** Chunjin Ye, Guanying Chen, Jianjie Huang, Jianhao Chen, Quanlin Chen et al. (9 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23566) | [PDF](https://arxiv.org/pdf/2610.23566)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable language-guided robot manipulation, but remain vulnerable to visual attacks that undermine user control over robot behavior. Prior studies optimize visual perturbations using fixed target supervision. However, the perturbation can change earlier actions and, in turn, the physical states reached later. As the attacked trajectory evolves, this supervision may no longer match the behavior needed at the states actually reached. Accurately matching these targets can therefore fail to advance the attacker-specified task. Even with suitable supervision, redu...

</details>

<details>
<summary>Share</summary>

```
Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization

Vision-language-action (VLA) models enable language-guided robot manipulation, but remain vulnerable to visual attacks that undermine user control over robot behavior.

arXiv: https://arxiv.org/abs/2610.23566

#VLA #robotics
```

</details>

---

### [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](https://arxiv.org/abs/2610.23378)

**Authors:** Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23378) | [PDF](https://arxiv.org/pdf/2610.23378)

<details>
<summary>Abstract</summary>

Robots manipulating objects in clutter must decide not only how to act, but also where to look. Although active camera motion can expose an occluded target, it may move the robot into an initial observation-state distribution that differs from the manipulation policy's training distribution. We identify this problem as first-frame distribution sensitivity: under perturbed starts in LIBERO, naively prepending camera repositioning to pi_0.5 reduces success from 46.3% to 11.5%. We introduce ActiveAlign, a data-adaptation framework that trains a Vision-Language-Action (VLA) policy from the states...

</details>

<details>
<summary>Share</summary>

```
Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

Robots manipulating objects in clutter must decide not only how to act, but also where to look.

arXiv: https://arxiv.org/abs/2610.23378

#VLA #robotics
```

</details>

---

### [Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2610.21522)

**Authors:** Lichao Ni, Yuhan Liu, Pengfei Li, Guanghuan Fang

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.21522) | [PDF](https://arxiv.org/pdf/2610.21522)

<details>
<summary>Abstract</summary>

Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging. On-policy distillation (OPD) transfers teacher knowledge on inputs induced by the student, addressing the distribution mismatch encountered during deployment. For flow-based VLAs, this mismatch arises at two levels: environment observations and intermediate action-generation states. We propose a two-level on-policy distillation framework that couples student-driven environment interaction with teacher velocity supervision along stud...

</details>

<details>
<summary>Share</summary>

```
Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models

Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging.

arXiv: https://arxiv.org/abs/2610.21522

#VLA #robotics
```

</details>

---

### [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](https://arxiv.org/abs/2610.21453)

**Authors:** Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21453) | [PDF](https://arxiv.org/pdf/2610.21453) | [Project Page](https://vincent2311.github.io/Projects/CarryOn/)

<details>
<summary>Abstract</summary>

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution. Second, reliable deployment demands explainable safety assurance that proactively prevents hazards and gracefully recovers from occasional physical failures. To address these gaps, we present Car...

</details>

<details>
<summary>Share</summary>

```
CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable exe...

arXiv: https://arxiv.org/abs/2610.21453
Project page: https://vincent2311.github.io/Projects/CarryOn/

#VLA #robotics
```

</details>

---

### [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2610.21251)

**Authors:** Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.21251) | [PDF](https://arxiv.org/pdf/2610.21251)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions that specify how to carry it out. Through our diagnoses, we find that How-level instructions do not help current VLAs and lower task success. We hypothesize that pairing each training episode with a single instruction limits How-level instruction following, and show that training with segment-level enriched instructions makes actions respond to such instructions without consistently...

</details>

<details>
<summary>Share</summary>

```
Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions tha...

arXiv: https://arxiv.org/abs/2610.21251

#VLA #robotics
```

</details>

---

### [When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models](https://arxiv.org/abs/2610.21160)

**Authors:** Shilin Zhang

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.21160) | [PDF](https://arxiv.org/pdf/2610.21160)

<details>
<summary>Abstract</summary>

Dual-system vision-language-action (VLA) models pair a high-frequency fast policy with a slow, expensive module, and published trigger mechanisms for invoking it lack a shared objective, measured costs, and any standard separating schedule quality from module quality. We provide the missing account: invocation is formalized as a calibrated decision problem whose fixed-ratio, fixed-budget, and history-gated schedules are degenerate cases of one quantity, the Value of Intervention (VoI); a renewal baseline proves the optimal schedule periodic under state-independent collapse, with adaptive gains...

</details>

<details>
<summary>Share</summary>

```
When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models

Dual-system vision-language-action (VLA) models pair a high-frequency fast policy with a slow, expensive module, and published trigger mechanisms for invoking it lack a shared objective, measured costs, and any standa...

arXiv: https://arxiv.org/abs/2610.21160

#VLA #robotics
```

</details>

---

### [A Phenomenology of Neural Geometry in Vision-Language-Action Models](https://arxiv.org/abs/2610.20840)

**Authors:** Mozes Jacobs, Aiden Swann, Mathilde Papillon, Siddharth Boppana, Fenil R. Doshi et al. (19 authors)

**Published:** 2026-10-14 (updated 2026-10-17) | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20840) | [PDF](https://arxiv.org/pdf/2610.20840)

<details>
<summary>Abstract</summary>

Robotic manipulation is inherently geometric, but what shape does the world take inside the policy that performs it? Prior work on vision-language-action (VLA) policies establishes that task-relevant variables are linearly readable from activations, yet readability certifies only that a variable is present and says nothing about the shape its values trace, which may be curved and multi-dimensional. Using controlled sweeps, natural rollouts, linear probes, and activation interventions, we build a taxonomy of seven task-relevant concepts in VLA models. We find that realized geometry is predomina...

</details>

<details>
<summary>Share</summary>

```
A Phenomenology of Neural Geometry in Vision-Language-Action Models

Robotic manipulation is inherently geometric, but what shape does the world take inside the policy that performs it?

arXiv: https://arxiv.org/abs/2610.20840

#VLA #robotics
```

</details>

---

### [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](https://arxiv.org/abs/2610.20504)

**Authors:** Xiaoman Li, Zhiqiang Yang, Jiayu Hu, Jipeng Kong, Yang Zhang et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20504) | [PDF](https://arxiv.org/pdf/2610.20504) | [Project Page](https://gr-bc.github.io/)

<details>
<summary>Abstract</summary>

Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations, failed attempts, and imperfect recoveries. The key challenge is to identify which action chunks actually advance the task, rather than uniformly cloning or discarding imperfect trajectories. We propose Graph-Reweighted Behavior Cloning (GR-BC), an offline iterative post-training framework that builds a task-conditioned goal-reachability graph over demonstrations and iteratively co...

</details>

<details>
<summary>Share</summary>

```
Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation

Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations,...

arXiv: https://arxiv.org/abs/2610.20504
Project page: https://gr-bc.github.io/

#VLA #robotics
```

</details>

---

### [One-shot Human Video-Guided Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.19746)

**Authors:** Qi Chen, Yuwei Wu, Quan Chen, Kunpeng Gao, Jin Chen et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19746) | [PDF](https://arxiv.org/pdf/2610.19746)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios. To reduce this dependence on target-task robot data, we propose CapPro, a framework that enables a...

</details>

<details>
<summary>Share</summary>

```
One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation.

arXiv: https://arxiv.org/abs/2610.19746

#VLA #robotics
```

</details>

---

### [ACRO: Actor-Critic Rollout Orchestration](https://arxiv.org/abs/2610.19677)

**Authors:** Junhoo Lee, Seungyeon Kim, Baekseung Kim, Minkyu Kim, Suhyun Jeon et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19677) | [PDF](https://arxiv.org/pdf/2610.19677) | [Project Page](https://junhoo.me/acro)

<details>
<summary>Abstract</summary>

Executing a vision-language-action (VLA) policy involves deciding when to continue an attempt and when to intervene to improve its chances of success. We introduce ACRO, an Actor--Critic rollout orchestration layer that makes these decisions for a fixed VLA. ACRO seeks interventions that offer a more promising continuation, are physically feasible, and leave sufficient time to complete the task. A Critic learned from policy rollouts estimates success prospects to decide when to intervene and select a re-entry target along the executed trajectory. Trajectory Retraction shortcuts the visited pat...

</details>

<details>
<summary>Share</summary>

```
ACRO: Actor-Critic Rollout Orchestration

Executing a vision-language-action (VLA) policy involves deciding when to continue an attempt and when to intervene to improve its chances of success.

arXiv: https://arxiv.org/abs/2610.19677
Project page: https://junhoo.me/acro

#VLA #robotics
```

</details>

---

### [ForceBench: Benchmarking Force Integration for Robotic Manipulation](https://arxiv.org/abs/2610.19604)

**Authors:** Xuan Han, Zinuo Jin, Tianlin Li, Yunfan Lou, Xin Liu et al. (11 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19604) | [PDF](https://arxiv.org/pdf/2610.19604) | [Project Page](https://forcebench-platform.github.io/)

<details>
<summary>Abstract</summary>

Force feedback provides vision-language-action (VLA) policies with physical observations that can guide action selection and execution. However, differences in tasks, demonstrations, and control settings across existing systems hinder reliable comparisons of force integration designs. We introduce ForceBench, a simulation benchmark for evaluating six-axis wrist-force integration under a unified protocol. ForceBench combines eight tasks spanning physical-property inference, resistance-dependent interaction, and contact-rich assembly with 1,600 synchronized demonstrations and task-specific succe...

</details>

<details>
<summary>Share</summary>

```
ForceBench: Benchmarking Force Integration for Robotic Manipulation

Force feedback provides vision-language-action (VLA) policies with physical observations that can guide action selection and execution.

arXiv: https://arxiv.org/abs/2610.19604
Project page: https://forcebench-platform.github.io/

#VLA #robotics
```

</details>

---

### [Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](https://arxiv.org/abs/2610.19600)

**Authors:** Zixuan Wang, Jia-Ning Li, Yinzhou Tang, Yanzhao Yu, Biao Wu et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19600) | [PDF](https://arxiv.org/pdf/2610.19600) | [Code](https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation.git)

<details>
<summary>Abstract</summary>

Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone. To uncover these bottlenecks, we systematically diagnose failures in long-horizon mobile manipulation and identify three...

</details>

<details>
<summary>Share</summary>

```
Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System

Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation.

arXiv: https://arxiv.org/abs/2610.19600
Code: https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation.git

#VLA #robotics
```

</details>

---

### [VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning](https://arxiv.org/abs/2610.19517)

**Authors:** Diyuan Shi, Yiqi Tang, Hongyin Zhang, You Wu, Donglin Wang

**Published:** 2026-10-14 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19517) | [PDF](https://arxiv.org/pdf/2610.19517)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation. However, conventional pretrained VLA policies lack a mechanism for gradual adaptation through accumulated interaction experience during deployment. We therefore propose VLRLA, a general framework that equips existing VLA models with \textit{in-context reinforcement learning} capabilities for deployment-time adaptation. Our approach augments a VLA model with a reinforcement learning module that learns from historical observ...

</details>

<details>
<summary>Share</summary>

```
VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning

Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation.

arXiv: https://arxiv.org/abs/2610.19517

#VLA #robotics
```

</details>

---

### [The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover](https://arxiv.org/abs/2610.17746)

**Authors:** Yiqing Xu, Jiajun Wu

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17746) | [PDF](https://arxiv.org/pdf/2610.17746) | [Project Page](https://commgap.github.io/)

<details>
<summary>Abstract</summary>

A robot may know how to perform a task yet fail when a human asks for it naturally. We study this human--VLA communication gap by separating an \emph{information gap}, where task semantics, grounding, or event structure remain unresolved, from a residual \emph{execution gap}, where even a fully specified task depends on how it is organized and invoked. To do this, we characterize how people naturally express demonstrated objectives and evaluate controlled variants of the same physical tasks, with detailed analysis on $π_{0.5}$ and consistent trends on $π_0$-FAST and Cosmos3-Edge. Our study rev...

</details>

<details>
<summary>Share</summary>

```
The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover

A robot may know how to perform a task yet fail when a human asks for it naturally.

arXiv: https://arxiv.org/abs/2610.17746
Project page: https://commgap.github.io/

#VLA #robotics
```

</details>

---

### [FlashRT-PAI: Fast Kernels Are Not Fast Pipelines for Physical AI Inference](https://arxiv.org/abs/2610.24349)

**Authors:** Liang Su, David Chen, Jason Li, Kevin Guo, Teresa Lv

**Published:** 2026-10-17 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.24349) | [PDF](https://arxiv.org/pdf/2610.24349) | [Code](https://github.com/flashrt-project/FlashRT)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA), video-action (VA), and world action models (WAMs) form the backbone of modern physical AI systems, yet their real-time single-batch inference remains a defining bottleneck. Latency is dominated not by individual kernel computation, but by system-level overhead: thousands of short kernel launches, intermediate data movement across operator boundaries, and redundant recomputation across consecutive decisions. General-purpose graph compilers cannot address these costs, as they optimize individual calls in isolation and lack visibility into cross-call state semantics...

</details>

<details>
<summary>Share</summary>

```
FlashRT-PAI: Fast Kernels Are Not Fast Pipelines for Physical AI Inference

Vision-language-action (VLA), video-action (VA), and world action models (WAMs) form the backbone of modern physical AI systems, yet their real-time single-batch inference remains a defining bottleneck.

arXiv: https://arxiv.org/abs/2610.24349
Code: https://github.com/flashrt-project/FlashRT

#VLA #robotics
```

</details>

---

### [SPECTRA-VLA: Base-Fine Hyperspectral Token Transfer at Frozen Vision-Language-Action Interfaces](https://arxiv.org/abs/2610.19651)

**Authors:** Chih-Chung Hsu

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19651) | [PDF](https://arxiv.org/pdf/2610.19651)

<details>
<summary>Abstract</summary>

Hyperspectral imaging distinguishes RGB-similar objects, but a pretrained vision-language-action model needs a state its frozen decoder can use. SPECTRA-VLA provides a native-width spectral upgrade without retraining the visual encoder or action decoder. A learned continuous residual enriches each target token through its own normalized false-color reference; projection, norm control and validation-calibrated injection regulate the change. Across 86 held-out acquisitions, category balanced accuracy rises from 0.812 to 0.883. With identical residuals and scale, own-token addition improves reuse...

</details>

<details>
<summary>Share</summary>

```
SPECTRA-VLA: Base-Fine Hyperspectral Token Transfer at Frozen Vision-Language-Action Interfaces

Hyperspectral imaging distinguishes RGB-similar objects, but a pretrained vision-language-action model needs a state its frozen decoder can use.

arXiv: https://arxiv.org/abs/2610.19651

#VLA #robotics
```

</details>

---

### [AQUAACT: A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchmark](https://arxiv.org/abs/2610.25534)

**Authors:** Zhenqi Wu, Trung Tien Dong, Aditya Penumarti, Mohamed A. Fouad, Menna A. Fouad et al. (8 authors)

**Published:** 2026-10-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.25534) | [PDF](https://arxiv.org/pdf/2610.25534)

<details>
<summary>Abstract</summary>

Underwater robots support a growing range of work, from inspecting offshore structures and pipelines to surveying reefs and accompanying divers. Most of these tasks, however, are still flown by hand by a pilot, which raises the question of whether they can be carried out autonomously instead. On land, vision-language-action (VLA) models already let robots carry out tasks autonomously from language instructions, which makes them a natural candidate for taking the pilot's place. Underwater, however, there is little data to train such models. We take inspiration from how these tasks are flown tod...

</details>

<details>
<summary>Share</summary>

```
AQUAACT: A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchmark

Underwater robots support a growing range of work, from inspecting offshore structures and pipelines to surveying reefs and accompanying divers.

arXiv: https://arxiv.org/abs/2610.25534

#VLA #robotics
```

</details>

---

### [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)

**Authors:** Yujia Yang, Quan Yuan, Jiawei Fan, Yang Li, Tiange Fu et al. (8 authors)

**Published:** 2026-10-17 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24590) | [PDF](https://arxiv.org/pdf/2610.24590)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving. However, the massive parameter scale of VLAs strains onboard computational resources during real-time inference. This directly increases energy consumption and limits vehicle battery range, making it critical to minimize computational overhead without compromising driving capability and explainability. Current research on efficient VLA-based driving focuses on sequential adaptation (\textit{e.g.}, Chain-of-Thought and token adjustment), leaving structural adaptation underexplored despite parameter redundancy...

</details>

<details>
<summary>Share</summary>

```
Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing

Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving.

arXiv: https://arxiv.org/abs/2610.24590

#VLA #robotics
```

</details>

---

### [Retrieval-triggered Action Projection Adjustment for Frozen VLA Policies: An Empirical Study and Failure Analysis](https://arxiv.org/abs/2610.24573)

**Authors:** Jinming Wang, Ruiheng Zhang, Yong Wang, Zipan Xiong, Keyuan Luo

**Published:** 2026-10-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24573) | [PDF](https://arxiv.org/pdf/2610.24573)

<details>
<summary>Abstract</summary>

Frozen Vision-Language-Action (VLA) policies cannot incorporate previously encountered failures without updating the underlying model. We present retrieval-triggered projection correction (RTPC), an auditable external-memory wrapper for frozen OpenVLA policies that retrieves stress-collected local-depth records and applies translation-only projection correction while keeping rotation and gripper commands unchanged. RTPC is evaluated on CALVIN single-task manipulation using primary and independent replication cohorts. In the primary evaluation, RTPC reduced a depth-based near-collision or stall...

</details>

<details>
<summary>Share</summary>

```
Retrieval-triggered Action Projection Adjustment for Frozen VLA Policies: An Empirical Study and Failure Analysis

Frozen Vision-Language-Action (VLA) policies cannot incorporate previously encountered failures without updating the underlying model.

arXiv: https://arxiv.org/abs/2610.24573

#VLA #robotics
```

</details>

---

### [Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems](https://arxiv.org/abs/2610.23372)

**Authors:** Keyuan Luo, Yi Xie, Wanyun Ling, Yuanzhe Li, Ziyue Li et al. (6 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23372) | [PDF](https://arxiv.org/pdf/2610.23372)

<details>
<summary>Abstract</summary>

When we say that a robot uses memory, does that memory actually play a role? Success-rate ablations alone cannot establish the use of task-relevant facts: they change information and computation together, while aggregate rates can hide offsetting gains and losses. We propose an Interventional Memory Evaluation Protocol (IMEP) for vision-language-action (VLA) systems to address four questions: (1) Does memory provide a net benefit? (2) Under what conditions does memory help? (3) Do changes to memory alter task outcomes? (4) Are these effects specific to task-relevant facts? At the retrieval int...

</details>

<details>
<summary>Share</summary>

```
Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems

When we say that a robot uses memory, does that memory actually play a role?

arXiv: https://arxiv.org/abs/2610.23372

#VLA #robotics
```

</details>

---

### [From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models](https://arxiv.org/abs/2610.23319)

**Authors:** Yong Wang, Boyu Shen, Xinwei Zhang, Yizheng Li, Keyuan Luo

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23319) | [PDF](https://arxiv.org/pdf/2610.23319)

<details>
<summary>Abstract</summary>

Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare rep...

</details>

<details>
<summary>Share</summary>

```
From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models

Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences.

arXiv: https://arxiv.org/abs/2610.23319

#VLA #robotics
```

</details>

---

### [LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](https://arxiv.org/abs/2610.22372)

**Authors:** Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.22372) | [PDF](https://arxiv.org/pdf/2610.22372) | [Project Page](https://libero-perm.github.io/)

<details>
<summary>Abstract</summary>

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings; 2) how they learn single preferences from demonstrations; 3) how efficiently they acquire preferenc...

</details>

<details>
<summary>Share</summary>

```
LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality.

arXiv: https://arxiv.org/abs/2610.22372
Project page: https://libero-perm.github.io/

#VLA #robotics
```

</details>

---

### [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models](https://arxiv.org/abs/2610.21985)

**Authors:** Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen et al. (7 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.21985) | [PDF](https://arxiv.org/pdf/2610.21985)

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the c...

</details>

<details>
<summary>Share</summary>

```
VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation.

arXiv: https://arxiv.org/abs/2610.21985

#VLA #robotics
```

</details>

---

### [What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning](https://arxiv.org/abs/2610.21915)

**Authors:** Haitao Shen, Hanyu Liu, Yihan Lin, Huiping Liu, Junbo Cui et al. (10 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.21915) | [PDF](https://arxiv.org/pdf/2610.21915)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV) prediction are often added to improve policy learning, yet they compete with action prediction for the same training budget. We ask whether, under a fixed budget, allocating a substantial share of training samples to such objectives, rather than to further action prediction, can improve policy learning. We build a unified VLA framework that couples a two-stream multim...

</details>

<details>
<summary>Share</summary>

```
What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions.

arXiv: https://arxiv.org/abs/2610.21915

#VLA #robotics
```

</details>

---

### [Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution](https://arxiv.org/abs/2610.21434)

**Authors:** Minkyu Kim, Junhoo Lee, Seungyeon Kim, Suhyun Jeon, Baekseung Kim et al. (7 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.21434) | [PDF](https://arxiv.org/pdf/2610.21434)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies generate action sequences that reduce repeated inference, but deciding how much of each sequence to execute is critical to task success. Existing adaptive methods make this decision using generation stability or prediction agreement, yet these signals do not establish whether executing a candidate prefix preserves the ability to complete the task. We introduce a policy-aligned predictive verifier (PAV) that anticipates the consequences of candidate action prefixes and evaluates their compatibility with successful continuation before execution. Rather than...

</details>

<details>
<summary>Share</summary>

```
Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution

Vision-language-action (VLA) policies generate action sequences that reduce repeated inference, but deciding how much of each sequence to execute is critical to task success.

arXiv: https://arxiv.org/abs/2610.21434

#VLA #robotics
```

</details>

---

### [An Agentic Framework for Proactive Robots with Procedural Assistance Memory](https://arxiv.org/abs/2610.21211)

**Authors:** Dohyun Lee, Minho Park, Jeonghoon Park, Dongyoon Hwang, Junha Hyung et al. (8 authors)

**Published:** 2026-10-15 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.21211) | [PDF](https://arxiv.org/pdf/2610.21211) | [Project Page](https://davian-robotics.github.io/PAM/)

<details>
<summary>Abstract</summary>

Proactive robots should anticipate user needs and provide assistance before being explicitly asked. A straightforward approach is to infer human intentions from commonsense knowledge, but the same observed behavior can imply different needs across users, potentially leading to unwanted assistance. We observe that everyday routines in the real world exhibit recurring patterns, so learning these patterns can reduce ambiguity in proactive decisions. Based on this, we propose a memory-based agentic framework in which a VLM task predictor reads a Procedural Assistance Memory (PAM) alongside the cur...

</details>

<details>
<summary>Share</summary>

```
An Agentic Framework for Proactive Robots with Procedural Assistance Memory

Proactive robots should anticipate user needs and provide assistance before being explicitly asked.

arXiv: https://arxiv.org/abs/2610.21211
Project page: https://davian-robotics.github.io/PAM/

#VLA #robotics
```

</details>

---

### [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474)

**Authors:** Peidong Wang, Ying Chang, Zhiming Ma, Xiaocui Yang, Shi Feng et al. (11 authors)

**Published:** 2026-10-14 | **Categories:** cs.CL, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20474) | [PDF](https://arxiv.org/pdf/2610.20474)

<details>
<summary>Abstract</summary>

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose AdaRSI, an on-demand RSI framework for embodied agents. A coding agent first improves its skills and h...

</details>

<details>
<summary>Share</summary>

```
AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks.

arXiv: https://arxiv.org/abs/2610.20474

#VLA #robotics
```

</details>

---

### [When Do Discrete Actions Make Good Continuous Controllers?](https://arxiv.org/abs/2610.20429)

**Authors:** Zeji Yi, Soham Dasgupta, Xinyang Zhang, Koushil Sreenath, Guannan Qu et al. (8 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20429) | [PDF](https://arxiv.org/pdf/2610.20429) | [Project Page](https://iscoyizj.github.io/discrete-action-website/)

<details>
<summary>Abstract</summary>

Though modern AI models like LLMs predict discrete tokens, today's robotic foundation models represent actions as continuous vectors. In this paper, we challenge this common consensus by asking if continuous action parametrizations are superior to their discrete counterparts. We conduct an extensive comparison of single-step regression and multi-step flow variants of both continuous and discrete policies in both from-scratch single-task and multi-task VLA training, in both simulation and on real hardware. In all regimes, we find that discrete action prediction, even the most naive, uniform-bin...

</details>

<details>
<summary>Share</summary>

```
When Do Discrete Actions Make Good Continuous Controllers?

Though modern AI models like LLMs predict discrete tokens, today's robotic foundation models represent actions as continuous vectors.

arXiv: https://arxiv.org/abs/2610.20429
Project page: https://iscoyizj.github.io/discrete-action-website/

#VLA #robotics
```

</details>

---

### [MorphAct: Robot Policies Morphing with the Worlds They Act In](https://arxiv.org/abs/2610.20019)

**Authors:** Ziyan Liu, Jiting Liu, Weihong Zhong, Wenda Yu, Yeqiu Chen et al. (10 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20019) | [PDF](https://arxiv.org/pdf/2610.20019) | [Project Page](https://mint-sjtu.github.io/MorphAct.io/)

<details>
<summary>Abstract</summary>

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When different operations favor competing parameter adjustments, fitting their mixture can leave individual operations insufficiently adapted. Our atomic-task diagnostics reveal competing update directions in both vision-language and action parameters, with source-improving updates increasing loss on other tasks. This motivates MorphAct, a contextual paramete...

</details>

<details>
<summary>Share</summary>

```
MorphAct: Robot Policies Morphing with the Worlds They Act In

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions.

arXiv: https://arxiv.org/abs/2610.20019
Project page: https://mint-sjtu.github.io/MorphAct.io/

#VLA #robotics
```

</details>

---

### [Accelerating VLA Inference with Perturbation Informed Execution](https://arxiv.org/abs/2610.19656)

**Authors:** Jehun Lee, Hajun Lee, Jimin Ryu, Youhan Lee, Beomseok Kang et al. (7 authors)

**Published:** 2026-10-14 (updated 2026-10-18) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19656) | [PDF](https://arxiv.org/pdf/2610.19656)

<details>
<summary>Abstract</summary>

Action-chunking vision-language-action (VLA) models predict sequences of future robot actions. Under fixed-horizon execution, the robot executes a fixedlength prefix of each predicted chunk before invoking the policy again, leaving the remaining predictions unused. For a given number of executed actions, short execution horizons require more policy calls. Extending the execution horizon amortizes policy inference cost over more actions. However, uniformly applying long horizons across episodes can limit opportunities for precise corrections. To address this limitation, we propose PICES (Pertur...

</details>

<details>
<summary>Share</summary>

```
Accelerating VLA Inference with Perturbation Informed Execution

Action-chunking vision-language-action (VLA) models predict sequences of future robot actions.

arXiv: https://arxiv.org/abs/2610.19656

#VLA #robotics
```

</details>

---

### [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2610.19479)

**Authors:** Liqian Ma, Vaibhav Saxena, Utkarsh Aashu Mishra, Shuo Cheng, Yongxin Chen et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19479) | [PDF](https://arxiv.org/pdf/2610.19479) | [Project Page](https://meta-gensim.github.io)

<details>
<summary>Abstract</summary>

Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data. However, existing approaches typically treat simulators as fixed data sources, relying on uniform generation, offline retrieval, or manual parameter alignment by domain experts. We formulate \textit{Active Generative Simulation}: optimizing a simulator's data-generation distribution to maximize downstream real-world performance. To solve this problem, we propose MetaGenSim, a meta-learning framework that trains an auxiliary rater network via meta-gradients...

</details>

<details>
<summary>Share</summary>

```
Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training

Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data.

arXiv: https://arxiv.org/abs/2610.19479
Project page: https://meta-gensim.github.io

#VLA #robotics
```

</details>

---

### [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](https://arxiv.org/abs/2610.19438)

**Authors:** Hanlong Li, Sihan Tan, Takeshi Ashizawa, Benjamin Yen, Kazuhiro Nakadai

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19438) | [PDF](https://arxiv.org/pdf/2610.19438)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies fine-tuned on LIBERO are trained and evaluated on the same ten instruction strings, and rewording the instruction changes base OpenVLA's success by -38.0 points. Test-time prompt ensembling, which improves language models, does not recover this loss in any setting we ran. Paraphrase consensus (the medoid action over K paraphrases) costs base OpenVLA 16.8 points when the training instruction is a member. Without it, the medoid of the paraphrases scores -32.4 points relative to the training instruction, and confidence-based selection scores -28.0. The same m...

</details>

<details>
<summary>Share</summary>

```
Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies

Vision-language-action (VLA) policies fine-tuned on LIBERO are trained and evaluated on the same ten instruction strings, and rewording the instruction changes base OpenVLA's success by -38.0 points.

arXiv: https://arxiv.org/abs/2610.19438

#VLA #robotics
```

</details>

---

### [ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures](https://arxiv.org/abs/2610.18650)

**Authors:** Chenru Wen, Huajian Zeng, Haokai Ding, Jian Kang, Anqing Duan et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18650) | [PDF](https://arxiv.org/pdf/2610.18650)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution. Recovery is typically learned during policy training or delegated to a monitor that triggers a scripted repair after detecting a failure. We introduce ForkCast, a predictive recovery framework that compares counterfactual futures to determine whether and how to intervene in a frozen VLA policy. At each decision point, ForkCast evaluates three candidates: executing the policy's nominal action chunk (Commit), adjusting the came...

</details>

<details>
<summary>Share</summary>

```
ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution.

arXiv: https://arxiv.org/abs/2610.18650

#VLA #robotics
```

</details>

---

### [ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models](https://arxiv.org/abs/2610.18596)

**Authors:** Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18596) | [PDF](https://arxiv.org/pdf/2610.18596) | [Project Page](https://accrue-rl.github.io)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency without addressing learner persistence across tasks. We propose ACCRUE, a continual off-policy RL framework that carries lightweight actor and critic networks across tasks, allowin...

</details>

<details>
<summary>Share</summary>

```
ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired...

arXiv: https://arxiv.org/abs/2610.18596
Project page: https://accrue-rl.github.io

#VLA #robotics
```

</details>

---

### [WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568)

**Authors:** Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.18568) | [PDF](https://arxiv.org/pdf/2610.18568)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly large-scale video pretraining. We introduce WAVE-0 (World-model-Augmented VLA Execution), a framework that bridges VLAs and WAMs through a lightweight latent world model. By connectin...

</details>

<details>
<summary>Share</summary>

```
WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences.

arXiv: https://arxiv.org/abs/2610.18568

#VLA #robotics
```

</details>

---

### [YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation](https://arxiv.org/abs/2610.17521)

**Authors:** Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17521) | [PDF](https://arxiv.org/pdf/2610.17521) | [Project Page](https://yubi-real2sim.airoa.io)

<details>
<summary>Abstract</summary>

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation. While 3D Gaussian Splatting (3DGS) enables rapid real-to-sim scene generation, the reconstruction quality required for reliable policy evaluation remains unquantified. In particular, policies relying on wrist-mounted fisheye cameras (e.g., YUBI handheld gripper data) are heavily exposed to visual artifacts (holes, floaters) in wide-angle views, directly degrading task performance. To address this, we present YUBI-Real2Sim, a unified fram...

</details>

<details>
<summary>Share</summary>

```
YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation.

arXiv: https://arxiv.org/abs/2610.17521
Project page: https://yubi-real2sim.airoa.io

#VLA #robotics
```

</details>

---

### [End-to-End Vision-Language-Action Policies for Autonomous Lunar Rover Docking](https://arxiv.org/abs/2610.19224)

**Authors:** Sitan Huang, Grace Gao

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19224) | [PDF](https://arxiv.org/pdf/2610.19224)

<details>
<summary>Abstract</summary>

Surface navigation on the Moon is subject to extreme illumination contrast and deployment-time perceptual disturbances. While modular navigation pipelines have long supported planetary rover navigation, robustness is compromised by measurement errors that propagate through hand-engineered components. End-to-end learned policies are an alternative approach to navigation, which maps observations directly to control actions without intermediate components. Vision-language-action models, in particular, have driven significant breakthroughs in robotics and autonomous vehicle research. By leveraging...

</details>

<details>
<summary>Share</summary>

```
End-to-End Vision-Language-Action Policies for Autonomous Lunar Rover Docking

Surface navigation on the Moon is subject to extreme illumination contrast and deployment-time perceptual disturbances.

arXiv: https://arxiv.org/abs/2610.19224

#VLA #robotics
```

</details>

---

### [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843)

**Authors:** Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang et al. (9 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18843) | [PDF](https://arxiv.org/pdf/2610.18843)

<details>
<summary>Abstract</summary>

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height, and gripper pads. Each axis has five severity lev...

</details>

<details>
<summary>Share</summary>

```
LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-eff...

arXiv: https://arxiv.org/abs/2610.18843

#VLA #robotics
```

</details>

---

### [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)

**Authors:** Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18774) | [PDF](https://arxiv.org/pdf/2610.18774) | [Project Page](https://greenvla.github.io/GreenWAM)

<details>
<summary>Abstract</summary>

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that describes 20 robot families, from bimanual arms to dexterous humanoids, in common joint coordinates; (...

</details>

<details>
<summary>Share</summary>

```
GreenWAM: A World Foundation Model for Robotics

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.

arXiv: https://arxiv.org/abs/2610.18774
Project page: https://greenvla.github.io/GreenWAM

#VLA #robotics
```

</details>

---

### [HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2610.26765)

**Authors:** Tianwei Luo, Yiming He, Hongjin Wu, Ting Pan, Debin Ren et al. (17 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26765) | [PDF](https://arxiv.org/pdf/2610.26765)

<details>
<summary>Abstract</summary>

General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The benchmark pairs 18,000 curated human demonstrations with 66 human-verified tasks: Core-50 supports demonstration-based learning and execution tests, while Transfer-16 evaluates asset and relation transfer, skill composition, and deformable m...

</details>

<details>
<summary>Share</summary>

```
HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands.

arXiv: https://arxiv.org/abs/2610.26765

#VLA #robotics
```

</details>

---

### [ALIGN: Aligning Condition Estimation and Expression in Advantage-Conditioned Behavior Cloning](https://arxiv.org/abs/2610.26455)

**Authors:** Zechen Wang, Zhenqi Qiu, Houlong Xiong, Suohang Zhang, Yiyu Ren et al. (11 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.26455) | [PDF](https://arxiv.org/pdf/2610.26455)

<details>
<summary>Abstract</summary>

Human-collected robot manipulation data often mix successful behavior with retries, pauses, recoveries, and failures. Advantage-Conditioned Behavior Cloning (AC-BC) can exploit such mixed-quality data, but only if the conditioning signal is both accurately constructed from offline trajectories and effectively incorporated into the policy's action-vector-field prediction. Existing pipelines can weaken this signal by thresholding estimator-derived advantage scores into noisy conditions, and by routing conditions through prompts that weakly affect the action vector field. We introduce ALIGN, a co...

</details>

<details>
<summary>Share</summary>

```
ALIGN: Aligning Condition Estimation and Expression in Advantage-Conditioned Behavior Cloning

Human-collected robot manipulation data often mix successful behavior with retries, pauses, recoveries, and failures.

arXiv: https://arxiv.org/abs/2610.26455

#VLA #robotics
```

</details>

---

### [SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning](https://arxiv.org/abs/2610.24804)

**Authors:** SeongJun Jeong, Chungwoo Lee, Gi-Cheon Kang, Byoung-Tak Zhang

**Published:** 2026-10-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24804) | [PDF](https://arxiv.org/pdf/2610.24804)

<details>
<summary>Abstract</summary>

Lifelong robot learning requires acquiring new tasks sequentially without forgetting earlier ones. With large pre-trained vision-language-action (VLA) backbones, adapter-based methods effectively mitigate this challenge. However, their task-specific adapters and selection modules accumulate with the task stream, creating a scalability challenge in on-disk storage and deployment cost under fixed onboard resource budgets. We propose SARAM, a lifelong learning framework that limits storage growth while keeping GPU memory and per-step inference cost independent of the task stream length. For each...

</details>

<details>
<summary>Share</summary>

```
SARAM: Sparse Adapter Allocation with Reuse and Merging for Lifelong Robot Learning

Lifelong robot learning requires acquiring new tasks sequentially without forgetting earlier ones.

arXiv: https://arxiv.org/abs/2610.24804

#VLA #robotics
```

</details>

---

### [EndoVLA-OOV: Language-Conditioned Out-of-View Target Acquisition in Robotic Endoscopy](https://arxiv.org/abs/2610.24747)

**Authors:** Chi Kit Ng, Yidong Zhang, Tianchun Wu, Zhiqing Tang, Hanlin Zhao et al. (12 authors)

**Published:** 2026-10-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24747) | [PDF](https://arxiv.org/pdf/2610.24747)

<details>
<summary>Abstract</summary>

The scan-then-revisit workflow of upper gastrointestinal endoscopy requires bringing a previously observed suspicious region back into view for closer inspection. Acquiring such targets requires translating anatomical and appearance descriptions into camera motions from partial observations of a confined, deformable environment. We present EndoVLA-OOV, a language-conditioned vision-language-action policy for out-of-view target acquisition in robotic endoscopy. The policy adapts a pretrained backbone to continuous two-degree-of-freedom distal bending commands and combines initial, intermediate,...

</details>

<details>
<summary>Share</summary>

```
EndoVLA-OOV: Language-Conditioned Out-of-View Target Acquisition in Robotic Endoscopy

The scan-then-revisit workflow of upper gastrointestinal endoscopy requires bringing a previously observed suspicious region back into view for closer inspection.

arXiv: https://arxiv.org/abs/2610.24747

#VLA #robotics
```

</details>

---

### [GazeAct: A Human-Gaze-Annotated Manipulation Dataset for Attention-Regularized Policies](https://arxiv.org/abs/2610.24507)

**Authors:** Anupam Pani, Wang Yuan, Qifan Wang, Yanchao Yang

**Published:** 2026-10-17 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24507) | [PDF](https://arxiv.org/pdf/2610.24507)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies must ground language instructions in the right objects, contact points, and target locations for reliable manipulation. Human gaze provides a natural signal for this grounding, but existing robot datasets rarely pair real human gaze with the multi-camera observations used by modern policies. We introduce GazeAct, a gaze-equipped real-robot manipulation dataset and training framework for multi-view VLA policies. Using screen-based teleoperation, we record gaze directly on the robot camera feed viewed by the operator, yielding 12000 demonstrations across 40...

</details>

<details>
<summary>Share</summary>

```
GazeAct: A Human-Gaze-Annotated Manipulation Dataset for Attention-Regularized Policies

Vision-language-action (VLA) policies must ground language instructions in the right objects, contact points, and target locations for reliable manipulation.

arXiv: https://arxiv.org/abs/2610.24507

#VLA #robotics
```

</details>

---

### [LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models](https://arxiv.org/abs/2610.24587)

**Authors:** Xueyang Zhou, Yangming Xu, Qianjiang Li, Guiyao Tie, Junhao Wu et al. (13 authors)

**Published:** 2026-10-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.24587) | [PDF](https://arxiv.org/pdf/2610.24587)

<details>
<summary>Abstract</summary>

LIBERO has emerged as a widely adopted benchmark for evaluating robotic manipulation policies. However, strong performance on LIBERO does not necessarily indicate robust embodied capabilities, as models may exploit benchmark-specific regularities rather than generalize to diverse operating conditions. In this work, we introduce LIBERO-Pro2.0, a comprehensive benchmark for systematically evaluating the robustness of embodied foundation models under distribution shifts. LIBERO-Pro2.0 encompasses 22 static perturbations and 20 runtime interventions across six dimensions: Condition, Environment, O...

</details>

<details>
<summary>Share</summary>

```
LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models

LIBERO has emerged as a widely adopted benchmark for evaluating robotic manipulation policies.

arXiv: https://arxiv.org/abs/2610.24587

#VLA #robotics
```

</details>

---

### [CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots](https://arxiv.org/abs/2610.23288)

**Authors:** Zicheng Liu, Haochen Wu, Jiawei He, Suyun Zhao, Huan Yang et al. (7 authors)

**Published:** 2026-10-16 (updated 2026-10-19) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23288) | [PDF](https://arxiv.org/pdf/2610.23288)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize task decomposition, allocation, and replanning, while providing limited support for adapting executable coordination when physical execution deviates from the intended behavior. We present CoEvolve, a framework that represents team coordina...

</details>

<details>
<summary>Share</summary>

```
CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots

Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots.

arXiv: https://arxiv.org/abs/2610.23288

#VLA #robotics
```

</details>

---

### [GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation](https://arxiv.org/abs/2610.23123)

**Authors:** Zeyuan Ren, Guanxun Zhao, Qi Li, Hao Wang, Wenlong Liao et al. (18 authors)

**Published:** 2026-10-16 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23123) | [PDF](https://arxiv.org/pdf/2610.23123)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models that directly regress joint-space actions avoid the deployment-time cost of inverse kinematics. However, their training objectives remain misaligned with task success, as joint-space losses ignore the unequal physical consequences of joint errors and visual conditioning lacks explicit focus on hand-object interaction regions. To address these issues, we propose a training-phase prior injection framework for fine-grained bimanual manipulation. First, a physics-grounded flow-matching loss maps the implicit clean-action estimate at every noise level through dif...

</details>

<details>
<summary>Share</summary>

```
GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation

Vision-Language-Action (VLA) models that directly regress joint-space actions avoid the deployment-time cost of inverse kinematics.

arXiv: https://arxiv.org/abs/2610.23123

#VLA #robotics
```

</details>

---

### [Unifying Embodied Foundation Models via a Model-to-Policy Formulation](https://arxiv.org/abs/2610.23053)

**Authors:** Xinyi Hong, Mingyang Ren

**Published:** 2026-10-16 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.23053) | [PDF](https://arxiv.org/pdf/2610.23053)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control. These models integrate multimodal perception and action generation, but differ in their architectures, output representations, and learning objectives. In this paper, we present a unified, architecture-agnostic probabilistic formulation for embodied foundation models based on stochastic kernels. Our formulation has two key components: (i) we characterize embodied foundation models through conditional output distributions and action-realization kernels, which to...

</details>

<details>
<summary>Share</summary>

```
Unifying Embodied Foundation Models via a Model-to-Policy Formulation

Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control.

arXiv: https://arxiv.org/abs/2610.23053

#VLA #robotics
```

</details>

---

### [Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations](https://arxiv.org/abs/2610.22576)

**Authors:** Devin Han, Hershraj Niranjani

**Published:** 2026-10-15 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.22576) | [PDF](https://arxiv.org/pdf/2610.22576)

<details>
<summary>Abstract</summary>

Flow-based policies such as $π_0$ are trained on a fixed set of embodiments, and transferring them to new ones is an open problem. To adapt a frozen $π_0$ to a new embodiment without additional demonstrations or parameter updates, we train a lightweight embodiment classifier to distinguish successful action chunks on the source body from those on the target body, using a few calibration tasks. On transfer tasks that $π_0$ saw on its source body but the classifier was never trained on, we nudge each denoising step of $π_0$ with the classifier's gradient, which estimates the direction from the d...

</details>

<details>
<summary>Share</summary>

```
Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

Flow-based policies such as $π_0$ are trained on a fixed set of embodiments, and transferring them to new ones is an open problem.

arXiv: https://arxiv.org/abs/2610.22576

#VLA #robotics
```

</details>

---

### [Causal Analysis of Robot Foundation Models Enables Efficiency Gains](https://arxiv.org/abs/2610.20750)

**Authors:** Aiden Swann, Mathilde Papillon, Mozes Jacobs, Siddharth Boppana, Tal Haklay et al. (16 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20750) | [PDF](https://arxiv.org/pdf/2610.20750)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($π_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input image and the instruction shape actions. Across the three models, activation patching shows that caus...

</details>

<details>
<summary>Share</summary>

```
Causal Analysis of Robot Foundation Models Enables Efficiency Gains

Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation.

arXiv: https://arxiv.org/abs/2610.20750

#VLA #robotics
```

</details>

---

### [Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2610.19753)

**Authors:** Yiming Meng, Yanming Shao, Weijie Shen, Kunyang Lin, Jiayu Sun et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19753) | [PDF](https://arxiv.org/pdf/2610.19753)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand interactions implicit within a single action vector. We introduce Coordi-$π$, a structured action representation for bimanual dexterous manipulation. Coordi-$π$ represents the right- and left-side arm--hand actions as individual action tokens an...

</details>

<details>
<summary>Share</summary>

```
Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space.

arXiv: https://arxiv.org/abs/2610.19753

#VLA #robotics
```

</details>

---

### [Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models](https://arxiv.org/abs/2610.20767)

**Authors:** Aiden Swann, Mozes Jacobs, Mathilde Papillon, Siddharth Boppana, David Chanin et al. (15 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20767) | [PDF](https://arxiv.org/pdf/2610.20767)

<details>
<summary>Abstract</summary>

Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover several multi-dimensional task-relevant features underlying the model's computation (e.g., perception, lan...

</details>

<details>
<summary>Share</summary>

```
Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

Can better feature discovery improve control over robot behavior through internal interventions and training data?

arXiv: https://arxiv.org/abs/2610.20767

#VLA #robotics
```

</details>

---

### [Towards Agentic Robots: Model, Data, Environment, and Harness](https://arxiv.org/abs/2610.20442)

**Authors:** Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu et al. (16 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.20442) | [PDF](https://arxiv.org/pdf/2610.20442)

<details>
<summary>Abstract</summary>

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic...

</details>

<details>
<summary>Share</summary>

```
Towards Agentic Robots: Model, Data, Environment, and Harness

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execut...

arXiv: https://arxiv.org/abs/2610.20442

#VLA #robotics
```

</details>

---

### [Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand](https://arxiv.org/abs/2610.20351)

**Authors:** Nagasrikanth Kallakuri

**Published:** 2026-10-14 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.20351) | [PDF](https://arxiv.org/pdf/2610.20351)

<details>
<summary>Abstract</summary>

Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots in industrial and general environments depends on. A human demonstration recorded on a simple and scalable device such as a mobile phone can serve as post-training data for a robot whose body differs in structure and capability from the human who recorded it. This is made possible not by retargeting the hand's motion but the object's. A capture yields a body-free record: the objec...

</details>

<details>
<summary>Share</summary>

```
Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand

Human demonstrations are today used largely for pretraining vision-language-action models, with little ability to use the same data for target-embodiment or task-oriented training, which scalable deployment of robots...

arXiv: https://arxiv.org/abs/2610.20351

#VLA #robotics
```

</details>

---

### [PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly](https://arxiv.org/abs/2610.19248)

**Authors:** Chang Liu, Sibo Tian, Litian Gong, Zhiwen Fan, Jiachen Li et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.19248) | [PDF](https://arxiv.org/pdf/2610.19248)

<details>
<summary>Abstract</summary>

Robotic disassembly of end-of-life (EoL) products requires robots to accommodate product variation, follow prerequisite sequences, and approach components precisely for contact-rich manipulation. Supervised fine-tuning (SFT) provides a practical path for adaptation, but limited and costly disassembly data cannot capture the distribution shifts arising from changing environments and product uncertainties. The policy's own rollouts record its approach attempts, and human corrections demonstrate recovery from its errors, but turning these experiences into better policy performance remains challen...

</details>

<details>
<summary>Share</summary>

```
PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly

Robotic disassembly of end-of-life (EoL) products requires robots to accommodate product variation, follow prerequisite sequences, and approach components precisely for contact-rich manipulation.

arXiv: https://arxiv.org/abs/2610.19248

#VLA #robotics
```

</details>

---

### [ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874)

**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18874) | [PDF](https://arxiv.org/pdf/2610.18874)

<details>
<summary>Abstract</summary>

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present Chunk...

</details>

<details>
<summary>Share</summary>

```
ChunkAct: Action Chunking for Agentic Robotics

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes...

arXiv: https://arxiv.org/abs/2610.18874

#VLA #robotics
```

</details>

---

### [EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning](https://arxiv.org/abs/2610.18790)

**Authors:** Haodong Yang, Runhan Huang, Bowen Zhang, Iofai Lei, Zunzhe Zhang et al. (10 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18790) | [PDF](https://arxiv.org/pdf/2610.18790)

<details>
<summary>Abstract</summary>

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve. We introduce Equilibrium Energy Control (EqC), a framework for introspective lifelong robot learning built around an explicit conditional energy landscape. EqC casts generative action refinement as equilibrium-seeking optimization, while the geometry of the refinement process reveals whether the generated behavior remains consistent with the learned landscape. This competence signal enables Energy-Gated DAgger, w...

</details>

<details>
<summary>Share</summary>

```
EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve.

arXiv: https://arxiv.org/abs/2610.18790

#VLA #robotics
```

</details>

---

### [Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments](https://arxiv.org/abs/2610.18381)

**Authors:** Zhibo Duan, Hanlin Kong, Tianran Ma, Yuze Wu, Yuxuan Xu et al. (11 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18381) | [PDF](https://arxiv.org/pdf/2610.18381)

<details>
<summary>Abstract</summary>

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the same trajectories. Existing aerial benchmarks are typically confined to single-environment settings, limiting evaluation of agents across continuous environmental transitions. When interaction is evaluated, agents are often initialized near the target, leaving the transition from navigation to interaction largely unassessed. This work introduces CrossFly, a benchmark for long-horizon...

</details>

<details>
<summary>Share</summary>

```
Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments

Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the sam...

arXiv: https://arxiv.org/abs/2610.18381

#VLA #robotics
```

</details>

---

### [DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations](https://arxiv.org/abs/2610.18373)

**Authors:** Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.18373) | [PDF](https://arxiv.org/pdf/2610.18373)

<details>
<summary>Abstract</summary>

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-invariant scene representation (DISR). The framework combines vision-language understanding and laten...

</details>

<details>
<summary>Share</summary>

```
DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways.

arXiv: https://arxiv.org/abs/2610.18373

#VLA #robotics
```

</details>

---

### [Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance](https://arxiv.org/abs/2610.17983)

**Authors:** Mohammed Daba, Waleed Abdulrahman Saleh AlAkwa

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.17983) | [PDF](https://arxiv.org/pdf/2610.17983)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets. However, these models frequently suffer from distributional convergence, a phenomenon where the policy regresses to "safe" but suboptimal mean behaviors due to mode averaging in the training data. This often results in generic grasp strategies, Convergent Defaults, that fail in constrained or long-tail scenarios. In this work, we propose a novel framework to identify and correct these behaviors without parameter updates. We...

</details>

<details>
<summary>Share</summary>

```
Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets.

arXiv: https://arxiv.org/abs/2610.17983

#VLA #robotics
```

</details>

---

### [Post-Training, Finetuning, and Steering:A Field Guide for Curating Training Data](https://arxiv.org/abs/2610.19143)

**Authors:** Maria Attarian, Yifan Ruan, Claas Voelcker, Chenyang Cao, Amy Zhang et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.19143) | [PDF](https://arxiv.org/pdf/2610.19143)

<details>
<summary>Abstract</summary>

While Vision-Language-Action models have enabled impressive cross-task transfer in zero-shot settings, \emph{adaptation} methods are often necessary to achieve consistent performance on novel tasks. However, even though a wealth of methods for adaptation have been proposed, it is unclear how to choose the best method based on available trajectories. We close this gap by studying the impact of the adaptation method under a variety of common data scenarios: on- and off-policy data, offline vs online adaptation, and whether the data contains optimal or suboptimal trajectories. Our evaluation span...

</details>

<details>
<summary>Share</summary>

```
Post-Training, Finetuning, and Steering:A Field Guide for Curating Training Data

While Vision-Language-Action models have enabled impressive cross-task transfer in zero-shot settings, \emph{adaptation} methods are often necessary to achieve consistent performance on novel tasks.

arXiv: https://arxiv.org/abs/2610.19143

#VLA #robotics
```

</details>

---

### [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792)

**Authors:** Xinyi Wang, Bangzheng Li, Hanyu Wang, Lin Zhang, Andrea Yaoyun Cui et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.18792) | [PDF](https://arxiv.org/pdf/2610.18792)

<details>
<summary>Abstract</summary>

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fin...

</details>

<details>
<summary>Share</summary>

```
SEAR: Self-Evolving Agentic Robotics

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task.

arXiv: https://arxiv.org/abs/2610.18792

#VLA #robotics
```

</details>

---

### [Memory as Weights: Internalizing Long-Term History for Streaming Videos](https://arxiv.org/abs/2610.22070)

**Authors:** Zhuoming Liu, Jinhong Lin, Lin Zhang, Yiwu Zhong, Yin Li

**Published:** 2026-10-15 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.22070) | [PDF](https://arxiv.org/pdf/2610.22070)

<details>
<summary>Abstract</summary>

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries. Existing memory mechanisms typically compress, retrieve, or cache historical observations and reintroduce them into the input context, forcing historical memory and current observations to compete for limited context. We propose MaLoW, a streaming memory framework that instead internalizes historical context into evolving lightweight parameter updates. MaLoW uses a recurrent HyperNetwork to incrementally consolidate incoming video ob...

</details>

<details>
<summary>Share</summary>

```
Memory as Weights: Internalizing Long-Term History for Streaming Videos

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries.

arXiv: https://arxiv.org/abs/2610.22070

#VLA #robotics
```

</details>

---

### [TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments](https://arxiv.org/abs/2610.17999)

**Authors:** Qingyu Lan, Zhihao Tian, Zifan Wang, Junwei Liang

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.17999) | [PDF](https://arxiv.org/pdf/2610.17999)

<details>
<summary>Abstract</summary>

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to the target robot.TRACE first injects kinematic priors into input and output projection layers and aligns nominal joint dynamics to reduce embodiment mismatch and support stable fine-tuning. It then combines encoder distillation with low-rank...

</details>

<details>
<summary>Share</summary>

```
TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch.

arXiv: https://arxiv.org/abs/2610.17999

#VLA #robotics
```

</details>

---
