# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-10 17:46 UTC

**Papers found:** 7

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

## Other Recent Papers

### [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375v1)

**Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang et al. (8 authors)

**Published:** 2026-07-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.08375v1) | [PDF](https://arxiv.org/pdf/2607.08375v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-V...

</details>

---

### [Write-Protected Discrete Bottlenecks for Language-Grounded World Models: A Structural Limitation and Sufficient Fix](https://arxiv.org/abs/2607.08312v1)

**Authors:** Jiayi Fang

**Published:** 2026-07-09 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.08312v1) | [PDF](https://arxiv.org/pdf/2607.08312v1.pdf)

<details>
<summary>Abstract</summary>

How should language interface with a world model's discrete symbol system? The dominant paradigm -- end-to-end injection of LLM/VLM features into robot world models (RT-2, Octo, PaLM-E) -- implicitly assumes that language gradients can directly shape physical symbol representations. We ask whether this assumption is safe, find that it is not, and characterize the minimal architectural constraint that prevents the failure. Any language gradient entering a Gumbel-softmax-based discrete symbol bott...

</details>

---

### [Unlocking Temporal Generalization in Hamiltonian Video Dynamics Models](https://arxiv.org/abs/2607.07763v1)

**Authors:** Eli Laird, Corey Clark

**Published:** 2026-07-08 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.07763v1) | [PDF](https://arxiv.org/pdf/2607.07763v1.pdf)

<details>
<summary>Abstract</summary>

World models are typically trained to predict discrete-time physical dynamics with a fixed step size baked into the model weights, preventing prediction at variable temporal resolutions. This matters for hierarchical planning, sim-to-real transfer, and scientific or game-engine applications that must query the same dynamics at multiple timescales. Hamiltonian Generative Networks (HGN) offer a principled path forward, grounding predictions in a continuous-time energy function that is, in principl...

</details>

---

### [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](https://arxiv.org/abs/2607.07287v2)

**Authors:** Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen et al. (12 authors)

**Published:** 2026-07-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.07287v2) | [PDF](https://arxiv.org/pdf/2607.07287v2.pdf)

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
