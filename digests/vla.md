# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-08-20 22:16 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.18035v1)

**Authors:** Zongzheng Zhang, Jijun Wang, Saining Zhang, Shuo Wang, Yiru Wang et al. (11 authors)

**Published:** 2026-08-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2608.18035v1) | [PDF](https://arxiv.org/pdf/2608.18035v1.pdf) | [Project Page](https://zzongzheng0918.github.io/TE-Aware-E2E-AD/)

<details>
<summary>Abstract</summary>

Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end driving research predominantly focuses on dynamic road participants (e.g., vehicles and pedestrians), while the role of traffic elements remains largely unexplored. The community still lacks a systematic study quantifying their impact, largely because public datasets rarely provide structured traffic-...

</details>

---

## Other Recent Papers

### [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](https://arxiv.org/abs/2608.19161v1)

**Authors:** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, Jugad Singh, Sumit Kumar Jha et al. (6 authors)

**Published:** 2026-08-19 | **Categories:** cs.AI, cs.CR

**Links:** [arXiv](https://arxiv.org/abs/2608.19161v1) | [PDF](https://arxiv.org/pdf/2608.19161v1.pdf)

<details>
<summary>Abstract</summary>

Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysi...

</details>

---

### [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066v1)

**Authors:** Yechan Park, HyunJin Kim

**Published:** 2026-08-19 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2608.19066v1) | [PDF](https://arxiv.org/pdf/2608.19066v1.pdf)

<details>
<summary>Abstract</summary>

This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displaceme...

</details>

---

### [The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433v1)

**Authors:** Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda et al. (10 authors)

**Published:** 2026-08-19 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18433v1) | [PDF](https://arxiv.org/pdf/2608.18433v1.pdf)

<details>
<summary>Abstract</summary>

Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs across methods and target robots, and those differences affect practical deployment. We call the gap between reusable models, representations, or ...

</details>

---

### [Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies](https://arxiv.org/abs/2608.18410v1)

**Authors:** Wei Jiang, Wei Wang

**Published:** 2026-08-19 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.18410v1) | [PDF](https://arxiv.org/pdf/2608.18410v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. Sub-token compression provides a complementary alternative by retaining more tokens while reducing their value width. However, directly applying sub-token compression to VLA policies is less effective ...

</details>

---

### [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600v1)

**Authors:** Zhengyan Qian, Rui Yan, Alex Jinpeng Wang, Jinhui Tang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17600v1) | [PDF](https://arxiv.org/pdf/2608.17600v1.pdf)

<details>
<summary>Abstract</summary>

Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear. Existing work covers only a narrow range of cue forms and focuses on final task success, providing only a coarse assessment of cue-following capability. Treating all visual cues as authorized also leaves safety risks of unauthorized following unexplored. To address these gaps, we introduce LIBERO-VI...

</details>

---

### [Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies](https://arxiv.org/abs/2608.17484v1)

**Authors:** Yuhwan Jeong, Kuk-Jin Yoon

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17484v1) | [PDF](https://arxiv.org/pdf/2608.17484v1.pdf)

<details>
<summary>Abstract</summary>

Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations. Yet there is little guidance for deciding which intervention a deployed policy actually needs. Additional sampling is useful only when better behavior already exists within the policy's stochastic rollouts and can be identified, whereas retrieval is most useful when the relevant action prior is not reliably represented by the policy. ...

</details>

---

### [EATR-Stereo: Embodiment-Aware Token Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453v2)

**Authors:** Songwei Wu, Rui Zhao, Fan Yang, Zhongqiang Nie, Zhiduo Jiang et al. (10 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17453v2) | [PDF](https://arxiv.org/pdf/2608.17453v2.pdf)

<details>
<summary>Abstract</summary>

Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...

</details>

---

### [Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](https://arxiv.org/abs/2608.17423v1)

**Authors:** Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping et al. (9 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2608.17423v1) | [PDF](https://arxiv.org/pdf/2608.17423v1.pdf)

<details>
<summary>Abstract</summary>

GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose rollouts all succeed or all fail have zero advantage and are discarded by dynamic sampling. These groups are especially common early in training, when most rollouts fail, wasting much of...

</details>

---

### [MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](https://arxiv.org/abs/2608.17386v1)

**Authors:** Yiyan Peng, Philip Wang, Simon Sinong Zhan, Yiqi Lyu, Zhenyang Ni et al. (14 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17386v1) | [PDF](https://arxiv.org/pdf/2608.17386v1.pdf)

<details>
<summary>Abstract</summary>

Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along ...

</details>

---

### [CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation](https://arxiv.org/abs/2608.17717v1)

**Authors:** Zhen Zhang, Ahmad Hafez, Peng Xie, Yanliang Huang, Wenyuan Wu et al. (6 authors)

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17717v1) | [PDF](https://arxiv.org/pdf/2608.17717v1.pdf)

<details>
<summary>Abstract</summary>

A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction. This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty. We...

</details>

---

### [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](https://arxiv.org/abs/2608.17496v1)

**Authors:** Kaiming Zhong, Tianhua Liu, Yue Wang

**Published:** 2026-08-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2608.17496v1) | [PDF](https://arxiv.org/pdf/2608.17496v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pip...

</details>

---
