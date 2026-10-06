# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-06 20:47 UTC

**Papers shown:** 111 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

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

### [Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation](https://arxiv.org/abs/2609.39822)

**Authors:** Di Wu, Rongtian Shen, Ping Liu, Yan Shen, Zhenhan Yin et al. (11 authors)

**Published:** 2026-09-30 (updated 2026-10-03) | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39822) | [PDF](https://arxiv.org/pdf/2609.39822) | [Project Page](https://embodied.magiclab.top/works/inference/index.html) | [Code](https://github.com/MagiclabRobotics/Inference)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution. We characterize this gap through end-to-end latency measurements of model inference and the robot execution chain. Repeated Flow Matching denoising contributes substantially to inference cost, while robot-side delays mainly arise from perception acquisition, communication scheduling, and physical response. Analysis of the velocity field shows relatively stable magnitude and direction in early integration, followed by stronger directional correction near the terminal steps. Based on t...

</details>

<details>
<summary>Share</summary>

```
Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution.

arXiv: https://arxiv.org/abs/2609.39822
Project page: https://embodied.magiclab.top/works/inference/index.html
Code: https://github.com/MagiclabRobotics/Inference

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

### [SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?](https://arxiv.org/abs/2610.02784)

**Authors:** Chen Yang, Linzhe Shi, Changjie Wu, Hang Zhang, Ronghan Chen et al. (10 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02784) | [PDF](https://arxiv.org/pdf/2610.02784) | [Project Page](https://simpletouch-robot.github.io/)

<details>
<summary>Abstract</summary>

Tactile sensing provides essential contact information for robotic manipulation, yet incorporating it into pretrained vision-language-action (VLA) models remains challenging. A common concern is that simply introducing touch during task-specific fine-tuning may fail to bridge the cross-modal gap, yielding limited gains or even reduced success. Consequently, existing methods often rely on large-scale tactile policy pretraining or separate visuotactile alignment, adding data requirements and training stages. We introduce SimpleTouch, a simple VLA extension that augments $π_{0.5}$ with a tactile...

</details>

<details>
<summary>Share</summary>

```
SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?

Tactile sensing provides essential contact information for robotic manipulation, yet incorporating it into pretrained vision-language-action (VLA) models remains challenging.

arXiv: https://arxiv.org/abs/2610.02784
Project page: https://simpletouch-robot.github.io/

#VLA #robotics
```

</details>

---

### [World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models](https://arxiv.org/abs/2610.02323)

**Authors:** Jie He, Wei Li, Junwen Tong, Rui Shao, Wei-Shi Zheng et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02323) | [PDF](https://arxiv.org/pdf/2610.02323) | [Code](https://github.com/JiuTian-VL/ProAct-page)

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies generate action chunks by transporting samples from a task-agnostic isotropic Gaussian source. As this source is conditioned on neither recent execution nor predicted future evolution, (i) it discards the local continuity established by recently executed motion. (ii) Even when predictive world representations are introduced, they often only condition the transport dynamics rather than determine where generation starts, how far it may deviate, or along which action directions it may expand. Building on this observation, we introduce ProAct, a wor...

</details>

<details>
<summary>Share</summary>

```
World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models

Flow-based Vision-Language-Action (VLA) policies generate action chunks by transporting samples from a task-agnostic isotropic Gaussian source.

arXiv: https://arxiv.org/abs/2610.02323
Code: https://github.com/JiuTian-VL/ProAct-page

#VLA #robotics
```

</details>

---

### [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)

**Authors:** Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding et al. (26 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39601) | [PDF](https://arxiv.org/pdf/2609.39601) | [Project Page](https://groundingpi.github.io/) | [Code](https://github.com/groundingpi/GroundingPI)

<details>
<summary>Abstract</summary>

Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding foundation model that generates points and boxes as quantized coordinates in a shared vocabulary. Training combines multimodal and spatial pretraining, supervised fine-tuning, and reinforce...

</details>

<details>
<summary>Share</summary>

```
GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

Precise grounding matters.

arXiv: https://arxiv.org/abs/2609.39601
Project page: https://groundingpi.github.io/
Code: https://github.com/groundingpi/GroundingPI

#VLA #robotics
```

</details>

---

### [Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead](https://arxiv.org/abs/2609.37165)

**Authors:** Junghyun Kim, Ngseo Kim, ChungWoo Lee, Seoyeon Lee, Woo-Jeong Baek et al. (10 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37165) | [PDF](https://arxiv.org/pdf/2609.37165) | [Project Page](https://dill-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure. We propose Domain-Invariant Latent Lookahead (DILL), a representation-learning framework that mitigates shortcut learning in VLA policies. Our key idea is to supervise policies with domain-invariant future latents learned from domain-transformed trajectory data. A Task-Domain Encoder is trained with contrastive objectives and Gaussian disentanglement regularization to separate task-relevant structure fro...

</details>

<details>
<summary>Share</summary>

```
Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure.

arXiv: https://arxiv.org/abs/2609.37165
Project page: https://dill-vla.github.io/

#VLA #robotics
```

</details>

---

### [FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation](https://arxiv.org/abs/2609.36416)

**Authors:** Jade Choghari, Pepijn Kooijmans, Mansi Agarwal, Yusuf Umut Ciftci, Aseem Doriwala et al. (11 authors)

**Published:** 2026-09-29 (updated 2026-09-30) | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36416) | [PDF](https://arxiv.org/pdf/2609.36416) | [Code](https://github.com/huggingface/lerobot)

<details>
<summary>Abstract</summary>

Robots operating in real-world environments must often execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions. Current manipulation datasets struggle to support this capability: although single-arm datasets reach hundreds of thousands of trajectories, they typically provide only one high-level instruction per episode, while existing bimanual datasets with subtask labels annotate only part of their recorded hours. We present FineART, a densely annotated bimanual manipulation dataset comprising 40,543 episodes (1,718 hours) and 533,913 subtasks across...

</details>

<details>
<summary>Share</summary>

```
FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation

Robots operating in real-world environments must often execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions.

arXiv: https://arxiv.org/abs/2609.36416
Code: https://github.com/huggingface/lerobot

#VLA #robotics
```

</details>

---

### [ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection](https://arxiv.org/abs/2610.01741)

**Authors:** Yijie Zhu, Rui Shao, Jie He, Wei Li, Bo Zhao et al. (11 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.01741) | [PDF](https://arxiv.org/pdf/2610.01741) | [Project Page](https://jiutian-vl.github.io/ATI-VLA-page/)

<details>
<summary>Abstract</summary>

Predictive Vision-Language-Action (VLA) models aim to improve robotic manipulation via future observation or world dynamics forecasting. However, existing approaches often fail to realize this potential and underperform direct action prediction models. We argue that these limitations stem from modality misalignment between observations and actions, together with joint optimization conflicts that drive learning away from an action-centric objective. To this end, we introduce ATI-VLA, an Action-Centric Predictive Vision-Language-Action framework via Actionable Alignment Then Adaptive Injection....

</details>

<details>
<summary>Share</summary>

```
ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection

Predictive Vision-Language-Action (VLA) models aim to improve robotic manipulation via future observation or world dynamics forecasting.

arXiv: https://arxiv.org/abs/2610.01741
Project page: https://jiutian-vl.github.io/ATI-VLA-page/

#VLA #robotics
```

</details>

---

### [VLALight: A Vision-Language-Action Model for Traffic Signal Control](https://arxiv.org/abs/2609.36934)

**Authors:** Pan Zhang, Siqi Lai, Kemu Dong, Hao Liu

**Published:** 2026-09-29 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36934) | [PDF](https://arxiv.org/pdf/2609.36934) | [Code](https://github.com/usail-hkust/VLALight.git)

<details>
<summary>Abstract</summary>

Traffic signal control (TSC) is essential for improving urban mobility and reducing congestion. Although roadside cameras are widely deployed at signalized intersections and provide rich visual observations of evolving traffic, existing TSC methods typically rely on manually engineered traffic states or separate perception modules, creating a gap between physical observations and control decisions. We present VLALight, the first vision-language-action (VLA) model for end-to-end traffic signal control from multi-view roadside videos. VLALight directly maps visual observations to coordinated sig...

</details>

<details>
<summary>Share</summary>

```
VLALight: A Vision-Language-Action Model for Traffic Signal Control

Traffic signal control (TSC) is essential for improving urban mobility and reducing congestion.

arXiv: https://arxiv.org/abs/2609.36934
Code: https://github.com/usail-hkust/VLALight.git

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

### [ForeAct3D: Policy-Grounded Future World Modeling for VLA Policies](https://arxiv.org/abs/2610.04607)

**Authors:** Zhe Tao, Feiran Wang, Gaowen Liu, Ramana Rao Kompella$, Yan Yan

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04607) | [PDF](https://arxiv.org/pdf/2610.04607) | [Code](https://github.com/anthonytao80-crypto/ForeAct3D)

<details>
<summary>Abstract</summary>

Robots need to anticipate how their actions will change the world, since manipulation success hinges on the resulting contacts and object motions. However, existing Vision-Language-Action (VLA) policies that predict future observations from shared features leave the forecast decoupled from the actions the policy will actually execute, and impose no physical constraints on how the scene may evolve. We introduce ForeAct3D, a framework for policy-grounded future world modeling within VLA policies. Learnable geometric queries decode depth, semantic segmentation, and camera pose from the policy rep...

</details>

<details>
<summary>Share</summary>

```
ForeAct3D: Policy-Grounded Future World Modeling for VLA Policies

Robots need to anticipate how their actions will change the world, since manipulation success hinges on the resulting contacts and object motions.

arXiv: https://arxiv.org/abs/2610.04607
Code: https://github.com/anthonytao80-crypto/ForeAct3D

#VLA #robotics
```

</details>

---

### [FastOPD: On-Policy Distillation for Lightweight VLA Deployment](https://arxiv.org/abs/2610.02832)

**Authors:** Yoojin Oh, Jeongsol Kim, Yeonwoo Seo, Jangho Park, Seonghyun Jin et al. (10 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02832) | [PDF](https://arxiv.org/pdf/2610.02832) | [Project Page](https://fastopd.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) foundation models have scaled rapidly to enhance manipulation performance and generalizability, but this scaling incurs high computational costs that render real-world deployment increasingly challenging. Existing approaches typically mitigate this issue by designing smaller architectures or reducing the iterative denoising steps in flow-based policies. In this work, we propose FastOPD, a foundation-to-lightweight VLA framework that enables the practical deployment of large-scale VLAs through efficient on-policy distillation. Specifically, FastOPD adapts a flow map...

</details>

<details>
<summary>Share</summary>

```
FastOPD: On-Policy Distillation for Lightweight VLA Deployment

Vision-Language-Action (VLA) foundation models have scaled rapidly to enhance manipulation performance and generalizability, but this scaling incurs high computational costs that render real-world deployment increasin...

arXiv: https://arxiv.org/abs/2610.02832
Project page: https://fastopd.github.io/

#VLA #robotics
```

</details>

---

### [Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies](https://arxiv.org/abs/2610.00982)

**Authors:** Xuehui Yu, Eason Yu, Meiyi Wang, Haozhe Du, Stefano V. Albrecht et al. (6 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00982) | [PDF](https://arxiv.org/pdf/2610.00982) | [Project Page](https://dnr-memory.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models struggle on history-dependent manipulation tasks, where the current observation alone does not determine the action, and the policy needs a memory of the history. Existing memory methods decide what to remember by design, for example, keeping frames with large pixel changes, and show inconsistent gains across tasks. We view what to remember as an optimisation problem. From the POMDP formulation of imitation learning, we show that the optimal memory maximises the conditional mutual information $I(a_t; m_t \mid o_t)$ between the action and the memory given the...

</details>

<details>
<summary>Share</summary>

```
Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies

Vision-language-action (VLA) models struggle on history-dependent manipulation tasks, where the current observation alone does not determine the action, and the policy needs a memory of the history.

arXiv: https://arxiv.org/abs/2610.00982
Project page: https://dnr-memory.github.io/

#VLA #robotics
```

</details>

---

### [NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields](https://arxiv.org/abs/2610.00981)

**Authors:** Shota Kobayashi, Koki Seno, Daichi Yashima, Komei Sugiura

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00981) | [PDF](https://arxiv.org/pdf/2610.00981) | [Project Page](https://shota0520.github.io/NarrativeFlow-project-page/)

<details>
<summary>Abstract</summary>

We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation models remains limited by the labor-intensive collection of embodiment-specific data. Existing methods either coarsely approximate robot flows with sparse keypoint displacements, or cannot handle language-conditioned manipulation. To address...

</details>

<details>
<summary>Share</summary>

```
NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platfo...

arXiv: https://arxiv.org/abs/2610.00981
Project page: https://shota0520.github.io/NarrativeFlow-project-page/

#VLA #robotics
```

</details>

---

### [TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2610.00899)

**Authors:** Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryoichi Nakajo, Roman Mykhailyshyn et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00899) | [PDF](https://arxiv.org/pdf/2610.00899) | [Project Page](https://kskshr.github.io/toast/)

<details>
<summary>Abstract</summary>

Autoregressive Vision-Language-Action models often represent continuous robot actions as discrete token sequences, enabling action prediction with standard next-token objectives. FAST has substantially improved this representation by compactly encoding action containing diverse temporal frequencies into relatively few tokens. However, while such compression reduces the number of action tokens required for autoregressive prediction, it does not necessarily improve the efficiency of policy learning from limited demonstrations. In particular, FAST typically assigns a single deterministic tokeniza...

</details>

<details>
<summary>Share</summary>

```
TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models

Autoregressive Vision-Language-Action models often represent continuous robot actions as discrete token sequences, enabling action prediction with standard next-token objectives.

arXiv: https://arxiv.org/abs/2610.00899
Project page: https://kskshr.github.io/toast/

#VLA #robotics
```

</details>

---

### [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://arxiv.org/abs/2610.00604)

**Authors:** Egor Cherepanov, Nikita Kachaev, Aleksandr I. Panov, Alexey K. Kovalev

**Published:** 2026-09-30 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00604) | [PDF](https://arxiv.org/pdf/2610.00604) | [Project Page](https://mikasarobo.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task. We introduce MIKASA-Robo-VLA, a benchmark of 90 language-conditioned manipulation tasks. All but 10 hide the cue an action depends on. Those 10 are reactive controls. MIKASA-Robo, the suite it rebuilds, has 32 tasks and uses language only in a representative VLA subset. Here every task provides an instruction, while memory-dependent tasks hide a task-relevant cue and reactive controls keep it available. For 70 tasks, environment...

</details>

<details>
<summary>Share</summary>

```
MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation

Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task.

arXiv: https://arxiv.org/abs/2610.00604
Project page: https://mikasarobo.github.io/

#VLA #robotics
```

</details>

---

### [Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs](https://arxiv.org/abs/2610.00524)

**Authors:** Taegeun Yang, Youngju Na, Yoonki Cho, Sung-Eui Yoon

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00524) | [PDF](https://arxiv.org/pdf/2610.00524) | [Project Page](https://taegeunyang.github.io/craft/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models often struggle to generalize to skill combinations absent from their fine-tuning demonstrations, even when every constituent skill has been demonstrated. We focus on a vision shortcut as one failure mode: during fine-tuning, visual observations can serve as a proxy for the instruction, so a policy may execute a demonstrated combination associated with similar observations rather than the instructed combination. This motivates training with counterfactual pairs formed by holding a demonstration observation fixed while changing the instruction to specify an un...

</details>

<details>
<summary>Share</summary>

```
Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs

Vision-language-action (VLA) models often struggle to generalize to skill combinations absent from their fine-tuning demonstrations, even when every constituent skill has been demonstrated.

arXiv: https://arxiv.org/abs/2610.00524
Project page: https://taegeunyang.github.io/craft/

#VLA #robotics
```

</details>

---

### [Multi-Link Safety Filtering for VLA Policies Around Moving Hazards](https://arxiv.org/abs/2609.40007)

**Authors:** Yatharth Agarwal, Vijay Raghunathan

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.40007) | [PDF](https://arxiv.org/pdf/2609.40007) | [Project Page](https://yathag.github.io/multilink-safety-filter/)

<details>
<summary>Abstract</summary>

A vision-language-action (VLA) policy can finish a manipulation task while knocking over objects unrelated to it, so task success alone does not show that the policy is safe to deploy in clutter. We study how to keep a pretrained VLA policy clear of such hazards at run time without retraining it, which requires guarding more of the arm than the end effector, following the hazard as it moves, and sharing onboard compute with the policy. Our training-free shield covers the gripper, wrist, and forearm with five ellipsoids and filters every commanded motion through one barrier program against a ke...

</details>

<details>
<summary>Share</summary>

```
Multi-Link Safety Filtering for VLA Policies Around Moving Hazards

A vision-language-action (VLA) policy can finish a manipulation task while knocking over objects unrelated to it, so task success alone does not show that the policy is safe to deploy in clutter.

arXiv: https://arxiv.org/abs/2609.40007
Project page: https://yathag.github.io/multilink-safety-filter/

#VLA #robotics
```

</details>

---

### [MotionWeave: Learning Motion-Centered Future Dynamics for Vision-Language-Action Policies](https://arxiv.org/abs/2609.39324)

**Authors:** Jingqiu Wang, Yan Wang

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39324) | [PDF](https://arxiv.org/pdf/2609.39324) | [Code](https://github.com/autu-mn/MotionWeave)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently incorporated world models to provide richer dynamic supervision beyond sparse action labels. However, explicitly predicting future images or videos may include control-irrelevant appearance, while guidance derived from holistic future visual representations and shared global action features may fail to establish timestep-specific correspondence between actions and local visual changes. To address this issue, we propose MotionWeave, a motion-centric future-dynamics framework for action-chunk prediction with two modules: the Action-Induced Motion...

</details>

<details>
<summary>Share</summary>

```
MotionWeave: Learning Motion-Centered Future Dynamics for Vision-Language-Action Policies

Vision-Language-Action (VLA) models have recently incorporated world models to provide richer dynamic supervision beyond sparse action labels.

arXiv: https://arxiv.org/abs/2609.39324
Code: https://github.com/autu-mn/MotionWeave

#VLA #robotics
```

</details>

---

### [Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation](https://arxiv.org/abs/2609.38989)

**Authors:** Haoxuan Wang, Griffin Galimi, Junhua Huang, Selina Song, Wayne Wu et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38989) | [PDF](https://arxiv.org/pdf/2609.38989) | [Project Page](https://hatchetproject.github.io/delivery_steer/)

<details>
<summary>Abstract</summary>

Open-world goods delivery requires mobile manipulators to follow free-form user instructions and manipulate potentially novel objects. Existing dual-system approaches use high-level grounding models to convert language into grounded visual prompts, but their low-level controllers can remain brittle under noisy perception, dynamic scenes, and contact-rich interactions. We instead use a pretrained flow-matching vision-language-action model as the low-level control interface, leveraging its reactivity and robustness to environmental changes while treating the grounding output as a spatial cue for...

</details>

<details>
<summary>Share</summary>

```
Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation

Open-world goods delivery requires mobile manipulators to follow free-form user instructions and manipulate potentially novel objects.

arXiv: https://arxiv.org/abs/2609.38989
Project page: https://hatchetproject.github.io/delivery_steer/

#VLA #robotics
```

</details>

---

### [Data-Efficient Adaptation of a Driving VLA to Class 8 Trucks](https://arxiv.org/abs/2609.38570)

**Authors:** Satyajeet Das, Aaron Buxbaum, Niels Joubert, Gaurav S. Sukhatme

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38570) | [PDF](https://arxiv.org/pdf/2609.38570) | [Project Page](https://truckvla.github.io)

<details>
<summary>Abstract</summary>

Class 8 trucks differ from passenger cars in geometry, dynamics, and maneuvering requirements. As a result, vision-language-action (VLA) models trained for passenger vehicles do not readily transfer to Class 8 trucks, particularly in unstructured scenarios such as accident scenes and construction zones. Rather than training a truck-driving VLA from scratch, we propose an adapt-then-steer strategy that adapts an off-the-shelf VLA to generate trajectories for Class-8 trucks in these challenging scenarios. In the adapt stage, we use NVIDIA's Alpamayo 1.5 as the base model, fine-tuning only its ac...

</details>

<details>
<summary>Share</summary>

```
Data-Efficient Adaptation of a Driving VLA to Class 8 Trucks

Class 8 trucks differ from passenger cars in geometry, dynamics, and maneuvering requirements.

arXiv: https://arxiv.org/abs/2609.38570
Project page: https://truckvla.github.io

#VLA #robotics
```

</details>

---

### [AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations](https://arxiv.org/abs/2609.36915)

**Authors:** Rui Huang, Yanlin Mu, Lidong Li, Yucong Wang, Zichen Yan et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36915) | [PDF](https://arxiv.org/pdf/2609.36915) | [Project Page](https://ruihuangnus.github.io/AeroManip-VLA-page/)

<details>
<summary>Abstract</summary>

Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation. However, extending Vision-Language-Action (VLA) models to aerial robots introduces distinct challenges due to the tight coupling between manipulation and flight, continuously changing observations, and safety-critical physical interactions. These challenges demand diverse training data and systematic policy evaluation, yet collecting demonstrations and evaluating policies directly on physical aerial platforms are c...

</details>

<details>
<summary>Share</summary>

```
AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations

Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2609.36915
Project page: https://ruihuangnus.github.io/AeroManip-VLA-page/

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

### [RoboIRS: Inference-Time Internal Representation Steering for Generalist Robot Policies](https://arxiv.org/abs/2610.04681)

**Authors:** Jiuzhou Lei, Chang Liu, Dayou Li, Zhiyuan Zhang, Xiao Liang et al. (8 authors)

**Published:** 2026-10-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.04681) | [PDF](https://arxiv.org/pdf/2610.04681) | [Project Page](https://rollingoat.github.io/roboirs/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) and world-action models (WAMs) often degrade under out-of-distribution task variations despite retaining partial task capability. To recover such capability, we propose RoboIRS, an inference-time internal representation steering method that uses successful and failed rollouts to train linear classifiers, select outcome-relevant intervention locations, and derive task-specific steering directions without updating policy parameters. On 15 simulation tasks with a frozen $π0.5$ policy, RoboIRS improves the average success rate from 44.4% to 66.2%, outperforming alterna...

</details>

<details>
<summary>Share</summary>

```
RoboIRS: Inference-Time Internal Representation Steering for Generalist Robot Policies

Vision-language-action (VLA) and world-action models (WAMs) often degrade under out-of-distribution task variations despite retaining partial task capability.

arXiv: https://arxiv.org/abs/2610.04681
Project page: https://rollingoat.github.io/roboirs/

#VLA #robotics
```

</details>

---

### [PerturBot: Breaking Shortcut Priors in Vision-Language-Action Models with Perturbative Training](https://arxiv.org/abs/2610.04616)

**Authors:** Mingyu Liu, Chonghao Sima, Tianjian Feng, Hanqing Wang, Cong Chen et al. (7 authors)

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.04616) | [PDF](https://arxiv.org/pdf/2610.04616)

<details>
<summary>Abstract</summary>

A vision--language--action (VLA) policy can complete complex tasks while ignoring the evidence that should determine its actions. An object held near the wrist camera can displace the instructed target. Language and action show the same pattern: a familiar noun can trigger the operation it was paired with in training even after the verb changes, and a gripper that closed on nothing may lift anyway. We call these dependencies modality shortcuts: regularities in successful demonstrations make visual, lexical, or motor cues sufficient to predict expert actions without the task evidence needed for...

</details>

<details>
<summary>Share</summary>

```
PerturBot: Breaking Shortcut Priors in Vision-Language-Action Models with Perturbative Training

A vision--language--action (VLA) policy can complete complex tasks while ignoring the evidence that should determine its actions.

arXiv: https://arxiv.org/abs/2610.04616

#VLA #robotics
```

</details>

---

### [MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2610.02898)

**Authors:** Pingrui Zhang, Yu Zhang, Pengyuan Wu, Bin Wang, Haoming Song et al. (11 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02898) | [PDF](https://arxiv.org/pdf/2610.02898)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved remarkable advances in robotic manipulation, yet their zero-shot generalization under out-of-distribution (OOD) conditions remains limited. These models often entangle task-relevant invariant structure with environment-specific non-invariant factors, causing policies to rely on spurious appearance cues during action prediction. In this work, we propose \textbf{MixVLA}, a model-agnostic training framework that improves the generalization of VLA models without requiring additional OOD data or architectural modifications. The key component of MixV...

</details>

<details>
<summary>Share</summary>

```
MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models

Vision-Language-Action (VLA) models have achieved remarkable advances in robotic manipulation, yet their zero-shot generalization under out-of-distribution (OOD) conditions remains limited.

arXiv: https://arxiv.org/abs/2610.02898

#VLA #robotics
```

</details>

---

### [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2610.03476)

**Authors:** Chenzhi Liu, Yue Zhang, Jiehong Lin, Jianan Wang, Bo Wang et al. (7 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.03476) | [PDF](https://arxiv.org/pdf/2610.03476) | [Project Page](https://kaiknower.github.io/mobiagent)

<details>
<summary>Abstract</summary>

Long-horizon mobile manipulation presents significant challenges due to compounding execution errors and capacity interference between locomotion and arm control. While recent Vision-Language-Action models excel at short-horizon tasks, they lack the hierarchical reasoning required for multi-stage objectives. Furthermore, existing hierarchical agents suffer from rigid sub-task mapping, inflexible replanning, and a lack of continuous learning. To address these limitations, we introduce MobiAgent, a dual-loop agentic framework that bridges robust deployment execution and recursive policy self-imp...

</details>

<details>
<summary>Share</summary>

```
MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation

Long-horizon mobile manipulation presents significant challenges due to compounding execution errors and capacity interference between locomotion and arm control.

arXiv: https://arxiv.org/abs/2610.03476
Project page: https://kaiknower.github.io/mobiagent

#VLA #robotics
```

</details>

---

### [ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control](https://arxiv.org/abs/2610.00801)

**Authors:** Yize Liu, Ke Wang, Mac Schwager, Yiqing Xu, Jiajun Wu

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.00801) | [PDF](https://arxiv.org/pdf/2610.00801) | [Project Page](https://ecomem.github.io/)

<details>
<summary>Abstract</summary>

A robot may lose sight of an object it must later retrieve, need to recall what a person demonstrated earlier, or track which steps of a task it has already completed. Current vision-language-action (VLA) policies often fail once the information needed for action disappears from the current observation, making memory critical for long-horizon robot behavior. Existing approaches typically provide longer histories or learn implicit memory from observation-action trajectories. But action supervision tells a policy how to act, not what to remember: it does not specify which past facts should persi...

</details>

<details>
<summary>Share</summary>

```
ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control

A robot may lose sight of an object it must later retrieve, need to recall what a person demonstrated earlier, or track which steps of a task it has already completed.

arXiv: https://arxiv.org/abs/2610.00801
Project page: https://ecomem.github.io/

#VLA #robotics
```

</details>

---

### [Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models](https://arxiv.org/abs/2609.39820)

**Authors:** Mingyue Cui, Zheyuan Liu, Yihan Zhu, Zheyuan Zhang, Meng Jiang

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39820) | [PDF](https://arxiv.org/pdf/2609.39820)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only te...

</details>

<details>
<summary>Share</summary>

```
Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact.

arXiv: https://arxiv.org/abs/2609.39820

#VLA #robotics
```

</details>

---

### [Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model](https://arxiv.org/abs/2609.39794)

**Authors:** Zaijing Li, Rui Shao, Bing Hu, Haoyu Zhang, Dongmei Jiang et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39794) | [PDF](https://arxiv.org/pdf/2609.39794)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, yet adapting them to new tasks and domains remains inefficient: existing methods often rely on parameter tuning, incurring substantial costs and risking catastrophic forgetting of previously learned tasks. To address this, we propose \textbf{Optimus-R}, a memory-centric VLA framework that formulates robotic adaptation as explicit query-skill memory tuning. Optimus-R introduces: (i) An \textbf{Inline Memory Interface for skill extraction}. It inserts learnable memory tokens into the VLA prefi...

</details>

<details>
<summary>Share</summary>

```
Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model

Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, yet adapting them to new tasks and domains remains inefficient: existing methods often rely on parameter tuning,...

arXiv: https://arxiv.org/abs/2609.39794

#VLA #robotics
```

</details>

---

### [Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2609.39178)

**Authors:** Songhua Yang, Ziyu Liu, Yuanwei Liu, Xuetao Li, Xuanye Fei et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.CR, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39178) | [PDF](https://arxiv.org/pdf/2609.39178)

<details>
<summary>Abstract</summary>

Recently, Vision-Language-Action (VLA) models have revolutionized robotic manipulation by seamlessly integrating visual perception, language understanding, and action generation in an end-to-end learning framework. However, since these models are designed to interact directly with the physical world and humans, their security is critical, and even small vulnerabilities can lead to catastrophic failures. In this work, we propose the Universal Adversarial Object, a sphere with optimized surface texture that significantly degrades task success rates when placed within the robot's field of view. S...

</details>

<details>
<summary>Share</summary>

```
Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics

Recently, Vision-Language-Action (VLA) models have revolutionized robotic manipulation by seamlessly integrating visual perception, language understanding, and action generation in an end-to-end learning framework.

arXiv: https://arxiv.org/abs/2609.39178

#VLA #robotics
```

</details>

---

### [EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation](https://arxiv.org/abs/2609.38046)

**Authors:** Yiming Jiang, Jin Chen, Chongyang Xu, Yilun Chen, Aimin Hao et al. (6 authors)

**Published:** 2026-09-29 (updated 2026-10-01) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.38046) | [PDF](https://arxiv.org/pdf/2609.38046) | [Project Page](https://lambdahumanoid.github.io/EgoAlign/)

<details>
<summary>Abstract</summary>

Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose, continuous whole-body controller, without collecting physical-robot demonstrations. Using the target-robot model and simulator, EgoAlign guides demonstration collection through execution feedback. It preserves locomotion re...

</details>

<details>
<summary>Share</summary>

```
EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation

Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervis...

arXiv: https://arxiv.org/abs/2609.38046
Project page: https://lambdahumanoid.github.io/EgoAlign/

#VLA #robotics
```

</details>

---

### [Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance](https://arxiv.org/abs/2609.38616)

**Authors:** Yanyan Zhang, Disheng Liu, Xinpeng Li, Chaoda Song, Mohsen Hariri et al. (11 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38616) | [PDF](https://arxiv.org/pdf/2609.38616)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models enable flexible action generation, their generalization across diverse environmental elements, including manipulated objects, destinations, and backgrounds, is limited by the lack of diversity in robotic training data. Trained end-to-end on such data, VLAs tend to exploit visual shortcuts, associating actions with task-irrelevant visual features rather than the intended task semantics. These shortcuts block recomposition of elements already seen by the policy, that is, compositional generalization. Existing approaches mitigate such entanglement through...

</details>

<details>
<summary>Share</summary>

```
Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance

While Vision-Language-Action (VLA) models enable flexible action generation, their generalization across diverse environmental elements, including manipulated objects, destinations, and backgrounds, is limited by the...

arXiv: https://arxiv.org/abs/2609.38616

#VLA #robotics
```

</details>

---

### [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](https://arxiv.org/abs/2609.36588)

**Authors:** Ruixiao Xu, Wong Lik Hang Kenny, Zhiqian Liu, Jianing Guo, Hanxiao Li et al. (15 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.MA | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36588) | [PDF](https://arxiv.org/pdf/2609.36588)

<details>
<summary>Abstract</summary>

We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models. This problem is challenging because VLAs are pretrained on large-scale single-agent data and therefore lack the fine-grained coordination skills required for inter-robot collaboration. Supervised fine-tuning (SFT) on multi-robot demonstrations partially bridges this gap, but its performance is bounded by the demonstration data and cannot improve from its own experience. We present a three-stage reinforced fine-tuning (RFT) pipeline for multi-agent VLAs. First, initialization-aware data...

</details>

<details>
<summary>Share</summary>

```
Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models.

arXiv: https://arxiv.org/abs/2609.36588

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

### [CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation](https://arxiv.org/abs/2610.02666)

**Authors:** Jin Hyun, Jung Gyu Min, Gyuhyun Jung, Youngjoo Lee

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02666) | [PDF](https://arxiv.org/pdf/2610.02666)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map visual observations and language instructions to continuous robot actions, but a diffusion-based action expert (AE) poses a key challenge for low-bit post-training quantization (PTQ). The AE is repeatedly invoked across denoising steps and policy queries, where fixed calibration scales can be mismatched with activation ranges that vary with denoising progress and intended motion. We propose CHASE-VLA, a chunk-aware PTQ method that exploits a VLA-specific signal readily available from the policy: the generated action chunk, including its unexecuted future...

</details>

<details>
<summary>Share</summary>

```
CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation

Vision-Language-Action (VLA) models map visual observations and language instructions to continuous robot actions, but a diffusion-based action expert (AE) poses a key challenge for low-bit post-training quantization...

arXiv: https://arxiv.org/abs/2610.02666

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

### [PermVLA: Factorization Order as a Regularizer for VLA Learning](https://arxiv.org/abs/2610.04659)

**Authors:** Yanqiao Chen, Yuhan Rui, Dongsheng Hou, Zijie Nie, Yutong Wan et al. (6 authors)

**Published:** 2026-10-03 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.04659) | [PDF](https://arxiv.org/pdf/2610.04659)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly learn action chunks through a fixed left-to-right (LTR) factorization, although the same expert trajectory distribution admits many valid chain-rule factorizations. We identify factorization order as an overlooked regularization choice and introduce causally anchored permutation (CAP), which samples action reveal orders with a tunable chronological prefix. Its auxiliary objective trains one shared policy to predict actions from different known subsets of the same expert chunk, while deployment retains deterministic LTR control. We call this condit...

</details>

<details>
<summary>Share</summary>

```
PermVLA: Factorization Order as a Regularizer for VLA Learning

Vision-language-action (VLA) policies commonly learn action chunks through a fixed left-to-right (LTR) factorization, although the same expert trajectory distribution admits many valid chain-rule factorizations.

arXiv: https://arxiv.org/abs/2610.04659

#VLA #robotics
```

</details>

---

### [AgenticTactileVLA: Contact-Guided Execution-Time Supervision for Generalizable Dexterous Manipulation without VLA Retraining](https://arxiv.org/abs/2610.04391)

**Authors:** Elizaveta Semenyakina, Ivan Snegirev, Mikhail Kiselev, Miguel Altamirano Cabrera, Artem Lykov et al. (7 authors)

**Published:** 2026-10-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.04391) | [PDF](https://arxiv.org/pdf/2610.04391)

<details>
<summary>Abstract</summary>

Vision-language-action policies may predict a transferable manipulation strategy yet fail to realize it reliably on the encountered object: objects compatible with the same grasp differ in geometry and compliance, and visual feedback degrades under closure occlusion. AgenticTactileVLA is presented as an execution-time supervisor that shifts part of object-specific adaptation from prediction to physical interaction. A fixed VLA provides the approach and hand targets; the supervisor decides whether to remain transparent, refine finger flexion, retain or release the corrected configuration, retur...

</details>

<details>
<summary>Share</summary>

```
AgenticTactileVLA: Contact-Guided Execution-Time Supervision for Generalizable Dexterous Manipulation without VLA Retraining

Vision-language-action policies may predict a transferable manipulation strategy yet fail to realize it reliably on the encountered object: objects compatible with the same grasp differ in geometry and compliance, and...

arXiv: https://arxiv.org/abs/2610.04391

#VLA #robotics
```

</details>

---

### [SUAVE: Unified Video-Action Models via Masked Diffusion](https://arxiv.org/abs/2610.04009)

**Authors:** Rhythm Syed, Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah et al. (8 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.04009) | [PDF](https://arxiv.org/pdf/2610.04009)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) inherit strong semantic grounding from pretrained vision-language backbones but are typically optimized for predicting actions rather than future observations. They can see and act, but they do not imagine the future before acting. World action models (WAMs) built on video diffusion backbones can imagine but treat language as frozen conditioning on a continuous latent space. Unified models bring these modalities into one architecture, but they either decode autoregressively, one token at a time, or keep video continuous with an auxiliary action head. In thi...

</details>

<details>
<summary>Share</summary>

```
SUAVE: Unified Video-Action Models via Masked Diffusion

Vision-language-action models (VLAs) inherit strong semantic grounding from pretrained vision-language backbones but are typically optimized for predicting actions rather than future observations.

arXiv: https://arxiv.org/abs/2610.04009

#VLA #robotics
```

</details>

---

### [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](https://arxiv.org/abs/2610.03498)

**Authors:** Yukiya Horiba, Koshiro Aoki, Shunsuke Yasuki, Bum Jun Kim, Taiki Miyanishi

**Published:** 2026-10-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.03498) | [PDF](https://arxiv.org/pdf/2610.03498)

<details>
<summary>Abstract</summary>

Adversarial patches can disrupt Vision-Language-Action (VLA) models by manipulating visual observations, leading to failures in robot control. However, it remains poorly understood which internal mechanisms underlie these failures and how targeted interventions can mitigate them. In this work, we mechanistically analyze VLA representations using a sparse autoencoder (SAE) and identify a feature whose activation strongly correlates with the presence of an adversarial patch. Based on this analysis, we suppress the identified feature at inference time only when a linear probe detects an attack. T...

</details>

<details>
<summary>Share</summary>

```
Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models

Adversarial patches can disrupt Vision-Language-Action (VLA) models by manipulating visual observations, leading to failures in robot control.

arXiv: https://arxiv.org/abs/2610.03498

#VLA #robotics
```

</details>

---

### [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](https://arxiv.org/abs/2610.02840)

**Authors:** Chunghyun Park, Beomjun Kim, Seungcheol Park, Heeseung Kwon, Yashu Shukla et al. (8 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.02840) | [PDF](https://arxiv.org/pdf/2610.02840) | [Project Page](https://chrockey.github.io/PointWAM)

<details>
<summary>Abstract</summary>

World action models jointly learn to forecast world dynamics and predict robot actions, such that the learned internal world dynamics guide accurate actions. Existing approaches typically represent the world as RGB frames or latent counterparts while predicting actions as end-effector poses or joint angles, but they often struggle to capture the 3D spatial structure and contact geometry central to dexterous manipulation. We introduce Point World Action Model (PointWAM), a 3D world action model that decomposes the world into a scene (i.e., environment) and hands (i.e., actor), and jointly forec...

</details>

<details>
<summary>Share</summary>

```
PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation

World action models jointly learn to forecast world dynamics and predict robot actions, such that the learned internal world dynamics guide accurate actions.

arXiv: https://arxiv.org/abs/2610.02840
Project page: https://chrockey.github.io/PointWAM

#VLA #robotics
```

</details>

---

### [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)

**Authors:** Sangwu Park, Yeonjun In, Wonjoong Kim, Sungwon Kim, Sein Kim et al. (6 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02802) | [PDF](https://arxiv.org/pdf/2610.02802)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models aim to perform diverse manipulation tasks, but task success in existing rigid-body benchmarks does not indicate whether they preserve objects. We introduce ManiPhysicsZoo, which consolidates literature-supported material properties, 3D meshes, and supporting references into reusable object assets. Using these assets, a solver-based assessment computes grasp-specific damage thresholds from object geometry, material properties, and recorded grasp conditions and compares them with recorded contact forces to assess potential deformation and fracture. Building on...

</details>

<details>
<summary>Share</summary>

```
ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation

Vision-language-action (VLA) models aim to perform diverse manipulation tasks, but task success in existing rigid-body benchmarks does not indicate whether they preserve objects.

arXiv: https://arxiv.org/abs/2610.02802

#VLA #robotics
```

</details>

---

### [SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation](https://arxiv.org/abs/2610.02360)

**Authors:** Sofya Konstantinova, Miguel Altamirano Cabrera, Artem Lykov, Dzmitry Tsetserukou

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02360) | [PDF](https://arxiv.org/pdf/2610.02360)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies enable diverse robotic manipulation but can fail during execution without recognizing their own errors. Human observers provide complementary signals, as unexpected robot behavior can trigger rapid vocal, facial, or verbal reactions before failure is completed. We introduce SocialVLA, a local, policy-agnostic social perception gateway that converts spontaneous human reactions into runtime intervention signals for VLA manipulation. SocialVLA combines causal paralinguistic audio detection, visual reaction recognition, explicit stop phrases, and robot-relevan...

</details>

<details>
<summary>Share</summary>

```
SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation

Vision-language-action (VLA) policies enable diverse robotic manipulation but can fail during execution without recognizing their own errors.

arXiv: https://arxiv.org/abs/2610.02360

#VLA #robotics
```

</details>

---

### [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](https://arxiv.org/abs/2610.02161)

**Authors:** Hanchu Zhou, Dechen Gao, Hang Wang, Brendan Lynch, Boqi Zhao et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02161) | [PDF](https://arxiv.org/pdf/2610.02161)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings. Extending these capabilities to multi-robot systems remains challenging because robots must coordinate long-horizon behaviors while maintaining reliable, fine-grained execution. We introduce DuoMind, a distributed hierarchical framework for multi-robot coordination through semantic communication. Each robot uses a VLA-based action model for low-level execution and a VLM-based orchestrator for high-level rea...

</details>

<details>
<summary>Share</summary>

```
DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication

Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings.

arXiv: https://arxiv.org/abs/2610.02161

#VLA #robotics
```

</details>

---

### [ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing](https://arxiv.org/abs/2610.01856)

**Authors:** Zhugang Liu, Kaichuang Zhang, Jinman Zhang, Pu Sun, Martha Asare et al. (10 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.01856) | [PDF](https://arxiv.org/pdf/2610.01856)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering new opportunities for automation in additive manufacturing (AM). However, deployment in AM remains challenging because adapting these models to unseen robot embodiments is costly, and performance can degrade under environment changes. In this work, we present a framework for deploying OpenVLA-OFT on a FAIRINO FR3 robot in a fixed AM workcell. A data pipeline converts monocular real-world demonstrations into OpenVLA-compatible TFDS/RLDS datasets to support adaptation to the FR3 e...

</details>

<details>
<summary>Share</summary>

```
ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing

Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering new opportunities for automation in additive manufacturing (AM).

arXiv: https://arxiv.org/abs/2610.01856

#VLA #robotics
```

</details>

---

### [Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors](https://arxiv.org/abs/2610.01794)

**Authors:** Edward W. Staley, Connor O. Pyles, Rahul Hingorani, Frank Camargo, Griffin Milsap et al. (8 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.01794) | [PDF](https://arxiv.org/pdf/2610.01794)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models rely strongly on language for describing task information, despite having multimodal inputs. We hypothesize that other modalities in the state space may present opportunities for supplemental task conditioning, which may be particularly relevant in cluttered or otherwise ambiguous scenes. We introduce two tuned models to test this hypothesis: (1) an electrophysiology-conditioned VLA (EC-VLA) that incorporates 8-channel electromyography envelopes as continuous conditioning input concatenated to the proprioceptive vector, and (2) a visually-annotated VLA (VA-V...

</details>

<details>
<summary>Share</summary>

```
Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors

Vision-Language-Action (VLA) models rely strongly on language for describing task information, despite having multimodal inputs.

arXiv: https://arxiv.org/abs/2610.01794

#VLA #robotics
```

</details>

---

### [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351)

**Authors:** Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci, Alessandro Suglia

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.01351) | [PDF](https://arxiv.org/pdf/2610.01351)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks. More recently, there has been an emphasis on evaluating the robustness of VLA models to perturbations. However, this robustness is still predominantly measured through Task Success Rate (TSR). In this work, we propose a benchmark-agnostic evaluation framework to measure the behavioural robustness of models by characterising how successful trajectories are executed under perturbation. We implement this methodology by extending the widely-used LIBERO and LIBERO-Plus benchmarks. Across...

</details>

<details>
<summary>Share</summary>

```
Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks

Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks.

arXiv: https://arxiv.org/abs/2610.01351

#VLA #robotics
```

</details>

---

### [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](https://arxiv.org/abs/2610.01083)

**Authors:** Samuel Zhen, Siwon Jo, Yanze Zhang, Wenhao Luo

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.01083) | [PDF](https://arxiv.org/pdf/2610.01083)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have demonstrated impressive capabilities in generalizable robotic manipulation, but their deployment in the real world remains challenging due to potential collisions involving different parts of the robot, manipulated objects, and the surrounding environment. Existing inference-time VLA safety frameworks typically rely on simplified end-effector-centered representations that do not explicitly model the full articulated robot and attached-object geometry. In this paper, we present WBAG, a safety framework that models the robot's whole-body and grasp-depen...

</details>

<details>
<summary>Share</summary>

```
WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation

Vision-language-action (VLA) policies have demonstrated impressive capabilities in generalizable robotic manipulation, but their deployment in the real world remains challenging due to potential collisions involving d...

arXiv: https://arxiv.org/abs/2610.01083

#VLA #robotics
```

</details>

---

### [eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing](https://arxiv.org/abs/2610.00913)

**Authors:** Dehao Huang, Jianbang Liu, Jianpan Gao, Chao Tang, Zilang Cen et al. (10 authors)

**Published:** 2026-10-01 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.00913) | [PDF](https://arxiv.org/pdf/2610.00913)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models provide strong behavioral priors for robotic manipulation, yet efficiently adapting them to downstream tasks remains challenging. Recent work addresses this challenge by adapting frozen VLAs through online reinforcement learning (RL), whose sample efficiency depends on the quality of the state representation used by the actor and critic. Existing methods construct such representations either with VLA-independent visual encoders or through fixed compression of internal VLA representations. Neither design explicitly extracts the task-specific action-relevant V...

</details>

<details>
<summary>Share</summary>

```
eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing

Vision-Language-Action (VLA) models provide strong behavioral priors for robotic manipulation, yet efficiently adapting them to downstream tasks remains challenging.

arXiv: https://arxiv.org/abs/2610.00913

#VLA #robotics
```

</details>

---

### [When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies](https://arxiv.org/abs/2610.00601)

**Authors:** Sathwik Karnik, Joseph JR. Lee, Aryaman Gupta, Somil Bansal

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.00601) | [PDF](https://arxiv.org/pdf/2610.00601)

<details>
<summary>Abstract</summary>

Reasoning-enabled VLA policies expose chain-of-thought (CoT) traces that appear to explain and guide their actions, creating a potential interface for runtime safety through reasoning monitoring and correction. In this work, we define and operationalize two evaluation axes for assessing when this interface can improve embodied behavior: correctability, which measures whether unreliable reasoning can be detected and improved during generation, and actionability, which measures whether reasoning corrections produce behaviorally meaningful changes in the intended direction. To enable correctabili...

</details>

<details>
<summary>Share</summary>

```
When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies

Reasoning-enabled VLA policies expose chain-of-thought (CoT) traces that appear to explain and guide their actions, creating a potential interface for runtime safety through reasoning monitoring and correction.

arXiv: https://arxiv.org/abs/2610.00601

#VLA #robotics
```

</details>

---

### [DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents](https://arxiv.org/abs/2609.40306)

**Authors:** Haoyuan Deng, Jiebin Liu, Tengxiao Zhang, Langning Yan, Hongye Cao et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.40306) | [PDF](https://arxiv.org/pdf/2609.40306) | [Project Page](https://denghaoyuan123.github.io/Dynaharness_page/)

<details>
<summary>Abstract</summary>

Pretrained robot policies provide useful action priors, but long-horizon manipulation still requires coordination between semantic reasoning and physical execution. Semantic reasoning operates at a coarser timescale than physical interaction, while episode-level failures provide limited guidance on which system component should be revised. We propose DynaHarness, a dynamic physical harness that couples semantic reasoning with physical governance through a shared execution contract and turns failure evidence into validated capability revisions. To be more specific, the slow brain proposes capab...

</details>

<details>
<summary>Share</summary>

```
DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents

Pretrained robot policies provide useful action priors, but long-horizon manipulation still requires coordination between semantic reasoning and physical execution.

arXiv: https://arxiv.org/abs/2609.40306
Project page: https://denghaoyuan123.github.io/Dynaharness_page/

#VLA #robotics
```

</details>

---

### [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](https://arxiv.org/abs/2609.39971)

**Authors:** Hung-Jen Chen, Yu-Hsun Hou, Yan-Hong Chen, Yan-Fu Chen, Binghua Cai et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39971) | [PDF](https://arxiv.org/pdf/2609.39971)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action. Aggregate robustness scores can therefore conceal a more specific failure, in which a policy responds to both language and vision yet does not combine them to select the action the task requires. We call this failure instruction-action binding. Instructions cue familiar trajectory families, and visual feedback adjusts their execution. Behavioral analyses of fine-tuned $π_{0.5}$...

</details>

<details>
<summary>Share</summary>

```
When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models

Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action.

arXiv: https://arxiv.org/abs/2609.39971

#VLA #robotics
```

</details>

---

### [From Local Whole-Body VLA Behaviors to Scene-Scale Aerial Manipulation](https://arxiv.org/abs/2609.39670)

**Authors:** Weixiang Guo, Rui Jin, Haotian Jin, Xinhang Xu, Ruiyang Liu et al. (10 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39670) | [PDF](https://arxiv.org/pdf/2609.39670)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable task-conditioned interaction, but extending them to scene-scale aerial manipulation remains challenging due to costly whole-body demonstrations, latency-induced action-state misalignment, and cross-site behavior composition. We present a unified framework for synthetic policy training and scene-scale execution on articulated uncrewed aerial manipulators (UAMs). A scene-reconfigurable pipeline synthesizes task-conditioned, kinodynamically feasible trajectories and synchronized multiview observations for VLA training without physical-platform demonstrat...

</details>

<details>
<summary>Share</summary>

```
From Local Whole-Body VLA Behaviors to Scene-Scale Aerial Manipulation

Vision-language-action (VLA) models enable task-conditioned interaction, but extending them to scene-scale aerial manipulation remains challenging due to costly whole-body demonstrations, latency-induced action-state...

arXiv: https://arxiv.org/abs/2609.39670

#VLA #robotics
```

</details>

---

### [DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction](https://arxiv.org/abs/2609.39198)

**Authors:** Wenhao Li, Xiu Su, Yu Han, Yichao Cao, Shan You et al. (6 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39198) | [PDF](https://arxiv.org/pdf/2609.39198)

<details>
<summary>Abstract</summary>

While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation). We identify three fundamental limitations hindering current VLAs in these scenarios: the \textbf{perception gap}, where static visual inputs lack temporal motion cues; the \textbf{latency gap}, where inference delays render actions obsolete; and the \textbf{control gap}, caused by the open-loop action chunk execution without real-time adjustment. In this work, we propose \textbf{DSDyn-VLA}, a Slow-Fast \textbf{D}ual-\textbf{S}tre...

</details>

<details>
<summary>Share</summary>

```
DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction

While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation).

arXiv: https://arxiv.org/abs/2609.39198

#VLA #robotics
```

</details>

---

### [Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults](https://arxiv.org/abs/2609.39145)

**Authors:** Heejae Suh, Jongwook Han, Zahra Gholami, Yohan Jo

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39145) | [PDF](https://arxiv.org/pdf/2609.39145)

<details>
<summary>Abstract</summary>

Unreliable visual inputs can harm task performance and cause potential physical safety risks for vision-language-action (VLA) models. We analyze how $π0.5$ and GR00T models act under input faults such as image blackouts and freezing. We find that blackout and freezing produce distinct physical failure modes even when task-success rates are similarly low: freezing causes more extreme joint behavior, whereas blackout after gripper closure can cause more object drops, most markedly without proprioception. Selective intervention studies reveal that proprioception (current robot state) partly compe...

</details>

<details>
<summary>Share</summary>

```
Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults

Unreliable visual inputs can harm task performance and cause potential physical safety risks for vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2609.39145

#VLA #robotics
```

</details>

---

### [Looking Back to Move Forward: Temporal Verification for Generative Robot Policies](https://arxiv.org/abs/2609.39038)

**Authors:** Haoxuan Wang, Wayne Wu, Yan Yan, Bolei Zhou

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.39038) | [PDF](https://arxiv.org/pdf/2609.39038) | [Project Page](https://hatchetproject.github.io/tev/)

<details>
<summary>Abstract</summary>

Generative policies have emerged as a promising paradigm for robot learning, combining expressive generative action modeling with scalable imitation learning from large demonstration corpora. However, heterogeneous demonstrations can induce suboptimal action chunks whose errors compound over time, eventually driving the robot into out-of-distribution states from which recovery is difficult. Action verification offers a test-time scaling strategy for mitigating this failure mode by sampling multiple candidate actions and using a verifier to select one for execution. Existing approaches, however...

</details>

<details>
<summary>Share</summary>

```
Looking Back to Move Forward: Temporal Verification for Generative Robot Policies

Generative policies have emerged as a promising paradigm for robot learning, combining expressive generative action modeling with scalable imitation learning from large demonstration corpora.

arXiv: https://arxiv.org/abs/2609.39038
Project page: https://hatchetproject.github.io/tev/

#VLA #robotics
```

</details>

---

### [Online Evolution Strategy for Flow-Matching VLA Policies via Self-Supervised Trajectory Distribution Optimization](https://arxiv.org/abs/2609.38855)

**Authors:** Gongxin Yao, Yongsheng Zhao, Jiayin Deng, Deng Liang, Han Gao et al. (7 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38855) | [PDF](https://arxiv.org/pdf/2609.38855)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models based on generative frameworks, such as Flow Matching, have recently achieved impressive performance in robotic manipulation. Unlike deterministic policies, Flow Matching enables VLA models to learn conditional action trajectory distributions, where latent noise vectors induce different actions under the same task scenario. However, we observe that these distributions are often ill-formed, with successful and failed behaviors coexisting while considerable probability mass remains in unfavorable regions. To this end, we propose Online-ES, an online adaptation...

</details>

<details>
<summary>Share</summary>

```
Online Evolution Strategy for Flow-Matching VLA Policies via Self-Supervised Trajectory Distribution Optimization

Vision-Language-Action (VLA) models based on generative frameworks, such as Flow Matching, have recently achieved impressive performance in robotic manipulation.

arXiv: https://arxiv.org/abs/2609.38855

#VLA #robotics
```

</details>

---

### [Vision-Language-Action Autonomous Driving Agent with Language-based Memory](https://arxiv.org/abs/2609.38641)

**Authors:** Kai Yan, Xiangyu Chen, Yulong Cao, Alex Naumann, Peter Karkus et al. (12 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38641) | [PDF](https://arxiv.org/pdf/2609.38641)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate and interpretable driving. However, VLAs can take only a limited number of frames as visual input due to the high token cost of an image, which is problematic for memory-dependent tasks such as determining the arrival order at all-way stops and long-horizon driving scene understanding. Existing solutions use latent vector memories accessed through cross-attention, which are neither...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Action Autonomous Driving Agent with Language-based Memory

Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate an...

arXiv: https://arxiv.org/abs/2609.38641

#VLA #robotics
```

</details>

---

### [Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control](https://arxiv.org/abs/2609.37772)

**Authors:** Zibo Wang, Haochen Han, Pengzhen Ren, Mingtong Dai, Fangming Liu

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37772) | [PDF](https://arxiv.org/pdf/2609.37772)

<details>
<summary>Abstract</summary>

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control. Existing acceleration methods treat an action chunk as a monolithic computational unit, ignoring a crucial physical reality of receding-horizon control: actions are generated jointly but consumed sequentially, resulting in inherently heterogeneous execution urgencies. We exploit this asymmetry to introduce Urgency-Aware Denoising (UAD), a novel inference-time framework that allocates denoisi...

</details>

<details>
<summary>Share</summary>

```
Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control

Diffusion and flow-matching Vision-Language-Action (VLA) policies generate action chunks through iterative denoising, incurring substantial inference latency that severely limits real-time robotic control.

arXiv: https://arxiv.org/abs/2609.37772

#VLA #robotics
```

</details>

---

### [Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration](https://arxiv.org/abs/2609.37771)

**Authors:** Qiwei Chen, Kaijun Zhou, Nuohui Shi, Zhiyang Li, Yuxuan Feng et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37771) | [PDF](https://arxiv.org/pdf/2609.37771)

<details>
<summary>Abstract</summary>

Simulated manipulation benchmarks are the standard tool for evaluating vision-language-action (VLA) policies and the acceleration methods that reduce their inference latency for on-robot deployment. On these benchmarks, we observe that some training-free acceleration methods, which approximate the baseline policy's computation, achieve higher measured success rates than the baseline itself. Success rates alone cannot establish whether such gains come from better task execution or from evaluation flaws. We therefore investigate two kinds of benchmark flaws behind these gains: bugs, where the im...

</details>

<details>
<summary>Share</summary>

```
Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration

Simulated manipulation benchmarks are the standard tool for evaluating vision-language-action (VLA) policies and the acceleration methods that reduce their inference latency for on-robot deployment.

arXiv: https://arxiv.org/abs/2609.37771

#VLA #robotics
```

</details>

---

### [Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing](https://arxiv.org/abs/2609.37334)

**Authors:** Sohyun Lee, Yoonjae Baek, Jaesang Won, Jinnyeong Kim, Kang Hyunwoo et al. (8 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37334) | [PDF](https://arxiv.org/pdf/2609.37334)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action. Such execution errors arise from the robot's mechanics and operating conditions, such as wear and payload changes. We propose self-compensating VLA, a deployment-time adaptation method that enables a VLA policy to pre-compensate for the robot's execution errors when generating commands. Without task rewards or labels, it updates the policy online using the residual between the action commanded by a VLA and the motion executed by the robot. To stress-test VLA robustness across e...

</details>

<details>
<summary>Share</summary>

```
Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action.

arXiv: https://arxiv.org/abs/2609.37334

#VLA #robotics
```

</details>

---

### [Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2609.37307)

**Authors:** Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37307) | [PDF](https://arxiv.org/pdf/2609.37307)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks. However, many existing VLAs lack explicit access to interaction history, making them vulnerable to perceptual aliasing: similar current observations and robot states at different task stages may induce action ambiguity and lower success rate. Existing methods incorporate temporal or progress cues through feature conditioning, action-prior modification, or sampling guidance. However, methods that jointly fine-tune memo...

</details>

<details>
<summary>Share</summary>

```
Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks.

arXiv: https://arxiv.org/abs/2609.37307

#VLA #robotics
```

</details>

---

### [Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2609.36967)

**Authors:** Jiayu Chen, Shuyong Gao, Jingkai Jia, Xiaosheng Bu, Jiyuan Fu et al. (9 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36967) | [PDF](https://arxiv.org/pdf/2609.36967)

<details>
<summary>Abstract</summary>

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a purely geometric pruning strategy. Surprisingly, Stride outperforms semantic pruning and random pruning at certain pruning ratios, but collapses when the token budget is only slightly reduced. We characterize this phenomenon through the spat...

</details>

<details>
<summary>Share</summary>

```
Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation.

arXiv: https://arxiv.org/abs/2609.36967

#VLA #robotics
```

</details>

---

### [Where Predictive Supervision Goes Shapes What VLA Policies Learn](https://arxiv.org/abs/2609.36645)

**Authors:** Hanseul Kim, Jewon Yeom, Youngjoon Jeong, Minsoo Jo, Taesup Kim

**Published:** 2026-09-29 (updated 2026-10-01) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36645) | [PDF](https://arxiv.org/pdf/2609.36645)

<details>
<summary>Abstract</summary>

Future prediction is increasingly used to improve vision-language-action (VLA) policies, based on the premise that anticipating scene evolution encourages representations useful for control. However, forecast quality alone does not establish that a policy has learned a better representation for action. This distinction matters under distribution shift, where successful control depends on preserving spatial state and likely scene change beyond familiar configurations. We study what determines whether predictive supervision improves the visual representation used by a VLA policy. Through control...

</details>

<details>
<summary>Share</summary>

```
Where Predictive Supervision Goes Shapes What VLA Policies Learn

Future prediction is increasingly used to improve vision-language-action (VLA) policies, based on the premise that anticipating scene evolution encourages representations useful for control.

arXiv: https://arxiv.org/abs/2609.36645

#VLA #robotics
```

</details>

---

### [DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies](https://arxiv.org/abs/2610.00317)

**Authors:** Youngjun Jun, Kyumin Choi, Youngmin Kim, Seonghyun Jin, Sunwoo Park et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.00317) | [PDF](https://arxiv.org/pdf/2610.00317)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models increasingly rely on action experts that generate short action chunks under receding-horizon control. While chunk-level training is convenient across robot embodiments, it optimizes local action likelihood without explicitly accounting for long-horizon task success. Sequence-level reinforcement learning can address this limitation, but typically requires policy rollouts and closed-loop interaction, which are costly for real-robot manipulation. We introduce DriftOPD, a teacher-free, rollout-free framework for sequence-level on-policy distillation of continuou...

</details>

<details>
<summary>Share</summary>

```
DriftOPD: Sequence-Level Reverse-KL Distillation for One-Step VLA Policies

Vision-Language-Action (VLA) models increasingly rely on action experts that generate short action chunks under receding-horizon control.

arXiv: https://arxiv.org/abs/2610.00317

#VLA #robotics
```

</details>

---

### [Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment](https://arxiv.org/abs/2609.36540)

**Authors:** Moritz Zoellner, Reece O'Mahoney, Ioannis Havoutis, Rohan Paleja

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36540) | [PDF](https://arxiv.org/pdf/2609.36540)

<details>
<summary>Abstract</summary>

Generalist robot policies such as vision-language-action models (VLAs) have achieved remarkable generalization, but their inference delays can conflict with the demands of real-time control. Asynchronous execution avoids pauses between action chunks by predicting the next sequence of actions while the robot carries out the previous one. In this paper, we study whether asynchronous execution produces the same action distribution as the original VLA. We find that, for non-Markovian demonstrations, asynchronous execution can produce a fundamentally different action distribution, which can limit t...

</details>

<details>
<summary>Share</summary>

```
Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment

Generalist robot policies such as vision-language-action models (VLAs) have achieved remarkable generalization, but their inference delays can conflict with the demands of real-time control.

arXiv: https://arxiv.org/abs/2609.36540

#VLA #robotics
```

</details>

---

### [LIBERO-MAX: Do Robot Policies Adapt When the World Changes?](https://arxiv.org/abs/2609.36518)

**Authors:** Yunbei Zhang, Zijian Jin, Yuanzhe Liu, Janet Wang, Xilun Zhang et al. (17 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36518) | [PDF](https://arxiv.org/pdf/2609.36518) | [Project Page](https://liberomax.github.io)

<details>
<summary>Abstract</summary>

Robots must often continue a task after a target moves, the viewpoint shifts, or an obstacle appears, even though their earlier observations and committed actions reflect the previous scene. Many simulation robustness benchmarks fix external conditions at reset, leaving this temporal challenge underexamined. We introduce LIBERO-MAX, a benchmark of 8,000 paired cases spanning eight types of changes to geometry, observations, appearance, clutter, and paths. Each pair compares task execution with and without a mid-task event, holding the task, initial state, policy seed, and pre-event action sequ...

</details>

<details>
<summary>Share</summary>

```
LIBERO-MAX: Do Robot Policies Adapt When the World Changes?

Robots must often continue a task after a target moves, the viewpoint shifts, or an obstacle appears, even though their earlier observations and committed actions reflect the previous scene.

arXiv: https://arxiv.org/abs/2609.36518
Project page: https://liberomax.github.io

#VLA #robotics
```

</details>

---

### [V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents](https://arxiv.org/abs/2609.37250)

**Authors:** Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Jiayu Hu, Xiu Yuan et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.37250) | [PDF](https://arxiv.org/pdf/2609.37250) | [Code](https://github.com/breez3young/VJEPA-Policy)

<details>
<summary>Abstract</summary>

World-action models (WAMs) couple future visual-state prediction with action generation. By adapting video generators or image-editing models pretrained at scale, a prominent line of recent WAMs inherits both predictive knowledge and the models in which it was learned. We ask whether a predictive visual latent space induced by large-scale predictive pretraining can instead provide a sufficient foundation for effective WAM learning without inheriting a complete pretrained visual generative model. To answer this question, we introduce V-JEPA Policy, a simple framework that builds a WAM on the la...

</details>

<details>
<summary>Share</summary>

```
V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents

World-action models (WAMs) couple future visual-state prediction with action generation.

arXiv: https://arxiv.org/abs/2609.37250
Code: https://github.com/breez3young/VJEPA-Policy

#VLA #robotics
```

</details>

---

### [T$^2$Mem: Learning Test-Time Memory for Robotics](https://arxiv.org/abs/2609.36720)

**Authors:** Yize Liu, Huang Huang, Yining Hong, Zijian Du, Zhi Cao et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2609.36720) | [PDF](https://arxiv.org/pdf/2609.36720) | [Project Page](https://yzliu84.github.io/T2MEM-project/)

<details>
<summary>Abstract</summary>

Memory-dependent robotic manipulation requires policies to use information that is no longer available in the current observation. Retaining history alone is insufficient: memory must preserve information that supports future actions. One challenge is whether a memory-free foundation model can learn to retain and use historical information from action demonstrations alone, without external memory support. We introduce T$^2$Mem, a framework that develops this capability within a pretrained vision-language-action policy, without external reasoning models or memory-specific annotations. T$^2$Mem...

</details>

<details>
<summary>Share</summary>

```
T$^2$Mem: Learning Test-Time Memory for Robotics

Memory-dependent robotic manipulation requires policies to use information that is no longer available in the current observation.

arXiv: https://arxiv.org/abs/2609.36720
Project page: https://yzliu84.github.io/T2MEM-project/

#VLA #robotics
```

</details>

---

### [Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination](https://arxiv.org/abs/2610.02626)

**Authors:** Shenglan Li, Zhendong Mi, Hengyi Zhu, Jingwu Luo, Chun Kit Chan et al. (9 authors)

**Published:** 2026-10-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02626) | [PDF](https://arxiv.org/pdf/2610.02626)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models increasingly incorporate intermediate reasoning to improve robotic manipulation, yet existing approaches primarily reason about observed states without explicitly anticipating future scene evolution. Extending such reasoning to explicit future rollouts at every inference step, however, introduces substantial computational overhead. We propose IG-VLA, a VLA reasoning framework that enables models to imagine the future and internalize the gist. Our Latent Spatiotemporal Reasoning learns to imagine task-relevant future scene evolution directly in visual represe...

</details>

<details>
<summary>Share</summary>

```
Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination

Vision-language-action (VLA) models increasingly incorporate intermediate reasoning to improve robotic manipulation, yet existing approaches primarily reason about observed states without explicitly anticipating futur...

arXiv: https://arxiv.org/abs/2610.02626

#VLA #robotics
```

</details>

---

### [WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325)

**Authors:** Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu et al. (8 authors)

**Published:** 2026-09-30 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.40325) | [PDF](https://arxiv.org/pdf/2609.40325)

<details>
<summary>Abstract</summary>

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close coupling of two distinct capabilities: action, to navigate the 3D world and search for anomalies system...

</details>

<details>
<summary>Share</summary>

```
WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents

As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, tr...

arXiv: https://arxiv.org/abs/2609.40325

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

### [Grounded in Time: A Multi-Source Dataset and Benchmark for Temporal Grounding in Robotic Manipulation](https://arxiv.org/abs/2610.04255)

**Authors:** Yi Wang, Yang Yang, Guangqi Xu, Sumin Lin, Ning Kang et al. (12 authors)

**Published:** 2026-10-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.04255) | [PDF](https://arxiv.org/pdf/2610.04255)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires inferring task-relevant states from past interactions when the current observation alone is insufficient to determine the appropriate action. Despite progress in benchmarking memory-augmented vision-language-action (VLA) models, application-oriented tasks requiring history-dependent semantic inference remain underrepresented. We introduce GiT (Grounded in Time), a dataset and benchmark for grounding manipulation decisions in past events across biolaboratory, household, and industrial scenarios. It includes real-robot and Universal Manipulation Interface (UMI...

</details>

<details>
<summary>Share</summary>

```
Grounded in Time: A Multi-Source Dataset and Benchmark for Temporal Grounding in Robotic Manipulation

Robotic manipulation often requires inferring task-relevant states from past interactions when the current observation alone is insufficient to determine the appropriate action.

arXiv: https://arxiv.org/abs/2610.04255

#VLA #robotics
```

</details>

---

### [SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation](https://arxiv.org/abs/2610.02804)

**Authors:** Xingxin He, Yuxuan Jiang, Haonan Zhang, Chuhan Cui, Kaile Li et al. (8 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.02804) | [PDF](https://arxiv.org/pdf/2610.02804)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models often require costly real-world demonstrations to adapt to contact-rich manipulation tasks, particularly when generalization across object placements is needed. We propose SARI (Simulated Approach, Real Interaction), a phase-split sim-and-real co-training framework built on a simple insight: spatial coverage and contact physics should be acquired from the domains best suited to them. Specifically, free-space approaches require spatial diversity but tolerate modest simulation gaps, making them ideal for synthetic generation; conversely, contact interactions d...

</details>

<details>
<summary>Share</summary>

```
SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation

Vision-language-action (VLA) models often require costly real-world demonstrations to adapt to contact-rich manipulation tasks, particularly when generalization across object placements is needed.

arXiv: https://arxiv.org/abs/2610.02804

#VLA #robotics
```

</details>

---

### [UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054)

**Authors:** Wenxuan Song, Jiayi Chen, Jingbo Wang, Shuai Zhou, Xicheng Gong et al. (16 authors)

**Published:** 2026-10-01 (updated 2026-10-03) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.02054) | [PDF](https://arxiv.org/pdf/2610.02054)

<details>
<summary>Abstract</summary>

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified architecture that integrates a physical reasoner, a world generator, and an action predictor to jointly learn semantic understanding of the physical world, visual generation, and action predi...

</details>

<details>
<summary>Share</summary>

```
UniWAM: Unified World-Action Model

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics.

arXiv: https://arxiv.org/abs/2610.02054

#VLA #robotics
```

</details>

---

### [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939)

**Authors:** Ruiyang Si, Jianxin Bi, Shunyu Yang, Rui Ni, Wenbo Huang et al. (12 authors)

**Published:** 2026-10-01 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.01939) | [PDF](https://arxiv.org/pdf/2610.01939)

<details>
<summary>Abstract</summary>

Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead. We introduce PyRUA-Lean, an interactive code-execution framework that couples feedback-driven primitive composition with selective observation: the agent composes classical robot primitives and learned vision-language-action (VLA) policies into Python cells that perform conditional checks and local retries, returning only explicitly requested images and state feedback for replanning. Across 700 simulated...

</details>

<details>
<summary>Share</summary>

```
Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead.

arXiv: https://arxiv.org/abs/2610.01939

#VLA #robotics
```

</details>

---

### [Tactile Curiosity Drives Robot Interaction](https://arxiv.org/abs/2609.40134)

**Authors:** Klemens Iten, Alexander Proshkin, Bhavya Sukhija, Stelian Coros, Andreas Krause et al. (7 authors)

**Published:** 2026-09-30 (updated 2026-10-02) | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.40134) | [PDF](https://arxiv.org/pdf/2609.40134)

<details>
<summary>Abstract</summary>

Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient. The most common RL algorithms rely on random action sampling to discover new strategies, resulting in agents that allocate most of their training budget to motions in free space, away from the contacts from which manipulation skills emerge. Existing intrinsic motivation methods based on model disagreement or epistemic uncertainty improve on isotropic noise, but they can also reward uncertainty in functionally irrelevant transitions, such as erratic motions in free space. In this work, we arg...

</details>

<details>
<summary>Share</summary>

```
Tactile Curiosity Drives Robot Interaction

Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient.

arXiv: https://arxiv.org/abs/2609.40134

#VLA #robotics
```

</details>

---

### [Discrete Forcing: Infusing Discrete Guidance into Continuous Denoising for Few-Step Action Experts](https://arxiv.org/abs/2609.39526)

**Authors:** Jingbo Wang, Wenxuan Song, Wenhao Yu, Han Zhao, Xi Wang et al. (9 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.39526) | [PDF](https://arxiv.org/pdf/2609.39526)

<details>
<summary>Abstract</summary>

Efficient action generation in vision-language-action (VLA) models requires capturing both coarse action structure and fine-grained details. Discrete action tokens provide compact structural representations but sacrifice precision, while continuous action tokens offer high precision but often require multiple denoising steps. We introduce Discrete Forcing, a flow-matching framework that combines these representations through an explicit coarse-to-fine generation process. It first predicts discrete action tokens to establish a coarse action structure, then uses them to guide continuous action r...

</details>

<details>
<summary>Share</summary>

```
Discrete Forcing: Infusing Discrete Guidance into Continuous Denoising for Few-Step Action Experts

Efficient action generation in vision-language-action (VLA) models requires capturing both coarse action structure and fine-grained details.

arXiv: https://arxiv.org/abs/2609.39526

#VLA #robotics
```

</details>

---

### [EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation](https://arxiv.org/abs/2609.37181)

**Authors:** Jin Chen, Yiming Jiang, Chongyang Xu, Modi Shi, Shijia Peng et al. (11 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2609.37181) | [PDF](https://arxiv.org/pdf/2609.37181)

<details>
<summary>Abstract</summary>

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid skill transfer framework for coordinated whole-body loco-manipulation. At its core, coarse-to-fine action alignment combines kinematic reference correction with dynamics-aware refinement. It improves end-effector pose accuracy while pre...

</details>

<details>
<summary>Share</summary>

```
EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation.

arXiv: https://arxiv.org/abs/2609.37181

#VLA #robotics
```

</details>

---

### [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)

**Authors:** Ke Zhang, Danica J. Sutherland, Chao Liu

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38401) | [PDF](https://arxiv.org/pdf/2609.38401)

<details>
<summary>Abstract</summary>

Training data variation, whether through designing a domain randomization (DR) scheme in simulation or curating demonstrations for imitation learning, is a primary lever for improving the robustness of robotic manipulation policies. Yet its underlying mechanisms remain poorly understood, and practitioners typically select randomization parameters through expensive trial and error. We investigate these mechanisms through a series of case studies, randomizing object size, color, and type as well as scene lighting and linguistic prompts across settings including pick-and-place RL in ManiSkill and...

</details>

<details>
<summary>Share</summary>

```
Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation

Training data variation, whether through designing a domain randomization (DR) scheme in simulation or curating demonstrations for imitation learning, is a primary lever for improving the robustness of robotic manipul...

arXiv: https://arxiv.org/abs/2609.38401

#VLA #robotics
```

</details>

---

### [Rho: A Foundation for Efficiently Adaptable VLA Models](https://arxiv.org/abs/2609.38164)

**Authors:** Rho Team, Simran Bagaria, Daphne Chen, Dean Fortier, Jianlong Fu et al. (14 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.38164) | [PDF](https://arxiv.org/pdf/2609.38164)

<details>
<summary>Abstract</summary>

General-purpose physical AI models must combine broad visual and linguistic capabilities with precise control across robot embodiments and efficient adaptation to downstream tasks. We introduce Rho, a family of open-weights VLA models for bimanual manipulation designed for data-light task adaptation on 3 embodiments representative of dual-arm robots across research labs and the industry -- YAM Box, UR AI Trainer, and FR3 Duo. We systematically ablate Rho's action-expert architecture and training recipe, and show in controlled simulation and physical-robot experiments that embodiment midtrainin...

</details>

<details>
<summary>Share</summary>

```
Rho: A Foundation for Efficiently Adaptable VLA Models

General-purpose physical AI models must combine broad visual and linguistic capabilities with precise control across robot embodiments and efficient adaptation to downstream tasks.

arXiv: https://arxiv.org/abs/2609.38164

#VLA #robotics
```

</details>

---

### [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078)

**Authors:** Bingxuan Li, Siqi Song, Yizhuo Wu, Jiarui Yao, Tong Zhang et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.38078) | [PDF](https://arxiv.org/pdf/2609.38078)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from benefiting directly from rapidly advancing general-purpose vision-language models (VLMs). In parallel, recent agentic robotic systems leverage VLMs for high-level reasoning or coding agents for robot control, but often depend on extensive external models and tools, introducing additional complexity and cost. This motivates us to ask: Can a general-purpose VLM itself operate a robot mo...

</details>

<details>
<summary>Share</summary>

```
MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation

Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from bene...

arXiv: https://arxiv.org/abs/2609.38078

#VLA #robotics
```

</details>

---

### [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation](https://arxiv.org/abs/2609.37530)

**Authors:** Shuhong Liu, Heng Zhou, Lingfeng Qian, Yuhao Fang, Xianbao Hou et al. (10 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37530) | [PDF](https://arxiv.org/pdf/2609.37530)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop. We systematically examine the consequences of this overlooked design choice across five fundamental ISP dimensions: gain, sensor noise, chromatic response, tonal response, and bit depth. Our analysis reveals that RAW-to-RGB processing materially shapes both action prediction and manipulation success, with different ISP dimensions exerting substantially different effects. Guided by these findings, we i...

</details>

<details>
<summary>Share</summary>

```
RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop.

arXiv: https://arxiv.org/abs/2609.37530

#VLA #robotics
```

</details>

---

### [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](https://arxiv.org/abs/2609.37150)

**Authors:** Tianhang Pan, Xuanhao Wang, Yiwen Pang, Bo Zhou, Jun Yang et al. (7 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title

**Links:** [arXiv](https://arxiv.org/abs/2609.37150) | [PDF](https://arxiv.org/pdf/2609.37150)

<details>
<summary>Abstract</summary>

VLAs combine pretrained vision-language representations with action generation to enable language-guided control across diverse tasks, becoming a mainstream paradigm in embodied intelligence. However, multiple studies have reported VLA's substantial declines in task success under camera shifts, revealing a key vulnerability that limits reliable deployment. To address this vulnerability, existing methods collect paired observations of the same scene from different viewpoints to fine-tune the VLA or train visual adaptation modules. Unfortunately, they require additional data collection and VLA t...

</details>

<details>
<summary>Share</summary>

```
CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

VLAs combine pretrained vision-language representations with action generation to enable language-guided control across diverse tasks, becoming a mainstream paradigm in embodied intelligence.

arXiv: https://arxiv.org/abs/2609.37150

#VLA #robotics
```

</details>

---

### [LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks](https://arxiv.org/abs/2609.36774)

**Authors:** Zeming Wei, Jianheng Ye, Xinshuai Song, Sirui Chen, Yang Liu et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.36774) | [PDF](https://arxiv.org/pdf/2609.36774)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models struggle to reuse recurring interactions in unseen tasks. Our diagnostic study reveals that reliable task completion does not imply consistent execution of constituent atomic actions across task contexts. We present LexiconVLA, a retrievable atomic-action lexicon for cross-task reuse. Global and detail codebooks capture shared interaction structure and fine-grained execution variation, respectively, preserving both reusable patterns and execution details. Visual-Atomic Action Alignment couples trajectory reconstruction from visual state changes with visual o...

</details>

<details>
<summary>Share</summary>

```
LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks

Vision-language-action (VLA) models struggle to reuse recurring interactions in unseen tasks.

arXiv: https://arxiv.org/abs/2609.36774

#VLA #robotics
```

</details>

---

### [Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving](https://arxiv.org/abs/2609.37046)

**Authors:** Katharina Winter, Stefan Englmeier, Fabian B. Flohr

**Published:** 2026-09-29 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2609.37046) | [PDF](https://arxiv.org/pdf/2609.37046)

<details>
<summary>Abstract</summary>

Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized. We study velocity understanding as a controlled diagnostic across three tasks: surrounding-agent speed, current ego speed, and short-horizon future ego-speed proposal. On nuScenes, we evaluate open-weight general-purpose and PhysicalAI VLMs, together with the driving-oriented Alpamayo-1.5 Vision-Language-Action model, using multiple input and output formulations. We combine verbal evaluation with temporal perturb...

</details>

<details>
<summary>Share</summary>

```
Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving

Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized.

arXiv: https://arxiv.org/abs/2609.37046

#VLA #robotics
```

</details>

---

### [RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer](https://arxiv.org/abs/2610.02717)

**Authors:** Chenxi Li, Zhangrui Zhao, Rui Li, Yuan Gao, Kehui Liu et al. (11 authors)

**Published:** 2026-10-02 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.02717) | [PDF](https://arxiv.org/pdf/2610.02717)

<details>
<summary>Abstract</summary>

A key challenge in bringing embodied intelligence into the real world is transferring capabilities from simulation to reality and enabling agents to continually adapt after deployment. End-to-end vision-language-action policies provide strong manipulation capabilities, but their transfer to physical environments typically relies on calibrating simulated visual and dynamical conditions, collecting additional target-domain demonstrations, and optimizing the policy through further training. Tool-using embodied agents offer flexible task orchestration, yet existing systems primarily emphasize task...

</details>

<details>
<summary>Share</summary>

```
RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer

A key challenge in bringing embodied intelligence into the real world is transferring capabilities from simulation to reality and enabling agents to continually adapt after deployment.

arXiv: https://arxiv.org/abs/2610.02717

#VLA #robotics
```

</details>

---

### [PrefPI: Preference-Guided Steering into Out-of-Distribution Behaviors](https://arxiv.org/abs/2609.40165)

**Authors:** Seungeun Rho, Wontaek Kim, Danfei Xu, Sehoon Ha

**Published:** 2026-09-30 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.40165) | [PDF](https://arxiv.org/pdf/2609.40165)

<details>
<summary>Abstract</summary>

We present PrefPI (Preference-Guided Policy Iteration), an iterative framework for steering pretrained generative robot policies using only relative preferences over self-generated trajectories. Unlike prior preference-learning methods that primarily sharpen modes already represented by the policy, we study steering beyond the initial effective support, where desired behaviors are rarely or never observed under the initial policy. Our key idea is to formulate preference learning as preference-conditioned generative modeling: preferred trajectories define a conditional distribution, whose densi...

</details>

<details>
<summary>Share</summary>

```
PrefPI: Preference-Guided Steering into Out-of-Distribution Behaviors

We present PrefPI (Preference-Guided Policy Iteration), an iterative framework for steering pretrained generative robot policies using only relative preferences over self-generated trajectories.

arXiv: https://arxiv.org/abs/2609.40165

#VLA #robotics
```

</details>

---

### [PRICE the Action Chunks: Physical Relational Credit Assignment for Embodied Reinforcement Learning](https://arxiv.org/abs/2609.38890)

**Authors:** Yangang Zou, Jiajun Lu, Weitao Zhou, Haibao Yu, Bozhou Zhang et al. (9 authors)

**Published:** 2026-09-30 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.38890) | [PDF](https://arxiv.org/pdf/2609.38890)

<details>
<summary>Abstract</summary>

Outcome-based reinforcement learning (RL) post-trains vision--language--action policies using terminal success signals, but assigns the same trajectory-level advantage to every action chunk. A failed episode can thus penalize useful early actions as if they caused the failure. Existing approaches seek finer-grained feedback through learned evaluators, adding task-specific supervision or additional model training. We explore, for the first time to our knowledge, whether physical relations across trajectories can provide action-chunk credit in embodied RL from terminal outcomes alone, without an...

</details>

<details>
<summary>Share</summary>

```
PRICE the Action Chunks: Physical Relational Credit Assignment for Embodied Reinforcement Learning

Outcome-based reinforcement learning (RL) post-trains vision--language--action policies using terminal success signals, but assigns the same trajectory-level advantage to every action chunk.

arXiv: https://arxiv.org/abs/2609.38890

#VLA #robotics
```

</details>

---

### [WayFinder: Hierarchical Visual-Language-Action for Zero-Shot Waypoint Generation and Low-Level Kinematic Control](https://arxiv.org/abs/2609.37922)

**Authors:** Timothy K Johnsen, Marco Levorato

**Published:** 2026-09-29 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.37922) | [PDF](https://arxiv.org/pdf/2609.37922)

<details>
<summary>Abstract</summary>

Visual Language Action (VLA) models offer unprecedented generalization for autonomous robots; however, their real-world deployment is frequently bottlenecked by unreliable execution and the prohibitive computational cost of fine-tuning for specific robot embodiments and tasks. To bridge this gap, we propose WayFinder, an end-to-end, closed-loop hierarchical VLA framework that circumvents the need for fine-tuning by decoupling high-level task reasoning from low-level kinematic control. WayFinder utilizes a zero-shot, offboard Multimodal Large Language Model (MLLM) policy to process linguistic c...

</details>

<details>
<summary>Share</summary>

```
WayFinder: Hierarchical Visual-Language-Action for Zero-Shot Waypoint Generation and Low-Level Kinematic Control

Visual Language Action (VLA) models offer unprecedented generalization for autonomous robots; however, their real-world deployment is frequently bottlenecked by unreliable execution and the prohibitive computational c...

arXiv: https://arxiv.org/abs/2609.37922

#VLA #robotics
```

</details>

---

### [Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks](https://arxiv.org/abs/2609.36471)

**Authors:** Guoheng Sun, Chen Chen, Jin Wang, Ang Li, Teresa Lv

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.36471) | [PDF](https://arxiv.org/pdf/2609.36471)

<details>
<summary>Abstract</summary>

World-Action Models (WAMs) improve robotic manipulation by conditioning action generation on predicted future observations, but future prediction adds further inference overhead to already expensive iterative action generation. Action chunking can amortize this cost over multiple actions, yet performance degrades over long execution horizons because later actions remain conditioned on stale observations. We introduce STAIRCASE POLICY, a streaming inference and training framework that turns a flow-matching VLA into a JEPA-style WAM and partitions a large action chunk into sub-chunks at staggere...

</details>

<details>
<summary>Share</summary>

```
Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks

World-Action Models (WAMs) improve robotic manipulation by conditioning action generation on predicted future observations, but future prediction adds further inference overhead to already expensive iterative action g...

arXiv: https://arxiv.org/abs/2609.36471

#VLA #robotics
```

</details>

---

### [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](https://arxiv.org/abs/2609.37810)

**Authors:** Sicheng Xie, Yitong Chen, Haidong Cao, Shunlin Lu, Zuxuan Wu et al. (6 authors)

**Published:** 2026-09-29 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2609.37810) | [PDF](https://arxiv.org/pdf/2609.37810)

<details>
<summary>Abstract</summary>

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging. More recently, general-purpose multimodal agents have shown great potential for zero-shot robotic task solving. However, they often incur high execution costs by reasoning and exploring the physical world from scratch. To reduce these costs, we introduce RoboSkill, a framework that connects skill acquisition and reuse through an Explore, Execute, Evolve loop. Within this loop, the agent explores to gather task-relevant information, execut...

</details>

<details>
<summary>Share</summary>

```
Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging.

arXiv: https://arxiv.org/abs/2609.37810

#VLA #robotics
```

</details>

---

### [What to Preserve in Recursive Computation: A Local Predictive Sufficiency Principle](https://arxiv.org/abs/2610.04303)

**Authors:** Peilin Wang, Feng Shiyang, Hongfu Gao, Cencheng Zhao, Di Yuan et al. (7 authors)

**Published:** 2026-10-03 | **Categories:** cs.LG, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.04303) | [PDF](https://arxiv.org/pdf/2610.04303)

<details>
<summary>Abstract</summary>

Recursive computation repeatedly compresses or reuses intermediate states, creating a simple tension: information that must remain useful across longer recursive paths is also exposed to more opportunities for loss before reaching the final prediction. Existing reconstruction or local-prediction objectives provide tractable supervision, but do not ensure that the retained information remains sufficient for subsequent recursive computation. We identify local predictive sufficiency with recursive predictive closure: controlling local predictive deficiencies at individual interfaces controls the...

</details>

<details>
<summary>Share</summary>

```
What to Preserve in Recursive Computation: A Local Predictive Sufficiency Principle

Recursive computation repeatedly compresses or reuses intermediate states, creating a simple tension: information that must remain useful across longer recursive paths is also exposed to more opportunities for loss be...

arXiv: https://arxiv.org/abs/2610.04303

#VLA #robotics
```

</details>

---
