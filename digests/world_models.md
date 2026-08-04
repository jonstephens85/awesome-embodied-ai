# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-04 17:47 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603v1)

**Authors:** Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan et al. (16 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.02603v1) | [PDF](https://arxiv.org/pdf/2608.02603v1.pdf) | [Project Page](https://WorldExam.github.io)

<details>
<summary>Abstract</summary>

Controllable video generation models are increasingly being developed as world models. Accordingly, evaluating them in this role extends beyond the apparent appearance of generated videos to the inherent reactivity of the worlds they depict: the ability to infer from the scene state how the world should react and to generate plausible consequences not explicitly described in the input. Yet existing benchmarks mainly assess visual quality or explicit instruction fulfillment by checking whether re...

</details>

---

## Other Recent Papers

### [DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation](https://arxiv.org/abs/2608.02428v1)

**Authors:** Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li et al. (6 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.02428v1) | [PDF](https://arxiv.org/pdf/2608.02428v1.pdf)

<details>
<summary>Abstract</summary>

Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this ...

</details>

---

### [Faster-WAM: Do World Action Models Need Deep Action Modules?](https://arxiv.org/abs/2608.02365v1)

**Authors:** Liheng Ma, Rui Heng Yang, Zhanguang Zhang, Mateo Clemente, Ziwen Hu et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.AI, cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02365v1) | [PDF](https://arxiv.org/pdf/2608.02365v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple robot action prediction with video world models. Existing WAMs with shared-backbone and Mixture-of-Transformers designs generally tie the depth of the action module to that of the video backbone, resulting in substantial computational overhead and high inference latency. To address this limitation, we introduce Dock of Transformer (DoT), a video-centric design principle that treats a pretrained video Transformer as a representation hub and connects lightweight o...

</details>

---

### [PhyCheck: Fine-Grained Evidence-Grounded Dataset for Physical Law Understanding in Video-LLMs](https://arxiv.org/abs/2608.02150v1)

**Authors:** Zhongjie Ba, Shengwang Xu, Peng Cheng, Jinyang Zou, Ting Yu et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.02150v1) | [PDF](https://arxiv.org/pdf/2608.02150v1.pdf)

<details>
<summary>Abstract</summary>

Embodied intelligence and world models require video understanding systems to go beyond recognizing objects and actions and develop an understanding of physical regularities. However, despite their strong performance on general video understanding tasks, current video-language models still struggle to reliably determine whether an observed event conforms to specific physical laws. Existing benchmarks primarily assess the physical quality of generated videos, providing limited support for systema...

</details>

---

### [ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching](https://arxiv.org/abs/2608.01926v1)

**Authors:** Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.01926v1) | [PDF](https://arxiv.org/pdf/2608.01926v1.pdf)

<details>
<summary>Abstract</summary>

JEPA-style visual world models offer an effective paradigm for visual goal planning by predicting future latent representations. Existing methods typically learn local transition consistency through next-step representation prediction. However, in long-horizon tasks, accurate local prediction alone need not ensure sustained progress toward the goal. First, multi-step rollouts can remain locally plausible while drifting away from goal-relevant trajectories. Second, locally similar future states c...

</details>

---

### [WorldDynCache: Risk-Controlled Latent Dynamics Approximation for Diffusion World Model](https://arxiv.org/abs/2608.01845v1)

**Authors:** Leyang Chen, Junyi Wu, Shaoqiu Zhang, Yulun Zhang

**Published:** 2026-08-03 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.01845v1) | [PDF](https://arxiv.org/pdf/2608.01845v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion world models generate high-quality futures, but re- peated transformer evaluations make inference prohibitively slow. Existing caches reuse intermediate features, selectively update tokens, or reuse and extrapolate denoising outputs ac- cording to local drift or short native-space histories. These criteria can miss both approximation-induced latent transition defects that accumulate across skipped steps and phase- or condition-dependent changes in the direction of latent evo- lution. W...

</details>

---

### [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397v1)

**Authors:** Ruiteng Zhao, Zhengshen Zhang, Yue Su, Wenshuo Wang, Jiahui Li et al. (9 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.01397v1) | [PDF](https://arxiv.org/pdf/2608.01397v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple action generation with prediction of future states. Their effectiveness depends on whether future dynamics are modeled in a space that is both aligned with action generation and sufficiently geometry-aware to capture where and how actions change the scene. Existing WAMs typically satisfy only part of this requirement, relying on either perceptually heavy observation-space targets or auxiliary latent spaces that are not jointly structured for action relevance and...

</details>

---

### [DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation](https://arxiv.org/abs/2608.01381v1)

**Authors:** Zheng Yang, Wenjie Zhang, Xiangyu Chen, Wenxuan Song, Xianpeng Wang et al. (10 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01381v1) | [PDF](https://arxiv.org/pdf/2608.01381v1.pdf)

<details>
<summary>Abstract</summary>

Mobile manipulation requires a robot to coordinate base and arm motion under continuously changing viewpoints and contact conditions, within an action space far larger than that of fixed-base manipulation. Existing Vision-Language-Action (VLA) policies are limited in two respects. (i)They map observations directly to whole-body action chunks, searching this large action space without an explicit task-space motion plan, which makes coordinated base--arm prediction imprecise. (ii)They execute the ...

</details>

---

### [EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation](https://arxiv.org/abs/2608.01221v1)

**Authors:** Jinsong Lin, Zikang Pan, Wanhao Liu, Chi Kit Ng, Liangjing Shao et al. (13 authors)

**Published:** 2026-08-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.01221v1) | [PDF](https://arxiv.org/pdf/2608.01221v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous endoscopic navigation can reduce clinicians' operational burden, yet robust control remains challenging due to tissue deformation, transient occlusions, and rapidly changing viewpoints. Existing learning-based policies typically predict actions from current observations without explicitly modeling future dynamics, limiting their robustness and reliability in safety-critical settings. World Action Models (WAMs) offer a promising alternative by coupling predictive visual dynamics with a...

</details>

---

### [Climate-Dyna Deep Hedging for XVAs: Model-Based Reinforcement Learning, Residual Climate HVA, and Hedge-Instrument Discovery](https://arxiv.org/abs/2608.01208v1)

**Authors:** Xiaozhen Wang, Francois Buet-Golfouse

**Published:** 2026-08-02 | **Categories:** q-fin.MF, cs.LG, q-fin.RM

**Links:** [arXiv](https://arxiv.org/abs/2608.01208v1) | [PDF](https://arxiv.org/pdf/2608.01208v1.pdf)

<details>
<summary>Abstract</summary>

For a trading desk, residual climate hedging valuation adjustment (HVA) is the climate cost left after its inherited hedge and any admissible overlay have been taken into account; it therefore cannot be inferred from a stand-alone stress loss. We obtain this residual by comparing paired climate-on and baseline worlds and reoptimizing the overlay for each hedge universe, which also turns hedge-instrument discovery into a valuation problem: an instrument is useful to the extent that it lowers the ...

</details>

---

### [MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v1)

**Authors:** Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang et al. (6 authors)

**Published:** 2026-08-02 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.01127v1) | [PDF](https://arxiv.org/pdf/2608.01127v1.pdf)

<details>
<summary>Abstract</summary>

Video world models predict future observations conditioned on historical observations and control signals, enabling long-horizon generation through autoregressive state transitions. Unlike conventional video generation models that primarily capture visual appearance and motion, video world models learn the underlying dynamics governing environment evolution under agent actions, providing a foundation for embodied AI and interactive simulation. Recent progress has largely relied on adapting pretr...

</details>

---

### [FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels for Crowded and Chaotic Global South Urban Worlds](https://arxiv.org/abs/2608.01049v1)

**Authors:** Kapil Wanaskar, Gaytri Jena, Aman Chadha, Vinija Jain, Vasu Sharma et al. (6 authors)

**Published:** 2026-08-02 | **Categories:** cs.AI, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.01049v1) | [PDF](https://arxiv.org/pdf/2608.01049v1.pdf)

<details>
<summary>Abstract</summary>

World models have attracted significant attention for their ability to capture and predict the structure and dynamics of the physical world. In this emerging landscape, Joint Embedding Predictive Architectures (JEPA) offer a particularly compelling direction. We study a largely unexplored regime: populous, crowded, and chaotic Global South urban environments, which we call DENSEWORLD. Unlike the lower-density, lane-structured settings that dominate existing evaluations, these scenes exhibit soft...

</details>

---
