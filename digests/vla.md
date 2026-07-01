# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-01 17:55 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](https://arxiv.org/abs/2606.31329v1)

**Authors:** Dongyoon Hwang, Byungkun Lee, Dongjin Kim, Hyojin Jang, Hoiyeong Jin et al. (10 authors)

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31329v1) | [PDF](https://arxiv.org/pdf/2606.31329v1.pdf) | [Project Page](is) | [GitHub](https://github.com/DAVIAN-Robotics/3D_HAMSTER)

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

### [Sequential Planning via Anchored Robotic Keypoints](https://arxiv.org/abs/2606.30613v1)

**Authors:** Bryce Grant, Aryeh Rothenberg, Logan Senning, Zonghe Chua, Zach Patterson et al. (6 authors)

**Published:** 2026-06-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.30613v1) | [PDF](https://arxiv.org/pdf/2606.30613v1.pdf) | [Project Page](https://cwru-aism.github.io/spark-page/)

<details>
<summary>Abstract</summary>

We present Sequential Planning via Anchored Robotic Keypoints, SPARK, a training-free neurosymbolic manipulation system that reaches 43.7% on six LIBERO-PRO position \& task cells, more than doubling CaP-Agent0 and Vision-Language-Action (VLA) baselines. CaP-Agent0, a multi-turn code-generation agent, achieves 18.2% by re-querying an LLM at every turn, but its restart-from-scratch solution proves costly against minor policy failures. Perception is the layer that fails most under position and tas...

</details>

---

### [Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision](https://arxiv.org/abs/2606.30552v1)

**Authors:** Haoyang Li, Guanlin Li, Youhe Feng, Chen Zhao, Zhuoran Wang et al. (12 authors)

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30552v1) | [PDF](https://arxiv.org/pdf/2606.30552v1.pdf) | [GitHub](https://github.com/RUCKBReasoning/ZR-0)

<details>
<summary>Abstract</summary>

Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe that the high-level cognitive process underlying manipulation, including scene perception, object identification, task planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of...

</details>

---

## Other Recent Papers

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

### [Vision-Language-Action Models: Experimental Insights from a Real-World UR5 Platform](https://arxiv.org/abs/2606.30456v1)

**Authors:** Mathilde Hochedel, Marc Lalonde

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30456v1) | [PDF](https://arxiv.org/pdf/2606.30456v1.pdf)

<details>
<summary>Abstract</summary>

This project investigates whether recent Vision-Language-Action (VLA) models can be transferred from controlled research benchmarks to a real-world robotic platform, specifically a UR5e manipulator, in a reproducible and operationally meaningful manner. The work integrates real-robot data acquisition, dataset engineering (compatible with the RLDS format), and the fine-tuning and deployment of OpenVLA and OpenVLA-OFT models, with systematic validation of action representations and control interfa...

</details>

---

### [Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation](https://arxiv.org/abs/2606.30318v1)

**Authors:** Yulin Zhou, Yimeng Wang, Nengyu Wang, Shaojia Xing, Shiyun Tu et al. (12 authors)

**Published:** 2026-06-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.30318v1) | [PDF](https://arxiv.org/pdf/2606.30318v1.pdf)

<details>
<summary>Abstract</summary>

General-purpose robot policies should be modeled as dynamical systems, yet many VLA and generative imitation policies still rely on present observations or short windows. This Markovian shortcut fails in memory-dependent manipulation: identical observations can demand different actions after different histories. We present Chronos, a physics-informed full-history framework for non-Markovian long-horizon manipulation. The key idea is to elevate observation history from auxiliary context to the la...

</details>

---

### [SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance](https://arxiv.org/abs/2606.30113v1)

**Authors:** Tengyue Jiang, Chunpu Xu, Jiayue Kang, Yao Mu

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.30113v1) | [PDF](https://arxiv.org/pdf/2606.30113v1.pdf)

<details>
<summary>Abstract</summary>

Discrete action tokenization provides a compact interface for autoregressive VLA policies, but accurately recovering continuous robot actions from discrete codes remains challenging. Existing tokenizers typically map each discrete code to a fixed continuous action prototype, ignoring the robot's current proprioceptive state. This limitation is particularly pronounced in manipulation, where the same action token may require different continuous controls under different joint configurations, objec...

</details>

---

### [OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action Generation Model](https://arxiv.org/abs/2606.29936v1)

**Authors:** Iok Tong Lei, Qingchen Xie, Yifan Wang, Yap Ying Jie, Zhidong Deng

**Published:** 2026-06-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.29936v1) | [PDF](https://arxiv.org/pdf/2606.29936v1.pdf)

<details>
<summary>Abstract</summary>

Open-environment tabletop robotic manipulation requires systems to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical execution, we propose OpenSPM, an open environment spatial persistent me...

</details>

---

### [Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models](https://arxiv.org/abs/2606.29892v1)

**Authors:** Siyao Chen, Jiakang Yuan, Jiaxin Wang, Tao Chen

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29892v1) | [PDF](https://arxiv.org/pdf/2606.29892v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has become indispensable for pushing Vision-Language-Action Models (VLAs) beyond static imitation learning. However, existing RL methods typically require external environmental feedback, relying on predefined success signals to guide policy updates. In this work, we show that VLA models possess useful internal evaluative capabilities: in discrete-action VLAs, trajectories with higher generation confidence are significantly more likely to succeed. Based on this observ...

</details>

---

### [Early Warning Signals for OpenVLA Failure under Visual Distribution Shift](https://arxiv.org/abs/2606.29699v1)

**Authors:** Dipesh Tharu Mahato, Rachel Ren

**Published:** 2026-06-29 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29699v1) | [PDF](https://arxiv.org/pdf/2606.29699v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action models combine perception, language grounding, and control in a single policy, but their failures are hard to diagnose once visual conditions shift. We test whether OpenVLA feedforward activations contain linearly decodable information about near term task failure in LIBERO manipulation rollouts. The policy is fixed throughout. We log internal activations during execution and fit lightweight monitors after the rollouts are collected. Occlusion is the main controlled stress...

</details>

---
