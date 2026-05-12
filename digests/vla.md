# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-12 17:59 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.10925v1)

**Authors:** Xinyu Guo, Bin Xie, Wei Chai, Xianchi Deng, Tiancai Wang et al. (7 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10925v1) | [PDF](https://arxiv.org/pdf/2605.10925v1.pdf) | [Project Page](https://priorvla.github.io/)

<details>
<summary>Abstract</summary>

Large-scale pretraining has made Vision-Language-Action (VLA) models promising foundations for generalist robot manipulation, yet adapting them to downstream tasks remains necessary. However, the common practice of full fine-tuning treats pretraining as initialization and can shift broad priors toward narrow training-distribution patterns. We propose PriorVLA, a novel framework that preserves pretrained priors and learns to leverage them for effective adaptation. PriorVLA keeps a frozen Prior Ex...

</details>

---

### [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921v1)

**Authors:** Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen et al. (13 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10921v1) | [PDF](https://arxiv.org/pdf/2605.10921v1.pdf) | [Project Page](https://robomemarena.github.io)

<details>
<summary>Abstract</summary>

Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments. However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world evaluation. We address this gap with RoboMemArena, a large-scale benchmark of 26 tasks, with average traject...

</details>

---

### [CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving](https://arxiv.org/abs/2605.10426v1)

**Authors:** Minqing Huang, Yujiao Xiang, Zihan Liang, Jiajie Huang, Jingqi Wang et al. (10 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.10426v1) | [PDF](https://arxiv.org/pdf/2605.10426v1.pdf) | [GitHub](https://github.com/potatochip1211/CoWorld-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing reasoning mechanisms still struggle to provide planning-oriented intermediate representations: textual Chain-of-Thought (CoT) fails to preserve continuous spatiotemporal structure, while latent world reasoning remains difficult to use as a direct condition for action generation. In this paper, we propose CoWorld-VLA, a multi-expert world reasoning framework for autonomous...

</details>

---

## Other Recent Papers

### [HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models](https://arxiv.org/abs/2605.10942v1)

**Authors:** Qiuxuan Feng, Jiale Yu, Jiaming Liu, Yueru Jia, Zhuangzhe Wu et al. (11 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10942v1) | [PDF](https://arxiv.org/pdf/2605.10942v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a promising paradigm for robot control by modeling physical dynamics. Current WAMs generally follow two paradigms: the "Imagine-then-Execute" approach, which uses video prediction to infer actions via inverse dynamics, and the "Joint Modeling" approach, which jointly models actions and video representations. Based on systematic experiments, we observe a fundamental trade-off between these paradigms: the former explicitly leverages world models for gener...

</details>

---

### [CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models](https://arxiv.org/abs/2605.10903v1)

**Authors:** Wenxuan Song, Han Zhao, Fuhao Li, Ziyang Zhou, Xi Wang et al. (10 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10903v1) | [PDF](https://arxiv.org/pdf/2605.10903v1.pdf)

<details>
<summary>Abstract</summary>

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhan...

</details>

---

### [Unified Noise Steering for Efficient Human-Guided VLA Adaptation](https://arxiv.org/abs/2605.10821v1)

**Authors:** Junjie Lu, Xinyao Qin, Yuhua Jiang, Kaixin Wang, Chuheng Zhang et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10821v1) | [PDF](https://arxiv.org/pdf/2605.10821v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) models have emerged as strong priors for robotic manipulation, yet adapting them to real-world distributions remains challenging. In particular, on-robot reinforcement learning (RL) is expensive and time-consuming, so effective adaptation depends on efficient policy improvement within a limited budget of real-world interactions. Noise-space RL lowers the cost by keeping the pretrained VLA fixed as a denoising generator while updating only a lightweigh...

</details>

---

### [ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models](https://arxiv.org/abs/2605.10819v1)

**Authors:** Zuojin Tang, Haoyun Liu, Xinyuan Chang, Changjie Wu, Dongjie Huo et al. (14 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.10819v1) | [PDF](https://arxiv.org/pdf/2605.10819v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models remain constrained by the scarcity of action-labeled robot data, whereas action-free videos provide abundant evidence of how the physical world changes. Latent action models offer a promising way to extract such priors from videos, but reconstruction-trained latent codes are not necessarily suitable for policy generation: they may predict future observations while lacking the structure needed to be reused or generated coherently with robot actions. We introduc...

</details>

---

### [VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models](https://arxiv.org/abs/2605.10485v1)

**Authors:** Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan et al. (13 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10485v1) | [PDF](https://arxiv.org/pdf/2605.10485v1.pdf)

<details>
<summary>Abstract</summary>

Precise spatial reasoning is fundamental to robotic manipulation, yet the visual backbones of current vision-language-action (VLA) models are predominantly pretrained on 2D image data without explicit 3D geometric supervision, resulting in representations that lack accurate spatial awareness. Existing implicit spatial grounding methods partially address this by aligning VLA features with those of 3D-aware foundation models, but they rely on empirical layer search and perform alignment on LLM-lev...

</details>

---

### [Temporal Sampling Frequency Matters: A Capacity-Aware Study of End-to-End Driving Trajectory Prediction](https://arxiv.org/abs/2605.10388v1)

**Authors:** Yumao Liu, Tao Liu, Xiangyu Li, Jiaxiang Li, Ke Ma

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10388v1) | [PDF](https://arxiv.org/pdf/2605.10388v1.pdf)

<details>
<summary>Abstract</summary>

End to end (E2E) autonomous driving trajectory prediction is often trained with camera frames sampled at the highest available temporal frequency, assuming that denser sampling improves performance. We question this assumption by treating temporal sampling frequency as an explicit training set design variable. Starting from high frequency E2E driving datasets, we construct frequency sweep training sets by temporally subsampling camera frames along each trajectory. For each model dataset pair, we...

</details>

---

### [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](https://arxiv.org/abs/2605.10094v1)

**Authors:** Jianchao Zhao, Huoren Yang, Hu Yusong, Yuyang Gao, Qiguan Ou et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.10094v1) | [PDF](https://arxiv.org/pdf/2605.10094v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions. Existing evaluations typically treat test episodes as independent zero-shot trials. However, real robots often operate repeatedly in the same or slowly changing environments, where successful executions provide environment-verified evidence of reliable behavior patterns. We study this persistent-deployment setting,...

</details>

---

### [StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception](https://arxiv.org/abs/2605.09989v1)

**Authors:** Evans Han, Yunfan Jiang, Yingke Wang, Haoyue Xiao, Huang Huang et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.09989v1) | [PDF](https://arxiv.org/pdf/2605.09989v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in robot imitation learning have yielded powerful visuomotor policies capable of manipulating a wide variety of objects directly from monocular visual inputs. However, monocular observations inherently lack reliable depth cues and spatial awareness, which are critical for precise manipulation in cluttered or geometrically complex scenes. To address this limitation, we introduce StereoPolicy, a new visuomotor policy learning framework that directly leverages synchronized stereo im...

</details>

---

### [LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models](https://arxiv.org/abs/2605.09948v1)

**Authors:** Boyang Shen, Kaixiang Yang, Hao Wang, Qiuyu Yu, Qiang Xie et al. (7 authors)

**Published:** 2026-05-11 | **Categories:** cs.AI, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.09948v1) | [PDF](https://arxiv.org/pdf/2605.09948v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models typically treat the deepest representation of a vision-language backbone as universally optimal for action prediction. However, robotic manipulation is composed of many frequent closed-loop spatial adjustments, for which excessive abstraction may waste computation and weaken low-level geometric cues essential for precise control. Existing early-exit strategies attempt to reduce computation by stopping at predefined layers or applying heuristic rules su...

</details>

---

### [SABER: A Scalable Action-Based Embodied Dataset for Real-World VLA Adaptation](https://arxiv.org/abs/2605.09613v1)

**Authors:** Narsimha Menga, Parikshit Sakurikar, Amirreza Rouhi, Satya Sai Reddy, Anirudh Govil et al. (9 authors)

**Published:** 2026-05-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.09613v1) | [PDF](https://arxiv.org/pdf/2605.09613v1.pdf)

<details>
<summary>Abstract</summary>

Robotic deployment in real-world environments depends on rich, domain-specific action data as much as on strong model architecture. General-purpose robot foundation models show modest performance in complex unseen tasks such as manipulation in a retail domain when applied out of the box. The root cause is a data gap: retail environments are structurally absent from general robot pretraining distributions, and the path to filling that gap through teleoperation is prohibitively expensive, logistic...

</details>

---

### [Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning](https://arxiv.org/abs/2605.09537v1)

**Authors:** Kewei Chen, Yayu Long, Mingsheng Shang

**Published:** 2026-05-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.09537v1) | [PDF](https://arxiv.org/pdf/2605.09537v1.pdf)

<details>
<summary>Abstract</summary>

Despite rapid progress in Vision-Language-Action (VLA) models for robotic control, instruction drift remains a persistent failure mode in long-horizon tasks. This paper reconceptualizes this phenomenon, positing that instruction drift is fundamentally a systematic sampling error: local greedy sampling is prone to collapsing into "Negative Pivotal Windows"--irreversible local optima with high local probability that sever global success pathways. To address this, we propose Context-Aware Power Sam...

</details>

---

### [RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.09410v1)

**Authors:** Weijia Liufu, Xiaoyu Guo, Ruiyi Chen, Jingzhi Liu, Kaidong Zhang et al. (19 authors)

**Published:** 2026-05-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.09410v1) | [PDF](https://arxiv.org/pdf/2605.09410v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models remain brittle in long-horizon, contact-rich manipulation because success-only imitation provides little supervision for execution drift, while failed rollouts are often discarded. We introduce RePO-VLA, a recovery-driven policy optimization framework that assigns distinct roles to success, recovery, and failure trajectories. RePO-VLA first applies Recovery-Aware Initialization (RAI), slicing recovery segments and resetting history so corrective actions depend...

</details>

---

### [SKG-VLA: Scene Knowledge Graph Priors for Structured Scene Semantics and Multimodal Reasoning for Decision Making](https://arxiv.org/abs/2605.09343v1)

**Authors:** Zeyu Li, Lei Li

**Published:** 2026-05-10 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.09343v1) | [PDF](https://arxiv.org/pdf/2605.09343v1.pdf)

<details>
<summary>Abstract</summary>

Decision making in large-scale complaint handling systems increasingly relies on heterogeneous evidence, including complaint narratives, screenshots, order metadata, historical interactions, and platform policies. Existing complaint understanding systems mainly perform shallow classification or template matching over isolated modalities, while underutilizing explicit scene structure, rule knowledge, and cross-evidence dependencies. To address this limitation, we present SKG-VLA for multimodal co...

</details>

---
