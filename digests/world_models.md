# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-10 18:29 UTC

**Papers found:** 22

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Next Forcing: Causal World Modeling with Multi-Chunk Prediction](https://arxiv.org/abs/2606.11187v1)

**Authors:** Gangwei Xu, Qihang Zhang, Jiaming Zhou, Xing Zhu, Yujun Shen et al. (7 authors)

**Published:** 2026-06-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.11187v1) | [PDF](https://arxiv.org/pdf/2606.11187v1.pdf) | [Project Page](https://gangweix.github.io/next-forcing/)

<details>
<summary>Abstract</summary>

Autoregressive video generation has emerged as a powerful paradigm for World Action Models (WAMs). However, existing approaches suffer from slow training convergence and limited converged accuracy, particularly at high frame rates, as the training supervision is confined to the current chunk without explicit signals about future dynamics; they also suffer from slow inference due to iterative video denoising. In this paper, we present Next Forcing, a multi-chunk prediction (MCP) framework for cau...

</details>

---

### [TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation](https://arxiv.org/abs/2606.11184v1)

**Authors:** Yujie Zang, Yuhang Zheng, Xian Nie, Yupeng Zheng, Shuai Tian et al. (10 authors)

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.11184v1) | [PDF](https://arxiv.org/pdf/2606.11184v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires robots to continuously perceive and regulate evolving physical interactions under dynamic contact transitions or complex surface geometries. Recent imitation learning methods improve contact-aware control by incorporating tactile or force feedback, but they rarely model the asymmetric spatiotemporal roles of global force and local tactile sensing. To address this, we propose TacForeSight, a lightweight force-conditioned tactile foresight framework for real-time...

</details>

---

### [WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129v1)

**Authors:** Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An et al. (11 authors)

**Published:** 2026-06-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.11129v1) | [PDF](https://arxiv.org/pdf/2606.11129v1.pdf) | [Project Page](https://alibaba-damo-academy.github.io/WorldOlympiad/) | [GitHub](https://github.com/alibaba-damo-academy/WorldOlympiad)

<details>
<summary>Abstract</summary>

We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-term temporal coherence, they provide limited insight into whether generated videos obey physical rules, preserve coherent 3D structure, and sustain controllable interactions over long horizons. To address this gap, WorldOlympiad decomposes world-model ev...

</details>

---

### [Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828v1)

**Authors:** Weijie Wang, Haoyu Zhao, Yifan Yang, Feng Chen, Zeyu Zhang et al. (10 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09828v1) | [PDF](https://arxiv.org/pdf/2606.09828v1.pdf) | [Project Page](https://aka.ms/latent-spatial-memory) | [GitHub](https://github.com/microsoft/LatentSpatialMemory)

<details>
<summary>Abstract</summary>

Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space. This design is both computationally expensive, requiring repeated rendering and VAE encoding, and inherently lossy, as the round trip through pixel space discards rich features of the learned latent representation. In this paper, we introduce \emph{latent spatial memory} for video world models, a persistent 3D cache that stores scene information ...

</details>

---

### [MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](https://arxiv.org/abs/2606.09827v1)

**Authors:** Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou et al. (9 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09827v1) | [PDF](https://arxiv.org/pdf/2606.09827v1.pdf) | [Project Page](https://shihao1895.github.io/MemoryVLA-PP-Web)

<details>
<summary>Abstract</summary>

Temporal modeling is essential for robotic manipulation, as effective control requires both memory of past interactions and imagination of future states. However, most VLA models rely primarily on the current observation and therefore struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived context, the hippocampal system to preserve episodic memory of past experience, and internal models to imagine possible futur...

</details>

---

### [iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](https://arxiv.org/abs/2606.09813v1)

**Authors:** Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng et al. (11 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09813v1) | [PDF](https://arxiv.org/pdf/2606.09813v1.pdf) | [Project Page](https://imac-wm.github.io/)

<details>
<summary>Abstract</summary>

Embodied world models have emerged as a pivotal paradigm for visual robotic decision-making and interactive environment simulation. However, conventional embodied frameworks rely on low-dimensional structured action vectors (e.g., joint angles and end-effector poses), which suffer from limited expressive capacity, poor generalization across diverse embodiments, and unnatural dynamic modeling for complex physical interactions. To address these limitations, this paper proposesiMac (Image as Action...

</details>

---

### [Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/abs/2606.09803v1)

**Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li et al. (16 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV, cs.GR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.09803v1) | [PDF](https://arxiv.org/pdf/2606.09803v1.pdf) | [GitHub](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Memory}{this)

<details>
<summary>Abstract</summary>

We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-action sequence, but their central failure is often memory rather than local image synthesis: after the camera leaves and returns, the scene or salient object may silently change. Existing memory designs are hard to compare because gains are entangled with backbone, training, retrieval, and evaluation d...

</details>

---

### [Prisma-World: Camera-Controllable Multi-Agent Video World Model](https://arxiv.org/abs/2606.09507v1)

**Authors:** Huiqiang Sun, Zhan Peng, Size Wu, Kun Wang, Kang Liao et al. (12 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.09507v1) | [PDF](https://arxiv.org/pdf/2606.09507v1.pdf) | [Project Page](https://huiqiang-sun.github.io/prisma-world/)

<details>
<summary>Abstract</summary>

Video world models have made rapid progress in generating controllable visual experiences, but most of them still simulate the world from a single observer. Extending such models to multiple agents raises a central challenge: if each agent's future state is generated independently, overlapping views may instantiate different versions of the same scene, leading to inconsistent objects, layouts, and appearances across agents. Conventional camera conditioning controls individual trajectories, but i...

</details>

---

## Other Recent Papers

### [Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football](https://arxiv.org/abs/2606.11120v1)

**Authors:** Andrew Kang, Priya Narasimhan

**Published:** 2026-06-09 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.11120v1) | [PDF](https://arxiv.org/pdf/2606.11120v1.pdf)

<details>
<summary>Abstract</summary>

We recast pass evaluation in football (soccer) as a Monte Carlo Tree Search (MCTS)-like evaluation problem whose components mostly exist in the literature under different names: a value model (possession value), a world model (multi-agent trajectories with ball interactions), and a policy over counterfactual actions (sampling pass variants with noise). Building on the first public high-fidelity tracking dataset with 3D ball trajectories from the Bundesliga, we introduce Monte Carlo Pass Search (...

</details>

---

### [WorldKernel: A World Model is the Coupling Kernel of Admissible Possible Worlds](https://arxiv.org/abs/2606.10934v1)

**Authors:** Fabio Rovai

**Published:** 2026-06-09 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10934v1) | [PDF](https://arxiv.org/pdf/2606.10934v1.pdf)

<details>
<summary>Abstract</summary>

A common assumption holds that enough observational and interventional data, given to a strong enough predictor, suffices. We report a failure mode that contradicts it. Across hundreds of structural causal models, on identified quantities a strong predictor and a Bayesian baseline both succeed, but on unidentified quantities (the couplings between counterfactual worlds) the predictor collapses to a point, on 28% of models to one no valid model can produce, while the truth is an admissible interv...

</details>

---

### [MODIP: Efficient Model-Based Optimization for Diffusion Policies](https://arxiv.org/abs/2606.10825v1)

**Authors:** Zakariae El Asri, Philippe Gratias-Quiquandon, Nicolas Thome, Olivier Sigaud

**Published:** 2026-06-09 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.10825v1) | [PDF](https://arxiv.org/pdf/2606.10825v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion policies (DPs) have emerged as expressive policy representations for robot learning, often used with imitation learning methods such as behavioral cloning (BC). However, while their success has largely been confined to BC, direct reinforcement learning (RL) fine-tuning remains challenging because actions are generated through a multi-step denoising process. In this work, we propose MODIP, a framework for the offline-to-online fine-tuning of DPs. Rather than directly applying RL to the ...

</details>

---

### [Can Image Models Imagine Time? ImageTime: A Novel Benchmark for Probing Visual World Modeling Through Spatiotemporal Consistency](https://arxiv.org/abs/2606.10620v1)

**Authors:** Xinrui Wu, Lichen Huang

**Published:** 2026-06-09 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10620v1) | [PDF](https://arxiv.org/pdf/2606.10620v1.pdf)

<details>
<summary>Abstract</summary>

Image generation models now produce high-quality static images, yet their ability to represent how a visual world changes over time remains poorly understood. Practical workflows such as storyboarding, step-by-step illustration, reference-guided editing, and video previsualization require models to preserve identities, objects, spatial relations, and causal order across multiple visual states. Existing evaluations largely measure single-image correctness, compositional alignment, or video qualit...

</details>

---

### [ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience](https://arxiv.org/abs/2606.10359v1)

**Authors:** Jia Luo

**Published:** 2026-06-09 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10359v1) | [PDF](https://arxiv.org/pdf/2606.10359v1.pdf)

<details>
<summary>Abstract</summary>

AI agents in supply chains face a fundamental epistemic gap: large language models (LLMs) interpret policies but lack physical grounding, while reinforcement learning (RL) optimizes flows but is semantically blind to unstructured constraints. We introduce REFLECTICHAIN, bridging this gap through a Generative Supply Chain World Model (SC-WM) - encoding heterogeneous supply networks into a 6-dim graph-latent space with physical conservation - and Double-Loop Learning that separates epistemic uncer...

</details>

---

### [BiWM: Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression](https://arxiv.org/abs/2606.10135v1)

**Authors:** Shaohao Rui, Xiaofeng Mao, Zhanyu Zhang, Peijia Lin, Yansong Zhu et al. (8 authors)

**Published:** 2026-06-08 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10135v1) | [PDF](https://arxiv.org/pdf/2606.10135v1.pdf)

<details>
<summary>Abstract</summary>

Transitioning bidirectional video diffusion models into an autoregressive paradigm improves the interactivity of video world models, but existing causal pipelines need many stages (control fine-tuning, autoregressive training, causal initialization, few-step distillation) and still trail bidirectional models in quality due to error accumulation. Recent world models such as Yume-1.5 and Matrix-Game-3.0 instead adopt a bidirectional autoregressive approach, gaining fidelity and stable long-horizon...

</details>

---

### [Business World Model](https://arxiv.org/abs/2606.10044v1)

**Authors:** Cecil Pang, Hiroki Sayama

**Published:** 2026-06-08 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.10044v1) | [PDF](https://arxiv.org/pdf/2606.10044v1.pdf)

<details>
<summary>Abstract</summary>

Businesses are increasingly adopting AI-enabled tools to improve productivity, reduce costs, and enhance products and services. However, the transformative potential of AI extends beyond automating predefined tasks: it lies in enabling intelligent systems to plan, optimize, and execute business initiatives from high-level strategic objectives. This paper introduces the concept and architecture of a business world model (BWM), a world model specialized for business and organizational environments...

</details>

---

### [Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics](https://arxiv.org/abs/2606.09640v1)

**Authors:** Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09640v1) | [PDF](https://arxiv.org/pdf/2606.09640v1.pdf)

<details>
<summary>Abstract</summary>

Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, p...

</details>

---

### [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499v1)

**Authors:** Ethan Rathbun, Ahmed Agha, Saaduddin Mahmud, Christopher Amato, Alina Oprea et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO, cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2606.09499v1) | [PDF](https://arxiv.org/pdf/2606.09499v1.pdf)

<details>
<summary>Abstract</summary>

World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing their integration into the robot learning pipeline. While highly practical, in this work we demonstrate that world models introduce a uniquely stealthy and effective data poisoning entry point into the robot learning supply chain that can result in the deployment of unsafe or otherwi...

</details>

---

### [$ω$-EVA: Envision, Verify, and Act with Latent Interactive World Models](https://arxiv.org/abs/2606.09457v1)

**Authors:** Zhenguo Sun, Yu Sun, Hande Huang, Alois Knoll

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09457v1) | [PDF](https://arxiv.org/pdf/2606.09457v1.pdf)

<details>
<summary>Abstract</summary>

Embodied policies typically map current observations directly to actions, leaving candidate-action consequences implicit. World models provide predictive supervision, representations, or external simulation, but rarely let a policy inspect the imagined consequence of its own proposal before acting. We introduce $ω$-EVA, a latent interactive world model that realizes an Envision--Verify--Act loop for embodied action generation. Its three-stage framework learns action-conditioned latent dynamics, ...

</details>

---

### [Toward Compiler World Models: Learning Latent Dynamics for Efficient Tensor Program Search](https://arxiv.org/abs/2606.09312v1)

**Authors:** Haolin Pan, Lianghong Huang, Xvlin Zhou, Mingjie Xing, Yanjun Wu

**Published:** 2026-06-08 | **Categories:** cs.LG, cs.PL

**Links:** [arXiv](https://arxiv.org/abs/2606.09312v1) | [PDF](https://arxiv.org/pdf/2606.09312v1.pdf)

<details>
<summary>Abstract</summary>

Tensor program optimization is essential for modern machine learning systems, but its search space is enormous. Existing auto-schedulers reduce measurement cost with learned cost models, yet they usually evaluate each candidate as a static code snapshot, ignoring the schedule trajectory that produced it. This makes them insensitive to action dependencies and vulnerable to superficial code variations. We propose a \emph{world-model-inspired} evaluator that models schedule evaluation as action-con...

</details>

---

### [FF-JEPA: Long-Horizon Planning in World Models with Latent Planners](https://arxiv.org/abs/2606.09311v1)

**Authors:** Sergi Masip, Jonathan Swinnen, Yutong Hu, Renaud Detry, Tinne Tuytelaars

**Published:** 2026-06-08 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.09311v1) | [PDF](https://arxiv.org/pdf/2606.09311v1.pdf)

<details>
<summary>Abstract</summary>

Joint Embedding Predictive Architectures (JEPAs) have shown promising world modeling capabilities, enabling planning in latent space by optimizing action trajectories using methods like the Cross-Entropy Method (CEM). These methods are, however, too computationally expensive and ineffective for long-horizon planning. Furthermore, these methods typically require an explicit image of the goal state, which is not always possible in real-world tasks. In this work, we tackle these limitations by prop...

</details>

---

### [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215v1)

**Authors:** Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang et al. (6 authors)

**Published:** 2026-06-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09215v1) | [PDF](https://arxiv.org/pdf/2606.09215v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple a video dynamics prior to the policy and have shown encouraging results on tabletop manipulation, but iterative denoising over high-dimensional video-action latents leaves them too slow for real-time humanoid loco-manipulation. The problem is compounded by the dominant hierarchical paradigm, in which a high-level manipulation policy controls only the upper body while a low-level controller tracks coarse base commands -- placing upper and lower body in inconsiste...

</details>

---

### [ATM: Action-Consistency Transfer Matrix for Diagnosing and Improving Latent World Models](https://arxiv.org/abs/2606.09028v1)

**Authors:** Jiaheng Chen

**Published:** 2026-06-08 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.09028v1) | [PDF](https://arxiv.org/pdf/2606.09028v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models are increasingly used for control and goal-conditioned planning, yet assessing whether their learned representations are useful for planning usually requires slow, planner-coupled simulator evaluation with CEM or similar planners. Such evaluation is black-box and model-complexity-dependent: under the same protocol, different world models may require minutes to hours per checkpoint. In this work, we propose ATM, an Action-Consistency Transfer Matrix for diagnosing whether late...

</details>

---
