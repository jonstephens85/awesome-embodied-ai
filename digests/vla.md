# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-04 16:44 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Chain of World: World Model Thinking in Latent Motion](https://arxiv.org/abs/2603.03195v1)

**Authors:** Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan et al. (9 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.03195v1) | [PDF](https://arxiv.org/pdf/2603.03195v1.pdf) | [Project Page](https://fx-hit.github.io/cowvla-io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are a promising path toward embodied intelligence, yet they often overlook the predictive and temporal-causal structure underlying visual dynamics. World-model VLAs address this by predicting future frames, but waste capacity reconstructing redundant backgrounds. Latent-action VLAs encode frame-to-frame transitions compactly, but lack temporally continuous dynamic modeling and world knowledge. To overcome these limitations, we introduce CoWVLA (Chain-of-World ...

</details>

---

### [Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283v1)

**Authors:** Yujia Zhang, Xiaoyang Wu, Yunhan Yang, Xianzhe Fan, Han Li et al. (9 authors)

**Published:** 2026-03-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.03283v1) | [PDF](https://arxiv.org/pdf/2603.03283v1.pdf) | [Project Page](https://pointcept.github.io/Utonia)

<details>
<summary>Abstract</summary>

We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across diverse domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent repres...

</details>

---

### [Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining](https://arxiv.org/abs/2603.01465v1)

**Authors:** Yipeng Chen, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li et al. (7 authors)

**Published:** 2026-03-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.01465v1) | [PDF](https://arxiv.org/pdf/2603.01465v1.pdf) | [GitHub](https://github.com/cytoplastm/KC-VLA)

<details>
<summary>Abstract</summary>

Existing Vision-Language-Action (VLA) models often struggle to generalize to long-horizon tasks due to their heavy reliance on immediate observations. While recent studies incorporate retrieval mechanisms or extend context windows to handle procedural tasks, they often struggle to capture Non-Markovian dependencies, where optimal actions rely solely on specific past states rather than the current observation. To address this, we introduce Keyframe-Chaining VLA, a framework that extracts and link...

</details>

---

## Other Recent Papers

### [$π$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs](https://arxiv.org/abs/2603.02083v1)

**Authors:** Siting Wang, Xiaofeng Wang, Zheng Zhu, Minnan Pei, Xinyu Cui et al. (10 authors)

**Published:** 2026-03-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.02083v1) | [PDF](https://arxiv.org/pdf/2603.02083v1.pdf)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models excel in embodied control but suffer from intractable likelihoods during multi-step sampling, hindering online reinforcement learning. We propose \textbf{\textit{$\boldsymbolπ$-StepNFT}} (Step-wise Negative-aware Fine-Tuning), a critic-and-likelihood-free framework that requires only a single forward pass per optimization step and eliminates auxiliary value networks. We identify that wider exploration spaces necessitate finer-grained, step-wise guid...

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

### [Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models](https://arxiv.org/abs/2603.01766v1)

**Authors:** Haoyun Liu, Jianzhuang Zhao, Xinyuan Chang, Tianle Shi, Chuanzhang Meng et al. (14 authors)

**Published:** 2026-03-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.01766v1) | [PDF](https://arxiv.org/pdf/2603.01766v1.pdf)

<details>
<summary>Abstract</summary>

Despite the rapid progress of Vision-Language-Action (VLA) models, the prevailing paradigm of predicting discrete waypoints remains fundamentally misaligned with the intrinsic continuity of physical motion. This discretization imposes rigid sampling rates, lacks high-order differentiability, and introduces quantization artifacts that hinder precise, compliant interaction. We propose Neural Implicit Action Fields (NIAF), a paradigm shift that reformulates action prediction from discrete waypoints...

</details>

---

### [TacMamba: A Tactile History Compression Adapter Bridging Fast Reflexes and Slow VLA Reasoning](https://arxiv.org/abs/2603.01700v1)

**Authors:** Zhenan Wang, Yanzhe Wang, Meixuan Ren, Peng Li, Yang Liu et al. (11 authors)

**Published:** 2026-03-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.01700v1) | [PDF](https://arxiv.org/pdf/2603.01700v1.pdf)

<details>
<summary>Abstract</summary>

In visually ambiguous manipulation such as detecting button click tactile feedback is often the sole source of ground truth. However, fusing tactile data poses a significant challenge due to a spatiotemporal mismatch: tactile perception requires high-frequency processing with long-horizon memory (System 1), whereas visual policies operate at low control frequencies (System 2). Existing architectures struggle to bridge this gap: Transformers are computationally prohibitive for high-frequency loop...

</details>

---

### [KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models](https://arxiv.org/abs/2603.01581v1)

**Authors:** Zihao Zheng, Zhihao Mao, Maoliang Li, Jiayu Chen, Xinhao Sun et al. (9 authors)

**Published:** 2026-03-02 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2603.01581v1) | [PDF](https://arxiv.org/pdf/2603.01581v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models build a token-domain robot control paradigm, yet suffer from low speed. Speculative Decoding (SD) is an optimization strategy that can boost inference speed. Two key issues emerge when integrating VLA and SD: first, SD relies on re-inference to address token errors, which is computationally expensive; second, to mitigate token errors, the acceptance threshold in SD requires careful adjustment. Existing works fail to address the above two issues effectively. Me...

</details>

---

### [Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation](https://arxiv.org/abs/2603.01549v1)

**Authors:** Jisoo Kim, Jungbin Cho, Sanghyeok Chu, Ananya Bal, Jinhyung Kim et al. (12 authors)

**Published:** 2026-03-02 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.01549v1) | [PDF](https://arxiv.org/pdf/2603.01549v1.pdf)

<details>
<summary>Abstract</summary>

Humans learn not only how their bodies move, but also how the surrounding world responds to their actions. In contrast, while recent Vision-Language-Action (VLA) models exhibit impressive semantic understanding, they often fail to capture the spatiotemporal dynamics governing physical interaction. In this paper, we introduce Pri4R, a simple yet effective approach that endows VLA models with an implicit understanding of world dynamics by leveraging privileged 4D information during training. Speci...

</details>

---

### [ATA: Bridging Implicit Reasoning with Attention-Guided and Action-Guided Inference for Vision-Language Action Models](https://arxiv.org/abs/2603.01490v1)

**Authors:** Cheng Yang, Jianhao Jiao, Lingyi Huang, Jinqi Xiao, Zhexiang Tang et al. (11 authors)

**Published:** 2026-03-02 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.01490v1) | [PDF](https://arxiv.org/pdf/2603.01490v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models rely on current observations, including images, language instructions, and robot states, to predict actions and complete tasks. While accurate visual perception is crucial for precise action prediction and execution, recent work has attempted to further improve performance by introducing explicit reasoning during inference. However, such approaches face significant limitations. They often depend on data-intensive resources such as Chain-of-Thought (CoT) style ...

</details>

---

### [Mean-Flow based One-Step Vision-Language-Action](https://arxiv.org/abs/2603.01469v1)

**Authors:** Yang Chen, Xiaoguang Ma, Bin Zhao

**Published:** 2026-03-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.01469v1) | [PDF](https://arxiv.org/pdf/2603.01469v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in FlowMatching-based Vision-Language-Action (VLA) frameworks have demonstrated remarkable advantages in generating high-frequency action chunks, particularly for highly dexterous robotic manipulation tasks. Despite these notable achievements, their practical applications are constrained by prolonged generation latency, which stems from inherent iterative sampling requirements and architectural limitations. To address this critical bottleneck, we propose a Mean-Flow based One-Ste...

</details>

---

### [Unifying Language-Action Understanding and Generation for Autonomous Driving](https://arxiv.org/abs/2603.01441v1)

**Authors:** Xinyang Wang, Qian Liu, Wenjie Ding, Zhao Yang, Wei Li et al. (10 authors)

**Published:** 2026-03-02 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.01441v1) | [PDF](https://arxiv.org/pdf/2603.01441v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are emerging as a promising paradigm for end-to-end autonomous driving, valued for their potential to leverage world knowledge and reason about complex driving scenes. However, existing methods suffer from two critical limitations: a persistent misalignment between language instructions and action outputs, and the inherent inefficiency of typical auto-regressive action generation. In this paper, we introduce LinkVLA, a novel architecture that directly addresse...

</details>

---
