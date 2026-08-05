# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-05 22:48 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Quo Vadis, World Modeling?](https://arxiv.org/abs/2608.02713v1)

**Authors:** Yu Yang, Xuemeng Yang, Licheng Wen, Lingdong Kong, Xiaobin Hu et al. (20 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02713v1) | [PDF](https://arxiv.org/pdf/2608.02713v1.pdf) | [Project Page](https://worldbench.github.io/awesome-agentic-world-model) | [GitHub](https://github.com/worldbench/awesome-agentic-world-model)

<details>
<summary>Abstract</summary>

Continually improving agents require dynamic interaction feedback beyond static supervision, yet direct real-environment interaction is costly, slow, unsafe, and hard to parallelize. World modeling offers a natural intermediate proxy that allows agents to query lower-cost, more controllable feedback before committing to real actions. Classical world models instantiate this proxy primarily through future physical-state prediction, a formulation useful yet narrow for agents that require actionable...

</details>

---

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

### [Enactive Artificial Intelligence: A Decision-Centric Architecture for Complex Systems](https://arxiv.org/abs/2608.03413v1)

**Authors:** Zuojun Max Shen, Yuan Qu, Pujun Zhang, Anbang Liu, Yunhao Liang

**Published:** 2026-08-04 | **Categories:** cs.AI, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2608.03413v1) | [PDF](https://arxiv.org/pdf/2608.03413v1.pdf)

<details>
<summary>Abstract</summary>

As artificial intelligence (AI) continues to evolve and mature, recent AI practices have moved beyond large language models (LLMs) and text or image generation tasks, increasingly integrating tools, agents, and harnesses to solve real business and industrial problems. However, the power of AI is not verified under these real-world complex systems for various reasons, considering reliability, feasibility, resilience, and responsibility requirements in real commercial and industrial operations. Th...

</details>

---

### [UniNav: A Unified World-Action Diffusion Model for Visual Navigation](https://arxiv.org/abs/2608.03244v1)

**Authors:** Changqing Zhou, Yueru Luo, Zeyu Jiang, Changhao Chen

**Published:** 2026-08-04 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.03244v1) | [PDF](https://arxiv.org/pdf/2608.03244v1.pdf)

<details>
<summary>Abstract</summary>

Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visual observations and continuous waypoint trajectories through a single diffusion process. Given history frames and a goal image, UniNav jointl...

</details>

---

### [CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)

**Authors:** Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan et al. (14 authors)

**Published:** 2026-08-04 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.03211v1) | [PDF](https://arxiv.org/pdf/2608.03211v1.pdf)

<details>
<summary>Abstract</summary>

Visual world models typically learn future dynamics from a single observation stream, limiting their ability to model cooperative systems with multiple independently moving observers. We investigate this challenge in Mother--Child endoscopic retrograde cholangiopancreatography (ERCP), where two flexible scopes provide complementary yet role-dependent views without a calibrated stereo relationship. Unlike conventional multi-view fusion that assumes symmetric information exchange, we formulate \te...

</details>

---

### [EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation](https://arxiv.org/abs/2608.02990v1)

**Authors:** Jiayi Luo, Hanxin Zhu, Chen Gao, Jiankun Wang, Cong Wang et al. (8 authors)

**Published:** 2026-08-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.02990v1) | [PDF](https://arxiv.org/pdf/2608.02990v1.pdf)

<details>
<summary>Abstract</summary>

Latent diffusion models (LDMs) have recently significantly advanced embodied learning in constructing powerful embodied manipulation world models. However, despite the remarkable performance, existing LDMs predominantly rely on Variational Autoencoders (VAEs) optimized for natural scenes while failing to account for the unique characteristics of embodied manipulation scenarios, yielding latent representations that are neither compact nor controllable, thereby hindering efficient training of LDMs...

</details>

---

### [RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)

**Authors:** Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang et al. (8 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.02953v1) | [PDF](https://arxiv.org/pdf/2608.02953v1.pdf)

<details>
<summary>Abstract</summary>

Realistic weather translation is valuable for developing and evaluating autonomous driving systems, yet collecting paired videos of the same scenes under different weather conditions at scale is impractical. Existing methods therefore rely on synthetic data, 3D weather editing, or geometry-conditioned generation, often compromising weather realism or scene fidelity. We propose RealWeather, a driving world model for both realistic and scene-faithful weather translation. Our key idea is to learn a...

</details>

---

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

### [PhyCheck: Fine-Grained Evidence-Grounded Dataset for Physical Law Understanding in Video-LLMs](https://arxiv.org/abs/2608.02150v2)

**Authors:** Zhongjie Ba, Shengwang Xu, Peng Cheng, Jinyang Zou, Ting Yu et al. (7 authors)

**Published:** 2026-08-03 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.02150v2) | [PDF](https://arxiv.org/pdf/2608.02150v2.pdf)

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
