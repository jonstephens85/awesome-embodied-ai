# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-22 19:45 UTC

**Papers shown:** 75 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30044)

**Authors:** Zhaohui Yang, Quanbao Lin, Chengqi Shi, Zhenglang Weng, Jicheng Lin et al. (12 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.30044) | [PDF](https://arxiv.org/pdf/2610.30044) | [Project Page](https://sp-hlm.github.io/)

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven interface. The interface combines five task-critical body poses with a learned latent motion prior to represent spatial intent and whole-body coordination in complementary forms. SP-VLA, a vision-language-action model, first predi...

</details>

<details>
<summary>Share</summary>

```
SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation

Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control.

arXiv: https://arxiv.org/abs/2610.30044
Project page: https://sp-hlm.github.io/

#VLA #robotics
```

</details>

---

### [Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](https://arxiv.org/abs/2610.29730)

**Authors:** Johannes Keller, Albrecht M. Bloße, Adrian Lindenmeyer, Thomas Neumuth, Daniel Schneider

**Published:** 2026-10-21 | **Categories:** cs.RO, cs.LG, stat.ML | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.29730) | [PDF](https://arxiv.org/pdf/2610.29730) | [Code](https://github.com/post-hoc-vla-uncertainty/post-hoc-vla-uncertainty)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly. Disagreement within an ensemble of independently trained policies can guide these decisions, but requires training and running multiple policies. We propose post-hoc kernel-variance heads that estimate epistemic uncertainty from the embeddings of a single policy. Each head computes the conditional variance of a Gaussian process conditioned on embeddings from the training demonstrations. Fitting requires n...

</details>

<details>
<summary>Share</summary>

```
Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies

Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly.

arXiv: https://arxiv.org/abs/2610.29730
Code: https://github.com/post-hoc-vla-uncertainty/post-hoc-vla-uncertainty

#VLA #robotics
```

</details>

---

### [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)

**Authors:** Haocheng Wang, Youquan Liu, Weiyu Guo, Aokai Zhang, Donghang Wu et al. (9 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.27861) | [PDF](https://arxiv.org/pdf/2610.27861) | [Code](https://github.com/HaochengWang23/RoboCasa-Shift)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce \textbf{RoboCasa-Shift}, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matched clean-perturbed rollouts in which each pair shares the same underlying settings and differs only in the target shift, and simulator-grounded stage-aware diagnostics. We evaluate GR00T N1.5 on four long-horizon tasks that pass a predefined...

</details>

<details>
<summary>Share</summary>

```
RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation

Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks.

arXiv: https://arxiv.org/abs/2610.27861
Code: https://github.com/HaochengWang23/RoboCasa-Shift

#VLA #robotics
```

</details>

---

### [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](https://arxiv.org/abs/2610.25961)

**Authors:** Hojin Jeon, Jimin Lee, Taekwan Kim, Nayoung Oh, Taeyoung Kim et al. (9 authors)

**Published:** 2026-10-19 (updated 2026-10-21) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

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

### [NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](https://arxiv.org/abs/2610.23271)

**Authors:** Guodong Du, Wanyu Lin

**Published:** 2026-10-16 (updated 2026-10-20) | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.23271) | [PDF](https://arxiv.org/pdf/2610.23271) | [Code](https://github.com/WanyuGroup/NeurIPS2026-NestedVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can learn a wide range of robotic skills, but combining separately trained skills remains challenging. The original training data may be unavailable for joint retraining, while directly merging model weights can cause interference. We propose NestedVLA, which consolidates independently fine-tuned VLA policies without access to their original training data. Instead of merging all updates into one checkpoint, a hypernetwork embedded in the VLA generates action-expert weight updates for a selected task. Each task's compressed vision-language model update is sto...

</details>

<details>
<summary>Share</summary>

```
NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

Vision-language-action (VLA) models can learn a wide range of robotic skills, but combining separately trained skills remains challenging.

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

**Published:** 2026-10-15 (updated 2026-10-19) | **Categories:** cs.RO | **Relevance:** ★★★★☆

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

### [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](https://arxiv.org/abs/2610.29329)

**Authors:** Qinghang Liu, Conglin Wang, Zongsheng Li, Boyong He, Han Gao et al. (9 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.29329) | [PDF](https://arxiv.org/pdf/2610.29329) | [Project Page](https://qinghangliu.github.io/pal-webpage/)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reason over it at execution time, placing a heavy reasoning burden on the high-level model. To address this challenge, we propose PAL (\textbf{P}lan first, \textbf{A}ct \textbf{L}ater), a hierarchical memory framework for vision-language robot manipulation. It maintains a short-term visual buffer, a semantic-event memory, and an executable \texttt{subtask\_list}. A high-level visio...

</details>

<details>
<summary>Share</summary>

```
Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window.

arXiv: https://arxiv.org/abs/2610.29329
Project page: https://qinghangliu.github.io/pal-webpage/

#VLA #robotics
```

</details>

---

### [Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.28166)

**Authors:** Matteo Cercola, Katie Z Luo, Milan Ganai, John Alora, Simone Formentin et al. (6 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28166) | [PDF](https://arxiv.org/pdf/2610.28166)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies increasingly reason before acting, but existing reasoning models compress this intermediate decision into a single representation. When several plans are valid, this commitment hides alternatives that could otherwise be selected or revised. We introduce the Generative Plan Latent (GPL), which represents the reasoning state as a low-dimensional conditional distribution over plans, such as which object, grasp, or route to use. This makes the reasoning state addressable: without retraining the VLA, plans can be sampled (coverage), selected on request (steerin...

</details>

<details>
<summary>Share</summary>

```
Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models

Vision-Language-Action (VLA) policies increasingly reason before acting, but existing reasoning models compress this intermediate decision into a single representation.

arXiv: https://arxiv.org/abs/2610.28166

#VLA #robotics
```

</details>

---

### [FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models](https://arxiv.org/abs/2610.28109)

**Authors:** Jiatong Li, Jisheng Dang, Qiangqiang Ma, Bimei Wang, Jingwen Zhao et al. (9 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28109) | [PDF](https://arxiv.org/pdf/2610.28109)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks. However, their reliability can degrade substantially when task conditions deviate from the nominal setting. Perturbations in object positions and task instructions may lead to complete task failure. Existing VLA policies generally lack an explicit runtime mechanism for distinguishing these failure modes and selecting an appropriate recovery strategy. To systematically mitigate this issue, we propose FIT-MAC, a failure-aware, closed-loop multi-agent control framework for improving t...

</details>

<details>
<summary>Share</summary>

```
FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models

Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks.

arXiv: https://arxiv.org/abs/2610.28109

#VLA #robotics
```

</details>

---

### [VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse](https://arxiv.org/abs/2610.25043)

**Authors:** Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu et al. (13 authors)

**Published:** 2026-10-18 (updated 2026-10-21) | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

### [GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.29866)

**Authors:** Qinfan Zhang, Yifan Luo, Haoyuan Shi, Guanlin Liu, Han Dong et al. (9 authors)

**Published:** 2026-10-21 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29866) | [PDF](https://arxiv.org/pdf/2610.29866)

<details>
<summary>Abstract</summary>

Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persistent task representation. Our key insight is that action generation needs a compact, task-relevant geometric abstraction that can be continuously updated, rather than a complete, renderable 3D reconstruction at every step. We introduce GeoMem-...

</details>

<details>
<summary>Share</summary>

```
GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

Geometric structure is essential for robotic manipulation and understanding the 3D world.

arXiv: https://arxiv.org/abs/2610.29866

#VLA #robotics
```

</details>

---

### [Agentic World Action Models](https://arxiv.org/abs/2610.30136)

**Authors:** Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang et al. (18 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.30136) | [PDF](https://arxiv.org/pdf/2610.30136) | [Project Page](https://agentic-wam.github.io/)

<details>
<summary>Abstract</summary>

Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. We introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and action prediction. We jointly model code, future video, and robot actions as three coupled generative streams within a unified mixture-of-transformers architecture. Within this architec...

</details>

<details>
<summary>Share</summary>

```
Agentic World Action Models

Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse.

arXiv: https://arxiv.org/abs/2610.30136
Project page: https://agentic-wam.github.io/

#VLA #robotics
```

</details>

---

### [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](https://arxiv.org/abs/2610.29203)

**Authors:** Josh Qixuan Sun, Xiaoying Xing, Yurun Chen, Huaiyuan Weng, Wentao Zhu et al. (6 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29203) | [PDF](https://arxiv.org/pdf/2610.29203)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) navigation models translate visual observations and instructions into actions. Navigation success assesses whether an agent reaches the goal. However, reaching the goal successfully does not establish whether the model genuinely follows the instructions or relies on visual cues or navigation history. We introduce NavBind to diagnose instruction-action binding: whether changing the instruction influences the probabilistic distribution of the actions, with the navigation context fixed. We construct 3,252 route-fork contexts by recombining route-aligned instruction se...

</details>

<details>
<summary>Share</summary>

```
NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs

Vision-language-action (VLA) navigation models translate visual observations and instructions into actions.

arXiv: https://arxiv.org/abs/2610.29203

#VLA #robotics
```

</details>

---

### [SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training](https://arxiv.org/abs/2610.29161)

**Authors:** Caicheng Wang, Zipeng Ye, Zhexuan Zhou, Zilong Huang, Xi Zhang et al. (6 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29161) | [PDF](https://arxiv.org/pdf/2610.29161)

<details>
<summary>Abstract</summary>

Human-in-the-loop (HIL) post-training improves vision-language-action (VLA) policies through expert corrections, but costly human supervision and repeated real-robot evaluation limit algorithm exploration and development. We introduce SimPT (Simulation-based Post-Training), a simulation framework that automates intervention-based VLA post-training by integrating policy rollouts, corrective data collection, policy training, and standalone evaluation. To automatically determine intervention timing and recovery strategies, we develop an Agent-Compiled Progress Graph that tracks task progress usin...

</details>

<details>
<summary>Share</summary>

```
SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training

Human-in-the-loop (HIL) post-training improves vision-language-action (VLA) policies through expert corrections, but costly human supervision and repeated real-robot evaluation limit algorithm exploration and developm...

arXiv: https://arxiv.org/abs/2610.29161

#VLA #robotics
```

</details>

---

### [Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs](https://arxiv.org/abs/2610.28184)

**Authors:** Matteo Cercola, Katie Z Luo, Simone Formentin, Marco Pavone

**Published:** 2026-10-20 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28184) | [PDF](https://arxiv.org/pdf/2610.28184)

<details>
<summary>Abstract</summary>

Reasoning-augmented vision-language-action (VLA) driving models can perceive and reason about safety-critical hazards yet fail to translate that evidence into safe actions. We characterize this failure as a perception-action binding gap: hazard information is available inside the model but exerts insufficient control over trajectory generation. Using matched simulated counterfactuals and logged driving replay, we show that in-path hazards are actually encoded in the visual representation, but longitudinal plans are dominated by ego-speed history and respond only weakly to hazard proximity or t...

</details>

<details>
<summary>Share</summary>

```
Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs

Reasoning-augmented vision-language-action (VLA) driving models can perceive and reason about safety-critical hazards yet fail to translate that evidence into safe actions.

arXiv: https://arxiv.org/abs/2610.28184

#VLA #robotics
```

</details>

---

### [From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation](https://arxiv.org/abs/2610.28164)

**Authors:** Xiaoxu Xu, Hao Li, Hongtao Zhang, Yili Tang, Jiafei Cao et al. (9 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28164) | [PDF](https://arxiv.org/pdf/2610.28164) | [Code](https://github.com/xuxiaoxxxx/CPR)

<details>
<summary>Abstract</summary>

Effective manipulation requires a policy to capture not only about the current scene geometry, but also about how that geometry will evolve under interaction. Existing approaches either augment policies with geometric information from current observations or introduce future prediction as auxiliary supervision, leaving open how predictive geometry should be represented for action generation. Therefore, we propose a two-stage framework, which learns complementary predictive representations from multi-view video clips. During pretraining, a frozen 3D foundation model provides dense geometric fea...

</details>

<details>
<summary>Share</summary>

```
From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation

Effective manipulation requires a policy to capture not only about the current scene geometry, but also about how that geometry will evolve under interaction.

arXiv: https://arxiv.org/abs/2610.28164
Code: https://github.com/xuxiaoxxxx/CPR

#VLA #robotics
```

</details>

---

### [PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations](https://arxiv.org/abs/2610.28019)

**Authors:** Yixiang Zhu, Ruilong Wu, Yonghao Chen, Jiaxiang Zou, Yusong Hu et al. (6 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28019) | [PDF](https://arxiv.org/pdf/2610.28019)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies are commonly deployed with asynchronous inference in real-world settings, where the next action chunk is generated while the robot is still executing the previous one. By the time the new chunk is committed, the robot and scene have changed, so the chunk is conditioned on a stale observation and task success drops sharply as this inference delay grows. Generating multiple candidate chunks could let newer observations inform the final choice, but existing multi-candidate methods either rank candidates with the stale inference-start observation or repeatedly...

</details>

<details>
<summary>Share</summary>

```
PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

Vision-language-action (VLA) policies are commonly deployed with asynchronous inference in real-world settings, where the next action chunk is generated while the robot is still executing the previous one.

arXiv: https://arxiv.org/abs/2610.28019

#VLA #robotics
```

</details>

---

### [Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880)

**Authors:** Matthew Strong, Ankush K. Dhawan, Julien Poffet, Giuse Pham, Jinho So et al. (6 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.28880) | [PDF](https://arxiv.org/pdf/2610.28880) | [Project Page](https://real2sem2real.github.io/)

<details>
<summary>Abstract</summary>

Human video scales easily and does not need robot hardware, but existing methods require depth sensing, overlay the robot onto 2D video, or generate data only for the demonstrated objects. We present Real2Sem2Real (R2Sem2R), a real-to-semantic-to-real pipeline that turns one monocular RGB video of a human demonstration into thousands of robot demonstrations across the semantic object instances of a category. R2Sem2R tracks the SE(3) pose of each object with DINOv3-distilled Gaussian splats, outperforming existing methods and FoundationPose with estimated metric depth. R2Sem2R then aligns digit...

</details>

<details>
<summary>Share</summary>

```
Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration

Human video scales easily and does not need robot hardware, but existing methods require depth sensing, overlay the robot onto 2D video, or generate data only for the demonstrated objects.

arXiv: https://arxiv.org/abs/2610.28880
Project page: https://real2sem2real.github.io/

#VLA #robotics
```

</details>

---

### [What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models](https://arxiv.org/abs/2610.27277)

**Authors:** Carson Sobolewski, Anjali Parashar, Fei Chen, Yingke Li, Chuchu Fan

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.27277) | [PDF](https://arxiv.org/pdf/2610.27277)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode. Furthermore, when several corruptions co-occur, deciding what to correct requires understanding which ones contribute to failure risk and how much their removal would help. We define this problem as failure attribution. Detecting corruption presence alone cannot answer this question, as corruptions can be present but relatively harmless, while directly measuring removal benefits requires costly pair...

</details>

<details>
<summary>Share</summary>

```
What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models

Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode.

arXiv: https://arxiv.org/abs/2610.27277

#VLA #robotics
```

</details>

---

### [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](https://arxiv.org/abs/2610.26717)

**Authors:** Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Published:** 2026-10-19 (updated 2026-10-20) | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

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

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

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

### [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](https://arxiv.org/abs/2610.27698)

**Authors:** Borui Xu, Han Chen, Bingsheng He, Ming Wu, Jason Zeng et al. (6 authors)

**Published:** 2026-10-20 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27698) | [PDF](https://arxiv.org/pdf/2610.27698)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain. Measuring this cross-dimension effect requires separating target gains from off-target changes, is...

</details>

<details>
<summary>Share</summary>

```
VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addr...

arXiv: https://arxiv.org/abs/2610.27698

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

### [AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.30097)

**Authors:** Likui Zhang, Zhe Zhu, Zhihao Zhan, Yibo Bai, Hanlin Wang et al. (10 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.30097) | [PDF](https://arxiv.org/pdf/2610.30097)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typically suffer from delayed and biased credit assignment due to trajectory-level sparse rewards, while imbalanced subtask mastery creates bottlenecks that limit overall performance. To address these challenges, we propose AtomicRL, an RL post-training framework that leverages atomic task structures for r...

</details>

<details>
<summary>Share</summary>

```
AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills.

arXiv: https://arxiv.org/abs/2610.30097

#VLA #robotics
```

</details>

---

### [FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring](https://arxiv.org/abs/2610.29692)

**Authors:** Liwen Yang, Yutian Zhang, Jiaqi Zhai, Li Yang, Tutian Tang et al. (13 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29692) | [PDF](https://arxiv.org/pdf/2610.29692)

<details>
<summary>Abstract</summary>

During steady pouring, images and robot pose may remain nearly unchanged while transferred mass accumulates, making the return decision ambiguous for a whole-task vision-language-action (VLA) policy. We present FlowVLA, which separates motor generation from physical-completion estimation. A shared $π_{0.5}$ action expert learns approach, pour, and return with boundary-aware supervision. A target-independent estimator fuses visual, joint, wrist-wrench, and recurrent force-belief histories to maintain an estimate of transferred mass. The controller initiates return when this estimate plus predic...

</details>

<details>
<summary>Share</summary>

```
FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring

During steady pouring, images and robot pose may remain nearly unchanged while transferred mass accumulates, making the return decision ambiguous for a whole-task vision-language-action (VLA) policy.

arXiv: https://arxiv.org/abs/2610.29692

#VLA #robotics
```

</details>

---

### [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560)

**Authors:** Tingwen Du, Haoyu Guo, Hanxue Zhang, Xuanxu Wang, Junting Dong et al. (12 authors)

**Published:** 2026-10-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29560) | [PDF](https://arxiv.org/pdf/2610.29560)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-leve...

</details>

<details>
<summary>Share</summary>

```
From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation.

arXiv: https://arxiv.org/abs/2610.29560

#VLA #robotics
```

</details>

---

### [PLaCA: Learning Patch-Level Future Latent Change for Action Generation](https://arxiv.org/abs/2610.27657)

**Authors:** Zhan Yi, Yuchen Wang, Chao Li, Lei Hong, Boyuan Yang

**Published:** 2026-10-20 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27657) | [PDF](https://arxiv.org/pdf/2610.27657)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generate robot actions from visual observations and language instructions, but effective manipulation also requires anticipating how the environment will change. Existing world-action models explore future image prediction and latent dynamics modeling. However, generating complete future images can be computationally expensive, while highly compressed latent representations may obscure local changes. To address these challenges, we propose PLaCA, a world-to-action framework built around future latent change. PLaCA directly predicts spatially structured patch...

</details>

<details>
<summary>Share</summary>

```
PLaCA: Learning Patch-Level Future Latent Change for Action Generation

Vision-Language-Action (VLA) models generate robot actions from visual observations and language instructions, but effective manipulation also requires anticipating how the environment will change.

arXiv: https://arxiv.org/abs/2610.27657

#VLA #robotics
```

</details>

---

### [EventSync: Event-Driven Memory Updates for History-Dependent Manipulation](https://arxiv.org/abs/2610.27917)

**Authors:** Jingjiao Zhao, Dong Jing, Mingyu Cao, Ruochuan Shi, Xiansheng Chen et al. (7 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27917) | [PDF](https://arxiv.org/pdf/2610.27917)

<details>
<summary>Abstract</summary>

History-dependent robotic manipulation requires task context and interaction history, as the current observation alone is insufficient to determine the next action. Hierarchical frameworks use task memory for high-level subgoal reasoning and low-level policies for execution. However, memory updates require accurate completion assessment: similar observations may correspond to different execution phases, and prematurely recording completion can mislead subsequent subgoal reasoning. We present EventSync, a hierarchical framework that coordinates task reasoning and action execution through event-...

</details>

<details>
<summary>Share</summary>

```
EventSync: Event-Driven Memory Updates for History-Dependent Manipulation

History-dependent robotic manipulation requires task context and interaction history, as the current observation alone is insufficient to determine the next action.

arXiv: https://arxiv.org/abs/2610.27917

#VLA #robotics
```

</details>

---

### [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2610.26584)

**Authors:** Langzhe Gu, Chengkai Hou, Meng Li, Xinhua Wang, Xinyuan Lv et al. (15 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-10-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

**Published:** 2026-10-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

### [From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection](https://arxiv.org/abs/2610.29646)

**Authors:** Nurmukhambet Serikbayev, Abdul Basit, Muhammad Shafique

**Published:** 2026-10-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.29646) | [PDF](https://arxiv.org/pdf/2610.29646)

<details>
<summary>Abstract</summary>

Choosing among robot demonstration corpora is a ranking problem: an upstream diagnostic must preserve which candidates produce better downstream policies, not merely correlate with average performance. We study paired instruction dependence, the rate at which a demonstrator changes its first decision when only the goal changes. Across 136 independently seeded quadruped-navigation corpora, predictions developed on 56 corpora are evaluated prospectively on 80 held-out corpora. The audit is reliable and associated with downstream paired correctness, and lowers mean absolute prediction error when...

</details>

<details>
<summary>Share</summary>

```
From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection

Choosing among robot demonstration corpora is a ranking problem: an upstream diagnostic must preserve which candidates produce better downstream policies, not merely correlate with average performance.

arXiv: https://arxiv.org/abs/2610.29646

#VLA #robotics
```

</details>

---

### [KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](https://arxiv.org/abs/2610.27417)

**Authors:** Zhikang Chen, Yueqing Sun, Sen Cui, Ziang Ye, Yu Wang et al. (9 authors)

**Published:** 2026-10-20 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.27417) | [PDF](https://arxiv.org/pdf/2610.27417)

<details>
<summary>Abstract</summary>

A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPHarness, a framework that adapts the external execution harness of a frozen vision-language-action model through knowledge-probing co-evolution. Recovery knowledge supplies context-specific intervention hypotheses that guide active probing; probe outcomes reveal when these hypotheses apply and provide evidence for refin...

</details>

<details>
<summary>Share</summary>

```
KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses

A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change.

arXiv: https://arxiv.org/abs/2610.27417

#VLA #robotics
```

</details>

---

### [UniWALM: Unified World Action Language Model for Embodied Robot Control](https://arxiv.org/abs/2610.28626)

**Authors:** Rahul Sajnani, Diego Romeres, Mingyuan Zhang, Kai Gao, Carl Qi et al. (12 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28626) | [PDF](https://arxiv.org/pdf/2610.28626)

<details>
<summary>Abstract</summary>

Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior? Unlike prior approaches that attach a reasoning or vision-language model to a video-action backbone and run them as distinct stages, UniWALM unifies all...

</details>

<details>
<summary>Share</summary>

```
UniWALM: Unified World Action Language Model for Embodied Robot Control

Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared re...

arXiv: https://arxiv.org/abs/2610.28626

#VLA #robotics
```

</details>

---

### [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589)

**Authors:** Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao et al. (7 authors)

**Published:** 2026-10-20 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.28589) | [PDF](https://arxiv.org/pdf/2610.28589)

<details>
<summary>Abstract</summary>

Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harnesses requires accommodating different execution mechanisms, including VLA skill invocation and cont...

</details>

<details>
<summary>Share</summary>

```
AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks.

arXiv: https://arxiv.org/abs/2610.28589

#VLA #robotics
```

</details>

---

### [AQUAACT: A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchmark](https://arxiv.org/abs/2610.25534)

**Authors:** Zhenqi Wu, Trung Tien Dong, Aditya Penumarti, Mohamed A. Fouad, Menna A. Fouad et al. (8 authors)

**Published:** 2026-10-18 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

### [HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2610.26765)

**Authors:** Tianwei Luo, Yiming He, Hongjin Wu, Ting Pan, Debin Ren et al. (17 authors)

**Published:** 2026-10-19 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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

**Published:** 2026-10-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

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
