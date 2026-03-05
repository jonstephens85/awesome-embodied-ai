# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-05 18:04 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485v1)

**Authors:** Haoran Lu, Shang Wu, Jianshu Zhang, Maojiang Su, Guo Ye et al. (12 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03485v1) | [PDF](https://arxiv.org/pdf/2603.03485v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Recent video diffusion models have achieved impressive capabilities as large-scale generative world models. However, these models often struggle with fine-grained physical consistency, exhibiting physically implausible dynamics over time. In this work, we present \textbf{Phys4D}, a pipeline for learning physics-consistent 4D world representations from video diffusion models. Phys4D adopts \textbf{a three-stage training paradigm} that progressively lifts appearance-driven video diffusion models i...

</details>

---

### [Beyond Pixel Histories: World Models with Persistent 3D State](https://arxiv.org/abs/2603.03482v1)

**Authors:** Samuel Garcin, Thomas Walker, Steven McDonagh, Tim Pearce, Hakan Bilen et al. (8 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.03482v1) | [PDF](https://arxiv.org/pdf/2603.03482v1.pdf) | [Project Page](https://francelico.github.io/persist.github.io)

<details>
<summary>Abstract</summary>

Interactive world models continually generate video by responding to a user's actions, enabling open-ended generation capabilities. However, existing models typically lack a 3D representation of the environment, meaning 3D consistency must be implicitly learned from data, and spatial memory is restricted to limited temporal context windows. This results in an unrealistic user experience and presents significant obstacles to down-stream tasks such as training agents. To address this, we present P...

</details>

---

### [Beyond Language Modeling: An Exploration of Multimodal Pretraining](https://arxiv.org/abs/2603.03276v1)

**Authors:** Shengbang Tong, David Fan, John Nguyen, Ellis Brown, Gaoyue Zhou et al. (21 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.03276v1) | [PDF](https://arxiv.org/pdf/2603.03276v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

The visual world offers a critical axis for advancing foundation models beyond language. Despite growing interest in this direction, the design space for native multimodal models remains opaque. We provide empirical clarity through controlled, from-scratch pretraining experiments, isolating the factors that govern multimodal pretraining without interference from language pretraining. We adopt the Transfusion framework, using next-token prediction for language and diffusion for vision, to train o...

</details>

---

### [Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195v1)

**Authors:** Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan et al. (9 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03195v1) | [PDF](https://arxiv.org/pdf/2603.03195v1.pdf) | [Project Page](https://fx-hit.github.io/cowvla-io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are a promising path toward embodied intelligence, yet they often overlook the predictive and temporal-causal structure underlying visual dynamics. World-model VLAs address this by predicting future frames, but waste capacity reconstructing redundant backgrounds. Latent-action VLAs encode frame-to-frame transitions compactly, but lack temporally continuous dynamic modeling and world knowledge. To overcome these limitations, we introduce CoWVLA (Chain-of-World ...

</details>

---

## Other Recent Papers

### [World Properties without World Models: Recovering Spatial and Temporal Structure from Co-occurrence Statistics in Static Word Embeddings](https://arxiv.org/abs/2603.04317v1)

**Authors:** Elan Barenholtz

**Published:** 2026-03-04 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.04317v1) | [PDF](https://arxiv.org/pdf/2603.04317v1.pdf)

<details>
<summary>Abstract</summary>

Recent work interprets the linear recoverability of geographic and temporal variables from large language model (LLM) hidden states as evidence for world-like internal representations. We test a simpler possibility: that much of the relevant structure is already latent in text itself. Applying the same class of ridge regression probes to static co-occurrence-based embeddings (GloVe and Word2Vec), we find substantial recoverable geographic signal and weaker but reliable temporal signal, with held...

</details>

---

### [IPD: Boosting Sequential Policy with Imaginary Planning Distillation in Offline Reinforcement Learning](https://arxiv.org/abs/2603.04289v1)

**Authors:** Yihao Qin, Yuanfei Wang, Hang Zhou, Peiran Liu, Hao Dong et al. (6 authors)

**Published:** 2026-03-04 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.04289v1) | [PDF](https://arxiv.org/pdf/2603.04289v1.pdf)

<details>
<summary>Abstract</summary>

Decision transformer based sequential policies have emerged as a powerful paradigm in offline reinforcement learning (RL), yet their efficacy remains constrained by the quality of static datasets and inherent architectural limitations. Specifically, these models often struggle to effectively integrate suboptimal experiences and fail to explicitly plan for an optimal policy. To bridge this gap, we propose \textbf{Imaginary Planning Distillation (IPD)}, a novel framework that seamlessly incorporat...

</details>

---

### [Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback](https://arxiv.org/abs/2603.04029v1)

**Authors:** Fabian Domberg, Georg Schildbach

**Published:** 2026-03-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.04029v1) | [PDF](https://arxiv.org/pdf/2603.04029v1.pdf)

<details>
<summary>Abstract</summary>

As learning-based robotic controllers are typically trained offline and deployed with fixed parameters, their ability to cope with unforeseen changes during operation is limited. Biologically inspired, this work presents a framework for online Continual Reinforcement Learning that enables automated adaptation during deployment. Building on DreamerV3, a model-based Reinforcement Learning algorithm, the proposed method leverages world model prediction residuals to detect out-of-distribution events...

</details>

---

### [Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism](https://arxiv.org/abs/2603.03784v1)

**Authors:** Zheyu Chen, Zhuohuan Li, Chuanhao Li

**Published:** 2026-03-04 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.03784v1) | [PDF](https://arxiv.org/pdf/2603.03784v1.pdf)

<details>
<summary>Abstract</summary>

World models are essential for planning and evaluation in agentic systems, yet existing approaches lie at two extremes: hand-engineered simulators that offer consistency and reproducibility but are costly to adapt, and implicit neural models that are flexible but difficult to constrain, verify, and debug over long horizons. We seek a principled middle ground that combines the reliability of explicit simulators with the flexibility of learned models, allowing world models to be adapted during onl...

</details>

---

### [The Controllability Trap: A Governance Framework for Military AI Agents](https://arxiv.org/abs/2603.03515v1)

**Authors:** Subramanyam Sahoo

**Published:** 2026-03-03 | **Categories:** cs.CY, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.03515v1) | [PDF](https://arxiv.org/pdf/2603.03515v1.pdf)

<details>
<summary>Abstract</summary>

Agentic AI systems - capable of goal interpretation, world modeling, planning, tool use, long-horizon operation, and autonomous coordination - introduce distinct control failures not addressed by existing safety frameworks. We identify six agentic governance failures tied to these capabilities and show how they erode meaningful human control in military settings. We propose the Agentic Military AI Governance Framework (AMAGF), a measurable architecture structured around three pillars: Preventive...

</details>

---

### [Contextual Latent World Models for Offline Meta Reinforcement Learning](https://arxiv.org/abs/2603.02935v1)

**Authors:** Mohammadreza Nakheai, Aidan Scannell, Kevin Luck, Joni Pajarinen

**Published:** 2026-03-03 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.02935v1) | [PDF](https://arxiv.org/pdf/2603.02935v1.pdf)

<details>
<summary>Abstract</summary>

Offline meta-reinforcement learning seeks to learn policies that generalize across related tasks from fixed datasets. Context-based methods infer a task representation from transition histories, but learning effective task representations without supervision remains a challenge. In parallel, latent world models have demonstrated strong self-supervised representation learning through temporal consistency. We introduce contextual latent world models, which condition latent world models on inferred...

</details>

---

### [Next Embedding Prediction Makes World Models Stronger](https://arxiv.org/abs/2603.02765v1)

**Authors:** George Bredis, Nikita Balagansky, Daniil Gavrilov, Ruslan Rakhimov

**Published:** 2026-03-03 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.02765v1) | [PDF](https://arxiv.org/pdf/2603.02765v1.pdf)

<details>
<summary>Abstract</summary>

Capturing temporal dependencies is critical for model-based reinforcement learning (MBRL) in partially observable, high-dimensional domains. We introduce NE-Dreamer, a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space. This approach enables NE-Dreamer to learn coherent, predictive state representations without reconstruction losses or auxiliar...

</details>

---

### [ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)

**Authors:** Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.02697v1) | [PDF](https://arxiv.org/pdf/2603.02697v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents ShareVerse, a video generation framework enabling multi-agent shared world modeling, addressing the gap in existing works that lack support for unified shared world construction with multi-agent interaction. ShareVerse leverages the generation capability of large video models and integrates three key innovations: 1) A dataset for large-scale multi-agent interactive world modeling is built on the CARLA simulation platform, featuring diverse scenes, weather conditions, and inte...

</details>

---

### [What Capable Agents Must Know: Selection Theorems for Robust Decision-Making under Uncertainty](https://arxiv.org/abs/2603.02491v1)

**Authors:** Aran Nayebi

**Published:** 2026-03-03 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.02491v1) | [PDF](https://arxiv.org/pdf/2603.02491v1.pdf)

<details>
<summary>Abstract</summary>

As artificial agents become increasingly capable, what internal structure is *necessary* for an agent to act competently under uncertainty? Classical results show that optimal control can be *implemented* using belief states or world models, but not that such representations are required. We prove quantitative "selection theorems" showing that low *average-case regret* on structured families of action-conditioned prediction tasks forces an agent to implement a predictive, structured internal sta...

</details>

---
