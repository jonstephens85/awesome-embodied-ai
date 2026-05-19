# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-19 18:06 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](https://arxiv.org/abs/2605.18287v1)

**Authors:** Yiyang Fu, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun et al. (10 authors)

**Published:** 2026-05-18 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.18287v1) | [PDF](https://arxiv.org/pdf/2605.18287v1.pdf) | [Project Page](https://dagroup-pku.github.io/StableVLA/) | [GitHub](https://github.com/DAGroup-PKU/HumanNet)

<details>
<summary>Abstract</summary>

It is infeasible to encompass all possible disturbances within the training dataset. This raises a critical question regarding the robustness of Vision-Language-Action (VLA) models when encountering unseen real-world visual disturbances, particularly under imperfect visual conditions. In this work, we conduct a systematic study based on recent state-of-the-art VLA models and reveal a significant performance drop when visual disturbances absent from the training data are introduced. To mitigate t...

</details>

---

### [Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies](https://arxiv.org/abs/2605.17204v1)

**Authors:** Xinchen Jin, Aditya Chatterjee, Pranav Kumar, Rohan Paleja

**Published:** 2026-05-17 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.17204v1) | [PDF](https://arxiv.org/pdf/2605.17204v1.pdf) | [GitHub](https://github.com/xc-j/Event-SAE})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies translate language and visual inputs into robot actions, where their hidden representations directly shape closed-loop behavior. However, mechanistic interpretability tools from language and vision-language models do not transfer cleanly to VLAs: outputs are robot actions rather than human-readable tokens, and interventions can only be tested via expensive closed-loop rollouts. We propose an event-grounded interpretability pipeline that anchors SAE feature a...

</details>

---

## Other Recent Papers

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

### [AffordVLA: Injecting Affordance Representations into Vision-Language-Action Models via Implicit Feature Alignment](https://arxiv.org/abs/2605.17517v1)

**Authors:** Weijie Kong, Zhian Su, Wei Yu, Huixu Dong

**Published:** 2026-05-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.17517v1) | [PDF](https://arxiv.org/pdf/2605.17517v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation. However, the visual representations of most VLA models are often dominated by global object appearance and struggle to focus on task-relevant functional interaction regions, which limits their robustness in unstructured environments. Existing affordance-based methods typically rely on explicit mask injection or external perception modules, requiring additional annotations ...

</details>

---

### [DyGRO-VLA: Cross-Task Scaling of Vision-Language-Action Models via Dynamic Grouped Residual Optimization](https://arxiv.org/abs/2605.17486v1)

**Authors:** Sixu Lin, Yunpeng Qing, Litao Liu, Ming Zhou, Ruixing Jin et al. (7 authors)

**Published:** 2026-05-17 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.17486v1) | [PDF](https://arxiv.org/pdf/2605.17486v1.pdf)

<details>
<summary>Abstract</summary>

Recent progress in Reinforcement Learning (RL) provides a principled approach to optimizing Vision-Language-Action (VLA) models, facilitating a shift from trajectory imitation to active learning in the task environment. Despite improvements in control precision, most RL optimizers remain task-specific, which reduces VLA models from generalist controllers to policies that overfit to a narrow set of tasks. In this study, we conduct an in-depth analysis of this phenomenon and highlight the importan...

</details>

---

### [CLAP: Contrastive Latent-space Prompt Optimization for End-to-end Autonomous Driving](https://arxiv.org/abs/2605.17284v1)

**Authors:** Ruiyang Zhu, Yuehan He, Boyuan Zheng, Zesen Zhao, Ahmad Chalhoub et al. (7 authors)

**Published:** 2026-05-17 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.17284v1) | [PDF](https://arxiv.org/pdf/2605.17284v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving systems powered by Vision-Language-Action (VLA) models achieve strong performance on common driving scenarios, yet remain brittle in rare but safety-critical long-tail situations such as active construction zones and complex yielding geometries. In this paper, we present a method that addresses the long-tail challenging scenes beyond data scaling and model training. We introduce CLAP (Contrastive Latent-space Prompt optimization), a location-aware adaptation framewo...

</details>

---

### [Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation](https://arxiv.org/abs/2605.17268v1)

**Authors:** Nicanor Mayumu, Xiaoheng Deng, Patrick Mukala

**Published:** 2026-05-17 | **Categories:** cs.AI, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.17268v1) | [PDF](https://arxiv.org/pdf/2605.17268v1.pdf)

<details>
<summary>Abstract</summary>

We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. Our main finding is that output natural-language rationales with trajectories may be significantly unfaithful: (i) overall reasoning fidelity is only 42.5%, with Chain-of-Causation matching scene reality less than half the time; (ii) 94 missed pedestrians in one-third of pedestrian-relevant scenes; (iii) 97.7% t...

</details>

---
