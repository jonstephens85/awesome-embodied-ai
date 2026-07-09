# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-09 23:02 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534v1)

**Authors:** Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu et al. (20 authors)

**Published:** 2026-07-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.07534v1) | [PDF](https://arxiv.org/pdf/2607.07534v1.pdf) | [Project Page](https://technology.robbyant.com/lingbot-world-v2) | [GitHub](https://github.com/robbyant/lingbot-world-v2)

<details>
<summary>Abstract</summary>

We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous versio...

</details>

---

### [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559v1)

**Authors:** Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06559v1) | [PDF](https://arxiv.org/pdf/2607.06559v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/RynnWorld-4D.github.io) | [GitHub](https://github.com/alibaba-damo-academy/RynnWorld-4D)

<details>
<summary>Abstract</summary>

Robotic manipulation in the open world requires not only recognizing what a scene looks like, but also anticipating how its 3D structure moves under interaction. We argue that synchronized RGB, depth, and optical flow, namely RGB-DF, provide a physically grounded representation that captures the underlying 4D dynamics of a scene. Compared to 2D pixel videos, this multi-modal synergy aligns visual appearance with geometric structure and temporal motion, creating a representation space significant...

</details>

---

### [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558v1)

**Authors:** Haoyu Zhao, Xingyue Zhao, Hangyu Li, Biao Gong, Kehan Li et al. (9 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06558v1) | [PDF](https://arxiv.org/pdf/2607.06558v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/RynnWorld-Teleop.github.io) | [GitHub](https://github.com/alibaba-damo-academy/RynnWorld-Teleop)

<details>
<summary>Abstract</summary>

Scaling robot learning requires massive, diverse trajectory data, yet collection is currently bottlenecked by physical teleoperation, where every demonstration binds operator time to specific hardware and workspaces. We introduce digital teleoperation, a paradigm that decouples data collection from physical constraints by replacing the real robot with a generative world model. In this framework, an operator's hand-pose stream drives a robot-centric generative world model to synthesize high-fidel...

</details>

---

### [MoWorld: A Flash World Model](https://arxiv.org/abs/2607.06216v1)

**Authors:** Team Moxin, Deyi Ji, Tianrun Chen, Xin Zhang, Jiale Yang et al. (29 authors)

**Published:** 2026-07-07 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.06216v1) | [PDF](https://arxiv.org/pdf/2607.06216v1.pdf) | [Project Page](https://moxin-tech.github.io/moworld/)

<details>
<summary>Abstract</summary>

The future of World Models depends not only on scaling model capability, but also on scaling practicality and inference efficiency. High-frame-rate inference enables responsive perception, planning, and control in real-world autonomous systems. To this end, we present MoWorld, a cost-effective yet high-performance Flash World Model with an end-to-end framework spanning data generation, pre-training, distillation, and efficient inference, enabling up to 50 FPS real-time interaction with cinematic...

</details>

---

## Other Recent Papers

### [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](https://arxiv.org/abs/2607.07287v1)

**Authors:** Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen et al. (12 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07287v1) | [PDF](https://arxiv.org/pdf/2607.07287v1.pdf)

<details>
<summary>Abstract</summary>

Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...

</details>

---

### [Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators](https://arxiv.org/abs/2607.07196v1)

**Authors:** Christian Oefinger, Finn Rasmus Schäfer, Korbinian Moller, Mattia Piccinini, Johannes Betz

**Published:** 2026-07-08 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.07196v1) | [PDF](https://arxiv.org/pdf/2607.07196v1.pdf)

<details>
<summary>Abstract</summary>

Across robotics, World Models (WMs) are increasingly used to evaluate action policies by simulating the consequences of actions in an imagined world, and returning a success or safety verdict. Yet a verdict is only as trustworthy as the WM that produced it, and the WM itself needs to be certified. In video-generation WMs, fidelity metrics such as Fréchet Video Distance (FVD) reward visual realism, but ignore whether the world responds correctly to the policy's actions, including those unseen in ...

</details>

---

### [Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix](https://arxiv.org/abs/2607.06925v1)

**Authors:** Yufeng Wang, Lu Wei, Haibin Ling

**Published:** 2026-07-08 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.06925v1) | [PDF](https://arxiv.org/pdf/2607.06925v1.pdf)

<details>
<summary>Abstract</summary>

Compact world models that condition on a language goal promise to ground relations such as ``put the red block left of the blue block'' using a sparse set of explicit \emph{reference anchors}. We ask when such references actually ground a relation, and identify a trap: a goal-conditioned predictor reaches a striking $0.90$ relation-readout accuracy, yet this is \emph{instruction transcription}, not perception. Withholding the goal collapses it to chance ($0.90\!\to\!0.27$, three seeds) and a cou...

</details>

---

### [Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review](https://arxiv.org/abs/2607.06706v1)

**Authors:** Inkyu Sa, Chanoh Park, Hea-Min Lee, Donghee Noh, Ho Seok Ahn

**Published:** 2026-07-07 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.06706v1) | [PDF](https://arxiv.org/pdf/2607.06706v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models unify visual perception, natural-language understanding, and action generation within a single foundation model, allowing a robot to follow instructions such as fold the towel or fly to the red building directly from camera images. Because VLAs inherit world knowledge from internet-scale pre-training, they have become the dominant framework for learning-based manipulation, with bimanual coordination serving as the most demanding testbed: two arms with 7 degree...

</details>

---

### [Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning](https://arxiv.org/abs/2607.06501v1)

**Authors:** Anxing Xiao, Hanbo Zhang, Tianrun Hu, David Hsu

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.06501v1) | [PDF](https://arxiv.org/pdf/2607.06501v1.pdf)

<details>
<summary>Abstract</summary>

We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in human environments. In this work, we propose an open-world planning framework that enables robots to automatically generate, verify, and update h...

</details>

---

### [A Definition and Roadmap for World Models](https://arxiv.org/abs/2607.06401v1)

**Authors:** Xinyuan Chen, Haoyu Guo, Shi Guo, Bingqi Jiang, Chunhua Shen et al. (13 authors)

**Published:** 2026-07-07 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.06401v1) | [PDF](https://arxiv.org/pdf/2607.06401v1.pdf)

<details>
<summary>Abstract</summary>

World models -- internal simulators that learn the structure and dynamics of an environment -- have become one of the most actively debated concepts in AI. From model-based reinforcement learning and video generation to embodied robotics and ultimately, physical AI, researchers across AI subfields are building systems that they call "world models", yet there is no consensus on what a world model fundamentally is, what it should predict, or how it should be built. This perspective article provide...

</details>

---

### [The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?](https://arxiv.org/abs/2607.06640v1)

**Authors:** Donna Vakalis

**Published:** 2026-07-07 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.06640v1) | [PDF](https://arxiv.org/pdf/2607.06640v1.pdf)

<details>
<summary>Abstract</summary>

A learned world model is usually judged by how faithfully it reconstructs its observations or predicts reward, as though quality were something the model simply has or lacks. But what a task actually needs from a model is narrower: the few predictive coordinates its queries depend on, which we call the closure. We show that how much of that closure a latent comes to represent is set not by the model's capacity or its observations but by the dimensionality of the objective it is trained against, ...

</details>

---

### [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291v1)

**Authors:**  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge et al. (17 authors)

**Published:** 2026-07-07 | **Categories:** cs.CV, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2607.06291v1) | [PDF](https://arxiv.org/pdf/2607.06291v1.pdf)

<details>
<summary>Abstract</summary>

Game worlds have traditionally been built through labor-intensive production pipelines, making them costly to develop, difficult to customization, and expensive to modify after deployment. Recent advances in video world models offer a fundamentally different paradigm. Rather than explicitly authoring every component of a virtual environment, these models autoregressively synthesize future observations conditioned on the current world state and user interactions, enabling playable worlds to be ge...

</details>

---

### [Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon World-Model Failure](https://arxiv.org/abs/2607.05966v1)

**Authors:** Finn Rasmus Schäfer, Korbinian Moller, Yuan Gao, Christian Oefinger, Sebastian Schmidt et al. (6 authors)

**Published:** 2026-07-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.05966v1) | [PDF](https://arxiv.org/pdf/2607.05966v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon failure in world models is conventionally attributed to compounding error, a generic framing that does not distinguish what kind of error compounds. We propose a kinematic-vs-dynamic reframing: world models tend to imagine kinematically rather than dynamically. We operationalize this as the imagined Kinematic-Consistency Error, a per-step diagnostic that measures how far a rollout departs from a closed-form kinematic null, paired with a perturbation protocol that tests whether iKCE ...

</details>

---
