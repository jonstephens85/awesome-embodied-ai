# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-12 22:29 UTC

**Papers found:** 23

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video](https://arxiv.org/abs/2608.11017v1)

**Authors:** Ke Ma, Yamin Mao, Weiming Li, Shuai Tan, Yijie Zhong et al. (8 authors)

**Published:** 2026-08-11 | **Categories:** cs.CV, cs.AI, cs.HC

**Links:** [arXiv](https://arxiv.org/abs/2608.11017v1) | [PDF](https://arxiv.org/pdf/2608.11017v1.pdf) | [Project Page](https://dualtransparency.github.io/R4DSG/)

<details>
<summary>Abstract</summary>

Long-horizon egocentric video is a rich substrate for wearable AI assistants, but object-centric questions such as where an item was moved, when it last changed state, or why it was relocated remain difficult because caption- and transcript-based memories rarely preserve persistent object identity or structured spatial change. Existing long-video QA methods mainly emphasize temporal grounding and clip retrieval, while prior 3D scene-graph methods typically assume stronger geometry than free-moti...

</details>

---

### [PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots](https://arxiv.org/abs/2608.10449v1)

**Authors:** Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang et al. (11 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10449v1) | [PDF](https://arxiv.org/pdf/2608.10449v1.pdf) | [Project Page](of)

<details>
<summary>Abstract</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples ...

</details>

---

### [FACT: Failure-Aware Causal Training for World-Action Models](https://arxiv.org/abs/2608.10232v1)

**Authors:** Quanquan Peng, Yutong Liang, Rui Yan, Nicklas Hansen, Xiaolong Wang

**Published:** 2026-08-10 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.10232v1) | [PDF](https://arxiv.org/pdf/2608.10232v1.pdf) | [Project Page](https://fact-wam.github.io/)

<details>
<summary>Abstract</summary>

Recent world-action models (WAMs) show that co-training policies with future prediction can provide physical priors for action generation. Building on the future-prediction ability of video models, many WAMs generate future videos and recover actions with inverse-dynamics models, or use these predicted videos as goal conditions for action generation. In both cases, the world model is trained mostly on successful demonstrations and has little reason to predict the consequences of bad actions. We ...

</details>

---

### [The Evaluation Protocol Determines the Result: An Independent Reproduction of LeWorldModel on TwoRoom](https://arxiv.org/abs/2608.10145v1)

**Authors:** Joyjeet Singh

**Published:** 2026-08-10 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.10145v1) | [PDF](https://arxiv.org/pdf/2608.10145v1.pdf) | [GitHub](https://github.com/joyjeet-singh/tinylab)

<details>
<summary>Abstract</summary>

LeWorldModel trains a latent world model with a prediction loss and a single anti-collapse regulariser, and reports approximately 87% of goals reached on TwoRoom, its simplest diagnostic environment. We reproduce that result by independent reimplementation on roughly $25 of rented compute, with all evaluation on one laptop CPU. We reach 94.0% at the repository's evaluation goal offset, against 84.0% for the authors' own released checkpoint measured under our protocol on identical episodes, and w...

</details>

---

### [Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926v1)

**Authors:** Haodong Li, Shaoteng Liu, Tianyu Wang, Chongjian Ge, Sihui Ji et al. (10 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.09926v1) | [PDF](https://arxiv.org/pdf/2608.09926v1.pdf) | [Project Page](https://lat-dyn-reason.github.io/)

<details>
<summary>Abstract</summary>

The world evolves following its dynamics, i.e., its laws of motion. However, leading video diffusion models largely fit the pixels without modeling how the pixels transit over time. Thus, they render visually plausible frames but may not accurately obey the laws. To capture the dynamics purely from pixels, we introduce Latent Dynamics Reasoning (LDR). LDR casts the latent transition as an explicit kinematic integration, where the lower-order dynamics are integrated numerically and the model regr...

</details>

---

### [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771v1)

**Authors:** Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen et al. (10 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09771v1) | [PDF](https://arxiv.org/pdf/2608.09771v1.pdf) | [Project Page](https://kzz1031.github.io/slim-project-page/)

<details>
<summary>Abstract</summary>

Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step. Much of this capacity supports open-domain semantics, whereas continuous robot manipulation primarily requires compact representations of observations, actions, and the transitions induced by actions. Pixel-level world models provide another route, but predicting visual details irrelevant to control can be unnecessarily expensive. W...

</details>

---

### [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](https://arxiv.org/abs/2608.09381v1)

**Authors:** Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li et al. (9 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09381v1) | [PDF](https://arxiv.org/pdf/2608.09381v1.pdf) | [Project Page](https://spritewithoutice.github.io/JEPA_WAM/)

<details>
<summary>Abstract</summary>

Robust robot control benefits from explicitly modeling state transitions, but video-generation world action models (WAMs) introduce substantial deployment cost. Existing latent WAMs avoid explicit future generation, but often compress predictive representations or separate predictive modeling from the representations used for action generation. We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space, which couples latent transition prediction with continuous action generation thro...

</details>

---

## Other Recent Papers

### [Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning](https://arxiv.org/abs/2608.11204v1)

**Authors:** Wenrui Bao, Tianyun Jiang, Zhiben Chen, Ser-Nam Lim, Peter D. Peng et al. (6 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.11204v1) | [PDF](https://arxiv.org/pdf/2608.11204v1.pdf)

<details>
<summary>Abstract</summary>

Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is comparatively inexpensive and abundant relative to synchronized video--kinematics trajectories, and a natural way to exploit it is to learn world models o...

</details>

---

### [VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174v1)

**Authors:** Haiyu Wu, Randall Balestriero, Morgan Levine

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.11174v1) | [PDF](https://arxiv.org/pdf/2608.11174v1.pdf)

<details>
<summary>Abstract</summary>

Regulating the latent space to an isotropic Gaussian distribution provides a stable and information-maximized landscape for world model planning. However, the latent space property and successful planning remain disconnected. We first study this by comparing SIGReg and VISReg, two regularization loss functions with the same distribution target but different properties. Compared with SIGReg, VISReg has more flexibility in controlling the weights of center, scale, and shape regularization, and a l...

</details>

---

### [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915v1)

**Authors:** Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Wang et al. (22 authors)

**Published:** 2026-08-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.10915v1) | [PDF](https://arxiv.org/pdf/2608.10915v1.pdf)

<details>
<summary>Abstract</summary>

After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeli...

</details>

---

### [Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618v1)

**Authors:** Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He et al. (11 authors)

**Published:** 2026-08-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10618v1) | [PDF](https://arxiv.org/pdf/2608.10618v1.pdf)

<details>
<summary>Abstract</summary>

Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicl...

</details>

---

### [Stream Forcing: Constructing Unified Training Trajectory for Robust Streaming Video Generation](https://arxiv.org/abs/2608.10439v1)

**Authors:** Yueting Zhu, Yuehao Song, Kaicheng Zhang, Bao Tang, Shaoyu Chen et al. (8 authors)

**Published:** 2026-08-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10439v1) | [PDF](https://arxiv.org/pdf/2608.10439v1.pdf)

<details>
<summary>Abstract</summary>

Streaming video generation holds strong potential for world modeling, where future frames must be inferred online sequentially to form a continuous video stream. However, streaming video diffusion models introduce a fundamental train-inference mismatch: inference follows a specialized denoising order, whereas advanced training strategies typically require diverse noise-level configurations. To address this trade-off between train-inference consistency and training coverage, we reformulate the vi...

</details>

---

### [Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving](https://arxiv.org/abs/2608.10386v1)

**Authors:** Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong

**Published:** 2026-08-11 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.10386v1) | [PDF](https://arxiv.org/pdf/2608.10386v1.pdf)

<details>
<summary>Abstract</summary>

Sample-efficient reinforcement learning for autonomous driving is often limited by the trade-off between data efficiency and model bias. While world models reduce the reliance on costly environment interactions, policy optimization over learned dynamics remains sensitive to prediction errors. This paper proposes the Dreamer-SAC framework, which integrates a recurrent state-space world model with an off-policy soft actor-critic algorithm trained directly in latent space. The framework uses a comb...

</details>

---

### [4D-WAM: 4D Consistent World Modeling for Autonomous Driving](https://arxiv.org/abs/2608.10107v1)

**Authors:** Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu et al. (11 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.10107v1) | [PDF](https://arxiv.org/pdf/2608.10107v1.pdf)

<details>
<summary>Abstract</summary>

Emerging World-Action Models (WAMs) have demonstrated promising performance in autonomous driving by jointly modeling future driving scene evolution and trajectory planning. However, existing WAMs are typically trained with video data, which is only 2D projections of the underlying 4D driving scene. Consequently, WAMs fail to understand and capture the structure of 4D scenes and thus generate visually plausible yet 4D inconsistent future predictions that mislead downstream planning. To alleviate...

</details>

---

### [Energy-Structured Latent World Models with Neural Time Fields for Physically Constistent Open-World Motion Planning](https://arxiv.org/abs/2608.09876v1)

**Authors:** Yapeng Liu, Yuanzhao Zhai, Bo Ding, Huaimin Wang, Lin Wang

**Published:** 2026-08-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.09876v1) | [PDF](https://arxiv.org/pdf/2608.09876v1.pdf)

<details>
<summary>Abstract</summary>

Physically consistent motion planning remains a fundamental challenge in embodied AI, as generated trajectories must strictly conform to real-world execution dynamics. While latent world models offer a promising approach by predicting these dynamics, existing methods learn unconstrained future representations where absorbed physics remains implicit. Therefore, they fail to form reusable physical knowledge, which compromises reliability in unpredictable open-world navigation. To address this, we ...

</details>

---

### [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730v1)

**Authors:** Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo et al. (6 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.09730v1) | [PDF](https://arxiv.org/pdf/2608.09730v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation or a large video backbone in the control loop substantially increases inference cost. We introduce World Tokens, an embodied policy architec...

</details>

---

### [Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models](https://arxiv.org/abs/2608.09696v2)

**Authors:** Kevin Murphy

**Published:** 2026-08-10 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.09696v2) | [PDF](https://arxiv.org/pdf/2608.09696v2.pdf)

<details>
<summary>Abstract</summary>

Predicting the answer to interventional ``what if'' questions --- the outcome of an action never taken --- requires a \emph{mechanistic}, causal model, not a curve fit; and learning such a model requires \emph{experiments}, because passive data leaves its mechanisms unidentified. Experiments are expensive, so the central problem is \emph{data efficiency}. We present the Model Discovery Agent (MDA), which couples a large language model (LLM), used as a \emph{proposer} of candidate structures, wit...

</details>

---

### [verdi: retrieval is not transfer for continual world model optimization](https://arxiv.org/abs/2608.09537v1)

**Authors:** Junyu Wu, Shiqin Nie, Youyi Kou, Baohua Yin, Guocai Yao et al. (12 authors)

**Published:** 2026-08-10 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.09537v1) | [PDF](https://arxiv.org/pdf/2608.09537v1.pdf)

<details>
<summary>Abstract</summary>

Foundation world models have made remarkable progress in planning, simulation, and embodied intelligence. However, optimizing a pretrained world model toward a user-specified objective remains difficult: each campaign typically rediscovers optimization strategies from scratch, and the resulting knowledge rarely transfers to the next model. Existing research agents automate the optimization loop but treat successful strategies as directly reusable recipes, without principled safeguards for when t...

</details>

---

### [Sekai2: From World Exploration to Interactive World Modeling](https://arxiv.org/abs/2608.09449v2)

**Authors:** Kang He, Wenshuo Peng, Zihui Gao, Jiaming Tan, Kaipeng Zhang et al. (6 authors)

**Published:** 2026-08-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.09449v2) | [PDF](https://arxiv.org/pdf/2608.09449v2.pdf)

<details>
<summary>Abstract</summary>

Video world models must capture how scenes evolve over time and across viewpoints. Training them for long-horizon generation and camera control therefore benefits from long videos paired with camera trajectories and temporally grounded semantics. Existing corpora rarely offer the three together: large-scale web video provides broad visual diversity but no trajectories or time-aligned text, while pose-annotated datasets are typically short-range or reconstruction-oriented. We introduce Sekai2, a ...

</details>

---

### [WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation](https://arxiv.org/abs/2608.09298v1)

**Authors:** Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo et al. (20 authors)

**Published:** 2026-08-10 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.09298v1) | [PDF](https://arxiv.org/pdf/2608.09298v1.pdf)

<details>
<summary>Abstract</summary>

Action-conditioned world models (ACWMs) promise to provide embodied AI with scalable predictive simulators for planning, policy evaluation, and data generation. Realizing this promise requires precise action-conditioned transitions rather than merely plausible outputs. Yet their applicability remains difficult to establish because prevailing evaluations emphasize visual quality, task outcomes, or coarse rollout-level responsiveness without directly testing simulator fidelity. To address this gap...

</details>

---

### [Did the Grid Erase the Event? EndoClock for Auditing Medical World-Model Pipelines](https://arxiv.org/abs/2608.09266v1)

**Authors:** Yarin Udi, Tom Sharon-Shahak, Roee Masad, Dan Pri-Tal

**Published:** 2026-08-10 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.09266v1) | [PDF](https://arxiv.org/pdf/2608.09266v1.pdf)

<details>
<summary>Abstract</summary>

Medical world models commonly learn from multimodal recordings synchronized onto a fixed-rate grid. This preprocessing resamples each native stream onto a shared time axis. Each stream has an observation clock that governs when observations are emitted or updated. When this clock depends on the latent or acquisition state, it is endogenous. In such settings, synchronization may not be neutral and can erase task-relevant evidence before the model sees the data. We introduce a four-regime taxonomy...

</details>

---

### [Latent World Models with Monotone Planning Costs for Image-Goal Navigation](https://arxiv.org/abs/2608.09073v1)

**Authors:** Amirhosein Chahe, Siwei Cai, Lifeng Zhou

**Published:** 2026-08-10 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.09073v1) | [PDF](https://arxiv.org/pdf/2608.09073v1.pdf)

<details>
<summary>Abstract</summary>

Image-goal navigation with latent world models requires not only accurate future prediction, but also a planning cost that reliably ranks candidate action sequences. We define the cost as the cosine distance between the predicted future embedding and the goal embedding, and show that poor cost ordering can mislead sampling-based planners such as Cross-Entropy Method (CEM). To address this, we propose a latent world model built on a frozen DINO-family encoder and train it with two complementary o...

</details>

---

### [Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models](https://arxiv.org/abs/2608.08982v1)

**Authors:** Yu Ma, Hongli Shi, Xinran Xu

**Published:** 2026-08-10 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.08982v1) | [PDF](https://arxiv.org/pdf/2608.08982v1.pdf)

<details>
<summary>Abstract</summary>

Interactive video world models generate rollouts autoregressively under an action stream, yet they are trained and evaluated almost exclusively on factual prediction. We study counterfactual generation inside the rollout: given a trajectory the model has itself generated, what would have happened had the actions differed from step t* onward? We formalize noise-coupled twin rollouts --- a factual and a counterfactual branch sharing the generated prefix and the future exogenous noise sequence, div...

</details>

---
