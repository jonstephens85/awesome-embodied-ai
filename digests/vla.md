# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-09-11 18:59 UTC

**Papers shown:** 43 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

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

### [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](https://arxiv.org/abs/2609.09119)

**Authors:** Yankai Fu, Ning Chen, Junkai Zhao, Heng Zhang, Guocai Yao et al. (8 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.09119) | [PDF](https://arxiv.org/pdf/2609.09119) | [Project Page](https://aureleopku.github.io/DeCAL)

<details>
<summary>Abstract</summary>

Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and complex contact dynamics. While recent works have incorporated tactile sensing into robotic manipulation, most approaches still rely on homogeneous multimodal fusion, lacking adaptive tactile integration and explicit modeling of physical dynamics. In this work, we present DeCAL, a physically-grounded dexterous vision-language-action model that unifies understanding, imagination and...

</details>

<details>
<summary>Share</summary>

```
DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination

Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and co...

arXiv: https://arxiv.org/abs/2609.09119
Project page: https://aureleopku.github.io/DeCAL

#VLA #robotics
```

</details>

---

### [MobileVLA-R1 2.0: RL-Enhanced Reasoning for Mobile Robot Control](https://arxiv.org/abs/2609.06251)

**Authors:** Ting Huang, Yue Huang, Zeyu Zhang, Shuicheng Yan, Hao Tang

**Published:** 2026-09-05 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06251) | [PDF](https://arxiv.org/pdf/2609.06251) | [Project Page](https://aigeeksgroup.github.io/MobileVLA-R1-2.0) | [Code](https://github.com/AIGeeksGroup/MobileVLA-R1-2.0)

<details>
<summary>Abstract</summary>

Grounding natural-language instructions into reliable and executable actions remains a fundamental challenge for vision-language-action (VLA) systems on mobile robots, due to the persistent gap between high-level semantic reasoning and low-level locomotion and manipulation control. Existing approaches often rely on implicit reasoning or monolithic action prediction, making it difficult to maintain coherent long-horizon decision making while producing precise and adaptable robot actions. To address this challenge, we propose MobileVLA-R1 2.0, an RL-enhanced VLA framework that explicitly couples...

</details>

<details>
<summary>Share</summary>

```
MobileVLA-R1 2.0: RL-Enhanced Reasoning for Mobile Robot Control

Grounding natural-language instructions into reliable and executable actions remains a fundamental challenge for vision-language-action (VLA) systems on mobile robots, due to the persistent gap between high-level sema...

arXiv: https://arxiv.org/abs/2609.06251
Project page: https://aigeeksgroup.github.io/MobileVLA-R1-2.0
Code: https://github.com/AIGeeksGroup/MobileVLA-R1-2.0

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

### [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2609.10405)

**Authors:** Haochen Niu, Shengye Dong, Hao Liu, Peiwen Lin, Wang Chuang

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10405) | [PDF](https://arxiv.org/pdf/2609.10405)

<details>
<summary>Abstract</summary>

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions. Yet Flow Matching--based vision-language-action (VLA) models typically generate actions in temporal coordinates, without explicitly modeling or systematically leveraging this frequency heterogeneity. We introduce \emph{FreqFM}, a frequency-conditioned Flow Matching framework for VLA models. It raises action frequency from an implicit trajectory property to an explicit conditioning dimension that spans the entire generation pipeline. Con...

</details>

<details>
<summary>Share</summary>

```
Frequency-Conditioned Flow Matching for Vision-Language-Action Models

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions.

arXiv: https://arxiv.org/abs/2609.10405

#VLA #robotics
```

</details>

---

### [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925)

**Authors:** Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang et al. (6 authors)

**Published:** 2026-09-09 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09925) | [PDF](https://arxiv.org/pdf/2609.09925)

<details>
<summary>Abstract</summary>

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entangles them. Second, cross-phase geometry: motions of different phases (reach, contact, grasp adjustme...

</details>

<details>
<summary>Share</summary>

```
Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass.

arXiv: https://arxiv.org/abs/2609.09925

#VLA #robotics
```

</details>

---

### [GloVLA: Let Geometry Move and Local VLA Interact for Robust Object-Centric Manipulation in Unstructured Environments](https://arxiv.org/abs/2609.06256)

**Authors:** Truong Thanh Nguyen, Huy Hoang Nguyen, Ha Anh Nguyen, Binh Khanh Dinh, Ngo Anh Vien et al. (8 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06256) | [PDF](https://arxiv.org/pdf/2609.06256) | [Project Page](https://glovla-project.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown promising generalization for language-conditioned robot manipulation, but deploying them in unstructured environments remains challenging. A single end-to-end VLA policy must simultaneously solve long-range transport of the end effector to task-relevant regions and short-horizon, contact-rich interaction upon arrival. This formulation is inefficient and brittle: small visual shifts, distractors, clutter, occlusions, or unfavorable initial gripper poses can push the policy outside the local state distribution in which it was trained, leading to tas...

</details>

<details>
<summary>Share</summary>

```
GloVLA: Let Geometry Move and Local VLA Interact for Robust Object-Centric Manipulation in Unstructured Environments

Vision-language-action (VLA) models have shown promising generalization for language-conditioned robot manipulation, but deploying them in unstructured environments remains challenging.

arXiv: https://arxiv.org/abs/2609.06256
Project page: https://glovla-project.github.io/

#VLA #robotics
```

</details>

---

### [RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?](https://arxiv.org/abs/2609.05324)

**Authors:** Zhenxuan Fan, Bo Zhang, Yutong Lin, Yuqian Yuan, Juekai Lin et al. (12 authors)

**Published:** 2026-09-04 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.05324) | [PDF](https://arxiv.org/pdf/2609.05324) | [Code](https://github.com/fanzhenxuan/RoboSPA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation. However, existing datasets and benchmarks mainly evaluate task completion under predefined settings, offering limited insight into model reasoning under increasing spatial and procedural complexity. We introduce \textbf{RoboSPA} (\textbf{Robo}t \textbf{S}patial-\textbf{P}rocedural \textbf{A}ssessment), a large-scale robotic manipulation dataset and benchmark for diagnosing embodied reasoning in VLA models. \texttt{RoboSPA} focuses on two core dimensions, Fine-Grained Spatial Reasonin...

</details>

<details>
<summary>Share</summary>

```
RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?

Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation.

arXiv: https://arxiv.org/abs/2609.05324
Code: https://github.com/fanzhenxuan/RoboSPA

#VLA #robotics
```

</details>

---

### [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)

**Authors:** Yanzhe Chen, Zechen Bai, Zhijun Cao, Wenzheng Zeng, Kevin Qinghong Lin et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.10522) | [PDF](https://arxiv.org/pdf/2609.10522) | [Project Page](https://showlab.github.io/Show-Harness)

<details>
<summary>Abstract</summary>

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging. We present Show-Harness, an Embodied Harness that enables VLMs to "play" robots through a compact semantic interface linking intent to action. Show-Harness exposes discrete semantic action units that VLMs can naturally reason over, while embodiment-specific interpreters deterministically ground them into local robot actions, keeping the VLM directly responsible for fine-grained physical decisions. Through the same interface, Show-Harness...

</details>

<details>
<summary>Share</summary>

```
Show-Harness: Just a VLM Agent Can Play Robots

Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging.

arXiv: https://arxiv.org/abs/2609.10522
Project page: https://showlab.github.io/Show-Harness

#VLA #robotics
```

</details>

---

### [RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility](https://arxiv.org/abs/2609.10021)

**Authors:** Runze Xu, Yuanfan Xu, Cuijie Xu, Shuang Dai, Yining Li et al. (7 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10021) | [PDF](https://arxiv.org/pdf/2609.10021)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data. Unlike pretraining, post-training targets task- and embodiment-specific adaptation, making it particularly sensitive to data quality. In practice, collected robot datasets often contain heterogeneous errors, including execution mistakes, sensor drift, and timestamp misalignment, which can impair post-training and policy performance. Manual inspection is costly, while existing data-cleaning...

</details>

<details>
<summary>Share</summary>

```
RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data.

arXiv: https://arxiv.org/abs/2609.10021

#VLA #robotics
```

</details>

---

### [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808)

**Authors:** M. Yunus Seker, Shobhit Aggarwal, Ruwan Wickramarachchi, Jonathan Francis, Oliver Kroemer

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.09808) | [PDF](https://arxiv.org/pdf/2609.09808) | [Project Page](https://gta2-project.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation tasks are often decomposed into behaviors or skills. However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills. As a result, these behaviors can remain too coarse to expose the geometric, control, and scene-dependent decisions required for execution. We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable object-centric task-axis components. Rather than predicting actions end-to-end or composing fixed task-le...

</details>

<details>
<summary>Share</summary>

```
GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes

Robotic manipulation tasks are often decomposed into behaviors or skills.

arXiv: https://arxiv.org/abs/2609.09808
Project page: https://gta2-project.github.io/

#VLA #robotics
```

</details>

---

### [ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models](https://arxiv.org/abs/2609.07581)

**Authors:** Songhua Yang, Ziyu Liu, Xuetao Li, Ruqi Xiao, Kangxin Zhu et al. (6 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.07581) | [PDF](https://arxiv.org/pdf/2609.07581)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are commonly adapted to new manipulation settings through additional gradient updates, which limits rapid deployment when task-specific data or compute is scarce. We present ICI-VLA, a training and retrieval framework that equips a text-action VLM with few-shot test-time adaptation through in-context demonstrations. Unlike mainstream VLA designs based on action-specific multimodal fusion, ICI-VLA retains the native text-generation interface. ICI-VLA updates its parameters only during offline training; at inference, the policy remains fixed and conditions a...

</details>

<details>
<summary>Share</summary>

```
ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models

Vision-Language-Action (VLA) policies are commonly adapted to new manipulation settings through additional gradient updates, which limits rapid deployment when task-specific data or compute is scarce.

arXiv: https://arxiv.org/abs/2609.07581

#VLA #robotics
```

</details>

---

### [MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation](https://arxiv.org/abs/2609.07047)

**Authors:** Haiyang Sun, Haoxiao Wang, Junming Chen, Weicheng Fang, Zihao Su et al. (9 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.07047) | [PDF](https://arxiv.org/pdf/2609.07047) | [Code](https://github.com/Collab-Gen/MEMOBench)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires acting on information that is no longer visible, yet Vision-Language-Action policies are usually evaluated when the current observation largely determines the next action. Existing robotic memory benchmarks expose this gap, but they still rely mainly on final task success and therefore conflate forgetting with manipulation failure. We present \textbf{MEMOBench}, a benchmark for process level memory evaluation in robotic manipulation. MEMOBench includes 30 history dependent tasks, 1{,}500 expert demonstrations, and 4{,}200 executable checkpoint instances from...

</details>

<details>
<summary>Share</summary>

```
MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation

Robotic manipulation often requires acting on information that is no longer visible, yet Vision-Language-Action policies are usually evaluated when the current observation largely determines the next action.

arXiv: https://arxiv.org/abs/2609.07047
Code: https://github.com/Collab-Gen/MEMOBench

#VLA #robotics
```

</details>

---

### [Where Success Breaks: Failure-Boundary Learning for Robust Vision-Language-Action Models](https://arxiv.org/abs/2609.06114)

**Authors:** Yanzhe Chen, Zhijun Cao, Mike Zheng Shou

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.06114) | [PDF](https://arxiv.org/pdf/2609.06114)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models adapted through supervised fine-tuning (SFT) inherit a structural asymmetry: expert demonstrations teach the policy where success behavior lies, but provide no signal about where it ceases to be reliable. We argue that robust VLA adaptation should therefore be viewed not as further demonstration fitting, but as **Failure-Boundary Learning**---the problem of *Discovering*, *Localizing*, and *Shaping* the boundary between recoverable deviations and task failure. To instantiate this view, we propose **DLS**: built on a **real-grounded behavioral prior** from fe...

</details>

<details>
<summary>Share</summary>

```
Where Success Breaks: Failure-Boundary Learning for Robust Vision-Language-Action Models

Vision-language-action (VLA) models adapted through supervised fine-tuning (SFT) inherit a structural asymmetry: expert demonstrations teach the policy where success behavior lies, but provide no signal about where it...

arXiv: https://arxiv.org/abs/2609.06114

#VLA #robotics
```

</details>

---

### [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)

**Authors:** Lin Liu, Zhicheng Bao, Lu Zhang, Ziying Song, Wu Yang et al. (8 authors)

**Published:** 2026-09-04 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.05178) | [PDF](https://arxiv.org/pdf/2609.05178) | [Project Page](https://liulin815.github.io/LIBERO-Recovery/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) or World Action (WAM) models have recently demonstrated remarkable performance in robotic manipulation. On LIBERO, SOTA method have achieved nearly 100\% success rates, seemingly suggesting that the models are ready for deployment in real world. However, near perfect performance on existing benchmarks can be misleading: success under ideal conditions does not imply real world robustness. Existing benchmarks primarily evaluate task completion from predefined initial states, while real world interactions inevitably involve failures such as failed grasps, collisions,...

</details>

<details>
<summary>Share</summary>

```
LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models

Vision-Language-Action (VLA) or World Action (WAM) models have recently demonstrated remarkable performance in robotic manipulation.

arXiv: https://arxiv.org/abs/2609.05178
Project page: https://liulin815.github.io/LIBERO-Recovery/

#VLA #robotics
```

</details>

---

### [Learning to Use Imagination: Progress-Conditioned Future Utilization for World Action Models](https://arxiv.org/abs/2609.06578)

**Authors:** Yijie Zhu, Zitong Yu, Wei Li, Hui Ma, Wen Li et al. (7 authors)

**Published:** 2026-09-06 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06578) | [PDF](https://arxiv.org/pdf/2609.06578) | [Code](https://github.com/JiuTian-VL/ProWAM)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) extend Vision-Language-Action (VLA) models by incorporating future visual dynamics into action generation. However, existing WAMs often utilize imagined futures with limited adaptation to evolving execution progress, potentially introducing distracting or unreliable predictive cues. This limitation arises from two empirically identified forms of non-uniformity in future utility: (i) at the inter-progress level, the utility of imagined futures varies across execution stages as control demands change; and (ii) at the intra-progress level, individual future latents exhi...

</details>

<details>
<summary>Share</summary>

```
Learning to Use Imagination: Progress-Conditioned Future Utilization for World Action Models

World Action Models (WAMs) extend Vision-Language-Action (VLA) models by incorporating future visual dynamics into action generation.

arXiv: https://arxiv.org/abs/2609.06578
Code: https://github.com/JiuTian-VL/ProWAM

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

### [3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints](https://arxiv.org/abs/2609.08224)

**Authors:** Ziqin Huang, Yingyue Li, Chenyangguang Zhang, Ruida Zhang, Yuxin Chen et al. (9 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.08224) | [PDF](https://arxiv.org/pdf/2609.08224) | [Code](https://github.com/ziqin-h/3DWay)

<details>
<summary>Abstract</summary>

Intermediate representations are key to bridging the modality gap between generalizable manipulation policies and large-scale pretrained vision-language models (VLMs). Among these, trajectory-based representations compactly represent motion-relevant cues, yet most existing approaches predict trajectories in 2D image space, resulting in intrinsic 3D ambiguity. Moreover, using 2D trajectories with depth still leaves the free-space waypoints ambiguous, limiting reliable 3D reasoning. To address this, we propose predicting 3D consistent waypoints (3DWay) from multi-view images. By reformulating 3D...

</details>

<details>
<summary>Share</summary>

```
3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints

Intermediate representations are key to bridging the modality gap between generalizable manipulation policies and large-scale pretrained vision-language models (VLMs).

arXiv: https://arxiv.org/abs/2609.08224
Code: https://github.com/ziqin-h/3DWay

#VLA #robotics
```

</details>

---

### [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209)

**Authors:** Weiwei Gu, Anmol Gupta, Anant Sah, Ryan Varghese, Lalitha Shreya Vanam et al. (8 authors)

**Published:** 2026-09-08 (updated 2026-09-09) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.08209) | [PDF](https://arxiv.org/pdf/2609.08209) | [Project Page](https://roboreel.github.io)

<details>
<summary>Abstract</summary>

Learning from Observation (LfO) is a fundamental robotic capability that replicates how humans and animals socially learn from each other. Beyond its biological parallels, this modality provides a practical solution for data scaling in sample-inefficient and data-starved domains like robotics. Recent work has demonstrated promising results in learning manipulation skills from human videos, yet progress in this area remains difficult to assess. Existing methods vary widely in assumptions, hardware choices, and environment setups making it difficult to draw meaningful comparisons and identify ad...

</details>

<details>
<summary>Share</summary>

```
Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation

Learning from Observation (LfO) is a fundamental robotic capability that replicates how humans and animals socially learn from each other.

arXiv: https://arxiv.org/abs/2609.08209
Project page: https://roboreel.github.io

#VLA #robotics
```

</details>

---

### [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158)

**Authors:** Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren et al. (7 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.09158) | [PDF](https://arxiv.org/pdf/2609.09158)

<details>
<summary>Abstract</summary>

We study the problem of navigating cluttered indoor environments with a humanoid robot. Unlike conventional methods that model navigation as a 2D path planning problem, humanoid traversal in cluttered environments requires continuous geometry-aware whole-body adaptation, including coordinated arm placement, torso adjustment, and gait modulation for collision-free movement through complex 3D spaces. We introduce TANGO, the first whole-body vision-language navigation framework for language-conditioned humanoid traversal in cluttered environments. Given a natural-language instruction and egocentr...

</details>

<details>
<summary>Share</summary>

```
TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

We study the problem of navigating cluttered indoor environments with a humanoid robot.

arXiv: https://arxiv.org/abs/2609.09158

#VLA #robotics
```

</details>

---

### [ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics](https://arxiv.org/abs/2609.07838)

**Authors:** Boliang Liu, Wint Yi Poe, Jingyun Di, Riccardo Trivisonno, Giuseppe Caire

**Published:** 2026-09-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.07838) | [PDF](https://arxiv.org/pdf/2609.07838)

<details>
<summary>Abstract</summary>

Connected robotics is an emerging 6G application where mobile robots follow natural-language instructions to manipulate physical objects. The Vision-Language-Action (VLA) models that enable this are too large to run on the robot; a common trend is to offload inference to the cloud. The wireless link, however, limits how much sensing data the edge can transmit per control step. Two recent lines address this constraint: semantic communication codecs compress sensor data but require channel-specific retraining, and VLA token pruners select tokens from image but ignore the channel. Our insight is...

</details>

<details>
<summary>Share</summary>

```
ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics

Connected robotics is an emerging 6G application where mobile robots follow natural-language instructions to manipulate physical objects.

arXiv: https://arxiv.org/abs/2609.07838

#VLA #robotics
```

</details>

---

### [Large Discrete Policy: Advancing Explicit Behavior Modeling with Stochastic Iterative Scoring](https://arxiv.org/abs/2609.07049)

**Authors:** Zhenxin Li, Nadine Chang, Xinglong Sun, Jingde Chen, Wenhao Yao et al. (11 authors)

**Published:** 2026-09-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.07049) | [PDF](https://arxiv.org/pdf/2609.07049) | [Project Page](https://zhenxinli.net/LargeDiscretePolicy/)

<details>
<summary>Abstract</summary>

Behavior policies are often formulated as continuous generative models, whose iterative denoising processes are expressive but difficult to interpret and prone to producing implausible actions. We propose the Large Discrete Policy (LDiP), a fully discrete behavior modeling framework that selects actions from a large vocabulary of physically plausible candidates. Rather than perturbing actions, LDiP improves expressivity through stochastic iterative scoring: it progressively re-scores and prunes candidates with score-space stochasticity, enabling fine-grained ranking and exploration among plaus...

</details>

<details>
<summary>Share</summary>

```
Large Discrete Policy: Advancing Explicit Behavior Modeling with Stochastic Iterative Scoring

Behavior policies are often formulated as continuous generative models, whose iterative denoising processes are expressive but difficult to interpret and prone to producing implausible actions.

arXiv: https://arxiv.org/abs/2609.07049
Project page: https://zhenxinli.net/LargeDiscretePolicy/

#VLA #robotics
```

</details>

---

### [ContextFlow: In-Context Flow Matching for Robot Manipulation](https://arxiv.org/abs/2609.06852)

**Authors:** Jian Ding, Xianjie Dai, Roei Herzig, Nussair Hroub, Jinjie Mai et al. (8 authors)

**Published:** 2026-09-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.06852) | [PDF](https://arxiv.org/pdf/2609.06852) | [Project Page](https://dingjiansw101.github.io/contextflow-page/)

<details>
<summary>Abstract</summary>

Although highly effective in vision and language domains, applying in-context learning to robotics remains challenging. Existing autoregressive in-context imitation methods discretize continuous actions and exacerbate the accumulation of early prediction errors through next-token prediction, limiting their generalization on unseen task configurations. Meanwhile, flow-matching policies have been explored for continuous robot control and can help mitigate compounding errors; however, in-context imitation learning within a flow-matching framework remains underexplored. To address these limitation...

</details>

<details>
<summary>Share</summary>

```
ContextFlow: In-Context Flow Matching for Robot Manipulation

Although highly effective in vision and language domains, applying in-context learning to robotics remains challenging.

arXiv: https://arxiv.org/abs/2609.06852
Project page: https://dingjiansw101.github.io/contextflow-page/

#VLA #robotics
```

</details>

---

### [VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies](https://arxiv.org/abs/2609.06508)

**Authors:** Chang Song, Bin Qian, Yan Feng, Zhijie Song

**Published:** 2026-09-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.06508) | [PDF](https://arxiv.org/pdf/2609.06508)

<details>
<summary>Abstract</summary>

Long-horizon robot manipulation with Vision-Language-Action (VLA) policies remains vulnerable to execution-time deviations, as final task success provides little information for diagnosing and correcting failures caused by action noise, object displacement, or goal misalignment. We introduce a stage-aware failure verification and Prompt Recovery framework that enables closed-loop correction of a fixed VLA policy without parameter updates or privileged simulator states. The framework introduces an observable-history-based Learned Verifier that jointly estimates manipulation progress and executi...

</details>

<details>
<summary>Share</summary>

```
VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies

Long-horizon robot manipulation with Vision-Language-Action (VLA) policies remains vulnerable to execution-time deviations, as final task success provides little information for diagnosing and correcting failures caus...

arXiv: https://arxiv.org/abs/2609.06508

#VLA #robotics
```

</details>

---

### [CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation](https://arxiv.org/abs/2609.05832)

**Authors:** Zhaohong Mai, Chao Wang, Chao Zeng, Sitong Mao, Heng Zhang et al. (7 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.05832) | [PDF](https://arxiv.org/pdf/2609.05832)

<details>
<summary>Abstract</summary>

Integrating visuomotor policies or Vision-Language-Action (VLA) models with force/torque (F/T) perception has demonstrated significant progress in imitation learning for robotic manipulation. However, existing force-aware VLA models frequently exhibit limited capability in precise force tracking and rapid successive adjustments. This deficiency stems from the limitations of action-chunk execution strategies and the substantial latency between perception and real-time control. Such limitations can lead to task failures and safety risks, particularly when the execution of an action chunk exerts...

</details>

<details>
<summary>Share</summary>

```
CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation

Integrating visuomotor policies or Vision-Language-Action (VLA) models with force/torque (F/T) perception has demonstrated significant progress in imitation learning for robotic manipulation.

arXiv: https://arxiv.org/abs/2609.05832

#VLA #robotics
```

</details>

---

### [Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action Manipulation](https://arxiv.org/abs/2609.05369)

**Authors:** Vivek Chavan, Yahuan Shi, Oliver Heimann, Kevin Haninger, Jörg Krüger

**Published:** 2026-09-04 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.05369) | [PDF](https://arxiv.org/pdf/2609.05369)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can execute short manipulation skills, but remain brittle in long-horizon procedures requiring persistent task state, dependency-aware reasoning, conditional decisions, and reliable grounding. We investigate a neuro-symbolic framework that combines learned VLA control with explicit task graphs and multimodal procedural memory. Task graphs encode action dependencies, valid transitions, and branch conditions, while memory maintains the active step, completed actions, textual context, and task-relevant visual evidence. Together, these structures guide object se...

</details>

<details>
<summary>Share</summary>

```
Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action Manipulation

Vision-language-action (VLA) models can execute short manipulation skills, but remain brittle in long-horizon procedures requiring persistent task state, dependency-aware reasoning, conditional decisions, and reliable...

arXiv: https://arxiv.org/abs/2609.05369

#VLA #robotics
```

</details>

---

### [Reasoning Without Inference Cost: Latent Semantic Scaffolding for Robot VLA Policies](https://arxiv.org/abs/2609.04893)

**Authors:** Andrew Ting Yan Li, Zhuo Li, Zhelin Yang, Zhipeng Dong, Quentin Rouxel et al. (6 authors)

**Published:** 2026-09-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.04893) | [PDF](https://arxiv.org/pdf/2609.04893)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are trained by imitation and capture what action to take but not why; adding causal reasoning improves manipulation, but current methods pay for it at inference time - generating reasoning tokens or rolling out predicted future states at every step, a cost that compounds over long horizons. We ask whether this benefit can instead be captured during training and discarded before deployment. We introduce Latent Semantic Scaffolding (LSS), an auxiliary loss applied during human-demonstration pretraining that aligns a VLA's action-token representations to text e...

</details>

<details>
<summary>Share</summary>

```
Reasoning Without Inference Cost: Latent Semantic Scaffolding for Robot VLA Policies

Vision-language-action (VLA) models are trained by imitation and capture what action to take but not why; adding causal reasoning improves manipulation, but current methods pay for it at inference time - generating re...

arXiv: https://arxiv.org/abs/2609.04893

#VLA #robotics
```

</details>

---

### [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](https://arxiv.org/abs/2609.09591)

**Authors:** Zhuodong Liu, Xiangyu Li, Chunhong Yuan, Hongyang Du, Bodong Shang et al. (8 authors)

**Published:** 2026-09-09 | **Categories:** eess.SP, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.09591) | [PDF](https://arxiv.org/pdf/2609.09591)

<details>
<summary>Abstract</summary>

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing. Vision-language-action (VLA) models offer a foundation by integrating visual perception, language understanding, and action generation into a unified closed-loop policy. However, training and adapting VLA models to distributed robotic agents introduce challenges in privacy protection, communication efficiency, and model heterogeneity. Existing federated lea...

</details>

<details>
<summary>Share</summary>

```
Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, a...

arXiv: https://arxiv.org/abs/2609.09591

#VLA #robotics
```

</details>

---

### [LayerRoute: Action-Conditioned Mixture-of-Layers Routing for Vision-Language-Action Policies](https://arxiv.org/abs/2609.06079)

**Authors:** Zheng Lu, Haoran Liao, Wanqi Zhong, Yunhe Ni, Lijie Wang et al. (12 authors)

**Published:** 2026-09-05 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.06079) | [PDF](https://arxiv.org/pdf/2609.06079)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies leverage pretrained vision-language models (VLMs) to guide action generation for robot control. VLMs provide hierarchical visual-semantic representations that evolve across layers, from local visual geometry to abstract, language-aligned semantics; different manipulation tasks may therefore require different mixtures of layer representations. Meanwhile, the action module maintains intermediate representations that evolve throughout action computation and may provide useful information for subsequent decisions. However, existing VLA interfaces offer limited...

</details>

<details>
<summary>Share</summary>

```
LayerRoute: Action-Conditioned Mixture-of-Layers Routing for Vision-Language-Action Policies

Vision-Language-Action (VLA) policies leverage pretrained vision-language models (VLMs) to guide action generation for robot control.

arXiv: https://arxiv.org/abs/2609.06079

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

### [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](https://arxiv.org/abs/2609.10243)

**Authors:** Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai et al. (10 authors)

**Published:** 2026-09-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2609.10243) | [PDF](https://arxiv.org/pdf/2609.10243)

<details>
<summary>Abstract</summary>

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world. Yet methods that perform well in simulation can degrade substantially on real robots, especially in long-horizon deformable-object manipulation, where policies must track changing states and execute reliable multi-stage bimanual interactions. Existing real-robot benchmarks mainly focus on short-horizon rigid-object tasks and offer limited coverage of long-horizon deformable manipulation. We introduce FolDeX, a physical-world benchmark built entirely from real-robot data, with gar...

</details>

<details>
<summary>Share</summary>

```
FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects

Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world.

arXiv: https://arxiv.org/abs/2609.10243

#VLA #robotics
```

</details>

---

### [GIFT: Goal-Injected Fine-Tuning for Efficient Manipulation Policy Adaptation](https://arxiv.org/abs/2609.07006)

**Authors:** Xiaoyuan Fang, Shuo Feng, Yuxuan Wang, Enhua Cheng, Peng Zhou et al. (6 authors)

**Published:** 2026-09-07 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.07006) | [PDF](https://arxiv.org/pdf/2609.07006)

<details>
<summary>Abstract</summary>

Compared with relying solely on initial observations and language instructions, predicting goal images with generative models as high-level visual guidance can significantly enhance the robustness of Vision-Language-Action (VLA) models. However, most existing foundation models have not systematically incorporated goal image conditioning due to the high computational training cost. To this end, we propose Goal-Injected Fine-Tuning (GIFT), a lightweight and efficient fine-tuning framework that seamlessly integrates generated goal images into multiple representative pretrained VLA models. Our app...

</details>

<details>
<summary>Share</summary>

```
GIFT: Goal-Injected Fine-Tuning for Efficient Manipulation Policy Adaptation

Compared with relying solely on initial observations and language instructions, predicting goal images with generative models as high-level visual guidance can significantly enhance the robustness of Vision-Language-A...

arXiv: https://arxiv.org/abs/2609.07006

#VLA #robotics
```

</details>

---

### [Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](https://arxiv.org/abs/2609.07470)

**Authors:** Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos

**Published:** 2026-09-07 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2609.07470) | [PDF](https://arxiv.org/pdf/2609.07470)

<details>
<summary>Abstract</summary>

Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible instruments produce false conclusions: a color-histogram metric rewards noise, a single-goal benchmark scores 84.6% under correct Greek and 82.6% under deliberately wrong instructions, training loss fails to predict Greek success, and singl...

</details>

<details>
<summary>Share</summary>

```
Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages.

arXiv: https://arxiv.org/abs/2609.07470

#VLA #robotics
```

</details>

---

### [RefGuard: Identity-Aware Language-Guided Robot Manipulation via Joint Target-Anchor-Frame Grounding](https://arxiv.org/abs/2609.06221)

**Authors:** Lan Wei, Kangyi Lu, Yongchen Wang, Chenmeng Bi, Qi Chen et al. (8 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.06221) | [PDF](https://arxiv.org/pdf/2609.06221)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have substantially advanced language-guided robot manipulation, yet reliable execution still hinges on identifying which physical object an instruction refers to. In cluttered scenes containing repeated objects, ambiguous anchors, or frame-dependent spatial terms, a robot can execute a geometrically valid action on a semantically compatible but unintended instance; we call this failure an identity switch. The referent is jointly determined by three coupled latent variables: the target, the anchor, and the reference frame, so committing to any one of them bef...

</details>

<details>
<summary>Share</summary>

```
RefGuard: Identity-Aware Language-Guided Robot Manipulation via Joint Target-Anchor-Frame Grounding

Vision-language-action (VLA) models have substantially advanced language-guided robot manipulation, yet reliable execution still hinges on identifying which physical object an instruction refers to.

arXiv: https://arxiv.org/abs/2609.06221

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

### [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](https://arxiv.org/abs/2609.08162)

**Authors:** Chi Wan, Kangrui Wang, Yuan Si, Pingyue Zhang, Manling Li

**Published:** 2026-09-08 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.08162) | [PDF](https://arxiv.org/pdf/2609.08162)

<details>
<summary>Abstract</summary>

How can vision-language-action (VLA) models adapt to new environments where world dynamics shift? While recent research has combined world modeling and action prediction to improve VLA performance, existing methods largely rely on pretraining on static datasets, without mechanisms for active adaptation at deployment time. As a result, these models often fail to generalize when deployed in unseen scenarios with novel object configurations or dynamics. We present WorldAgen, a unified framework that jointly learns world modeling and action prediction while enabling Test-Time Training (TTT) to ada...

</details>

<details>
<summary>Share</summary>

```
WorldAgen: Unified State-Action Prediction with Test-Time World Model Training

How can vision-language-action (VLA) models adapt to new environments where world dynamics shift?

arXiv: https://arxiv.org/abs/2609.08162

#VLA #robotics
```

</details>

---

### [No Free Checker: A Survey of Verifiers for Robot Policies](https://arxiv.org/abs/2609.09250)

**Authors:** Yang Wan, Xihang Yue, Zhirui Liu, Ziyuan Chu, Shuxun Wang et al. (10 authors)

**Published:** 2026-09-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.09250) | [PDF](https://arxiv.org/pdf/2609.09250)

<details>
<summary>Abstract</summary>

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two properties. Availability is how much a verdict costs, how early in a rollout the verdict arrives, and how often a verdict can be asked for. Availability rises as verdicts get cheaper, earlier, and denser. Credibility is how much a high score...

</details>

<details>
<summary>Share</summary>

```
No Free Checker: A Survey of Verifiers for Robot Policies

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them.

arXiv: https://arxiv.org/abs/2609.09250

#VLA #robotics
```

</details>

---

### [A4A: Cross-Embodiment Transfer of Action-Oriented 4D Affordances from Human Demonstrations](https://arxiv.org/abs/2609.05892)

**Authors:** Yifan Han, Litao Liu, Yuqi Gu, Ye Lu, Hanqing Wang et al. (10 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.05892) | [PDF](https://arxiv.org/pdf/2609.05892)

<details>
<summary>Abstract</summary>

Human demonstrations contain rich manipulation knowledge, but it remains unclear what information can be transferred effectively to robot control. Existing affordance representations are typically formulated as 2D masks, 3D regions, contact points, or actionability scores, and therefore primarily identify where interaction may occur. However, effective manipulation also requires modeling how interaction-relevant geometry evolves during task execution. To bridge this gap, we introduce action-oriented 4D affordances, which represent the language-conditioned future trajectories of interaction-rel...

</details>

<details>
<summary>Share</summary>

```
A4A: Cross-Embodiment Transfer of Action-Oriented 4D Affordances from Human Demonstrations

Human demonstrations contain rich manipulation knowledge, but it remains unclear what information can be transferred effectively to robot control.

arXiv: https://arxiv.org/abs/2609.05892

#VLA #robotics
```

</details>

---

### [A Brain-inspired Hierarchical Framework for Zero-Shot Robot Task Reasoning and Execution](https://arxiv.org/abs/2609.05985)

**Authors:** Guangming Wang, Pengfei Ye, Qizhen Ying, Yixiong Jing, Yuxiang Ma et al. (10 authors)

**Published:** 2026-09-05 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.05985) | [PDF](https://arxiv.org/pdf/2609.05985)

<details>
<summary>Abstract</summary>

Robots that follow open-ended language instructions need to connect semantic intent to visual scene understanding, geometric feasibility, object states, and physical interaction conditions. End-to-end Vision-Language-Action policies have improved cross-task generalization, but they typically map visual and language inputs directly to robot actions, leaving limited explicit structure for long-horizon decomposition, physical verification, and recovery. We present \method, a zero-shot hierarchical framework functionally inspired by the division of roles in the human brain, comprising visual perce...

</details>

<details>
<summary>Share</summary>

```
A Brain-inspired Hierarchical Framework for Zero-Shot Robot Task Reasoning and Execution

Robots that follow open-ended language instructions need to connect semantic intent to visual scene understanding, geometric feasibility, object states, and physical interaction conditions.

arXiv: https://arxiv.org/abs/2609.05985

#VLA #robotics
```

</details>

---

### [Temporal Tactile Encoding and Compliance for Intent-Aware Robot-to-Human Bimanual Handover](https://arxiv.org/abs/2609.05282)

**Authors:** Pasquale Marra, Stefano Berti, Gabriele Mario Caddeo, Lorenzo Natale

**Published:** 2026-09-04 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.05282) | [PDF](https://arxiv.org/pdf/2609.05282)

<details>
<summary>Abstract</summary>

Reliable robot-to-human handover requires the robot to infer when the person is ready to receive the object, and release it safely, comfortably, and at the right time. This is challenging because visual observations alone may not disambiguate clear taking intent from accidental contact, weak grasping, wrong-direction forces, or transient interactions. In this work we treat human-robot handover as an intrinsically multimodal problem. Our approach couples a VLA model with a compliance controller that reduces interaction forces during object transfer. We finetune the VLA model with human demonstr...

</details>

<details>
<summary>Share</summary>

```
Temporal Tactile Encoding and Compliance for Intent-Aware Robot-to-Human Bimanual Handover

Reliable robot-to-human handover requires the robot to infer when the person is ready to receive the object, and release it safely, comfortably, and at the right time.

arXiv: https://arxiv.org/abs/2609.05282

#VLA #robotics
```

</details>

---

### [What Matters, When? Diagnosing and Improving Conditional Visual Grounding in Visuomotor Imitation Policies](https://arxiv.org/abs/2609.05376)

**Authors:** Vivek Chavan, Pengtao Xie, Yahuan Shi, Oliver Heimann, Kevin Haninger et al. (6 authors)

**Published:** 2026-09-04 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.05376) | [PDF](https://arxiv.org/pdf/2609.05376)

<details>
<summary>Abstract</summary>

Visuomotor imitation policies can achieve high performance under in-distribution visual conditions yet fail when visually similar objects or receptacles are introduced. We study this behavior as a problem of conditional visual grounding: the visual target required for successful control changes with the manipulation phase and, in more complex tasks, with the observed task state. Using Action Chunking with Transformers (ACT), we systematically introduce distractor objects and receptacles with controlled color and shape similarity and localize failures to picking and placement. We find that dist...

</details>

<details>
<summary>Share</summary>

```
What Matters, When? Diagnosing and Improving Conditional Visual Grounding in Visuomotor Imitation Policies

Visuomotor imitation policies can achieve high performance under in-distribution visual conditions yet fail when visually similar objects or receptacles are introduced.

arXiv: https://arxiv.org/abs/2609.05376

#VLA #robotics
```

</details>

---
