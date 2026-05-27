# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-27 18:26 UTC

**Papers found:** 8

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

## Other Recent Papers

### [Riding the Shifting Potential: When Reactive Control Suffices for Multi-Goal Behavior](https://arxiv.org/abs/2605.27314v1)

**Authors:** Vito Mengers, Oliver Brock

**Published:** 2026-05-26 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2605.27314v1) | [PDF](https://arxiv.org/pdf/2605.27314v1.pdf)

<details>
<summary>Abstract</summary>

Reactive control is often considered insufficient for multi-objective tasks because conflicting objectives give rise to local minima. We argue this limitation is not inherent but arises from static encodings that fail to reflect how objectives currently interact. We exploit the interaction structure encoded in a graph-based world model by extending it with nullspace projections: conflicts are resolved where they arise by projecting lower-priority gradients into the nullspace of higher-priority o...

</details>

---

### [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379v1)

**Authors:** David Klindt, Yann LeCun, Randall Balestriero

**Published:** 2026-05-25 | **Categories:** stat.ML, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.26379v1) | [PDF](https://arxiv.org/pdf/2605.26379v1.pdf)

<details>
<summary>Abstract</summary>

A representation that scrambles the true degrees of freedom of the world cannot support reliable planning or compositional generalization. We prove that LeJEPA (alignment plus Gaussian regularization) linearly recovers the world's latent variables from nonlinear observations, a property known as linear identifiability, in a broad class of worlds where latents evolve under stationary, additive-noise transitions. Our main result is that among all such worlds, the Gaussian is the unique latent dist...

</details>

---

### [Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization](https://arxiv.org/abs/2605.26282v1)

**Authors:** Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang et al. (8 authors)

**Published:** 2026-05-25 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.26282v1) | [PDF](https://arxiv.org/pdf/2605.26282v1.pdf)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning (RL) can be effectively supported at scale through the use of world models. However, in practice, scaling such approaches remains fundamentally limited. A commonly recognized challenge is model bias and error compounding, which degrade long-horizon predictions. Beyond these issues, we identify a more critical yet underexplored bottleneck: a structural misalignment between search and value learning in existing world model approaches. In particular, policy improv...

</details>

---

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
