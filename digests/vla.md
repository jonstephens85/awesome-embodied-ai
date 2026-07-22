# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-22 22:52 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](https://arxiv.org/abs/2607.18231v1)

**Authors:** Ruicheng Li, Qixiu Li, Ruichun Ma, Yu Deng, Lin Luo et al. (11 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18231v1) | [PDF](https://arxiv.org/pdf/2607.18231v1.pdf) | [Project Page](https://qft-333.github.io/FM-VLA-Page/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited when temporal events are visually ambiguous, e.g., pushing a button multiple times with small movements. We propose FM-...

</details>

---

### [RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model](https://arxiv.org/abs/2607.17977v1)

**Authors:** Kehan Li, Bohan Hou, Minghao Zhu, Tianyi Zhang, Zesen Cheng et al. (30 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.17977v1) | [PDF](https://arxiv.org/pdf/2607.17977v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/RynnBrain) | [GitHub](https://github.com/alibaba-damo-academy/RynnBrain)

<details>
<summary>Abstract</summary>

We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales. Trained with a unified spatio-temporal and physically grounded framework, RynnBrain 1.1 supports embodied perception, spatial reasoning, localization, and planning. Compared with RynnBrain 1.0, it further introduces contact-point prediction across the model family and native 3D grounding for the 2B and 9B models, yielding representations and outputs that are more directly aligned with robot ma...

</details>

---

## Other Recent Papers

### [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](https://arxiv.org/abs/2607.18709v1)

**Authors:** Ziqin Wang, Hao Li, Weijun Wang, Junhao Cai, Jia Zeng et al. (8 authors)

**Published:** 2026-07-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18709v1) | [PDF](https://arxiv.org/pdf/2607.18709v1.pdf)

<details>
<summary>Abstract</summary>

Existing robot datasets remain expensive to curate, embodiment-specific, and insufficiently annotated with the fine-grained structure required for generalizable reasoning, execution, or long-horizon environment dynamics simulation. Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling. RoboInter1.5 provides a unified resource of data, benchmarks, and models center...

</details>

---

### [STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models](https://arxiv.org/abs/2607.18580v1)

**Authors:** Kasra Torshizi, Anukriti Singh, Sidharth Mathur, Khuzema Habib, Leo Du et al. (6 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18580v1) | [PDF](https://arxiv.org/pdf/2607.18580v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language understanding with low-level robot execution. A high-level policy leverages a VLM to decompose language instructions into high-level subtask...

</details>

---

### [Patch Policy: Efficient Embodied Control via Dense Visual Representations](https://arxiv.org/abs/2607.18236v1)

**Authors:** Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun et al. (6 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.18236v1) | [PDF](https://arxiv.org/pdf/2607.18236v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning. Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While there exist policies that do operate on dense patch features like large vision-language-action models (VLAs), they tend to be heavy and sl...

</details>

---

### [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060v1)

**Authors:** Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao et al. (9 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18060v1) | [PDF](https://arxiv.org/pdf/2607.18060v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide. Heterogeneous policies offer complementary strengths, but orchestrating them requires reasoning over uncertain capability boundaries and cross-policy distribution mismatch, which are largely overlooked by existing planning methods built on homogeneous, predefined skills with fixed applicability. We propose RoboHarness, a unified framework that encapsulates independently developed robot control sys...

</details>

---

### [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](https://arxiv.org/abs/2607.18016v1)

**Authors:** Peng Ren, Haoyang Ge, Jiang Zhao, Cong Huang, Yukun Shi et al. (7 authors)

**Published:** 2026-07-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.18016v1) | [PDF](https://arxiv.org/pdf/2607.18016v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery. We study this problem as object-state divergence: the object state used to condition a whole-body action can differ from the state used to decide whether the action achieved the intended physical relation. We propose \emph{Persistent Object Token...

</details>

---

### [Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2607.17786v1)

**Authors:** Tuan Duong Trinh, Naveed Akhtar, Basim Azam

**Published:** 2026-07-20 | **Categories:** cs.RO, cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2607.17786v1) | [PDF](https://arxiv.org/pdf/2607.17786v1.pdf)

<details>
<summary>Abstract</summary>

Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions. We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thought, and a latent iterative loop), perturbing each at the vision, reasoning, and action stages on LIBERO and SimplerEnv. Two questions organiz...

</details>

---
