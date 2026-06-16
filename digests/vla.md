# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-16 23:17 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055v1)

**Authors:** Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin et al. (35 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17055v1) | [PDF](https://arxiv.org/pdf/2606.17055v1.pdf) | [Project Page](https://tactile-rex.github.io/)

<details>
<summary>Abstract</summary>

The ability to react dynamically to tactile signals has long been considered crucial to agile human-level dexterity. Yet contemporary learning-based Vision-Language-Action (VLA) models for robotic manipulation generally either overlook the tactile modality or are limited to encoders with static cues, due in part to the scarcity of diverse training data and standardized evaluation, architectural constraints in current VLA models, and limitations of static tactile encoders. In this paper, we push ...

</details>

---

### [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046v1)

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An et al. (10 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17046v1) | [PDF](https://arxiv.org/pdf/2606.17046v1.pdf) | [Project Page](https://cvlab-kaist.github.io/Geometric-Action-Model/)

<details>
<summary>Abstract</summary>

Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action M...

</details>

---

### [Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes](https://arxiv.org/abs/2606.17043v1)

**Authors:** Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo et al. (9 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17043v1) | [PDF](https://arxiv.org/pdf/2606.17043v1.pdf) | [Project Page](https://acerobotics-vla.github.io/HABC-Website)

<details>
<summary>Abstract</summary>

When pretrained VLA policies are fine-tuned through online RL, each rollout episode produces only a single binary outcome (success or failure), yet the actor update requires per-transition supervision. Existing approaches commonly reduce this sparse outcome to a single scalar reward or advantage signal, which conflates distinct forms of transition-level feedback and provides limited guidance once basic task success becomes achievable. First, a single scalar signal conflates the two objectives of...

</details>

---

### [R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies](https://arxiv.org/abs/2606.17040v1)

**Authors:** Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu et al. (10 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17040v1) | [PDF](https://arxiv.org/pdf/2606.17040v1.pdf) | [Project Page](https://r2rdreamer.github.io/)

<details>
<summary>Abstract</summary>

Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation can create controllable variation, but requires complex environment and object setup and may introduce a sim-to-real gap. Recent real-to-real ...

</details>

---

### [Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks](https://arxiv.org/abs/2606.16178v1)

**Authors:** Rutav Shah, Rajat Kumar Jenamani, Xiaohan Zhang, Lingfeng Sun, Roberto Martín-Martín et al. (8 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.16178v1) | [PDF](https://arxiv.org/pdf/2606.16178v1.pdf) | [Project Page](https://shahrutav.github.io/short-term-memory)

<details>
<summary>Abstract</summary>

Many robotic tasks require short-term memory, whether it's retrieving an object that's no longer visible or turning off an appliance after a set period. Yet, most visuomotor policies trained via imitation learning rely only on immediate sensory input without using past experiences to guide decisions. We present PRISM, a transformer-based architecture for visuomotor policies to effectively use short-term memory via two key components: (i) gated attention, which filters retrieved information to su...

</details>

---

### [Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time](https://arxiv.org/abs/2606.15631v1)

**Authors:** Jeongeun Park, Juhan Park, Taekyung Kim, Sungjoon Choi, Dongyoon Han et al. (6 authors)

**Published:** 2026-06-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.15631v1) | [PDF](https://arxiv.org/pdf/2606.15631v1.pdf) | [Project Page](https://recap-robot.github.io/)

<details>
<summary>Abstract</summary>

Extending a vision-language-action (VLA) policy to a new task typically requires task-specific teleoperated demonstrations and per-task fine-tuning, making adaptation costly in both data collection and compute. In this paper, we show that this target-side per-task adaptation cost can be replaced by retrieval. Our retrieval-augmented policy is trained once on paired demonstrations from the target embodiment (query) and a cheaper embodiment (pool, e.g., human-hand video), then frozen. New tasks ar...

</details>

---

## Other Recent Papers

### [ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011v1)

**Authors:** Wei Xiao, Weiliang Tang, Yuying Ge, Hui Zhou, Yao Mu et al. (7 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17011v1) | [PDF](https://arxiv.org/pdf/2606.17011v1.pdf)

<details>
<summary>Abstract</summary>

Human interventions provide crucial corrective signals for post-training Vision-Language-Action (VLA) models. However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control. Consequently, the collected intervention trajectories are often suboptimal, and methods that rely on human interventions as expert supervision can absorb hesitant, inefficient, or even erroneous behaviors. To address both the system and algo...

</details>

---

### [APEX: Adaptive Policy Execution for Precise Manipulation](https://arxiv.org/abs/2606.16504v1)

**Authors:** Mengfei Zhao, Chenxi Jiang, Tuo An, Jindou Jia, Jianfei Yang

**Published:** 2026-06-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.16504v1) | [PDF](https://arxiv.org/pdf/2606.16504v1.pdf)

<details>
<summary>Abstract</summary>

Modern imitation learning methods, including visuomotor and Vision-Language-Action (VLA) policies, typically output high-level action references that are executed by low-level controllers. However, the absence of higher-order reference signals, together with the policy's lack of awareness of the underlying low-level control dynamics during training, inevitably induces an execution gap. As a result, realized actions deviate systematically from policy-commanded ones, with a critical impact on prec...

</details>

---

### [Learned Image Compression for Vision-Language-Action Models](https://arxiv.org/abs/2606.16253v1)

**Authors:** Hyeonjun Kim, Jegwang Ryu, Sangbeom Ha, Junhyeok Lee, Jun-Hyuk Kim et al. (7 authors)

**Published:** 2026-06-15 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.16253v1) | [PDF](https://arxiv.org/pdf/2606.16253v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models increasingly rely on high-frequency multi-camera observations, making visual communication a major bottleneck for real-time robotic control in bandwidth-constrained or distributed deployment settings. Existing image and video codecs, however, are designed to preserve generic visual fidelity rather than the control performance of downstream VLA policies. In this work, we introduce SPARC (SPatially Adaptive Rate Control), a learned image compression framework ta...

</details>

---

### [ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation](https://arxiv.org/abs/2606.16208v1)

**Authors:** Tao Xu, Jiaxin Wang, Runhao Zhang, Jiayi Guan, Xianchao Zeng et al. (10 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.16208v1) | [PDF](https://arxiv.org/pdf/2606.16208v1.pdf)

<details>
<summary>Abstract</summary>

In robot imitation learning, influence functions provide a principled approach to quantify each demonstration's effect on robot task outcomes, yet scaling them to billion-parameter Vision-Language-Action (VLA) models is limited by computational and multitask bottlenecks. To this end, we propose ATHENA, an influence function framework tailored for multitask VLA data curation at a billion-parameter scale. Concretely, it leverages the Kronecker structure of linear-layer gradients to reduce projecti...

</details>

---

### [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768v1)

**Authors:** Jialei Chen, Kai Wang, Kang Chen, Shuaihang Chen, Feng Gao et al. (12 authors)

**Published:** 2026-06-14 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.15768v1) | [PDF](https://arxiv.org/pdf/2606.15768v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) leverage large-scale vision-language pretraining for semantic robot control, but often lack explicit foresight into how robot actions change the scene. World-Action Models (WAMs) address this limitation by conditioning policies on predicted futures, yet existing approaches typically rely on computationally expensive video generation with substantial pixel-level redundancy. We present LaWAM, a Latent World Action Model that exposes predictive dynamics to robot...

</details>

---

### [Beyond English: Uncovering the Multilingual Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.15714v1)

**Authors:** Hanyang Chen, Hongliang Li, Jiarui Cao, Yang Li, Yang Jiang et al. (9 authors)

**Published:** 2026-06-14 | **Categories:** cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.15714v1) | [PDF](https://arxiv.org/pdf/2606.15714v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have recently demonstrated promising capabilities in learning generalist robot policies from large-scale multimodal data. However, most existing VLA systems are trained and evaluated primarily with English instructions, leaving their ability to understand and execute instructions in other languages largely unexplored. While the underlying large language models often possess multilingual capabilities, it remains unclear whether these multilingual capabilities transfe...

</details>

---

### [SAPS: Shared Autonomy for Policy Steering by Blending Teleoperation with a Pretrained VLA](https://arxiv.org/abs/2606.15568v1)

**Authors:** Crystal Zhou, Jehan Yang, Douglas J. Weber, Zackory Erickson

**Published:** 2026-06-14 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.15568v1) | [PDF](https://arxiv.org/pdf/2606.15568v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in Vision-Language-Action (VLA) models have demonstrated impressive generalist capabilities in robot manipulation, yet these policies can be brittle under out-of-distribution spatial and semantic perturbations. While human teleoperation offers reliable recovery, it can demand high cognitive load and precise manual control, and existing policy steering methods often require auxiliary models or sampler modifications. In this work, we introduce Shared Autonomy for Policy Steerin...

</details>

---

### [Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation](https://arxiv.org/abs/2606.15869v1)

**Authors:** Jingyu Li, Zhe Liu, Dongnan Hu, Junjie Wu, Zipei Ma et al. (13 authors)

**Published:** 2026-06-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.15869v1) | [PDF](https://arxiv.org/pdf/2606.15869v1.pdf)

<details>
<summary>Abstract</summary>

World action models~(WAMs) have shown great promise for autonomous driving and urban navigation. Built upon Vision-Language-Action models or video generation models, existing approaches suffer key limitations: (1) High inference latency due to future observation prediction at test time, and (2) tightly coupled video and action modeling leading to representational mismatch and degraded generalization. To address both issues, we propose Metis, an end-to-end WAM framework that decouples video gener...

</details>

---
