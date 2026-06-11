# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-11 18:46 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](https://arxiv.org/abs/2606.12403v1)

**Authors:** Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li et al. (7 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12403v1) | [PDF](https://arxiv.org/pdf/2606.12403v1.pdf) | [Project Page](https://world-pilot.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit semantic grounding from large-scale pretraining and perform competently across in-distribution manipulation tasks. This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture. We present World Pilot, a VLA framework that augments the policy with priors from a World-Action Model (WAM), routed into the decision chain through two complementary pathw...

</details>

---

### [VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.12396v1)

**Authors:** Jin Yao, Dhruva Dixith Kurra, Tom Lampo, Zezhou Cheng, Danhua Guo et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12396v1) | [PDF](https://arxiv.org/pdf/2606.12396v1.pdf) | [Project Page](https://yaojin17.github.io/VLGA/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that provide no dense spatial signal. We introduce VLGA, the first vision-language-action model supervised to reconstruct the dense 3D world it d...

</details>

---

### [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/abs/2606.12366v1)

**Authors:** Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12366v1) | [PDF](https://arxiv.org/pdf/2606.12366v1.pdf) | [Project Page](https://xukechun.github.io/papers/APT/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs) with continuous action experts have achieved strong manipulation performance, yet generalization to out-of-distribution (OOD) language instructions remains poor. A known challenge is the structural imbalance in VLA data, where language is far less diverse than visual and action content, making policies prone to visual shortcuts. While discrete-action methods mitigate this through vision-language co-training,...

</details>

---

### [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](https://arxiv.org/abs/2606.12352v1)

**Authors:** Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12352v1) | [PDF](https://arxiv.org/pdf/2606.12352v1.pdf) | [Project Page](https://chorus-model.github.io)

<details>
<summary>Abstract</summary>

Multi-robot collaboration allows robots to efficiently take on a wide range of tasks, from moving a couch through a doorway to assembling structures on a construction site. However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team size, and decentralized methods that train one policy per robot often require explicit alignment procedures or information sharing at inference ...

</details>

---

### [DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model](https://arxiv.org/abs/2606.12105v1)

**Authors:** Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, Moritz Reuss, Gianluca Geraci et al. (7 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12105v1) | [PDF](https://arxiv.org/pdf/2606.12105v1.pdf) | [Project Page](\href{https://intuitive-robots.github.io/DAM-VLA/}{intuitive-robots.github.io/DAM-VLA/})

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models inherit a shared synchronous clock from vision-language pretraining, processing every input at one rate. This is misaligned with physical interaction, where a high-frequency modality changes at hundreds of hertz, vision evolves more slowly, and language stays constant across an episode. A synchronous VLA oversamples slow modalities, undersamples fast ones, and caps action generation at the lowest effective frequency. We hypothesize that decoupling temporal pro...

</details>

---

### [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](https://arxiv.org/abs/2606.11743v1)

**Authors:** Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su et al. (8 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.GR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.11743v1) | [PDF](https://arxiv.org/pdf/2606.11743v1.pdf) | [Project Page](https://tac-corl.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models provide strong visual, language, and action priors for robot manipulation, but visual observations alone often miss the local contact state required for contact-rich tasks. We present TacCoRL, a scalable framework that injects Tactile feedback into VLA policies and improves them through sim-real Co-training and simulation-based reinforcement learning (RL), without requiring large-scale tactile pretraining or extensive real-world contact exploration. The key id...

</details>

---

### [DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World](https://arxiv.org/abs/2606.11901v1)

**Authors:** Tobias Jülg, Seongjin Bien, Simon Hilber, Yannik Blei, Pierre Krack et al. (10 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.11901v1) | [PDF](https://arxiv.org/pdf/2606.11901v1.pdf) | [Project Page](https://duobench.github.io/)

<details>
<summary>Abstract</summary>

Bimanual robot systems substantially expand manipulation capabilities, but coordinating two arms introduces additional control complexity and failure modes that are not well captured by existing benchmarks. We introduce DuoBench, an extensible benchmarking framework for bimanual manipulation policies on the FR3 Duo platform. DuoBench comprises eleven tasks spanning four coordination categories, implemented in simulation and partially reproduced in the real world through reproducible task recipes...

</details>

---

### [Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models](https://arxiv.org/abs/2606.11324v1)

**Authors:** Yifu Yuan, Yaoting Huang, Xianze Yao, Yutong Li, Shuoheng Zhang et al. (23 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.11324v1) | [PDF](https://arxiv.org/pdf/2606.11324v1.pdf) | [Project Page](https://embodied-r.github.io/)

<details>
<summary>Abstract</summary>

We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates comprehensive embodied reasoning capabilities, spanning embodied cognition, task planning, correction, and pointing, within a single architecture toward general physical intelligence. Leveraging three automated data construction pipelines to significantly expand the data coverage of critical capabilities, we build a large-scale data system of over 15B tokens, and design a multi-task balanced RL recipe to allevi...

</details>

---

### [LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination](https://arxiv.org/abs/2606.10862v1)

**Authors:** Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei

**Published:** 2026-06-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10862v1) | [PDF](https://arxiv.org/pdf/2606.10862v1.pdf) | [GitHub](https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ})

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VL...

</details>

---

### [SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation](https://arxiv.org/abs/2606.10305v1)

**Authors:** Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun et al. (11 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10305v1) | [PDF](https://arxiv.org/pdf/2606.10305v1.pdf) | [Project Page](https://qianzhong-chen.github.io/sarm2.github.io/)

<details>
<summary>Abstract</summary>

Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still relies heavily on behavior cloning, which requires costly high-quality demonstrations and keeps policies near the demonstration distribution. Reward models can reduce this dependence by reweighting demonstrations and providing dense supervision for on-robot reinforcement learning (RL), but they must be dense, accurate, and general. Existing methods fall short: task-specific stage-aware models are accurate but r...

</details>

---

### [Dynamic Execution Horizon Prediction for Chunk-based Robot Policies](https://arxiv.org/abs/2606.11408v1)

**Authors:** Yuchi Zhao, Miroslav Bogdanovic, Arjun Sohal, Liyu Tao, Kourosh Darvish et al. (8 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.11408v1) | [PDF](https://arxiv.org/pdf/2606.11408v1.pdf) | [Project Page](https://dehp-chunking.github.io/)

<details>
<summary>Abstract</summary>

Action chunking has become a standard design in modern robot policies, from diffusion/flow policies to vision-language-action models, where the policy predicts a sequence of actions and executes a fixed number of them instead of acting one step at a time. However, this paradigm relies on a key assumption: a fixed execution horizon. During chunk execution, the policy operates open-loop, which is particularly problematic for fine-grained manipulation tasks that require frequent replanning. In prac...

</details>

---

## Other Recent Papers

### [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/abs/2606.12299v1)

**Authors:** Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12299v1) | [PDF](https://arxiv.org/pdf/2606.12299v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide a natural language interface to robot control, but the mapping from language to behavior is often brittle and unintuitive: semantically similar instructions can induce drastically different behaviors, while some capabilities may not be elicitable through prompting alone. As a result, both human instructions and zero-shot language models can fail to reliably steer VLAs toward successful task execution. In this work, we propose a framework that interacti...

</details>

---

### [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/abs/2606.12109v1)

**Authors:** Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12109v1) | [PDF](https://arxiv.org/pdf/2606.12109v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and acute action manifold collapse due to data scarcity. In this paper, we present I...

</details>

---

### [Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations](https://arxiv.org/abs/2606.10614v1)

**Authors:** Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee et al. (6 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.10614v1) | [PDF](https://arxiv.org/pdf/2606.10614v1.pdf)

<details>
<summary>Abstract</summary>

Robotic foundation models pre-trained on human demonstration videos have shown promise, but a significant embodiment gap remains when the resulting policies are deployed on real robots. A common remedy is to fine-tune these models on robot-specific demonstrations. However, robot data collection can be prohibitively expensive and time-consuming, which is particularly acute in dexterous manipulation, e.g., teleoperating a multi-fingered hand for even a single atomic task can take days. To address ...

</details>

---

### [VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models](https://arxiv.org/abs/2606.10568v1)

**Authors:** Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei et al. (9 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10568v1) | [PDF](https://arxiv.org/pdf/2606.10568v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong promise for robotic manipulation, but their reliability at test time remains limited by one-shot action prediction, where even small action errors can cause grasp failure, collision, or incorrect task progression. A natural alternative is to equip VLA systems with test-time verification, allowing multiple candidate actions to be proposed and evaluated before execution. However, reliable action verification is challenging because it requires n...

</details>

---

### [Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults](https://arxiv.org/abs/2606.10501v1)

**Authors:** Minsoo Jo, Taeju Kwon, Junha Chun, Youngjoon Jeong, Taesup Kim

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10501v1) | [PDF](https://arxiv.org/pdf/2606.10501v1.pdf)

<details>
<summary>Abstract</summary>

Deploying Vision-Language-Action (VLA) models in real robotic systems requires robustness not only to semantic and perceptual variations, but also to embodiment-side faults that change how actions are physically realized. Real robots can experience joint-level changes caused by actuator degradation, hardware faults, safety limits, collision damage, or wear-induced friction. These faults are critical because they alter the action-to-motion interface of a policy, disrupting the learned closed-loop...

</details>

---

### [Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models](https://arxiv.org/abs/2606.10495v1)

**Authors:** Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang et al. (6 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.10495v1) | [PDF](https://arxiv.org/pdf/2606.10495v1.pdf)

<details>
<summary>Abstract</summary>

Safe social navigation requires robots to distinguish people from ordinary obstacles and to react before danger becomes imminent. We show that pretrained Vision-Language-Action (VLA) models already encode pedestrian-object distinctions and future collision signals in their internal representations, but behavior cloning fails to translate these signals into socially appropriate actions. To address this mismatch, we propose SALSA, a two-stage annotation-free post-training framework: (1) social beh...

</details>

---

### [A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation](https://arxiv.org/abs/2606.10366v1)

**Authors:** Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10366v1) | [PDF](https://arxiv.org/pdf/2606.10366v1.pdf)

<details>
<summary>Abstract</summary>

Simulation has become an essential tool for evaluating and improving vision-language-action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation. Recent simulation benchmarks have made substantial progress on realism and diversity, yet these platforms have not been widely adopted as reliable proxies for real-world policy evaluation. In this work, we investigate this issue through the lens of sim-and-real correlation. We conduct a sy...

</details>

---

### [What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents](https://arxiv.org/abs/2606.10267v1)

**Authors:** Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang et al. (7 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.10267v1) | [PDF](https://arxiv.org/pdf/2606.10267v1.pdf)

<details>
<summary>Abstract</summary>

Hierarchical vision-language-action (Hi-VLA) systems have emerged as a promising paradigm for complex robot manipulation, by using high-level VLM planners to decompose tasks into language subgoals executed by low-level VLA controllers. Despite recent empirical progress, there is a lack of unified design principles for these systems: existing Hi-VLA systems differ in how they choose and connect planners, controllers, mechanisms to switch between the two, and how observations and memory are repres...

</details>

---
