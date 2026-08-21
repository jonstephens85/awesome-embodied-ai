# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-21 16:32 UTC

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

## Other Recent Papers

### [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111v1)

**Authors:** Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li et al. (10 authors)

**Published:** 2026-08-20 | **Categories:** cs.RO, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2608.20111v1) | [PDF](https://arxiv.org/pdf/2608.20111v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols. This survey reviews this transition across behavior cloning, conditional imitation learning, privileged distillation, BEV and vectorized planning, unified perception-prediction-planning architectures, world-model-based planners, and vision-language-action systems. We argue that ...

</details>

---

### [Orthogonal JEPA: Factorized Predictive States for Latent World Models](https://arxiv.org/abs/2608.20065v1)

**Authors:** Taoyong Cui, Pheng Ann Heng, Wanli Ouyang

**Published:** 2026-08-20 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.20065v1) | [PDF](https://arxiv.org/pdf/2608.20065v1.pdf)

<details>
<summary>Abstract</summary>

World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to ...

</details>

---

### [ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control](https://arxiv.org/abs/2608.19804v1)

**Authors:** Xu Yang, Kailai Sun, Dianyu Zhong, Qianchuan Zhao

**Published:** 2026-08-20 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19804v1) | [PDF](https://arxiv.org/pdf/2608.19804v1.pdf)

<details>
<summary>Abstract</summary>

Buildings account for roughly one-third of global energy consumption and CO$_2$ emissions. Optimizing indoor climate systems plays a critical role for urban climate mitigation aligned with UN Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors, especially for out-of-distribution env...

</details>

---

### [An Irreducible Quantum Advantage in Aligning World Models with Reality](https://arxiv.org/abs/2608.19779v1)

**Authors:** Josep Lumbreras, Hailan Ma, Jayne Thompson, Mile Gu

**Published:** 2026-08-20 | **Categories:** quant-ph, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.19779v1) | [PDF](https://arxiv.org/pdf/2608.19779v1.pdf)

<details>
<summary>Abstract</summary>

World models provide digital simulacra of the true world, allowing agents to be trained and tested before costly real-world deployment. At each time step, they receive an action and generate an observation and reward matching the statistics of the true world. In complex environments where present outcomes depend on events far in the past, this requires memory. One might expect that, by increasing memory, we can always build a model accurately enough to align the optimal agent policies of the rea...

</details>

---

### [World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms](https://arxiv.org/abs/2608.19661v1)

**Authors:** Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot

**Published:** 2026-08-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.19661v1) | [PDF](https://arxiv.org/pdf/2608.19661v1.pdf)

<details>
<summary>Abstract</summary>

Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle. We proposed the use of a world model to expand the capabilities of Large Language model-based planners. Our method has three components: a physics-grounded neural world model, a three-phase gradient-based trajectory optimizer, and a Model Predictive Controller...

</details>

---

### [Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution](https://arxiv.org/abs/2608.19492v1)

**Authors:** Kaizhen Tan, Xin Xu, Siru Tao, Yixiao Li, Hanzhe Hong et al. (7 authors)

**Published:** 2026-08-19 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.19492v1) | [PDF](https://arxiv.org/pdf/2608.19492v1.pdf)

<details>
<summary>Abstract</summary>

World models increasingly treat compact multimodal representations as interfaces between perception and physical interaction, yet existing probes do not establish whether different sensors carry the same executable meaning or whether that meaning survives a new action composition. We introduce an operational capability hierarchy and the Disjoint-Bridge Operator-Substitution Certificate (DBOSC), which asks whether independently trained modality compilers enter a frozen response chart interchangea...

</details>

---

### [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085v2)

**Authors:** Ruiguo Zhong, Benshan Ma, Xiaolong Chen, Lang Zhang, Mingyue Feng et al. (8 authors)

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19085v2) | [PDF](https://arxiv.org/pdf/2608.19085v2.pdf)

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
