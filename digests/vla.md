# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-20 23:05 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](https://arxiv.org/abs/2605.18287v1)

**Authors:** Yiyang Fu, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun et al. (10 authors)

**Published:** 2026-05-18 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.18287v1) | [PDF](https://arxiv.org/pdf/2605.18287v1.pdf) | [Project Page](https://dagroup-pku.github.io/StableVLA/) | [GitHub](https://github.com/DAGroup-PKU/HumanNet)

<details>
<summary>Abstract</summary>

It is infeasible to encompass all possible disturbances within the training dataset. This raises a critical question regarding the robustness of Vision-Language-Action (VLA) models when encountering unseen real-world visual disturbances, particularly under imperfect visual conditions. In this work, we conduct a systematic study based on recent state-of-the-art VLA models and reveal a significant performance drop when visual disturbances absent from the training data are introduced. To mitigate t...

</details>

---

## Other Recent Papers

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

### [Dexora: Open-source VLA for High-DoF Bimanual Dexterity](https://arxiv.org/abs/2605.18722v1)

**Authors:** Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, Minwen Liao et al. (25 authors)

**Published:** 2026-05-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.18722v1) | [PDF](https://arxiv.org/pdf/2605.18722v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently become a central direction in embodied AI, but current systems are restricted to either dual-gripper control or single-arm dexterous hand manipulation. While low-dimensional gripper control can often be handled with simpler methods, high-dimensional dexterous hand control benefits greatly from full end-to-end VLA learning. In this work, we introduce Dexora, the first open-source VLA system that natively targets dual-arm, dual-hand high-DoF manipu...

</details>

---

### [Key-Gram: Extensible World Knowledge for Embodied Manipulation](https://arxiv.org/abs/2605.18556v1)

**Authors:** Jingjing Fan, Siyuan Li, Botao Ren, Zhidong Deng

**Published:** 2026-05-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.18556v1) | [PDF](https://arxiv.org/pdf/2605.18556v1.pdf)

<details>
<summary>Abstract</summary>

Embodied control increasingly requires models to follow compositional language instructions while reasoning over dynamic visual states. However, current vision-language-action policies and world-action models often couple linguistic knowledge with visual computation in a shared backbone or conditioning pathway, leading to modality competition and making knowledge extension dependent on backbone updates. In this paper, we introduce Key-Gram, a conditional-memory framework that separates language-...

</details>

---
