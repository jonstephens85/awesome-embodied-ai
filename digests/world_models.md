# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-12 18:06 UTC

**Papers found:** 19

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672v1)

**Authors:** Arnav Kumar Jain, Yilin Wu, Jesse Farebrother, Gokul Swamy, Andrea Bajcsy

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.13672v1) | [PDF](https://arxiv.org/pdf/2606.13672v1.pdf) | [Project Page](https://arnavkj1995.github.io/WEAVER/)

<details>
<summary>Abstract</summary>

The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction. To unlock these downstream capabilities, a WM needs to jointly satisfy three desiderata: $\textit{(i)}$ fidelity (i.e., producing simulated trajectories that correlate with reality), $\textit{(ii)}$ consistency (i.e., producing simulated trajectories that are coherent over long horizons), an...

</details>

---

### [NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](https://arxiv.org/abs/2606.13494v1)

**Authors:** Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu et al. (9 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.13494v1) | [PDF](https://arxiv.org/pdf/2606.13494v1.pdf) | [Project Page](https://dachii-azm.github.io/navwam/)

<details>
<summary>Abstract</summary>

Goal-conditioned visual navigation requires a robot to act under partial observability by anticipating how its motion will change the future egocentric view and whether that change brings it closer to the goal. Navigation world models provide such visual foresight, but they remain prediction modules that require an external planner to convert predicted futures into closed-loop control. We propose Navigation World Action Model (NavWAM), a diffusion-transformer policy that turns navigation world-m...

</details>

---

### [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/abs/2606.13092v1)

**Authors:** Hongbo Wang

**Published:** 2026-06-11 | **Categories:** cs.LG, cs.RO, math.DS

**Links:** [arXiv](https://arxiv.org/abs/2606.13092v1) | [PDF](https://arxiv.org/pdf/2606.13092v1.pdf) | [GitHub](https://github.com/TimothyWang418/se3-ejepa)

<details>
<summary>Abstract</summary>

Scale buys interpolation; structure buys a certified horizon. A world model's average error says nothing about whether a particular prediction can be trusted, or for how long. For equivariant latent world models we give a computable, multi-step certificate of the predictable horizon: $T$-step rollout error is provably constant over each symmetry orbit (Theorem A) and stratified channel-by-channel by the predictor's Lyapunov spectrum, $T_j(ε)\sim\log(1/ε)/λ_j$. The horizon is two-sided -- a match...

</details>

---

### [Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics](https://arxiv.org/abs/2606.12828v1)

**Authors:** Rasul Khanbayov, Hasan Kurban

**Published:** 2026-06-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12828v1) | [PDF](https://arxiv.org/pdf/2606.12828v1.pdf) | [GitHub](https://github.com/KurbanIntelligenceLab/ai-phase-transitions)

<details>
<summary>Abstract</summary>

Do research topics in artificial intelligence grow gradually, or do they advance through abrupt, detectable jumps? Analyzing 80,814 accepted main-track papers from five premier AI conferences (ACL, CVPR, ICLR, ICML, NeurIPS) spanning 2017 to 2025, we show major AI topics advance through topical phase transitions: remaining marginal for years, then surging across venues within one to three years. Large language models became the dominant cross-venue topic by 2025, diffusion models rose with compa...

</details>

---

### [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.12780v1)

**Authors:** Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiaoguang Guo et al. (8 authors)

**Published:** 2026-06-11 | **Categories:** cs.LG, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.12780v1) | [PDF](https://arxiv.org/pdf/2606.12780v1.pdf) | [GitHub](https://github.com/antman9914/proplay)

<details>
<summary>Abstract</summary>

Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. Existing LLM-agent methods often rely on memory or planning modules, yet they rarely close the loop between them to continually refine an internal understanding of environment dynamics. We introduce ProPlay, a procedural world model ...

</details>

---

### [G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation](https://arxiv.org/abs/2606.12579v1)

**Authors:** Tanmay Bishnoi, Riddhiman Laha, Tobias Löw, Jose Alex Chandy, Luis F. C. Figueredo et al. (6 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12579v1) | [PDF](https://arxiv.org/pdf/2606.12579v1.pdf) | [GitHub](https://github.com/chart-research/g-mapp)

<details>
<summary>Abstract</summary>

Reactive motion generation in unstructured environments remains an open challenge in robotics. Due to the computational complexity of collision-free motion generation, existing methods either generate global trajectories for static scenarios, or employ models that make conservative assumptions about the environment. This paper identifies the primary bottleneck as the runtime performance demand of planning on high-fidelity environments, and the temporal integration between the perception and plan...

</details>

---

### [World Pilot: Steering Vision-Language-Action Models with World-Action Priors](https://arxiv.org/abs/2606.12403v1)

**Authors:** Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li et al. (7 authors)

**Published:** 2026-06-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12403v1) | [PDF](https://arxiv.org/pdf/2606.12403v1.pdf) | [Project Page](https://world-pilot.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models inherit semantic grounding from large-scale pretraining and perform competently across in-distribution manipulation tasks. This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture. We present World Pilot, a VLA framework that augments the policy with priors from a World-Action Model (WAM), routed into the decision chain through two complementary pathw...

</details>

---

## Other Recent Papers

### [Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday Reasoning](https://arxiv.org/abs/2606.13607v1)

**Authors:** Zach Studdiford, Gary Lupyan

**Published:** 2026-06-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.13607v1) | [PDF](https://arxiv.org/pdf/2606.13607v1.pdf)

<details>
<summary>Abstract</summary>

When large language models (LLMs) fail to generalize or make haphazard errors in reasoning, it is often taken as evidence that LLMs are not truly reasoning, but rather performing a kind of pattern matching. The implication is that people's behavior does not exhibit the same types of failures because human reasoning uses principled and abstract world models. We evaluate human participants and 25 LLMs on their ability to engage in common-sense reasoning about a variety of everyday situations and o...

</details>

---

### [VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460v1)

**Authors:** Ruiqi Xian, Yuehan Xian, Jing Liang, Xuewei Qi, Dinesh Manocha

**Published:** 2026-06-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.13460v1) | [PDF](https://arxiv.org/pdf/2606.13460v1.pdf)

<details>
<summary>Abstract</summary>

Semantic 3D occupancy provides a voxelized world state for autonomous driving and robot decision making, but object and rare-class errors can affect free-space interpretation, collision checking, and temporal state propagation. We show that a common VLM strategy, aligning 3D voxel or object features with crop-caption embeddings, improves text-space similarity without reliably improving closed-set occupancy mIoU. Motivated by this mismatch, we propose VISA, a training-time semantic auditing appro...

</details>

---

### [MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376v1)

**Authors:** Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang et al. (7 authors)

**Published:** 2026-06-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.13376v1) | [PDF](https://arxiv.org/pdf/2606.13376v1.pdf)

<details>
<summary>Abstract</summary>

We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations. MoVerse addresses this problem by separating world construction from observation rendering. It firs...

</details>

---

### [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](https://arxiv.org/abs/2606.13053v1)

**Authors:** Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.13053v1) | [PDF](https://arxiv.org/pdf/2606.13053v1.pdf)

<details>
<summary>Abstract</summary>

Pretrained-feature world models provide a useful substrate for robot imagination, but visual or latent prediction alone does not determine whether an imagined future satisfies task-relevant events. Long-horizon manipulation requires progress signals that are relational, predicate-level, and physically grounded: whether an object has moved, whether a drawer or contact state has changed, whether a placement predicate is satisfied, and whether a candidate future is reliable enough for execution. We...

</details>

---

### [Diffusion Transformer World-Action Model for AV Scene Prediction](https://arxiv.org/abs/2606.12987v1)

**Authors:** Ruslan Sharifullin, Benjamin Jiang, Kai Xi Chew

**Published:** 2026-06-11 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12987v1) | [PDF](https://arxiv.org/pdf/2606.12987v1.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models let an autonomous vehicle predict future camera scenes from its own planned controls, enabling planning and simulation without real-world rollouts, but at compact, trainable scale the futures are ambiguous and the field's standard distortion metrics actively mislead: they reward a blurry regression mean over a realistic prediction. We confront this with a compact latent world model that, given the present front-camera latent and a sequence of ego-actions, predicts...

</details>

---

### [EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models](https://arxiv.org/abs/2606.12979v1)

**Authors:** Vedant Pandya

**Published:** 2026-06-11 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.12979v1) | [PDF](https://arxiv.org/pdf/2606.12979v1.pdf)

<details>
<summary>Abstract</summary>

JEPA-family world models use a static predictor whose weights do not adapt when test-time dynamics diverge from training. We compare two mechanisms for incorporating accumulated experience into a JEPA predictor under distribution shift: operand-side injection, where a compressed experience representation is added as a residual to the predictor's hidden state (EI-JEPA), and operator-side modulation, where the same representation generates low-rank weight deltas via LoRA applied to the predictor's...

</details>

---

### [A Tutorial on World Models and Physical AI](https://arxiv.org/abs/2606.12783v1)

**Authors:** Il-Seok Oh

**Published:** 2026-06-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12783v1) | [PDF](https://arxiv.org/pdf/2606.12783v1.pdf)

<details>
<summary>Abstract</summary>

World modeling is emerging as a central principle for building intelligent systems capable of prediction, reasoning, and decision making. A central distinction can be drawn between explicit world models, which learn structured dynamics for rollout-based reasoning and planning, and implicit world models, which encode predictive structure within scalable learned representations. These complementary paradigms provide a foundation for physical AI in domains such as robotics and autonomous driving, e...

</details>

---

### [The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism](https://arxiv.org/abs/2606.12721v1)

**Authors:** Nikolos Gurney, Stacy Marsella

**Published:** 2026-06-10 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12721v1) | [PDF](https://arxiv.org/pdf/2606.12721v1.pdf)

<details>
<summary>Abstract</summary>

Inferring others' beliefs requires more than reading surface signals; it requires tracking who told them what, in what order, and how credibly. The Theory of Mind Utility (ToM-U) formalizes this epistemic state inference problem at the computational level of analysis, specifying what mentalizing computes and why without commitment to algorithmic or neural implementation. ToM-U achieves this by constructing Local Epistemic World Models (LEWMs) -- directed typed graphs that represent agents, state...

</details>

---

### [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688v1)

**Authors:** Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin, Rohan Sanda et al. (12 authors)

**Published:** 2026-06-10 | **Categories:** cs.LG, cs.AI, cs.DC

**Links:** [arXiv](https://arxiv.org/abs/2606.12688v1) | [PDF](https://arxiv.org/pdf/2606.12688v1.pdf)

<details>
<summary>Abstract</summary>

We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about mode...

</details>

---

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
