# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-28 18:36 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling](https://arxiv.org/abs/2605.28803v1)

**Authors:** Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang et al. (9 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28803v1) | [PDF](https://arxiv.org/pdf/2605.28803v1.pdf) | [GitHub](https://github.com/UCMP13753/Omega-QVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We c...

</details>

---

### [How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures](https://arxiv.org/abs/2605.28726v1)

**Authors:** Krishnam Gupta

**Published:** 2026-05-27 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28726v1) | [PDF](https://arxiv.org/pdf/2605.28726v1.pdf) | [GitHub](https://github.com/krishnam94/vla-edge)

<details>
<summary>Abstract</summary>

We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level. Running VQ-BeT, Diffusion Policy, and ACT on identical evaluation protocols (n=450 episodes across PushT and ALOHA 14-DOF bimanual manipulation), we find: (1) direction reversal rate is a universal failure predictor across all three architectures (AUROC=0.93, 0.79, 0.91; p<0.001); (2) jerk monitoring is predictive only for discrete-token architectures, following a discrete-to-continuo...

</details>

---

### [GEM: Generative Supervision Helps Embodied Intelligence](https://arxiv.org/abs/2605.28548v1)

**Authors:** Ruowen Zhao, Bangguo Li, Zuyan Liu, Yinan Liang, Junliang Ye et al. (12 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28548v1) | [PDF](https://arxiv.org/pdf/2605.28548v1.pdf) | [Project Page](https://zhaorw02.github.io/GEM/)

<details>
<summary>Abstract</summary>

Embodied Vision-Language Models (VLMs) have demonstrated impressive performance and generalization in robotics, particularly within Vision-Language-Action frameworks. However, a significant gap remains between the high-level semantic focus of standard text-guided pre-training paradigms and the low-level spatial and physical knowledge critical for execution in embodied environments. In this paper, we introduce GEM, a Generative-supervised Embodied vision-language Model designed to bridge this div...

</details>

---

### [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](https://arxiv.org/abs/2605.27886v1)

**Authors:** Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.27886v1) | [PDF](https://arxiv.org/pdf/2605.27886v1.pdf) | [GitHub](https://github.com/NathanWu7/Tabero)

<details>
<summary>Abstract</summary>

Tactile sensing is essential for robots to achieve human-like gentle manipulation. However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop force feedback mechanisms. To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception. Fi...

</details>

---

### [Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation](https://arxiv.org/abs/2605.27582v1)

**Authors:** Hongyu Ding, Sizhuo Zhang, Ziming Xu, Jinwen Guo, Hongxiu Liu et al. (16 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.27582v1) | [PDF](https://arxiv.org/pdf/2605.27582v1.pdf) | [Project Page](https://xetroubadour.github.io/Uni-LaViRA/)

<details>
<summary>Abstract</summary>

Embodied navigation requires an agent to map language and visual observations to a stream of spatial actions that drive a real robot through environments it has never seen. The dominant approach has been to scale vision-language-action (VLA) foundation models on ever-larger collections of robot trajectories. This paper argues that, for navigation specifically, generality can be obtained structurally, not only through data scale. The underlying decision structure of navigation reduces to a single...

</details>

---

### [FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies](https://arxiv.org/abs/2605.27284v1)

**Authors:** Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun et al. (14 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.27284v1) | [PDF](https://arxiv.org/pdf/2605.27284v1.pdf) | [Project Page](https://finevla.xlang.ai/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly expected to not only complete robot tasks, but also follow human instructions about how those tasks should be executed. However, existing robot datasets usually pair trajectories with coarse goal-level language, leaving execution-critical details such as active arm, approach direction, and contact region unspecified. This limits steerable policy learning and robotic video understanding. We introduce FineVLA, an open framework for action-aligne...

</details>

---

## Other Recent Papers

### [PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation](https://arxiv.org/abs/2605.28634v1)

**Authors:** Yutai Li, Shaohui Peng, Jiaming Guo, Di Huang, Zihao Zhang et al. (11 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28634v1) | [PDF](https://arxiv.org/pdf/2605.28634v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for generalist robotic policies, yet their adaptation is hindered by data inefficiency and poor generalization. We argue that these bottlenecks stem from the prevailing Direct Instruction-to-Control Mapping, which forces models to memorize monolithic trajectories rather than reusable motion patterns, i.e., primitives. We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble & Assemble para...

</details>

---

### [What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies](https://arxiv.org/abs/2605.28527v1)

**Authors:** Jiachen Zhang, Junnan Nie, Junyi Lao, Wei Cheng, Chenghao Liu et al. (7 authors)

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28527v1) | [PDF](https://arxiv.org/pdf/2605.28527v1.pdf)

<details>
<summary>Abstract</summary>

Vision--language--action (VLA) policies are trained to imitate actions; their loss never asks them to estimate reward, progress, or future success. Their frozen representations nevertheless carry such information, and it can be read out and used to guide action choice without retraining the policy. From mixed successful and failed manipulation trajectories on LIBERO-Goal, we recover Monte-Carlo outcome targets using lightweight linear probes on frozen features. The targets are consistently predi...

</details>

---

### [Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation](https://arxiv.org/abs/2605.28486v1)

**Authors:** Yongchen Wang, Kangyi Lu, Lan Wei, Dandan Zhang

**Published:** 2026-05-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.28486v1) | [PDF](https://arxiv.org/pdf/2605.28486v1.pdf)

<details>
<summary>Abstract</summary>

Magnetically actuated microrobots have been used as wireless, non-contact manipulation tools at microscales, making them promising for minimally invasive applications. However, their control remains challenging due to indirect actuation, limited sensing, and nonlinear magnetic interactions. In this work, we propose Mag-VLA, a vision-language-action (VLA) model for dexterous magnetic microrobot manipulation using two robotic arms with mounted magnets for dynamic magnetic-field construction. Biman...

</details>

---

### [ProgVLA: Progress-Aware Robot Manipulation Skill Learning](https://arxiv.org/abs/2605.28231v1)

**Authors:** Seungsu Kim, Jinyoung Choi, Seungmin Baek, Jean-Michel Renders

**Published:** 2026-05-27 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.28231v1) | [PDF](https://arxiv.org/pdf/2605.28231v1.pdf)

<details>
<summary>Abstract</summary>

We present ProgVLA, a compact vision-language-action (VLA) model designed for reliable robot manipulation under tight compute and memory budgets. The model specifically focuses on efficiently processing long multi-modal sequences by maintaining an explicit representation of task progress over extended horizons. To this end, ProgVLA integrates two key components. First, a multi-modal encoder with a two-stage Perceiver resampling scheme compresses variable-length visual, language, and propriocepti...

</details>

---

### [VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking](https://arxiv.org/abs/2605.28083v1)

**Authors:** Jiyuan Fu, Kaixun Jiang, Jingkai Jia, Zhaoyu Chen, Xueyao Chen et al. (10 authors)

**Published:** 2026-05-27 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.28083v1) | [PDF](https://arxiv.org/pdf/2605.28083v1.pdf)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models have emerged as powerful generalist policies, their severe vulnerability to adversarial patches significantly hinders their deployment in safety-critical domains. Moreover, existing patch attacks primarily focus on white-box settings, heavily overfitting to the specific action output space of the target model, which results in poor cross-architecture transferability. To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that...

</details>

---

### [Colosseum V2: Benchmarking Generalization for Vision Language Action Models](https://arxiv.org/abs/2605.27759v1)

**Authors:** Jeremy Morgan, Prajwal Vijay, Hyeonho Oh, Jincen Song, Ashvin Arora et al. (9 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.27759v1) | [PDF](https://arxiv.org/pdf/2605.27759v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models demonstrate promising generalization in robotic manipulation, driven by advances in large-scale vision and language pre-training. This progress can be misleading. Despite the zero-shot perception and language capabilities of VLAs, their overall task performance often degrades under distribution shifts, revealing gaps in how these systems translate high-level understanding into robust behavior. To systematically study this gap, we introduce Colosseum V2, a larg...

</details>

---

### [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](https://arxiv.org/abs/2605.27491v1)

**Authors:** Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang, Lintao Wang et al. (15 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.27491v1) | [PDF](https://arxiv.org/pdf/2605.27491v1.pdf)

<details>
<summary>Abstract</summary>

We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation. Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially improving action-following fidelity and trajectory coverage. On top of this foundation, three new modules close the loop fr...

</details>

---

### [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820v1)

**Authors:** Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Mingqi Yuan et al. (8 authors)

**Published:** 2026-05-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.26820v1) | [PDF](https://arxiv.org/pdf/2605.26820v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide a promising foundation for general-purpose robotics. However, their successful deployment in real-world scenarios requires the ability to continually acquire new skills while retaining previously learned behaviors. While pioneering research has studied the continual learning of VLA models in narrowly simulated environments, this challenge remains largely unexplored under realistic conditions. To address this limitation, we construct a real-world contin...

</details>

---
