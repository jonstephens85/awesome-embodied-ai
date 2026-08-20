# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-20 22:15 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484v1)

**Authors:** Pardis Taghavi, Reza Langari, Gaurav Pandey

**Published:** 2026-08-19 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18484v1) | [PDF](https://arxiv.org/pdf/2608.18484v1.pdf) | [Project Page](https://pardistaghavi.github.io/SparsePR-website/)

<details>
<summary>Abstract</summary>

Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator. Queries sharing a block route may have poorly overlapping supports, while retained attention mass alone does not determine the post-softmax error from skipped interactions. We show that partition geometry affects both pooled support and the predictability of the remaining residual from the sparse output. We introduce SparsePR, whic...

</details>

---

### [GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](https://arxiv.org/abs/2608.18234v1)

**Authors:** Ziyang Cheng, Tianshu Tang, Jinxin Lan, Xinze Chen, Yuhan Gong et al. (20 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18234v1) | [PDF](https://arxiv.org/pdf/2608.18234v1.pdf) | [Project Page](https://shepherd1226.github.io/gigabrain-wbc-0.5/)

<details>
<summary>Abstract</summary>

Whole-body motion tracking policies turn a humanoid into a robust control interface: the teleoperator---or an upstream model---only supplies a coarse movement intent, while the low-level policy keeps the robot balanced and physically feasible. Existing trackers deliver this interface only on flat ground: trained in empty scenes, they never learn how contact with terrain and objects reshapes their dynamics, and they attempt to teach the policy to balance under any command by continually enlarging...

</details>

---

### [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077v1)

**Authors:** Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du et al. (11 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.18077v1) | [PDF](https://arxiv.org/pdf/2608.18077v1.pdf) | [Project Page](https://nvidia-isaac.github.io/video_to_data/hydra-0/)

<details>
<summary>Abstract</summary>

We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion. This shared visual interface enables generalist world modeling and control by learning action consequences across embodiments, tasks, environments, and video-generation backbones. Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient ad...

</details>

---

### [An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](https://arxiv.org/abs/2608.17956v1)

**Authors:** Javier Aguilar Martín

**Published:** 2026-08-18 | **Categories:** cs.LG, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2608.17956v1) | [PDF](https://arxiv.org/pdf/2608.17956v1.pdf) | [GitHub](https://github.com/JaviMaligno/code-world-models)

<details>
<summary>Abstract</summary>

In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On th...

</details>

---

### [No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models](https://arxiv.org/abs/2608.17542v1)

**Authors:** Jack Boylan, Chris Hokamp

**Published:** 2026-08-18 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.17542v1) | [PDF](https://arxiv.org/pdf/2608.17542v1.pdf) | [GitHub](https://github.com/jackboyla/action-contrastive-jepa)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future embeddings, but the objective admits a trivial solution of a constant encoder, so every practical system adds an anti-collapse mechanism (LeCun, 2022; Assran et al., 2023; Bardes et al., 2022; 2024). LeWorldModel (LeWM) prevents collapse with SIGReg, a regularizer that forces the latent distribution to match an isotropic Gaussian: the representation is stabilized by prescribing what it must look like, indepe...

</details>

---

## Other Recent Papers

### [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085v1)

**Authors:** Ruiguo Zhong, Benshan Ma, Xiaolong Chen, Lang Zhang, Mingyue Feng et al. (8 authors)

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19085v1) | [PDF](https://arxiv.org/pdf/2608.19085v1.pdf)

<details>
<summary>Abstract</summary>

Anticipating how scenes evolve under ego actions is fundamental to safe autonomous driving, yet the full potential of world models for decision-making remains unrealized. The critical challenge lies in ensuring that future modeling is not merely predictive, but decision-informative: the predicted future must directly shape which trajectory is selected. Existing approaches decouple future representation learning from planning optimization, or share predicted states across trajectory candidates, t...

</details>

---

### [Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning](https://arxiv.org/abs/2608.18746v1)

**Authors:** Jiawei Wang, Ke Rui, Yushen Zuo, Yichun Feng, Minglei Li

**Published:** 2026-08-19 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.18746v1) | [PDF](https://arxiv.org/pdf/2608.18746v1.pdf)

<details>
<summary>Abstract</summary>

JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task variables, however, does not guarantee that this particular cost ranks candidate action sequences by real task progress. We call the latter property \emph{decision-metric alignment}. We introduce Plan-Real Spearman, which measures latent--real rank agreement on random plans, and CEM-stage Spearman, which measures the same agreement as cross-entropy-me...

</details>

---

### [Reinforced Planning with Latent World Models](https://arxiv.org/abs/2608.18669v1)

**Authors:** Armin Sommer, Jannik Schilling

**Published:** 2026-08-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18669v1) | [PDF](https://arxiv.org/pdf/2608.18669v1.pdf)

<details>
<summary>Abstract</summary>

Humans solve complex problems by constructing plans and mentally simulating their outcomes with an internal model of the world. Machine learning has produced world models that similarly predict the outcomes of action sequences, but the improvement of candidate plans still isn't fully learned. Current planners are either hand-designed, distilled from a hand-designed optimizer, or learned only to inform an amortized policy rather than to revise the plan itself. We introduce the Reinforced Planning...

</details>

---

### [Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation](https://arxiv.org/abs/2608.18647v1)

**Authors:** Harry Robertshaw, Maxence Boels, Nikola Fischer, Sebastien Ourselin, Christos Bergeles et al. (7 authors)

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18647v1) | [PDF](https://arxiv.org/pdf/2608.18647v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous endovascular navigation could support the delivery of mechanical thrombectomy to underserved areas, but controllers must navigate long, multi-stage paths across varying vascular anatomies. This study investigates Progressive Experience Fusion (PEF) to train a multi-task TD-MPC2 controller. We additionally evaluate a heuristic that changes the Model Predictive Path Integral planning horizon using residual action-sequence dispersion, and fine-tuning in a patient-specific simulation. Acr...

</details>

---

### [Towards Zero-Shot Task Transfer with Neurosymbolic World Models](https://arxiv.org/abs/2608.17959v1)

**Authors:** Isidoro Tamassia, Lennert De Smet, Giuseppe Marra

**Published:** 2026-08-18 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.17959v1) | [PDF](https://arxiv.org/pdf/2608.17959v1.pdf)

<details>
<summary>Abstract</summary>

State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlying environment. While expressive, these models are generally task-dependent: they learn uninterpretable latent representations that are tied to the training task and thus hard to generalize to new tasks. In this work, we present a novel world model formulation where the reward prediction only depends...

</details>

---

### [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](https://arxiv.org/abs/2608.17496v1)

**Authors:** Kaiming Zhong, Tianhua Liu, Yue Wang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17496v1) | [PDF](https://arxiv.org/pdf/2608.17496v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pip...

</details>

---
