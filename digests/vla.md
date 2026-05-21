# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-21 22:57 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction](https://arxiv.org/abs/2605.21414v1)

**Authors:** Shizhe Chen, Paul Pacaud, Cordelia Schmid

**Published:** 2026-05-20 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.21414v1) | [PDF](https://arxiv.org/pdf/2605.21414v1.pdf) | [Project Page](https://cshizhe.github.io/projects/pointact.html)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation by leveraging large pretrained vision-language backbones. However, most existing VLAs rely primarily on 2D visual representations, which limit their ability to reason about fine-grained geometry and spatial grounding - capabilities that are essential for precise and robust manipulation in 3D environments. In this paper, we propose PointACT, a dual-system 3D-aware VLA policy that integrates hi...

</details>

---

### [Beyond Binary Success: A Diagnostic Meta-Evaluation Framework for Fine-Grained Manipulation](https://arxiv.org/abs/2605.19986v1)

**Authors:** He-Yang Xu, Pengyuan Zhang, Zongyuan Ge, Xiaoshuai Hao, Serge Belongie et al. (8 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.19986v1) | [PDF](https://arxiv.org/pdf/2605.19986v1.pdf) | [Project Page](https://metafine.github.io/)

<details>
<summary>Abstract</summary>

Fine-grained manipulation marks a regime where global scene context no longer suffices, and success hinges on the tight coupling of local attribute grounding, high-fidelity spatial perception, and constraint-respecting motor execution. However, current embodied AI benchmarks collapse these capacities into binary success rates, systematically inflating reported capabilities by up to 70% and masking the architectural bottlenecks that impede real-world deployment. We introduce MetaFine, a diagnosti...

</details>

---

### [RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models](https://arxiv.org/abs/2605.19678v1)

**Authors:** Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu et al. (6 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19678v1) | [PDF](https://arxiv.org/pdf/2605.19678v1.pdf) | [GitHub](https://github.com/HCPLab-SYSU/RoVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong performance on embodied manipulation, yet they remain brittle under visual observation changes, paraphrased language instructions, and compounded perturbations. This limitation suggests that existing methods still rely heavily on shallow correlations in the training distribution, rather than learning stable couplings among task semantics, environment states, and action generation. Although recent efforts improve robustness through larger-scal...

</details>

---

## Other Recent Papers

### [Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs](https://arxiv.org/abs/2605.21446v1)

**Authors:** Abhinaw Priyadershi, Jelena Frtunikj

**Published:** 2026-05-20 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.21446v1) | [PDF](https://arxiv.org/pdf/2605.21446v1.pdf)

<details>
<summary>Abstract</summary>

Interpretable autonomous driving planners depend not only on generating explanations, but also on those explanations remaining reliable under real-world sensor degradation. In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference t...

</details>

---

### [DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions](https://arxiv.org/abs/2605.21273v1)

**Authors:** Weicheng Zheng, Yixin Huang, Qiao Sun, Derun Li, Hang Zhao

**Published:** 2026-05-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.21273v1) | [PDF](https://arxiv.org/pdf/2605.21273v1.pdf)

<details>
<summary>Abstract</summary>

Driving Vision-Language-Action Models (Driving VLAs) commonly introduce natural-language reasoning as an intermediate interface for end-to-end planning, but reasoning-centric interfaces face three practical bottlenecks: obtaining high-quality reasoning annotations is difficult, generating and understanding long reasoning chains is challenging for compact models, and inference latency is substantially increased. In this paper, we rethink the design of language interfaces in Driving VLAs and show ...

</details>

---

### [Grounding Driving VLA via Inverse Kinematics](https://arxiv.org/abs/2605.21061v1)

**Authors:** Junsung Park, Hyunjung Shim

**Published:** 2026-05-20 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.21061v1) | [PDF](https://arxiv.org/pdf/2605.21061v1.pdf)

<details>
<summary>Abstract</summary>

Existing Driving VLAs predict trajectories while largely ignoring their visual tokens -- a phenomenon we trace not to insufficient training but to a structurally ill-posed task formulation. We show that trajectory recovery, when viewed through the lens of inverse kinematics, requires both a current and a future visual state as boundary conditions; existing VLAs supply only the former, which encourages the model to shortcut through ego status and text commands alone. To address this, we re-design...

</details>

---

### [VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2605.20774v1)

**Authors:** Alex S. Huang, Jiahui Zhang, Shiqing Tang, Yu Xiang

**Published:** 2026-05-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.20774v1) | [PDF](https://arxiv.org/pdf/2605.20774v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, but their real-world evaluation remains limited by a lack of accessible, reproducible, and consistent benchmarks. Simulation benchmarks fail to capture real-world complexity, while existing real-world benchmarks often require expensive hardware, centralized evaluation, or are limited in task diversity. We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluatin...

</details>

---

### [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/abs/2605.20752v1)

**Authors:** Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao et al. (8 authors)

**Published:** 2026-05-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.20752v1) | [PDF](https://arxiv.org/pdf/2605.20752v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have advanced language-conditioned robotic manipulation by transferring semantic priors from pretrained vision-language models to action generation. Yet, standard action-imitation training often provides limited explicit supervision for 3D geometry, dense visual structure, and short-horizon environment evolution, which are critical for physically precise manipulation. We introduce \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in that tu...

</details>

---

### [PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.19580v1)

**Authors:** Peizheng Guo, Jingyao Wang, Changwen Zheng, Wenwen Qiang

**Published:** 2026-05-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19580v1) | [PDF](https://arxiv.org/pdf/2605.19580v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show promising ability in language-guided robotic tasks. However, making VLA policies reliable remains challenging, because a manipulation task is completed through closed-loop interaction, where each action affects subsequent execution. To analyze this problem, we revisit VLA policy during execution and argue that a VLA policy acts both as a planner, which makes task-oriented decisions that change the direction of execution, and as an executor, which realizes...

</details>

---

### [SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving](https://arxiv.org/abs/2605.19524v1)

**Authors:** Kefei Tian, Yuansheng Lian, Kai Yang, Xiangdong Chen, Shen Li

**Published:** 2026-05-19 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.19524v1) | [PDF](https://arxiv.org/pdf/2605.19524v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving systems excel in common scenarios but struggle with safety-critical long-tail cases. Vision-Language-Action (VLA) models are promising due to their strong reasoning capabilities. However, most VLA-based approaches rely on positive expert demonstrations, rarely exploiting negative samples, leading to insufficient understanding of risky behaviors and safety boundaries. To address this limitation, we propose SafeAlign-VLA, a unified negative-enhanced safe alignment fra...

</details>

---

### [DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies](https://arxiv.org/abs/2605.19294v1)

**Authors:** Yixiang Zhu, Yonghao Chen, Rui Meng, Jingyu Guo, Jiaxiang Zou et al. (8 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.19294v1) | [PDF](https://arxiv.org/pdf/2605.19294v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are typically deployed with asynchronous inference: the robot executes a previously predicted action chunk while the model computes the next one. This creates a prediction-execution misalignment: the chunk is conditioned on the observation taken before inference began, but executes in a physical state that has already drifted forward by several control steps; naive asynchronous rollover collapses from 89% to under 1% on Kinetix as the inference cycle covers ...

</details>

---

### [Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR](https://arxiv.org/abs/2605.19282v1)

**Authors:** Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu

**Published:** 2026-05-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.19282v1) | [PDF](https://arxiv.org/pdf/2605.19282v1.pdf)

<details>
<summary>Abstract</summary>

Muon is a matrix-aware optimizer that leverages Newton-Schulz (NS) iterations to enforce spectral gradient orthogonalization by driving all singular values of the momentum matrix toward 1. While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplificatio...

</details>

---
