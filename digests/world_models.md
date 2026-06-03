# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-03 19:48 UTC

**Papers found:** 25

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning](https://arxiv.org/abs/2606.03603v1)

**Authors:** Yucheng Zhou, Wei Tao, Yiwen Guo, Jianbing Shen

**Published:** 2026-06-02 | **Categories:** cs.CV, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.03603v1) | [PDF](https://arxiv.org/pdf/2606.03603v1.pdf) | [GitHub](https://github.com/yczhou001/PF-OPSD)

<details>
<summary>Abstract</summary>

World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations. World models can generate concrete visual rollouts of possible futures, while MLLMs can reason abstractly over questions, goals, and rules. However, generated rollouts are stochastic and may be visually plausible but task-incorrect, making it necessary to determine when visual simulation is useful, whether a rollout is credible, and how it s...

</details>

---

### [Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800v1)

**Authors:**  Aditi, Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini et al. (291 authors)

**Published:** 2026-06-01 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.02800v1) | [PDF](https://arxiv.org/pdf/2606.02800v1.pdf) | [Project Page](is) | [GitHub](https://github.com/nvidia/cosmos}{github.com/nvidia/cosmos)

<details>
<summary>Abstract</summary>

We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers architecture. By supporting highly flexible input-output configurations, Cosmos 3 seamlessly unifies critical modalities for Physical AI -- effectively subsuming vision-language models, video generators, world simulators, and world-action models into a single framework. Our evaluation demonstrates that Cosm...

</details>

---

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

## Other Recent Papers

### [A Close Look At World Model Recovery In Supervised Fine-Tuned LLM Planners](https://arxiv.org/abs/2606.03685v1)

**Authors:** Patrick Emami, Nan Qiang, Peter Graf

**Published:** 2026-06-02 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.03685v1) | [PDF](https://arxiv.org/pdf/2606.03685v1.pdf)

<details>
<summary>Abstract</summary>

Supervised fine-tuning (SFT) improves end-to-end classical planning in large language models (LLMs), but do these models also learn to represent and reason about the planning problems they are solving? Due to the relative complexity of classical planning problems and the challenge that end-to-end plan generation poses for LLMs, it has been difficult to explore this question. In our work, we devise and perform a series of interpretability experiments that holistically interrogate world model reco...

</details>

---

### [A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature](https://arxiv.org/abs/2606.03609v1)

**Authors:** Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang

**Published:** 2026-06-02 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.03609v1) | [PDF](https://arxiv.org/pdf/2606.03609v1.pdf)

<details>
<summary>Abstract</summary>

Embodied agents that navigate cities rely on world models that predict how their surroundings will change as they move. But for navigation, what matters is not what the buildings look like; it is where the agent can go. Most world models nonetheless predict appearance, learning how a scene looks rather than the space an agent can move through. Those that do target geometry, such as bird's-eye-view occupancy grids, flatten the three-dimensional environment onto a ground plane, discarding the abov...

</details>

---

### [SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation](https://arxiv.org/abs/2606.03297v1)

**Authors:** Jeonguk Kang, Hanbyel Cho, Sanghyun Kang, Donghan Koo

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03297v1) | [PDF](https://arxiv.org/pdf/2606.03297v1.pdf)

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation requires stable whole-body control under varying object masses and pickup/placement heights. This becomes particularly challenging in sim-to-real transfer, where object-induced load variation and robot-side dynamics mismatch interact during physical contact. Existing history-based adapters often compress these factors into a single latent representation, which can weaken robustness under heavy-load manipulation. We propose \textbf{SplitAdapter: Load-Aware Humanoid Loco...

</details>

---

### [AirDreamer: Generalist Drone Navigation with World Models](https://arxiv.org/abs/2606.03252v1)

**Authors:** Zian Liu, Andong Yang, Chunkai Yang, Ruidong An, Chao Gao et al. (6 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.03252v1) | [PDF](https://arxiv.org/pdf/2606.03252v1.pdf)

<details>
<summary>Abstract</summary>

Navigating a drone in unseen and cluttered environments requires reliable generalization to unseen scene layouts and understanding of environmental structure relative to the robot's capabilities. Previous methods, which assume the same environment configuration, often rely heavily on human-designed perception pipelines and predefined rules to guide the robot toward the target. This process is environment-dependent and generalizes poorly across environments. Inspired by animal navigation behavior...

</details>

---

### [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188v1)

**Authors:** Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang et al. (7 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03188v1) | [PDF](https://arxiv.org/pdf/2606.03188v1.pdf)

<details>
<summary>Abstract</summary>

Recent World Action Models (WAMs) have demonstrated impressive capabilities in embodied decision-making. However, whether their effectiveness stems from explicit future imagination during inference or representation learning induced by predictive training remains an open question. Emerging evidence suggests the primary advantage lies in learning robust latent representations rather than generating future observations at test time. Nevertheless, existing WAMs mainly rely on RGB-based future predi...

</details>

---

### [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159v1)

**Authors:**  NVIDIA,  :, Aarti Basant, Amlan Kar, Despoina Paschalidou et al. (35 authors)

**Published:** 2026-06-02 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03159v1) | [PDF](https://arxiv.org/pdf/2606.03159v1.pdf)

<details>
<summary>Abstract</summary>

As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. While recent reconstruction-based neural simulators offer photorealism, they are fundamentally constrained by their initial captured data and ...

</details>

---

### [Exact equivariance, kept through training, buys zero-shot generalisation across the symmetry group](https://arxiv.org/abs/2606.03003v1)

**Authors:** Hongbo Wang

**Published:** 2026-06-02 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03003v1) | [PDF](https://arxiv.org/pdf/2606.03003v1.pdf)

<details>
<summary>Abstract</summary>

A latent world model built from an equivariant encoder $E$ and an equivariant predictor $f$ inherits a provable symmetry of its training loss: when the world's dynamics genuinely carries a group $G$ acting on latents by an orthogonal representation $ρ(g)$, the one-step prediction relMSE is exactly invariant across the whole group, so fitting the dynamics on a restricted slice of orientations mathematically determines it on the entire orbit (jǔ yī fǎn sān). We verify this end-to-end at laptop sca...

</details>

---

### [One Transit Is All You Need: Detecting Exoplanets Through Learned Stellar Behaviour with EXOVEIL](https://arxiv.org/abs/2606.02778v1)

**Authors:** Pratik Priyanshu

**Published:** 2026-06-01 | **Categories:** astro-ph.EP, astro-ph.IM, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.02778v1) | [PDF](https://arxiv.org/pdf/2606.02778v1.pdf)

<details>
<summary>Abstract</summary>

I present EXOVEIL, a transit detection system that learns what a star's brightness should look like and flags when reality disagrees. Unlike existing systems that require phase-folded input, EXOVEIL operates on raw flux time series and can detect planets that transit only once.A Transformer world model, trained on 16,499 Kepler light curves with transit-masked self-supervised learning, predicts expected stellar flux. A matched-filter detector with variance weighting extracts transit signals from...

</details>

---

### [MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data](https://arxiv.org/abs/2606.02753v1)

**Authors:** Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao et al. (9 authors)

**Published:** 2026-06-01 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.02753v1) | [PDF](https://arxiv.org/pdf/2606.02753v1.pdf)

<details>
<summary>Abstract</summary>

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physic...

</details>

---

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
