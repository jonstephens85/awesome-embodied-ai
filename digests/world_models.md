# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-16 22:48 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch](https://arxiv.org/abs/2607.13960v1)

**Authors:**  GigaWorld Team, Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni et al. (29 authors)

**Published:** 2026-07-15 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.13960v1) | [PDF](https://arxiv.org/pdf/2607.13960v1.pdf) | [Project Page](https://open-gigaai.github.io/giga-world-policy/)

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

### [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017v1)

**Authors:** Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang et al. (16 authors)

**Published:** 2026-07-14 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.13017v1) | [PDF](https://arxiv.org/pdf/2607.13017v1.pdf) | [Project Page](https://flow-wam.github.io)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy the former, and prior visual action representations overlook the temporal motion structure across fram...

</details>

---

## Other Recent Papers

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

### [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](https://arxiv.org/abs/2607.13172v1)

**Authors:** Ilias Kazantzidis, Timothy J. Norman, Yali Du, Christopher T. Freeman

**Published:** 2026-07-14 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.13172v1) | [PDF](https://arxiv.org/pdf/2607.13172v1.pdf)

<details>
<summary>Abstract</summary>

We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. We introduce DROPJ, a human-centred method for both safe training and deployment. We first learn a world model (a learned simulator) from a dataset of pr...

</details>

---

### [TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480v1)

**Authors:** Edward Y. Chang, Emily J. Chang

**Published:** 2026-07-14 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12480v1) | [PDF](https://arxiv.org/pdf/2607.12480v1.pdf)

<details>
<summary>Abstract</summary>

This paper defines TRACE (Typed Reasoning And Commitment Evidence): a typed, versioned schema for recording reasoning traces, a reference procedure for writing records against it, and one operating discipline, no durable state change without a record. The paper argues in three layers that reasoning is not in the language model: the autoregressive mechanism natively computes association; chain-of-thought and reinforcement learning inherit its limits; and the formal constructs of reasoning theory,...

</details>

---

### [From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery](https://arxiv.org/abs/2607.12474v2)

**Authors:** Ingmar Posner, Anson Lei, Bernhard Schölkopf

**Published:** 2026-07-14 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.12474v2) | [PDF](https://arxiv.org/pdf/2607.12474v2.pdf)

<details>
<summary>Abstract</summary>

Recent advances in foundation models have transformed AI for Science, enabling remarkably accurate predictive performance across domains ranging from protein folding to weather forecasting. Yet prediction alone does not constitute scientific discovery. Scientific understanding depends on uncovering the reusable explanatory mechanisms that generate observations, whereas contemporary machine learning remains fundamentally organised around predictive mappings rather than explanatory structure. In t...

</details>

---

### [The GEST-Engine: From Event Graphs to Synthetic Video. A Full Technical Report](https://arxiv.org/abs/2607.12231v1)

**Authors:** Nicolae Cudlenco, Mihai Masala, Marius Leordeanu

**Published:** 2026-07-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.12231v1) | [PDF](https://arxiv.org/pdf/2607.12231v1.pdf)

<details>
<summary>Abstract</summary>

We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video. At its core is an explicit world model: rather than encoding state as a learned latent, the engine maintains a complete, inspectable representation of the world (which actors exist, where they are, what they are doing, which objects they hold, and how events relate in time and space), expressed as a formal Graph of Events in Space and Time (GEST) and realized deterministically...

</details>

---
