# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-17 17:10 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278v1)

**Authors:** Zezhong Qian, Xiaowei Chi, Chak-Wing Mak, Tianze Zhou, Ruibin Yuan et al. (12 authors)

**Published:** 2026-07-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.15278v1) | [PDF](https://arxiv.org/pdf/2607.15278v1.pdf) | [Project Page](https://hierarchical-diffusion-reasoning.github.io/)

<details>
<summary>Abstract</summary>

Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework ...

</details>

---

### [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065v1)

**Authors:** Susie Lu, Haonan Chen, Weirui Ye, Yilun Du

**Published:** 2026-07-16 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.15065v1) | [PDF](https://arxiv.org/pdf/2607.15065v1.pdf) | [Project Page](https://susie-lu.github.io/driftworld/)

<details>
<summary>Abstract</summary>

Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. We introduce DriftWorld, an action-conditioned world model based on drifting generative models. Rather than denoising iteratively at inference, DriftWorld learns an action-con...

</details>

---

### [GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch](https://arxiv.org/abs/2607.13960v2)

**Authors:**  GigaWorld Team, Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni et al. (29 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13960v2) | [PDF](https://arxiv.org/pdf/2607.13960v2.pdf) | [Project Page](https://open-gigaai.github.io/giga-world-policy/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) improve robot policy learning by jointly modeling actions and future visual observations, using future scene evolution as dense supervision for physically grounded action generation. However, a common design in existing WAMs is to explicitly generate future videos at inference time, incurring substantial computational overhead and hindering real-time closed-loop deployment. GigaWorld-Policy addresses this issue with an action-centered formulation, where future visual d...

</details>

---

### [Towards Spatial Supersensing in the Wild](https://arxiv.org/abs/2607.13681v1)

**Authors:** Tianjun Gu, Tianyu Xin, Kuan Zhang, Bowen Yang, Kok-Chung Chua et al. (15 authors)

**Published:** 2026-07-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13681v1) | [PDF](https://arxiv.org/pdf/2607.13681v1.pdf) | [Project Page](https://vsi-super-wild.github.io/)

<details>
<summary>Abstract</summary>

Humans can efficiently parse continuous sensory streams, from hours to years, scaffolding an internal world model that grounds spatial reasoning and prediction. To mimic this capacity, spatial supersensing challenges multimodal models to move beyond linguistic understanding toward true world modeling. However, their benchmark relies on synthetic long videos, formed by concatenating random short clips, and is mostly limited to household scenes, leaving real-world continuity and diversity underexp...

</details>

---

### [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/abs/2607.14169v1)

**Authors:** Javier Aguilar Martín

**Published:** 2026-07-15 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.14169v1) | [PDF](https://arxiv.org/pdf/2607.14169v1.pdf) | [GitHub](https://github.com/JaviMaligno/code-world-models)

<details>
<summary>Abstract</summary>

Large language models can synthesize a game's rules as executable code - a Code World Model (CWM) - which a classical planner then searches over. Such models are typically accepted when they reach high transition accuracy on sampled trajectories. We argue this is the wrong notion of adequacy for planning. We show four things. (1) An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be $\geq 98\%$ state-accurate on the planner's own search distribution, yet lose systema...

</details>

---

## Other Recent Papers

### [Concept-Guided Spatial Regularization for World Models in Atari Pong](https://arxiv.org/abs/2607.15142v1)

**Authors:** Yukuan Lu, Zaishuo Xia, Weyl Lu, Yubei Chen

**Published:** 2026-07-16 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.15142v1) | [PDF](https://arxiv.org/pdf/2607.15142v1.pdf)

<details>
<summary>Abstract</summary>

World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation. We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and evaluate them with a closed-loop rollout diagnostic: a policy trained separately f...

</details>

---

### [From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076v1)

**Authors:** Zhen Li, Zian Meng, Shuwei Shi, Mingliang Zhai, Jiaming Tan et al. (7 authors)

**Published:** 2026-07-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.14076v1) | [PDF](https://arxiv.org/pdf/2607.14076v1.pdf)

<details>
<summary>Abstract</summary>

Building interactive worlds that respond coherently to player actions has long been a shared goal of computer graphics, games, and artificial intelligence. Recent video generative models provide a data-driven route toward this goal by predicting future observations conditioned on user actions, and are increasingly regarded as potential next-generation game engines. Realizing a genuinely interactive game world, however, requires interaction outcomes that follow rules over evolving game conditions...

</details>

---

### [M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming](https://arxiv.org/abs/2607.14005v1)

**Authors:** Ke Cheng, Hanqiao Ye, Lei Shi, Yahui Liu, Yunhan Shen et al. (11 authors)

**Published:** 2026-07-15 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14005v1) | [PDF](https://arxiv.org/pdf/2607.14005v1.pdf)

<details>
<summary>Abstract</summary>

Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We present M$^\text{4}$World, a Multi-view and Multimodal generative driving world model that synthesizes future surround-view video streams and synchronized LiDAR scans while supporting interactive object Manipulation and stable Minute-long streaming. Fine-grained object manipulation is realized thro...

</details>

---

### [RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination](https://arxiv.org/abs/2607.14187v1)

**Authors:** Haotian Liang, Mingkang Chen, Yufei Huang, Yuchun Guo, Xiaomeng Zhu et al. (30 authors)

**Published:** 2026-07-15 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.14187v1) | [PDF](https://arxiv.org/pdf/2607.14187v1.pdf)

<details>
<summary>Abstract</summary>

Embodied cognition requires agents to connect high-level task reasoning with the physical states to be achieved. We introduce Hy-Embodied-RxBrain, an embodied cognition foundation model with joint language-visual reasoning and imagination. Unlike vision-language models that emphasize scene understanding and textual decision making, or generative world models that mainly predict future visual states, RxBrain represents embodied plans in a single planning sequence where language and visual imagina...

</details>

---

### [Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning](https://arxiv.org/abs/2607.14183v1)

**Authors:** Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen et al. (32 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.14183v1) | [PDF](https://arxiv.org/pdf/2607.14183v1.pdf)

<details>
<summary>Abstract</summary>

Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in na...

</details>

---

### [RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences](https://arxiv.org/abs/2607.14180v1)

**Authors:** Logan Mondal Bhamidipaty, Mykel Kochenderfer, Subramanian Ramamoorthy

**Published:** 2026-07-15 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.14180v1) | [PDF](https://arxiv.org/pdf/2607.14180v1.pdf)

<details>
<summary>Abstract</summary>

World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset. However, they are vulnerable to model exploitation where data coverage is thin. Prior work addresses this either by collecting more expert demonstrations, which is often expensive, unsafe, or unavailable, or by conservative algorithms that avoid uncertain regions, which limits generalization. We propose instead to repair exploitation directly using huma...

</details>

---

### [From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring](https://arxiv.org/abs/2607.13651v1)

**Authors:** Mohanad Albughdadi

**Published:** 2026-07-15 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13651v1) | [PDF](https://arxiv.org/pdf/2607.13651v1.pdf)

<details>
<summary>Abstract</summary>

The bottleneck of Earth Observation processing chains is not the arrival of new imagery but whether the surface is actually visible when the image arrives. We study this as an observability forecasting problem on EarthNet2021. Given recent multispectral imagery and exogenous weather drivers, the goal is to predict whether the next acquisition will be usable and, if not, when a usable view is likely to return. To do this, we adapt LeWorldModel, a joint-embedding predictive architecture world mode...

</details>

---

### [The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models](https://arxiv.org/abs/2607.13612v1)

**Authors:** Fabio Arnez, Alexandra Gomez-Villa

**Published:** 2026-07-15 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.13612v1) | [PDF](https://arxiv.org/pdf/2607.13612v1.pdf)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) are the dominant design for latent world models, yet they are usually justified by empirical performance rather than a normative principle. We show that the choice of anti-collapse regulariser determines whether a JEPA's training objective, a prediction loss plus a weighted embedding regulariser, is a valid Active Inference (AIF) variational free energy. We organise four non-contrastive regularisers (VICReg, LogDet, PairDist, and SIGReg) into an e...

</details>

---

### [Grounded world models in biological organisms and future embodied AI](https://arxiv.org/abs/2607.13560v1)

**Authors:** Giovanni Pezzulo, Davide Nuzzi, Marco D'Alessandro, Riccardo Proietti, Roberto Bottini et al. (6 authors)

**Published:** 2026-07-15 | **Categories:** q-bio.NC, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.13560v1) | [PDF](https://arxiv.org/pdf/2607.13560v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in generative and embodied AI have been driven by large-scale predictive learning over multimodal data. However, the resulting systems remain largely based on passive training regimes where linguistic regularities create the scaffold onto which information from other modalities is attached. Conversely, neuroscience and cognitive science suggest that biological intelligence is organized in the opposite way, where grounded world models acquired through interaction with the environm...

</details>

---

### [Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation](https://arxiv.org/abs/2607.13410v1)

**Authors:** Zhidong Wang, Jingsong Liang, Zirui Li, Zhan Chen, Han Yu et al. (6 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13410v1) | [PDF](https://arxiv.org/pdf/2607.13410v1.pdf)

<details>
<summary>Abstract</summary>

World model (WM)-based reinforcement learning enables sample-efficient end-to-end autonomous driving learning by imagining long-horizon trajectories in latent space. However, most driving WMs operate on bird's-eye-view (BEV) representations that are inherently egocentric: the transition between consecutive frames entangles the ego vehicle's own motion with scene dynamics. As a result, the WM devotes significant capacity to recovering ego-motion from warped observations, at the cost of scene mode...

</details>

---
