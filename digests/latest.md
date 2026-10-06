# What's New

Papers discovered in the run at **2026-10-06 20:47 UTC**.

**New this run:** 38

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (23)

### [When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models](https://arxiv.org/abs/2610.05719)

**Authors:** Seonghoon Yu, Dongwon Kim, HyungRok Jung, Yoonjae Baek, Byung-kwan Lee et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05719) | [PDF](https://arxiv.org/pdf/2610.05719) | [Code](https://github.com/Seonghoon-Yu/RACE-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models serve as unified policies for robotic manipulation, yet their expensive inference forces robots to pause between policy calls, resulting in stop-and-go execution that interrupts smooth motion and prolongs task completion. Extending the action chunk reduces policy calls and hence these pauses, but predicting farther into the future makes long-chunk execution unreliable. To understand where this unreliability arises, we analyze action errors within long chunks and find that they concentrate around transitions between manipulation subskills, growing sharply wit...

</details>

<details>
<summary>Share</summary>

```
When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models

Vision-Language-Action (VLA) models serve as unified policies for robotic manipulation, yet their expensive inference forces robots to pause between policy calls, resulting in stop-and-go execution that interrupts smo...

arXiv: https://arxiv.org/abs/2610.05719
Code: https://github.com/Seonghoon-Yu/RACE-VLA

#VLA #robotics
```

</details>

---

### [How (and How Not) to Use Data Augmentation in VLA Post-Training](https://arxiv.org/abs/2610.05994)

**Authors:** Bram Grooten, Joaquin Vanschoren

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05994) | [PDF](https://arxiv.org/pdf/2610.05994) | [Project Page](https://bramgrooten.nl/vla-augm/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models currently demonstrate strong performance in a wide range of real-world robotics tasks. However, they often still lack the generalization ability to handle large visual out-of-distribution shifts. Post-training of VLAs with reinforcement learning (RL) has been shown to benefit robustness, but significant room for improvement remains. In this work, we systematically study the effect of image augmentation on VLA post-training. We find that it is crucial to augment only the critic module during RL updates, while leaving the actor's input clean during both rollou...

</details>

<details>
<summary>Share</summary>

```
How (and How Not) to Use Data Augmentation in VLA Post-Training

Vision-language-action (VLA) models currently demonstrate strong performance in a wide range of real-world robotics tasks.

arXiv: https://arxiv.org/abs/2610.05994
Project page: https://bramgrooten.nl/vla-augm/

#VLA #robotics
```

</details>

---

### [Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization](https://arxiv.org/abs/2610.05230)

**Authors:** Yifan Li, Jiaxu Wang, Dongming Wu, Yicheng Jiang, Ryan Ji et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05230) | [PDF](https://arxiv.org/pdf/2610.05230) | [Project Page](https://clementine24.github.io/Vela/)

<details>
<summary>Abstract</summary>

Most vision-language-action models represent future motion as fixed-rate action chunks, tying temporal resolution and prediction horizon to a fixed output budget. This pointwise representation wastes capacity on highly correlated neighboring actions, leaves temporal continuity and smoothness to be learned implicitly, and forces a tradeoff between long-horizon coverage and the local precision required for contact-rich manipulation. To address these limitations, we introduce Vela, a vision-language-action foundation model that represents future robot behavior as continuous trajectories. Vela com...

</details>

<details>
<summary>Share</summary>

```
Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

Most vision-language-action models represent future motion as fixed-rate action chunks, tying temporal resolution and prediction horizon to a fixed output budget.

arXiv: https://arxiv.org/abs/2610.05230
Project page: https://clementine24.github.io/Vela/

#VLA #robotics
```

</details>

---

### [ExStereo: Lifting 2D Vision-Language-Action Models to 3D with Explicit Stereo Representations](https://arxiv.org/abs/2610.04805)

**Authors:** I-Chun Arthur Liu, Jason Chen, Gaurav S. Sukhatme, Daniel Seita

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04805) | [PDF](https://arxiv.org/pdf/2610.04805) | [Project Page](https://exstereo-vla.github.io/ExStereo/)

<details>
<summary>Abstract</summary>

Three-dimensional perception is critical for robotic manipulation, particularly for high-precision tasks, as recovering metric depth and precise 3D object positions from monocular RGB observations is inherently ill-posed. However, many Vision-Language-Action (VLA) models rely solely on RGB observations for perception. Leveraging recent advances in foundation models for stereo matching, we introduce ExStereo, a stereo module that augments pre-trained 2D VLAs with 3D perception. ExStereo reconstructs scene geometry from stereo image pairs and renders multi-view observations as an explicit stereo...

</details>

<details>
<summary>Share</summary>

```
ExStereo: Lifting 2D Vision-Language-Action Models to 3D with Explicit Stereo Representations

Three-dimensional perception is critical for robotic manipulation, particularly for high-precision tasks, as recovering metric depth and precise 3D object positions from monocular RGB observations is inherently ill-po...

arXiv: https://arxiv.org/abs/2610.04805
Project page: https://exstereo-vla.github.io/ExStereo/

#VLA #robotics
```

</details>

---

### [VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.06271)

**Authors:** Jaemin Kim, Jiahn Kim, Taesik Gong

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06271) | [PDF](https://arxiv.org/pdf/2610.06271)

<details>
<summary>Abstract</summary>

Adapting vision-language-action (VLA) models to deployment-time distribution shifts is important for reliable robotic operation, but conventional first-order adaptation can exceed the memory budget of inference-oriented deployment platforms. Zeroth-order (ZO) optimization offers a forward-only alternative with inference-level memory, but accurate gradient estimation requires many perturbation queries, making naive ZO prohibitively slow for large VLA models. We present VLA-ZO, a framework for fast ZO adaptation that exploits the structure of VLA computation. By confining adaptation to the actio...

</details>

<details>
<summary>Share</summary>

```
VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models

Adapting vision-language-action (VLA) models to deployment-time distribution shifts is important for reliable robotic operation, but conventional first-order adaptation can exceed the memory budget of inference-orient...

arXiv: https://arxiv.org/abs/2610.06271

#VLA #robotics
```

</details>

---

### [Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models](https://arxiv.org/abs/2610.06184)

**Authors:** Zaibin Zhang, Binghao Ran, Yuhan Wu, Zhongbo Zhang, Yifan Wang et al. (13 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06184) | [PDF](https://arxiv.org/pdf/2610.06184)

<details>
<summary>Abstract</summary>

Generalization in multi-arm collaboration can be studied as composing familiar atomic skills in new ways across arms. However, existing evaluations offer limited insight into which training and architectural choices support this ability under different coordination requirements. We introduce \textbf{ACG-Bench}, a benchmark for \emph{Arm-wise Compositional Generalization} that provides a common testbed for studying skill recomposition in dual-arm policies. It contains 23 task--condition pairs across 8 task families, with 6 in-domain conditions and 17 unseen compositions covering reordering, syn...

</details>

<details>
<summary>Share</summary>

```
Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models

Generalization in multi-arm collaboration can be studied as composing familiar atomic skills in new ways across arms.

arXiv: https://arxiv.org/abs/2610.06184

#VLA #robotics
```

</details>

---

### [What the Guard Misses, the Robot Executes: Implied Harm in VLA Instructions](https://arxiv.org/abs/2610.05818)

**Authors:** Sripad Karne, Arjun Balaji

**Published:** 2026-10-05 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05818) | [PDF](https://arxiv.org/pdf/2610.05818)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) act on instructions without being able to refuse, so screening harmful requests falls to monitors. We test whether these monitors catch ordinary robot tasks requested for harmful reasons, holding the task fixed while varying only how explicitly the intent is stated. $π_{0.5}$ completes the task at every level of explicitness, as often as for harmless controls. Text guards flag nearly every blunt request but few implied ones: up to 95% of implied-harm runs end with the task done and no flag raised, and up to 90% even after recalibrating on robot instructions...

</details>

<details>
<summary>Share</summary>

```
What the Guard Misses, the Robot Executes: Implied Harm in VLA Instructions

Vision-language-action models (VLAs) act on instructions without being able to refuse, so screening harmful requests falls to monitors.

arXiv: https://arxiv.org/abs/2610.05818

#VLA #robotics
```

</details>

---

### [Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning](https://arxiv.org/abs/2610.05745)

**Authors:** Shen Ruan, Wenchang Gao, Jin Wang, Siao Liu, Zhoxizhuoma et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05745) | [PDF](https://arxiv.org/pdf/2610.05745) | [Code](https://github.com/ruanruan-andy/PIVOT-Q)

<details>
<summary>Abstract</summary>

Post-training quantization has been shown to preserve VLA performance under standard evaluation conditions, but whether it preserves the full-precision model's robustness and generalization remains underexplored. In this study, we systematically study the robustness and generalization of post-quantized VLA policies under environmental disturbances. Empirical results show that quantized policies can become fragile to subtle environmental variations despite retaining comparable in-distribution performance. We further observe that action discrepancies are concentrated in a small subset of rollout...

</details>

<details>
<summary>Share</summary>

```
Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning

Post-training quantization has been shown to preserve VLA performance under standard evaluation conditions, but whether it preserves the full-precision model's robustness and generalization remains underexplored.

arXiv: https://arxiv.org/abs/2610.05745
Code: https://github.com/ruanruan-andy/PIVOT-Q

#VLA #robotics
```

</details>

---

### [GeoBridge-VLA: Geometry-Aware Residual Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.05026)

**Authors:** Hyun Song, Kangmin Kim, Loren Jinsoo Um, Minhui Han, Jaehyeok Park et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05026) | [PDF](https://arxiv.org/pdf/2610.05026)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models encode semantic information from vision-language pretraining, but manipulation also requires precise spatial reasoning. We present GeoBridge-VLA, a two-stage method for learning geometric features from a pretrained VLA's frozen visual encoder and using them for action prediction. Stage I trains a feature bridge and geometry decoder with depth supervision. Stage II freezes these modules and trains a gated residual interface together with the action-side projections and action expert. The residual augments the existing visual tokens without adding a second ima...

</details>

<details>
<summary>Share</summary>

```
GeoBridge-VLA: Geometry-Aware Residual Adaptation for Vision-Language-Action Models

Vision-language-action (VLA) models encode semantic information from vision-language pretraining, but manipulation also requires precise spatial reasoning.

arXiv: https://arxiv.org/abs/2610.05026

#VLA #robotics
```

</details>

---

### [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2610.05492)

**Authors:** Zixuan Liu, Joris Köster, Zizhan Zheng, Siavash Khajavi

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05492) | [PDF](https://arxiv.org/pdf/2610.05492)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong potential as generalist robot policies, but adapting them to unseen tasks often requires costly parameter updates. Recent work such as RICL introduces in-context adaptability by retrieving expert demonstrations based on the current VLA observation and providing them as additional context at test time. The effectiveness of this adaptation therefore depends critically on the retrieval mechanism. In this work, we systematically study how different retrieval methods affect both retrieval quality and task performance within the RICL framework. S...

</details>

<details>
<summary>Share</summary>

```
When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

Vision-language-action (VLA) models have shown strong potential as generalist robot policies, but adapting them to unseen tasks often requires costly parameter updates.

arXiv: https://arxiv.org/abs/2610.05492

#VLA #robotics
```

</details>

---

### [OGAM: Connecting Systematic Testing to Runtime Assurance through Object-Grounded Attention Monitoring for VLA Policies](https://arxiv.org/abs/2610.05878)

**Authors:** Haki Darwish, Xiangyu Yin, Changwen Li, Rongjie Yan, Francisco Gomes de Oliveira Neto et al. (6 authors)

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05878) | [PDF](https://arxiv.org/pdf/2610.05878)

<details>
<summary>Abstract</summary>

Benchmarks expose vision-language-action (VLA) policies to few canonical instructions, while exhaustive deployment testing is impossible. We introduce Object-Grounded Attention Monitoring (OGAM), connecting systematic testing to runtime assurance: testing reveals attention divergence between successful and failed executions, and OGAM uses this signal to stop failures beyond the finite suite. We generate scene-grounded instructions through pairwise combinations of action templates and objects, and separately test meaning-preserving paraphrases. All 87 out-of-benchmark cases reveal problematic b...

</details>

<details>
<summary>Share</summary>

```
OGAM: Connecting Systematic Testing to Runtime Assurance through Object-Grounded Attention Monitoring for VLA Policies

Benchmarks expose vision-language-action (VLA) policies to few canonical instructions, while exhaustive deployment testing is impossible.

arXiv: https://arxiv.org/abs/2610.05878

#VLA #robotics
```

</details>

---

### [EvoMem-VLA: State-Evolution Memory for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.05418)

**Authors:** Yuheng Na, Zhide Zhong, Junjie He, Junfeng Li, Haodong Yan et al. (10 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05418) | [PDF](https://arxiv.org/pdf/2610.05418)

<details>
<summary>Abstract</summary>

Most vision-language-action (VLA) models rely on current observations and lose task-relevant evidence once it leaves view, limiting performance on long-horizon, memory-dependent tasks. Existing efforts incorporate compressed historical features or sparse visual keyframes. However, isolated snapshots can leave the policy uncertain about what changed during past interactions and which action should follow. To overcome this limitation, we propose EvoMem-VLA, which constructs state-evolution memory by explicitly encoding and retaining observed changes between historical states. These change repres...

</details>

<details>
<summary>Share</summary>

```
EvoMem-VLA: State-Evolution Memory for Long-Horizon Robot Manipulation

Most vision-language-action (VLA) models rely on current observations and lose task-relevant evidence once it leaves view, limiting performance on long-horizon, memory-dependent tasks.

arXiv: https://arxiv.org/abs/2610.05418

#VLA #robotics
```

</details>

---

### [When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA](https://arxiv.org/abs/2610.05273)

**Authors:** Tianjun Shi, Haotian Xiong, Ziyu Gong, Qi Lu, Li Li

**Published:** 2026-10-04 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05273) | [PDF](https://arxiv.org/pdf/2610.05273)

<details>
<summary>Abstract</summary>

Visual token pruning is an effective way to accelerate vision-language models and is especially useful for vision-language-action (VLA) inference, where many visual tokens must be processed before predicting robot actions. Existing pruning methods usually estimate which tokens can be pruned based on attention scores or feature diversity, retaining tokens that are either highly attended or visually different from others. However, most of them use fixed pruning schedules, such as pruning once at a preset layer or pruning at uniformly spaced layers. Such schedules can be risky for VLA models, bec...

</details>

<details>
<summary>Share</summary>

```
When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA

Visual token pruning is an effective way to accelerate vision-language models and is especially useful for vision-language-action (VLA) inference, where many visual tokens must be processed before predicting robot act...

arXiv: https://arxiv.org/abs/2610.05273

#VLA #robotics
```

</details>

---

### [A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies](https://arxiv.org/abs/2610.05166)

**Authors:** Tu Nguyen, Matthieu Zimmer, Vu Anh Vu, Ziyi Wang, Jannik Hammel Nielsen et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05166) | [PDF](https://arxiv.org/pdf/2610.05166)

<details>
<summary>Abstract</summary>

A safe action is not necessarily a viable one. Under a frozen vision-language-action (VLA) policy, an action can be likely and locally admissible yet leave no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the current action, whereas feasibility depends on the futures that remain after it. We derive the exact next-block marginal of the history-conditioned policy-environment trajectory law restricted to safe task completion. The derivation exposes a candidate-dependent feasible-future mass with two roles: its support records whether...

</details>

<details>
<summary>Share</summary>

```
A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies

A safe action is not necessarily a viable one.

arXiv: https://arxiv.org/abs/2610.05166

#VLA #robotics
```

</details>

---

### [Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design](https://arxiv.org/abs/2610.05062)

**Authors:** Seonghun Jung, Sieun Moon, Jiyoung Jeong, Jimin Lee, Jaehyuk Huh

**Published:** 2026-10-04 | **Categories:** cs.AR, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05062) | [PDF](https://arxiv.org/pdf/2610.05062)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models translate multimodal observations into low-level robot actions. During robot operation, each control period sets an inference deadline, and overruns leave the robot acting on stale observations, reducing task success. Meeting this deadline motivates on-device or nearby edge execution, where a single robot requires batch-1 inference outside the design point of LLM serving systems. Although VLA architectures combine familiar vision-language, autoregressive, and diffusion-style components, their runtime behavior in this batch-1 control setting remains uncharact...

</details>

<details>
<summary>Share</summary>

```
Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design

Vision-language-action (VLA) models translate multimodal observations into low-level robot actions.

arXiv: https://arxiv.org/abs/2610.05062

#VLA #robotics
```

</details>

---

### [DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling](https://arxiv.org/abs/2610.04933)

**Authors:** Seongheon Park, Heecheol Kim, Shulin Tian, Lilika Makabe, Namiko Saito et al. (8 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.04933) | [PDF](https://arxiv.org/pdf/2610.04933)

<details>
<summary>Abstract</summary>

Scaling robot data and model capacity has improved Vision-Language-Action (VLA) policies, but further progress is constrained by the high cost of robotic data. Verifier-guided test-time scaling offers an efficient alternative by sampling multiple action candidates and selecting the one most likely to lead to task success at inference time. Existing classification-based verifiers learn from trajectory-level outcomes but treat all visited states equally, even though their value for candidate discrimination can vary across a trajectory. At many states, plausible actions are similar and provide li...

</details>

<details>
<summary>Share</summary>

```
DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling

Scaling robot data and model capacity has improved Vision-Language-Action (VLA) policies, but further progress is constrained by the high cost of robotic data.

arXiv: https://arxiv.org/abs/2610.04933

#VLA #robotics
```

</details>

---

### [Wiring Matters: Injection Topology and Initialization of Affordance Heads in Vision-Language-Action Policies](https://arxiv.org/abs/2610.06318)

**Authors:** Zijian An, Linhan Wang, Jiayan Wang, Shijie Geng, Ran Yang et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06318) | [PDF](https://arxiv.org/pdf/2610.06318)

<details>
<summary>Abstract</summary>

Dense affordance supervision is an appealing auxiliary signal for vision-language-action (VLA) policies, yet naively co-training an affordance head can severely damage instruction following. We present a controlled study of how to wire such a head into a modern VLA on the LIBERO benchmark. Our recipe reads the backbone through a stop-gradient and re-injects an intermediate head feature into the action expert via a learned bridge. The stop-gradient is a precondition: letting affordance gradients reach the backbone drops the policy below the headless base (85.5% vs. 93.1%). With the backbone pro...

</details>

<details>
<summary>Share</summary>

```
Wiring Matters: Injection Topology and Initialization of Affordance Heads in Vision-Language-Action Policies

Dense affordance supervision is an appealing auxiliary signal for vision-language-action (VLA) policies, yet naively co-training an affordance head can severely damage instruction following.

arXiv: https://arxiv.org/abs/2610.06318

#VLA #robotics
```

</details>

---

### [Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA](https://arxiv.org/abs/2610.05025)

**Authors:** Hyemin Yang, Wooseong Jeong, Giwon Lee, Kuk-Jin Yoon

**Published:** 2026-10-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05025) | [PDF](https://arxiv.org/pdf/2610.05025)

<details>
<summary>Abstract</summary>

Dual-system Vision-Language-Action (VLA) models improve real-time robotic control by pairing a slow, reasoning-capable generalist with a fast specialist action expert. However, existing methods invoke the generalist at a fixed frequency, ignoring the fact that decision-making complexity varies throughout a rollout. This static strategy wastes computation in easy phases and can delay renewed reasoning when the scene changes unexpectedly. We propose TUD (Triggering generalist reasoning via predictive Uncertainty for Dual-system VLA), an adaptive inference framework that selectively skips unneces...

</details>

<details>
<summary>Share</summary>

```
Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA

Dual-system Vision-Language-Action (VLA) models improve real-time robotic control by pairing a slow, reasoning-capable generalist with a fast specialist action expert.

arXiv: https://arxiv.org/abs/2610.05025

#VLA #robotics
```

</details>

---

### [Recursive Video In-Context Learning for Agentic Robot](https://arxiv.org/abs/2610.06843)

**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, Yuzhang Shang

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06843) | [PDF](https://arxiv.org/pdf/2610.06843)

<details>
<summary>Abstract</summary>

LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration video shows it, but fits poorly into an agent's context. The full video slows every turn, fixed keyframes lose the contact detail that decides whether a grasp holds, and what the agent needs shifts from the task's structure while planning to the frames around each contact. We introduce Recursive Video In-Context Learning (RV-ICL), a training-free method that turns a demonstration into a hierarchy the...

</details>

<details>
<summary>Share</summary>

```
Recursive Video In-Context Learning for Agentic Robot

LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done.

arXiv: https://arxiv.org/abs/2610.06843

#VLA #robotics
```

</details>

---

### [Odyssey: A Closed-Loop Benchmark for Long-Horizon Real-World Driving with Explicit Navigation Routes](https://arxiv.org/abs/2610.06469)

**Authors:** Jungho Kim, Hongjae Shin, Seunghoon Yu, Heecheol Yoo, Myeongjun Kim et al. (14 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06469) | [PDF](https://arxiv.org/pdf/2610.06469)

<details>
<summary>Abstract</summary>

Closed-loop evaluation of end-to-end driving requires continuous rollouts that reveal how earlier decisions affect subsequent driving. However, existing benchmarks evaluate only short segments and fail to capture later consequences. Ambiguous directional commands also obscure the intended navigation objective. We introduce Odyssey, a closed-loop benchmark for long-horizon driving comprising 100 scenarios, each reconstructed from a 100-second nuPlan driving log to preserve the context of navigation maneuvers and traffic interactions. To provide a consistent navigation objective, Odyssey replace...

</details>

<details>
<summary>Share</summary>

```
Odyssey: A Closed-Loop Benchmark for Long-Horizon Real-World Driving with Explicit Navigation Routes

Closed-loop evaluation of end-to-end driving requires continuous rollouts that reveal how earlier decisions affect subsequent driving.

arXiv: https://arxiv.org/abs/2610.06469

#VLA #robotics
```

</details>

---

### [Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies](https://arxiv.org/abs/2610.06235)

**Authors:** Shaohan Jiang, Jiahang Cao, Qiduo He, Fengting Deng, Kun Wu et al. (12 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06235) | [PDF](https://arxiv.org/pdf/2610.06235)

<details>
<summary>Abstract</summary>

Instruction following is central to language-conditioned robot policies: language should determine what to do when the same scene permits multiple valid actions. Yet successful execution alone cannot establish whether a policy follows the instruction or infers the task from the scene. We study this ambiguity through scene-preserving instruction interventions, using valid target substitutions, arbitrary nouns, and unrelated sentences while holding the scene fixed. We evaluate vision-language-action (VLA) policies and world-action models (WAMs) in simulation and in real-world experiments. Our an...

</details>

<details>
<summary>Share</summary>

```
Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies

Instruction following is central to language-conditioned robot policies: language should determine what to do when the same scene permits multiple valid actions.

arXiv: https://arxiv.org/abs/2610.06235

#VLA #robotics
```

</details>

---

### [Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?](https://arxiv.org/abs/2610.06078)

**Authors:** Xinnuo Xu

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06078) | [PDF](https://arxiv.org/pdf/2610.06078)

<details>
<summary>Abstract</summary>

This paper asks whether VLA generalization is grounded in a global understanding of objects' physical properties that enables policies to adapt their motion to unseen setups, or if policies simply replay the motions they've learnt that happen to succeed in new setups. The former reflects genuine generalization; the latter reflects incidental robustness. We first examine awareness of physical properties in seven VLAs by applying linear probing and representational similarity analysis (RSA) to their activations. We find that physical properties, including mass, fragility, deformability, friction...

</details>

<details>
<summary>Share</summary>

```
Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?

This paper asks whether VLA generalization is grounded in a global understanding of objects' physical properties that enables policies to adapt their motion to unseen setups, or if policies simply replay the motions t...

arXiv: https://arxiv.org/abs/2610.06078

#VLA #robotics
```

</details>

---

### [Demonstration-Calibrated Port-Hamiltonian Retuning for Manipulation Policies](https://arxiv.org/abs/2610.05755)

**Authors:** Yulong Yang, Fan Wu, Christine Allen-Blanchette, Amit Chakraborty

**Published:** 2026-10-05 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05755) | [PDF](https://arxiv.org/pdf/2610.05755)

<details>
<summary>Abstract</summary>

Diffusion and VLA policies for manipulation are often deployed through downstream impedance controllers. The stiffness and damping gains of these controllers affect task success, yet are commonly inherited from data collection rather than selected for the deployed policy. Although empirical gain sweeps can improve performance, they require repeated evaluation rollouts. We introduce PHRetune, an offline method that derives controller gains for a frozen policy without evaluation rollouts or gain search. Our approach learns a port-Hamiltonian model from demonstrations to estimate the effort and e...

</details>

<details>
<summary>Share</summary>

```
Demonstration-Calibrated Port-Hamiltonian Retuning for Manipulation Policies

Diffusion and VLA policies for manipulation are often deployed through downstream impedance controllers.

arXiv: https://arxiv.org/abs/2610.05755

#VLA #robotics
```

</details>

---

## World Models (15)

### [PWM: Personalized World Models with Online Reinforcement Learning](https://arxiv.org/abs/2610.04920)

**Authors:** Zhexin Lou, Guancheng Lu, Zeyu Zhang, Yi Zhang, Yang Zhao et al. (6 authors)

**Published:** 2026-10-04 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04920) | [PDF](https://arxiv.org/pdf/2610.04920) | [Project Page](https://aigeeksgroup.github.io/PWM) | [Code](https://github.com/AIGeeksGroup/PWM)

<details>
<summary>Abstract</summary>

Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video. This requires learning the scene's visual identity while retaining the quality of action-conditioned generation. We introduce Personalized World Models (PWM), a framework for customizing interactive world models from short scene videos through online reinforcement learning. In PWM, the support trajectory and its associated controls provide reward feedback on continuations sampled from the current policy. In the GRPO instantiation, group-relative optimizati...

</details>

<details>
<summary>Share</summary>

```
PWM: Personalized World Models with Online Reinforcement Learning

Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video.

arXiv: https://arxiv.org/abs/2610.04920
Project page: https://aigeeksgroup.github.io/PWM
Code: https://github.com/AIGeeksGroup/PWM

#worldmodels #robotics
```

</details>

---

### [SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](https://arxiv.org/abs/2610.06598)

**Authors:** Xiaodong Wang, Tianle Li, Chuanxin Song, Junliang Xie, Zhanmi Zhong et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; code repo; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06598) | [PDF](https://arxiv.org/pdf/2610.06598) | [Code](https://github.com/Wang-Xiaodong1899/SimForcing)

<details>
<summary>Abstract</summary>

Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation. We present SimForcing, a simulation-guided framework that uses simulation both as a source of transferable motion knowledge and as a controllable reference for prediction. First, we transfer motion knowledge from a simulation te...

</details>

<details>
<summary>Share</summary>

```
SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging.

arXiv: https://arxiv.org/abs/2610.06598
Code: https://github.com/Wang-Xiaodong1899/SimForcing

#worldmodels #robotics
```

</details>

---

### [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805)

**Authors:** Wancong Zhang, Basile Terver, Michael Rabbat, Yann LeCun, Randall Balestriero

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06805) | [PDF](https://arxiv.org/pdf/2610.06805)

<details>
<summary>Abstract</summary>

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and each level's predictions become subgoals for the planner below it. When factors in the data evolve at...

</details>

<details>
<summary>Share</summary>

```
H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction.

arXiv: https://arxiv.org/abs/2610.06805

#worldmodels #robotics
```

</details>

---

### [KineWorld: Action-Induced Transport Fields for Embodied World Modeling](https://arxiv.org/abs/2610.06349)

**Authors:** Ziying Song, Yuchen Liu, Zhuoran Xu, Ziyang Liu, Jian Jin et al. (9 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06349) | [PDF](https://arxiv.org/pdf/2610.06349) | [Project Page](https://modaxiansheng.github.io/KineWorld/)

<details>
<summary>Abstract</summary>

Embodied world models predict the visual consequences of candidate actions before execution. However, existing action-conditioned world models often adopt uniformly weighted visual generation objectives that can be misaligned with embodied prediction needs. Even with explicit motion conditioning, these objectives can underemphasize spatially sparse changes that are critical to interaction. We propose KineWorld, a transport-aware world-modeling framework that extends robot kinematics from motion conditioning to the spatial allocation of generative supervision. Kinematic Transport Lifting (KTL)...

</details>

<details>
<summary>Share</summary>

```
KineWorld: Action-Induced Transport Fields for Embodied World Modeling

Embodied world models predict the visual consequences of candidate actions before execution.

arXiv: https://arxiv.org/abs/2610.06349
Project page: https://modaxiansheng.github.io/KineWorld/

#worldmodels #robotics
```

</details>

---

### [Tackling Sim-to-Real Mismatch Through Sampling-Based Disturbance Observers: From Analytical Models to Learned World Models](https://arxiv.org/abs/2610.04896)

**Authors:** Tianqi Zhu, Jun Yang, Jianliang Mao, Cong Li, Shihua Li

**Published:** 2026-10-04 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04896) | [PDF](https://arxiv.org/pdf/2610.04896) | [Project Page](https://sampling-based-dob.github.io/)

<details>
<summary>Abstract</summary>

Robotic controllers increasingly rely on analytical models, simulators, cost-query interfaces, and learned world models. However, physical deployment can deviate from nominal assumptions, and additional disturbances may arise even when the model itself is accurate. In control systems, disturbance observers (DOB) are widely used to estimate such unmeasured effects from nominal models and measured feedback. Classical DOB formulations are generally built around explicit plant models. This paper develops the sampling-based disturbance observer (SDOB), extending the DOB principle to a broader range...

</details>

<details>
<summary>Share</summary>

```
Tackling Sim-to-Real Mismatch Through Sampling-Based Disturbance Observers: From Analytical Models to Learned World Models

Robotic controllers increasingly rely on analytical models, simulators, cost-query interfaces, and learned world models.

arXiv: https://arxiv.org/abs/2610.04896
Project page: https://sampling-based-dob.github.io/

#worldmodels #robotics
```

</details>

---

### [Flow Policies as Actions of Skill-Level World Models: Learned and Symbolic Abstractions for Long-Horizon Planning](https://arxiv.org/abs/2610.04767)

**Authors:** Andreu Matoses Gimenez, Andrei-Carlo Papuc, Chris Pek, Javier Alonso-Mora

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04767) | [PDF](https://arxiv.org/pdf/2610.04767) | [Project Page](https://andreumatoses.github.io/research/flow-skill-wm)

<details>
<summary>Abstract</summary>

Latent world models enable robots to plan by predicting the consequences of actions. Planning long tasks with control-rate actions requires many prediction steps, which enlarges the search space and accumulates error. Skill-level actions shorten these sequences, but a symbolic skill vocabulary requires domain knowledge and labeled demonstrations. We construct skill-level actions from the inputs of a flow-matching policy trained on demonstrations segmented into complete skills. The policy maps a noise seed and an observation, optionally with a code or label, to a complete skill execution, so on...

</details>

<details>
<summary>Share</summary>

```
Flow Policies as Actions of Skill-Level World Models: Learned and Symbolic Abstractions for Long-Horizon Planning

Latent world models enable robots to plan by predicting the consequences of actions.

arXiv: https://arxiv.org/abs/2610.04767
Project page: https://andreumatoses.github.io/research/flow-skill-wm

#worldmodels #robotics
```

</details>

---

### [Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training](https://arxiv.org/abs/2610.05861)

**Authors:** Yongxin Ning, Runliang Niu, Qianli Xing, Zhiyi Duan, Qingzu He et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.05861) | [PDF](https://arxiv.org/pdf/2610.05861) | [Code](https://github.com/swaydy-n/Infinite-Dreamer)

<details>
<summary>Abstract</summary>

Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications. However, training highly capable and generalizable agents fundamentally relies on massive, high-fidelity visual-action trajectories, which are notoriously difficult to acquire. While human demonstrations are unscalable, existing GUI world models rely on text descriptions or HTML rendering, discarding crucial pixel-level visual details like icons and layout styles. To address this issue, we introduce Infinite-Dreamer, a simulation-free data synthesis m...

</details>

<details>
<summary>Share</summary>

```
Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training

Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications.

arXiv: https://arxiv.org/abs/2610.05861
Code: https://github.com/swaydy-n/Infinite-Dreamer

#worldmodels #robotics
```

</details>

---

### [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)

**Authors:** Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, Yichen Feng, Yaorui Ding et al. (11 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.06814) | [PDF](https://arxiv.org/pdf/2610.06814) | [Project Page](https://tapdreamer.github.io)

<details>
<summary>Abstract</summary>

World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action models that instead uses a public encoder alone to construct a fixed local perturbation that transfer...

</details>

<details>
<summary>Share</summary>

```
TAPDreamer: Transferable Adversarial Patches for World Action Models

World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control.

arXiv: https://arxiv.org/abs/2610.06814
Project page: https://tapdreamer.github.io

#worldmodels #robotics
```

</details>

---

### [EpicWorldModel: Exploration-driven Planning with Latent World Models](https://arxiv.org/abs/2610.05996)

**Authors:** Bowen Feng, Julian Ost, May Mei, Anirudha Majumdar, Felix Heide

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05996) | [PDF](https://arxiv.org/pdf/2610.05996)

<details>
<summary>Abstract</summary>

Latent world models based on Joint-Embedding Predictive Architecture (JEPA) are deterministic by design. While successful in fully observable scenarios, this paradigm breaks down when past observations and actions lead to multiple plausible future possibilities, e.g., due to occlusion. We introduce EpicWorldModel, a framework to train stochastic JEPAs for environments and tasks with inherent uncertainty under partially observability. We jointly train the EpicWorldModel predictor with its latent representation space to directly predict multiple potential future states using a flow-matching obje...

</details>

<details>
<summary>Share</summary>

```
EpicWorldModel: Exploration-driven Planning with Latent World Models

Latent world models based on Joint-Embedding Predictive Architecture (JEPA) are deterministic by design.

arXiv: https://arxiv.org/abs/2610.05996

#worldmodels #robotics
```

</details>

---

### [When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models](https://arxiv.org/abs/2610.05550)

**Authors:** Rui Min, Xianyao Li, Fang Xu, Jing Du

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05550) | [PDF](https://arxiv.org/pdf/2610.05550)

<details>
<summary>Abstract</summary>

The component that dominates a latent world model's prediction error need not be the one whose repair most improves action selection. We show this by comparing action sequences from identical physical starts and separating endpoint error into a candidate-pool center and action-relative responses. Across four model families and four tasks, a confirmation pool of 256 new starts per task and 300 shared candidates per start shows that center error dominates MSE in 14/16 model-task cells. Yet in six of these cells, an oracle that corrects only the action-relative responses yields better physical ra...

</details>

<details>
<summary>Share</summary>

```
When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models

The component that dominates a latent world model's prediction error need not be the one whose repair most improves action selection.

arXiv: https://arxiv.org/abs/2610.05550

#worldmodels #robotics
```

</details>

---

### [How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models](https://arxiv.org/abs/2610.04988)

**Authors:** Lama Moukheiber, Haotian Xue, Yongxin Chen

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.04988) | [PDF](https://arxiv.org/pdf/2610.04988)

<details>
<summary>Abstract</summary>

Latent world models plan by rolling a frozen predictor forward under candidate action sequences and ranking the candidates by the latent distance between their imagined end state and the goal. However, this ranking breaks down when the goal lies several plans away, because the latent distance measures how closely an end state resembles the goal rather than how far it remains from reaching it. To address this, we propose TEMPO, a temporal-distance planning objective that leaves the world model untouched, learns only from the demonstrations already used to train it, and adds negligible cost to t...

</details>

<details>
<summary>Share</summary>

```
How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models

Latent world models plan by rolling a frozen predictor forward under candidate action sequences and ranking the candidates by the latent distance between their imagined end state and the goal.

arXiv: https://arxiv.org/abs/2610.04988

#worldmodels #robotics
```

</details>

---

### [FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning](https://arxiv.org/abs/2610.05483)

**Authors:** R. Khorrambakht, Joseph Amigo, Félix Lebel, Leon Seetoo, Jean Ponce et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.05483) | [PDF](https://arxiv.org/pdf/2610.05483)

<details>
<summary>Abstract</summary>

World--action models (WAMs) promise a unified model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination. However, existing joint video--action models often use computationally heavy, fixed-horizon backbones ill-suited to streaming inference and stable long-horizon open-loop rollouts. We introduce FLEX-WAM, a Flexible and Efficient Block-Causal World--Action Model for unified simulation and policy inference. FLEX-WAM supports variable-length contexts and non-causal prediction horizons, as well as infinite autoregressive generation frame by...

</details>

<details>
<summary>Share</summary>

```
FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning

World--action models (WAMs) promise a unified model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination.

arXiv: https://arxiv.org/abs/2610.05483

#worldmodels #robotics
```

</details>

---

### [PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation](https://arxiv.org/abs/2610.04916)

**Authors:** Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Junwei Yang et al. (7 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.04916) | [PDF](https://arxiv.org/pdf/2610.04916)

<details>
<summary>Abstract</summary>

Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations. However, existing agentic navigation methods often struggle to translate distant goals into coherent local decisions in large-scale physical environments. Their reliance on linguistic reasoning over transient observations or limited history constrains anticipation of the consequences of actions and future conditions, despite the importance of such foresight for navigating long and complex urban routes. To bridge this gap, we propose PreAct-Nav, an agentic navigation...

</details>

<details>
<summary>Share</summary>

```
PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation

Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations.

arXiv: https://arxiv.org/abs/2610.04916

#worldmodels #robotics
```

</details>

---

### [Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control](https://arxiv.org/abs/2610.06582)

**Authors:** Shengtao Wen, Xiang Chen, Yu Tian, Lingbing Guo, Lina Gong et al. (6 authors)

**Published:** 2026-10-05 | **Categories:** cs.AI, cs.CL, cs.IR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06582) | [PDF](https://arxiv.org/pdf/2610.06582)

<details>
<summary>Abstract</summary>

World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator buffering. We study how asynchronous execution changes the action semantics assumed within world-model controllers, rather than treating it only as an external control disturbance. Through controlled interventions, we identify two architecture-dependent failure modes: planning-based controllers such as TD-MPC2 suffer from a future-action timeline mismatch between imagined and exe...

</details>

<details>
<summary>Share</summary>

```
Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control

World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator...

arXiv: https://arxiv.org/abs/2610.06582

#worldmodels #robotics
```

</details>

---

### [Generative World Models Enable Predictive Control of Laser Melt Pool Dynamics](https://arxiv.org/abs/2610.06250)

**Authors:** Yiyang Yan, Markus Bambach, Mohamadreza Afrasiabi

**Published:** 2026-10-05 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.06250) | [PDF](https://arxiv.org/pdf/2610.06250)

<details>
<summary>Abstract</summary>

World models, which learn how environments respond to actions, are emerging as a powerful paradigm for planning through imagined futures, transforming decision-making across games, robotics and autonomous driving. Bringing this capability to manufacturing could enable process decisions on timescales inaccessible to high-fidelity simulation. Here we introduce a generative world model for localized highly dynamic laser melt pool that predicts evolution from histories of temperature and phase morphology under candidate actions. Its generative latent dynamics capture the effects of unresolved melt...

</details>

<details>
<summary>Share</summary>

```
Generative World Models Enable Predictive Control of Laser Melt Pool Dynamics

World models, which learn how environments respond to actions, are emerging as a powerful paradigm for planning through imagined futures, transforming decision-making across games, robotics and autonomous driving.

arXiv: https://arxiv.org/abs/2610.06250

#worldmodels #robotics
```

</details>

---
