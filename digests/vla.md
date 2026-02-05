# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-05 22:18 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning](https://arxiv.org/abs/2602.04315v1)

**Authors:** Guoqing Ma, Siheng Wang, Zeyu Zhang, Shan Yu, Hao Tang

**Published:** 2026-02-04 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.04315v1) | [PDF](https://arxiv.org/pdf/2602.04315v1.pdf) | [Project Page](https://aigeeksgroup.github.io/GeneralVLA) | [GitHub](https://github.com/AIGeeksGroup/GeneralVLA)

<details>
<summary>Abstract</summary>

Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is that the models exhibit limited zero-shot capability, which hampers their ability to generalize effectively to unseen scenarios. In this work, we propose GeneralVLA (Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning), a hierarchical vision-language-...

</details>

---

### [Reshaping Action Error Distributions for Reliable Vision-Language-Action Models](https://arxiv.org/abs/2602.04228v1)

**Authors:** Shuanghao Bai, Dakai Wang, Cheng Chi, Wanqi Zhou, Jing Lyu et al. (11 authors)

**Published:** 2026-02-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.04228v1) | [PDF](https://arxiv.org/pdf/2602.04228v1.pdf) | [Project Page](https://cognition2actionlab.github.io/VLA-TMEE.github.io/)

<details>
<summary>Abstract</summary>

In robotic manipulation, vision-language-action (VLA) models have emerged as a promising paradigm for learning generalizable and scalable robot policies. Most existing VLA frameworks rely on standard supervised objectives, typically cross-entropy for discrete actions and mean squared error (MSE) for continuous action regression, which impose strong pointwise constraints on individual predictions. In this work, we focus on continuous-action VLA models and move beyond conventional MSE-based regres...

</details>

---

### [Natural Language Instructions for Scene-Responsive Human-in-the-Loop Motion Planning in Autonomous Driving using Vision-Language-Action Models](https://arxiv.org/abs/2602.04184v1)

**Authors:** Angel Martinez-Sanchez, Parthib Roy, Ross Greer

**Published:** 2026-02-04 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.04184v1) | [PDF](https://arxiv.org/pdf/2602.04184v1.pdf) | [GitHub](https://github.com/Mi3-Lab/doScenes-VLM-Planning)

<details>
<summary>Abstract</summary>

Instruction-grounded driving, where passenger language guides trajectory planning, requires vehicles to understand intent before motion. However, most prior instruction-following planners rely on simulation or fixed command vocabularies, limiting real-world generalization. doScenes, the first real-world dataset linking free-form instructions (with referentiality) to nuScenes ground-truth motion, enables instruction-conditioned planning. In this work, we adapt OpenEMMA, an open-source MLLM-based ...

</details>

---

### [RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization](https://arxiv.org/abs/2602.03310v1)

**Authors:** Songming Liu, Bangguo Li, Kai Ma, Lingxuan Wu, Hengkai Tan et al. (8 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03310v1) | [PDF](https://arxiv.org/pdf/2602.03310v1.pdf) | [Project Page](https://rdt-robotics.github.io/rdt2/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models hold promise for generalist robotics but currently struggle with data scarcity, architectural inefficiencies, and the inability to generalize across different hardware platforms. We introduce RDT2, a robotic foundation model built upon a 7B parameter VLM designed to enable zero-shot deployment on novel embodiments for open-vocabulary tasks. To achieve this, we collected one of the largest open-source robotic datasets--over 10,000 hours of demonstrations in div...

</details>

---

## Other Recent Papers

### [Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data](https://arxiv.org/abs/2602.04600v1)

**Authors:** Jialiang Li, Yi Qiao, Yunhan Guo, Changwen Chen, Wenzhao Lian

**Published:** 2026-02-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.04600v1) | [PDF](https://arxiv.org/pdf/2602.04600v1.pdf)

<details>
<summary>Abstract</summary>

Achieving generalizable manipulation in unconstrained environments requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However, existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex environments. In this work, we formalize active perception as a non-Markovian process driven by information gain and decision branching, providing a structured categorization of visual active perc...

</details>

---

### [SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models](https://arxiv.org/abs/2602.04208v1)

**Authors:** Hyeonbeom Choi, Daechul Ahn, Youhan Lee, Taewook Kang, Seongwon Cho et al. (6 authors)

**Published:** 2026-02-04 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2602.04208v1) | [PDF](https://arxiv.org/pdf/2602.04208v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic control, with test-time scaling (TTS) gaining attention to enhance robustness beyond training. However, existing TTS methods for VLAs require additional training, verifiers, and multiple forward passes, making them impractical for deployment. Moreover, they intervene only at action decoding while keeping visual representations fixed-insufficient under perceptual ambiguity, where reconsidering how...

</details>

---

### [Efficient Long-Horizon Vision-Language-Action Models via Static-Dynamic Disentanglement](https://arxiv.org/abs/2602.03983v1)

**Authors:** Weikang Qiu, Tinglin Huang, Aosong Feng, Rex Ying

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03983v1) | [PDF](https://arxiv.org/pdf/2602.03983v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for generalist robotic control. Built upon vision-language model (VLM) architectures, VLAs predict actions conditioned on visual observations and language instructions, achieving strong performance and generalization across tasks. However, VLAs face two major challenges: limited long-horizon context and inefficient inference due to the quadratic attention complexity and large parameter counts. Our work is motivated...

</details>

---

### [QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization](https://arxiv.org/abs/2602.03782v1)

**Authors:** Yuhao Xu, Yantai Yang, Zhenyang Fan, Yufan Liu, Yuming Li et al. (7 authors)

**Published:** 2026-02-03 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03782v1) | [PDF](https://arxiv.org/pdf/2602.03782v1.pdf)

<details>
<summary>Abstract</summary>

The advent of Vision-Language-Action (VLA) models represents a significant leap for embodied intelligence, yet their immense computational demands critically hinder deployment on resource-constrained robotic platforms. Intuitively, low-bit quantization is a prevalent and preferred technique for large-scale model compression. However, we find that a systematic analysis of VLA model's quantization is fundamentally lacking. We argue that naively applying uniform-bit quantization from Large Language...

</details>

---

### [MVP-LAM: Learning Action-Centric Latent Action via Cross-Viewpoint Reconstruction](https://arxiv.org/abs/2602.03668v1)

**Authors:** Jung Min Lee, Dohyeok Lee, Seokhun Ju, Taehyun Cho, Jin Woo Koo et al. (8 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.03668v1) | [PDF](https://arxiv.org/pdf/2602.03668v1.pdf)

<details>
<summary>Abstract</summary>

Learning \emph{latent actions} from diverse human videos enables scaling robot learning beyond embodiment-specific robot datasets, and these latent actions have recently been used as pseudo-action labels for vision-language-action (VLA) model pretraining. To make VLA pretraining effective, latent actions should contain information about the underlying agent's actions despite the absence of ground-truth labels. We propose \textbf{M}ulti-\textbf{V}iew\textbf{P}oint \textbf{L}atent \textbf{A}ction ...

</details>

---

### [CRL-VLA: Continual Vision-Language-Action Learning](https://arxiv.org/abs/2602.03445v1)

**Authors:** Qixin Zeng, Shuo Zhang, Hongyin Zhang, Renjie Wang, Han Zhao et al. (9 authors)

**Published:** 2026-02-03 | **Categories:** cs.AI, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03445v1) | [PDF](https://arxiv.org/pdf/2602.03445v1.pdf)

<details>
<summary>Abstract</summary>

Lifelong learning is critical for embodied agents in open-world environments, where reinforcement learning fine-tuning has emerged as an important paradigm to enable Vision-Language-Action (VLA) models to master dexterous manipulation through environmental interaction. Thus, Continual Reinforcement Learning (CRL) is a promising pathway for deploying VLA models in lifelong robotic scenarios, yet balancing stability (retaining old skills) and plasticity (learning new ones) remains a formidable cha...

</details>

---

### [When Attention Betrays: Erasing Backdoor Attacks in Robotic Policies by Reconstructing Visual Tokens](https://arxiv.org/abs/2602.03153v1)

**Authors:** Xuetao Li, Pinhan Fu, Wenke Huang, Nengyuan Pan, Songhua Yang et al. (10 authors)

**Published:** 2026-02-03 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.03153v1) | [PDF](https://arxiv.org/pdf/2602.03153v1.pdf)

<details>
<summary>Abstract</summary>

Downstream fine-tuning of vision-language-action (VLA) models enhances robotics, yet exposes the pipeline to backdoor risks. Attackers can pretrain VLAs on poisoned data to implant backdoors that remain stealthy but can trigger harmful behavior during inference. However, existing defenses either lack mechanistic insight into multimodal backdoors or impose prohibitive computational costs via full-model retraining. To this end, we uncover a deep-layer attention grabbing mechanism: backdoors redire...

</details>

---
