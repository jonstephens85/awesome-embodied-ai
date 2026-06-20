# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-06-20 22:57 UTC

**Papers found:** 6

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Holo-World: Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083v1)

**Authors:** Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen et al. (9 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20083v1) | [PDF](https://arxiv.org/pdf/2606.20083v1.pdf) | [Project Page](is) | [GitHub](https://github.com/XiangchenYin/Holo-World})

<details>
<summary>Abstract</summary>

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instructio...

</details>

---

## Other Recent Papers

### [Current World Models Lack a Persistent State Core](https://arxiv.org/abs/2606.20545v1)

**Authors:** Jinpeng Lu, Dexu Zhu, Haoyuan Shi, Linghan Cai, Guo Tang et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20545v1) | [PDF](https://arxiv.org/pdf/2606.20545v1.pdf)

<details>
<summary>Abstract</summary>

World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking. This requirement is a blind spot of existing benchmarks, which...

</details>

---

### [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104v1)

**Authors:** Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf

**Published:** 2026-06-18 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20104v1) | [PDF](https://arxiv.org/pdf/2606.20104v1.pdf)

<details>
<summary>Abstract</summary>

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce ...

</details>

---

### [Reward as An Agent for Embodied World Models](https://arxiv.org/abs/2606.19990v1)

**Authors:** Pu Li, Zhigang Lin, Qiang Wu, Yongxuan Lv, Fei Wang et al. (6 authors)

**Published:** 2026-06-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.19990v1) | [PDF](https://arxiv.org/pdf/2606.19990v1.pdf)

<details>
<summary>Abstract</summary>

While RL has become a promising tool for refining world models, existing methods largely rely on conservative rollouts near the training distribution, limiting exploration, behavioral diversity, and richer dynamic discovery. In this work, we challenge this conservative paradigm. We argue that the core limitation is not exploration itself, but the lack of reliable verification strategies to support broader exploration. Without reliable verification, expanded exploration becomes highly susceptible...

</details>

---

### [SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928v1)

**Authors:** Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu et al. (9 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19928v1) | [PDF](https://arxiv.org/pdf/2606.19928v1.pdf)

<details>
<summary>Abstract</summary>

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both t...

</details>

---

### [SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics](https://arxiv.org/abs/2606.19889v1)

**Authors:** Wentao Pan, Wuyang Li, Shengyuan Liu, Xinyu Liu, Hengyu Liu et al. (6 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.19889v1) | [PDF](https://arxiv.org/pdf/2606.19889v1.pdf)

<details>
<summary>Abstract</summary>

Scaling robot policy learning for autonomous surgery is challenging, as expert demonstrations are expensive and in vivo exploration poses substantial safety risks. Surgical world models address this by generating realistic, action-conditioned future frames from an initial observation, but existing methods exhibit two persistent failure modes: spatial interaction incoherence, where visible instrument contact fails to induce spatially consistent tissue deformation, and temporal fidelity collapse, ...

</details>

---
