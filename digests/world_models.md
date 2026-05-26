# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-26 18:25 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/abs/2605.25874v1)

**Authors:** Kaining Ying, Hengrui Hu, Siyu Ren, Jiamu Li, Fengjiao Chen et al. (9 authors)

**Published:** 2026-05-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.25874v1) | [PDF](https://arxiv.org/pdf/2605.25874v1.pdf) | [Project Page](https://meituan-longcat.github.io/WBench/) | [GitHub](https://github.com/meituan-longcat/WBench)

<details>
<summary>Abstract</summary>

Interactive world models are advancing rapidly, yet existing benchmarks cover only part of the required competencies, leaving no unified standard for systematic evaluation. To fill this gap, we introduce WBench, a comprehensive multi-turn benchmark for interactive world model evaluation along five dimensions, namely video quality, setting adherence, interaction adherence, consistency, and physics compliance. WBench contains 289 test cases and 1,058 interaction turns, where each case specifies a ...

</details>

---

### [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/abs/2605.25313v1)

**Authors:** Santosh Kumar Radha, Oktay Goktas

**Published:** 2026-05-25 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.25313v1) | [PDF](https://arxiv.org/pdf/2605.25313v1.pdf) | [GitHub](https://github.com/santoshkumarradha/uwm-jepa)

<details>
<summary>Abstract</summary>

World models for partially observed environments must imagine multiple compatible hidden futures and steer between them under counterfactual actions. Joint Embedding Predictive Architectures (JEPAs) do this in latent space, but a vector-valued latent has no internal structure for carrying the belief over hidden continuations through blind rollout. We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learne...

</details>

---

### [WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models](https://arxiv.org/abs/2605.25077v1)

**Authors:** Bohai Gu, Taiyi Wu, Yueyang Yuan, Jian Liu, Xiaocheng Lu et al. (12 authors)

**Published:** 2026-05-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.25077v1) | [PDF](https://arxiv.org/pdf/2605.25077v1.pdf) | [Project Page](https://nevsdev.github.io/WorldCraft/)

<details>
<summary>Abstract</summary>

Recent video-based world models have made pixel-space environments interactive at the camera level: users can navigate viewpoints while the model generates coherent visual continuations. Yet their action spaces remain incomplete: users can move the camera, but cannot act on individual objects. Since real-world interaction is inherently object-centric, such models remain closer to passive scene observers than truly manipulable environments. We present WorldCraft, a framework that expands interact...

</details>

---

## Other Recent Papers

### [Back to Parsimonious Latents: Learning Task-Centric World Models from Visual Foundations](https://arxiv.org/abs/2605.25620v1)

**Authors:** Minghao Fu, Fan Feng, Nicklas Hansen, Biwei Huang

**Published:** 2026-05-25 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.25620v1) | [PDF](https://arxiv.org/pdf/2605.25620v1.pdf)

<details>
<summary>Abstract</summary>

World models enable agents to predict future dynamics conditioned on actions, making the choice of latent representation central to planning and control. Such representations are often either learned directly from pixels with limited semantic structure or inherited from frozen visual foundation models with excessive task-irrelevant detail, yielding state spaces that are poorly matched to downstream planning and control. This is especially challenging in reward-free offline settings, where the mo...

</details>

---

### [Toward Native Multimodal Modeling: A Roadmap](https://arxiv.org/abs/2605.25343v1)

**Authors:** Siyu An, Junru Lu, Junnan Dong, Qiufeng Wang, Yinghui Li et al. (21 authors)

**Published:** 2026-05-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.25343v1) | [PDF](https://arxiv.org/pdf/2605.25343v1.pdf)

<details>
<summary>Abstract</summary>

Multimodal modeling represents a vital step from modality-agnostic reasoning toward world modeling. While early approaches predominantly rely on late-fusion that assembles encoders and frozen language backbones with output heads, recent efforts have shifted the paradigm toward native multimodal modeling (NMM) with the intrinsic integration of modalities for superior multimodal performance. Despite its potential, the design space of native architectures remains insufficiently defined. In this pap...

</details>

---

### [Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution](https://arxiv.org/abs/2605.25333v1)

**Authors:** Tianshuo Xu, Yichen Xie, Depu Meng, Chensheng Peng, Quentin Herau et al. (8 authors)

**Published:** 2026-05-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.25333v1) | [PDF](https://arxiv.org/pdf/2605.25333v1.pdf)

<details>
<summary>Abstract</summary>

Video world models should maintain evolving states when evidence is unobserved, yet current generators often freeze hidden states upon interruption. This is not simply a capacity problem: pretrained video diffusion transformers already possess KV-cache mechanisms capable of non-local retrieval, but they are rarely trained to use them as dynamic memory. We introduce ReMind, a framework eliciting dynamic memory behavior via memory-oriented data, event-aware training, and cache adaptation. Organize...

</details>

---

### [Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation](https://arxiv.org/abs/2605.25170v1)

**Authors:** Kordel K. France, Ovidiu Daescu

**Published:** 2026-05-24 | **Categories:** cs.LG, cs.AI, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2605.25170v1) | [PDF](https://arxiv.org/pdf/2605.25170v1.pdf)

<details>
<summary>Abstract</summary>

Training data for olfaction is scattered through disparate, non-standardized datasets that limit the ability to build representative world models. Olfactory navigation is a highly dynamic and non-stationary task that benefits from real-time continual learning. We introduce an adaptive framework called Grow-Prune-Freeze (GPF) networks that enable an agent to continually learn through growing, pruning, and freezing early layers of its policy in response to world complexity. Grounding GPFs in non-l...

</details>

---

### [Reinforcement Learning for Laser Additive Manufacturing Scan-Order Optimisation: A Bilevel Proxy--FEA Diagnostic Framework for Reward and World-Model Diagnosis](https://arxiv.org/abs/2605.25063v1)

**Authors:** Xian Wu, Haoran Li, Dongbin Zhao, Ruiyao Zhang, Yuanqi Chu et al. (6 authors)

**Published:** 2026-05-24 | **Categories:** cs.LG, cond-mat.mtrl-sci

**Links:** [arXiv](https://arxiv.org/abs/2605.25063v1) | [PDF](https://arxiv.org/pdf/2605.25063v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning offers a promising approach for scan-order optimisation in laser additive manufacturing, where sequential scan decisions critically influence thermal accumulation, residual stress, distortion, and final part quality. A central challenge in applying RL to this domain lies in reward and world-model fidelity: full finite-element analysis is computationally prohibitive for dense in-the-loop evaluation, while cheap thermo-inspired proxy metrics, though efficient, may capture on...

</details>

---

### [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/abs/2605.24892v1)

**Authors:** Baolu Li, Jingyu Qian, Rui Guo, Yilun Chen, Hanpeng Liu et al. (17 authors)

**Published:** 2026-05-24 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.24892v1) | [PDF](https://arxiv.org/pdf/2605.24892v1.pdf)

<details>
<summary>Abstract</summary>

Physical world knowledge resides mainly in videos. Equipping Vision-Language-Action (VLA) models with such knowledge is fundamental for safe and generalizable planning. Predictive world modeling enables VLA to internalize physical dynamics and long-term causality by predicting future video from past observations. However, naive next-frame prediction faces two challenges: 1) unlike semantically distinct text tokens, video tokens are low-entropy and redundant, causing prediction to degenerate into...

</details>

---
