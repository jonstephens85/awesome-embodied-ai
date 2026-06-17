# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-17 18:15 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Uncertainty Quantification for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2606.18043v1)

**Authors:** Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella et al. (8 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.18043v1) | [PDF](https://arxiv.org/pdf/2606.18043v1.pdf) | [Project Page](tum-lsy.github.io/uq_vla/)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This presents a critical limitation for real-world deployment in non-stationary environments, where models inevitably encounter scenarios outside...

</details>

---

### [GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning](https://arxiv.org/abs/2606.17480v1)

**Authors:** Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi et al. (6 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17480v1) | [PDF](https://arxiv.org/pdf/2606.17480v1.pdf) | [Project Page](https://aigeeksgroup.github.io/GeneralVLA-2) | [GitHub](https://github.com/AIGeeksGroup/GeneralVLA-2)

<details>
<summary>Abstract</summary>

Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Sec...

</details>

---

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

## Other Recent Papers

### [WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](https://arxiv.org/abs/2606.18097v1)

**Authors:** Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao et al. (8 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.18097v1) | [PDF](https://arxiv.org/pdf/2606.18097v1.pdf)

<details>
<summary>Abstract</summary>

Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an infinite-dimensional configuration space and deform continuously under contact with grippers, fixtures, and the workspace, making them a demanding benchmark for general dexterous manipulation. Despite their importance, policy development and comparison remain difficult: existing benchmarks are often tied to specific hardware s...

</details>

---

### [ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation](https://arxiv.org/abs/2606.17937v1)

**Authors:** Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu et al. (11 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17937v1) | [PDF](https://arxiv.org/pdf/2606.17937v1.pdf)

<details>
<summary>Abstract</summary>

Most Vision-Language-Action (VLA) models map observations directly to actions without explicit reasoning, limiting their capacity for reasoning-intensive long-horizon tasks. To address this, existing approaches adopt Chain-of-Thought (CoT) reasoning to enable subgoal decomposition and spatial anticipation. However, those methods lack a unified architecture for effective cross-modal reasoning and fail to explicitly include inverse reasoning ability based on the target state. We argue that manipul...

</details>

---

### [PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space](https://arxiv.org/abs/2606.17924v1)

**Authors:** Bochen Yang, Lianlei Shan

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.17924v1) | [PDF](https://arxiv.org/pdf/2606.17924v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model...

</details>

---

### [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](https://arxiv.org/abs/2606.17598v1)

**Authors:** Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang et al. (10 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.17598v1) | [PDF](https://arxiv.org/pdf/2606.17598v1.pdf)

<details>
<summary>Abstract</summary>

Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present MuseVLA, an adaptive multimodal sensing VLA model that integrates novel sensors as on-demand tools for robotic manipulation. Given a task ins...

</details>

---

### [WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation](https://arxiv.org/abs/2606.17463v1)

**Authors:** Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue et al. (9 authors)

**Published:** 2026-06-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17463v1) | [PDF](https://arxiv.org/pdf/2606.17463v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off i...

</details>

---

### [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846v1)

**Authors:** Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li et al. (23 authors)

**Published:** 2026-06-16 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.17846v1) | [PDF](https://arxiv.org/pdf/2606.17846v1.pdf)

<details>
<summary>Abstract</summary>

Foundation models in language and multimodality achieve strong generalization by aligning heterogeneous data under a unified formulation and training at scale. In this report, we investigate whether this scaling recipe can be applied to robotic manipulation to achieve genuine generalization. This is challenging because, unlike text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in diversity, making alignment and scale simultaneously difficult. We present Qwen-Rob...

</details>

---

### [ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining](https://arxiv.org/abs/2606.17200v1)

**Authors:** Hao Li, Ganlong Zhao, Yufei Liu, Haotian Hou, Guoquan Ye et al. (11 authors)

**Published:** 2026-06-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.17200v1) | [PDF](https://arxiv.org/pdf/2606.17200v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models benefit from large-scale and diverse embodied data, yet scaling robot trajectory collection is costly and labor-intensive. Recent advances show that large-scale egocentric human videos provide complementary real-world supervision in pretraining. However, joint training on human and robot data remains challenging due to divergences in action spaces, embodiment structures, temporal dynamics, and supervision quality. We introduce ACE-EGO-0, a unified VLA pretrain...

</details>

---

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
