# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-02 22:56 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model](https://arxiv.org/abs/2607.01212v1)

**Authors:** Chenyang Ma, Yue Yang, Radu Corcodel, Siddarth Jain, Andrew Wu et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.01212v1) | [PDF](https://arxiv.org/pdf/2607.01212v1.pdf) | [Project Page](https://dannymcy.github.io/furniturevla/)

<details>
<summary>Abstract</summary>

Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect high-quality real-world demonstrations. To address extreme long-h...

</details>

---

### [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678v1)

**Authors:** Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin et al. (21 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00678v1) | [PDF](https://arxiv.org/pdf/2607.00678v1.pdf) | [GitHub](https://github.com/amap-cvlab/ABot-Manipulation)

<details>
<summary>Abstract</summary>

Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...

</details>

---

### [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](https://arxiv.org/abs/2607.00666v1)

**Authors:** Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.00666v1) | [PDF](https://arxiv.org/pdf/2607.00666v1.pdf) | [Project Page](https://twkang43.github.io/projects/dart) | [GitHub](https://github.com/snumprlab/dart)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models often fail to perform the same learned tasks under environmental shifts, such as changes in camera pose and shifts to a different but similar robot (e.g., from Panda to UR5e). Adapting these models to the shifted environment (i.e., target domain) often requires training on multiple demonstrations for each task, which are costly to collect. To reduce the burden of data curation and training, we propose an analogy-based method that adapts VLA models under enviro...

</details>

---

### [Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments](https://arxiv.org/abs/2606.32009v1)

**Authors:** Xiaopeng Lin, Ruoqi Yang, Shijie Lian, Zhaolong Shen, Bin Yu et al. (17 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.32009v1) | [PDF](https://arxiv.org/pdf/2606.32009v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models across robot embodiments require high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enable...

</details>

---

### [Adapting Generalist Robot Policies with Semantic Reinforcement Learning](https://arxiv.org/abs/2606.31958v1)

**Authors:** Jagdeep Singh Bhatia, Andrew Wagenmaker, William Chen, Sergey Levine

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31958v1) | [PDF](https://arxiv.org/pdf/2606.31958v1.pdf) | [Project Page](https://semantic-action-rl.github.io/)

<details>
<summary>Abstract</summary>

Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretr...

</details>

---

### [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](https://arxiv.org/abs/2606.31329v2)

**Authors:** Dongyoon Hwang, Byungkun Lee, Dongjin Kim, Hyojin Jang, Hoiyeong Jin et al. (10 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31329v2) | [PDF](https://arxiv.org/pdf/2606.31329v2.pdf) | [Project Page](is) | [GitHub](https://github.com/DAVIAN-Robotics/3D_HAMSTER)

<details>
<summary>Abstract</summary>

Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene...

</details>

---

### [MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents](https://arxiv.org/abs/2606.31167v1)

**Authors:** Hao Sun, Yu Song, Shiyu Teng, Ziwei Niu, Yen-Wei Chen

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31167v1) | [PDF](https://arxiv.org/pdf/2606.31167v1.pdf) | [GitHub](http://github.com/kiva12138/mirth)

<details>
<summary>Abstract</summary>

VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH...

</details>

---

### [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](https://arxiv.org/abs/2606.31993v1)

**Authors:** Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu et al. (6 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31993v1) | [PDF](https://arxiv.org/pdf/2606.31993v1.pdf) | [Project Page](https://robin-lab.cs.utexas.edu/oopsieverse/)

<details>
<summary>Abstract</summary>

While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for...

</details>

---

## Other Recent Papers

### [Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation](https://arxiv.org/abs/2607.01067v1)

**Authors:** Chi Zhang, Penglin Cai, Ziheng Xi, Haoqi Yuan, Hao Luo et al. (9 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.01067v1) | [PDF](https://arxiv.org/pdf/2607.01067v1.pdf)

<details>
<summary>Abstract</summary>

As an essential modality for dexterous and contact-rich tasks, tactile sensing provides precise force feedback that cannot be reliably inferred from vision. However, limited by hardware and data collection systems, existing datasets with tactility remain small in scale and narrow in contact coverage. Meanwhile, Vision-Language-Action (VLA) models with tactile modality are constrained on dynamics-agnostic post-training, which limits the performance ceiling on downstream tasks. In this paper, we p...

</details>

---

### [Unleashing More Actions via Action Compositional Training for VLA Models](https://arxiv.org/abs/2607.00351v1)

**Authors:** Kai Peng, Jie Lu, Xiaojiang Peng

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00351v1) | [PDF](https://arxiv.org/pdf/2607.00351v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models excel at robotic manipulation, driven by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this overfitting, acquiring high-quality robot data remains notoriously labor...

</details>

---

### [Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models](https://arxiv.org/abs/2606.31846v1)

**Authors:** Lang Cao, Renhong Chen, Luyi Li, Peng Wang, Mofan Peng et al. (6 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31846v1) | [PDF](https://arxiv.org/pdf/2606.31846v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top ...

</details>

---

### [UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models](https://arxiv.org/abs/2606.31723v1)

**Authors:** Xidong Zhang, Yichi Zhang, Jiaxin Shi, Fucai Zhu, Siyu Zhu et al. (8 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31723v1) | [PDF](https://arxiv.org/pdf/2606.31723v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile semantics and future physical interactions. To this end, we...

</details>

---

### [Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation](https://arxiv.org/abs/2606.31382v1)

**Authors:** Fengnian Zhang, Tao Huang, Siyu Xu, Zhong Jin, Chang Xu

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31382v1) | [PDF](https://arxiv.org/pdf/2606.31382v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this ...

</details>

---

### [Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2606.31160v1)

**Authors:** Anh Dung Dinh, Simon Khan, Flora Salim

**Published:** 2026-06-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.31160v1) | [PDF](https://arxiv.org/pdf/2606.31160v1.pdf)

<details>
<summary>Abstract</summary>

Modern Vision-Language-Action (VLA) planners for autonomous driving emit a chain-of-causation (CoC) reasoning step \emph{before} producing a trajectory. The reasoning is autoregressive and dominates inference latency, while the trajectory head is parallel and cheap. Latency is an operational constraint in autonomous driving, so accelerating the reasoning step is the central problem we address. We observe that CoC reasoning has two qualitatively different needs: most tokens continue routine setup...

</details>

---

### [A Modular Vision-Language-Action Robotics Framework for Indoor Environments](https://arxiv.org/abs/2606.31144v1)

**Authors:** Anindya Jana, Snehasis Banerjee, Arup Sadhu, Ranjan Dasgupta

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31144v1) | [PDF](https://arxiv.org/pdf/2606.31144v1.pdf)

<details>
<summary>Abstract</summary>

This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline t...

</details>

---

### [ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies](https://arxiv.org/abs/2606.31132v1)

**Authors:** Andrew Zou Li, Gokul Swamy, Yonatan Bisk, Andrea Bajcsy

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31132v1) | [PDF](https://arxiv.org/pdf/2606.31132v1.pdf)

<details>
<summary>Abstract</summary>

Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, tas...

</details>

---
