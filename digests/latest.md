# What's New

Papers discovered in the run at **2026-09-11 18:59 UTC**.

**New this run:** 9

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (7)

### [IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2609.10915)

**Authors:** Kian Hosseinkhani, Qinhe Peng, George Shramko, Mehran Aghabozorgi, Jianing Qian et al. (9 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10915) | [PDF](https://arxiv.org/pdf/2609.10915) | [Project Page](https://kianhk6.github.io/IMLE-VLA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization. A leading design couples this backbone with a dedicated continuous action head trained via diffusion or flow matching. However, such heads rely on iterative multi-step sampling, for example 10 Euler steps in $π_{0.5}$. This creates an inference bottleneck that produces stop-and-go movement in the robot and slower task completion. We introduce IMLE-VLA, which replaces the iterative action head with a single-step conditional generator trained via conditional Implicit M...

</details>

<details>
<summary>Share</summary>

```
IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies

Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization.

arXiv: https://arxiv.org/abs/2609.10915
Project page: https://kianhk6.github.io/IMLE-VLA/

#VLA #robotics
```

</details>

---

### [HuRo: Robotizing Human Videos for Scalable VLA Pretraining](https://arxiv.org/abs/2609.10706)

**Authors:** Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim et al. (7 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10706) | [PDF](https://arxiv.org/pdf/2609.10706) | [Project Page](https://3587jjh.github.io/HuRo)

<details>
<summary>Abstract</summary>

Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale. To bridge the human-to-robot embodiment gap, existing approaches either robotize videos in task-matched settings or address observation and action alignment separately at scale. In this work, we systematically examine whether robotized human videos can provide effective and scalable supervision for pretraining vision-language-action (VLA) policies. To this end, we develop a robotization pipeline that converts heterogeneous human videos into robot-aligned observations an...

</details>

<details>
<summary>Share</summary>

```
HuRo: Robotizing Human Videos for Scalable VLA Pretraining

Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale.

arXiv: https://arxiv.org/abs/2609.10706
Project page: https://3587jjh.github.io/HuRo

#VLA #robotics
```

</details>

---

### [UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling](https://arxiv.org/abs/2609.11875)

**Authors:** Wei Li, Rui Shao, Jie He, Lingsen Zhang, Ziwei Liu et al. (6 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.11875) | [PDF](https://arxiv.org/pdf/2609.11875) | [Project Page](https://JiuTian-VL.github.io/UniMPA-page/)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have improved robotic manipulation, yet observation-to-action learning remains limited by a fundamental transition realizability gap, manifested in three tightly coupled problems: (i) Transition ambiguity. Visually similar current observations may correspond to different manipulation phases and imply different subsequent transitions. (ii) Prediction--execution mismatch. A visually plausible predicted future observation does not necessarily correspond to a physically realizable transition. (iii) Experience--realization mismatch. A historica...

</details>

<details>
<summary>Share</summary>

```
UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling

Recent advances in Vision-Language-Action (VLA) models have improved robotic manipulation, yet observation-to-action learning remains limited by a fundamental transition realizability gap, manifested in three tightly...

arXiv: https://arxiv.org/abs/2609.11875
Project page: https://JiuTian-VL.github.io/UniMPA-page/

#VLA #robotics
```

</details>

---

### [ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies](https://arxiv.org/abs/2609.11697)

**Authors:** Jianming Ma, Rongjun Jin, Xiaxi Si, Yang Zhang, Yiheng Li et al. (6 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.11697) | [PDF](https://arxiv.org/pdf/2609.11697)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) and World-Action Models (WAMs) have demonstrated strong capabilities in general-purpose robotic manipulation, yet their generated actions may violate hard physical constraints and therefore be unsafe or infeasible for deployment. Existing safety approaches either optimize statistical safety objectives without deterministic per-step guarantees or correct unsafe actions only during inference, creating a mismatch between policy training and execution. We introduce ActSafeGuard, a differentiable and training-aligned safeguard layer for flow-matching based policies. Act...

</details>

<details>
<summary>Share</summary>

```
ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies

Vision-Language-Action (VLA) and World-Action Models (WAMs) have demonstrated strong capabilities in general-purpose robotic manipulation, yet their generated actions may violate hard physical constraints and therefor...

arXiv: https://arxiv.org/abs/2609.11697

#VLA #robotics
```

</details>

---

### [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](https://arxiv.org/abs/2609.11308)

**Authors:** Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry

**Published:** 2026-09-10 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.11308) | [PDF](https://arxiv.org/pdf/2609.11308)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constrained design: less tool breadth, but greater interface bandwidth. 2AM makes a multimodal Agent the s...

</details>

<details>
<summary>Share</summary>

```
2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

Long-horizon robot manipulation requires memory, but not necessarily inside the action policy.

arXiv: https://arxiv.org/abs/2609.11308

#VLA #robotics
```

</details>

---

### [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2609.11310)

**Authors:** Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao et al. (8 authors)

**Published:** 2026-09-10 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.11310) | [PDF](https://arxiv.org/pdf/2609.11310)

<details>
<summary>Abstract</summary>

We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen. We identify two key design choices. First, placing prompt tokens at the cross-modal boundary between visual and text tokens outperforms other placements (10.0 vs. 8.4 mA...

</details>

<details>
<summary>Share</summary>

```
Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision.

arXiv: https://arxiv.org/abs/2609.11310

#VLA #robotics
```

</details>

---

### [When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents](https://arxiv.org/abs/2609.10873)

**Authors:** Qinzhen Ma, Ruihai Wu

**Published:** 2026-09-09 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10873) | [PDF](https://arxiv.org/pdf/2609.10873)

<details>
<summary>Abstract</summary>

Independent evaluation can reject harmful policy updates yet also prevent useful continual learning. We argue that update admission must be assessed through both error control and retained learning opportunities at a stated interaction budget. We identify a concrete failure: a range-based confidence gate cannot certify unchanged old-task behavior within otherwise substantial budgets. A standard paired-binomial construction reduces this burden when outcome disagreements are rare. We also specify certified historical-reference promotion and a round-level missed-opportunity metric. In a construct...

</details>

<details>
<summary>Share</summary>

```
When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents

Independent evaluation can reject harmful policy updates yet also prevent useful continual learning.

arXiv: https://arxiv.org/abs/2609.10873

#VLA #robotics
```

</details>

---

## World Models (2)

### [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](https://arxiv.org/abs/2609.11445)

**Authors:** Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo et al. (7 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** [arXiv](https://arxiv.org/abs/2609.11445) | [PDF](https://arxiv.org/pdf/2609.11445)

<details>
<summary>Abstract</summary>

Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components. We ask whether the internal predictive states of a frozen pretrained robotic world model already contain directly decodable failure information. Failure-Aware Readout from World Models (FARM) trains only a 33,985-parameter supervised readout over frozen VLA-JEPA predictive states, producing step-wise failure scores and causal trajectory risk. Five-fold out-of-fold evaluation across seven source tasks reaches 85.68/88.59 pooled AUROC...

</details>

<details>
<summary>Share</summary>

```
FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model

Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components.

arXiv: https://arxiv.org/abs/2609.11445

#worldmodels #robotics
```

</details>

---

### [CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising](https://arxiv.org/abs/2609.11553)

**Authors:** Hongjin Chen, Zijun Xu, Shihao Ma, Yi Zhao, Xilai Liu et al. (11 authors)

**Published:** 2026-09-10 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.11553) | [PDF](https://arxiv.org/pdf/2609.11553)

<details>
<summary>Abstract</summary>

Humanoid locomotion across complex terrain demands forward-looking exteroception to anticipate obstacles, yet this signal is unreliable in real-world deployment, failing partially and intermittently. Existing perceptive policies often assume that depth observations remain clean and in-distribution, while recent attempts to unify perceptive and blind control typically route or switch between separate sub-policies, leaving recoverable information in partially corrupted depth unexploited. We instead propose CAP, a single-stage humanoid locomotion policy that recovers this signal with a perceptive...

</details>

<details>
<summary>Share</summary>

```
CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising

Humanoid locomotion across complex terrain demands forward-looking exteroception to anticipate obstacles, yet this signal is unreliable in real-world deployment, failing partially and intermittently.

arXiv: https://arxiv.org/abs/2609.11553

#worldmodels #robotics
```

</details>

---
