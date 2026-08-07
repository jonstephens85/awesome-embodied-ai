# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-07 16:53 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](https://arxiv.org/abs/2608.05042v1)

**Authors:** Peiyan Li, Yuze Zhu, Yixiang Chen, Qisen Ma, Yuan Xu et al. (13 authors)

**Published:** 2026-08-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.05042v1) | [PDF](https://arxiv.org/pdf/2608.05042v1.pdf) | [Project Page](https://bridgevla-plus.github.io/)

<details>
<summary>Abstract</summary>

Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations. These limitations hinder their application to data-scarce, open-world, and memory-dependent manipulation scenarios. Our previous work, BridgeVLA, improves data efficiency and ge...

</details>

---

## Other Recent Papers

### [$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation](https://arxiv.org/abs/2608.06375v1)

**Authors:** Zhe Li, Zhenzhe Zhang, Yangyang Wei, Wenjie Zhang, Xichen Yuan et al. (11 authors)

**Published:** 2026-08-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.06375v1) | [PDF](https://arxiv.org/pdf/2608.06375v1.pdf)

<details>
<summary>Abstract</summary>

Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent predictive whole-body world-action model for real-world humanoid concurrent loco-manipulation. Given a language instruction, cur...

</details>

---

### [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374v1)

**Authors:** Junfeng Li, Junjie He, Zhide Zhong, Yangyang Zheng, Pingyue Sheng et al. (15 authors)

**Published:** 2026-08-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.06374v1) | [PDF](https://arxiv.org/pdf/2608.06374v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer. Second, they require extensive manual preprocessing to convert embodiment-specific actions into a common format. To overcome these limitati...

</details>

---

### [Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation](https://arxiv.org/abs/2608.05999v1)

**Authors:** He Kong, Zengjue Chen, Qi Wang, Qianli Xing, Runliang Niu et al. (9 authors)

**Published:** 2026-08-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.05999v1) | [PDF](https://arxiv.org/pdf/2608.05999v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform robust long-horizon manipulation. Although hierarchical approaches introduce task decomposition, they mainly rely on supervised learning from offline demonstrations and cannot effectively ...

</details>

---

### [SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation](https://arxiv.org/abs/2608.05970v1)

**Authors:** Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma et al. (11 authors)

**Published:** 2026-08-06 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.05970v1) | [PDF](https://arxiv.org/pdf/2608.05970v1.pdf)

<details>
<summary>Abstract</summary>

Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with limited capability to capture reusable skill structures. To address this limitation, we propose Skill-Base...

</details>

---

### [In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use](https://arxiv.org/abs/2608.05738v1)

**Authors:** Jiarui Yang, Wen Huang, Jiale Zhang, Maowei Hu, Hang Guo

**Published:** 2026-08-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.05738v1) | [PDF](https://arxiv.org/pdf/2608.05738v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become the dominant recipe for generalist manipulation, yet they are almost universally trained by behavior cloning: a policy imitates expert action chunks conditioned on a static image and a fixed instruction. A natural remedy is to inject explicit reasoning through textual chain-of-thought (CoT). We show, both empirically and analytically, that free-form textual CoT degrades low-level control: the reasoning it produces is ungrounded, its latency breaks ...

</details>

---

### [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369v1)

**Authors:** Yuhao Pan, Haosong Peng, Zhengshen Zhang, Zhengyang Yan, Yalun Dai et al. (11 authors)

**Published:** 2026-08-05 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.05369v1) | [PDF](https://arxiv.org/pdf/2608.05369v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context. To address this limitation, we present World-to-Wrist VLA (W2-VLA), a VLA model for fine-grained robot manipulation with task-conditioned future wrist modeling. Given current multi-view observation...

</details>

---

### [Explicit Language Memory for Long-Horizon Planning in Vision-Language-Action Models](https://arxiv.org/abs/2608.04765v1)

**Authors:** Houze Xu, Jizhong Li, Ziyi Ye

**Published:** 2026-08-05 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.04765v1) | [PDF](https://arxiv.org/pdf/2608.04765v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a unified paradigm for connecting visual perception, language understanding, and robotic control. However, existing VLA models still face major challenges in long-horizon tasks: sparse expert demonstrations constrain cross-task compositional generalization; the non-Markovian nature of long-horizon tasks makes it difficult for policies conditioned only on current observations to maintain temporal consistency; limited closed-loop error correction allows ...

</details>

---

### [Suppression Sticks, Locality Is Fragile: A Closed-Loop Target-and-Control Audit of Task-Vector Negation in VLA Policies](https://arxiv.org/abs/2608.04692v1)

**Authors:** Shaoguang Wang, Weiyu Guo, Rushi Dai, Yiren Zhao, Yandong Guo et al. (6 authors)

**Published:** 2026-08-05 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.04692v1) | [PDF](https://arxiv.org/pdf/2608.04692v1.pdf)

<details>
<summary>Abstract</summary>

Task-vector arithmetic offers a closed-form way to modify a model, yet its behavioral locality remains unclear in closed-loop robot control. We present a target-and-control audit of per-skill task-vector subtraction from multitask vision-language-action (VLA) policies. Across all ten LIBERO-Goal skills, subtraction produces three qualitatively different regimes: target-control separation for five skills, resistance for three, and global collapse for two. On held-out initial states, the five supp...

</details>

---

### [Mind-VLA: Instruction-Aware Spatial Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2608.04633v1)

**Authors:** Xingyu Ding, Yuzhong Zhao, Yang Wu, Chaoyang Zhao, Chunhai Zhao et al. (7 authors)

**Published:** 2026-08-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.04633v1) | [PDF](https://arxiv.org/pdf/2608.04633v1.pdf)

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) methods improve generalization by aligning their representations with 3D scene geometry. However, these methods are fundamentally instruction-agnostic: the representations align the entire scene uniformly, neglecting the 3D geometry of the specific target object designated by the language instruction. This causes failures on fine-grained manipulation and target occlusion tasks, where success depends on accurate 3D understanding of the target object rather than...

