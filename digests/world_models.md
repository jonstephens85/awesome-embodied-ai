# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-11 23:13 UTC

**Papers found:** 14

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

### [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/abs/2606.11417v1)

**Authors:** Ayush Mittal, Dhruv Gupta

**Published:** 2026-06-09 | **Categories:** cs.LG, cs.AI, stat.ML

**Links:** [arXiv](https://arxiv.org/abs/2606.11417v1) | [PDF](https://arxiv.org/pdf/2606.11417v1.pdf) | [GitHub](https://github.com/Zetetic-Dhruv/audit-compression-progress)

<details>
<summary>Abstract</summary>

Compression progress is a long-standing proposal for intrinsic motivation: reward an agent when its world model becomes better at predicting or compressing experience. The folk claim is that this reward is "credible" because it is paid only for learning. We make this precise and prove it. If intrinsic reward is the signed decrease of a fixed sealed-audit loss, r_t = E(theta_{t-1}) - E(theta_t), then cumulative reward telescopes exactly to endpoint audit improvement, so no policy can push reward ...

</details>

---

### [PLUME: Probabilistic Latent Unified World Modeling and Parameter Estimation for Multi-Finger Manipulation](https://arxiv.org/abs/2606.11396v1)

**Authors:** Abhinav Kumar, Soshi Iba, Rana Soltani Zarrin, Dmitry Berenson

**Published:** 2026-06-09 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.11396v1) | [PDF](https://arxiv.org/pdf/2606.11396v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Dexterous manipulation with multi-finger hands can be sensitive to physical parameters such as object shape, pose, and friction coefficients. While simulation enables large-scale data collection with known parameter values, simulation-trained policies must still handle uncertainty at deployment, where the true parameters and therefore the true dynamics are unknown. Standard domain randomization strategies may be insufficient for precise tasks like screwdriver turning, as manipulation strategies ...

</details>

---

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

## Other Recent Papers

### [Slots, Transitions, Loops: Learning Composable World Models for ARC](https://arxiv.org/abs/2606.12316v1)

**Authors:** Gege Gao, Bernhard Schölkopf, Andreas Geiger

**Published:** 2026-06-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.12316v1) | [PDF](https://arxiv.org/pdf/2606.12316v1.pdf)

<details>
<summary>Abstract</summary>

ARC tests in-context rule induction: given a few input-output demonstrations, a model must infer the hidden rule and apply it to a new query. While many approaches express ARC rules through language, code, or symbolic programs, ARC itself is visual-symbolic: rules appear as grid transitions over objects, colors, shapes, and spatial relations. We introduce Loop-OWM, an object-centric world-modeling architecture that learns these rules as composable transitions over structured states. It combines ...

</details>

---

### [Making Foresight Actionable: Repurposing Representation Alignment in World Action Models](https://arxiv.org/abs/2606.12217v1)

**Authors:** Lu Qiu, Yizhuo Li, Yi Chen, Yuying Ge, Yixiao Ge et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12217v1) | [PDF](https://arxiv.org/pdf/2606.12217v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) offer a promising route for robot manipulation by using video generation models to model future scene evolution before producing control actions. However, our empirical observations reveal a phenomenon: generating plausible visual futures does not always guarantee the extraction of accurate actions. To diagnose this failure, we conduct action-head attention analysis and causal interventions. We find that the action decoder fails to focus on task-relevant interaction re...

</details>

---

### [World Model Self-Distillation: Training World Models to Solve General Tasks](https://arxiv.org/abs/2606.12072v1)

**Authors:** Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro

**Published:** 2026-06-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.12072v1) | [PDF](https://arxiv.org/pdf/2606.12072v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making. Existing approaches either outsource this reasoning to language or vision-language models, or rely on supervised fine-tuning with paired task-execution videos, which are costly to collect and difficult to scale. We propose a scalable framework that elicits task-solving ability...

</details>

---

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
