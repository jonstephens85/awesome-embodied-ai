# World Models

Papers on world models for robotics, video prediction, interactive simulation, and planning.

**Last updated:** 2026-10-14 00:44 UTC

**Papers shown:** 36 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

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

### [Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation](https://arxiv.org/abs/2610.09309)

**Authors:** Tzu-Yu Chuang, Ching-Hsiang Chang, Yi-Hsiu Lee, Yi-Ting Chen, Min Sun et al. (6 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in abstract; project page; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09309) | [PDF](https://arxiv.org/pdf/2610.09309) | [Project Page](https://claire0730.github.io/executable-goals/) | [Code](https://github.com/Claire0730/executable-goals)

<details>
<summary>Abstract</summary>

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control. When training supervises future prediction alone, terminal goal accuracy is not an explicit learning objective, even when geometric recovery is available. We present Entity-Level Goal Readout, a learned prediction-to-execution interface that makes the executable terminal goal an explicit output of a 3D trace world model. It combines object-centric pose prediction with translation grounded in obser...

</details>

<details>
<summary>Share</summary>

```
Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control.

arXiv: https://arxiv.org/abs/2610.09309
Project page: https://claire0730.github.io/executable-goals/
Code: https://github.com/Claire0730/executable-goals

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

### [Cross-Embodiment Robot Foundation World Models with Latent Actions](https://arxiv.org/abs/2610.10846)

**Authors:** Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan et al. (12 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10846) | [PDF](https://arxiv.org/pdf/2610.10846) | [Project Page](https://lacwm.github.io/)

<details>
<summary>Abstract</summary>

The diversity of robot embodiments and action spaces makes it challenging to build robot world models that generalize across different embodiments. We introduce the Latent Action-Conditioned Robot World Model (LAC-WM), which operates within a learned unified latent action space shared across diverse embodiments. This unified action space improves the world model's performance when adapted to previously unseen robot embodiments. We compare LAC-WM with an Explicit Action-Conditioned World Model (EAC-WM), which conditions on explicit motion labels. Our results show that explicit action conditioni...

</details>

<details>
<summary>Share</summary>

```
Cross-Embodiment Robot Foundation World Models with Latent Actions

The diversity of robot embodiments and action spaces makes it challenging to build robot world models that generalize across different embodiments.

arXiv: https://arxiv.org/abs/2610.10846
Project page: https://lacwm.github.io/

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

### [Sparse Planning in Visual World Models via Cost Gradients](https://arxiv.org/abs/2610.10274)

**Authors:** Yingchen Xu, Edward Grefenstette

**Published:** 2026-10-07 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.10274) | [PDF](https://arxiv.org/pdf/2610.10274) | [Project Page](https://ycxuyingchen.github.io/costgrad/)

<details>
<summary>Abstract</summary>

Token-based world models enable fine-grained latent planning, but repeatedly processing large spatial token grids makes action search expensive. We introduce COSTGRAD, a training-free, goal-conditioned selector that ranks spatial tokens by the gradient norm of the planning cost with respect to each input token. By deriving importance from the downstream control objective, COSTGRAD targets tokens that matter for planning rather than merely for prediction. On AdaLN-conditioned predictors at $50\%$ sparsity, COSTGRAD matches or exceeds full-token planning on three of four continuous-control bench...

</details>

<details>
<summary>Share</summary>

```
Sparse Planning in Visual World Models via Cost Gradients

Token-based world models enable fine-grained latent planning, but repeatedly processing large spatial token grids makes action search expensive.

arXiv: https://arxiv.org/abs/2610.10274
Project page: https://ycxuyingchen.github.io/costgrad/

#worldmodels #robotics
```

</details>

---

### [Controllable Crowd Generation through World-Model Planning](https://arxiv.org/abs/2610.09438)

**Authors:** JunGyu Lee, Jisu Shin, Seunghyun Shin, Hae-Gon Jeon

**Published:** 2026-10-07 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09438) | [PDF](https://arxiv.org/pdf/2610.09438) | [Project Page](https://jungyu0413.github.io/Ctrl-CWM)

<details>
<summary>Abstract</summary>

Crowd simulation plays a central role in robot navigation, autonomous driving, and urban planning. For these applications, realistic simulation requires crowds to adapt their behavior to environmental changes and user objectives. However, existing methods that rely on predefined control settings have limited flexibility in accommodating new user-specified objectives. To address this limitation, we propose Ctrl-CWM, a multi-agent Controllable Crowd World Model that integrates crowd generation and run-time control. Our key idea is to adapt the world-model principle of planning using imagined fut...

</details>

<details>
<summary>Share</summary>

```
Controllable Crowd Generation through World-Model Planning

Crowd simulation plays a central role in robot navigation, autonomous driving, and urban planning.

arXiv: https://arxiv.org/abs/2610.09438
Project page: https://jungyu0413.github.io/Ctrl-CWM

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

### [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2610.09763)

**Authors:** Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09763) | [PDF](https://arxiv.org/pdf/2610.09763) | [Project Page](https://mahmoud-selim.github.io/ICDP/)

<details>
<summary>Abstract</summary>

Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous driving, this can be insufficient: a candidate ego trajectory may remain well supported under the marg...

</details>

<details>
<summary>Share</summary>

```
Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving

Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains.

arXiv: https://arxiv.org/abs/2610.09763
Project page: https://mahmoud-selim.github.io/ICDP/

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

### [DSReg: Provably Recovering Individual World Latents without Reconstruction](https://arxiv.org/abs/2610.09457)

**Authors:** Yujia Zheng, David Klindt, Randall Balestriero, Bernhard Schölkopf

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.09457) | [PDF](https://arxiv.org/pdf/2610.09457) | [Project Page](https://dsreg.github.io/)

<details>
<summary>Abstract</summary>

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear transformation, so individual latents remain mixed. We close this gap: individual world latents can be provably recovered with no reconstruction, no decoder, and no labels. The key cond...

</details>

<details>
<summary>Share</summary>

```
DSReg: Provably Recovering Individual World Latents without Reconstruction

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervi...

arXiv: https://arxiv.org/abs/2610.09457
Project page: https://dsreg.github.io/

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

**Published:** 2026-10-08 | **Categories:** cs.AI, cond-mat.mtrl-sci | **Relevance:** ★★☆☆☆

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

### [RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515)

**Authors:** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan et al. (12 authors)

**Published:** 2026-10-07 | **Categories:** cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.10515) | [PDF](https://arxiv.org/pdf/2610.10515)

<details>
<summary>Abstract</summary>

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to pre...

</details>

<details>
<summary>Share</summary>

```
RoboJEPA: Scaling Robotic Latent World Models

Latent world models have shown a remarkable ability to predict future states and to plan in the real world.

arXiv: https://arxiv.org/abs/2610.10515

#worldmodels #robotics
```

</details>

---

### [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](https://arxiv.org/abs/2610.09285)

**Authors:** Mayank Sengupta, Nirmit Desai, Eric Song, Kunal Sawarkar

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.09285) | [PDF](https://arxiv.org/pdf/2610.09285)

<details>
<summary>Abstract</summary>

Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a separate, larger downstream model. To build this model, we choose LeWorldModel (LeWM)as our latent...

</details>

<details>
<summary>Share</summary>

```
LeCuration: A Tiny World Model as a Data Curation Multi-Tool

Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior.

arXiv: https://arxiv.org/abs/2610.09285

#worldmodels #robotics
```

</details>

---

### [Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217)

**Authors:** Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang et al. (7 authors)

**Published:** 2026-10-09 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★☆☆☆

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

### [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](https://arxiv.org/abs/2610.09335)

**Authors:** Yatai Ji, Zhengqiu Zhu, Yong Zhao, Yue Hu, Fanglong Yao et al. (8 authors)

**Published:** 2026-10-07 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.09335) | [PDF](https://arxiv.org/pdf/2610.09335)

<details>
<summary>Abstract</summary>

Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain largely reactive, reasoning over past observations without explicitly predicting future states. World m...

</details>

<details>
<summary>Share</summary>

```
SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models

Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability.

arXiv: https://arxiv.org/abs/2610.09335

#worldmodels #robotics
```

</details>

---

### [Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams](https://arxiv.org/abs/2610.10810)

**Authors:** Pranav Wagh, Yu Fang, Yue Yang, Mingyu Ding

**Published:** 2026-10-07 | **Categories:** cs.RO, cs.LG | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.10810) | [PDF](https://arxiv.org/pdf/2610.10810)

<details>
<summary>Abstract</summary>

Long-horizon robotic manipulation is often built by chaining independently trained skills. Although each skill can be reliable in isolation, performance degrades sharply when skills are chained: each downstream skill must start from the state its predecessor leaves behind rather than from its training distribution. We study this failure mode, Observation-Space Shift (OSS), and ask what causes these skill-seam failures. Using privileged simulator resets, we find that the dominant shift comes from displaced scene state (e.g., an open drawer or secondary objects left behind by earlier skills), no...

</details>

<details>
<summary>Share</summary>

```
Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams

Long-horizon robotic manipulation is often built by chaining independently trained skills.

arXiv: https://arxiv.org/abs/2610.10810

#worldmodels #robotics
```

</details>

---

### [ΔWAM: Distilling Action Tangent Fields into World Action Models](https://arxiv.org/abs/2610.09734)

**Authors:** Ke Wu, Hanwen Huang, Bo Gu, Kaizhao Zhang, Xiangting Meng et al. (9 authors)

**Published:** 2026-10-07 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.09734) | [PDF](https://arxiv.org/pdf/2610.09734)

<details>
<summary>Abstract</summary>

World Action Models (WAM) improve robot policies by augmenting sparse action supervision with dense future prediction. However, much of the predictable future is dominated by appearance and scene persistence rather than action-dependent dynamics. We observe that several recent WAM designs, including optical flow, motion-centric representations, and latent actions, can be understood from a common perspective in which world supervision becomes more efficient as it contains a higher proportion of action-relevant variation. Based on this insight, we introduce Action Tangent Fields, which reformula...

</details>

<details>
<summary>Share</summary>

```
ΔWAM: Distilling Action Tangent Fields into World Action Models

World Action Models (WAM) improve robot policies by augmenting sparse action supervision with dense future prediction.

arXiv: https://arxiv.org/abs/2610.09734

#worldmodels #robotics
```

</details>

---

### [Kuration SDK: Addressing the Virtual2Real Gap via Data Curation](https://arxiv.org/abs/2610.09305)

**Authors:** Nirmit Desai, Eric Song, Mayank Sengupta, Tejal Bedmutha, Siri Reddy et al. (7 authors)

**Published:** 2026-10-07 | **Categories:** cs.LG, cs.AI, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.09305) | [PDF](https://arxiv.org/pdf/2610.09305)

<details>
<summary>Abstract</summary>

Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically-grounded metrics. However, for domain and task-agnostic action-conditioned world model training, existing benchmarks provide a limited signal. By training and evaluating diffusion world models on CounterStrike gameplay data, we confirm that qualitative playability does not correspond with metrics such as FVD, LPIPS, and JEDi. We term this the Virtual2Real gap. We posit that, in lieu of reliable benchmarks, curating r...

</details>

<details>
<summary>Share</summary>

```
Kuration SDK: Addressing the Virtual2Real Gap via Data Curation

Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically-grounded metrics.

arXiv: https://arxiv.org/abs/2610.09305

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

### [AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding](https://arxiv.org/abs/2610.11060)

**Authors:** Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song et al. (9 authors)

**Published:** 2026-10-08 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2610.11060) | [PDF](https://arxiv.org/pdf/2610.11060)

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

#worldmodels #robotics
```

</details>

---
