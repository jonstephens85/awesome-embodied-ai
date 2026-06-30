# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-30 17:53 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics](https://arxiv.org/abs/2606.29247v1)

**Authors:** Jiashuo Sun, Yue He, Wenxuan Liu, Tao Mao, Jiazheng Wang et al. (7 authors)

**Published:** 2026-06-28 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29247v1) | [PDF](https://arxiv.org/pdf/2606.29247v1.pdf) | [GitHub](https://github.com/VCL-HNU/SurgVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models represent a promising direction for embodied intelligence in surgical robotics. Despite the prevalence of VLA benchmarks for general robotics, standardized evaluation platforms specifically designed for surgical contexts remain absent. To address this limitation, we present SurgVLA-Bench, the first comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics. Leveraging the SurRoL simulation platform, we construct a hierarchical task tax...

</details>

---

## Other Recent Papers

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

### [Event-VLA: Action-Conditioned Event Fusion for Robust Vision-Language-Action Model](https://arxiv.org/abs/2606.29384v1)

**Authors:** Jiaxin Liu, Xun Xu, Zhenhao Zhang, Hanqing Wang, Ruiqi Chen et al. (8 authors)

**Published:** 2026-06-28 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.29384v1) | [PDF](https://arxiv.org/pdf/2606.29384v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become an important paradigm of embodied AI. However, existing VLA models typically assume well-lit and stable indoor settings, while real-world embodied manipulation may involve degraded RGB observations caused by illumination shifts, posing critical challenges for robust robotic manipulation. To address this gap, we propose \textbf{Event-VLA}, an event-enhanced VLA framework for generalizable manipulation across varying illumination conditions. We formu...

</details>

---

### [Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs](https://arxiv.org/abs/2606.29350v1)

**Authors:** Junzhou Chen, Jindong Wang, Gang Zhou

**Published:** 2026-06-28 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29350v1) | [PDF](https://arxiv.org/pdf/2606.29350v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language models and vision-language action models endow the robot with unprecedented capabilities. However, the input of video and high-resolution images yields a massive number of visual tokens, leading to extremely high inference latency and severely hindering the robot's real-time control. To break through this computational bottleneck, we propose ST-Merge, a plug-and-play, training-free framework that efficiently fuses redundant tokens directly during the visual encoding phase. By exp...

</details>

---

### [Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering](https://arxiv.org/abs/2606.29201v1)

**Authors:** Hao Wang, Jiuzhou Lei, Dayou Li, Bangya Liu, Minghui Zheng et al. (8 authors)

**Published:** 2026-06-28 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29201v1) | [PDF](https://arxiv.org/pdf/2606.29201v1.pdf)

<details>
<summary>Abstract</summary>

Behavior-cloned policies often learn multiple behavior modes from demonstration datasets, including modes that are unsafe or otherwise undesired at deployment. For example, a policy trained on diverse handover demonstrations may learn to pass a knife blade-first. Standard remedies such as data curation and inference-time steering either require access to the original demonstrations for full retraining or add substantial inference-time overhead. To address this gap, we propose MoRE(Mode Redirecti...

</details>

---
