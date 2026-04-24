# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-24 16:56 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)

**Authors:** Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi et al. (9 authors)

**Published:** 2026-04-23 | **Categories:** cs.CV, cs.AI, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2604.21931v1) | [PDF](https://arxiv.org/pdf/2604.21931v1.pdf) | [Project Page](https://seeing-fast-and-slow.github.io/)

<details>
<summary>Abstract</summary>

How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to l...

</details>

---

### [Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](https://arxiv.org/abs/2604.21741v1)

**Authors:** Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu et al. (8 authors)

**Published:** 2026-04-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.21741v1) | [PDF](https://arxiv.org/pdf/2604.21741v1.pdf) | [Project Page](https://hi-wm.github.io/)

<details>
<summary>Abstract</summary>

Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training ...

</details>

---

### [Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics](https://arxiv.org/abs/2604.21017v1)

**Authors:** Open-H-Embodiment Consortium,  :, Nigel Nelson, Juo-Tung Chen, Jesse Haworth et al. (216 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.21017v1) | [PDF](https://arxiv.org/pdf/2604.21017v1.pdf) | [Project Page](https://open-h.github.io/open-h-embodiment/)

<details>
<summary>Abstract</summary>

Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with s...

</details>

---

### [Occupancy Reward Shaping: Improving Credit Assignment for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2604.20627v1)

**Authors:** Aravind Venugopal, Jiayu Chen, Xudong Wu, Chongyi Zheng, Benjamin Eysenbach et al. (6 authors)

**Published:** 2026-04-22 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20627v1) | [PDF](https://arxiv.org/pdf/2604.20627v1.pdf) | [Project Page](https://aravindvenu7.github.io/website/ors/) | [GitHub](https://github.com/aravindvenu7/occupancy_reward_shaping)

<details>
<summary>Abstract</summary>

The temporal lag between actions and their long-term consequences makes credit assignment a challenge when learning goal-directed behaviors from data. Generative world models capture the distribution of future states an agent may visit, indicating that they have captured temporal information. How can that temporal information be extracted to perform credit assignment? In this paper, we formalize how the temporal information stored in world models encodes the underlying geometry of the world. Lev...

</details>

---

## Other Recent Papers

### [WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)

**Authors:** Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao et al. (8 authors)

**Published:** 2026-04-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.21686v1) | [PDF](https://arxiv.org/pdf/2604.21686v1.pdf)

<details>
<summary>Abstract</summary>

Interactive video generation models such as Genie, YUME, HY-World, and Matrix-Game are advancing rapidly, yet every model is evaluated on its own benchmark with private scenes and trajectories, making fair cross-model comparison impossible. Existing public benchmarks offer useful metrics such as trajectory error, aesthetic scores, and VLM-based judgments, but none supplies the standardized test conditions -- identical scenes, identical action sequences, and a unified control interface -- needed ...

</details>

---

### [CCTVBench: Contrastive Consistency Traffic VideoQA Benchmark for Multimodal LLMs](https://arxiv.org/abs/2604.20460v1)

**Authors:** Xingcheng Zhou, Hao Guo, Rui Song, Walter Zimmer, Mingyu Liu et al. (8 authors)

**Published:** 2026-04-22 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.20460v1) | [PDF](https://arxiv.org/pdf/2604.20460v1.pdf)

<details>
<summary>Abstract</summary>

Safety-critical traffic reasoning requires contrastive consistency: models must detect true hazards when an accident occurs, and reliably reject plausible-but-false hypotheses under near-identical counterfactual scenes. We present CCTVBench, a Contrastive Consistency Traffic VideoQA Benchmark built on paired real accident videos and world-model-generated counterfactual counterparts, together with minimally different, mutually exclusive hypothesis questions. CCTVBench enforces a single structured...

</details>

---

### [X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)

**Authors:** Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu et al. (13 authors)

**Published:** 2026-04-22 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2604.20289v1) | [PDF](https://arxiv.org/pdf/2604.20289v1.pdf)

<details>
<summary>Abstract</summary>

Real-time world simulation is becoming a key infrastructure for scalable evaluation and online reinforcement learning of autonomous driving systems. Recent driving world models built on autoregressive video diffusion achieve high-fidelity, controllable multi-camera generation, but their inference cost remains a bottleneck for interactive deployment. However, existing diffusion caching methods are designed for offline video generation with multiple denoising steps, and do not transfer to this sce...

</details>

---

### [Cortex 2.0: Grounding World Models in Real-World Industrial Deployment](https://arxiv.org/abs/2604.20246v1)

**Authors:** Adriana Aida, Walid Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch et al. (28 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.20246v1) | [PDF](https://arxiv.org/pdf/2604.20246v1.pdf)

<details>
<summary>Abstract</summary>

Industrial robotic manipulation demands reliable long-horizon execution across embodiments, tasks, and changing object distributions. While Vision-Language-Action models have demonstrated strong generalization, they remain fundamentally reactive. By optimizing the next action given the current observation without evaluating potential futures, they are brittle to the compounding failure modes of long-horizon tasks. Cortex 2.0 shifts from reactive control to plan-and-act by generating candidate fu...

</details>

---

### [Toward Safe Autonomous Robotic Endovascular Interventions using World Models](https://arxiv.org/abs/2604.20151v1)

**Authors:** Harry Robertshaw, Nikola Fischer, Han-Ru Wu, Andrea Walker Perez, Weiyuan Deng et al. (9 authors)

**Published:** 2026-04-22 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.20151v1) | [PDF](https://arxiv.org/pdf/2604.20151v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous mechanical thrombectomy (MT) presents substantial challenges due to highly variable vascular geometries and the requirements for accurate, real-time control. While reinforcement learning (RL) has emerged as a promising paradigm for the automation of endovascular navigation, existing approaches often show limited robustness when faced with diverse patient anatomies or extended navigation horizons. In this work, we investigate a world-model-based framework for autonomous endovascular na...

</details>

---
