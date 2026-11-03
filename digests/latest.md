# What's New

Papers discovered in the run at **2026-11-03 03:09 UTC**.

**New this run:** 19

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (1)

### [AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation](https://arxiv.org/abs/2611.00177)

**Authors:** Hao Xue, Peng-Fei Zhang, Ying Cheng, Lanyun Zhu, Lei Zhu et al. (6 authors)

**Published:** 2026-10-30 | **Categories:** cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "egocentric video" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.00177) | [PDF](https://arxiv.org/pdf/2611.00177)

<details>
<summary>Abstract</summary>

Egocentric observations provide a robot-centric view of manipulation processes, capturing contact interactions and object-state changes that are important for visuomotor policy learning but difficult to observe from external cameras. However, collecting such data at scale remains expensive due to additional hardware requirements and platform-specific deployment costs. Synthesizing egocentric observations from large-scale exocentric manipulation videos provides a scalable alternative. However, existing methods struggle to synthesize physically consistent and policy-relevant egocentric videos un...

</details>

<details>
<summary>Share</summary>

```
AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation

Egocentric observations provide a robot-centric view of manipulation processes, capturing contact interactions and object-state changes that are important for visuomotor policy learning but difficult to observe from e...

arXiv: https://arxiv.org/abs/2611.00177

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (10)

### [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)

**Authors:** Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang, Jinjing Zhao et al. (21 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01112) | [PDF](https://arxiv.org/pdf/2611.01112) | [Project Page](https://auriga.stelledge.com/) | [Code](https://github.com/lose4578/Auriga)

<details>
<summary>Abstract</summary>

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3% of this gap in zero-shot manipulation without target-task trials or resets. In Auriga, the model makes all task decisions over an explicit task belief and acts through either direc...

</details>

<details>
<summary>Share</summary>

```
Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies.

arXiv: https://arxiv.org/abs/2611.01112
Project page: https://auriga.stelledge.com/
Code: https://github.com/lose4578/Auriga

#VLA #robotics
```

</details>

---

### [Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2611.00896)

**Authors:** Rafiqul Islam

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00896) | [PDF](https://arxiv.org/pdf/2611.00896)

<details>
<summary>Abstract</summary>

Simulation-based VLA evaluation often treats matching task, seed, and episode identifiers as sufficient evidence that two policies faced identical test conditions. Under specific vectorized reset and autoreset conditions, different termination timing can change subsequent initial-state assignment, so the same episode index need not mean the same test state. We present an evaluation-integrity framework for paired comparison - invariants I1-I5, provenance logging, optional scene fingerprints, and an automated checker - and a controlled LeRobot 0.6.1 LIBERO harness study with emulated controllers...

</details>

<details>
<summary>Share</summary>

```
Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models

Simulation-based VLA evaluation often treats matching task, seed, and episode identifiers as sufficient evidence that two policies faced identical test conditions.

arXiv: https://arxiv.org/abs/2611.00896

#VLA #robotics
```

</details>

---

### [Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)

**Authors:** James Tcheng, Feiyu Gavin Zhu

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00522) | [PDF](https://arxiv.org/pdf/2611.00522)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is increasingly used to adapt pretrained vision-language-action models (VLAs). We investigate the problem of behavioral steering: adapting a VLA's execution style to preferences such as carrying objects higher. To investigate how little trainable capacity such steering requires and how much pretrained capability can be retained, we freeze an OpenVLA-OFT 7B policy and optimize TinyLoRA adapters with 8 to 384 trainable parameters using either policy-gradient RL (GRPO) or evolutionary search (CMA-ES). With just 256 trainable parameters, we raise carry height by 120 mm...

</details>

<details>
<summary>Share</summary>

```
Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime

Reinforcement learning (RL) is increasingly used to adapt pretrained vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.00522

#VLA #robotics
```

</details>

---

### [ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding](https://arxiv.org/abs/2611.01190)

**Authors:** Zilong Huang, Zipeng Ye, Caicheng Wang, Yuchen Xie, Jiaxiang Luo

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01190) | [PDF](https://arxiv.org/pdf/2611.01190) | [Project Page](https://clothdojo.github.io/)

<details>
<summary>Abstract</summary>

Garment flattening and folding require robots to identify garment structure during manipulation and adapt their actions as the cloth deforms. We present ClothDojo, a simulation platform that generates adaptive manipulation trajectories at scale across diverse garments and initial states and evaluates policies in closed loop. ClothDojo encodes each garment's canonical mesh coordinates as an NOCS texture, providing canonical surface-position cues through the visual interface of a pretrained vision-language-action model. We fine-tune the model on human demonstrations and corrections to obtain a d...

</details>

<details>
<summary>Share</summary>

```
ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding

Garment flattening and folding require robots to identify garment structure during manipulation and adapt their actions as the cloth deforms.

arXiv: https://arxiv.org/abs/2611.01190
Project page: https://clothdojo.github.io/

#VLA #robotics
```

</details>

---

### [CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision](https://arxiv.org/abs/2611.00394)

**Authors:** Boniface Chukwuemeka Godwin

**Published:** 2026-10-30 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00394) | [PDF](https://arxiv.org/pdf/2611.00394)

<details>
<summary>Abstract</summary>

Can a vision-language-action (VLA) policy signal likely task failure from its own action probabilities? We introduce CalVLA, which shapes native action-token confidence using successful and failed rollouts and an Action-Confidence Alignment (ACal) squared margin-ranking loss. Low-rank adapters update OpenVLA-7B without an auxiliary failure detector. Observations are paired within tasks at similar normalized elapsed times, not necessarily equivalent physical progress. On a held-out test split from 500 LIBERO-10 configurations, adapted confidence achieves a joint failure-discrimination AUROC of...

</details>

<details>
<summary>Share</summary>

```
CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision

Can a vision-language-action (VLA) policy signal likely task failure from its own action probabilities?

arXiv: https://arxiv.org/abs/2611.00394

#VLA #robotics
```

</details>

---

### [Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone](https://arxiv.org/abs/2611.01011)

**Authors:** Lin Yang, Yunjie Shen, Zheyu Li, Zhenjie Tian, Yongli Wang et al. (11 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01011) | [PDF](https://arxiv.org/pdf/2611.01011)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive control requires 20-50 Hz. We present a VLA that decouples the two: a VLM runs as a low-frequency semantic anchor whose cached context is reused across control steps, while a flow-matching action expert operates at high frequency, consuming the cached semantics with a fresh, low-latency visual stream from a compact encoder pretrained on robot video with masked reconstruction, opt...

</details>

<details>
<summary>Share</summary>

```
Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone

Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive...

arXiv: https://arxiv.org/abs/2611.01011

#VLA #robotics
```

</details>

---

### [Vision-Language Models Are Joint Denoisers in Robotic Action Generation](https://arxiv.org/abs/2611.01215)

**Authors:** Xicheng Gong, Wenxuan Song, Chengze Liu, Qiwei Li, Qize Yu et al. (8 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.01215) | [PDF](https://arxiv.org/pdf/2611.01215)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning. This separation limits how much pretrained perception and reasoning can guide action generation, especially in out-of-distribution settings. We introduce JADE, a Joint Action DEnoiser that enables the VLM and action expert to jointly refine actions. Our key insight is that structured action latents allow the VLM to read the current noisy action together with visual observations and language instructi...

</details>

<details>
<summary>Share</summary>

```
Vision-Language Models Are Joint Denoisers in Robotic Action Generation

Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning.

arXiv: https://arxiv.org/abs/2611.01215

#VLA #robotics
```

</details>

---

### [STEER: Route-Aware Adaptive Reasoning for Autonomous Driving](https://arxiv.org/abs/2611.00718)

**Authors:** Yangang Zou, Pei Liu, Nan Song, Bozhou Zhang, Mingyu Guo et al. (9 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00718) | [PDF](https://arxiv.org/pdf/2611.00718)

<details>
<summary>Abstract</summary>

Vision-language action (VLA) models excel for end-to-end autonomous driving, yet their tendency to over-invoke chain-of-thought (CoT) reasoning mirrors a human cognitive pitfall: overthinking. Just as deliberate reasoning can slow or mislead human judgment in routine tasks, excessive CoT in VLA incurs unnecessary compute overhead and can paradoxically degrade planning performance. Recent research tackles this via adaptive reasoning, which dynamically modulates inference complexity by selectively triggering CoT for complex scenes while responding directly to routine ones. While prior adaptive m...

</details>

<details>
<summary>Share</summary>

```
STEER: Route-Aware Adaptive Reasoning for Autonomous Driving

Vision-language action (VLA) models excel for end-to-end autonomous driving, yet their tendency to over-invoke chain-of-thought (CoT) reasoning mirrors a human cognitive pitfall: overthinking.

arXiv: https://arxiv.org/abs/2611.00718

#VLA #robotics
```

</details>

---

### [Learning from an Imitable Teacher: Competition Solution for the MetaFine Challenge](https://arxiv.org/abs/2611.00615)

**Authors:** Yanze Zhang, Hao Liu, Haochang Hao, Zhixiang Shen, Chunyu Miao et al. (6 authors)

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.00615) | [PDF](https://arxiv.org/pdf/2611.00615)

<details>
<summary>Abstract</summary>

The MetaFine Open Competition (RoboFineMani workshop, CoRL 2026) evaluates fine-grained manipulation beyond binary success. Its five simulated tasks, from grasping a bottle by an instructed part to inserting letter-shaped pegs with 4 mm clearance, are scored on perception under lighting and camera changes, instruction understanding, and behavior. This report presents Team Friday's solution, which got second place with an overall score of 0.947, more than twice the $π_0$ baseline. Instead of fine-tuning a large vision-language-action (VLA) model, we train one 19M-parameter policy per task with...

</details>

<details>
<summary>Share</summary>

```
Learning from an Imitable Teacher: Competition Solution for the MetaFine Challenge

The MetaFine Open Competition (RoboFineMani workshop, CoRL 2026) evaluates fine-grained manipulation beyond binary success.

arXiv: https://arxiv.org/abs/2611.00615

#VLA #robotics
```

</details>

---

### [PREM: Prediction-Regulated Memory for Robot Manipulation](https://arxiv.org/abs/2611.00634)

**Authors:** Xiao Huang, Ya Zhang, Weidi Xie

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.00634) | [PDF](https://arxiv.org/pdf/2611.00634)

<details>
<summary>Abstract</summary>

A robot's next action can depend on recent motion or earlier visual evidence absent from its current observation. A recurrent visual-memory architecture can retain this history in a visual state, but its usefulness depends on what the state represents and how it is updated with new observations. We introduce Prediction-Regulated Memory (PREM), a framework that uses action-conditioned future prediction to guide both memory learning and updating in vision-language-action policies. During training, predicting future visual features provides temporal supervision for memory learning. During executi...

</details>

<details>
<summary>Share</summary>

```
PREM: Prediction-Regulated Memory for Robot Manipulation

A robot's next action can depend on recent motion or earlier visual evidence absent from its current observation.

arXiv: https://arxiv.org/abs/2611.00634

#VLA #robotics
```

</details>

---

## World Models (8)

### [pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model](https://arxiv.org/abs/2611.01039)

**Authors:** Keivalya Pandya

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.01039) | [PDF](https://arxiv.org/pdf/2611.01039) | [Code](https://github.com/keivalya/pico-wam)

<details>
<summary>Abstract</summary>

When a World Action Model fails at control, is the bottleneck proposal generation or trajectory scoring? We introduce pico-WAM, a compact model with supplied physical state for tracing policy-dynamics interactions. Using 206 Push-T demonstrations and 15 training seeds, we compare data regimes and search configurations. Counterfactual branch training improves short-horizon cost ranking and enlarges the coverage advantage of policy-restarted over warm-started search by 4.8 percentage points; restart wins under both data regimes. Replacing learned trajectory scores with simulator costs improves c...

</details>

<details>
<summary>Share</summary>

```
pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model

When a World Action Model fails at control, is the bottleneck proposal generation or trajectory scoring?

arXiv: https://arxiv.org/abs/2611.01039
Code: https://github.com/keivalya/pico-wam

#worldmodels #robotics
```

</details>

---

### [TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](https://arxiv.org/abs/2611.00455)

**Authors:** Jiaxin Shi, Zibin Wu, Yichi Zhang, Jianghua Duan, Siyu Zhu et al. (6 authors)

**Published:** 2026-10-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.00455) | [PDF](https://arxiv.org/pdf/2611.00455) | [Project Page](https://tacmind-bench.github.io/)

<details>
<summary>Abstract</summary>

Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipulation. However, existing tactile manipulation studies are often developed and evaluated within specific task settings, making it difficult to systematically compare how tactile information contributes under different interaction conditions. In this work, we develop a benchmark in simulation comprising 128 tasks organized around three complementary evaluation regimes: Precise, Recognition, and Dynamic. The benchmark f...

</details>

<details>
<summary>Share</summary>

```
TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation

Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.00455
Project page: https://tacmind-bench.github.io/

#worldmodels #robotics
```

</details>

---

### [WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation](https://arxiv.org/abs/2611.00513)

**Authors:** Jiaming Wang

**Published:** 2026-10-31 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.00513) | [PDF](https://arxiv.org/pdf/2611.00513)

<details>
<summary>Abstract</summary>

Most agentic robotic systems use vision-language models (VLMs) either to orchestrate predefined skills or to directly generate actions, constraints, and control programs. The former is limited by the available skill library, while the latter requires VLMs to reason about precise geometry and contact. In this paper, we propose WorldSketch, a new paradigm for agentic robotics in which a VLM constructs a world model rather than generating robot actions. The VLM acts as an agent that actively queries perception tools to build and visually validate a minimal kinematic world model, capturing only ta...

</details>

<details>
<summary>Share</summary>

```
WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation

Most agentic robotic systems use vision-language models (VLMs) either to orchestrate predefined skills or to directly generate actions, constraints, and control programs.

arXiv: https://arxiv.org/abs/2611.00513

#worldmodels #robotics
```

</details>

---

### [Roz: A Taste Test for World Model Latents](https://arxiv.org/abs/2611.00612)

**Authors:** Kenneth Ge, Dhruv Sheth, Kunvar Thaman

**Published:** 2026-10-31 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.00612) | [PDF](https://arxiv.org/pdf/2611.00612)

<details>
<summary>Abstract</summary>

State of the art latent dynamics world models achieve impressive performance for robot planning. But do they actually encode the physics of the world? In this paper, we show that popular world models today achieve strong results on tasks that reduce to image similarity but forget key details about objects in the scene like mass, deformation, friction, and bounciness. We achieve this by defining precisely what ought to be encoded in such a world model and introducing two new evaluation methods that can directly tease physical properties and easily scale to new ones. Our evaluation, which we cal...

</details>

<details>
<summary>Share</summary>

```
Roz: A Taste Test for World Model Latents

State of the art latent dynamics world models achieve impressive performance for robot planning.

arXiv: https://arxiv.org/abs/2611.00612

#worldmodels #robotics
```

</details>

---

### [World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits](https://arxiv.org/abs/2611.01139)

**Authors:** Ahanaf Hasan Ariq, Hasaan Ahmad

**Published:** 2026-10-31 | **Categories:** cs.LG, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.01139) | [PDF](https://arxiv.org/pdf/2611.01139)

<details>
<summary>Abstract</summary>

Selecting a reinforcement-learning (RL) policy usually requires additional environment interaction, while learned world models offer cheap but potentially biased evaluations. This raises two distinct questions: can shared model errors preserve pairwise rankings despite poor absolute values, and do they make a small number of real audits more informative? We derive an exact pairwise simulation identity and a relative bound separating common-mode Bellman residuals from policy-specific error. The analysis motivates RAVEL (Relative Auditing of Value Errors in Learned models), a selective policy to...

</details>

<details>
<summary>Share</summary>

```
World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits

Selecting a reinforcement-learning (RL) policy usually requires additional environment interaction, while learned world models offer cheap but potentially biased evaluations.

arXiv: https://arxiv.org/abs/2611.01139

#worldmodels #robotics
```

</details>

---

### [X-World 1.6: Building Controllable Virtual Cities with World Models](https://arxiv.org/abs/2611.00596)

**Authors:** XPeng, :, Boyang Wang, Boyi Sun, Chaoda Zheng et al. (36 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.00596) | [PDF](https://arxiv.org/pdf/2611.00596)

<details>
<summary>Abstract</summary>

Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions. This report presents \emph{X-World~1.6}, advancing X-World~1.0 toward a more reliable and versatile driving simulator. The upgraded base model offers finer-grained control over traffic semantics, including traffic lights and road markings, together with improved spatial consistency across cameras. Virtual City capabilities broaden scenario construction through a family of models con...

</details>

<details>
<summary>Share</summary>

```
X-World 1.6: Building Controllable Virtual Cities with World Models

Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions.

arXiv: https://arxiv.org/abs/2611.00596

#worldmodels #robotics
```

</details>

---

### [Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel](https://arxiv.org/abs/2611.00427)

**Authors:** Kunal Bhosikar, Nicole Meng, Charu Sharma, Yingjie Lao

**Published:** 2026-10-30 | **Categories:** cs.CV, cs.CR, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.00427) | [PDF](https://arxiv.org/pdf/2611.00427)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) have recently emerged as general-purpose visual world models for control. A prominent example is LeWorldModel (LeWM), which trains end-to-end from pixels using an isotropic Gaussian anti-collapse regularizer (SIGReg) and plans by minimizing the squared Euclidean distance between predicted and goal embeddings. In this work, we investigate the test-time robustness of this latent planning interface. Analyzing the learned metric on Push-T, we first find that task-relevant object state heavily dominates latent distance: shifting the block by a single...

</details>

<details>
<summary>Share</summary>

```
Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel

Joint-embedding predictive architectures (JEPAs) have recently emerged as general-purpose visual world models for control.

arXiv: https://arxiv.org/abs/2611.00427

#worldmodels #robotics
```

</details>

---

### [GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](https://arxiv.org/abs/2611.01001)

**Authors:** Allan Grosvenor, Anton Zemlyansky, Abdul Wahab, Kyrylo Bohachov, Aras Dogan et al. (7 authors)

**Published:** 2026-10-31 | **Categories:** cs.AI, cs.CE, cs.MA | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.01001) | [PDF](https://arxiv.org/pdf/2611.01001)

<details>
<summary>Abstract</summary>

An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose, rank, and accelerate; a symbolic rules engine checks every consequential action against hard limits before it executes; and validated physics confirms and decides. GURU runs a workflow as a closed control loop, with Navigation, Action, and Planning agents sharing one Common Internal Language and one training factory....

</details>

<details>
<summary>Share</summary>

```
GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations

An AI can find a safe action faster than any human, but it must never decide what counts as safe.

arXiv: https://arxiv.org/abs/2611.01001

#worldmodels #robotics
```

</details>

---
