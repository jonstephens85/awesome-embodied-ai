# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-01 16:58 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](https://arxiv.org/abs/2607.28625v1)

**Authors:** Yukang Cao, Haozhe Xie, Beichen Wen, Runmao Yao, Yinghao Liu et al. (16 authors)

**Published:** 2026-07-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.28625v1) | [PDF](https://arxiv.org/pdf/2607.28625v1.pdf) | [Project Page](https://ace-data-engine.github.io/ACE-Data-0/)

<details>
<summary>Abstract</summary>

Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environme...

</details>

---

### [PhiZero: A World Model Built Around Physical Language](https://arxiv.org/abs/2607.28624v1)

**Authors:** Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan et al. (7 authors)

**Published:** 2026-07-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.28624v1) | [PDF](https://arxiv.org/pdf/2607.28624v1.pdf) | [Project Page](https://phi-zero.github.io/)

<details>
<summary>Abstract</summary>

We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. Motivated by humans' ability to abstract predictive structure from visual experience and organize it in natural language for explicit reasoning, we learn physical language from in-the...

</details>

---

### [Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3](https://arxiv.org/abs/2607.28287v1)

**Authors:** Jens Lehmann, Andrei Aioanei, Sahar Vahdati

**Published:** 2026-07-30 | **Categories:** cs.AI, cs.CV, cs.SC

**Links:** [arXiv](https://arxiv.org/abs/2607.28287v1) | [PDF](https://arxiv.org/pdf/2607.28287v1.pdf) | [GitHub](https://github.com/NIMI-research/Tycho)

<details>
<summary>Abstract</summary>

ARC-AGI-3 turns abstraction into an interactive problem of skill acquisition. A player must infer an unfamiliar game's rules, hidden state, and goal while maintaining action efficiency because every move counts. We formalize these environments as parameterized rendered deterministic Moore machines and introduce Tycho, a coding-agent system that constructs and uses game-specific models during interaction. Tycho separates actionable observations from intermediate animation, level-completion, and g...

</details>

---

### [ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](https://arxiv.org/abs/2607.27924v1)

**Authors:** Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang et al. (8 authors)

**Published:** 2026-07-30 | **Categories:** cs.LG, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27924v1) | [PDF](https://arxiv.org/pdf/2607.27924v1.pdf) | [Project Page](https://dstate.github.io/odeworld_website/}{Project)

<details>
<summary>Abstract</summary>

In the physical world we inhabit, space and time are fundamentally continuous. However, existing machine learning paradigms for world modeling are largely confined to discrete-time prediction, thereby exhibiting significant inefficiency in capturing the dynamics of physical world. We introduce Physical-Time Flow (\textbf{PT-Flow}), a novel approach that learns a continuous latent velocity field operating in physical time. Crucially, the underlying dynamics of sequential data are parameterized by...

</details>

---

### [World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models](https://arxiv.org/abs/2607.27599v1)

**Authors:** Xiangcheng Zhang, Yilun Du

**Published:** 2026-07-30 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27599v1) | [PDF](https://arxiv.org/pdf/2607.27599v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Building generalizable agents for diverse applications remains a fundamental challenge. While imitation learning-based policies succeed in specific training environments, they often fail to generalize to novel scenes and tasks. In this work, we propose World Action Planner, a robot planning system that leverages the reasoning capabilities of Vision-Language Models (VLMs) and the physical grounding of a multi-task pose-image conditioned world model. Our system enables an agent to propose initial ...

</details>

---

## Other Recent Papers

### [AuricularWorld: Hierarchical Action-Guided World Modeling for Fine-Grained Auricular Structure Segmentation from CT Scans](https://arxiv.org/abs/2607.28487v1)

**Authors:** Jingwen Yang, Senmao Wang, Luoyao Kang, Runmeng Cui, Keying Zhang et al. (9 authors)

**Published:** 2026-07-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.28487v1) | [PDF](https://arxiv.org/pdf/2607.28487v1.pdf)

<details>
<summary>Abstract</summary>

Fine-grained segmentation of auricular structures in CT is challenging because the ear occupies a small image region, cartilage boundaries are highly irregular, and interfaces between cartilage and surrounding soft tissues are often ambiguous. Clinical annotations may also include both composite structures containing cartilage and adjacent skin and their corresponding cartilage-only regions, producing nested and overlapping labels. We propose a world-model-based segmentation framework that enabl...

</details>

---

### [QQWorld: Quantile-Quantile Matching for World Model Regularization](https://arxiv.org/abs/2607.28415v1)

**Authors:** Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu

**Published:** 2026-07-30 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.28415v1) | [PDF](https://arxiv.org/pdf/2607.28415v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models enable efficient planning by predicting future states in a compact representation space, but their performance depends critically on the quality of the learned latent distribution. LeWorldModel (LeWM) regularizes its latents toward an isotropic Gaussian using the Epps-Pulley (EP) objective. We show that the corrective gradients of EP rapidly vanish for isolated tail samples, leaving heavy-tailed deviations insufficiently controlled. To address this limitation, we propose QQWo...

</details>

---

### [ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow](https://arxiv.org/abs/2607.28362v1)

**Authors:** Jin Cao, Zian Meng, Kaipeng Zhang

**Published:** 2026-07-30 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.28362v1) | [PDF](https://arxiv.org/pdf/2607.28362v1.pdf)

<details>
<summary>Abstract</summary>

We present ShadowDancer, a novel approach to any-action, frame-level control of interactive video world models. The obstacle is representational: existing interfaces either encode an action loosely, leaving how it unfolds for the model to improvise, or encode it exactly through structured signals that serve one family and are hard to acquire, so precise control across diverse dynamics remains impractical. Demonstration videos are the natural remedy, specifying any dynamics frame by frame; yet a ...

</details>

---

### [Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation](https://arxiv.org/abs/2607.28226v1)

**Authors:** Fazhong Liu, Zhuoyan Chen, Haozhen Tan, Yan Meng, Guoxing Chen et al. (6 authors)

**Published:** 2026-07-30 | **Categories:** cs.CR, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.28226v1) | [PDF](https://arxiv.org/pdf/2607.28226v1.pdf)

<details>
<summary>Abstract</summary>

World models give embodied AI a predictive core: they compress observations into states, simulate action-conditioned futures, and enable planning beyond reactive control. This predictive layer, however, opens a new security boundary-compromise can propagate from data, sensors, prompts, or feedback into physical action. Rather than treating world models as an isolated component, this survey traces threats across their entire lifecycle-from data construction and representation learning, through st...

</details>

---

### [Learning to Understand Body Language from Flight through Robust 3D Avatar Placing](https://arxiv.org/abs/2607.27865v1)

**Authors:** Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu

**Published:** 2026-07-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.27865v1) | [PDF](https://arxiv.org/pdf/2607.27865v1.pdf)

<details>
<summary>Abstract</summary>

Perceiving human motion and intent at long range is a prerequisite for socially intelligent aerial robots, yet the data to learn it barely exists. We introduce Drones2BodyLanguage, a dataset grounding human motion in real UAV footage: avatars manifesting ten communicative intents are placed into unmodified 4K drone scenes with metrically correct position, scale and orientation, maintained over hundreds of frames of camera motion. Enabling it is a lightweight geometric world model of the local sc...

</details>

---
