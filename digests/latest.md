# What's New

Papers discovered in the run at **2026-11-09 23:57 UTC**.

**New this run:** 18

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use](https://arxiv.org/abs/2611.09036)

**Authors:** Mohamed Elmoghany, Kehan Li, Ruoqu Chen, Tarun Chiruvolu, Shutong Zhang et al. (14 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "Ego-Exo" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.09036) | [PDF](https://arxiv.org/pdf/2611.09036) | [Project Page](https://tooluse-dataset.github.io/)

<details>
<summary>Abstract</summary>

Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence. It requires agents to reason about object affordances, physical constraints, and manipulation strategies, especially when standard tools are unavailable. However, progress in this area is limited by the lack of real-world datasets that capture human tool-use behavior with sufficient scale, fidelity, and diversity. Existing benchmarks are often simulation-based, focus on simplified interactions, or lack detailed observations and annotations. We introduce ToolDex, a large-scale...

</details>

<details>
<summary>Share</summary>

```
ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use

Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence.

arXiv: https://arxiv.org/abs/2611.09036
Project page: https://tooluse-dataset.github.io/

#egocentric #robotlearning
```

</details>

---

### [TouchAnnotator: Multi-Source Tactile Supervision with Privileged-View Distillation](https://arxiv.org/abs/2611.09129)

**Authors:** Ao Li, Zhihao Yuan, Chubin Zhang, Kunrui Huang, Sheng Xu et al. (9 authors)

**Published:** 2026-11-06 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "egocentric video" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.09129) | [PDF](https://arxiv.org/pdf/2611.09129)

<details>
<summary>Abstract</summary>

Egocentric video captures human-object interaction at scale but rarely includes tactile labels for hidden contact and pressure. We introduce TouchAnnotator, an ego-only bimanual tactile annotator trained with multi-source tactile supervision and privileged-view distillation. A canonical hand field unifies glove pressure, geometry-derived human contact, and robot fingertip deformation from six datasets and three embodiments, while source-aware masks preserve valid targets. During training, an EMA teacher observes synchronized ego and wrist views and distills hand-local representations and tacti...

</details>

<details>
<summary>Share</summary>

```
TouchAnnotator: Multi-Source Tactile Supervision with Privileged-View Distillation

Egocentric video captures human-object interaction at scale but rarely includes tactile labels for hidden contact and pressure.

arXiv: https://arxiv.org/abs/2611.09129

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (13)

### [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation](https://arxiv.org/abs/2611.08577)

**Authors:** Meituan Robotics Team, Caicheng Wang, Chen Zhao, Chengpeng Jin, Duo Xu et al. (38 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08577) | [PDF](https://arxiv.org/pdf/2611.08577) | [Project Page](https://meituan-robotics.github.io/Meituan-Robotics-0/) | [Code](https://github.com/Meituan-Robotics/Meituan-Robotics-0)

<details>
<summary>Abstract</summary>

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced polic...

</details>

<details>
<summary>Share</summary>

```
Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation.

arXiv: https://arxiv.org/abs/2611.08577
Project page: https://meituan-robotics.github.io/Meituan-Robotics-0/
Code: https://github.com/Meituan-Robotics/Meituan-Robotics-0

#VLA #robotics
```

</details>

---

### [VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models](https://arxiv.org/abs/2611.08698)

**Authors:** Luca Macesanu, Tianluo Zhang, Aditya Patil, Archit Sharma, Kevin Angers et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08698) | [PDF](https://arxiv.org/pdf/2611.08698) | [Project Page](https://ai4ce.github.io/VICTR/)

<details>
<summary>Abstract</summary>

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning. Previous work has used retrieval-based post-training to equip pretrained vision-language-action (VLA) models with the capability for ICL by teaching them to condition action predictions on retrieved visually-relevant demonstration chunks. However, the effectiveness of retrieval hinges on selecting context relevant to the current execution stage, which visual similarity alone may not capture. We introduce VICTR, a fra...

</details>

<details>
<summary>Share</summary>

```
VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning.

arXiv: https://arxiv.org/abs/2611.08698
Project page: https://ai4ce.github.io/VICTR/

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

### [Q-OIL: Optimistic Exploration in Learning from Human Interventions](https://arxiv.org/abs/2611.08576)

**Authors:** Pranav Teegavarapu, Sriyash Poddar, Rico Qi, Cleah Winston, Krisha Khandelwal et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08576) | [PDF](https://arxiv.org/pdf/2611.08576) | [Project Page](https://weirdlabuw.github.io/qoil)

<details>
<summary>Abstract</summary>

As robots are deployed in the real world, they will inevitably make mistakes. Human interventions provide valuable feedback for improving their behavior, enabling them to adapt online to new scenarios. However, studying human-in-the-loop robot learning is difficult: real-world experiments are slow and expensive, so most algorithm development relies on simulated human models. We show that common human modeling assumptions do not match how real people intervene in practice. Through analyzing intervention data from human participants, we find that humans tend to intervene when agent progress stal...

</details>

<details>
<summary>Share</summary>

```
Q-OIL: Optimistic Exploration in Learning from Human Interventions

As robots are deployed in the real world, they will inevitably make mistakes.

arXiv: https://arxiv.org/abs/2611.08576
Project page: https://weirdlabuw.github.io/qoil

#VLA #robotics
```

</details>

---

### [ODEAction: From Predicting Chunks to Evolving Actions](https://arxiv.org/abs/2611.09672)

**Authors:** Qishen Wang, Pengxiang Ding, Shifeng Bao, Mingyang Sun, Hengtao Li et al. (17 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09672) | [PDF](https://arxiv.org/pdf/2611.09672)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically generate actions in chunks, organizing continuous robot execution into separately predicted segments and thus introducing potential discontinuities at action-chunk transitions. We propose ODEAction, a chunk-free action generation paradigm that replaces action-chunk prediction with Continuous Action Evolution. Given visual observations, language instructions, and robot proprioceptive information, ODEAction learns an action transition field defined over action space, where a transition vector characterizes the evolution rate of the current action wit...

</details>

<details>
<summary>Share</summary>

```
ODEAction: From Predicting Chunks to Evolving Actions

Vision-language-action (VLA) models typically generate actions in chunks, organizing continuous robot execution into separately predicted segments and thus introducing potential discontinuities at action-chunk transit...

arXiv: https://arxiv.org/abs/2611.09672

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

## World Models (3)

### [FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking](https://arxiv.org/abs/2611.08898)

**Authors:** Xiaorui Wang, Zeyu Sha, Mingyang Yang, David Chen Wang, Feitian Zhang

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.08898) | [PDF](https://arxiv.org/pdf/2611.08898)

<details>
<summary>Abstract</summary>

Reliable relative tracking is fundamental to cooperative autonomous underwater vehicles (AUVs), yet remains challenging under nonlinear vehicle dynamics and degraded underwater visual conditions. Active light markers improve robustness to appearance variation, but provide deliberately sparse observations that can become incomplete or corrupted by occlusion, reflections, and detection noise during dynamic motion. To address the resulting partial-observation control problem, this paper proposes FATHOM, a world-model-guided diffusion action-trajectory selection framework for sparse-marker AUV tra...

</details>

<details>
<summary>Share</summary>

```
FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking

Reliable relative tracking is fundamental to cooperative autonomous underwater vehicles (AUVs), yet remains challenging under nonlinear vehicle dynamics and degraded underwater visual conditions.

arXiv: https://arxiv.org/abs/2611.08898

#worldmodels #robotics
```

</details>

---

### [Toward the Era of Agentic Embodied Intelligence](https://arxiv.org/abs/2611.09124)

**Authors:** Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang, Yufeng Sun et al. (10 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2611.09124) | [PDF](https://arxiv.org/pdf/2611.09124)

<details>
<summary>Abstract</summary>

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execution history, and action proposals. MetaBrain provides training supervision and runtime guidance. A correction encoder and adapter absorb this knowledge into policy weights during training, while fresh codes adapt behavior with frozen weights at deployment. The action model, A2-WLA, adds motion-aware...

</details>

<details>
<summary>Share</summary>

```
Toward the Era of Agentic Embodied Intelligence

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery.

arXiv: https://arxiv.org/abs/2611.09124

#worldmodels #robotics
```

</details>

---

### [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](https://arxiv.org/abs/2611.09625)

**Authors:** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte

**Published:** 2026-11-06 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.09625) | [PDF](https://arxiv.org/pdf/2611.09625)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-Based Reinforcement Learning (TT-MBRL), using gradient descent at test time to encode the memory of e...

</details>

<details>
<summary>Share</summary>

```
Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories.

arXiv: https://arxiv.org/abs/2611.09625

#worldmodels #robotics
```

</details>

---
