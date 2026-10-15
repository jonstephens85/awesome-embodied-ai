# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-15 19:42 UTC

**Papers shown:** 79 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)

**Authors:** Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20609) | [PDF](https://arxiv.org/pdf/2610.20609) | [Project Page](https://safedrive-vla.github.io/SafeDriveVLA/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose. We present the first benchmark suite that evaluates navigation following and conflict awareness together, along with adversarial rob...

</details>

<details>
<summary>Share</summary>

```
SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-f...

arXiv: https://arxiv.org/abs/2610.20609
Project page: https://safedrive-vla.github.io/SafeDriveVLA/

#worldmodels #robotics
```

</details>

---

### [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/abs/2610.12468)

**Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12468) | [PDF](https://arxiv.org/pdf/2610.12468) | [Project Page](https://brave-eai.github.io/DreamTrue) | [Code](https://github.com/brave-eai/DreamTrue)

<details>
<summary>Abstract</summary>

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render action trajectories into image-space conditions and introduce offline geometric calibration to align these conditions with the target videos. To broaden interaction coverage, we introduc...

</details>

<details>
<summary>Share</summary>

```
DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction.

arXiv: https://arxiv.org/abs/2610.12468
Project page: https://brave-eai.github.io/DreamTrue
Code: https://github.com/brave-eai/DreamTrue

#worldmodels #robotics
```

</details>

---

### [Back on Track: Deployment-time Policy Improvement via World Model Planning](https://arxiv.org/abs/2610.19579)

**Authors:** Colton Crosby, Hao Wang, Mac Schwager, Somil Bansal

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Vision-Language-Action Models

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19579) | [PDF](https://arxiv.org/pdf/2610.19579) | [Project Page](https://policy-improvement-wm.pages.dev/)

<details>
<summary>Abstract</summary>

State-of-the-art visuomotor policies are increasingly capable of executing complex tasks, yet can fail during deployment in ways they cannot predict or recover from on their own. Improving their performance and robustness typically requires collecting more data, retraining, or modifying the policy architecture, all of which are time- and resource-intensive in practice. We instead propose an offline-trained monitoring-and-intervention framework that improves a policy during deployment using only black-box query access. From a limited set of labeled on-policy rollouts, we learn a policy-conditio...

</details>

<details>
<summary>Share</summary>

```
Back on Track: Deployment-time Policy Improvement via World Model Planning

State-of-the-art visuomotor policies are increasingly capable of executing complex tasks, yet can fail during deployment in ways they cannot predict or recover from on their own.

arXiv: https://arxiv.org/abs/2610.19579
Project page: https://policy-improvement-wm.pages.dev/

#worldmodels #robotics
```

</details>

---

### [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](https://arxiv.org/abs/2610.18447)

**Authors:** Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo et al. (11 authors)

**Published:** 2026-10-13 (updated 2026-10-14) | **Categories:** cs.AI, cs.CV, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18447) | [PDF](https://arxiv.org/pdf/2610.18447) | [Project Page](https://thinkercosmos.ubtrobot.com/thinker-wm)

<details>
<summary>Abstract</summary>

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and generates RGB, metric depth, and robot action through a shared intermediate Unified Dynamics Transformer...

</details>

<details>
<summary>Share</summary>

```
Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support.

arXiv: https://arxiv.org/abs/2610.18447
Project page: https://thinkercosmos.ubtrobot.com/thinker-wm

#worldmodels #robotics
```

</details>

---

### [PILOT: Guiding Long-Horizon World-Model Planning for Robot Manipulation with Visual Subgoals and Policy Priors](https://arxiv.org/abs/2610.14335)

**Authors:** Yang Liu, Hanchen Cui, Karthik Desingh

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14335) | [PDF](https://arxiv.org/pdf/2610.14335) | [Project Page](https://pilot-planner.github.io/)

<details>
<summary>Abstract</summary>

Latent world-model planning has shown promising results in goal-conditioned robotic manipulation, but remains challenging for long-horizon planning due to limited temporal guidance and inefficient action search. A distant visual goal provides little guidance for preparatory actions, while uninformed action sampling makes local optimization inefficient. We propose PILOT (Policy-Initialized Local Optimization with Temporal subgoals), which uses a video model to generate intermediate visual subgoals and a learned policy to initialize the cross-entropy method (CEM). CEM refines candidate action se...

</details>

<details>
<summary>Share</summary>

```
PILOT: Guiding Long-Horizon World-Model Planning for Robot Manipulation with Visual Subgoals and Policy Priors

Latent world-model planning has shown promising results in goal-conditioned robotic manipulation, but remains challenging for long-horizon planning due to limited temporal guidance and inefficient action search.

arXiv: https://arxiv.org/abs/2610.14335
Project page: https://pilot-planner.github.io/

#worldmodels #robotics
```

</details>

---

### [Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](https://arxiv.org/abs/2610.13164)

**Authors:** Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13164) | [PDF](https://arxiv.org/pdf/2610.13164) | [Project Page](https://fffstrong.github.io/Grounded-Dreamer/)

<details>
<summary>Abstract</summary>

Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale. Existing methods either depend on human teleoperation, rely on simulation with limited visual realism, or use human videos that lack embodiment-specific annotations. In this paper, we introduce Grounded-Dreamer, a framework for synthesizing physically grounded robot manipulation data with video world models while avoiding human teleoperation demonstrations. Grounded-Dreamer combines the visual realism of generative vide...

</details>

<details>
<summary>Share</summary>

```
Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding

Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale.

arXiv: https://arxiv.org/abs/2610.13164
Project page: https://fffstrong.github.io/Grounded-Dreamer/

#worldmodels #robotics
```

</details>

---

### [Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction](https://arxiv.org/abs/2610.19212)

**Authors:** Anton Arapin, Aditya Singh, Yixin Wang, Jun Gao, Bernadette Bucher

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19212) | [PDF](https://arxiv.org/pdf/2610.19212) | [Project Page](https://anton-arapin.github.io/d3wm-site)

<details>
<summary>Abstract</summary>

World models of visual information predict future image frames conditioned on given action sequences. This predicted scene evolution is driven by deterministic changes such as controlled motion on a robot platform, as well as stochastic changes such as rendering of manipulated objects or previously occluded regions. Our key insight is that the spatial location of these stochastic changes is itself learnable. We leverage this insight by jointly regressing both the deterministic next-state prediction and the spatial uncertainty map, then using the uncertainty map to guide a conditional diffusion...

</details>

<details>
<summary>Share</summary>

```
Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction

World models of visual information predict future image frames conditioned on given action sequences.

arXiv: https://arxiv.org/abs/2610.19212
Project page: https://anton-arapin.github.io/d3wm-site

#worldmodels #robotics
```

</details>

---

### [Across Viewpoints and Time: Trajectory-Generalizable Physical Attacks on World Models and Video Understanding Models](https://arxiv.org/abs/2610.15343)

**Authors:** Song Xia, Meiwen Ding, Chenqi Kong, Wenhan Yang, Xudong Jiang

**Published:** 2026-10-11 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15343) | [PDF](https://arxiv.org/pdf/2610.15343) | [Project Page](https://xiasong0501.github.io/TARA/)

<details>
<summary>Abstract</summary>

World models and video understanding models are increasingly deployed in dynamic visual environments, yet their robustness to physical adversarial threats remains largely underexplored. We study whether a single physical adversarial texture can mislead the victim model across different real-world scenarios where observing viewpoints vary along uncontrolled object--camera trajectories. We identify that heterogeneous video semantics and trajectories induce poorly aligned gradients for optimizing the adversarial texture. To address that, we propose the Trajectory-aware adversarial Alignment and R...

</details>

<details>
<summary>Share</summary>

```
Across Viewpoints and Time: Trajectory-Generalizable Physical Attacks on World Models and Video Understanding Models

World models and video understanding models are increasingly deployed in dynamic visual environments, yet their robustness to physical adversarial threats remains largely underexplored.

arXiv: https://arxiv.org/abs/2610.15343
Project page: https://xiasong0501.github.io/TARA/

#worldmodels #robotics
```

</details>

---

### [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](https://arxiv.org/abs/2610.19201)

**Authors:** Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19201) | [PDF](https://arxiv.org/pdf/2610.19201) | [Project Page](https://research.nvidia.com/labs/sil/projects/lidarverse)

<details>
<summary>Abstract</summary>

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors. Existing LiDAR simulators largely follow one of two complementary paradigms: reconstruction-based methods preserve the geometry of a captured scene but require lengthy per-scene optimization, whereas generative methods amortize learning across data but lack the consistency needed for long-horizon rollouts. LidarVerse brings both paradigms into a single, unified conditional generative framework. A universal tokenizer maps LiDAR range sequences into a shared latent space, where a bidirect...

</details>

<details>
<summary>Share</summary>

```
Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.

arXiv: https://arxiv.org/abs/2610.19201
Project page: https://research.nvidia.com/labs/sil/projects/lidarverse

#worldmodels #robotics
```

</details>

---

### [Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](https://arxiv.org/abs/2610.18991)

**Authors:** Nolan Fey, Khai Nguyen, Yash Prabhu, Gabriel B. Margolis, Pulkit Agrawal

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18991) | [PDF](https://arxiv.org/pdf/2610.18991) | [Project Page](https://contact-uan.csail.mit.edu/)

<details>
<summary>Abstract</summary>

Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness to impacts. This failure can arise from actuator sim-to-real gaps because forces depend on actuator torques. We introduce Contact-UAN, a residual world model that preserves a simulator's physics priors while correcting actuator dynamics to align simulated rollouts with recorded hardware rollouts. For humanoid motion with contact, this requires contact-consistent replay: if hardwar...

</details>

<details>
<summary>Share</summary>

```
Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control

Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness...

arXiv: https://arxiv.org/abs/2610.18991
Project page: https://contact-uan.csail.mit.edu/

#worldmodels #robotics
```

</details>

---

### [ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18852)

**Authors:** Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen et al. (19 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18852) | [PDF](https://arxiv.org/pdf/2610.18852) | [Project Page](https://force-wam.github.io/)

<details>
<summary>Abstract</summary>

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions. Task-agnostic play provides broader experience of contact dynamics without specifying task goals. To fully leverage these two types of data, we introduce ForceWAM, a force world action model that decouples knowledge of task-compatible interaction outcomes from knowledge of how local actions change contact. A world model learns from successful demonstrations to jointly predict future video and six-axis force/torque trajectories. Together, these futu...

</details>

<details>
<summary>Share</summary>

```
ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions.

arXiv: https://arxiv.org/abs/2610.18852
Project page: https://force-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation](https://arxiv.org/abs/2610.18135)

**Authors:** Yifei Yang, Zehua Fan, Zike Yan, Zhongyu Li, Yan Wang

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18135) | [PDF](https://arxiv.org/pdf/2610.18135)

<details>
<summary>Abstract</summary>

World-model-based visual navigation enables action planning by predicting future states under candidate trajectories. However, long-horizon rollout remains challenging: models are often trained with ground-truth visual histories but deployed in closed-loop prediction, and evaluating many candidates with step-by-step rollout is computationally expensive. We propose SkipWorld, a latent skip planning framework for efficient visual navigation. SkipWorld introduces three components: (i) Latent AutoRoll, which trains a world model to recursively roll out future states in latent space, reducing the m...

</details>

<details>
<summary>Share</summary>

```
SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation

World-model-based visual navigation enables action planning by predicting future states under candidate trajectories.

arXiv: https://arxiv.org/abs/2610.18135

#worldmodels #robotics
```

</details>

---

### [ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409)

**Authors:** Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang et al. (10 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13409) | [PDF](https://arxiv.org/pdf/2610.13409) | [Code](https://github.com/wyh-autonomy/maneuverflow)

<details>
<summary>Abstract</summary>

End-to-end planning in complex scenes must model diverse driving intentions and select the most appropriate trajectory using scene context and future risks. However, multi-query regression may collapse to one mode, while anchor-based and generative planners share a scaling bottleneck: small candidate sets limit maneuver coverage or discovery of high-quality trajectories, whereas large sets increase generation and scoring costs. We propose ManeuverFlow to generate trajectories for distinct intentions in one step and evaluate and refine them using current and future evidence. The model selects r...

</details>

<details>
<summary>Share</summary>

```
ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving

End-to-end planning in complex scenes must model diverse driving intentions and select the most appropriate trajectory using scene context and future risks.

arXiv: https://arxiv.org/abs/2610.13409
Code: https://github.com/wyh-autonomy/maneuverflow

#worldmodels #robotics
```

</details>

---

### [PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents](https://arxiv.org/abs/2610.20240)

**Authors:** Siqi Yang, Yimu Wang, Ziqi Cai, Chengxuan Zhu, Shuchen Weng et al. (9 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.20240) | [PDF](https://arxiv.org/pdf/2610.20240) | [Project Page](https://pawa.siki.moe)

<details>
<summary>Abstract</summary>

A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view. A point-of-view (POV) video captures such changes only after they enter its field of view, whereas panoramic video records the surroundings in every viewing direction and has served as an intermediate representation of the world state in recent world models. Learning this task therefore requires synchronized POV and panoramic videos of interacting players together with their actions, yet no existing dataset provides this...

</details>

<details>
<summary>Share</summary>

```
PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents

A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view.

arXiv: https://arxiv.org/abs/2610.20240
Project page: https://pawa.siki.moe

#worldmodels #robotics
```

</details>

---

### [One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models](https://arxiv.org/abs/2610.19375)

**Authors:** Joshua Cheung, Zhang He

**Published:** 2026-10-14 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.19375) | [PDF](https://arxiv.org/pdf/2610.19375)

<details>
<summary>Abstract</summary>

Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model. In model-based RL this assumption is known to be unreliable; we ask whether it also fails for latent world models, where the training target is the model's own embedding and the loss is not expressed in interpretable units. We introduce a frozen-decoder protocol reporting one-step error in physical units, decomposed into the part already present in the encoder's representation and the part the predictor adds. A...

</details>

<details>
<summary>Share</summary>

```
One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models

Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model.

arXiv: https://arxiv.org/abs/2610.19375

#worldmodels #robotics
```

</details>

---

### [Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold](https://arxiv.org/abs/2610.19007)

**Authors:** Anton Arapin, Chahyon Ku, Bernadette Bucher

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.19007) | [PDF](https://arxiv.org/pdf/2610.19007) | [Project Page](https://anton-arapin.github.io/action-jets-site)

<details>
<summary>Abstract</summary>

World models are a powerful means of reasoning and planning, but many of these action-conditioned predictive models are high dimensional and computationally expensive. These challenges limit the number of action candidates that can be evaluated by a planner. We show that this cost is avoidable for planners over short horizons, which only require local information with respect to the current state. For a fixed state, the frames reachable by varying a low-dimensional action (a camera movement or an end-effector command) lie on a low-dimensional manifold. We estimate the local shape of that manif...

</details>

<details>
<summary>Share</summary>

```
Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold

World models are a powerful means of reasoning and planning, but many of these action-conditioned predictive models are high dimensional and computationally expensive.

arXiv: https://arxiv.org/abs/2610.19007
Project page: https://anton-arapin.github.io/action-jets-site

#worldmodels #robotics
```

</details>

---

### [RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control](https://arxiv.org/abs/2610.17584)

**Authors:** Binghan Wu, Kai Zeng, Kai Yang, Ya-Qin Zhang, Joseph Sifakis et al. (6 authors)

**Published:** 2026-10-13 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17584) | [PDF](https://arxiv.org/pdf/2610.17584)

<details>
<summary>Abstract</summary>

Operational mobile networks are rich in observations but poor in interventions: they continuously generate large volumes of passive telemetry, while controlled action--response trajectories remain comparatively scarce and costly to collect. This observation--intervention asymmetry is a central obstacle to building practical world models for RAN control. We address this problem with RAN-JEPA, an action-conditioned world model that separates representation learning from intervention learning. The model first learns a predictive latent representation from observation-only network data, adapts tha...

</details>

<details>
<summary>Share</summary>

```
RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control

Operational mobile networks are rich in observations but poor in interventions: they continuously generate large volumes of passive telemetry, while controlled action--response trajectories remain comparatively scarce...

arXiv: https://arxiv.org/abs/2610.17584

#worldmodels #robotics
```

</details>

---

### [Multics: Generative Multi-Player World Model with Hierarchical Communication](https://arxiv.org/abs/2610.17201)

**Authors:** Kaiyi Huang, Wangbo Yu, Yukun Huang, Jiwen Yu, Kunhao Liu et al. (9 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17201) | [PDF](https://arxiv.org/pdf/2610.17201) | [Project Page](https://karine-huang.github.io/Multics/)

<details>
<summary>Abstract</summary>

Multi-player interactive world models aim to simulate shared environments from multiple players' perspectives, but achieving robust generation while scaling to more players remains challenging. Existing approaches that rely on fully-connected communication (e.g., Solaris) incur quadratic attention costs as the number of players grows, while centralized approaches (e.g., $γ$-World) suffer from interference between unrelated events in a shared global representation. To address these challenges, we present Multics, a multi-player video generation framework with hierarchical communication that str...

</details>

<details>
<summary>Share</summary>

```
Multics: Generative Multi-Player World Model with Hierarchical Communication

Multi-player interactive world models aim to simulate shared environments from multiple players' perspectives, but achieving robust generation while scaling to more players remains challenging.

arXiv: https://arxiv.org/abs/2610.17201
Project page: https://karine-huang.github.io/Multics/

#worldmodels #robotics
```

</details>

---

### [World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models](https://arxiv.org/abs/2610.16365)

**Authors:** Shinseong Kim, Jaeseok Jeong, Jianlong Fu, Youngjung Uh

**Published:** 2026-10-12 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16365) | [PDF](https://arxiv.org/pdf/2610.16365) | [Project Page](https://grainsack.github.io/physical-registry/)

<details>
<summary>Abstract</summary>

Video world models must generate physically plausible futures, not just realistic frames. Existing approaches typically use semantic, physical, or predictive information to guide the visual generation stream, leaving a fundamental question: where inside the generator should predictions of scene evolution live? Standard video tokens jointly encode appearance and dynamics, but provide no distinct state for learning and reading predictive dynamics. We answer this question with the Physical Registry: temporally grounded registry slots inside a video DiT that are initialized from an observation-con...

</details>

<details>
<summary>Share</summary>

```
World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models

Video world models must generate physically plausible futures, not just realistic frames.

arXiv: https://arxiv.org/abs/2610.16365
Project page: https://grainsack.github.io/physical-registry/

#worldmodels #robotics
```

</details>

---

### [RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models](https://arxiv.org/abs/2610.16302)

**Authors:** Yaoyang Liu, Dongyu Yan, Yihua Du, Shengju Qian, Zeke Xie et al. (8 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.16302) | [PDF](https://arxiv.org/pdf/2610.16302) | [Project Page](https://hkust-longgroup.github.io/RAR)

<details>
<summary>Abstract</summary>

Video-based interactive world models aim to enable real-time, user-controllable environments. Yet most existing systems are trained and rolled out at a fixed temporal rate, limiting both runtime-rate adaptation and physical-horizon coverage -- a limitation we term temporal-rate coupling. Specifically, when runtime generation throughput differs from the learned temporal rate, the generated world evolves unintentionally more slowly or quickly. Moreover, using a single temporal rate imposes an inherent trade-off between temporal granularity and physical horizon: higher rates capture finer motion...

</details>

<details>
<summary>Share</summary>

```
RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models

Video-based interactive world models aim to enable real-time, user-controllable environments.

arXiv: https://arxiv.org/abs/2610.16302
Project page: https://hkust-longgroup.github.io/RAR

#worldmodels #robotics
```

</details>

---

### [SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781)

**Authors:** Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang et al. (11 authors)

**Published:** 2026-10-09 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.13781) | [PDF](https://arxiv.org/pdf/2610.13781) | [Project Page](https://opendrivelab.com/SimVTA/)

<details>
<summary>Abstract</summary>

Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a simulation-grounded post-training framework that combines trajectory optimization with video supervision. First, we sample candidate trajectories for each observation and use a real-world sim...

</details>

<details>
<summary>Share</summary>

```
SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models

Driving world action models (WAMs) learn from paired trajectories and future observations.

arXiv: https://arxiv.org/abs/2610.13781
Project page: https://opendrivelab.com/SimVTA/

#worldmodels #robotics
```

</details>

---

### [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826)

**Authors:** Haoyi Duan, Liliang Chen, Nan Wang, Yang Zhang, Yuhang Lu et al. (16 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18826) | [PDF](https://arxiv.org/pdf/2610.18826)

<details>
<summary>Abstract</summary>

We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions. Given the same initial observation and low-level action sequence, WorldOracle asks whether a predicted rollout reproduces what happens in the real world, including physical consequences and task-state transitions. We evaluate models along four complementary dimensions: physical state correctness, interaction spatial alignment, key interaction area fidelity, and multi-view action coherence. To support this evaluation, we curate real-world training...

</details>

<details>
<summary>Share</summary>

```
WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions

We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions.

arXiv: https://arxiv.org/abs/2610.18826

#worldmodels #robotics
```

</details>

---

### [LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction](https://arxiv.org/abs/2610.18093)

**Authors:** Jun Tian, Hao Wu, Ruo Chen, Yili Liao, Hongyi Lin et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18093) | [PDF](https://arxiv.org/pdf/2610.18093)

<details>
<summary>Abstract</summary>

Wheel-legged robots operating in outdoor spaces shared with humans require accurate perception, socially compliant navigation, future-scene reasoning, and scene reconstruction. However, existing datasets typically support these capabilities in isolation and rarely provide dense spatial and behavior-level supervision on real wheel-legged platforms. We introduce LynxScenes, a large-scale real-world dataset and benchmark collected with a LYNX M20 wheel-legged robot. It contains approximately 100K 30-s navigation clips spanning 833.6 h and 3,294.7 km, with 3.0M annotated frames. The synchronized r...

</details>

<details>
<summary>Share</summary>

```
LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction

Wheel-legged robots operating in outdoor spaces shared with humans require accurate perception, socially compliant navigation, future-scene reasoning, and scene reconstruction.

arXiv: https://arxiv.org/abs/2610.18093

#worldmodels #robotics
```

</details>

---

### [From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction](https://arxiv.org/abs/2610.17630)

**Authors:** Ruo Chen, Jiahua Pang, Yingjie Niu, Hongyi Lin, Jun Tian et al. (7 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17630) | [PDF](https://arxiv.org/pdf/2610.17630)

<details>
<summary>Abstract</summary>

In outdoor environments, varying terrain and contact conditions can cause identical action commands to produce different motion outcomes for quadruped robots. Predicting these outcomes is essential for reliable navigation and informed path selection. Existing video world models can generate visually plausible futures, yet often struggle to capture robot dynamics and terrain interactions, leading to overly optimistic predictions of action outcomes. We present DR-WM, a physically consistent world model that incorporates robot-terrain contact dynamics to predict the consequences of quadruped acti...

</details>

<details>
<summary>Share</summary>

```
From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction

In outdoor environments, varying terrain and contact conditions can cause identical action commands to produce different motion outcomes for quadruped robots.

arXiv: https://arxiv.org/abs/2610.17630

#worldmodels #robotics
```

</details>

---

### [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)

**Authors:** Minghao Fu, Tavis Siebert, Eryk Halicki, Randall Balestriero

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.12818) | [PDF](https://arxiv.org/pdf/2610.12818) | [Project Page](https://le-wam.github.io/)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and action-conditioned dynamics before adding a control policy or solver. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic Gaussian constraint on the latent state, enabling a single model to support direct policy execution and efficient planning by evaluating sampled actions with its learned latent dyna...

</details>

<details>
<summary>Share</summary>

```
LeWAM: End-to-End World and Action Modeling with JEPAs

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction.

arXiv: https://arxiv.org/abs/2610.12818
Project page: https://le-wam.github.io/

#worldmodels #robotics
```

</details>

---

### [Order-Consistent Latent Geometry for Reliable Short-Horizon Planning in World Models](https://arxiv.org/abs/2610.18570)

**Authors:** Junlin Wu, Wen Fan, Dandan Zhang

**Published:** 2026-10-13 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18570) | [PDF](https://arxiv.org/pdf/2610.18570)

<details>
<summary>Abstract</summary>

Latent planners often rank candidate action sequences by terminal Euclidean distance to a goal latent. Exact agreement with transition distance would make this score ideal, but is stronger than planning requires: along a transition-shortest rollout, the essential requirement is that latent distance does not reverse true transition progress. We show that this pathwise no-reversal requirement is precisely the classical self-approaching condition. To the best of our knowledge, we are the first to identify self-approachingness as a planner-facing compatibility condition for terminal Euclidean late...

</details>

<details>
<summary>Share</summary>

```
Order-Consistent Latent Geometry for Reliable Short-Horizon Planning in World Models

Latent planners often rank candidate action sequences by terminal Euclidean distance to a goal latent.

arXiv: https://arxiv.org/abs/2610.18570

#worldmodels #robotics
```

</details>

---

### [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](https://arxiv.org/abs/2610.18289)

**Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.18289) | [PDF](https://arxiv.org/pdf/2610.18289) | [Code](https://github.com/Fantasy-AMAP/LongForcing)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models have emerged as a foundation for long-horizon world rollout. However, when extended far beyond their training windows, these models suffer from progressive drift: visual quality deteriorates, motion becomes inconsistent, and object identity gradually collapses as generated frames are recursively reused as context. We study a supervision-horizon gap: short-horizon distillation leaves later rollout states without direct supervision. We show that matching short-window marginals need not determine long-horizon behavior, while longer on-policy trajectories expo...

</details>

<details>
<summary>Share</summary>

```
LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout

Autoregressive video diffusion models have emerged as a foundation for long-horizon world rollout.

arXiv: https://arxiv.org/abs/2610.18289
Code: https://github.com/Fantasy-AMAP/LongForcing

#worldmodels #robotics
```

</details>

---

### [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](https://arxiv.org/abs/2610.17434)

**Authors:** Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang et al. (12 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV, cs.AI, cs.MM | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.17434) | [PDF](https://arxiv.org/pdf/2610.17434) | [Project Page](https://adreamwu.github.io/World-T3/)

<details>
<summary>Abstract</summary>

Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously observed world must remain consistent as the model continues to generate. Existing autoregressive approaches often implicitly rely on the generative model itself to retain such information, leading to spatial memory decay beyond the active context. We introduce World-T3, a camera-controlled video world model with a test-time training memory that consolidates past observations into dedicated model parameters. To robustly...

</details>

<details>
<summary>Share</summary>

```
World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models

Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously observed world must remain consistent as...

arXiv: https://arxiv.org/abs/2610.17434
Project page: https://adreamwu.github.io/World-T3/

#worldmodels #robotics
```

</details>

---

### [Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](https://arxiv.org/abs/2610.20134)

**Authors:** Kiyanoush Nazari, Luchen Li, Haoshu Fang, Nima Fazeli, Zhibin Li et al. (7 authors)

**Published:** 2026-10-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.20134) | [PDF](https://arxiv.org/pdf/2610.20134)

<details>
<summary>Abstract</summary>

Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation. Beyond its traditional role in contact detection and reactive control, touch is increasingly used to learn transferable representations, condition manipulation policies, and support embodied physical reasoning. Yet existing surveys largely emphasize tactile hardware and perception, leaving the rapid shift toward learning-based tactile manipulation insufficiently synthesized. This paper reviews tactile-guided skill learning from a learning-centric perspective, organized by the functional role of touch a...

</details>

<details>
<summary>Share</summary>

```
Tactile-Guided Robot Learning: From Representation Learning to Foundation Models

Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation.

arXiv: https://arxiv.org/abs/2610.20134

#worldmodels #robotics
```

</details>

---

### [RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories](https://arxiv.org/abs/2610.18699)

**Authors:** Yunfu Deng, Sangwoo Shin, Brahma S. Pavse, Josiah P. Hanna

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18699) | [PDF](https://arxiv.org/pdf/2610.18699)

<details>
<summary>Abstract</summary>

Evaluating robot policies before deployment typically requires producing new trajectories through real-world execution, simulators, or learned world models. These rollout-based approaches impose infrastructure requirements; simulator and world-model evaluators additionally face prediction errors that can compound over the evaluation horizon. In this paper, we study off-policy evaluation as an alternative to rollout-based robot-policy evaluation methods. Specifically, we introduce RoboFQE, an evaluator that estimates the discounted expected return of a target policy from offline robot trajector...

</details>

<details>
<summary>Share</summary>

```
RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories

Evaluating robot policies before deployment typically requires producing new trajectories through real-world execution, simulators, or learned world models.

arXiv: https://arxiv.org/abs/2610.18699

#worldmodels #robotics
```

</details>

---

### [Grid or Nodes? Probing Object Memory in World Models Under Partial Observability](https://arxiv.org/abs/2610.18637)

**Authors:** Justin McMillen, Yasin Yilmaz

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18637) | [PDF](https://arxiv.org/pdf/2610.18637)

<details>
<summary>Abstract</summary>

A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also scores 8 points higher in view although no frame is shown, which we attribute to its write-back of its...

</details>

<details>
<summary>Share</summary>

```
Grid or Nodes? Probing Object Memory in World Models Under Partial Observability

A robot's world model must remember objects that leave the camera's view.

arXiv: https://arxiv.org/abs/2610.18637

#worldmodels #robotics
```

</details>

---

### [DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2610.17903)

**Authors:** Shuzheng Wang, Haoxuan Li, Shengzhen Li, Chenxi Wu, Yajing Sun et al. (8 authors)

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17903) | [PDF](https://arxiv.org/pdf/2610.17903)

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving. However, effectively integrating both capabilities for trajectory generation remains challenging. In this work, we propose DriveWLA, a unified World-Language-Action model based on Mixture-of-Transformers (MoT) that jointly models semantic understanding, future scene dynamics, and trajectory generation. DriveWLA consists of three experts: a World Expert for future prediction, a Language Expert for semantic understanding, and an Action...

</details>

<details>
<summary>Share</summary>

```
DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving

Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving.

arXiv: https://arxiv.org/abs/2610.17903

#worldmodels #robotics
```

</details>

---

### [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](https://arxiv.org/abs/2610.17688)

**Authors:** Qihang Huang, Wenhui Huang, Collister Chua, Shiyu Fang, Zhan Chen et al. (9 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17688) | [PDF](https://arxiv.org/pdf/2610.17688)

<details>
<summary>Abstract</summary>

Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving. However, existing occupancy-aware planners typically couple occupancy prediction and action generation through either hierarchical coupling or parallel multi-task learning. Hierarchical methods use occupancy either as a fully predicted future preceding action generation or as an action-conditioned rollout for trajectory evaluation, whereas parallel multi-task methods predict occupancy alongside planning through a separate branch or auxili...

</details>

<details>
<summary>Share</summary>

```
OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching

Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving.

arXiv: https://arxiv.org/abs/2610.17688

#worldmodels #robotics
```

</details>

---

### [Directional Pullback Regularization for Long-Horizon Rollout of Latent World Models in Autonomous Driving](https://arxiv.org/abs/2610.16139)

**Authors:** Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.16139) | [PDF](https://arxiv.org/pdf/2610.16139)

<details>
<summary>Abstract</summary>

Learned world models for autonomous driving operate in unconstrained latent spaces, yet the physical systems they represent are governed by strict non-holonomic constraints: ground vehicles cannot realize instantaneous pure lateral motion. We study long-horizon latent rollout modeling for autonomous driving and ask whether rollout quality can be improved by assigning a motion-aware geometry to latent transitions, rather than by redesigning the predictor architecture. Starting from an unconstrained latent rollout baseline, we introduce Directional Pullback Regularization (DPR), a training time...

</details>

<details>
<summary>Share</summary>

```
Directional Pullback Regularization for Long-Horizon Rollout of Latent World Models in Autonomous Driving

Learned world models for autonomous driving operate in unconstrained latent spaces, yet the physical systems they represent are governed by strict non-holonomic constraints: ground vehicles cannot realize instantaneou...

arXiv: https://arxiv.org/abs/2610.16139

#worldmodels #robotics
```

</details>

---

### [StreamingWAM: Streaming World Action Modeling via Chunk-Wise Staircase Flow Matching](https://arxiv.org/abs/2610.15585)

**Authors:** Shaojie Ren, Jingwen Sun, Zezhi Liu, Hongjin Chen, Xin Jin et al. (7 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15585) | [PDF](https://arxiv.org/pdf/2610.15585) | [Project Page](https://renshaojie233.github.io/StreamingWAM/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs), often built upon pretrained video-generation world models, have emerged as a promising framework for general-purpose and open-ended robot control. However, their real-world deployment often suffers from discontinuous and jerky execution. Existing methods typically address this issue by either improving inference efficiency or enhancing action continuity across prediction chunks, without jointly addressing both challenges. To bridge this gap, we propose StreamingWAM, a streaming-diffusion framework for WAM-based robot control. StreamingWAM combines a noise ladder for...

</details>

<details>
<summary>Share</summary>

```
StreamingWAM: Streaming World Action Modeling via Chunk-Wise Staircase Flow Matching

World Action Models (WAMs), often built upon pretrained video-generation world models, have emerged as a promising framework for general-purpose and open-ended robot control.

arXiv: https://arxiv.org/abs/2610.15585
Project page: https://renshaojie233.github.io/StreamingWAM/

#worldmodels #robotics
```

</details>

---

### [Chunk-wise Model-based Policy Optimization](https://arxiv.org/abs/2610.14564)

**Authors:** Weixi Song, Donglin Wang, Yong-Lu Li

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14564) | [PDF](https://arxiv.org/pdf/2610.14564) | [Project Page](https://song-wx.github.io/cmpo.github.io/)

<details>
<summary>Abstract</summary>

Model-based reinforcement learning has shown superior sample efficiency by leveraging the learned latent dynamics either in the form of derivative-free planning/imagined rollout training or dynamics gradient-based policy updates. While these approaches achieve comparatively fast learning, they all suffer, to varying degrees, from issues of recurrent compounding errors, high inference-time latency, and instability in backward propagation through time (BPTT). In this work, we propose a model-based RL approach that uses the chunk world model as a differentiable training-time evaluator to optimize...

</details>

<details>
<summary>Share</summary>

```
Chunk-wise Model-based Policy Optimization

Model-based reinforcement learning has shown superior sample efficiency by leveraging the learned latent dynamics either in the form of derivative-free planning/imagined rollout training or dynamics gradient-based pol...

arXiv: https://arxiv.org/abs/2610.14564
Project page: https://song-wx.github.io/cmpo.github.io/

#worldmodels #robotics
```

</details>

---

### [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522)

**Authors:** Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2610.13522) | [PDF](https://arxiv.org/pdf/2610.13522)

<details>
<summary>Abstract</summary>

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance of successful demonstrations leaves failure dynamics substantially underrepresented, limiting the ab...

</details>

<details>
<summary>Share</summary>

```
Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions.

arXiv: https://arxiv.org/abs/2610.13522

#worldmodels #robotics
```

</details>

---

### [Dream to Remember: Continual Steering of Generalist Robot Policies with World Models](https://arxiv.org/abs/2610.13816)

**Authors:** Bahey Tharwat, Iman Nematollahi, Marvin Alles, Xingyuan Zhang, Akshay L Chandra et al. (6 authors)

**Published:** 2026-10-09 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.13816) | [PDF](https://arxiv.org/pdf/2610.13816)

<details>
<summary>Abstract</summary>

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering module. We propose Dream to Remember (D2R), which continually steers a frozen generalist policy toward...

</details>

<details>
<summary>Share</summary>

```
Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations.

arXiv: https://arxiv.org/abs/2610.13816

#worldmodels #robotics
```

</details>

---

### [Sampling-based Kinodynamic Planning with World Models](https://arxiv.org/abs/2610.12910)

**Authors:** Yitian Gao, Hanlan Yang, Zachary Kingston

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12910) | [PDF](https://arxiv.org/pdf/2610.12910)

<details>
<summary>Abstract</summary>

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI. However, these optimizers stall on long-horizon tasks where progress requires motion the objective does not reward, such as moving around a block before pushing it. This paper revisits kinodynamic sampling-based motion planning for world models, using the learned model as the propagator of a tree search in latent space. Our key insight is that the sampling strategies devised for high-dimensional search in configuration space apply directly to the lat...

</details>

<details>
<summary>Share</summary>

```
Sampling-based Kinodynamic Planning with World Models

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI.

arXiv: https://arxiv.org/abs/2610.12910

#worldmodels #robotics
```

</details>

---

### [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](https://arxiv.org/abs/2610.12368)

**Authors:** Linkai Liu, Yuntian Zhang, Zhenshan Bing, Chen Chen, Lingjuan Lyu et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12368) | [PDF](https://arxiv.org/pdf/2610.12368)

<details>
<summary>Abstract</summary>

Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences. Generative navigation world models provide this foresight through visual rollouts, which are costly when evaluating multiple candidates. We present LiteNWM, a latent navigation world model that shares visual encoding across candidates and jointly predicts their action-conditioned future representations at multiple horizons, while a learned scorer uses these predictions to select trajectories. In offline evaluations on RECON, SCAND, and SACSoN, LiteNWM reduces macro-aver...

</details>

<details>
<summary>Share</summary>

```
LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild

Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences.

arXiv: https://arxiv.org/abs/2610.12368

#worldmodels #robotics
```

</details>

---

### [Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception](https://arxiv.org/abs/2610.11591)

**Authors:** Feihong Yang, Xiang Long, Jincheng Yu, Jianfei Zhang, Guangjun Ge et al. (7 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.11591) | [PDF](https://arxiv.org/pdf/2610.11591)

<details>
<summary>Abstract</summary>

Robot navigation commonly uses wide-coverage, high-frequency sensing to reduce partial observability; this reliance becomes restrictive when another task temporarily redirects a shared sensor from navigation, interrupting navigation-relevant observations. We study navigation under intermittent perception: acting from an internal spatial belief and looking again only when execution needs a new observation, potentially freeing the shared sensor for other tasks between navigation observations. ALONE, a Bayesian spatial world model, propagates a structured spatial belief using executed actions and...

</details>

<details>
<summary>Share</summary>

```
Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception

Robot navigation commonly uses wide-coverage, high-frequency sensing to reduce partial observability; this reliance becomes restrictive when another task temporarily redirects a shared sensor from navigation, interrup...

arXiv: https://arxiv.org/abs/2610.11591

#worldmodels #robotics
```

</details>

---

### [PlanWAM: Planning-Shaped Future Representations for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.11382)

**Authors:** Jinchang Xu, Hongda Yu, Fengwei Dong, Wenhui Huang, Xi Wei et al. (12 authors)

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.11382) | [PDF](https://arxiv.org/pdf/2610.11382)

<details>
<summary>Abstract</summary>

World models in end-to-end autonomous driving predict future scene evolution to provide foresight for trajectory planning. Existing methods mainly study how to predict the future and how to use it, but less often ask which future representation is actually most useful for planning. To this end, we propose PlanWAM, a Planning-Shaped World Action Model. The key idea is to let the planning task shape the future-state representation, so that it retains the information most useful for planning. A latent world model then predicts this planning-shaped future latent representation from historical obse...

</details>

<details>
<summary>Share</summary>

```
PlanWAM: Planning-Shaped Future Representations for End-to-End Autonomous Driving

World models in end-to-end autonomous driving predict future scene evolution to provide foresight for trajectory planning.

arXiv: https://arxiv.org/abs/2610.11382

#worldmodels #robotics
```

</details>

---

### [Neurosymbolic Learning of Interpretable World Models](https://arxiv.org/abs/2610.19955)

**Authors:** Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini, Alessandro Daniele, Emile van Krieken

**Published:** 2026-10-14 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.19955) | [PDF](https://arxiv.org/pdf/2610.19955)

<details>
<summary>Abstract</summary>

World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about the world. We introduce Concept-Grounded World Models (CGWMs), a neurosymbolic world model design that instead learns interpretable concept representations. We learn these concepts from observations using explicit and complete knowledge, expressed in temporal logic, that specifies the valid world states and the temporal...

</details>

<details>
<summary>Share</summary>

```
Neurosymbolic Learning of Interpretable World Models

World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour.

arXiv: https://arxiv.org/abs/2610.19955

#worldmodels #robotics
```

</details>

---

### [Enhancing Latent World Models with Associative Memory](https://arxiv.org/abs/2610.19683)

**Authors:** Yuwei Sun, Siyu Zhu

**Published:** 2026-10-14 | **Categories:** cs.LG, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.19683) | [PDF](https://arxiv.org/pdf/2610.19683)

<details>
<summary>Abstract</summary>

World models trained via latent dynamics offer a scalable path for embodied planning, yet existing methods suffer from representational collapse, computational overhead, and limited long-horizon capability. We introduce a memory-enhanced latent world model that augments JEPA-style prediction with a content-addressable memory bank. Our approach learns high-level representations directly from observations, operating at multiple temporal scales within a shared latent space, and conditions predictions via adaptive layer normalization. To prevent collapse and ensure effective memory usage, we desig...

</details>

<details>
<summary>Share</summary>

```
Enhancing Latent World Models with Associative Memory

World models trained via latent dynamics offer a scalable path for embodied planning, yet existing methods suffer from representational collapse, computational overhead, and limited long-horizon capability.

arXiv: https://arxiv.org/abs/2610.19683

#worldmodels #robotics
```

</details>

---

### [Esports World Model Dataset](https://arxiv.org/abs/2610.16166)

**Authors:** Weiyu Ma, Zeyuan Gong, Xuhui Liu, Wenxuan Zhang, Jian Ding et al. (8 authors)

**Published:** 2026-10-12 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.16166) | [PDF](https://arxiv.org/pdf/2610.16166)

<details>
<summary>Abstract</summary>

Interactive world models must capture how multiple participants jointly change a shared environment while observing different parts of it. Competitive games make this challenge concrete: players cooperate and compete, while fog of war, team vision and camera placement determine what each can see. Modeling these interactions requires data that connect individual observations and actions to shared state and events. We introduce the Esports World Model Dataset (EWM), a collection of human gameplay spanning StarCraft II, Dota 2 and Counter-Strike 2, with 3,053 games and maps and approximately 4,88...

</details>

<details>
<summary>Share</summary>

```
Esports World Model Dataset

Interactive world models must capture how multiple participants jointly change a shared environment while observing different parts of it.

arXiv: https://arxiv.org/abs/2610.16166

#worldmodels #robotics
```

</details>

---

### [SurgCast: Action-Conditioned Future Skeletons for Controllable Surgical World Models](https://arxiv.org/abs/2610.15645)

**Authors:** Wanhao Liu, Rulin Zhou, Liangjing Shao, Zhaocheng Lin, Dongyue Li et al. (12 authors)

**Published:** 2026-10-11 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.15645) | [PDF](https://arxiv.org/pdf/2610.15645)

<details>
<summary>Abstract</summary>

Surgical world models must turn prospective robot actions into visually faithful, structurally consistent instrument motion. We introduce SurgCast, which predicts future instrument skeletons from current structure, robot state, and future actions, then uses the forecast to control video generation. Dual-path injection combines skeleton geometry with derived, instrument-specific motion descriptors through geometric residuals and conditioning modulation. Both paths complement native action conditioning and are retained in a four-step causal student. On SutureBot and SRTH-Porcine-Cholei, the teac...

</details>

<details>
<summary>Share</summary>

```
SurgCast: Action-Conditioned Future Skeletons for Controllable Surgical World Models

Surgical world models must turn prospective robot actions into visually faithful, structurally consistent instrument motion.

arXiv: https://arxiv.org/abs/2610.15645

#worldmodels #robotics
```

</details>

---

### [A Plausible Future Is Not a Causal Future: Can Video Models Generate How the World Unfolds?](https://arxiv.org/abs/2610.15562)

**Authors:** Jialiang Li, Zhengning Xu, Zongyang Ma, Shaobo Cui

**Published:** 2026-10-11 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.15562) | [PDF](https://arxiv.org/pdf/2610.15562) | [Code](https://github.com/SJTU-DeepDeltaLab/CausalCascade)

<details>
<summary>Abstract</summary>

Large-scale video generation models are increasingly viewed as a promising path toward world models, yet their ability to capture causally coherent physical dynamics remains poorly understood. Existing evaluations largely emphasize visual quality, prompt adherence, or broad physical plausibility, leaving open whether a model can faithfully realize a complete causal cascade, in which an initiating event propagates through causally dependent interactions to a terminal outcome. We introduce CausalCascade, a simulator-grounded benchmark centered on 50 event-rich Blender scenes with structured even...

</details>

<details>
<summary>Share</summary>

```
A Plausible Future Is Not a Causal Future: Can Video Models Generate How the World Unfolds?

Large-scale video generation models are increasingly viewed as a promising path toward world models, yet their ability to capture causally coherent physical dynamics remains poorly understood.

arXiv: https://arxiv.org/abs/2610.15562
Code: https://github.com/SJTU-DeepDeltaLab/CausalCascade

#worldmodels #robotics
```

</details>

---

### [MORE: Learning Motion-Oriented Registers for Driving World Models and Planning](https://arxiv.org/abs/2610.14871)

**Authors:** Yingdong Gu, Haoyu Wang, Shaocheng Yan, Zhenjun Zhao, Hao Han et al. (12 authors)

**Published:** 2026-10-10 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.14871) | [PDF](https://arxiv.org/pdf/2610.14871)

<details>
<summary>Abstract</summary>

By predicting future states, latent world models provide rich self-supervision for end-to-end driving, but often inherit dense features from pretrained visual encoders as their world-state interface. This creates a mismatch: visual pretraining produces information-rich, spatially dense features, but their adaptation for motion-conditioned world modeling and planning is deferred to downstream training. The dense grid also makes future prediction more computationally expensive as visual resolution increases. We therefore argue that video pretraining should directly learn state representations su...

</details>

<details>
<summary>Share</summary>

```
MORE: Learning Motion-Oriented Registers for Driving World Models and Planning

By predicting future states, latent world models provide rich self-supervision for end-to-end driving, but often inherit dense features from pretrained visual encoders as their world-state interface.

arXiv: https://arxiv.org/abs/2610.14871

#worldmodels #robotics
```

</details>

---

### [Latent World Action Model for GUI Agents](https://arxiv.org/abs/2610.14228)

**Authors:** Seungjun Yu, Hojun Choi, Seojeong Park, Jaeyo Shin, Hyunjung Shim

**Published:** 2026-10-09 | **Categories:** cs.CV, cs.AI, cs.HC | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.14228) | [PDF](https://arxiv.org/pdf/2610.14228) | [Code](https://github.com/sjyu001/latent2world)

<details>
<summary>Abstract</summary>

Pixel-space world models have recently emerged as a promising approach for GUI agents, predicting future screens prior to execution and subsequently re-perceiving them for action selection. However, this two-stage paradigm faces two key challenges in GUI environments: (L1) the high computational cost of pixel reconstruction and (L2) the need to reconstruct large and diverse appearance-level details beyond what is required for action selection. In practice, this screen-generation objective can induce an identity shortcut problem, where future-state prediction largely preserves the current state...

</details>

<details>
<summary>Share</summary>

```
Latent World Action Model for GUI Agents

Pixel-space world models have recently emerged as a promising approach for GUI agents, predicting future screens prior to execution and subsequently re-perceiving them for action selection.

arXiv: https://arxiv.org/abs/2610.14228
Code: https://github.com/sjyu001/latent2world

#worldmodels #robotics
```

</details>

---

### [Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction](https://arxiv.org/abs/2610.12299)

**Authors:** Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12299) | [PDF](https://arxiv.org/pdf/2610.12299)

<details>
<summary>Abstract</summary>

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate multi-agent egocentric world modeling as synchronized ego-stream generation for multiple agents interacting through fine-grained actions in a shared world. This requires cross-view actio...

</details>

<details>
<summary>Share</summary>

```
Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent.

arXiv: https://arxiv.org/abs/2610.12299

#worldmodels #robotics
```

</details>

---

### [AtomWorld-Mirror: Macro-Step World Modeling of Critical Evolution Backbones for Materials Dynamics](https://arxiv.org/abs/2610.11527)

**Authors:** Ziming Pan, Ruge Zhang, Haozhi Han, Junkai Zhou, Xingyuan Chen et al. (10 authors)

**Published:** 2026-10-08 (updated 2026-10-10) | **Categories:** cs.AI, cond-mat.mtrl-sci | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11527) | [PDF](https://arxiv.org/pdf/2610.11527) | [Project Page](https://atomworld-mirror.github.io)

<details>
<summary>Abstract</summary>

Atomistic simulation is a fundamental tool for studying long-term materials evolution, from diffusion and defect dynamics to interfacial reactions and fracture. Yet conventional simulators typically advance at microscopic resolution, spending substantial computation on low-impact local updates before reaching structurally consequential states, an evolutionary-resolution bottleneck that limits long-horizon simulation. We propose AtomWorld-Mirror, a time-aware macro-step world model for the critical evolution backbone of atomic systems. For Step-Wise atomistic simulation, AtomWorld-Mirror distil...

</details>

<details>
<summary>Share</summary>

```
AtomWorld-Mirror: Macro-Step World Modeling of Critical Evolution Backbones for Materials Dynamics

Atomistic simulation is a fundamental tool for studying long-term materials evolution, from diffusion and defect dynamics to interfacial reactions and fracture.

arXiv: https://arxiv.org/abs/2610.11527
Project page: https://atomworld-mirror.github.io

#worldmodels #robotics
```

</details>

---

### [AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding](https://arxiv.org/abs/2610.11060)

**Authors:** Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song et al. (9 authors)

**Published:** 2026-10-08 (updated 2026-10-13) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.11060) | [PDF](https://arxiv.org/pdf/2610.11060) | [Project Page](https://afforddrive3d.github.io/)

<details>
<summary>Abstract</summary>

World-action models have recently improved autonomous driving by jointly learning future scene prediction and trajectory generation. Most existing approaches model the future primarily through RGB appearance, and recent works have begun to incorporate geometric prediction to improve spatial understanding. However, dense geometry describes the spatial layout of the entire scene without indicating which parts are most relevant to the ego vehicle's action. For driving, the model must also identify and anticipate where it can safely move and which regions may pose collision risks. Jointly modeling...

</details>

<details>
<summary>Share</summary>

```
AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding

World-action models have recently improved autonomous driving by jointly learning future scene prediction and trajectory generation.

arXiv: https://arxiv.org/abs/2610.11060
Project page: https://afforddrive3d.github.io/

#worldmodels #robotics
```

</details>

---

### [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](https://arxiv.org/abs/2610.18697)

**Authors:** Jingbo Xu, Jianjie Fang, Zhuohang Li, Zihao Song, Zhaolu Wang et al. (12 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18697) | [PDF](https://arxiv.org/pdf/2610.18697)

<details>
<summary>Abstract</summary>

World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities required by each paradigm. We propose UniW(A)M, a mixture-of-experts world-(action) model built upon di...

</details>

<details>
<summary>Share</summary>

```
UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models

World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively.

arXiv: https://arxiv.org/abs/2610.18697

#worldmodels #robotics
```

</details>

---

### [Acting Through Registers](https://arxiv.org/abs/2610.17638)

**Authors:** Yiwei Zhang, Yantai Yang, Jin Gao, Jin Lou, Andong Chen et al. (10 authors)

**Published:** 2026-10-13 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.17638) | [PDF](https://arxiv.org/pdf/2610.17638)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood. We identify persistent high-norm spatial outliers in WAM representations and find that their action relevance persists even after normalization and K/V projection attenuate their extreme magnitude. Motivated by this observation, we introduce RegisterWAM, which adds learnable non-spatial registers to the world model and uses them directly for action conditioning. Registers alone do not fully eliminate spatial o...

</details>

<details>
<summary>Share</summary>

```
Acting Through Registers

World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood.

arXiv: https://arxiv.org/abs/2610.17638

#worldmodels #robotics
```

</details>

---

### [G$^2$WAM: World Action Models for Efficient and Geometry Grounded Image-Goal Navigation](https://arxiv.org/abs/2610.16558)

**Authors:** Ke Gui, Chenghao Shi, Ziyue Wang, Longwen Chen, Xieyuanli Chen et al. (6 authors)

**Published:** 2026-10-12 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.16558) | [PDF](https://arxiv.org/pdf/2610.16558)

<details>
<summary>Abstract</summary>

World models capture environment dynamics and support counterfactual reasoning for planning. In image-goal navigation, where the target often lies beyond the current field of view, the agent must not only model environmental dynamics but also maintain a persistent spatial memory of the scene. Existing approaches either introduce spatial context by fine-tuning pretrained models on the target task, which underexploits their spatial priors, or rely on external 3D reconstruction, which is computationally expensive for real-world deployment. In this paper, we propose the Geometry Grounded World Act...

</details>

<details>
<summary>Share</summary>

```
G$^2$WAM: World Action Models for Efficient and Geometry Grounded Image-Goal Navigation

World models capture environment dynamics and support counterfactual reasoning for planning.

arXiv: https://arxiv.org/abs/2610.16558

#worldmodels #robotics
```

</details>

---

### [ProWorld: Multi-View World Model with Proprioceptive Feedback for Closed-Loop Policy Evaluation](https://arxiv.org/abs/2610.15294)

**Authors:** Zijun Wang, Tianyi Yan, Haokun Lin, Panwen Hu, Bohang He et al. (15 authors)

**Published:** 2026-10-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.15294) | [PDF](https://arxiv.org/pdf/2610.15294)

<details>
<summary>Abstract</summary>

Evaluating robot manipulation policies through repeated physical trials is costly. We study whether an action-conditioned world model can serve as a closed-loop test environment whose policy success rates track those on real robots. Beyond realistic video, the model must return the camera views and proprioceptive state needed for the policy's next action and preserve failed-action outcomes to avoid overestimating policy capability. We introduce ProWorld, a world model that jointly predicts multi-view video and robot state, then feeds both back to a frozen policy for repeated interaction. ProWo...

</details>

<details>
<summary>Share</summary>

```
ProWorld: Multi-View World Model with Proprioceptive Feedback for Closed-Loop Policy Evaluation

Evaluating robot manipulation policies through repeated physical trials is costly.

arXiv: https://arxiv.org/abs/2610.15294

#worldmodels #robotics
```

</details>

---

### [LeHami: Symplectic Latent Dynamics for World Models](https://arxiv.org/abs/2610.15267)

**Authors:** Romina Yalovetzky, Randall Balestriero, Yann LeCun

**Published:** 2026-10-11 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.15267) | [PDF](https://arxiv.org/pdf/2610.15267)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over long rollouts. We introduce Symplectic Hamiltonian JEPA (LeHami), which replaces the standard predictor with an action-conditioned Hamiltonian flow over a structured latent state (q, p) integrated using an exactly symplectic leapfrog step. This construction preserves phase-space volume at every rollout step and rules out uniform contraction, asymptotically stable fixed points, and merging of distinct latent states, i...

</details>

<details>
<summary>Share</summary>

```
LeHami: Symplectic Latent Dynamics for World Models

Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over long rollouts.

arXiv: https://arxiv.org/abs/2610.15267

#worldmodels #robotics
```

</details>

---

### [AnyRank: Reliable Anytime Policy Ranking via Sequential Testing](https://arxiv.org/abs/2610.14603)

**Authors:** Apurva Badithela, David Snyder, Tenny Yin, Jade Sceats, George Pappas et al. (9 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.14603) | [PDF](https://arxiv.org/pdf/2610.14603)

<details>
<summary>Abstract</summary>

Due to the high cost of hardware experiments, robot policies are predominantly evaluated by comparing their empirical performance on a limited number of hardware trials. However, finite-sample statistical uncertainty can lead to erroneous conclusions, especially when ranking multiple policies using a fixed batch of evaluation data. We propose AnyRank: a sequential method for multi-policy ranking that (i) adaptively allocates trials to hard-to-separate policies, (ii) provides (partial) rankings at any stopping time while bounding the probability of an incorrect ranking, and (iii) optionally exp...

</details>

<details>
<summary>Share</summary>

```
AnyRank: Reliable Anytime Policy Ranking via Sequential Testing

Due to the high cost of hardware experiments, robot policies are predominantly evaluated by comparing their empirical performance on a limited number of hardware trials.

arXiv: https://arxiv.org/abs/2610.14603

#worldmodels #robotics
```

</details>

---

### [Remembering What Matters for Long-Horizon Robotic World Models](https://arxiv.org/abs/2610.14583)

**Authors:** Hao Wu, Tianyu Shao, Shengju Qian, Yizhou Zhao, Fan Zhang et al. (13 authors)

**Published:** 2026-10-10 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.14583) | [PDF](https://arxiv.org/pdf/2610.14583)

<details>
<summary>Abstract</summary>

Autoregressive robot video world models based on discrete visual tokens remain unreliable over long rollout horizons. Retaining the entire generated history does not necessarily improve prediction quality. We investigate a possible memory-role conflict in Full Context decoding: persistent scene information, recent visual-action states, and stale generated history compete for attention despite their different predictive roles. This perspective motivates ReCAP (Receding Context with Anchor Preservation), a training-free context-scheduling method for long-horizon robot video world models. ReCAP k...

</details>

<details>
<summary>Share</summary>

```
Remembering What Matters for Long-Horizon Robotic World Models

Autoregressive robot video world models based on discrete visual tokens remain unreliable over long rollout horizons.

arXiv: https://arxiv.org/abs/2610.14583

#worldmodels #robotics
```

</details>

---

### [Learning to See through Action: Predictive Curiosity for Robots](https://arxiv.org/abs/2610.14302)

**Authors:** Stelios Zarifis, Panagiotis Filntisis, George Retsinas, Petros Maragos

**Published:** 2026-10-09 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.14302) | [PDF](https://arxiv.org/pdf/2610.14302)

<details>
<summary>Abstract</summary>

Humans and animals do not learn vision from a fixed set of data: they move, interact, and learn from the visual consequences of their actions. Motivated by this developmental view, we study whether robots can improve visual learning by actively collecting experience through curiosity-driven interaction. We introduce DySCOVER, a self-supervised framework for active robot visual learning. A robot observes RGB frames, learns a visual autoencoder that encodes and reconstructs them, and trains a recurrent world model to predict the next visual latent state conditioned on the current state and actio...

</details>

<details>
<summary>Share</summary>

```
Learning to See through Action: Predictive Curiosity for Robots

Humans and animals do not learn vision from a fixed set of data: they move, interact, and learn from the visual consequences of their actions.

arXiv: https://arxiv.org/abs/2610.14302

#worldmodels #robotics
```

</details>

---

### [LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC](https://arxiv.org/abs/2610.12407)

**Authors:** Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy

**Published:** 2026-10-08 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12407) | [PDF](https://arxiv.org/pdf/2610.12407)

<details>
<summary>Abstract</summary>

World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions. We introduce LeWAM, a bidirectional transformer for forward, backward, inverse dynamics and policy prediction, on a decoder-free JEPA latent trained end-to-end through all four modes. We see the following benefits: 1) Alignment: linear probes read robot and object state from LeWAM's latent better than from a regular Le World Model (a forward-only JEPA world model), while the latent ignores...

</details>

<details>
<summary>Share</summary>

```
LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC

World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions.

arXiv: https://arxiv.org/abs/2610.12407

#worldmodels #robotics
```

</details>

---

### [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220)

**Authors:** Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.20220) | [PDF](https://arxiv.org/pdf/2610.20220)

<details>
<summary>Abstract</summary>

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show it can be made dramatically more efficient. Pushing this efficiency to its extreme, we reduce trajectory supervision to a single sample, the strictest setting possible, and find that...

</details>

<details>
<summary>Share</summary>

```
Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models.

arXiv: https://arxiv.org/abs/2610.20220

#worldmodels #robotics
```

</details>

---

### [SceneAE: Scene Generation and Reconstruction in Queryable 3D-Anchored Latent Space](https://arxiv.org/abs/2610.19708)

**Authors:** Shuofeng Sun, Wenzhao Zheng, Yunpeng Zhang, Yi Wu, Linqing Zhao et al. (6 authors)

**Published:** 2026-10-14 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.19708) | [PDF](https://arxiv.org/pdf/2610.19708)

<details>
<summary>Abstract</summary>

Recent video world models have increasingly adopted 3D memory mechanisms to integrate historical observations into a lightweight and persistent scene representation. This naturally raises a complementary question: if 3D representations can serve as an effective mechanism for memorizing observed scenes, can they also be directly used as the latent space for reconstructing and generating scenes? Motivated by this idea, we represent a scene as a compact and unstructured 3D-anchored latent space (\textbf{SceneAE}). Each latent combines an explicit 3D position with an implicit content feature and i...

</details>

<details>
<summary>Share</summary>

```
SceneAE: Scene Generation and Reconstruction in Queryable 3D-Anchored Latent Space

Recent video world models have increasingly adopted 3D memory mechanisms to integrate historical observations into a lightweight and persistent scene representation.

arXiv: https://arxiv.org/abs/2610.19708

#worldmodels #robotics
```

</details>

---

### [AffectWorld: Benchmarking Emotion-Driven Future World Prediction](https://arxiv.org/abs/2610.18305)

**Authors:** Changhao Song, Yacong Chen, Hui Gao, Yazhou Zhang, Peng Zhang

**Published:** 2026-10-13 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2610.18305) | [PDF](https://arxiv.org/pdf/2610.18305)

<details>
<summary>Abstract</summary>

The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotions shape human actions. However, existing world model benchmarks primarily assess physical plausibility and perceptual quality, leaving emotion-driven world evolution largely untested.We introduce AffectWorld, a benchmark that evaluates the chain Emotion-Action-World State through three tasks: World-State Consistency, Emotion-Action Consistency, and Causal Consistency. It comprises 1,498 everyday video samples annotated with plausible emotions, act...

</details>

<details>
<summary>Share</summary>

```
AffectWorld: Benchmarking Emotion-Driven Future World Prediction

The world encompasses both physical environments and human actors.

arXiv: https://arxiv.org/abs/2610.18305

#worldmodels #robotics
```

</details>

---

### [InfraWorld: Motion-Aware World Modeling for Roadside 4D Occupancy Forecasting](https://arxiv.org/abs/2610.14544)

**Authors:** Songkai Wang, Xiaokai Bai, Lei Yang, Hui-liang Shen

**Published:** 2026-10-10 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.14544) | [PDF](https://arxiv.org/pdf/2610.14544)

<details>
<summary>Abstract</summary>

Roadside 4D occupancy forecasting predicts future semantic occupancy in a fixed infrastructure coordinate system. Roadside scenes are globally structured yet locally evolving, requiring comprehensive scene-level context while precisely modeling sparse localized motion. However, existing forecasting paradigms struggle to tackle both requirements. To address this limitation, we propose InfraWorld, a world model formulating roadside occupancy forecasting as selective state evolution. InfraWorld maintains a dense BEV state for the complete scene and persistent motion queries for moving regions, as...

</details>

<details>
<summary>Share</summary>

```
InfraWorld: Motion-Aware World Modeling for Roadside 4D Occupancy Forecasting

Roadside 4D occupancy forecasting predicts future semantic occupancy in a fixed infrastructure coordinate system.

arXiv: https://arxiv.org/abs/2610.14544

#worldmodels #robotics
```

</details>

---

### [Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217)

**Authors:** Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang et al. (7 authors)

**Published:** 2026-10-09 (updated 2026-10-12) | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.13217) | [PDF](https://arxiv.org/pdf/2610.13217)

<details>
<summary>Abstract</summary>

Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models. State-of-the-art systems achieve controllability primarily through image-to-video (I2V) generation, in which an injected anchor image determines the identity, composition, and style of the resulting video. In modern pipelines, this anchor is synthesized by a text-to-image (T2I) generator. This raises a largely overlooked question: Are images obtained directly from the T2I model truly suitable for current video models? Our analysis shows tha...

</details>

<details>
<summary>Share</summary>

```
Golden Anchor for Video Generation

Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models.

arXiv: https://arxiv.org/abs/2610.13217

#worldmodels #robotics
```

</details>

---

### [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](https://arxiv.org/abs/2610.12459)

**Authors:** Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.12459) | [PDF](https://arxiv.org/pdf/2610.12459)

<details>
<summary>Abstract</summary>

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as \emph{clos...

</details>

<details>
<summary>Share</summary>

```
WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced.

arXiv: https://arxiv.org/abs/2610.12459

#worldmodels #robotics
```

</details>

---

### [RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning](https://arxiv.org/abs/2610.12333)

**Authors:** Ruixiang Ouyang, Guanren Qiao, Fansen Meng, Yueci Deng, Ruixing Jin et al. (7 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.AI, cs.GR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.12333) | [PDF](https://arxiv.org/pdf/2610.12333)

<details>
<summary>Abstract</summary>

Accurate simulation of rigid-body interactions is essential for predictive physical world models. Despite recent progress in modeling object dynamics, capturing how local contacts between surfaces shape object motion remains challenging. While end-to-end world models predict interactions across entire scenes or objects, in practice, rigid-body contact is inherently local, and only nearby surfaces can directly exchange contact forces. Motivated by this observation, we introduce Rigid-body Contact Reasoning (RiCo), which represents interactions between objects through sparse neighborhoods of con...

</details>

<details>
<summary>Share</summary>

```
RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning

Accurate simulation of rigid-body interactions is essential for predictive physical world models.

arXiv: https://arxiv.org/abs/2610.12333

#worldmodels #robotics
```

</details>

---

### [CausalDreamer: Learning Predictive World Models with Latent Disentanglement](https://arxiv.org/abs/2610.12016)

**Authors:** Prince Jha, Nils Lukas, Kun Zhang, Salem Lahlou

**Published:** 2026-10-08 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.12016) | [PDF](https://arxiv.org/pdf/2610.12016)

<details>
<summary>Abstract</summary>

World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward. Generative world models such as Dreamer 4 consist of a video tokenizer, which encodes each frame into a latent, and a dynamics model, which is pretrained to predict future latents from past latents and actions. Yet the tokenizer is trained with a reconstruction objective, without action or reward supervision, so its latent provides no explicit mechanism to separate controllable, uncontrollable, reward-relevant, and reward-irrelevant information. We propose \te...

</details>

<details>
<summary>Share</summary>

```
CausalDreamer: Learning Predictive World Models with Latent Disentanglement

World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward.

arXiv: https://arxiv.org/abs/2610.12016

#worldmodels #robotics
```

</details>

---

### [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942)

**Authors:** Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu et al. (6 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.11942) | [PDF](https://arxiv.org/pdf/2610.11942)

<details>
<summary>Abstract</summary>

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the observed screen requires a second model to judge the two. We argue that a world model meant for verificat...

</details>

<details>
<summary>Share</summary>

```
Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack.

arXiv: https://arxiv.org/abs/2610.11942

#worldmodels #robotics
```

</details>

---

### [D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control](https://arxiv.org/abs/2610.17114)

**Authors:** Xuan Wen, Baichao Wang

**Published:** 2026-10-12 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.17114) | [PDF](https://arxiv.org/pdf/2610.17114)

<details>
<summary>Abstract</summary>

Frontier large language models (LLMs) now reason about space well enough to program robots, yet the world models behind robot policies are implicit, held in network weights or predicted video, and cannot be inspected or corrected directly. We present D-World, an explicit world-language-action model built on the Sense, Plan and Act decomposition. A perception agent writes the scene as an executable digital twin using generated vision and geometry code. A planning agent searches for actions in simulation and, after each executed action chunk, revises the twin's object states and named physical p...

</details>

<details>
<summary>Share</summary>

```
D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control

Frontier large language models (LLMs) now reason about space well enough to program robots, yet the world models behind robot policies are implicit, held in network weights or predicted video, and cannot be inspected...

arXiv: https://arxiv.org/abs/2610.17114

#worldmodels #robotics
```

</details>

---

### [What Limits Cross-Task Generalization in World Action Models?](https://arxiv.org/abs/2610.16641)

**Authors:** Chen Zhao, Zipeng Ye, Yihan Lin, Yuchen Xie, Jing Zhang

**Published:** 2026-10-12 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.16641) | [PDF](https://arxiv.org/pdf/2610.16641)

<details>
<summary>Abstract</summary>

Cross-task generalization remains difficult for world action models (WAMs), even when their predicted futures depict plausible manipulation. This gap can be attributed directly: we make this gap directly testable by decoupling a WAM into a world model and an inverse-dynamics model (IDM), then holding the IDM fixed while replacing the source of future images. We introduce Align Once, Evaluate Everywhere (AoE), a camera-space inverse-dynamics model pretrained on large-scale robot data, which provides this recovery interface for different future sources across tasks and environments. Through it,...

</details>

<details>
<summary>Share</summary>

```
What Limits Cross-Task Generalization in World Action Models?

Cross-task generalization remains difficult for world action models (WAMs), even when their predicted futures depict plausible manipulation.

arXiv: https://arxiv.org/abs/2610.16641

#worldmodels #robotics
```

</details>

---

### [Observation-Referenced Tissue Deformation Forecasting with Tool-Driven and Residual Dynamics](https://arxiv.org/abs/2610.14191)

**Authors:** Tom Olesch, Nan Xiao, Xiongye Xiao, Jonathan C. DeLong, Fei Liu

**Published:** 2026-10-09 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14191) | [PDF](https://arxiv.org/pdf/2610.14191)

<details>
<summary>Abstract</summary>

Forecasting tissue deformation from future instrument motion could support predictive planning and increasingly autonomous surgical systems. We study this problem using a scene-specific differentiable surface model fitted to an observed tool-tissue interaction window. Rather than forecasting absolute simulated positions, we introduce an \textit{observation-referenced} formulation that anchors each tissue point to its last valid observation and adds only the deformation induced by the known, preplanned future tool trajectory. This reduces sensitivity to reconstruction, initialization, and persi...

</details>

<details>
<summary>Share</summary>

```
Observation-Referenced Tissue Deformation Forecasting with Tool-Driven and Residual Dynamics

Forecasting tissue deformation from future instrument motion could support predictive planning and increasingly autonomous surgical systems.

arXiv: https://arxiv.org/abs/2610.14191

#worldmodels #robotics
```

</details>

---

### [World Modeling through Spectral Alignment](https://arxiv.org/abs/2610.15429)

**Authors:** Holger Molin, William Peng, Marco Bagatella, Randall Balestriero

**Published:** 2026-10-11 | **Categories:** cs.LG, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.15429) | [PDF](https://arxiv.org/pdf/2610.15429)

<details>
<summary>Abstract</summary>

How do we tell a world model what information to preserve? We study this question through the lens of spectral representation learning. We introduce SpecWM, a JEPA framework that explicitly specifies desired relationships between observations through a target similarity kernel and trains the encoder to reproduce those relationships in its embedding geometry. Different kernels provide different supervision, ranging from physical state information to a fully self-supervised temporal kernel requiring only the ordering of observations within trajectories. We characterize the global optima of the o...

</details>

<details>
<summary>Share</summary>

```
World Modeling through Spectral Alignment

How do we tell a world model what information to preserve?

arXiv: https://arxiv.org/abs/2610.15429

#worldmodels #robotics
```

</details>

---

### [MHWA: Multi-timescale Hierarchical World-Action Model](https://arxiv.org/abs/2610.14727)

**Authors:** Pengcheng Pan, Guoqing Ma, Yuhan Zhang, Yang Chen, Yichen Liu et al. (7 authors)

**Published:** 2026-10-10 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.14727) | [PDF](https://arxiv.org/pdf/2610.14727)

<details>
<summary>Abstract</summary>

Autoregressive world models have emerged as a powerful paradigm for sample efficient decision making, yet their open loop rollouts often exhibit increasing drift that leads to error accumulation even within a relatively small planning horizon. Hierarchical temporal abstraction is a natural candidate to mitigate such drift by reducing the effective prediction horizon; however, existing hierarchical designs can introduce added structural and conceptual complexity, sometimes making them difficult to control and limiting gains over flat baselines. To this end, we introduce MHWA (Multi-timescale Hi...

</details>

<details>
<summary>Share</summary>

```
MHWA: Multi-timescale Hierarchical World-Action Model

Autoregressive world models have emerged as a powerful paradigm for sample efficient decision making, yet their open loop rollouts often exhibit increasing drift that leads to error accumulation even within a relative...

arXiv: https://arxiv.org/abs/2610.14727

#worldmodels #robotics
```

</details>

---

### [Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing](https://arxiv.org/abs/2610.12881)

**Authors:** Zheng Ren, Yanning Wang, Ziheng Huang, Fei Huang, Shiqi Wang et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12881) | [PDF](https://arxiv.org/pdf/2610.12881)

<details>
<summary>Abstract</summary>

Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models. However, existing evaluations of multimodal large language models (MLLMs) for spatial reasoning rely predominantly on static question-answering (QA) over small-scale or synthetic scenes, rarely probing whether models can modify spatial configurations while satisfying explicit geometric constraints. We introduce GeoSpatialBench, a benchmark designed to evaluate an escalating progression of spatial cognition, ranging from spatial relation unde...

</details>

<details>
<summary>Share</summary>

```
Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing

Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models.

arXiv: https://arxiv.org/abs/2610.12881

#worldmodels #robotics
```

</details>

---

### [What 30,000 Hours of Ego-centric Video Does Not Teach](https://arxiv.org/abs/2610.12464)

**Authors:** Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov et al. (10 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12464) | [PDF](https://arxiv.org/pdf/2610.12464)

<details>
<summary>Abstract</summary>

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains ne...

</details>

<details>
<summary>Share</summary>

```
What 30,000 Hours of Ego-centric Video Does Not Teach

World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment.

arXiv: https://arxiv.org/abs/2610.12464

#worldmodels #robotics
```

</details>

---

### [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417)

**Authors:** Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang et al. (12 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.CL, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.12417) | [PDF](https://arxiv.org/pdf/2610.12417)

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a traini...

</details>

<details>
<summary>Share</summary>

```
WOVEN: Weaving Visual World Modeling into Multimodal LLMs

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning.

arXiv: https://arxiv.org/abs/2610.12417

#worldmodels #robotics
```

</details>

---

### [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](https://arxiv.org/abs/2610.11794)

**Authors:** Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov et al. (8 authors)

**Published:** 2026-10-08 | **Categories:** cs.AI, cs.CL, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.11794) | [PDF](https://arxiv.org/pdf/2610.11794)

<details>
<summary>Abstract</summary>

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects...

</details>

<details>
<summary>Share</summary>

```
Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives.

arXiv: https://arxiv.org/abs/2610.11794

#worldmodels #robotics
```

</details>

---
