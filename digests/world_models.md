# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-07-02 22:56 UTC

**Papers found:** 22

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Valdi: Value Diffusion World Models](https://arxiv.org/abs/2607.00917v1)

**Authors:** Christopher Lindenberg, Kashyap Chitta

**Published:** 2026-07-01 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00917v1) | [PDF](https://arxiv.org/pdf/2607.00917v1.pdf) | [GitHub](https://github.com/Kit115/ValueDiffusionWorldModels)

<details>
<summary>Abstract</summary>

World models can enable Model Predictive Control (MPC), but this requires dynamics prediction that is both fast enough for online use and expressive enough to represent uncertain futures. Diffusion models offer a natural mechanism for modeling uncertain dynamics, yet their iterative inference procedure makes them difficult to use for low-latency latent planning. We bridge this gap with Value Diffusion World Models (Valdi), combining end-to-end online training for MPC with a latent diffusion dyna...

</details>

---

### [From World Models to World Action Models: A Concise Tutorial for Robotics](https://arxiv.org/abs/2607.00836v1)

**Authors:** Xiaoxiong Zhang, Xiong Zeng, Wei Zhang

**Published:** 2026-07-01 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2607.00836v1) | [PDF](https://arxiv.org/pdf/2607.00836v1.pdf) | [Project Page](https://clearlab-sustech.github.io/WorldModelSurvey/)

<details>
<summary>Abstract</summary>

World models are increasingly used in embodied intelligence and generative simulation, yet their scope remains ambiguous across communities. This tutorial presents a design-space view of world models as action-conditioned predictive models that estimate the future evolution of task-relevant observations or states. We categorize existing methods into observation-space and state-space world models, comparing their trade-offs in visual fidelity, spatial structure, physical interpretability, and con...

</details>

---

### [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678v1)

**Authors:** Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin et al. (21 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00678v1) | [PDF](https://arxiv.org/pdf/2607.00678v1.pdf) | [GitHub](https://github.com/amap-cvlab/ABot-Manipulation)

<details>
<summary>Abstract</summary>

Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result,...

</details>

---

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

## Other Recent Papers

### [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](https://arxiv.org/abs/2607.01060v1)

**Authors:** Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo, Sungdong Kim, Minjoon Seo et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.01060v1) | [PDF](https://arxiv.org/pdf/2607.01060v1.pdf)

<details>
<summary>Abstract</summary>

Video world models are emerging as a scalable alternative for evaluating generalist robot policies, bypassing the physical constraints and engineering burdens of real-world deployment. However, evaluating policies with video world models remains challenging, as world-model errors can make generated rollouts unreliable and slow inference limits large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that pairs a fast autoregressive video world model with a task-progress-a...

</details>

---

### [DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889v1)

**Authors:** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin et al. (7 authors)

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00889v1) | [PDF](https://arxiv.org/pdf/2607.00889v1.pdf)

<details>
<summary>Abstract</summary>

We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single p...

</details>

---

### [Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)

**Authors:** Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu et al. (6 authors)

**Published:** 2026-07-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.00673v1) | [PDF](https://arxiv.org/pdf/2607.00673v1.pdf)

<details>
<summary>Abstract</summary>

Robots deployed in unstructured outdoor environments often plan from scene reconstructions collected before deployment because operators cannot remap large or remote sites before every mission. As a result, robots must make long-horizon planning decisions using stale maps that assume the terrain remains unchanged, even though physical changes to the environment may render previously feasible routes unsafe or unreachable at execution time. We present a physically viable world model for evaluating...

</details>

---

### [AGI Maze as a Benchmark Framework for World-Modeling Agents](https://arxiv.org/abs/2607.00627v1)

**Authors:** Alexey Potapov

**Published:** 2026-07-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00627v1) | [PDF](https://arxiv.org/pdf/2607.00627v1.pdf)

<details>
<summary>Abstract</summary>

Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environ...

</details>

---

### [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457v1)

**Authors:** Jinwoo Jang, Daniel J. Rho, Sihyung Yoon, Hyunsuk Cho, Honguk Woo

**Published:** 2026-07-01 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00457v1) | [PDF](https://arxiv.org/pdf/2607.00457v1.pdf)

<details>
<summary>Abstract</summary>

Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a uniform update policy cannot accommodate the different rates at which knowledge at each scale becomes outdated. We present MuSix, a framework that addresses both challenges through scale-aware world mo...

</details>

---

### [RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail](https://arxiv.org/abs/2607.00310v1)

**Authors:** Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar, Anoop M. Namboodiri, Sashi P. Reddi

**Published:** 2026-07-01 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.00310v1) | [PDF](https://arxiv.org/pdf/2607.00310v1.pdf)

<details>
<summary>Abstract</summary>

Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocentric video of the same activity are available, which viewpoint of training data produces the strongest adapted model? We introduce RetailSMV (...

</details>

---

### [Testing Frontier Large Language Models' Physics Literacy in Parallel Physical Worlds](https://arxiv.org/abs/2607.00276v1)

**Authors:** Dong Zhang

**Published:** 2026-06-30 | **Categories:** cs.LG, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2607.00276v1) | [PDF](https://arxiv.org/pdf/2607.00276v1.pdf)

<details>
<summary>Abstract</summary>

Current large-language-model (LLM) physics benchmarks are usually scored by answer accuracy, which cannot distinguish genuine reasoning from recall of familiar problem patterns and reveals little about where a model's reasoning breaks down. We introduce an auditable four-stage diagnostic that evaluates whether an LLM can reason inside an unfamiliar physics framework through induction, formulation, prediction, and review. The diagnostic combines locked pre-registrations, fresh sessions between st...

</details>

---

### [VOCA: Visual Odometry with Codec Awareness](https://arxiv.org/abs/2607.00189v1)

**Authors:** Nouri Alexander Hilscher, Mateo de Mayo, Dominik Muhle, Christoph Otten genannt Hermes, Daniel Cremers

**Published:** 2026-06-30 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.00189v1) | [PDF](https://arxiv.org/pdf/2607.00189v1.pdf)

<details>
<summary>Abstract</summary>

Camera pose estimation from image streams is a critical component of spatial world models that integrate perception into planning and decision-making. Nearly all Visual Odometry (VO) and Simultaneous Localization and Mapping (V-SLAM) systems have focused on datasets containing raw, uncompressed videos. Many working systems instead use ubiquitous hardware units to efficiently compress and decode video streams, saving orders of magnitude in storage and bandwidth. However, this lossy compression in...

</details>

---

### [3D Point World Models: Point Completion Enables More Accurate Dynamics Learning](https://arxiv.org/abs/2607.00148v1)

**Authors:** Skand Peri, Hung Nguyen, Chanho Kim, Li Fuxin, Stefan Lee

**Published:** 2026-06-30 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.00148v1) | [PDF](https://arxiv.org/pdf/2607.00148v1.pdf)

<details>
<summary>Abstract</summary>

Learning predictive models of the world enables robotic control through planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models lack explicit 3D spatial structure and suffer from geometrically inconsistent long-term rollouts with compounding errors. Emerging 3D dynamics models based on partial point clouds improve geometric consistency but remain sensitive to occlusions and accumulated prediction drift. To address these challenges, we...

</details>

---

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
