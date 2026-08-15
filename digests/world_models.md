# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-08-15 16:22 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552v1)

**Authors:** Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang et al. (12 authors)

**Published:** 2026-08-13 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13552v1) | [PDF](https://arxiv.org/pdf/2608.13552v1.pdf) | [Project Page](https://kxding.github.io/project/PlayWorld/) | [GitHub](https://github.com/kxding/PlayWorld)

<details>
<summary>Abstract</summary>

Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or w...

</details>

---

### [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489v1)

**Authors:**  DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li et al. (10 authors)

**Published:** 2026-08-13 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.13489v1) | [PDF](https://arxiv.org/pdf/2608.13489v1.pdf) | [GitHub](https://github.com/AMAP-ML/DreamX-Phi)

<details>
<summary>Abstract</summary>

We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mat...

</details>

---

### [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](https://arxiv.org/abs/2608.12904v1)

**Authors:** Yunhao Bai, Zhongwei Qiu, Guangyu Guo, Yiming Huang, Tony C. W. Mok et al. (8 authors)

**Published:** 2026-08-13 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.12904v1) | [PDF](https://arxiv.org/pdf/2608.12904v1.pdf) | [GitHub](https://github.com/byhwhite/HounsWorld.git)

<details>
<summary>Abstract</summary>

Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-depe...

</details>

---

## Other Recent Papers

### [Alaya-EVOKE: From Linear-Scaling Supervision to Endless World](https://arxiv.org/abs/2608.13546v1)

**Authors:** Yuanyang Yin, Gongxuan Wang, Yifan Zhan, Chuanhao Li, Kaipeng Zhang et al. (6 authors)

**Published:** 2026-08-13 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13546v1) | [PDF](https://arxiv.org/pdf/2608.13546v1.pdf)

<details>
<summary>Abstract</summary>

Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state...

</details>

---

### [Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology](https://arxiv.org/abs/2608.13518v1)

**Authors:** Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar et al. (7 authors)

**Published:** 2026-08-13 | **Categories:** cs.LG, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13518v1) | [PDF](https://arxiv.org/pdf/2608.13518v1.pdf)

<details>
<summary>Abstract</summary>

Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregular trajectory: clinical observations, medication changes, repeat interventions, and physiological measurements are recorded asynchronously and can change risk assessment over time. We propose an intervention-aware clinical world model that represents each patient with a structured latent state and ev...

</details>

---

### [AlayaWorld: Interactive Long-Horizon World Modeling - Full Technical Report (v1.1)](https://arxiv.org/abs/2608.13492v1)

**Authors:**  AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge et al. (18 authors)

**Published:** 2026-08-13 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.13492v1) | [PDF](https://arxiv.org/pdf/2608.13492v1.pdf)

<details>
<summary>Abstract</summary>

This report presents an improved version of AlayaWorld. While the backbone architecture, chunk-wise autoregressive generation scheme, and training data remain unchanged from the previous release, we substantially revise how conditioning signals are represented and integrated into the model. The new design is guided by a simple principle: conditioning signals should match the generated content as closely as possible in both latent representation and temporal structure. To this end, we make two ma...

</details>

---

### [A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](https://arxiv.org/abs/2608.13456v1)

**Authors:** Avinash Kori, Fabrizio Russo

**Published:** 2026-08-13 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13456v1) | [PDF](https://arxiv.org/pdf/2608.13456v1.pdf)

<details>
<summary>Abstract</summary>

World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entit...

</details>

---

### [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438v1)

**Authors:** Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi

**Published:** 2026-08-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13438v1) | [PDF](https://arxiv.org/pdf/2608.13438v1.pdf)

<details>
<summary>Abstract</summary>

Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon conseque...

</details>

---

### [S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation](https://arxiv.org/abs/2608.13103v1)

**Authors:** Shuzhe Zhang, Xin Zhu, Yinling Qian, Qiong Wang

**Published:** 2026-08-13 | **Categories:** cs.RO, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2608.13103v1) | [PDF](https://arxiv.org/pdf/2608.13103v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon surgical robot manipulation is challenging because task rewards are sparse, while meaningful interaction changes occur at irregular intervals. Existing world-model agents typically imagine at primitive-step resolution, leaving variable-duration task progress implicit. Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions. We propose S2-HWM, a Sparse Event-Structured Hierarc...

</details>

---

### [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049v1)

**Authors:** Dingyi Rong, Yue Shi, Chaofan Ma, Jiezhang Cao, Zongrui Wang et al. (9 authors)

**Published:** 2026-08-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.13049v1) | [PDF](https://arxiv.org/pdf/2608.13049v1.pdf)

<details>
<summary>Abstract</summary>

Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transferring them across embodiments remains challenging due to differences between human hands and robotic end-effectors. Recent advances in video world models offer a promising pathway to synthesize robot-centric manipulation videos from human observations, w...

</details>

---

### [The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use](https://arxiv.org/abs/2608.12959v1)

**Authors:** Joyjeet Singh

**Published:** 2026-08-13 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.12959v1) | [PDF](https://arxiv.org/pdf/2608.12959v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models are judged by how well they predict, so when planning fails at long horizons the natural reading is that the predictor degrades. On a reproduction of LeWorldModel on TwoRoom we show the binding constraint is the planner's objective instead. The predictor is not the limit: its imagined state seventy-five environment steps ahead is still only 0.189 as wrong as assuming the world froze, while the planner never imagines beyond twenty-five. The objective is. Cross-entropy-method p...

</details>

---

### [Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency](https://arxiv.org/abs/2608.12939v1)

**Authors:** Guo An, Zijing Wu, Honghua Dong, Yuhao Yan, Zixuan Gui et al. (10 authors)

**Published:** 2026-08-13 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.12939v1) | [PDF](https://arxiv.org/pdf/2608.12939v1.pdf)

<details>
<summary>Abstract</summary>

Joint-embedding predictive architectures (JEPAs) learn world models that predict in a compact latent space rather than in pixels, reducing the pressure to model nuisance appearance. Yet this provides no guarantee against visual perturbations: they can still alter the encoded representation and affect subsequent action-conditioned predictions. Bisimulation captures this requirement precisely: two observations should be treated as the same state only when their action-conditioned consequences agre...

</details>

---

### [BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving](https://arxiv.org/abs/2608.12854v1)

**Authors:** Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu et al. (11 authors)

**Published:** 2026-08-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.12854v1) | [PDF](https://arxiv.org/pdf/2608.12854v1.pdf)

<details>
<summary>Abstract</summary>

Autonomous driving requires planning under both semantic constraints and predictive dynamics. Existing end-to-end driving approaches, however, typically emphasize only one side of this requirement: Vision-Language-Action (VLA) models exploit VLM priors for semantic reasoning, while World Action Models (WAMs) provide future-aware prediction through generative world modeling. This naturally motivates a unified planner that can leverage both semantic priors and predictive dynamics. However, we find...

</details>

---