</details>

---

### [Retrieve in Time, Correct in Frequency](https://arxiv.org/abs/2608.04527v1)

**Authors:** Yuze Fan, Yue Cao, Pengjie Gao, Haojia Gao, Guangqiu Guo et al. (10 authors)

**Published:** 2026-08-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.04527v1) | [PDF](https://arxiv.org/pdf/2608.04527v1.pdf)

<details>
<summary>Abstract</summary>

Frozen vision-language-action (VLA) policies generate temporally extended action chunks, but long-horizon manipulation remains vulnerable to accumulated execution error and visual aliasing across task stages. Successful rollouts provide useful corrective evidence, yet current frame retrieval can return progress-misaligned actions,while direct replay or time-domain fusion can overwrite the reactive structure of the policy proposal. We introduce Retrieve in Time, Correct in Frequency (RTCF), a tra...

</details>

---

### [GUARD: Grounding Uncertainty and Ablation-Based Risk Detection for Diffusion-Based VLAs](https://arxiv.org/abs/2608.04510v1)

**Authors:** Suhas Hegde, Jitendra Yasaswi Bharadwaj Katta

**Published:** 2026-08-05 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.04510v1) | [PDF](https://arxiv.org/pdf/2608.04510v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) policies can generate plausible actions even when their predictions are weakly grounded in the visual and language evidence defining the task. We introduce GUARD, a test-time failure detection method that measures this grounding without modifying the pretrained policy. GUARD estimates the influence of token-indexed entries in the final vision-language model key-value (KV) cache, constructs counterfactual caches by ablating salient KV entries, and comp...

</details>

---

### [Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference](https://arxiv.org/abs/2608.04428v1)

**Authors:** Zheng Liu, Zeyu Guo, Zihan Liu, Anbang Wu, Han Zhao et al. (12 authors)

**Published:** 2026-08-05 | **Categories:** cs.AR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.04428v1) | [PDF](https://arxiv.org/pdf/2608.04428v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a key component in embodied AI. Among existing approaches, diffusion-based VLA models achieve superior motion quality and generalization. However, diffusion-based VLA models are compute-intensive and must run at high control frequency, e.g., 50-200 Hz. Thus, it imposes strict latency and energy constraints on edge devices. In this work, we present Deltoris, an algorithm-hardware co-design framework for efficient diffusion-based VLA inference. F...

</details>

---

### [CofactVLA: Deconfounding Vision-Language-Action Models via Counterfactual Intervention](https://arxiv.org/abs/2608.04396v1)

**Authors:** Yan Zhang, Yinan Wu, Haoran Duan, Jungong Han

**Published:** 2026-08-05 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.04396v1) | [PDF](https://arxiv.org/pdf/2608.04396v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have driven significant progress in robotic manipulation, yet they fundamentally struggle with the vision-override phenomenon. Driven by the severe modality imbalance between dense visual streams and sparse linguistic instructions, VLAs frequently fall prey to causal confusion. Instead of treating language as the primary causal driver, the policy entirely bypasses the original instruction by overfitting to spurious visual confounders, such as prominent objects...

</details>

---
