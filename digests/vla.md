# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-23 22:42 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations](https://arxiv.org/abs/2605.22812v1)

**Authors:** Wenxuan Guo, Ziyuan Li, Meng Zhang, Yichen Liu, Yimeng Dong et al. (10 authors)

**Published:** 2026-05-21 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.22812v1) | [PDF](https://arxiv.org/pdf/2605.22812v1.pdf) | [Project Page](https://gwxuan.github.io/GesVLA/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong potential for general-purpose robot manipulation by unifying perception and action. However, existing VLA systems primarily rely on textual instructions and struggle to resolve spatial ambiguity in complex scenes with multiple similar objects. To address this limitation, we introduce gesture as a parallel instruction modality and propose a Gesture-aware Vision-Language-Action model (GesVLA). Our approach encodes gesture features directly into...

</details>

---

### [Action with Visual Primitives](https://arxiv.org/abs/2605.22183v1)

**Authors:** Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang et al. (9 authors)

**Published:** 2026-05-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.22183v1) | [PDF](https://arxiv.org/pdf/2605.22183v1.pdf) | [Project Page](https://kingdroper.github.io/AVP/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for generalist robotic manipulation. A common design in current architectures maps language instructions and visual observations to actions in a single forward pass. While conceptually simple, this formulation entangles instruction comprehension, spatial scene understanding, and motor control within a single learning objective. As a result, the action expert must implicitly relearn cognitive and perceptual capabilities alre...

</details>

---

### [CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.21854v1)

**Authors:** Zhi Liu

**Published:** 2026-05-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.21854v1) | [PDF](https://arxiv.org/pdf/2605.21854v1.pdf) | [GitHub](https://github.com/lz-googlefycy/vla-lab)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. OpenVLA) and continuous-action flow-matching (e.g. pi-0.5). Yet preference alignment via Direct Preference Optimisation (DPO) -- the de-facto post-training step in language models -- has been studied almost exclusively on autoregressive VLAs. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. Three contributions: (i) a surrogate flow-m...

</details>

---

## Other Recent Papers

### [From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](https://arxiv.org/abs/2605.22671v1)

**Authors:** Bing Hu, Zaijing Li, Rui Shao, Junda Chen, April Hua Liu et al. (7 authors)

**Published:** 2026-05-21 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.22671v1) | [PDF](https://arxiv.org/pdf/2605.22671v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propos...

</details>

---

### [Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts](https://arxiv.org/abs/2605.22446v1)

**Authors:** Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu et al. (9 authors)

**Published:** 2026-05-21 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.22446v1) | [PDF](https://arxiv.org/pdf/2605.22446v1.pdf)

<details>
<summary>Abstract</summary>

While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity ass...

</details>

---

### [How can reasoning capability empower the AI copilot robot in endoscopic surgery](https://arxiv.org/abs/2605.22322v1)

**Authors:** Guankun Wang, Long Bai, Hongliang Ren

**Published:** 2026-05-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.22322v1) | [PDF](https://arxiv.org/pdf/2605.22322v1.pdf)

<details>
<summary>Abstract</summary>

Reasoning capability has significantly advanced complex logical inference and robotic decision-making in general domains. However, its potential in the Artificial Intelligence (AI) copilot robot-particularly implemented based on the Vision-Language-Action (VLA) model-remains unexplored in endoscopic surgery. Effective reasoning should enable AI copilot robots to integrate multimodal cues, interpret surgical intent, and infer hidden tissue dynamics, thereby alleviating intraoperative uncertainty ...

</details>

---

### [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://arxiv.org/abs/2605.22283v1)

**Authors:** Pengteng Li, Weiyu Guo, He Zhang, Tiefu Cai, Xiao He et al. (7 authors)

**Published:** 2026-05-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.22283v1) | [PDF](https://arxiv.org/pdf/2605.22283v1.pdf)

<details>
<summary>Abstract</summary>

We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of view. SOMA addresses this limitation by equipping VLAs with a persistent spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visu...

</details>

---

### [LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model](https://arxiv.org/abs/2605.22089v1)

**Authors:** Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye et al. (6 authors)

**Published:** 2026-05-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.22089v1) | [PDF](https://arxiv.org/pdf/2605.22089v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Vi...

</details>

---

### [EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control](https://arxiv.org/abs/2605.21862v1)

**Authors:** Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang et al. (6 authors)

**Published:** 2026-05-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.21862v1) | [PDF](https://arxiv.org/pdf/2605.21862v1.pdf)

<details>
<summary>Abstract</summary>

Chunked vision-language-action (VLA) policies predict multi-step robot controls, conditioning each update on the current visual observation alone. Yet robot actions cause contact, occlusion, and object motion, and the geometry that later decisions depend on can change before the next visual update arrives. Spatial VLAs improve current-frame geometry. Temporal VLAs aggregate past frames. Neither maintains an action-updated scene prior across chunks. We argue for a persistent action-updated scene ...

</details>

---
