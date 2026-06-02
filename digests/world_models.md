# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-02 23:26 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RoboDream: Compositional World Models for Scalable Robot Data Synthesis](https://arxiv.org/abs/2606.02577v1)

**Authors:** Junjie Ye, Rong Xue, Basile Van Hoorick, Runhao Li, Harshitha Rajaprakash et al. (9 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.02577v1) | [PDF](https://arxiv.org/pdf/2606.02577v1.pdf) | [Project Page](https://junjieye.com/RoboDream/)

<details>
<summary>Abstract</summary>

Scaling robot learning requires large-scale, diverse demonstrations, yet real-world data collection via teleoperation remains prohibitively expensive and time-consuming. While video diffusion models offer a promising avenue for data scaling, existing generative approaches are often limited to superficial visual augmentation, or suffer from embodiment hallucinations that yield physically infeasible motions. We present a generalizable embodiment-centric world model that achieves scalable data gene...

</details>

---

### [Geometry-Aware Implicit Memory for Video World Models](https://arxiv.org/abs/2606.02436v1)

**Authors:** Zhengxuan Wei, Xu Guo, Xinghui Li, Xunzhi Xiang, Min Wei et al. (11 authors)

**Published:** 2026-06-01 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.02436v1) | [PDF](https://arxiv.org/pdf/2606.02436v1.pdf) | [Project Page](https://gim-world.github.io/)

<details>
<summary>Abstract</summary>

Video world models aim to simulate controllable visual environments, but long-horizon rollouts depend on what the model remembers after observations leave its native context window. Explicit memories retain frames or online 3D reconstructions, which can suffer from heuristic retrieval errors, redundant appearance storage, or reconstruction artifacts. Implicit memories compress history into a compact state, but existing designs are not explicitly constrained to encode cross-view scene geometry. W...

</details>

---

### [TabPrep: Closing the Feature Engineering Gap in Tabular Benchmarks](https://arxiv.org/abs/2606.02384v1)

**Authors:** Andrej Tschalzev, Nick Erickson, Yuyang Wang, Huzefa Rangwala, Stefan Lüdtke et al. (7 authors)

**Published:** 2026-06-01 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.02384v1) | [PDF](https://arxiv.org/pdf/2606.02384v1.pdf) | [GitHub](https://github.com/atschalz/tabprep)

<details>
<summary>Abstract</summary>

Progress in tabular machine learning has largely focused on increasingly sophisticated model architectures. At the same time, feature engineering remains a critical yet underexplored component of real-world modeling pipelines that is entirely absent from modern benchmarks, which creates an unquantified evaluation gap. In this work, we introduce TabPrep, a lightweight preprocessing pipeline composed of feature generators that are carefully designed to target three specific structural data pattern...

</details>

---

### [COMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/abs/2606.02372v1)

**Authors:** Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li

**Published:** 2026-06-01 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.02372v1) | [PDF](https://arxiv.org/pdf/2606.02372v1.pdf) | [GitHub](https://github.com/loyiv/CoMAP)

<details>
<summary>Abstract</summary>

Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution. However, existing textual world models are typically fixed after training, preventing them from adapting to the on-policy state-action distributions induced by an evolving agent. Meanwhile, agent-improvement methods often rely on external rewards or verifiers, limiting their applicability in realistic interactive environments. In this paper, we propose COMA...

</details>

---

### [RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation](https://arxiv.org/abs/2606.01600v1)

**Authors:** Huiqiong Li, Jiayu Wang, Zhiting Mei, Anirudha Majumdar, Jingjing Chen et al. (6 authors)

**Published:** 2026-06-01 | **Categories:** cs.CV, cs.CL, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01600v1) | [PDF](https://arxiv.org/pdf/2606.01600v1.pdf) | [Project Page](https://huiqiongli.github.io/RoboTrustBench/)

<details>
<summary>Abstract</summary>

Video world models are increasingly used in robotic manipulation, yet existing benchmarks mostly evaluate them under valid, feasible, and safe instructions. We introduce RoboTrustBench, a benchmark for evaluating the trustworthiness of video world models under four scenarios: Normal, Constraint-Sensitive, Counterfactual, and Adversarial. Built from real-world DROID episodes, RoboTrustBench contains 1,207 expert-validated instruction-image pairs and a six-dimensional evaluation protocol with 13 f...

</details>

---

### [BRo-JEPA: Learning Modular Arithmetic in Latent Space](https://arxiv.org/abs/2606.01372v1)

**Authors:** Divyansh Jha, Yuanfang Xie, Varan Mehra, Brennen Yu

**Published:** 2026-05-31 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.01372v1) | [PDF](https://arxiv.org/pdf/2606.01372v1.pdf) | [GitHub](https://github.com/DL-World-Models/mnist-math}{accessed)

<details>
<summary>Abstract</summary>

Can neural networks learn abstract algebraic rules, or do they merely memorize training patterns? We investigate this using MNIST digits as states and modular arithmetic operations as actions in a JEPA-style latent world model. Standard supervised baselines and JEPA models with additive operation embeddings fit seen operations but fail to extrapolate reliably to unseen ones. To bridge this gap, we introduce a block-rotation predictor that imposes the circular structure of modulo-10 arithmetic in...

</details>

---

### [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164v1)

**Authors:** Jiuming Liu, Chaojun Ni, Mengmeng Liu, Chensheng Peng, Fangjinhua Wang et al. (10 authors)

**Published:** 2026-05-31 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.01164v1) | [PDF](https://arxiv.org/pdf/2606.01164v1.pdf) | [GitHub](https://github.com/liujiuming123/Awesome-Interactive-World-Model)

<details>
<summary>Abstract</summary>

With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI, autonomous driving, etc. Through explicitly incorporating user actions into world state transition, recent literature empowers world modeling with interactivity in an action-conditioned video or 3D generation paradigm, further enhancing controllability over world evolutions and ...

</details>

---

## Other Recent Papers

### [From Zero to Hero: Training-Free Custom Concept Spawning in World Models](https://arxiv.org/abs/2606.02575v1)

**Authors:** Kiymet Akdemir, Pinar Yanardag

**Published:** 2026-06-01 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.02575v1) | [PDF](https://arxiv.org/pdf/2606.02575v1.pdf)

<details>
<summary>Abstract</summary>

Autoregressive world models have emerged as a powerful paradigm for interactive video generation, allowing users to navigate dynamically generated environments through actions. These models are typically conditioned on a text prompt and/or a single reference frame, from which the entire world is generated. Yet the moment the user navigates beyond what is visible in that frame, the unseen regions are populated by the base model's priors, with no mechanism for the user to specify what should appea...

</details>

---

### [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/abs/2606.02486v1)

**Authors:** Shahram Najam Syed, Arthur Jakobsson, Haoran Hao, Jeffrey Ichnowski

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02486v1) | [PDF](https://arxiv.org/pdf/2606.02486v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generalize across static manipulation but fail when objects move during task execution. They map the current observation to an action and assume the scene is stationary between observation and execution, so at any non-trivial object speed the resulting latency exceeds the time available to grasp. We close this gap with AHEAD (Anticipatory Horizon Extrapolation with Adaptive Dynamics), a predict-then-act wrapper that augments a frozen VLA with a motion-aware la...

</details>

---

### [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388v1)

**Authors:** Ning Lu, Baijiong Lin, Shengcai Liu, Jiahao Wu, Haoze Lv et al. (12 authors)

**Published:** 2026-06-01 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.02388v1) | [PDF](https://arxiv.org/pdf/2606.02388v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) improves large language model (LLM) agents by teaching them which actions lead to high rewards, but provides little supervision on what those actions do to the environment. World modeling (WM) can fill this gap, yet existing approaches often require separate simulators, extra training stages, or additional inference-time computation. We observe that on-policy RL rollouts already contain the needed signal: each transition pairs an action with its resulting next observa...

</details>

---

### [World-Task Factorization for Robot Learning](https://arxiv.org/abs/2606.02027v1)

**Authors:** Eduardo Sebastián, Adrian Pfisterer, Vito Mengers, Oliver Brock, Amanda Prorok

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.LG, cs.MA

**Links:** [arXiv](https://arxiv.org/abs/2606.02027v1) | [PDF](https://arxiv.org/pdf/2606.02027v1.pdf)

<details>
<summary>Abstract</summary>

Robot learning must produce policies that generalize to new combinations of constraints, teammates, and environments. To achieve this, we must structurally factor the policy, which is a choice that dictates what generalizes, what requires retraining, and what remains entangled. Existing methods span a wide spectrum, from expecting structure to emerge from data scaling, to hand-designing it via hierarchies, skill libraries or learned specializations. In this paper, we study what we argue is the m...

</details>

---

### [SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning](https://arxiv.org/abs/2606.01991v1)

**Authors:** Lichao Wang, Zhaoxing Ren, Tianzhuo Yang, Jiaming Ji, Chi Harold Liu et al. (7 authors)

**Published:** 2026-06-01 | **Categories:** cs.AI, cs.CL, cs.CY

**Links:** [arXiv](https://arxiv.org/abs/2606.01991v1) | [PDF](https://arxiv.org/pdf/2606.01991v1.pdf)

<details>
<summary>Abstract</summary>

As Large Language Model (LLM) agents increasingly leverage the Model Context Protocol (MCP) to operate in complex environments, the expansion of their action spaces offers agents unsafe capabilities and underscores the risk of power-seeking. While broad action space and greater environment influence are essential for task fulfillment, they create a fragile risk surface where minor errors or hallucinations are magnified into catastrophic failures. In response, we propose SafeMCP, a {server-side} ...

</details>

---

### [Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects](https://arxiv.org/abs/2606.01950v1)

**Authors:** Jens U. Kreber, Lukas Mack, Joerg Stueckler

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.01950v1) | [PDF](https://arxiv.org/pdf/2606.01950v1.pdf)

<details>
<summary>Abstract</summary>

World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. By representing the scene by object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel spatio-temporal transformer architecture that predicts future rigid body motion from a history of obj...

</details>

---

### [Unified Driving Tokens: Representation- and Geometry-Guided Discrete Tokenizer for Driving World Models and Planning](https://arxiv.org/abs/2606.01935v1)

**Authors:** Ziyang Yao, Zeyu Zhu, YunCheng Jiang, Zibin Guo, Huijing Zhao

**Published:** 2026-06-01 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.01935v1) | [PDF](https://arxiv.org/pdf/2606.01935v1.pdf)

<details>
<summary>Abstract</summary>

Discrete visual tokens should provide a compact representation for both token-based world modeling and planning in autonomous driving. However, most tokenizers are inherited from image generation and are optimized mainly for pixel reconstruction, which may leave a gap between what is easy to generate and what is useful to decode for driving decisions. We present a representation-guided and geometry-enhanced tokenizer that learns discrete tokens under joint supervision. The tokenizer aligns its d...

</details>

---

### [IMWM: Intuition Models Complement World Models for Latent Planning](https://arxiv.org/abs/2606.01626v1)

**Authors:** Baoqi Gao, Ruize Han, Miao Wang, Song Wang

**Published:** 2026-06-01 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.01626v1) | [PDF](https://arxiv.org/pdf/2606.01626v1.pdf)

<details>
<summary>Abstract</summary>

Planning with a learned latent world model is a promising route to control from raw pixels, but a strong world model alone is not enough. We show this experimentally: even with a perfect world model (operationalized by replacing the learned forward predictor with an idealized rollout of the true environment dynamics), a finite-budget sample-based planner still fails on some tasks, indicating that the bottleneck can lie in search rather than in world-model accuracy. Motivated by this gap, we prop...

</details>

---

### [TERRA: Task-Embedded Reasoning and Representation Architecture for Cross-Domain Applications](https://arxiv.org/abs/2606.01520v1)

**Authors:** Shayan Shokri

**Published:** 2026-06-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.01520v1) | [PDF](https://arxiv.org/pdf/2606.01520v1.pdf)

<details>
<summary>Abstract</summary>

A single action-conditioned latent predictive architecture can in principle be trained on the structured state of a driving scene, a robot workspace, or a financial order book. The ingredients for doing so within any one domain already exist and are individually validated: masked-latent prediction, action-conditioned latent world models, discrete action tokenization, and joint-embedding prediction on voxelized state. What is not established, and what TERRA addresses, is the transfer question: wh...

</details>

---

### [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](https://arxiv.org/abs/2606.01444v1)

**Authors:** Fiona Y. Wang, Markus J. Buehler

**Published:** 2026-05-31 | **Categories:** cs.AI, cond-mat.mtrl-sci, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.01444v1) | [PDF](https://arxiv.org/pdf/2606.01444v1.pdf)

<details>
<summary>Abstract</summary>

Scientific discovery is not only answer generation but revision of the representational regime in which evidence, artifacts, operations, and verifiers are typed. We develop a category-theoretic account of agentic discovery for materials science. In a fixed regime b with schema category S_b, the system state is a copresheaf I_t: S_b -> Set, and provenance is the category of elements \int_{S_b} I_t. Fixed-regime operation is an update on such states, endofunctorial only when provenance-preserving ...

</details>

---

### [$τ_0$-WM: A Unified Video-Action World Model for Robotic Manipulation](https://arxiv.org/abs/2606.01027v1)

**Authors:** Pengfei Zhou, Shengcong Chen, Di Chen, Jiaxu Wang, Rongjun Jin et al. (20 authors)

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01027v1) | [PDF](https://arxiv.org/pdf/2606.01027v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation requires models that generate executable actions while anticipating and evaluating their future consequences before physical execution. We present $τ_0$-World Model ($τ_0$-WM), a unified video-action world model that integrates policy learning, video prediction, and action evaluation within a single future-predictive framework. Built on a shared video diffusion backbone, $τ_0$-WM provides two complementary interfaces. First, a video action model jointly predicts future visua...

</details>

---
