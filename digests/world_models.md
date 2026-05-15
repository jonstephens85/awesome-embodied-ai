# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-15 17:26 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)

**Authors:** Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou

**Published:** 2026-05-14 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.15185v1) | [PDF](https://arxiv.org/pdf/2605.15185v1.pdf) | [Project Page](https://pdi-bench.github.io/)

<details>
<summary>Abstract</summary>

Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video evaluation pipelines rely heavily on human judgment or learned graders, which can be subjective and weakly diagnostic for geometric failures. We introduce PDI-Bench (Perspective Distortion Index), a quantitative framework for auditing geometric coherence in generated videos. Given a generated clip, we ...

</details>

---

### [SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](https://arxiv.org/abs/2605.15178v1)

**Authors:** Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen et al. (9 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.15178v1) | [PDF](https://arxiv.org/pdf/2605.15178v1.pdf) | [Project Page](https://nvlabs.github.io/Sana/WM/)

<details>
<summary>Abstract</summary>

We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. SANA-WM achieves visual quality comparable to large-scale industrial baselines such as LingBot-World and HY-WorldPlay, while significantly improving efficiency. Four core designs drive our architecture: (1) Hybrid Linear Attention combines frame-wise Gated DeltaNet (GDN) with softmax attention for ...

</details>

---

### [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)

**Authors:** Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan et al. (9 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.15141v1) | [PDF](https://arxiv.org/pdf/2605.15141v1.pdf) | [GitHub](https://github.com/thu-ml/Causal-Forcing)

<details>
<summary>Abstract</summary>

Real-time interactive video generation requires low-latency, streaming, and controllable rollout. Existing autoregressive (AR) diffusion distillation methods have achieved strong results in the chunk-wise 4-step regime by distilling bidirectional base models into few-step AR students, but they remain limited by coarse response granularity and non-negligible sampling latency. In this paper, we study a more aggressive setting: frame-wise autoregression with only 1--2 sampling steps. In this regime...

</details>

---

### [IFPV: An Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification](https://arxiv.org/abs/2605.14851v1)

**Authors:** Zhigao Huang, Zhengqing Hu, Dong Chen, Shaohan Zhang, Zhao Jin et al. (8 authors)

**Published:** 2026-05-14 | **Categories:** cs.MA, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.14851v1) | [PDF](https://arxiv.org/pdf/2605.14851v1.pdf) | [GitHub](https://github.com/zhigao3ks/IFPV)

<details>
<summary>Abstract</summary>

Operational plan generation and verification are critical for modern complex and rapidly changing battlefield environments, yet traditional generation and verification methods still respectively face the challenges of generation infeasibility and verification insufficiency. To alleviate these limitations, we propose an Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification (IFPV). IFPV consists of two tightly coupled modules: Multi-Perspective Hi...

</details>

---

### [Learning POMDP World Models from Observations with Language-Model Priors](https://arxiv.org/abs/2605.13740v1)

**Authors:** Valentin Six, Frederik Panse, Mathis Fajeau, Lancelot Da Costa, Mridul Sharma et al. (10 authors)

**Published:** 2026-05-13 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.13740v1) | [PDF](https://arxiv.org/pdf/2605.13740v1.pdf) | [GitHub](https://github.com/atomresearch/pinductor)

<details>
<summary>Abstract</summary>

Whether navigating a building, operating a robot, or playing a game, an agent that acts effectively in an environment must first learn an internal model of how that environment works. Partially-observable Markov decision processes (POMDPs) provide a flexible modeling class for such internal world models, but learning them from observation-action trajectories alone is challenging and typically requires extensive environment interaction. We ask whether language-model priors can reduce costly inter...

</details>

---

## Other Recent Papers

### [Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations](https://arxiv.org/abs/2605.14937v1)

**Authors:** Jonathan Spieler, Angel Villar-Corrales, Sven Behnke

**Published:** 2026-05-14 | **Categories:** cs.LG, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.14937v1) | [PDF](https://arxiv.org/pdf/2605.14937v1.pdf)

<details>
<summary>Abstract</summary>

Predictive world models enable agents to model scene dynamics and reason about the consequences of their actions. Inspired by human perception, object-centric world models capture scene dynamics using object-level representations, which can be used for downstream applications such as action planning. However, most object-centric world models and reinforcement learning (RL) approaches learn reactive policies that are fixed at inference time, limiting generalization to novel situations. We propose...

</details>

---

### [Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model](https://arxiv.org/abs/2605.14723v1)

**Authors:** Minghao Wu, Yuting Yan, Zhenyang Cai, Ke Ji, Chuangsen Fang et al. (12 authors)

**Published:** 2026-05-14 | **Categories:** cs.AI, cs.CL, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.14723v1) | [PDF](https://arxiv.org/pdf/2605.14723v1.pdf)

<details>
<summary>Abstract</summary>

Sepsis management in the ICU requires sequential treatment decisions under rapidly evolving patient physiology. Although large language models (LLMs) encode broad clinical knowledge and can reason over guidelines, they are not inherently grounded in action-conditioned patient dynamics. We introduce SepsisAgent, a world model-augmented LLM agent for sepsis treatment recommendation. SepsisAgent uses a learned Clinical World Model to simulate patient responses under candidate fluid--vasopressor int...

</details>

---

### [EponaV2: Driving World Model with Comprehensive Future Reasoning](https://arxiv.org/abs/2605.14696v1)

**Authors:** Jiawei Xu, Zhizhou Zhong, Zhijian Shu, Mingkai Jia, Mingxiao Li et al. (11 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.14696v1) | [PDF](https://arxiv.org/pdf/2605.14696v1.pdf)

<details>
<summary>Abstract</summary>

Data scaling plays a pivotal role in the pursuit of general intelligence. However, the prevailing perception-planning paradigm in autonomous driving relies heavily on expensive manual annotations to supervise trajectory planning, which severely limits its scalability. Conversely, although existing perception-free driving world models achieve impressive driving performance, their real-world reasoning ability for planning is solely built on next frame image forecasting. Due to the lack of enough s...

</details>

---

### [When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution](https://arxiv.org/abs/2605.14504v1)

**Authors:** Zilin Zhu, Longteng Guo, Yanghong Mei, Bowen Pang, Zongxun Zhang et al. (8 authors)

**Published:** 2026-05-14 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.14504v1) | [PDF](https://arxiv.org/pdf/2605.14504v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon household tasks demand robust high-level planning and sustained reasoning capabilities, which are largely overlooked by existing embodied AI benchmarks that emphasize short-horizon navigation or manipulation and rely on fixed task categories. We introduce LongAct, a benchmark designed to evaluate planning-level autonomy in long-horizon household tasks specified through free-form instructions. By abstracting away embodiment-specific low-level control, LongAct isolates high-level cogn...

</details>

---

### [Coding Agent Is Good As World Simulator](https://arxiv.org/abs/2605.14398v1)

**Authors:** Hongyu Wang, Jingquan Wang, Bocheng Zou, Radu Serban, Dan Negrut

**Published:** 2026-05-14 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.14398v1) | [PDF](https://arxiv.org/pdf/2605.14398v1.pdf)

<details>
<summary>Abstract</summary>

World models have emerged as a powerful paradigm for building interactive simulation environments, with recent video-based approaches demonstrating impressive progress in generating visually plausible dynamics. However, because these models typically infer dynamics from video and represent them in latent states, they do not explicitly enforce physical constraints. As a result, the generated video rollouts are not physically plausible, exhibiting unstable contacts, distorted shapes, or inconsiste...

</details>

---

### [Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation](https://arxiv.org/abs/2605.14382v1)

**Authors:** Yuheng Wu, Xiangbo Gao, Tianhao Chen, Xinghao Chen, Qing Yin et al. (7 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV, cs.GR, cs.MM

**Links:** [arXiv](https://arxiv.org/abs/2605.14382v1) | [PDF](https://arxiv.org/pdf/2605.14382v1.pdf)

<details>
<summary>Abstract</summary>

Interactive real-time autoregressive video generation is essential for applications such as content creation and world modeling, where visual content must adapt to dynamically evolving event conditions. A fundamental challenge lies in balancing reactivity and stability: models must respond promptly to new events while maintaining temporal coherence over long horizons. Existing approaches distill bidirectional models into autoregressive generators and further adapt them via streaming long tuning,...

</details>

---

### [Enhanced and Efficient Reasoning in Large Learning Models](https://arxiv.org/abs/2605.14036v1)

**Authors:** Leslie G. Valiant

**Published:** 2026-05-13 | **Categories:** cs.AI, cs.CC, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.14036v1) | [PDF](https://arxiv.org/pdf/2605.14036v1.pdf)

<details>
<summary>Abstract</summary>

In current Large Language Models we can trust the production of smoothly flowing prose on the basis of the principles of machine learning. However, there is no comparably principled basis to justify trust in the content of the text produced. It appears to be conventional wisdom that addressing this issue by adding more principled reasoning is not computationally affordable. Here we propose a principled method of reasoning that is efficient enough to be practical for large language models. Furthe...

</details>

---

### [JEDI: Joint Embedding Diffusion World Model for Online Model-Based Reinforcement Learning](https://arxiv.org/abs/2605.13013v1)

**Authors:** Jing Yu Lim, Rushi Shah, Zarif Ikram, Samson Yu, Haozhe Ma et al. (7 authors)

**Published:** 2026-05-13 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.13013v1) | [PDF](https://arxiv.org/pdf/2605.13013v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion world models have recently become competitive for online model-based reinforcement learning, but current approaches expose a tension: pixel diffusion is effective but computationally expensive while the latest latent diffusion approach improves efficiency yet performs subpar. The latter also relies on separately trained latents rather than the end-to-end world-model objectives that have driven much of modern MBRL progress. In particular, JEPA-style predictive representation learning ha...

</details>

---

### [Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue](https://arxiv.org/abs/2605.12920v1)

**Authors:** Vardhan Dongre, Dilek Hakkani-Tür

**Published:** 2026-05-13 | **Categories:** cs.MA, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.12920v1) | [PDF](https://arxiv.org/pdf/2605.12920v1.pdf)

<details>
<summary>Abstract</summary>

Effective collaboration between embodied agents requires more than acting in a shared environment; it demands communication grounded in each agent's evolving understanding of the world. When agents can only partially observe their surroundings, coordination without communication is provably hard, but communication can, in principle, bridge this gap by allowing agents to share observations and align their world models. In this work, we examine whether LLM-based embodied agents actually realize th...

</details>

---

### [PROMETHEUS: Automating Deep Causal Research Integrating Text, Data and Models](https://arxiv.org/abs/2605.12835v1)

**Authors:** Sridhar Mahadevan

**Published:** 2026-05-13 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.12835v1) | [PDF](https://arxiv.org/pdf/2605.12835v1.pdf)

<details>
<summary>Abstract</summary>

Large language models can extract local causal claims from text, but those claims become more useful when organized as persistent, navigable world models rather than as flat summaries. We introduce PROMETHEUS, a framework that turns retrieved literature, filings, reviews, reports, agent traces, source data, code, simulations, and scientific models into causal atlases: sheaf-like families of local causal predictive-state models over an explicit cover of a research substrate. Each local region con...

</details>

---
