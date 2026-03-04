# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-03-04 22:21 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Scaling Tasks, Not Samples: Mastering Humanoid Control through Multi-Task Model-Based Reinforcement Learning](https://arxiv.org/abs/2603.01452v1)

**Authors:** Shaohuai Liu, Weirui Ye, Yilun Du, Le Xie

**Published:** 2026-03-02 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.01452v1) | [PDF](https://arxiv.org/pdf/2603.01452v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Developing generalist robots capable of mastering diverse skills remains a central challenge in embodied AI. While recent progress emphasizes scaling model parameters and offline datasets, such approaches are limited in robotics, where learning requires active interaction. We argue that effective online learning should scale the \emph{number of tasks}, rather than the number of samples per task. This regime reveals a structural advantage of model-based reinforcement learning (MBRL). Because phys...

</details>

---

## Other Recent Papers

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

### [WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)

**Authors:** Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu et al. (7 authors)

**Published:** 2026-03-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.02049v1) | [PDF](https://arxiv.org/pdf/2603.02049v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in foundational Video Diffusion Models (VDMs) have yielded significant progress. Yet, despite the remarkable visual quality of generated videos, reconstructing consistent 3D scenes from these outputs remains challenging, due to limited camera controllability and inconsistent generated content when viewed from distinct camera trajectories. In this paper, we propose WorldStereo, a novel framework that bridges camera-guided video generation and 3D reconstruction via two dedicated ge...

</details>

---

### [LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving](https://arxiv.org/abs/2603.01928v1)

**Authors:** Yuechen Luo, Fang Li, Shaoqing Xu, Yang Ji, Zehan Zhang et al. (13 authors)

**Published:** 2026-03-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.01928v1) | [PDF](https://arxiv.org/pdf/2603.01928v1.pdf)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have revolutionized autonomous driving by unifying perception and planning, their reliance on explicit textual Chain-of-Thought (CoT) leads to semantic-perceptual decoupling and perceptual-symbolic conflicts. Recent shifts toward latent reasoning attempt to bypass these bottlenecks by thinking in continuous hidden space. However, without explicit intermediate constraints, standard latent CoT often operates as a physics-agnostic representation. To address...

</details>

---

### [Discrete World Models via Regularization](https://arxiv.org/abs/2603.01748v1)

**Authors:** Davide Bizzaro, Luciano Serafini

**Published:** 2026-03-02 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.01748v1) | [PDF](https://arxiv.org/pdf/2603.01748v1.pdf)

<details>
<summary>Abstract</summary>

World models aim to capture the states and dynamics of an environment in a compact latent space. Moreover, using Boolean state representations is particularly useful for search heuristics and symbolic reasoning and planning. Existing approaches keep latents informative via decoder-based reconstruction, or instead via contrastive or reward signals. In this work, we introduce Discrete World Models via Regularization (DWMR): a reconstruction-free and contrastive-free method for unsupervised Boolean...

</details>

---
