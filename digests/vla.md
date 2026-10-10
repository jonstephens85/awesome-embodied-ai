# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-10-10 01:23 UTC

**Papers shown:** 85 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation](https://arxiv.org/abs/2610.12451)

**Authors:** Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12451) | [PDF](https://arxiv.org/pdf/2610.12451) | [Project Page](https://boyaohan.github.io/VersaCamVLA.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-A...

</details>

<details>
<summary>Share</summary>

```
VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pos...

arXiv: https://arxiv.org/abs/2610.12451
Project page: https://boyaohan.github.io/VersaCamVLA.github.io/

#VLA #robotics
```

</details>

---

### [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models](https://arxiv.org/abs/2610.12007)

**Authors:** Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren et al. (11 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12007) | [PDF](https://arxiv.org/pdf/2610.12007) | [Project Page](https://react-vla.github.io)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon...

</details>

<details>
<summary>Share</summary>

```
REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, wherea...

arXiv: https://arxiv.org/abs/2610.12007
Project page: https://react-vla.github.io

#VLA #robotics
```

</details>

---

### [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526)

**Authors:** Mikey Watts, Yuchen Cui

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CL, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10526) | [PDF](https://arxiv.org/pdf/2610.10526) | [Project Page](https://sttawm.github.io/rephrase-before-you-act)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmentation still shows swings of up to 61 points. We characterize this sensitivity with statistically tested single-edit swings and an oracle phrase search, which shows that phrasing alone nearly closes the...

</details>

<details>
<summary>Share</summary>

```
Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on.

arXiv: https://arxiv.org/abs/2610.10526
Project page: https://sttawm.github.io/rephrase-before-you-act

#VLA #robotics
```

</details>

---

### [Juno: Taming Predictive Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.09940)

**Authors:** Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Also relevant to:** World Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09940) | [PDF](https://arxiv.org/pdf/2610.09940) | [Project Page](https://juno-policy.github.io/)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predict...

</details>

<details>
<summary>Share</summary>

```
Juno: Taming Predictive Latents for Vision-Language-Action Models

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2610.09940
Project page: https://juno-policy.github.io/

#VLA #robotics
```

</details>

---

### [VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.08133)

**Authors:** Owen Du, Yang Yue, Jie Zhang, Jiaqi Pi, Chi Bene Chen et al. (6 authors)

**Published:** 2026-10-06 (updated 2026-10-08) | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.08133) | [PDF](https://arxiv.org/pdf/2610.08133) | [Code](https://github.com/du-owen/VLA-ACL)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment. Visual token pruning offers a direct solution, as visual patches dominate the input sequence and contain considerable redundancy. Existing approaches, however, either rely on indirect training-free heuristics, such as attention scores and motion thresholds, or require costly fine-tuning of the base VLA model. We introduce VLA-ACL (Action Consistency Learning), which learns a lightweight...

</details>

<details>
<summary>Share</summary>

```
VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models

Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment.

arXiv: https://arxiv.org/abs/2610.08133
Code: https://github.com/du-owen/VLA-ACL

#VLA #robotics
```

</details>

---

### [StairVLA: Stage-Aware Hierarchical Action Generation for Vision-Language-Action Models](https://arxiv.org/abs/2610.07756)

**Authors:** Shangyuan Yuan, Xinda Qi, Yujiang Pu, Wenliang Guo, Xiaobo Tan

**Published:** 2026-10-06 (updated 2026-10-07) | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.07756) | [PDF](https://arxiv.org/pdf/2610.07756) | [Project Page](https://dicomsky.github.io/projects/stairvla)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models increasingly rely on diffusion- or flow-matching-based action heads to generate continuous robot actions. These action heads typically process the denoising trajectory in a largely uniform manner. However, we observe that the conditioning focus naturally shifts across denoising stages: early stages combine language instructions and visual observations to establish a coarse action trajectory, whereas later stages place greater emphasis on current visual observations for action alignment. Based on this insight, we introduce StairVLA, a stage-aware hierarchical...

</details>

<details>
<summary>Share</summary>

```
StairVLA: Stage-Aware Hierarchical Action Generation for Vision-Language-Action Models

Vision-language-action (VLA) models increasingly rely on diffusion- or flow-matching-based action heads to generate continuous robot actions.

arXiv: https://arxiv.org/abs/2610.07756
Project page: https://dicomsky.github.io/projects/stairvla

#VLA #robotics
```

</details>

---

### [When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models](https://arxiv.org/abs/2610.05719)

**Authors:** Seonghoon Yu, Dongwon Kim, HyungRok Jung, Yoonjae Baek, Byung-kwan Lee et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

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

### [CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding](https://arxiv.org/abs/2610.11971)

**Authors:** Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11971) | [PDF](https://arxiv.org/pdf/2610.11971) | [Project Page](https://capable-vla.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that mot...

</details>

<details>
<summary>Share</summary>

```
CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed.

arXiv: https://arxiv.org/abs/2610.11971
Project page: https://capable-vla.github.io/

#VLA #robotics
```

</details>

---

### [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models](https://arxiv.org/abs/2610.11508)

**Authors:** Junmyeong Lee, Dongmin Shin, Min-Gyu Park, Wooseok Jeon, Inho Chang et al. (6 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11508) | [PDF](https://arxiv.org/pdf/2610.11508)

<details>
<summary>Abstract</summary>

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration. The problem becomes more evident in cross-setup deployment, as reproducing the exact camera pose used for training is nearly impossible. Unlike fixed external views, wrist views are more challenging because the camera moves with the robot, causing even small mounting variations to alter fine-grained geometric cues. To address this, we propose WARP-VLA, a camera-view robust VLA for diverse wrist camera configurations. WARP-VLA adopts a...

</details>

<details>
<summary>Share</summary>

```
WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration.

arXiv: https://arxiv.org/abs/2610.11508

#VLA #robotics
```

</details>

---

### [SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation](https://arxiv.org/abs/2610.11248)

**Authors:** Kyoungin Baik, Youngwoon Lee

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11248) | [PDF](https://arxiv.org/pdf/2610.11248) | [Project Page](https://kyounginbaik.github.io/simvla/)

<details>
<summary>Abstract</summary>

Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework that trains VLAs entirely on synthetic simulation data without teleoperation for mobile manipulation. SimVLA is first pre-trained on two complementary simulation-derived datasets: SimAction, a large-scale robot action dataset spanning 35 diver...

</details>

<details>
<summary>Share</summary>

```
SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation

Large-scale, diverse datasets have driven the success of LLMs and VLMs.

arXiv: https://arxiv.org/abs/2610.11248
Project page: https://kyounginbaik.github.io/simvla/

#VLA #robotics
```

</details>

---

### [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](https://arxiv.org/abs/2610.09718)

**Authors:** Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu, Hanlong Li, Tatsuya Matsushima et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09718) | [PDF](https://arxiv.org/pdf/2610.09718) | [Project Page](https://yubi-stag.airoa.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grounding that automatically enriches manipulation demonstrations with interaction-rich semantics to ali...

</details>

<details>
<summary>Share</summary>

```
YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions.

arXiv: https://arxiv.org/abs/2610.09718
Project page: https://yubi-stag.airoa.io/

#VLA #robotics
```

</details>

---

### [TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks](https://arxiv.org/abs/2610.09462)

**Authors:** Zirun Zhou, Jingfeng Zhang, HaoChuan Xu, Xizhe Zhang, Elliott Wen et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09462) | [PDF](https://arxiv.org/pdf/2610.09462) | [Project Page](https://zzr42.github.io/tmt/)

<details>
<summary>Abstract</summary>

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears. Detecting such activation is difficult because malicious behavior can comprise individually plausible actions, while unfamiliar tasks introduce legitimate changes in observations and behavior. We introduce TMT, a runtime backdoor detector based on Token Manifold and latent Transition modeling. Trained on benign rollouts, its two branches assess input-token structure and prediction errors in adjacent-layer latent dynamics. A suspicious rollout identifie...

</details>

<details>
<summary>Share</summary>

```
TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears.

arXiv: https://arxiv.org/abs/2610.09462
Project page: https://zzr42.github.io/tmt/

#VLA #robotics
```

</details>

---

### [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09451)

**Authors:** Yeonseo Lee, Hyosup Shin, Guebin Hwang, Sungho Jo

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09451) | [PDF](https://arxiv.org/pdf/2610.09451) | [Project Page](https://lysees.github.io/tempobridge-page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextual VLM representations, aligns them with task progress through a causal phase router, and modulates n...

</details>

<details>
<summary>Share</summary>

```
TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly.

arXiv: https://arxiv.org/abs/2610.09451
Project page: https://lysees.github.io/tempobridge-page/

#VLA #robotics
```

</details>

---

### [How (and How Not) to Use Data Augmentation in VLA Post-Training](https://arxiv.org/abs/2610.05994)

**Authors:** Bram Grooten, Joaquin Vanschoren

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page

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

### [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](https://arxiv.org/abs/2610.12090)

**Authors:** Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12090) | [PDF](https://arxiv.org/pdf/2610.12090)

<details>
<summary>Abstract</summary>

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and...

</details>

<details>
<summary>Share</summary>

```
Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions.

arXiv: https://arxiv.org/abs/2610.12090

#VLA #robotics
```

</details>

---

### [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](https://arxiv.org/abs/2610.10390)

**Authors:** Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10390) | [PDF](https://arxiv.org/pdf/2610.10390) | [Code](https://github.com/TabGuigui/GeoCoTDrive)

<details>
<summary>Abstract</summary>

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critic...

</details>

<details>
<summary>Share</summary>

```
Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving.

arXiv: https://arxiv.org/abs/2610.10390
Code: https://github.com/TabGuigui/GeoCoTDrive

#VLA #robotics
```

</details>

---

### [ARC: A Reasoning Recipe for Robot Foundation Models](https://arxiv.org/abs/2610.12386)

**Authors:** Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12386) | [PDF](https://arxiv.org/pdf/2610.12386) | [Project Page](https://arc-robot-reasoning.github.io/)

<details>
<summary>Abstract</summary>

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces s...

</details>

<details>
<summary>Share</summary>

```
ARC: A Reasoning Recipe for Robot Foundation Models

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale.

arXiv: https://arxiv.org/abs/2610.12386
Project page: https://arc-robot-reasoning.github.io/

#VLA #robotics
```

</details>

---

### [PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.12285)

**Authors:** Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen et al. (14 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12285) | [PDF](https://arxiv.org/pdf/2610.12285)

<details>
<summary>Abstract</summary>

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented representation space, reducing the need to predict control-irrelevant visual details. Built on a Mixture-of-Transformers architecture, PLaW-VLA conditions action generation on observation history, current task semantics, and predicted future stat...

</details>

<details>
<summary>Share</summary>

```
PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and...

arXiv: https://arxiv.org/abs/2610.12285

#VLA #robotics
```

</details>

---

### [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](https://arxiv.org/abs/2610.12185)

**Authors:** Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12185) | [PDF](https://arxiv.org/pdf/2610.12185) | [Code](https://github.com/JIA-Lab-research/RESETTLE)

<details>
<summary>Abstract</summary>

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery w...

</details>

<details>
<summary>Share</summary>

```
RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors.

arXiv: https://arxiv.org/abs/2610.12185
Code: https://github.com/JIA-Lab-research/RESETTLE

#VLA #robotics
```

</details>

---

### [Tell Robot What Not to Do: A Negation Understanding Perspective](https://arxiv.org/abs/2610.11952)

**Authors:** Fazeng Li, Gan Sun, Hao Cheng, Weihong Ren, Yang Cong

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11952) | [PDF](https://arxiv.org/pdf/2610.11952)

<details>
<summary>Abstract</summary>

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-play framework that extends pretrained VLAs to follow negated instructions through image-language super...

</details>

<details>
<summary>Share</summary>

```
Tell Robot What Not to Do: A Negation Understanding Perspective

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction.

arXiv: https://arxiv.org/abs/2610.11952

#VLA #robotics
```

</details>

---

### [PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies](https://arxiv.org/abs/2610.11771)

**Authors:** Qing Huang, Yifei Yang, Ziqing Zou, Anzhe Chen, Zhenjie Zhu et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11771) | [PDF](https://arxiv.org/pdf/2610.11771)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace. This coupling complicates adaptation from teleoperation: useful geometric guidance comes with timing shaped by interface delays and operator behavior. Our key insight is to bring the path-time parameterization of classical motion planning into the learned action representation of a VLA. We introduce PathTime-VLA, which represents motion as a progress-indexed interaction path $X(s)$ and a positive interval-time profile. The latter defines a monoton...

</details>

<details>
<summary>Share</summary>

```
PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace.

arXiv: https://arxiv.org/abs/2610.11771

#VLA #robotics
```

</details>

---

### [Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning](https://arxiv.org/abs/2610.12231)

**Authors:** Yuchen Zhou, Jiacheng You, Weikang Wan, Weijun Dong, Yang Gao et al. (6 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12231) | [PDF](https://arxiv.org/pdf/2610.12231) | [Project Page](https://the-labone.github.io/regression-policy-project/)

<details>
<summary>Abstract</summary>

Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective of statistical modeling: how action-prediction residuals shape policy optimization. Our analysis of real-world robot demonstration data reveals substantial state-dependent variation in residual scales and heavier-than-Gaussian tails. While bo...

</details>

<details>
<summary>Share</summary>

```
Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning

Learning from demonstration has enabled impressive robot behaviors.

arXiv: https://arxiv.org/abs/2610.12231
Project page: https://the-labone.github.io/regression-policy-project/

#VLA #robotics
```

</details>

---

### [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](https://arxiv.org/abs/2610.10178)

**Authors:** Theodor Wulff, Angelo Cangelosi

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.10178) | [PDF](https://arxiv.org/pdf/2610.10178)

<details>
<summary>Abstract</summary>

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their Vision-Language model backbones. For this reason, we conduct a controlled mechanistic interpretabil...

</details>

<details>
<summary>Share</summary>

```
Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they...

arXiv: https://arxiv.org/abs/2610.10178

#VLA #robotics
```

</details>

---

### [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](https://arxiv.org/abs/2610.09496)

**Authors:** Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09496) | [PDF](https://arxiv.org/pdf/2610.09496)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened attention to task-relevant visual regions, and a mechanistic interpretation via sparse autoencoders...

</details>

<details>
<summary>Share</summary>

```
Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models.

arXiv: https://arxiv.org/abs/2610.09496

#VLA #robotics
```

</details>

---

### [Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228)

**Authors:** Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang et al. (7 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09228) | [PDF](https://arxiv.org/pdf/2610.09228) | [Project Page](https://robo-cop.pages.dev/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bo...

</details>

<details>
<summary>Share</summary>

```
Co-Evolving Robot Orchestrators and Policies through Deployment

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment.

arXiv: https://arxiv.org/abs/2610.09228
Project page: https://robo-cop.pages.dev/

#VLA #robotics
```

</details>

---

### [ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models](https://arxiv.org/abs/2610.08150)

**Authors:** Yuan Xu, Yixiang Chen, Qisen Ma, Jiabing Yang, Peiyan Li et al. (13 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.08150) | [PDF](https://arxiv.org/pdf/2610.08150)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a central paradigm for robot policy learning, which predict actions in three forms: raw action chunks, discrete action tokens, or continuous action latents. However, existing action representations primarily model action trajectories, with limited consideration of the visual dynamics induced by these actions. We introduce ViDAL, a Visual Dynamics-grounded Action Latent Space that anchors continuous action latents in the future visual dynamics of the scene. Specifically, ViDAL learns action latent space by training an Action Variational Autoencode...

</details>

<details>
<summary>Share</summary>

```
ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models

Vision-Language-Action (VLA) models have become a central paradigm for robot policy learning, which predict actions in three forms: raw action chunks, discrete action tokens, or continuous action latents.

arXiv: https://arxiv.org/abs/2610.08150

#VLA #robotics
```

</details>

---

### [Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution](https://arxiv.org/abs/2610.07946)

**Authors:** Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.07946) | [PDF](https://arxiv.org/pdf/2610.07946)

<details>
<summary>Abstract</summary>

Visual disruptions can arise while a robot is executing a task, leaving a vision-language-action (VLA) policy to respond without knowing the disruption type or timing. We introduce Self-supervised Adaptation from Leftover Trajectories (SALT), which uses the leftover trajectory, the unexecuted part of the previous action chunk, as self-supervision for test-time adaptation. Because consecutive chunks overlap in time, the leftover provides a temporally aligned target for the current prediction over the same future control interval. At the onset of a visual shift, the leftover can retain a plan fo...

</details>

<details>
<summary>Share</summary>

```
Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution

Visual disruptions can arise while a robot is executing a task, leaving a vision-language-action (VLA) policy to respond without knowing the disruption type or timing.

arXiv: https://arxiv.org/abs/2610.07946

#VLA #robotics
```

</details>

---

### [VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.06271)

**Authors:** Jaemin Kim, Jiahn Kim, Taesik Gong

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in title; code repo

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

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

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

### [RoboIRS: Inference-Time Internal Representation Steering for Generalist Robot Policies](https://arxiv.org/abs/2610.04681)

**Authors:** Jiuzhou Lei, Chang Liu, Dayou Li, Zhiyuan Zhang, Xiao Liang et al. (8 authors)

**Published:** 2026-10-03 (updated 2026-10-08) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

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

### [SWAP: Stepwise Action Policy Routing for Vision-Language-Action Models](https://arxiv.org/abs/2610.06926)

**Authors:** Mousumi Das, Aditeya Prajapati, Abrar Anwar, Jesse Thomason

**Published:** 2026-10-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.06926) | [PDF](https://arxiv.org/pdf/2610.06926)

<details>
<summary>Abstract</summary>

Robot manipulation systems using Vision-Language-Action (VLA) model backbones typically use just one VLA for task execution. However, individual VLAs do not perform well across different task states and environments. We introduce a framework for dynamically composing multiple VLA policies during execution: StepWise Action Policy Routing (SWAP). SWAP formulates policy routing as an offline reinforcement learning problem, learning a routing critic that selects the most appropriate policy at each decision step given the current observation. SWAP enables robots to select new policies to execute on...

</details>

<details>
<summary>Share</summary>

```
SWAP: Stepwise Action Policy Routing for Vision-Language-Action Models

Robot manipulation systems using Vision-Language-Action (VLA) model backbones typically use just one VLA for task execution.

arXiv: https://arxiv.org/abs/2610.06926

#VLA #robotics
```

</details>

---

### [PAIR: Bridging Perception and Action in Vision-Language-Action Models](https://arxiv.org/abs/2610.09016)

**Authors:** Kaixi Feng, Guoheng Sun, Ang li

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09016) | [PDF](https://arxiv.org/pdf/2610.09016)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Lat...

</details>

<details>
<summary>Share</summary>

```
PAIR: Bridging Perception and Action in Vision-Language-Action Models

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions.

arXiv: https://arxiv.org/abs/2610.09016

#VLA #robotics
```

</details>

---

### [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2610.05492)

**Authors:** Zixuan Liu, Joris Köster, Zizhan Zheng, Siavash Khajavi

**Published:** 2026-10-04 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

### [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](https://arxiv.org/abs/2610.12089)

**Authors:** Guoting Wei, Dawei Yan, Xia Yuan, Gengming Zhang, Yelin He et al. (13 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12089) | [PDF](https://arxiv.org/pdf/2610.12089)

<details>
<summary>Abstract</summary>

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction. Learning and evaluating these skills present three challenges: similar observations under a fixed task instruction may make skill selection ambiguous; even when a preceding skill succeeds, the robot state inherited by the next skill may deviate from its demonstrated starting states and affect execution; and task-level metrics hinder skill-specific diagnosis, while early failures leave later skills untested. We therefore...

</details>

<details>
<summary>Share</summary>

```
ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction.

arXiv: https://arxiv.org/abs/2610.12089

#VLA #robotics
```

</details>

---

### [Humanoid World Action Model With Joint State--Action Generation](https://arxiv.org/abs/2610.12026)

**Authors:** Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu et al. (10 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12026) | [PDF](https://arxiv.org/pdf/2610.12026)

<details>
<summary>Abstract</summary>

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robo...

</details>

<details>
<summary>Share</summary>

```
Humanoid World Action Model With Joint State--Action Generation

Humanoid robots are a promising platform for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2610.12026

#VLA #robotics
```

</details>

---

### [Experience-Guided Initiation Search for Learned Skills in Skill Composition](https://arxiv.org/abs/2610.11418)

**Authors:** Qixuan Li, Yanhong Zhao, Jincheng Yu

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11418) | [PDF](https://arxiv.org/pdf/2610.11418)

<details>
<summary>Abstract</summary>

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution. In skill composition, an initiation configuration affects not only the current skill but also the physical state passed to subsequent skills, so successful execution of an individual skill does not necessarily imply successful completion of the composed task. Estimating target-specific capability through extensive rollouts is costly in real-world deployment, while directly reusing historical experience can be unrelia...

</details>

<details>
<summary>Share</summary>

```
Experience-Guided Initiation Search for Learned Skills in Skill Composition

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution.

arXiv: https://arxiv.org/abs/2610.11418

#VLA #robotics
```

</details>

---

### [Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer](https://arxiv.org/abs/2610.11416)

**Authors:** Shuang Luo, Yilun Kong, Yunpeng Qing, Yihang Jiao, Zhi Hou et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.11416) | [PDF](https://arxiv.org/pdf/2610.11416)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs). However, such VLM backbones offer insufficient physical dynamics priors, which limits the generalization capabilities of robot policies. Recent efforts therefore integrate video-generation World Models (WMs) into robot policies through various strategies, using predictive dynamics to facilitate action generation. Despite these advances, harnessing semantic understanding and dynamics prediction as c...

</details>

<details>
<summary>Share</summary>

```
Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer

Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs).

arXiv: https://arxiv.org/abs/2610.11416

#VLA #robotics
```

</details>

---

### [VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving](https://arxiv.org/abs/2610.11161)

**Authors:** Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.11161) | [PDF](https://arxiv.org/pdf/2610.11161)

<details>
<summary>Abstract</summary>

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations. Although recent extensions enable temporal 3D prediction, their future evolution remains weakly conditioned on driving intentions and actions, limiting their ability to model alternative action-dependent futures. We propose VGGTWorld-VLA, an intention-conditioned extension of VGGT-World for controllable 3D world evolution in autonomous driving. First, we introduce an action--semantic conditioning mechanism that injects complementary driving semantics and ego-mot...

</details>

<details>
<summary>Share</summary>

```
VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations.

arXiv: https://arxiv.org/abs/2610.11161

#VLA #robotics
```

</details>

---

### [When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs](https://arxiv.org/abs/2610.10912)

**Authors:** Jasper Gerigk, Kenzo Aspuru-Takata, Chin-Hsuan Wu, Mohammad Mohammadi, Shuhong Zheng et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.10912) | [PDF](https://arxiv.org/pdf/2610.10912)

<details>
<summary>Abstract</summary>

Shortcut learning is a prevalent issue in robot learning. The limited diversity of robot demonstration datasets can mislead policies into exploiting spurious correlations between tasks and irrelevant features, such as viewpoint or background. Collecting sufficiently diverse robot demonstrations is costly and inefficient, motivating algorithmic alternatives. We focus on vision-language-action (VLA) models and discover that different vision-language model backbones exhibit substantially different levels of susceptibility to visual shortcut learning. We find that model behavior correlates with ou...

</details>

<details>
<summary>Share</summary>

```
When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs

Shortcut learning is a prevalent issue in robot learning.

arXiv: https://arxiv.org/abs/2610.10912

#VLA #robotics
```

</details>

---

### [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787)

**Authors:** Gengze Zhou, Yicong Hong, Jiazhao Zhang, Xunyi Zhao, Jian Zhou et al. (12 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10787) | [PDF](https://arxiv.org/pdf/2610.10787) | [Project Page](https://metacognitionai.github.io/NavGPT3/)

<details>
<summary>Abstract</summary>

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control. We present NavGPT-3, a harness that connects the two models, with an OS-like runtime built above it: reasoning, acting, and monitoring run as threads with their own context, tools, and permissions, while the runtime schedules them and deci...

</details>

<details>
<summary>Share</summary>

```
NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied a...

arXiv: https://arxiv.org/abs/2610.10787
Project page: https://metacognitionai.github.io/NavGPT3/

#VLA #robotics
```

</details>

---

### [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework](https://arxiv.org/abs/2610.10384)

**Authors:** Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao et al. (17 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10384) | [PDF](https://arxiv.org/pdf/2610.10384) | [Project Page](https://fvl-repo.github.io/OpenViTac/)

<details>
<summary>Abstract</summary>

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulation and the real world. OpenViTac organizes contact-rich manipulation into four tactile-relevant capab...

</details>

<details>
<summary>Share</summary>

```
OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world.

arXiv: https://arxiv.org/abs/2610.10384
Project page: https://fvl-repo.github.io/OpenViTac/

#VLA #robotics
```

</details>

---

### [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](https://arxiv.org/abs/2610.09943)

**Authors:** Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun et al. (8 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09943) | [PDF](https://arxiv.org/pdf/2610.09943)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternative strategies under distribution shifts. Inspired by this, we introduce DRIVE (Diversity-driven RL fI...

</details>

<details>
<summary>Share</summary>

```
Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited.

arXiv: https://arxiv.org/abs/2610.09943

#VLA #robotics
```

</details>

---

### [WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses](https://arxiv.org/abs/2610.08526)

**Authors:** Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2610.08526) | [PDF](https://arxiv.org/pdf/2610.08526)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and dataset for language-guided human search, localization, and tracking in warehouse environments. It conta...

</details>

<details>
<summary>Share</summary>

```
WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses

Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remain...

arXiv: https://arxiv.org/abs/2610.08526

#VLA #robotics
```

</details>

---

### [ActTune: Action-Aware Precision and GPU Operating-Point Adaptation for Energy-Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2610.08444)

**Authors:** Zou Qingyun, Bin Gao, Wenju Zhao, Weng-Fai Wong, Bingsheng He et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AR | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.08444) | [PDF](https://arxiv.org/pdf/2610.08444)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies repeatedly invoke inference to control robots, making graphics processing unit (GPU) energy a recurring cost of task execution. Reducing energy per inference call, however, may not reduce energy per successful task if numerical errors increase failures or slower inference prolongs execution. We therefore target GPU energy per successful task while preserving task success and keeping the inference-latency increase within 10\%. Our approach builds on two observations: quantization sensitivity varies across action classes, model layers, and weights versus act...

</details>

<details>
<summary>Share</summary>

```
ActTune: Action-Aware Precision and GPU Operating-Point Adaptation for Energy-Efficient Vision-Language-Action Inference

Vision-language-action (VLA) policies repeatedly invoke inference to control robots, making graphics processing unit (GPU) energy a recurring cost of task execution.

arXiv: https://arxiv.org/abs/2610.08444

#VLA #robotics
```

</details>

---

### [MIM-VLA: Learning Physical Interaction Representations from Gripper Motor Feedback](https://arxiv.org/abs/2610.08425)

**Authors:** Jaeyoung Lee, Jiyeon Koo, Taehwa Kim, Yerin Cha, Andrew Jaeyong Choi

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.08425) | [PDF](https://arxiv.org/pdf/2610.08425)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies infer grasp actions primarily from visual observations and robot state, but do not explicitly represent the physical response observed after contact. We present MIM-VLA, a motor-feedback-based architecture that encodes recent gripper current, position, velocity, and signal validity as a 128-dimensional interaction token. A motor-only Motor Interaction Module (MIM) is pretrained with human-reviewed contact and interaction-phase labels and then conditions only the gripper-action pathway of SmolVLA; arm actions and the position-control interface remain unchan...

</details>

<details>
<summary>Share</summary>

```
MIM-VLA: Learning Physical Interaction Representations from Gripper Motor Feedback

Vision-language-action (VLA) policies infer grasp actions primarily from visual observations and robot state, but do not explicitly represent the physical response observed after contact.

arXiv: https://arxiv.org/abs/2610.08425

#VLA #robotics
```

</details>

---

### [Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation](https://arxiv.org/abs/2610.07558)

**Authors:** Hojoon Son, Fan Zhang

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.07558) | [PDF](https://arxiv.org/pdf/2610.07558)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a major paradigm for Vision-and-Language Navigation (VLN). However, in safety-critical facilities, invisible risks such as radiation or temperature spikes cannot be detected by an RGB camera, and handling each risk is expensive, requiring a new encoder, new data, and model retraining. We propose Physics-Guided Visual Prompting (PG-VP), a plug-and-play multimodal perception module that instead reuses what a frozen VLA model already does well: avoiding visible obstacles. Given a proximal radiation or thermal source, PG-VP performs a physics-guided...

</details>

<details>
<summary>Share</summary>

```
Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation

Vision-Language-Action (VLA) models have become a major paradigm for Vision-and-Language Navigation (VLN).

arXiv: https://arxiv.org/abs/2610.07558

#VLA #robotics
```

</details>

---

### [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594)

**Authors:** Zexi Zhang, Zecheng Zhu, Zidong Chen, Zulkhuu Tuya, Stephen James

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.07594) | [PDF](https://arxiv.org/pdf/2610.07594) | [Code](https://github.com/swirl-uk/BiGym2)

<details>
<summary>Abstract</summary>

Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchronised multi-camera views and full-body execution records. We benchmark vision-language-action fine-tuning, imitation learning, demo-driven reinforcement learning, and cold-start coding agents given the interaction budget of online reinforceme...

</details>

<details>
<summary>Share</summary>

```
BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture.

arXiv: https://arxiv.org/abs/2610.07594
Code: https://github.com/swirl-uk/BiGym2

#VLA #robotics
```

</details>

---

### [OGAM: Connecting Systematic Testing to Runtime Assurance through Object-Grounded Attention Monitoring for VLA Policies](https://arxiv.org/abs/2610.05878)

**Authors:** Haki Darwish, Xiangyu Yin, Changwen Li, Rongjie Yan, Francisco Gomes de Oliveira Neto et al. (6 authors)

**Published:** 2026-10-05 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-10-04 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-10-04 (updated 2026-10-06) | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.05166) | [PDF](https://arxiv.org/pdf/2610.05166)

<details>
<summary>Abstract</summary>

A safe action is not necessarily a viable one. A frozen vision-language-action (VLA) policy can favor a locally admissible move that leaves no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the next move, while feasibility depends on the futures it leaves open. To bring those futures into the decision, we derive the exact next-block marginal of the history-conditioned policy-environment trajectory law restricted to safe task completion. The derivation reveals a candidate-dependent feasible-future mass: its support records whether s...

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

**Published:** 2026-10-04 | **Categories:** cs.AR, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

### [ProactiveVLA: Augmenting Embodied Memory through Proactive Environment Exploration](https://arxiv.org/abs/2610.06999)

**Authors:** Shizuo Tian, Haodong Luo, Yutong Li, Yuebing Song, Yunxin Liu et al. (6 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.06999) | [PDF](https://arxiv.org/pdf/2610.06999)

<details>
<summary>Abstract</summary>

Rapid adaptation to a new environment requires a robot to acquire useful knowledge about local objects, states, and interactions from limited experience. Systems that combine a reasoning agent with a frozen vision-language-action model (VLA) can adapt through execution feedback and memory, making the choice of experience central to their effectiveness. Repeated practice of a target task may refine a familiar solution while leaving other interactions relevant to changed conditions untested. We introduce ProactiveVLA, which uses proactive environment exploration to acquire reusable knowledge for...

</details>

<details>
<summary>Share</summary>

```
ProactiveVLA: Augmenting Embodied Memory through Proactive Environment Exploration

Rapid adaptation to a new environment requires a robot to acquire useful knowledge about local objects, states, and interactions from limited experience.

arXiv: https://arxiv.org/abs/2610.06999

#VLA #robotics
```

</details>

---

### [DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling](https://arxiv.org/abs/2610.04933)

**Authors:** Seongheon Park, Heecheol Kim, Shulin Tian, Lilika Makabe, Namiko Saito et al. (8 authors)

**Published:** 2026-10-04 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

### [DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09144)

**Authors:** Kaixi Feng, Guoheng Sun, Ziyao Wang, Yexiao He, Zheyu Shen et al. (6 authors)

**Published:** 2026-10-06 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09144) | [PDF](https://arxiv.org/pdf/2610.09144)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tokens influence policy computation. We introduce DIVA, a Dual-Space Intent-Aware Visual Attenuation module with an anchor-then-attenuate design. DIVA combines high-level task intent with low-level visual evidence to estimate patch-wise relevance anchors, then applies them in two complementary spaces: it reweights projected visual tokens before backbone entry and persistently attenua...

</details>

<details>
<summary>Share</summary>

```
DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tok...

arXiv: https://arxiv.org/abs/2610.09144

#VLA #robotics
```

</details>

---

### [CARE: Certifying Acceleration for Vision-Language-Action Inference](https://arxiv.org/abs/2610.08917)

**Authors:** Rui Liu, Tong Zheng, Jindong Gu, Zhipeng Wang

**Published:** 2026-10-06 | **Categories:** cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.08917) | [PDF](https://arxiv.org/pdf/2610.08917)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive. Prior work accelerates VLA inference using techniques like action chunking and visual-token pruning, typically evaluating based on latency and average task success. However, acceleration may discard information and break tasks the original policy would solve, a risk hidden by average metrics. Measuring these failures is challenging because action deviations compound over closed-loop trajectories, meaning task failure is only observable across full episodes. We therefore define...

</details>

<details>
<summary>Share</summary>

```
CARE: Certifying Acceleration for Vision-Language-Action Inference

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive.

arXiv: https://arxiv.org/abs/2610.08917

#VLA #robotics
```

</details>

---

### [Wiring Matters: Injection Topology and Initialization of Affordance Heads in Vision-Language-Action Policies](https://arxiv.org/abs/2610.06318)

**Authors:** Zijian An, Linhan Wang, Jiayan Wang, Shijie Geng, Ran Yang et al. (7 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

### [VioLA: Learning Generalist Humanoid Control Policies from Human Data](https://arxiv.org/abs/2610.12435)

**Authors:** Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12435) | [PDF](https://arxiv.org/pdf/2610.12435)

<details>
<summary>Abstract</summary>

Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing...

</details>

<details>
<summary>Share</summary>

```
VioLA: Learning Generalist Humanoid Control Policies from Human Data

Teaching a humanoid to follow instructions with its whole body runs into two obstacles.

arXiv: https://arxiv.org/abs/2610.12435

#VLA #robotics
```

</details>

---

### [Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](https://arxiv.org/abs/2610.12369)

**Authors:** Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12369) | [PDF](https://arxiv.org/pdf/2610.12369)

<details>
<summary>Abstract</summary>

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code measures and tracks the robot, environment, and task state from camera images and proprioception, a...

</details>

<details>
<summary>Share</summary>

```
Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time.

arXiv: https://arxiv.org/abs/2610.12369

#VLA #robotics
```

</details>

---

### [RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes](https://arxiv.org/abs/2610.11480)

**Authors:** Bohan Zhou, Xingbei Chen, Emily Huang, Weilin Ruan, Haojian Huang et al. (20 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.11480) | [PDF](https://arxiv.org/pdf/2610.11480)

<details>
<summary>Abstract</summary>

Embodied coding agents can combine modular robot skills with frozen end-to-end policies, yet effective composition requires anticipating which policy family will succeed in the current physical state. We present RoboAware, which builds on coding agents' skill orchestration by learning only a state-conditioned responsibility coordinator from counterfactual outcomes. Inspired by the success of REPL, we propose the $P^5$ schema and formulate a hierarchical MDP based on it. $P^5$ organizes skills uniformly into five semantic stages, defining where responsibility can be compared. To address the lac...

</details>

<details>
<summary>Share</summary>

```
RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes

Embodied coding agents can combine modular robot skills with frozen end-to-end policies, yet effective composition requires anticipating which policy family will succeed in the current physical state.

arXiv: https://arxiv.org/abs/2610.11480

#VLA #robotics
```

</details>

---

### [RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies](https://arxiv.org/abs/2610.09696)

**Authors:** Mimo Shirasaka, Takehiko Ohkawa, Takuya Okubo, Nicola Scianca, Tatsuya Matsushima et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09696) | [PDF](https://arxiv.org/pdf/2610.09696)

<details>
<summary>Abstract</summary>

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands. Vision-Language-Action (VLA) policies trained on such data inherit the demonstrator's timing. Yet human timing does not directly transfer to robots: compliant hands tolerate fast contact, whereas robots may overshoot due to actuator and tracking limitations; conversely, robots can move faster in free space. This motivates a unified approach that reconciles execution speed with contact safety...

</details>

<details>
<summary>Share</summary>

```
RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands.

arXiv: https://arxiv.org/abs/2610.09696

#VLA #robotics
```

</details>

---

### [VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation](https://arxiv.org/abs/2610.08220)

**Authors:** Yutian Zhang, Xingrui Xiong, Siyuan Ma, Yang Li, Jiawen Wen et al. (15 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.08220) | [PDF](https://arxiv.org/pdf/2610.08220)

<details>
<summary>Abstract</summary>

Portable mobile-manipulation demonstrations can help alleviate data scarcity for embodied intelligence, but obtaining reliable, low-cost, and robot-free motion supervision from RGB observations remains challenging. Existing approaches often rely on teleoperation or specialized devices equipped with additional sensing hardware, while directly using estimated visual odometry (VO) trajectories can introduce inconsistencies due to accumulated drift and imperfect motion supervision. We present the Visual-Odometry-Conditioned Mobile Manipulation Interface (VOMMI), a portable demonstration collection...

</details>

<details>
<summary>Share</summary>

```
VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation

Portable mobile-manipulation demonstrations can help alleviate data scarcity for embodied intelligence, but obtaining reliable, low-cost, and robot-free motion supervision from RGB observations remains challenging.

arXiv: https://arxiv.org/abs/2610.08220

#VLA #robotics
```

</details>

---

### [ESP: Energy-Score Policy for One-Step Multimodal Action Generation](https://arxiv.org/abs/2610.07696)

**Authors:** Lilika Makabe, Heecheol Kim, Yasuyuki Matsushita

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.07696) | [PDF](https://arxiv.org/pdf/2610.07696)

<details>
<summary>Abstract</summary>

Generative action models based on diffusion and flow matching have been increasingly adopted in vision-language-action (VLA) policies for their ability to capture diverse behaviors, including multiple valid action sequences under the same observation and instruction. Their iterative sampling procedures, however, require repeated network evaluations to generate each action chunk, increasing inference latency in closed-loop control. We propose ESP (Energy-Score Policy), a teacher-free approach that maps policy context and noise directly to an action chunk in a single network evaluation. ESP trai...

</details>

<details>
<summary>Share</summary>

```
ESP: Energy-Score Policy for One-Step Multimodal Action Generation

Generative action models based on diffusion and flow matching have been increasingly adopted in vision-language-action (VLA) policies for their ability to capture diverse behaviors, including multiple valid action seq...

arXiv: https://arxiv.org/abs/2610.07696

#VLA #robotics
```

</details>

---

### [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining](https://arxiv.org/abs/2610.07652)

**Authors:** Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao et al. (10 authors)

**Published:** 2026-10-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.07652) | [PDF](https://arxiv.org/pdf/2610.07652)

<details>
<summary>Abstract</summary>

The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation constraints, hindering agentic task generation and scalable synthesis of high-quality articulated-man...

</details>

<details>
<summary>Share</summary>

```
SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining

The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contac...

arXiv: https://arxiv.org/abs/2610.07652

#VLA #robotics
```

</details>

---

### [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)

**Authors:** Haoran Chen, Jingtian Ji, Samuel Wheeler, Kaylene Caswell Stocking, Matthew Walter

**Published:** 2026-10-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.09170) | [PDF](https://arxiv.org/pdf/2610.09170)

<details>
<summary>Abstract</summary>

Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space. Many action tokenizers learn the mapping between tokens and actions via a reconstruction objective. However, as we show through extensive analysis, sufficiently accurate action reconstruction is only one part of what makes a downstream robot policy successful. It is also critical that the policy is able to predict the right tokens for new observations, and that unseen policy token predictions still decode in...

</details>

<details>
<summary>Share</summary>

```
Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space.

arXiv: https://arxiv.org/abs/2610.09170

#VLA #robotics
```

</details>

---

### [Recursive Video In-Context Learning for Agentic Robot](https://arxiv.org/abs/2610.06843)

**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, Yuzhang Shang

**Published:** 2026-10-05 | **Categories:** cs.RO, cs.AI, cs.CL | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in title

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

### [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](https://arxiv.org/abs/2610.12107)

**Authors:** Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou, Shuhan Yang, Junchao Huang et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.12107) | [PDF](https://arxiv.org/pdf/2610.12107)

<details>
<summary>Abstract</summary>

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise boundary delineation. This requirement challenges existing cascaded vision-language architectures, which typically rely on static feature interfaces and single-pass mask prediction, limiting adaptive perception and geometric correction. We introduce ContourVLA, a vision-language-action policy that recasts GRES as a closed-loop visuomotor process, in which editable contours serve a...

</details>

<details>
<summary>Share</summary>

```
ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation

Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise...

arXiv: https://arxiv.org/abs/2610.12107

#VLA #robotics
```

</details>

---

### [PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence](https://arxiv.org/abs/2610.07127)

**Authors:** Dheeraj Varghese, Anna Vettoruzzo, Walter Simoncini, Michelle Lorena Acevedo Callejas, Mohammad Mahdi Derakhshani et al. (8 authors)

**Published:** 2026-10-05 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.07127) | [PDF](https://arxiv.org/pdf/2610.07127)

<details>
<summary>Abstract</summary>

Recent advances in multimodal foundation models yield strong performance on static perception and reasoning benchmarks, yet such evaluations largely overlook a central aspect of intelligence: acting competently in dynamic environments over extended time horizons. We introduce PlaySuite, a large-scale benchmark for evaluating interactive visual intelligence across more than 5K open-source video games curated from PyWeek and itch.io. Spanning diverse genres and engines, including Pygame, HTML5, Godot, and Unity, these independent games are largely out-of-distribution for current models, reducing...

</details>

<details>
<summary>Share</summary>

```
PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence

Recent advances in multimodal foundation models yield strong performance on static perception and reasoning benchmarks, yet such evaluations largely overlook a central aspect of intelligence: acting competently in dyn...

arXiv: https://arxiv.org/abs/2610.07127

#VLA #robotics
```

</details>

---

### [Q-Learning with Scalar Adjoint Matching](https://arxiv.org/abs/2610.10437)

**Authors:** Yonghoon Dong, Minsung Yoon, Jaehyuk Kim, Jungwoo Park, Changyeon Kim et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.10437) | [PDF](https://arxiv.org/pdf/2610.10437)

<details>
<summary>Abstract</summary>

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to update the flow model itself by propagating value information from the final action back to each flow step, but it requires a vector--Jacobian product through the policy at every step, a cost that grows with the number of flow steps and the pol...

</details>

<details>
<summary>Share</summary>

```
Q-Learning with Scalar Adjoint Matching

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest.

arXiv: https://arxiv.org/abs/2610.10437

#VLA #robotics
```

</details>

---

### [Demonstration-Calibrated Port-Hamiltonian Retuning for Manipulation Policies](https://arxiv.org/abs/2610.05755)

**Authors:** Yulong Yang, Fan Wu, Christine Allen-Blanchette, Amit Chakraborty

**Published:** 2026-10-05 (updated 2026-10-06) | **Categories:** cs.RO, eess.SY | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

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
