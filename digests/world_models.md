# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-04-23 22:34 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Occupancy Reward Shaping: Improving Credit Assignment for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2604.20627v1)

**Authors:** Aravind Venugopal, Jiayu Chen, Xudong Wu, Chongyi Zheng, Benjamin Eysenbach et al. (6 authors)

**Published:** 2026-04-22 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.20627v1) | [PDF](https://arxiv.org/pdf/2604.20627v1.pdf) | [Project Page](https://aravindvenu7.github.io/website/ors/) | [GitHub](https://github.com/aravindvenu7/occupancy_reward_shaping)

<details>
<summary>Abstract</summary>

The temporal lag between actions and their long-term consequences makes credit assignment a challenge when learning goal-directed behaviors from data. Generative world models capture the distribution of future states an agent may visit, indicating that they have captured temporal information. How can that temporal information be extracted to perform credit assignment? In this paper, we formalize how the temporal information stored in world models encodes the underlying geometry of the world. Lev...

</details>

---

### [UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)

**Authors:** Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge et al. (6 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19734v1) | [PDF](https://arxiv.org/pdf/2604.19734v1.pdf) | [Project Page](https://xpeng-robotics.github.io/unit/)

<details>
<summary>Abstract</summary>

Scaling humanoid foundation models is bottlenecked by the scarcity of robotic data. While massive egocentric human data offers a scalable alternative, bridging the cross-embodiment chasm remains a fundamental challenge due to kinematic mismatches. We introduce UniT (Unified Latent Action Tokenizer via Visual Anchoring), a framework that establishes a unified physical language for human-to-humanoid transfer. Grounded in the philosophy that heterogeneous kinematics share universal visual consequen...

</details>

---

## Other Recent Papers

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

**Authors:** Adriana Aida, Walida Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch et al. (28 authors)

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

### [ChipCraftBrain: Validation-First RTL Generation via Multi-Agent Orchestration](https://arxiv.org/abs/2604.19856v1)

**Authors:** Cagri Eryilmaz

**Published:** 2026-04-21 | **Categories:** cs.AR, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2604.19856v1) | [PDF](https://arxiv.org/pdf/2604.19856v1.pdf)

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) show promise for generating Register-Transfer Level (RTL) code from natural language specifications, but single-shot generation achieves only 60-65% functional correctness on standard benchmarks. Multi-agent approaches such as MAGE reach 95.9% on VerilogEval yet remain untested on harder industrial benchmarks such as NVIDIA's CVDP, lack synthesis awareness, and incur high API costs. We present ChipCraftBrain, a framework combining symbolic-neural reasoning with adapt...

</details>

---

### [Mask World Model: Predicting What Matters for Robust Robot Policy Learning](https://arxiv.org/abs/2604.19683v2)

**Authors:** Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li et al. (12 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2604.19683v2) | [PDF](https://arxiv.org/pdf/2604.19683v2.pdf)

<details>
<summary>Abstract</summary>

World models derived from large-scale video generative pre-training have emerged as a promising paradigm for generalist robot policy learning. However, standard approaches often focus on high-fidelity RGB video prediction, this can result in overfitting to irrelevant factors, such as dynamic backgrounds and illumination changes. These distractions reduce the model's ability to generalize, ultimately leading to unreliable and fragile control policies. To address this, we introduce the Mask World ...

</details>

---

### [Safety-Critical Contextual Control via Online Riemannian Optimization with World Models](https://arxiv.org/abs/2604.19639v1)

**Authors:** Tongxin Li

**Published:** 2026-04-21 | **Categories:** eess.SY, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19639v1) | [PDF](https://arxiv.org/pdf/2604.19639v1.pdf)

<details>
<summary>Abstract</summary>

Modern world models are becoming too complex to admit explicit dynamical descriptions. We study safety-critical contextual control, where a Planner must optimize a task objective using only feasibility samples from a black-box Simulator, conditioned on a context signal $ξ_t$. We develop a sample-based Penalized Predictive Control (PPC) framework grounded in online Riemannian optimization, in which the Simulator compresses the feasibility manifold into a score-based density $\hat{p}(u \mid ξ_t)$ ...

</details>

---

### [LASER: Learning Active Sensing for Continuum Field Reconstruction](https://arxiv.org/abs/2604.19355v1)

**Authors:** Huayu Deng, Jinghui Zhong, Xiangming Zhu, Yunbo Wang, Xiaokang Yang

**Published:** 2026-04-21 | **Categories:** cs.LG, cs.AI, cs.CE

**Links:** [arXiv](https://arxiv.org/abs/2604.19355v1) | [PDF](https://arxiv.org/pdf/2604.19355v1.pdf)

<details>
<summary>Abstract</summary>

High-fidelity measurements of continuum physical fields are essential for scientific discovery and engineering design but remain challenging under sparse and constrained sensing. Conventional reconstruction methods typically rely on fixed sensor layouts, which cannot adapt to evolving physical states. We propose LASER, a unified, closed-loop framework that formulates active sensing as a Partially Observable Markov Decision Process (POMDP). At its core, LASER employs a continuum field latent worl...

</details>

---

### [RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)

**Authors:** Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang et al. (11 authors)

**Published:** 2026-04-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2604.19092v1) | [PDF](https://arxiv.org/pdf/2604.19092v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in large-scale video world models have enabled increasingly realistic future prediction, raising the prospect of leveraging imagined videos for robot learning. However, visual realism does not imply physical plausibility, and behaviors inferred from generated videos may violate dynamics and fail when executed by embodied agents. Existing benchmarks begin to incorporate notions of physical plausibility, but they largely remain perception- or diagnostic-oriented and do not systemat...

</details>

---
