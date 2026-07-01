# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-01 17:54 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734v1)

**Authors:** Jiwen Yu, Jianxiong Gao, Jianhong Bai, Yiran Qin, Kaiyi Huang et al. (10 authors)

**Published:** 2026-06-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.31734v1) | [PDF](https://arxiv.org/pdf/2606.31734v1.pdf) | [Project Page](https://yujiwen.github.io/memlearner/)

<details>
<summary>Abstract</summary>

Video World Models are interactive video generation models that predict future world states based on user actions and history video frames. A critical challenge in video world models is the lack of memory, causing inconsistent generated scenes over extended durations. Previous methods explored rule-based context frame retrieval as memory, but they fail to generalize in scenarios with scene occlusions and dynamic objects. We propose MemLearner, a learning-based adaptive context query method using...

</details>

---

### [One Video, One World: Turning Monocular Video into Physical 4D Scenes](https://arxiv.org/abs/2606.31388v1)

**Authors:** Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang et al. (10 authors)

**Published:** 2026-06-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.31388v1) | [PDF](https://arxiv.org/pdf/2606.31388v1.pdf) | [Project Page](https://OneVideoOneWorld.github.io/)

<details>
<summary>Abstract</summary>

We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-la...

</details>

---

### [DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model](https://arxiv.org/abs/2606.30292v1)

**Authors:** Daniyel Ayupov, Artur Markov-Tsoy

**Published:** 2026-06-29 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30292v1) | [PDF](https://arxiv.org/pdf/2606.30292v1.pdf) | [Project Page](https://trydreamforge.com/)

<details>
<summary>Abstract</summary>

We present DreamForge-World 0.1 Preview, a preview foundational world model for real-time interactive world simulation. The system adapts the LongLive 1 autoregressive video stack, itself derived from Wan2.1-T2V-1.3B, with a residual action pathway inspired by the Matrix-Game family. DreamForge-World 0.1 Preview focuses on a complementary axis to frontier-scale world simulators: low-compute adaptation, consumer-GPU runtime, and broad interactive capability coverage. It supports live keyboard and...

</details>

---

## Other Recent Papers

### [DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation](https://arxiv.org/abs/2606.32028v1)

**Authors:** Ziyu Shan, Zhenyu Wu, Xiaofeng Wang, Zheng Zhu, Ziwei Wang

**Published:** 2026-06-30 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.32028v1) | [PDF](https://arxiv.org/pdf/2606.32028v1.pdf)

<details>
<summary>Abstract</summary>

Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich det...

</details>

---

### [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026v1)

**Authors:** Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren

**Published:** 2026-06-30 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.32026v1) | [PDF](https://arxiv.org/pdf/2606.32026v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes ...

</details>

---

### [WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models](https://arxiv.org/abs/2606.31672v1)

**Authors:** Ting-Bing Xu, Jiacheng Sui, Zhe Gao, Kewei Shi, Wenjin Yang et al. (14 authors)

**Published:** 2026-06-30 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31672v1) | [PDF](https://arxiv.org/pdf/2606.31672v1.pdf)

<details>
<summary>Abstract</summary>

Despite rapid progress in interactive world models (IWMs), existing benchmarks evaluate action following only at trajectory level and ignore memory and interaction physics. We introduce WorldRoamBench, an open-world benchmark for long-horizon stability across four dimensions, each with tailored innovations: (i) Action: per-frame action metric bypassing cross-model semantic scale disparity and exposing failures hidden by trajectory; (ii) Vision: segment-based drift metric capturing non-monotonic ...

</details>

---

### [Ask the World Before Acting: Budgeted Environment Probing for World-Model Calibration](https://arxiv.org/abs/2606.31422v1)

**Authors:** Xinyuan Song, Zekun Cai

**Published:** 2026-06-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31422v1) | [PDF](https://arxiv.org/pdf/2606.31422v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon language agents do not only choose actions; they carry a private model of the world from one decision to the next. When that model drifts, a later failure can be decided before the failing action is ever taken. We study a direct repair mechanism: before committing to the next task action, an agent may ask the environment about one belief field and write the answer back into its world model. This makes environment interaction a scarce calibration resource, not merely a way to advance...

</details>

---

### [World-Model Collapse as a Phase Transition](https://arxiv.org/abs/2606.31399v1)

**Authors:** Xinyuan Song, Zekun Cai

**Published:** 2026-06-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31399v1) | [PDF](https://arxiv.org/pdf/2606.31399v1.pdf)

<details>
<summary>Abstract</summary>

Water looks unchanged as it warms, then at a critical point it boils. We ask whether long-horizon language agents show an analogous transition in their implicit world models. In some parameter settings, changing state load by a small amount, or adding a single step of horizon, leaves behavior nearly unchanged; near a critical boundary, the same small change causes a sudden world collapse. We study this effect in a deterministic task family with exact per-step gold state. A large grid search over...

</details>

---

### [Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding](https://arxiv.org/abs/2606.31232v1)

**Authors:** Zhenghao Zhang, Yuanxiang Wang, Zhenyu Guan, Yujia Yang, Bingkang Shi et al. (14 authors)

**Published:** 2026-06-30 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.31232v1) | [PDF](https://arxiv.org/pdf/2606.31232v1.pdf)

<details>
<summary>Abstract</summary>

Learning visual world models for planning requires compact latent dynamics that remain sensitive to actions, yet reconstruction-free joint-embedding objectives can collapse to action-insensitive representations. We propose Delta-JEPA, an end-to-end reconstruction-free world model that augments latent forward prediction with a Latent Difference Action Decoder (LDAD). Unlike inverse decoders that infer actions from concatenated endpoint embeddings, LDAD reconstructs the executed action from the la...

</details>

---

### [ForgeDrive: Bidirectional Cross-Conditioning for Unified Visual-Action Generation in Autonomous Driving](https://arxiv.org/abs/2606.31226v1)

**Authors:** Xuchang Zhong, He Zheng, Chenxu Zhao, Tianxiong Lv, Hangqi Fan et al. (11 authors)

**Published:** 2026-06-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.31226v1) | [PDF](https://arxiv.org/pdf/2606.31226v1.pdf)

<details>
<summary>Abstract</summary>

World-model-based autonomous driving endows the model with the ability to understand scene evolution. Yet this promise is undermined by the prevailing imagine-then-act paradigm, which allows errors from the more challenging visual generation stage to cascade into action planning. We introduce ForgeDrive, a unified autoregressive diffusion framework with visual-action cross-conditioning that closes this gap through act-then-imagine paradigm. ForgeDrive factorizes the future as a sequence of per-t...

</details>

---

### [Long-term Traffic Simulation via Structured Autoregressive Modeling](https://arxiv.org/abs/2606.31209v1)

**Authors:** Lingyu Xiao, Zexin Feng, Xintao Yan

**Published:** 2026-06-30 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.31209v1) | [PDF](https://arxiv.org/pdf/2606.31209v1.pdf)

<details>
<summary>Abstract</summary>

Interactive traffic simulation is a vital world model for autonomous driving. A central challenge in long-horizon simulation is modeling sustained multi-agent interactions, which is further exacerbated by dynamic token cardinality as agents continuously enter and exit the scene. In this work, we propose that the solution lies in the synergy between the architectural inductive biases and statistical priors of large-scale sequence models, e.g., Large Language Models (LLMs). Our probing experiments...

</details>

---

### [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)

**Authors:** Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng

**Published:** 2026-06-29 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2606.30639v1) | [PDF](https://arxiv.org/pdf/2606.30639v1.pdf)

<details>
<summary>Abstract</summary>

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits...

</details>

---

### [OWMDrive: Causality-Aware End-to-End Autonomous Driving via 4D Occupancy World Model](https://arxiv.org/abs/2606.30421v1)

**Authors:** Junjie Cheng, Ruiqi Song, Ye Wu, Nanxing Zeng, Ximiao Li et al. (6 authors)

**Published:** 2026-06-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.30421v1) | [PDF](https://arxiv.org/pdf/2606.30421v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving systems are steadily moving toward end-to-end paradigms to mitigate the limited adaptability of rule-based pipelines in complex traffic environments. However, most existing learning-based methods still make decisions from static representations of the current scene, without explicit future rollouts or modeling of the temporal causal dynamics in traffic interactions. This limitation often results in unstable or overly conservative planning under high-uncertainty conditions, suc...

</details>

---

### [Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation](https://arxiv.org/abs/2606.29908v1)

**Authors:** Hong Chen, Daqi Liu, Zehan Zhang, Haiguang Wang, Tianhao Lu et al. (13 authors)

**Published:** 2026-06-29 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29908v1) | [PDF](https://arxiv.org/pdf/2606.29908v1.pdf)

<details>
<summary>Abstract</summary>

Existing world model-based planners for visual navigation typically follow a verification-centric paradigm, decoupling goal intent from trajectory synthesis. This approach suffers from candidate dependence, heavy computational overhead, and inconsistencies between sampled actions and predicted visuals. To address these issues, we propose SWAM (Spatial-perceiving World Action Model), a task-centric joint observation-action generation framework. Given start and goal RGB observations, SWAM performs...

</details>

---

### [LWDrive: Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879v2)

**Authors:** Chen Yang, Yuhao Wei, Ze Xu, Ziheng Zou, Shuang Liang et al. (9 authors)

**Published:** 2026-06-29 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29879v2) | [PDF](https://arxiv.org/pdf/2606.29879v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) provide powerful semantic understanding and commonsense reasoning for End-to-End Autonomous Driving (E2E-AD) planning. However, trajectories directly generated by VLMs often encode only coarse driving intentions and remain insufficient for geometrically accurate, future-aware, and multi-view-grounded planning. To address these limitations, we develop the Layer-Wise World-Model-Guided Driving framework (LWDrive). LWDrive is a VLM planning framework that refines coars...

</details>

---

### [The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models](https://arxiv.org/abs/2606.29799v1)

**Authors:** Rafael Kaufmann, Felix Neubürger, Michael Walters, Thomas Kopinski, Dimitrije Marković

**Published:** 2026-06-29 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.29799v1) | [PDF](https://arxiv.org/pdf/2606.29799v1.pdf)

<details>
<summary>Abstract</summary>

This project introduces the CRISTAL Method (Coherent Reliable Intentional Synthesis of Truthful Analysis Logic), a neurosymbolic framework for automating complex analysis workflows, with fundamental investment analysis as a primary use case. This domain poses major challenges: high structural uncertainty, noisy and subjective data, tight attention budgets, and the need for justified, reproducible decisions. Human analysts often struggle in this domain due to cognitive biases and limitations, sug...

</details>

---

### [HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data](https://arxiv.org/abs/2606.29784v1)

**Authors:** Xinrui Ruan, Zhenyu Zhao, Waverly Wei, Yueshan Zhang, Zeyu Zheng et al. (7 authors)

**Published:** 2026-06-29 | **Categories:** stat.ME, cs.AI, econ.EM

**Links:** [arXiv](https://arxiv.org/abs/2606.29784v1) | [PDF](https://arxiv.org/pdf/2606.29784v1.pdf)

<details>
<summary>Abstract</summary>

Reliable generative AI models critically rely on expert human annotations to evaluate output quality, yet these "gold" labels are expensive to collect and limited in quantity. Organizations thus often turn to collecting vast but noisy "silver" labels from crowdsourced workers or vendor annotators as proxies for gold labels. Because gold remains the evaluation target, naively aggregating noisy silver labels may introduce bias, and estimators built on sparsely observed gold labels may have high va...

</details>

---
