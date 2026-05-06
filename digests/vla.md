# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-06 22:39 UTC

**Papers found:** 5

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269v1)

**Authors:** Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim et al. (68 authors)

**Published:** 2026-05-05 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.03269v1) | [PDF](https://arxiv.org/pdf/2605.03269v1.pdf) | [Project Page](https://rlwrld.ai/rldx-1)

<details>
<summary>Abstract</summary>

While Vision-Language-Action models (VLAs) have shown remarkable progress toward human-like generalist robotic policies through the versatile intelligence (i.e. broad scene understanding and language-conditioned generalization) inherited from pre-trained Vision-Language Models, they still struggle with complex real-world tasks requiring broader functional capabilities (e.g. motion awareness, memory-aware decision making, and physical sensing). To address this, we introduce RLDX-1, a general-purp...

</details>

---

### [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881v1)

**Authors:** Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu et al. (29 authors)

**Published:** 2026-05-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02881v1) | [PDF](https://arxiv.org/pdf/2605.02881v1.pdf) | [Project Page](https://allenai.org/blog/molmoact2)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deploym...

</details>

---

### [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](https://arxiv.org/abs/2605.02757v1)

**Authors:** Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You et al. (8 authors)

**Published:** 2026-05-04 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02757v1) | [PDF](https://arxiv.org/pdf/2605.02757v1.pdf) | [GitHub](https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically rely on large-scale real-world videos, whereas simulated data, despite being inexpensive and highly parallelizable to collect, often suffers from a substantial visual domain gap and limited environmental diversity, resulting in weak real-world generalization. We present an efficient video augmentation framework that converts simulated VLA videos into realistic training videos while preserving task semantics and action trajectories. Our pipeline extra...

</details>

---

## Other Recent Papers

### [Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference](https://arxiv.org/abs/2605.02739v1)

**Authors:** Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin et al. (15 authors)

**Published:** 2026-05-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.02739v1) | [PDF](https://arxiv.org/pdf/2605.02739v1.pdf)

<details>
<summary>Abstract</summary>

Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We instantiate Latent Bridge on two architecturally distinct...

</details>

---

### [CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation](https://arxiv.org/abs/2605.02600v1)

**Authors:** Berk Çiçek, Mert K. Er, Özgür S. Öğüz

**Published:** 2026-05-04 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.02600v1) | [PDF](https://arxiv.org/pdf/2605.02600v1.pdf)

<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) and Vision-Language Models (VLMs) demonstrate remarkable capabilities in high-level reasoning and semantic understanding, applying them directly to contact-rich manipulation remains a challenge due to their lack of explicit physical grounding and inability to perform adaptive control. To bridge this gap, we propose CoRAL (Contact-Rich Adaptive LLM-based control), a modular framework that enables zero-shot planning by decoupling high-level reasoning from low-lev...

</details>

---
