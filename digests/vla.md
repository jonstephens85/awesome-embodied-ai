# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-03 16:54 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://arxiv.org/abs/2602.02459v1)

**Authors:** Zhiyu Huang, Yun Zhang, Johnson Liu, Rui Song, Chen Tang et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.02459v1) | [PDF](https://arxiv.org/pdf/2602.02459v1.pdf) | [Project Page](https://ucla-mobility.github.io/TIC-VLA/)

<details>
<summary>Abstract</summary>

Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control. Vision-language-action (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action. We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation. TIC-VLA defines a delayed ...

</details>

---

### [World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454v1)

**Authors:** Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, Yunzhe Zhang, Jiarao Liu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2602.02454v1) | [PDF](https://arxiv.org/pdf/2602.02454v1.pdf) | [Project Page](https://world-gymnast.github.io/)

<details>
<summary>Abstract</summary>

Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world...

</details>

---

### [Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2602.01166v1)

**Authors:** Shuanghao Bai, Jing Lyu, Wanqi Zhou, Zhe Li, Dakai Wang et al. (12 authors)

**Published:** 2026-02-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01166v1) | [PDF](https://arxiv.org/pdf/2602.01166v1.pdf) | [Project Page](\href{https://loveju1y.github.io/Latent-Reasoning-VLA/}{LaRA-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception and control. We propose Latent Reasoning VLA (\textbf{LaRA-VLA}), a unified VLA framework that internalizes multi-modal CoT reasoning into continuous latent representations for embodied action. LaRA-VLA performs unified reasoning and prediction in latent space, eliminating explic...

</details>

---

## Other Recent Papers

### [MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models](https://arxiv.org/abs/2602.02212v1)

**Authors:** Zheyuan Zhou, Liang Du, Zixun Sun, Xiaoyu Zhou, Ruimin Ye et al. (8 authors)

**Published:** 2026-02-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02212v1) | [PDF](https://arxiv.org/pdf/2602.02212v1.pdf)

<details>
<summary>Abstract</summary>

Despite significant progress in Visual-Language-Action (VLA), in highly complex and dynamic environments that involve real-time unpredictable interactions (such as 3D open worlds and large-scale PvP games), existing approaches remain inefficient at extracting action-critical signals from redundant sensor streams. To tackle this, we introduce MAIN-VLA, a framework that explicitly Models the Abstraction of Intention and eNvironment to ground decision-making in deep semantic alignment rather than s...

</details>

---

### [FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2602.02142v1)

**Authors:** Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay et al. (7 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.02142v1) | [PDF](https://arxiv.org/pdf/2602.02142v1.pdf)

<details>
<summary>Abstract</summary>

Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot s...

</details>

---

### [Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models](https://arxiv.org/abs/2602.01834v1)

**Authors:** Siqi Wen, Shu Yang, Shaopeng Fu, Jingfeng Zhang, Lijie Hu et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01834v1) | [PDF](https://arxiv.org/pdf/2602.01834v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models close the perception action loop by translating multimodal instructions into executable behaviors, but this very capability magnifies safety risks: jailbreaks that merely yield toxic text in LLMs can trigger unsafe physical actions in embodied systems. Existing defenses alignment, filtering, or prompt hardening intervene too late or at the wrong modality, leaving fused representations exploitable. We introduce a concept-based dictionary learning framework for ...

</details>

---

### [From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models](https://arxiv.org/abs/2602.01811v1)

**Authors:** Wentao Zhang, Aolan Sun, Wentao Mo, Xiaoyang Qu, Yuxin Zheng et al. (6 authors)

**Published:** 2026-02-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01811v1) | [PDF](https://arxiv.org/pdf/2602.01811v1.pdf)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models for embodied agents integrate perception, reasoning, and control, they remain constrained by two critical weaknesses: first, during grasping tasks, the action tokens generated by the language model often exhibit subtle spatial deviations from the target object, resulting in grasp failures; second, they lack the ability to reliably recognize task completion, which leads to redundant actions and frequent timeout errors. To address these challenges and enha...

</details>

---

### [Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs](https://arxiv.org/abs/2602.01158v1)

**Authors:** Daniel Yezid Guarnizo Orjuela, Leonardo Scappatura, Veronica Di Gennaro, Riccardo Andrea Izzo, Gianluca Bardaro et al. (6 authors)

**Published:** 2026-02-01 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01158v1) | [PDF](https://arxiv.org/pdf/2602.01158v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a dominant paradigm for generalist robotic manipulation, unifying perception and control within a single end-to-end architecture. However, despite their success in controlled environments, reliable real-world deployment is severely hindered by their fragility to visual disturbances. While existing literature extensively addresses physical occlusions caused by scene geometry, a critical mode remains largely unexplored: image corruptions. These s...

</details>

---

### [StreamVLA: Breaking the Reason-Act Cycle via Completion-State Gating](https://arxiv.org/abs/2602.01100v1)

**Authors:** Hang Wu, Tongqing Chen, Jiasen Wang, Xiaotao Li, Lu Fang

**Published:** 2026-02-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01100v1) | [PDF](https://arxiv.org/pdf/2602.01100v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robotic manipulation requires bridging the gap between high-level planning (System 2) and low-level control (System 1). Current Vision-Language-Action (VLA) models often entangle these processes, performing redundant multimodal reasoning at every timestep, which leads to high latency and goal instability. To address this, we present StreamVLA, a dual-system architecture that unifies textual task decomposition, visual goal imagination, and continuous action generation within a single...

</details>

---

### [A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation](https://arxiv.org/abs/2602.01067v1)

**Authors:** Fanqi Lin, Kushal Arora, Jean Mercat, Haruki Nishimura, Paarth Shah et al. (12 authors)

**Published:** 2026-02-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.01067v1) | [PDF](https://arxiv.org/pdf/2602.01067v1.pdf)

<details>
<summary>Abstract</summary>

Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy per...

</details>

---
