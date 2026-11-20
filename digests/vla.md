# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-20 22:29 UTC

**Papers shown:** 79 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action](https://arxiv.org/abs/2611.26405)

**Authors:** Weile Li, Yunfan Lou, Muqing Shi, Zihao Zhang, Zhenbiao Huang et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26405) | [PDF](https://arxiv.org/pdf/2611.26405) | [Project Page](https://tacinno.github.io)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich manipulation. However, adding tactile input yields inconsistent gains, and some visuo-tactile VLA models rely little on tactile input, because much of the tactile change, such as the gel deformation during gripper closure, is predictable from visual observations and executed actions. To address this problem, we introduce TacInno, which isolates the contact dynamics that vision and executed actions cannot explain, termed tactile innovation, and uses tac...

</details>

<details>
<summary>Share</summary>

```
TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action

Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.26405
Project page: https://tacinno.github.io

#VLA #robotics
```

</details>

---

### [Towards Pose-Robust Few-Shot Vision-Language-Action Models](https://arxiv.org/abs/2611.24360)

**Authors:** Wenhao Li, Zhongyi Han, Yuhao Wei, Liang Han, Yilong Yin et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24360) | [PDF](https://arxiv.org/pdf/2611.24360) | [Project Page](https://peacelwh.github.io/WACO/)

<details>
<summary>Abstract</summary>

Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-docked a few centimetres away makes it reach for the wrong place. We show that both failures are one phenomenon, a change of the camera-to-base extrinsic that the policy has memorised, and that the robot carries everything needed to undo it. We introduce WACO, a world-anchored canonicalization framew...

</details>

<details>
<summary>Share</summary>

```
Towards Pose-Robust Few-Shot Vision-Language-Action Models

Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base...

arXiv: https://arxiv.org/abs/2611.24360
Project page: https://peacelwh.github.io/WACO/

#VLA #robotics
```

</details>

---

### [AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation](https://arxiv.org/abs/2611.24077)

**Authors:** Shiwei Wu, Yuwen Pan, Zhi Li, Yaowen Li, Yan Zhou et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24077) | [PDF](https://arxiv.org/pdf/2611.24077) | [Project Page](https://starsholic.github.io/AeroRSI/) | [Code](https://github.com/starsholic/AeroRSI)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight. Correcting these failures requires repairs, i.e., actions that avoid them at the states the policy itself reaches, which human pilots cannot label at scale and rule-based planners cannot supply reliably. In this paper, we present AeroRSI, a recursive self-improvement framework in which an aerial navigation policy iteratively learns from its own failures. Our key insight is that a failing policy should judge its own repairs by flyin...

</details>

<details>
<summary>Share</summary>

```
AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight.

arXiv: https://arxiv.org/abs/2611.24077
Project page: https://starsholic.github.io/AeroRSI/
Code: https://github.com/starsholic/AeroRSI

#VLA #robotics
```

</details>

---

### [SuperGlance: Driving at a Glance with a Vision-Language Model](https://arxiv.org/abs/2611.19138)

**Authors:** Jieyuan Pei, Xin Yan, Mingwei Xu, Haiyi Zhang, Siyu Zou et al. (12 authors)

**Published:** 2026-11-14 (updated 2026-11-18) | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19138) | [PDF](https://arxiv.org/pdf/2611.19138) | [Project Page](https://guobapei.github.io/SuperGlance/) | [Code](https://github.com/GuobaPei/SuperGlance)

<details>
<summary>Abstract</summary>

Autonomous driving is turning to vision-language-action models (VLAs). They answer and plan by decoding, one step at a time. Each step is another forward pass, so a plan can take over a second of GPU time. Embodied AI often pairs such a slow, reasoning System 2 with a fast System 1 that acts. Human drivers plan at a glance, with System 1. Faster designs usually put System 1 outside the vision-language model (VLM), in a planner without its abilities. Yet before a VLM writes its first token, it has already read the scene into one hidden state. We show that, once trained, this hidden state is eno...

</details>

<details>
<summary>Share</summary>

```
SuperGlance: Driving at a Glance with a Vision-Language Model

Autonomous driving is turning to vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.19138
Project page: https://guobapei.github.io/SuperGlance/
Code: https://github.com/GuobaPei/SuperGlance

#VLA #robotics
```

</details>

---

### [FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving](https://arxiv.org/abs/2611.26242)

**Authors:** Changtao Zhao, Yingxue Guan, Li Wang, Shijie Zhao, Yuhang Zhang et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26242) | [PDF](https://arxiv.org/pdf/2611.26242) | [Code](https://github.com/ADEPT-ORG/FastRoverVLA)

<details>
<summary>Abstract</summary>

Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference. Reusing a prediction reduces this demand while leaving its commands exposed to changes in vehicle motion. FastRoverVLA addresses this mismatch by decoupling visual plan generation from motion-conditioned execution. Its training-free interface maintains decoded plans between visual predictions. A speed-curvature action buffer is aligned with measured motion at each update, integrated into a local trajectory, and advanced by consumin...

</details>

<details>
<summary>Share</summary>

```
FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving

Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference.

arXiv: https://arxiv.org/abs/2611.26242
Code: https://github.com/ADEPT-ORG/FastRoverVLA

#VLA #robotics
```

</details>

---

### [$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling](https://arxiv.org/abs/2611.24940)

**Authors:** Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong et al. (15 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24940) | [PDF](https://arxiv.org/pdf/2611.24940) | [Project Page](https://junjieye.com/Z-sight/)

<details>
<summary>Abstract</summary>

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight instead predicts the future directly in the visual token space in which its VLM perceives the present. C...

</details>

<details>
<summary>Share</summary>

```
$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling.

arXiv: https://arxiv.org/abs/2611.24940
Project page: https://junjieye.com/Z-sight/

#VLA #robotics
```

</details>

---

### [Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience](https://arxiv.org/abs/2611.26420)

**Authors:** EngineAI

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26420) | [PDF](https://arxiv.org/pdf/2611.26420) | [Project Page](https://engineai-robotics.github.io/Awaken-HI)

<details>
<summary>Abstract</summary>

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with synchronized whole-body human motion and covers more than 100 skills. Building on this, we also introduce Awaken-HI (Humanoid Intelligence), a vision-language-action model for humanoid loco-manipulation that jointly predicts origi...

</details>

<details>
<summary>Share</summary>

```
Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces.

arXiv: https://arxiv.org/abs/2611.26420
Project page: https://engineai-robotics.github.io/Awaken-HI

#VLA #robotics
```

</details>

---

### [PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.26596)

**Authors:** Kai Lu, Chenyang Ma, Ioannis Havoutis

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.26596) | [PDF](https://arxiv.org/pdf/2611.26596) | [Project Page](https://kl-research.github.io/pgx)

<details>
<summary>Abstract</summary>

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using p...

</details>

<details>
<summary>Share</summary>

```
PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are ti...

arXiv: https://arxiv.org/abs/2611.26596
Project page: https://kl-research.github.io/pgx

#VLA #robotics
```

</details>

---

### [PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity](https://arxiv.org/abs/2611.26565)

**Authors:** Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi et al. (11 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26565) | [PDF](https://arxiv.org/pdf/2611.26565)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. As a result, it remains unclear whether current policies truly understand physics or merely interpolate from their training data. We address this gap through the lens of dynamic extrinsic dexterity and introduce PhyDEX, a throwing benchmark in which a robot must infer an object's mass, center of mass, and frict...

</details>

<details>
<summary>Share</summary>

```
PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity

Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the...

arXiv: https://arxiv.org/abs/2611.26565

#VLA #robotics
```

</details>

---

### [Teaching Vision-Language-Action Models to Stop Safely](https://arxiv.org/abs/2611.26239)

**Authors:** Zheyuan Liu, Chuhan Wang, Jinduo Guo, Yue Huang, Xiangchi Yuan et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26239) | [PDF](https://arxiv.org/pdf/2611.26239)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to perform diverse tasks from visual observations and language instructions. While prior work has explored task suppression and refusal, stopping prohibited behavior once execution is underway and controlling the resulting physical response remain challenging. Our evaluation reveals that policies which suppress a task from its initial state can still complete it when taking over partway through execution. Even when the task remains unfinished, the robot may drop a held object, making non-completion an incomplete measure of safety. To address th...

</details>

<details>
<summary>Share</summary>

```
Teaching Vision-Language-Action Models to Stop Safely

Vision-language-action (VLA) models enable robots to perform diverse tasks from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.26239

#VLA #robotics
```

</details>

---

### [CoachSI: Self-Improvement of Robot Policies with a Language Coach](https://arxiv.org/abs/2611.25529)

**Authors:** Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25529) | [PDF](https://arxiv.org/pdf/2611.25529) | [Project Page](https://tlxhlll.github.io/CoachSI/)

<details>
<summary>Abstract</summary>

Generalist robot policies execute atomic skills reliably but fail when the same skills are composed into long-horizon tasks. Self-improvement from the policy's own experience does not close this gap: experience collected by the policy alone stays within its own distribution and reproduces what it can already do. We show that what the policy lacks is not a skill but the next step. We present CoachSI, a self-improvement method in which a frozen, off-the-shelf vision-language model (VLM) coaches the policy in language: it watches the robot and names the next step in the format of the policy's ato...

</details>

<details>
<summary>Share</summary>

```
CoachSI: Self-Improvement of Robot Policies with a Language Coach

Generalist robot policies execute atomic skills reliably but fail when the same skills are composed into long-horizon tasks.

arXiv: https://arxiv.org/abs/2611.25529
Project page: https://tlxhlll.github.io/CoachSI/

#VLA #robotics
```

</details>

---

### [Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation](https://arxiv.org/abs/2611.24247)

**Authors:** Haotian Xu, Yue Hu, Zhengqiu Zhu, Tuo Feng, Wenguan Wang et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.24247) | [PDF](https://arxiv.org/pdf/2611.24247)

<details>
<summary>Abstract</summary>

Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight. A key challenge is linking changing egocentric perception with spatial evidence anchored to stable locations for long-range navigation. We propose CityNav-VLA, a dual-frame vision-language-action model for urban navigation integrating dynamic egocentric context with persistent allocentric spatial memory. The UAV incrementally accumulates visual observations on a fixed north-up map initialized with geographic and landmark priors, preserving evidence acr...

</details>

<details>
<summary>Share</summary>

```
Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation

Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight.

arXiv: https://arxiv.org/abs/2611.24247

#VLA #robotics
```

</details>

---

### [CoRA-VTLA: Contact-Guided Attention and Queryable Response Memory for Tactile Post-Training](https://arxiv.org/abs/2611.23963)

**Authors:** Chengye Song, Rui Song, Shengqi Wang, Jiawei Zhang, Hongzhou Wang et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.23963) | [PDF](https://arxiv.org/pdf/2611.23963) | [Project Page](https://cora-vtla.github.io/)

<details>
<summary>Abstract</summary>

In precision manipulation, small errors in alignment or force can cause jamming or deformation, making contact feedback essential for adapting pretrained vision-language-action (VLA) models to these tasks. A single tactile observation leaves the response to recent actions ambiguous. Direct tactile fusion during post-training can also disperse the action expert's visual attention and reduce the share it allocates to contact regions. To address these challenges, CoRA-VTLA augments pretrained VLAs with lightweight tactile modules. A queryable action-response memory retrieves recent contact respon...

</details>

<details>
<summary>Share</summary>

```
CoRA-VTLA: Contact-Guided Attention and Queryable Response Memory for Tactile Post-Training

In precision manipulation, small errors in alignment or force can cause jamming or deformation, making contact feedback essential for adapting pretrained vision-language-action (VLA) models to these tasks.

arXiv: https://arxiv.org/abs/2611.23963
Project page: https://cora-vtla.github.io/

#VLA #robotics
```

</details>

---

### [RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models](https://arxiv.org/abs/2611.23843)

**Authors:** Apoorva Vashisth, Manav Kulshrestha, Damon Conover, Zachary Kingston, Aniket Bera

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23843) | [PDF](https://arxiv.org/pdf/2611.23843)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipulations. Instead of burdening the VLA policies with long-horizon reasoning, memory, action generation, progress tracking, and error recovery, we argue for leveraging their short-horizon manipulation capabilities within an execution-aware framework. To this end, we introduce \textnormal{\textbf{RePlan-VLA}}, a VLA-agnostic framework that translates a VLA's short-horizon capabilitie...

</details>

<details>
<summary>Share</summary>

```
RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipu...

arXiv: https://arxiv.org/abs/2611.23843

#VLA #robotics
```

</details>

---

### [ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2611.23714)

**Authors:** Keke Tang, Guolin Qiu, Tianyu Hao, Daizong Liu, Yikai Zhang et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23714) | [PDF](https://arxiv.org/pdf/2611.23714)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have become a powerful paradigm for robotic manipulation and show strong promise for real-world deployment, making adversarial robustness critical for reliable robot operation. Existing adversarial attacks on VLA-controlled robots mainly optimize prediction-level discrepancies or rollout-level deviations to disrupt manipulation. However, they rarely account for the fact that VLA-predicted commands are not executed directly, but must be realized through downstream control and robot embodiment. In this paper, we propose ExecGap, an adversarial patch attack fra...

</details>

<details>
<summary>Share</summary>

```
ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models

Vision-Language-Action (VLA) models have become a powerful paradigm for robotic manipulation and show strong promise for real-world deployment, making adversarial robustness critical for reliable robot operation.

arXiv: https://arxiv.org/abs/2611.23714

#VLA #robotics
```

</details>

---

### [Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need](https://arxiv.org/abs/2611.23676)

**Authors:** Artur Kuramshin, Charlotte Cloutier, Michael Przystupa, Kirsty Ellis, Mohammad S. Akhter et al. (6 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23676) | [PDF](https://arxiv.org/pdf/2611.23676)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best adapt VLAs to dexterous hands by pairing supervised fine-tuning (SFT) with diffusion-steering reinforcement learning (DSRL). Using $π_{0.5}$ and a LEAP hand, we evaluate five fine-tuning recipes across two simulation tasks using only a handfu...

</details>

<details>
<summary>Share</summary>

```
Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need

Vision-Language-Action models have demonstrated strong manipulation capabilities.

arXiv: https://arxiv.org/abs/2611.23676

#VLA #robotics
```

</details>

---

### [InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](https://arxiv.org/abs/2611.22584)

**Authors:** Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen et al. (8 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.22584) | [PDF](https://arxiv.org/pdf/2611.22584) | [Project Page](https://lingwupro.github.io/InteractVLA/)

<details>
<summary>Abstract</summary>

Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agents. In the forward direction, test-time geometric guidance translates an agent-specified end-effecto...

</details>

<details>
<summary>Share</summary>

```
InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation

Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agen...

arXiv: https://arxiv.org/abs/2611.22584
Project page: https://lingwupro.github.io/InteractVLA/

#VLA #robotics
```

</details>

---

### [Right Goal, Wrong Body: Re-grounding Frozen VLAs under Actuation Shift](https://arxiv.org/abs/2611.20244)

**Authors:** Umer Siddique, Peilang Li, Yongcan Cao

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.20244) | [PDF](https://arxiv.org/pdf/2611.20244) | [Project Page](https://umersiddique94.github.io/ReGround/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are capable of producing desired robotic behaviors in ideal settings. However, they often fail when the robot's actuation changes at deployment. For example, remounting, mechanical wear, or command latency changes can lead to failed tasks and unsafe behaviors. To address the inevitable actuation shift, we propose ReGround, an inference-time method that keeps the VLA frozen and re-grounds its intended motion. ReGround learns the deployed robot's dynamics from task-agnostic motor babbling, and then tracks the policy's intended motion while staying close to the...

</details>

<details>
<summary>Share</summary>

```
Right Goal, Wrong Body: Re-grounding Frozen VLAs under Actuation Shift

Vision-language-action (VLA) models are capable of producing desired robotic behaviors in ideal settings.

arXiv: https://arxiv.org/abs/2611.20244
Project page: https://umersiddique94.github.io/ReGround/

#VLA #robotics
```

</details>

---

### [ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents](https://arxiv.org/abs/2611.18176)

**Authors:** Yundi Cai, Zihan Wang, Chenxi Han, Yi Cheng, Houde Liu et al. (6 authors)

**Published:** 2026-11-13 (updated 2026-11-16) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.18176) | [PDF](https://arxiv.org/pdf/2611.18176) | [Code](https://github.com/ZERITH-ZLab/ESI)

<details>
<summary>Abstract</summary>

Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior. The VLA may generate actions that diverge from the LLM's intended subtask and, upon regaining control after a correction, undo the promising state restored by the LLM. We introduce ESI (Embodied Self-Improvement), an automated flywheel that uses environmental interaction to align reasoning and action. ESI treats the modular agent as the unit of post-training, repeatedly refining the...

</details>

<details>
<summary>Share</summary>

```
ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents

Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior.

arXiv: https://arxiv.org/abs/2611.18176
Code: https://github.com/ZERITH-ZLab/ESI

#VLA #robotics
```

</details>

---

### [Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2611.26438)

**Authors:** Zixuan Liu, Hashem Haghbayan, Zizhan Zheng, Siavash Khajavi

**Published:** 2026-11-19 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26438) | [PDF](https://arxiv.org/pdf/2611.26438)

<details>
<summary>Abstract</summary>

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters. However, even when retrieved demonstrations are relevant to the current task, the VLA may fail to effectively utilize the retrieved information, ultimately leading to task failure. To address this challenge, we propose R2-VLA, a risk-controlled retrieval-augmented VLA framework that enables reliable test-time adaptation by satisfying a user-specified task success rate requirement with minimal expert assistance...

</details>

<details>
<summary>Share</summary>

```
Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters.

arXiv: https://arxiv.org/abs/2611.26438

#VLA #robotics
```

</details>

---

### [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](https://arxiv.org/abs/2611.25461)

**Authors:** Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.25461) | [PDF](https://arxiv.org/pdf/2611.25461) | [Code](https://github.com/LigphiDonk/ActMem)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual...

</details>

<details>
<summary>Share</summary>

```
ActMem: From Latent Memory Reasoning to Grounded Robotic Action

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.

arXiv: https://arxiv.org/abs/2611.25461
Code: https://github.com/LigphiDonk/ActMem

#VLA #robotics
```

</details>

---

### [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444)

**Authors:** Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang et al. (43 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26444) | [PDF](https://arxiv.org/pdf/2611.26444)

<details>
<summary>Abstract</summary>

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a failure comes from reasoning, execution, or their composition. We introduce Mind2Act World, a diagnosti...

</details>

<details>
<summary>Share</summary>

```
Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and tim...

arXiv: https://arxiv.org/abs/2611.26444

#VLA #robotics
```

</details>

---

### [One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency](https://arxiv.org/abs/2611.26161)

**Authors:** Jinxi Liu, Ruifeng Zhai, Hao Liu, Guangrun Wang

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26161) | [PDF](https://arxiv.org/pdf/2611.26161)

<details>
<summary>Abstract</summary>

Multi-view vision-language-action (VLA) models still face challenges in spatial generalization, particularly under changes in camera viewpoints and robot initial states. These models typically receive action supervision only in the robot base frame, requiring them to implicitly learn the spatial correspondence between observations from each view and base-frame actions. We propose One View, One Action (OVOA-VLA), which learns to predict actions in each view's camera frame, allowing the same physical motion to provide diverse, observation-aligned supervision across views. OVOA-VLA jointly trains...

</details>

<details>
<summary>Share</summary>

```
One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency

Multi-view vision-language-action (VLA) models still face challenges in spatial generalization, particularly under changes in camera viewpoints and robot initial states.

arXiv: https://arxiv.org/abs/2611.26161

#VLA #robotics
```

</details>

---

### [A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery](https://arxiv.org/abs/2611.25656)

**Authors:** Chenyuan Zhou, Chaoyi Huang, Zibo Wang, Zhiyuan Li, Yong-Lu Li

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25656) | [PDF](https://arxiv.org/pdf/2611.25656)

<details>
<summary>Abstract</summary>

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with a VLA policy. It treats tool affordances as hypotheses the agent can construct, test, and revise. Gi...

</details>

<details>
<summary>Share</summary>

```
A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy a...

arXiv: https://arxiv.org/abs/2611.25656

#VLA #robotics
```

</details>

---

### [Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation](https://arxiv.org/abs/2611.25400)

**Authors:** Chengyang Dong, Ze Chen, Kai Ye, Chutian Wang, Heng Xu et al. (14 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25400) | [PDF](https://arxiv.org/pdf/2611.25400)

<details>
<summary>Abstract</summary>

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining. However, backpropagation-based adaptation incurs heavy memory overhead on resource-constrained robots, whereas zeroth-order (ZO) methods suffer from high estimation variance under limited perturbation budgets. We observe that while ZO estimation enables low-memory adaptation with rapid initial gains, it often stalls or degrades over long-horizon updates due to noisy gradient estimates. To address these limitations, we propose Dune, a zeroth-or...

</details>

<details>
<summary>Share</summary>

```
Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining.

arXiv: https://arxiv.org/abs/2611.25400

#VLA #robotics
```

</details>

---

### [3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation](https://arxiv.org/abs/2611.23961)

**Authors:** Xin Zhang, Shiqi Zhang, Siyuan Cao, Juncheng Cai, Yedong Shen et al. (12 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23961) | [PDF](https://arxiv.org/pdf/2611.23961)

<details>
<summary>Abstract</summary>

In contact-rich dexterous manipulation, occlusion by the fingers and interacting objects obscures local geometry, preventing visual observations from fully capturing contact locations. Visually similar scenes may also differ subtly in the relative positions of interacting objects, leading to different contact states. We propose 3DTouch, a tactile-geometric conditioning approach for vision-language-action (VLA) models. 3DTouch constructs a shared 3D visuo-tactile representation by expressing RGB-D scene points and dense five-finger tactile measurements in the robot-base frame, preserving each t...

</details>

<details>
<summary>Share</summary>

```
3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation

In contact-rich dexterous manipulation, occlusion by the fingers and interacting objects obscures local geometry, preventing visual observations from fully capturing contact locations.

arXiv: https://arxiv.org/abs/2611.23961

#VLA #robotics
```

</details>

---

### [GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation](https://arxiv.org/abs/2611.23926)

**Authors:** Tianqi Gong, Haochen Niu, Yusheng Zhao, Lantao Zhang, Haoyu Liu et al. (7 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.23926) | [PDF](https://arxiv.org/pdf/2611.23926)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generate local actions from visual observations, language, and robot state, but long-horizon manipulation requires the global task intent to remain grounded in the currently executable context. We propose GTI (Grounding Task Intent), which uses the current observation and execution history to localize the active subtask and its execution phase. For the same local subtask, GTI generates two phase-dependent visual targets: an interaction/contact state and a local completion state. The local language instruction and the corresponding phase-specific visual targe...

</details>

<details>
<summary>Share</summary>

```
GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation

Vision-language-action (VLA) models generate local actions from visual observations, language, and robot state, but long-horizon manipulation requires the global task intent to remain grounded in the currently executa...

arXiv: https://arxiv.org/abs/2611.23926

#VLA #robotics
```

</details>

---

### [RoboMorpher: Scaling Robot Morphology Representations for Cross-Embodiment Action Prediction](https://arxiv.org/abs/2611.24816)

**Authors:** Wenwei Lin, Yan Qin, Weiliang Deng, Zixuan Li, Kaixuan Wang et al. (15 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.24816) | [PDF](https://arxiv.org/pdf/2611.24816) | [Project Page](https://robomorpher.github.io/)

<details>
<summary>Abstract</summary>

Learning shared action representations is central to cross-embodiment manipulation. However, identical joint values can produce different spatial configurations across robots, limiting representations learned from joint values alone. We introduce RoboMorpher, a morphology-conditioned action tokenizer that jointly reconstructs joint angles and link poses to associate control coordinates with their kinematic effects. MorphGen supplies scalable kinematic supervision by generating serial-arm descriptions from survey-derived geometric priors. We pretrain RoboMorpher on 40 million morphology-state p...

</details>

<details>
<summary>Share</summary>

```
RoboMorpher: Scaling Robot Morphology Representations for Cross-Embodiment Action Prediction

Learning shared action representations is central to cross-embodiment manipulation.

arXiv: https://arxiv.org/abs/2611.24816
Project page: https://robomorpher.github.io/

#VLA #robotics
```

</details>

---

### [VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2611.22666)

**Authors:** Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22666) | [PDF](https://arxiv.org/pdf/2611.22666)

<details>
<summary>Abstract</summary>

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time. Speculative decoding makes this possible: a lightweight draft model proposes several tokens at once, and the VLA verifies them in a single pass, accepting only those that match its own predictions, so decoding remains lossless. The speedup, however, is limited in robot control, where many different tokens encode nearly the same motion and a draft close to the correct action is still rejected. To address this, our approach, VSpark, is built upon three design choices: (...

</details>

<details>
<summary>Share</summary>

```
VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time.

arXiv: https://arxiv.org/abs/2611.22666

#VLA #robotics
```

</details>

---

### [VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2611.22453)

**Authors:** Arusa Kanwal, Pablo Valle, Paola Roggero, Miren Illarramendi, Shaukat Ali et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.SE | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22453) | [PDF](https://arxiv.org/pdf/2611.22453)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action generation to control robots. Testing these systems produces trajectories and task outcomes, but existing approaches provide limited guidance on using these recorded trajectories to assess subsequent executions or inform policy repair. We conjecture that, for a given policy and task, traversing certain workspace regions is associated with a higher likelihood of failure. To investigate this conjecture, we propose VoxelSBFL, a black-box adaptation of Spectrum-Based Fault Localization (SBFL) in whi...

</details>

<details>
<summary>Share</summary>

```
VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models

Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action generation to control robots.

arXiv: https://arxiv.org/abs/2611.22453

#VLA #robotics
```

</details>

---

### [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://arxiv.org/abs/2611.21607)

**Authors:** Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li et al. (12 authors)

**Published:** 2026-11-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.21607) | [PDF](https://arxiv.org/pdf/2611.21607)

<details>
<summary>Abstract</summary>

Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for robot learning. We introduce ScaleVLA, which connects a 552B DeepSeek-V4.1-Flash backbone to a trainable action DiT, and systematically compare VLMs from 2B to 552B under a shared trai...

</details>

<details>
<summary>Share</summary>

```
ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action.

arXiv: https://arxiv.org/abs/2611.21607

#VLA #robotics
```

</details>

---

### [Stochastic Self-Distillation for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2611.20460)

**Authors:** Jingru Guo, Alessandra Russo, Joey Bose, Christos Ziakas

**Published:** 2026-11-16 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20460) | [PDF](https://arxiv.org/pdf/2611.20460)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models achieve strong performance in robotics through imitation learning, yet fine-tuning them with on-policy reinforcement learning (RL) is limited. In group-based RL methods like Group Relative Policy Optimization (GRPO), every rollout step requires multi-step ODE integration, and the sampler's limited stochasticity leads to rollout groups with low variance. We propose VLA-SSD, which addresses both high inference latency and limited stochasticity. In particular, our method self-distills a pretrained flow-matching action head into a stochastic one-step...

</details>

<details>
<summary>Share</summary>

```
Stochastic Self-Distillation for Flow-Based Vision-Language-Action Models

Flow-based vision-language-action (VLA) models achieve strong performance in robotics through imitation learning, yet fine-tuning them with on-policy reinforcement learning (RL) is limited.

arXiv: https://arxiv.org/abs/2611.20460

#VLA #robotics
```

</details>

---

### [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](https://arxiv.org/abs/2611.20011)

**Authors:** Nikos Theodoridis, Reenu Mohandas, Sushil Sharma, Ciarán Hogan, Ganesh Sistu et al. (8 authors)

**Published:** 2026-11-15 (updated 2026-11-17) | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20011) | [PDF](https://arxiv.org/pdf/2611.20011)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios. Although these models achieve state-of-the-art results on autonomous driving benchmarks, most existing benchmarks are dominated by nominal scenarios and therefore cannot test this promise. To test one such long-tail capability that is critical for safety, we introduce ReactBench-AD, a benchmark that measures how driving models react to objects that appear in the ego vehicle's path. Built on real NAVSIM and PhysicalAI-Autonomous...

</details>

<details>
<summary>Share</summary>

```
ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?

Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios.

arXiv: https://arxiv.org/abs/2611.20011

#VLA #robotics
```

</details>

---

### [PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models](https://arxiv.org/abs/2611.20010)

**Authors:** Hanbo Zhang, Lianlei Shan, Liuhaichen Yang, Zezhi Tang

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20010) | [PDF](https://arxiv.org/pdf/2611.20010)

<details>
<summary>Abstract</summary>

Test-time scaling improves vision-language-action (VLA) policies by drawing several action candidates and executing the best one. We find that its returns diminish quickly when the candidates are resampled from one decoder: they differ by noise rather than by plan, and for each of three resampling sources, going from four to eight candidates adds only 0.06-0.07 to the average number of completed tasks on CALVIN. We introduce PlanDiv, an action head that makes the candidates differ by plan: a lightweight planner proposes K latent plan hypotheses, a shared masked-diffusion executor decodes one a...

</details>

<details>
<summary>Share</summary>

```
PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models

Test-time scaling improves vision-language-action (VLA) policies by drawing several action candidates and executing the best one.

arXiv: https://arxiv.org/abs/2611.20010

#VLA #robotics
```

</details>

---

### [Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations](https://arxiv.org/abs/2611.19196)

**Authors:** Chen Liu, Nikolaus Correll

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.19196) | [PDF](https://arxiv.org/pdf/2611.19196) | [Project Page](https://robonana.github.io/ego2sim2humanoid/)

<details>
<summary>Abstract</summary>

Imitation learning for visuomotor policies typically relies on teleoperated robot demonstrations, which are costly because every episode requires a trained operator controlling a physical robot in real time through teleoperation interfaces and wearable body-tracking hardware. Egocentric glasses capture human demonstrations without a robot or handheld grippers, yet they track only the head and in-view human hands, and directly copying human motion to a robot with different stature, arm reach and hand morphology fails to produce feasible contacts. \method{} converts egocentric glasses recordings...

</details>

<details>
<summary>Share</summary>

```
Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations

Imitation learning for visuomotor policies typically relies on teleoperated robot demonstrations, which are costly because every episode requires a trained operator controlling a physical robot in real time through te...

arXiv: https://arxiv.org/abs/2611.19196
Project page: https://robonana.github.io/ego2sim2humanoid/

#VLA #robotics
```

</details>

---

### [Wireless Edge-Assisted Adaptive Latent Reasoning for Vision-Language-Action Models in Physical AI](https://arxiv.org/abs/2611.19131)

**Authors:** Fatih Temiz, Melike Erol-Kantarci

**Published:** 2026-11-14 | **Categories:** cs.RO, cs.NI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19131) | [PDF](https://arxiv.org/pdf/2611.19131)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable embodied artificial intelligence (AI) by translating visual observations and language instructions into robotic actions. Emerging use cases in physical AI are expected to drive the need for efficient inference and communication, as the computational demands of the VLA models pose challenges for real-time control with limited onboard resources. Test-time scaling through latent reasoning allows these models to refine hidden representations without generating explicit chain-of-thought (CoT) tokens, but introduces a trade-off between task success, inferen...

</details>

<details>
<summary>Share</summary>

```
Wireless Edge-Assisted Adaptive Latent Reasoning for Vision-Language-Action Models in Physical AI

Vision-language-action (VLA) models enable embodied artificial intelligence (AI) by translating visual observations and language instructions into robotic actions.

arXiv: https://arxiv.org/abs/2611.19131

#VLA #robotics
```

</details>

---

### [Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment](https://arxiv.org/abs/2611.18372)

**Authors:** Suvarna Kadam, Soran Parsa

**Published:** 2026-11-13 (updated 2026-11-19) | **Categories:** cs.RO, cs.AI, cs.ET | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.18372) | [PDF](https://arxiv.org/pdf/2611.18372)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control. In under four years the field has grown from RT-2, the first VLA, to open models that fine-tune on a single consumer GPU and proprietary generalists that clean unseen homes. VLA research joins robotics, computer vision and language modelling, so this survey is written for researchers and practitioners from each of these fields. It reviews 89 works from December 2022 to October 2026, mainly on manipulation and navigation, plus humanoid...

</details>

<details>
<summary>Share</summary>

```
Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control.

arXiv: https://arxiv.org/abs/2611.18372

#VLA #robotics
```

</details>

---

### [DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies](https://arxiv.org/abs/2611.25695)

**Authors:** Jun Xia, Shangwen Wang, Jun Ma, Ruichao Ren, Zhouyang Jia et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25695) | [PDF](https://arxiv.org/pdf/2611.25695)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks. However, optimized patterns can stand out from their surroundings, making an attack easier to notice and its carrier more likely to be inspected or removed. To address this limitation, our key insight is to search the structured image distribution of a diffusion model for natural-looking textures while using closed-loop feedback to identify task-disruptive candidates. Based on this idea, we propose DMT-Attack, a gradient-free gray-box attack that generate...

</details>

<details>
<summary>Share</summary>

```
DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies

Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks.

arXiv: https://arxiv.org/abs/2611.25695

#VLA #robotics
```

</details>

---

### [RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models](https://arxiv.org/abs/2611.22736)

**Authors:** Shaozhen Liu, Zhiwei Li, Jiayang Sun, Shuangjun Du, Yi Zhong et al. (9 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22736) | [PDF](https://arxiv.org/pdf/2611.22736)

<details>
<summary>Abstract</summary>

Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retraining when manipulation objects change. We introduce RefCloth, a framework that optimizes one persistent adversarial tablecloth on a frozen source policy and deploys it zero-shot across unseen tasks and target models without modifying task objects or cameras. Throughout manipulation, static third-person and moving wrist views observe this shared world-bound texture under evolving oc...

</details>

<details>
<summary>Share</summary>

```
RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models

Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retrain...

arXiv: https://arxiv.org/abs/2611.22736

#VLA #robotics
```

</details>

---

### [POKE: Probe Offline, Keep Efficiently for Vision-Language-Action Models](https://arxiv.org/abs/2611.21033)

**Authors:** Jaehyuk Lee, Yeajin Lee, Suhyun Bae, Donghun Lee

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.21033) | [PDF](https://arxiv.org/pdf/2611.21033)

<details>
<summary>Abstract</summary>

Visual token pruning reduces the inference cost of Vision-Language-Action (VLA) models, but attention-based scores do not directly measure a token's effect on the predicted action. We define action sensitivity as the magnitude of the first-order action change when a token is replaced by its camera's mean token and estimate it for all tokens with a single backward pass. Computing it online is costly: scoring on the full (unpruned) graph needs an extra forward pass at every control step. Scoring on the pruned forward pass is cheaper but causes scoring-graph lock-in: removed tokens lose their dir...

</details>

<details>
<summary>Share</summary>

```
POKE: Probe Offline, Keep Efficiently for Vision-Language-Action Models

Visual token pruning reduces the inference cost of Vision-Language-Action (VLA) models, but attention-based scores do not directly measure a token's effect on the predicted action.

arXiv: https://arxiv.org/abs/2611.21033

#VLA #robotics
```

</details>

---

### [Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules](https://arxiv.org/abs/2611.20648)

**Authors:** Barkin Dagda, Vinal Asodia, Iman Sharifi, Peng Wei, Saber Fallah

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20648) | [PDF](https://arxiv.org/pdf/2611.20648)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models offer a unified approach to perception, reasoning, and control for autonomous driving, but accurate action prediction alone does not establish compliance with traffic regulations. This paper presents a rule-guided VLA framework that incorporates symbolic traffic-rule feedback into policy optimisation. The framework combines supervised fine-tuning on expert demonstrations with reinforcement learning (RL) refinement using a reward that encourages encoded-rule compliance while penalising deviations from expert actions. Selected provisions of the United Kingdom...

</details>

<details>
<summary>Share</summary>

```
Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules

Vision-language-action (VLA) models offer a unified approach to perception, reasoning, and control for autonomous driving, but accurate action prediction alone does not establish compliance with traffic regulations.

arXiv: https://arxiv.org/abs/2611.20648

#VLA #robotics
```

</details>

---

### [When Backdoors Can Be Switched Off: Suppression-Aware Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2611.19774)

**Authors:** Nur Afsa Syeda, Mohamed Elmahallawy

**Published:** 2026-11-15 | **Categories:** cs.CV, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19774) | [PDF](https://arxiv.org/pdf/2611.19774)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models map visual observations, robot states, and natural-language instructions to robotic actions, but their multimodal interfaces introduce new security risks. Existing VLA backdoor attacks primarily study trigger-based activation and stealthy action manipulation, leaving conditional suppression of malicious behavior underexplored. We investigate suppression-aware backdoors, which combine conjunctive trigger activation with instruction-conditioned suppression. We instantiate this design through three variants: Cross-Modal Trigger, combining robot-state and spatia...

</details>

<details>
<summary>Share</summary>

```
When Backdoors Can Be Switched Off: Suppression-Aware Backdoor Attacks on Vision-Language-Action Models

Vision-Language-Action (VLA) models map visual observations, robot states, and natural-language instructions to robotic actions, but their multimodal interfaces introduce new security risks.

arXiv: https://arxiv.org/abs/2611.19774

#VLA #robotics
```

</details>

---

### [Bring Back Language to Actions: Restoring VLM capabilities in VLA Models via Parameter Merging](https://arxiv.org/abs/2611.18891)

**Authors:** Mohamed Salim Aissi, Olivier Sigaud, Laure Soulier, Nicolas Thome

**Published:** 2026-11-13 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.18891) | [PDF](https://arxiv.org/pdf/2611.18891)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) are obtained by fine-tuning pre-trained Vision-Language Models (VLMs) on robot demonstration data, enabling action prediction from visual observations and language instructions. However, this fine-tuning induces catastrophic forgetting, substantially degrading the semantic and visual grounding capabilities of the original VLM. We address this by merging the parameters of a VLM and its VLA derivative without retraining either model. Concretely, we extract the task vector (the difference between VLA and VLM weights) and decompose it via Singular Value Decompo...

</details>

<details>
<summary>Share</summary>

```
Bring Back Language to Actions: Restoring VLM capabilities in VLA Models via Parameter Merging

Vision-Language-Action models (VLAs) are obtained by fine-tuning pre-trained Vision-Language Models (VLMs) on robot demonstration data, enabling action prediction from visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.18891

#VLA #robotics
```

</details>

---

### [Beyond the Sink Interpretation: Radial Attention in Flow-Based VLA Policies](https://arxiv.org/abs/2611.26385)

**Authors:** Yuxi Zheng, Yueqian Lin, Yudong Liu, Zijia Tang, Junyu Pan et al. (8 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.26385) | [PDF](https://arxiv.org/pdf/2611.26385)

<details>
<summary>Abstract</summary>

Prior work calls the high attention on the first and last action tokens of a flow-based VLA policy a radial action sink, and uses these tokens to set the execution horizon. In language models, a sink is a token with high incoming attention, a small value, and little effect on the output. We test whether that profile holds, not the horizon rule, in one $π_{0.5}$ checkpoint on five RoboCasa tasks. The two endpoints receive 5.4% of action-key mass, 1.4 percentage points above their uniform share, and rotary positional encoding produces this excess: directly in shallow layers and through upstream...

</details>

<details>
<summary>Share</summary>

```
Beyond the Sink Interpretation: Radial Attention in Flow-Based VLA Policies

Prior work calls the high attention on the first and last action tokens of a flow-based VLA policy a radial action sink, and uses these tokens to set the execution horizon.

arXiv: https://arxiv.org/abs/2611.26385

#VLA #robotics
```

</details>

---

### [CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control](https://arxiv.org/abs/2611.25667)

**Authors:** Xu Pan, Chubin Zhang, Xingrui Yu, Runmin Lan, Zihao Wang et al. (9 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.25667) | [PDF](https://arxiv.org/pdf/2611.25667)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies must react while visual inference is still running. Overlapping computation and execution reduces waiting, yet leaves perceptual memory stale and successive action chunks disconnected. We present CauSyncVLA, an asynchronous dual-system controller that aligns perceptual-memory prediction and trajectory correction with actual robot execution. Rather than forecasting pixels or physical states, a Causal Latent World Model predicts current perceptual memory from delayed visual anchors and executed state-action history, supervised through action-sensitive distil...

</details>

<details>
<summary>Share</summary>

```
CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control

Vision-Language-Action (VLA) policies must react while visual inference is still running.

arXiv: https://arxiv.org/abs/2611.25667

#VLA #robotics
```

</details>

---

### [FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash](https://arxiv.org/abs/2611.25580)

**Authors:** Yuseon Choi, Sanghyeon Park, Eunjong Lee, Hanseo Lee, Sangjin Kim

**Published:** 2026-11-19 | **Categories:** cs.AR, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25580) | [PDF](https://arxiv.org/pdf/2611.25580)

<details>
<summary>Abstract</summary>

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computational overhead. This creates a new opportunity to improve task accuracy and inference efficiency simu...

</details>

<details>
<summary>Share</summary>

```
FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iter...

arXiv: https://arxiv.org/abs/2611.25580

#VLA #robotics
```

</details>

---

### [RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning](https://arxiv.org/abs/2611.25398)

**Authors:** Dijia Zhan, Jinyi Li, Xuemiao Xu, Yan Zhou, Yu Liu et al. (7 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25398) | [PDF](https://arxiv.org/pdf/2611.25398)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training. However, we find that demonstration data vary sharply in supervision value across temporal windows, and that each window's value to the policy evolves substantially during training rather than being fixed or captured by raw loss alone. Motivated by this finding, we propose RefreshGrad, an online adaptive data-sampling framework that periodically scores temporal windows from the evolving policy using five policy-native sign...

</details>

<details>
<summary>Share</summary>

```
RefreshGrad: An Online Adaptive Data-sampling Method for Diffusion-based Visuomotor Learning

Training vision-language-action (VLA) policies from demonstrations typically samples trajectory segments uniformly or relies on static offline data curation before training.

arXiv: https://arxiv.org/abs/2611.25398

#VLA #robotics
```

</details>

---

### [RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback](https://arxiv.org/abs/2611.24494)

**Authors:** Jiayou Zhu, Peng Guo, Litian Zhang, Xinze Shi, Yuting Zhang et al. (9 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CR, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24494) | [PDF](https://arxiv.org/pdf/2611.24494)

<details>
<summary>Abstract</summary>

Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observations. To mitigate these threats, many existing defenses rely on policy adaptation or auxiliary models, but require additional training or inference. We introduce RECLAIM, a training-free, inference-time defense that uses a frozen VLA's own attention response to local visual interventions to guide purification during closed-loop embodied manipulation. Our key insight is that attent...

</details>

<details>
<summary>Share</summary>

```
RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback

Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observat...

arXiv: https://arxiv.org/abs/2611.24494

#VLA #robotics
```

</details>

---

### [Homeward: No Place Like the Training View](https://arxiv.org/abs/2611.24455)

**Authors:** Mingyang Lyu, Yinqian Sun, Gongce Cao, Guobin Shen, Yuhao Zhang et al. (11 authors)

**Published:** 2026-11-18 (updated 2026-11-19) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24455) | [PDF](https://arxiv.org/pdf/2611.24455)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems from a closed-loop diagnostic paradox in simulation: while re-rendering perturbed views into the train...

</details>

<details>
<summary>Share</summary>

```
Homeward: No Place Like the Training View

Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precip...

arXiv: https://arxiv.org/abs/2611.24455

#VLA #robotics
```

</details>

---

### [Adaptive Action Horizon Selection via Flow-Field Uncertainty](https://arxiv.org/abs/2611.24178)

**Authors:** Idan Ben-Ami, Arnon Netzer, Sarah Keren, Idit Diamant

**Published:** 2026-11-18 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24178) | [PDF](https://arxiv.org/pdf/2611.24178)

<details>
<summary>Abstract</summary>

Reliable uncertainty estimates are important for adaptive execution in vision-language-action (VLA) models. Existing approaches such as Adaptive Action Chunking (AAC) estimate action entropy from multiple sampled action chunks, introducing additional inference cost and capturing both uncertainty within an action trajectory and diversity across alternative strategies. We introduce Divergence-based Uncertainty-aware Adaptive Action Chunking (DUAC), a post-hoc method that extracts trajectory-conditioned predictive uncertainty from the vector field of a pretrained VLA. Building on a closed-form fl...

</details>

<details>
<summary>Share</summary>

```
Adaptive Action Horizon Selection via Flow-Field Uncertainty

Reliable uncertainty estimates are important for adaptive execution in vision-language-action (VLA) models.

arXiv: https://arxiv.org/abs/2611.24178

#VLA #robotics
```

</details>

---

### [Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?](https://arxiv.org/abs/2611.24076)

**Authors:** Ryoichi Kurihara, Kota Sunamoto

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.CL, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24076) | [PDF](https://arxiv.org/pdf/2611.24076)

<details>
<summary>Abstract</summary>

VLA policies are fragile to rewording. Success rates alone cannot say whether a policy fails to choose the object or to complete the task, nor where in the policy to intervene. We study the released GR00T N1.7 on two LIBERO-Spatial tasks differing only in the landmark word telling which of two bowls to take. Synonyms absent from the training instructions send the policy to the bowl they name, unlike made-up words, yet complete 67.6% of one task's closed-loop episodes, against the original word's 100%. Before the connector between the vision-language model and the action generator, replacing on...

</details>

<details>
<summary>Share</summary>

```
Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?

VLA policies are fragile to rewording.

arXiv: https://arxiv.org/abs/2611.24076

#VLA #robotics
```

</details>

---

### [NereidVLA: Learning to Understand and Navigate the Underwater World](https://arxiv.org/abs/2611.24864)

**Authors:** Chenjie Zhao, Zhiliang Zhu, Quan Chen, Yuquan Xue, Xingxue Shi et al. (11 authors)

**Published:** 2026-11-18 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.24864) | [PDF](https://arxiv.org/pdf/2611.24864)

<details>
<summary>Abstract</summary>

Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories. We present NereidVLA, a vision-language-action model that transfers marine spatial knowledge to language-conditioned 3D navigation. We first train Sea2Know on approximately two million marine examples to learn target grounding, spatial relations, and scene structure without paired robot-motion supervision. We then adapt it using expert trajectories executed under simulated underwater vehicle dynamics. Given RGB histories and a language instru...

</details>

<details>
<summary>Share</summary>

```
NereidVLA: Learning to Understand and Navigate the Underwater World

Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories.

arXiv: https://arxiv.org/abs/2611.24864

#VLA #robotics
```

</details>

---

### [SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair](https://arxiv.org/abs/2611.22356)

**Authors:** Tao Zhang, Yi Zhong, Jinhao Ruan, Yipeng Gao, Linfeng Zhong et al. (7 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22356) | [PDF](https://arxiv.org/pdf/2611.22356)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies incur control stalls when inference blocks the next action chunk. Asynchronous early inference can hide latency, but its results may be inconsistent with the arriving actual inputs. Unconditional reuse risks acting on mismatched inputs, whereas full recomputation discards useful precomputation. We propose SR-VLA, combining predicted-input lookahead with selective KV cache repair. During current chunk execution, a lightweight action-conditioned predictor generates next-boundary visual observations and proprioceptive state. These predictions, together with t...

</details>

<details>
<summary>Share</summary>

```
SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair

Vision-language-action (VLA) policies incur control stalls when inference blocks the next action chunk.

arXiv: https://arxiv.org/abs/2611.22356

#VLA #robotics
```

</details>

---

### [WiTac: Wrist-Informed Tactile Representations for Contact-Rich Manipulation](https://arxiv.org/abs/2611.21057)

**Authors:** Haotian He, Yiyang Chen, Congsheng Xu, Wenchao Yue, Mingze Ye et al. (12 authors)

**Published:** 2026-11-16 (updated 2026-11-17) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.21057) | [PDF](https://arxiv.org/pdf/2611.21057) | [Project Page](https://wrist-informed-tactile-representations.github.io/)

<details>
<summary>Abstract</summary>

Similar tactile contacts can call for different corrections depending on the configuration of the hand, object and target. Rather than supplying touch and wrist vision separately, fusing them before policy injection better grounds tactile features in visual context, yielding more accurate contact representations. We introduce Wrist-Informed Tactile Representations (WiTac), a pretrained encoder that learns such representations before action generation. Pretrained on nearly 300 hours of SharpaDex data, WiTac deeply fuses tactile signals with hand motion and wrist views into a comprehensive conta...

</details>

<details>
<summary>Share</summary>

```
WiTac: Wrist-Informed Tactile Representations for Contact-Rich Manipulation

Similar tactile contacts can call for different corrections depending on the configuration of the hand, object and target.

arXiv: https://arxiv.org/abs/2611.21057
Project page: https://wrist-informed-tactile-representations.github.io/

#VLA #robotics
```

</details>

---

### [Instructions Before Actions: Prospective and Retrospective Language Supervision for Driving Vision-Language-Action Data](https://arxiv.org/abs/2611.20631)

**Authors:** Angel Martinez-Sanchez, Ross Greer

**Published:** 2026-11-16 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20631) | [PDF](https://arxiv.org/pdf/2611.20631)

<details>
<summary>Abstract</summary>

Driving vision-language-action (VLA) models can accept navigation instructions, yet predicting a driver's trajectory does not establish that a model follows the instruction. We study how driving-language supervision is collected and evaluated, distinguishing prospective instructions issued before an action from retrospective labels written after observing it. We develop ADVLAT-Engine to synchronize spoken instructions, road-scene video, and vehicle trajectories, and compare three navigation apps on 48 replayed routes. On 87 maneuvers announced by both Google Maps and a passenger, the passenger...

</details>

<details>
<summary>Share</summary>

```
Instructions Before Actions: Prospective and Retrospective Language Supervision for Driving Vision-Language-Action Data

Driving vision-language-action (VLA) models can accept navigation instructions, yet predicting a driver's trajectory does not establish that a model follows the instruction.

arXiv: https://arxiv.org/abs/2611.20631

#VLA #robotics
```

</details>

---

### [NF-VLA: A Normalizing-Flow Baseline for Vision-Language-Action Learning](https://arxiv.org/abs/2611.20314)

**Authors:** Ruichen Deng, Qinyu Zhao, Yong-Hyun Park, Mutian Tong, Liang Zheng et al. (6 authors)

**Published:** 2026-11-15 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20314) | [PDF](https://arxiv.org/pdf/2611.20314)

<details>
<summary>Abstract</summary>

Autoregressive normalizing flows (NFs) provide a tractable density for learning and sampling continuous robot actions. We show that a single maximum-likelihood objective can train vision--language--action (VLA) policies competitive with leading methods on manipulation benchmarks. We present NF-VLA, which combines conditional autoregressive normalizing flows with score-based action refinement. Its deep--shallow architecture concentrates visual, language, and proprioceptive prefix conditioning in a high-capacity deep block, while unconditioned shallow blocks provide a shared invertible action tr...

</details>

<details>
<summary>Share</summary>

```
NF-VLA: A Normalizing-Flow Baseline for Vision-Language-Action Learning

Autoregressive normalizing flows (NFs) provide a tractable density for learning and sampling continuous robot actions.

arXiv: https://arxiv.org/abs/2611.20314

#VLA #robotics
```

</details>

---

### [Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning](https://arxiv.org/abs/2611.19198)

**Authors:** Jae Hun Hwang, Yechan Seo, Hong-In Won

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19198) | [PDF](https://arxiv.org/pdf/2611.19198)

<details>
<summary>Abstract</summary>

In simulation, Vision-Agent-Action (VAA) performs pick-and-place in robot cells with gripper or base-frame changes without robot demonstrations or fine-tuning. It uses pre-trained vision-language and language models for interpretation, measures the command map and camera geometry from its own motion and fingertips, estimates lens distortion, and plans grasps from measured object depth. A controlled study of eight public LIBERO-fine-tuned vision-language-action models (VLAs) varies robot hardware, camera geometry, appearance, and base frame. Gripper and frame changes dominate their losses in th...

</details>

<details>
<summary>Share</summary>

```
Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning

In simulation, Vision-Agent-Action (VAA) performs pick-and-place in robot cells with gripper or base-frame changes without robot demonstrations or fine-tuning.

arXiv: https://arxiv.org/abs/2611.19198

#VLA #robotics
```

</details>

---

### [LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models](https://arxiv.org/abs/2611.25460)

**Authors:** LoongForge Team

**Published:** 2026-11-19 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.25460) | [PDF](https://arxiv.org/pdf/2611.25460)

<details>
<summary>Abstract</summary>

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraini...

</details>

<details>
<summary>Share</summary>

```
LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to r...

arXiv: https://arxiv.org/abs/2611.25460

#VLA #robotics
```

</details>

---

### [GRID-UAV: Geometry and Ray-depth Integrated Decision-making for Unmanned Aerial Vehicles](https://arxiv.org/abs/2611.23491)

**Authors:** Anas Anwarul Haq Khan, Amrin Kareem, Muhammad Umer Sheikh, Biplab Banerjee, Muhammad Haris Khan

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23491) | [PDF](https://arxiv.org/pdf/2611.23491)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) encode images with 2D encoders that capture little 3D structure. A common approach is to feed the policy estimated depth, but a UAV chooses its own altitude, must judge distances tens of meters away, where monocular depth is less reliable, and must relate its forward and downward views. On long aerial routes, adding depth features directly brings no significant gain (42.5% vs. 42.6% success), so we study how 3D information should be given to the policy. Analyzing flight failures, we find that two forms of 3D grounding fail in opposite ways: explicit 3D lift...

</details>

<details>
<summary>Share</summary>

```
GRID-UAV: Geometry and Ray-depth Integrated Decision-making for Unmanned Aerial Vehicles

Vision-language-action models (VLAs) encode images with 2D encoders that capture little 3D structure.

arXiv: https://arxiv.org/abs/2611.23491

#VLA #robotics
```

</details>

---

### [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2611.22880)

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.22880) | [PDF](https://arxiv.org/pdf/2611.22880)

<details>
<summary>Abstract</summary>

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portion of the tokens directly encode critical planning-relevant factors, such as agent geometry, motion d...

</details>

<details>
<summary>Share</summary>

```
Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely re...

arXiv: https://arxiv.org/abs/2611.22880

#VLA #robotics
```

</details>

---

### [Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies](https://arxiv.org/abs/2611.22878)

**Authors:** Yuhan Wang, Ruiyang Wang, Jiaguan Zhu

**Published:** 2026-11-17 | **Categories:** cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22878) | [PDF](https://arxiv.org/pdf/2611.22878)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction. However, this optimization raises two challenges: policy updates can alter the velocity-field geometry underlying the score approximation used for stochastic transitions, and sparse multi-task rollouts can yield uneven learning signals across tasks and advantage signs. We introduce an RL framework that combines Outcome-Balanced Proximal Policy Optimization (PPO) with policy-induced flow rectification. Outcome-Balanced PPO rewe...

</details>

<details>
<summary>Share</summary>

```
Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies

Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction.

arXiv: https://arxiv.org/abs/2611.22878

#VLA #robotics
```

</details>

---

### [FAVR: Flow-Aware Visual Residual Alignment for Vision-Language-Action Policies](https://arxiv.org/abs/2611.20971)

**Authors:** Qixuan Wu, Xiaole Yang, Yuguang Yang, Canyu Chen, Linlin Yang et al. (8 authors)

**Published:** 2026-11-16 (updated 2026-11-17) | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.20971) | [PDF](https://arxiv.org/pdf/2611.20971)

<details>
<summary>Abstract</summary>

Pretrained video representations provide rich temporal information for robotic manipulation, yet effectively integrating them into existing vision-language-action (VLA) policies remains challenging. We present Flow-Aware Visual Residual Alignment (FAVR), a lightweight framework for flow-aware visual conditioning of frozen VLA policies. FAVR maintains a compact temporal visual state through linear Test-Time Training (TTT) and retrieves action-conditioned visual features throughout flow-based action generation. By exploiting the affine structure of the frozen action head, we explicitly character...

</details>

<details>
<summary>Share</summary>

```
FAVR: Flow-Aware Visual Residual Alignment for Vision-Language-Action Policies

Pretrained video representations provide rich temporal information for robotic manipulation, yet effectively integrating them into existing vision-language-action (VLA) policies remains challenging.

arXiv: https://arxiv.org/abs/2611.20971

#VLA #robotics
```

</details>

---

### [GraF-VTA: Neuro-Symbolic Trajectory Generation from Vision and Temporal Logic via Graph-Based Fusion](https://arxiv.org/abs/2611.25589)

**Authors:** Zezhi Liu, Zhiwei Zheng, Hanqian Luo, Deyun Qin, Shizhen Wu et al. (6 authors)

**Published:** 2026-11-19 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25589) | [PDF](https://arxiv.org/pdf/2611.25589)

<details>
<summary>Abstract</summary>

Robotic planning from visual observations and signal temporal logic (STL) requires grounding task requirements in scene evidence while adapting plans to execution feedback. We present GraF-VTA, a graph-based framework that extends Vision-TL-Action with structured task representations, causal observation history, and closed-loop trajectory generation. Bidirectional cross-attention fuses STL syntax tokens with visual features, while an optional frozen automaton embedding supplies complementary untimed task structure. A temporal pyramid preserves detailed current observations and compresses older...

</details>

<details>
<summary>Share</summary>

```
GraF-VTA: Neuro-Symbolic Trajectory Generation from Vision and Temporal Logic via Graph-Based Fusion

Robotic planning from visual observations and signal temporal logic (STL) requires grounding task requirements in scene evidence while adapting plans to execution feedback.

arXiv: https://arxiv.org/abs/2611.25589

#VLA #robotics
```

</details>

---

### [TuringPAI: A Foundation for On-Device Physical AI](https://arxiv.org/abs/2611.25474)

**Authors:** Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang et al. (28 authors)

**Published:** 2026-11-19 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25474) | [PDF](https://arxiv.org/pdf/2611.25474)

<details>
<summary>Abstract</summary>

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation histo...

</details>

<details>
<summary>Share</summary>

```
TuringPAI: A Foundation for On-Device Physical AI

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute.

arXiv: https://arxiv.org/abs/2611.25474

#VLA #robotics
```

</details>

---

### [MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation](https://arxiv.org/abs/2611.25105)

**Authors:** Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu et al. (13 authors)

**Published:** 2026-11-18 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25105) | [PDF](https://arxiv.org/pdf/2611.25105)

<details>
<summary>Abstract</summary>

Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the high...

</details>

<details>
<summary>Share</summary>

```
MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

Every move in a robot team changes the world in which its teammates must act.

arXiv: https://arxiv.org/abs/2611.25105

#VLA #robotics
```

</details>

---

### [RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO](https://arxiv.org/abs/2611.23517)

**Authors:** Amrit Lal Singh, Smarak Kanjilal

**Published:** 2026-11-17 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23517) | [PDF](https://arxiv.org/pdf/2611.23517)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models look saturated on LIBERO, yet most of them fall apart on LIBERO-PRO as soon as an object moves or the instruction asks for something new. We argue that what is missing is not scale but decoupling. In these policies, what to do is tied to where things were during training, to the scene around them and to the wording of the instruction. We cut these ties in two places. In the data, LIBERO demonstrations are re-arranged by general rules: every object and fixture is moved and rotated, tasks are carried into other environments and onto other surfaces, and every i...

</details>

<details>
<summary>Share</summary>

```
RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO

Vision-language-action (VLA) models look saturated on LIBERO, yet most of them fall apart on LIBERO-PRO as soon as an object moves or the instruction asks for something new.

arXiv: https://arxiv.org/abs/2611.23517

#VLA #robotics
```

</details>

---

### [BiCAT: Bimanual Coordination Action Tokenization](https://arxiv.org/abs/2611.23499)

**Authors:** Xuanwei Liu, Guipu Cao, Zhongyi Luo, Jiafei Duan

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.23499) | [PDF](https://arxiv.org/pdf/2611.23499)

<details>
<summary>Abstract</summary>

Autoregressive vision-language-action (VLA) models predict discrete action tokens with the next-token objective of their vision-language backbone, so the action tokenizer defines the interface between the policy and the robot. In bimanual manipulation, the two arms share a repertoire of movements yet coordinate through complementary roles, and an action representation should capture both. However, most existing tokenizers encode both arms as a single concatenated action vector, in which motion patterns common to the two arms are not shared and cross-arm dependencies remain entangled within eac...

</details>

<details>
<summary>Share</summary>

```
BiCAT: Bimanual Coordination Action Tokenization

Autoregressive vision-language-action (VLA) models predict discrete action tokens with the next-token objective of their vision-language backbone, so the action tokenizer defines the interface between the policy and t...

arXiv: https://arxiv.org/abs/2611.23499

#VLA #robotics
```

</details>

---

### [CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation](https://arxiv.org/abs/2611.22395)

**Authors:** Mehul Arora, Dhruv Agarwal, Ambuj Agrawal

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22395) | [PDF](https://arxiv.org/pdf/2611.22395)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve high success rates on the LIBERO benchmark but remain sensitive to paraphrasing. Existing VLAs ranging from 0.6B to 7.5B parameters experience a 22-52 point performance drop on LIBERO-Para while SmolVLA exhibits an even larger decline, from 83\% to 8\%. Because most VLAs jointly learn language understanding and action generation, it is difficult to determine whether a failure originates from misunderstanding an instruction or executing it incorrectly. To address these challenges, we introduce CoBoVLA, or CodeBookVLA, a 250M-parameter VLA that decoupl...

</details>

<details>
<summary>Share</summary>

```
CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation

Vision-Language-Action (VLA) models achieve high success rates on the LIBERO benchmark but remain sensitive to paraphrasing.

arXiv: https://arxiv.org/abs/2611.22395

#VLA #robotics
```

</details>

---

### [ResWAM: Learning What Changes, Not What Stays, for World-Action Models](https://arxiv.org/abs/2611.19559)

**Authors:** Chongyu Fan, Gaowen Liu, Ramana Rao Kompella, Jason Corso, Sijia Liu

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.19559) | [PDF](https://arxiv.org/pdf/2611.19559)

<details>
<summary>Abstract</summary>

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world. Existing WAMs supervise complete future observations. However, observations typically change little over an action chunk, so the future loss is dominated by copying static background content rather than learning task-relevant robot and object motion, limiting policy learning. Moreover, existing WAMs rely on large video generation models or separate world models, incurring heavy training and inference compute that hind...

</details>

<details>
<summary>Share</summary>

```
ResWAM: Learning What Changes, Not What Stays, for World-Action Models

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world.

arXiv: https://arxiv.org/abs/2611.19559

#VLA #robotics
```

</details>

---

### [MARS: Dynamic Routing of Reinforcement-Learned Atomic Skills for Multi-Stage Robotic Manipulation](https://arxiv.org/abs/2611.19324)

**Authors:** Zequan Zeng, Junqin Yang, Kai Wang

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19324) | [PDF](https://arxiv.org/pdf/2611.19324)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in multi-task robotic manipulation. However, they still face limitations in control precision and execution stability during critical manipulation stages, such as object grasping, alignment and insertion. To combine general-purpose manipulation capabilities with task-specific fine-grained control, while enabling effective coordination between generalist and specialized policies throughout multi-stage manipulation tasks, this paper proposes MARS (Modular Atomic-skill Routing System), a dynamic routing framework for reinfo...

</details>

<details>
<summary>Share</summary>

```
MARS: Dynamic Routing of Reinforcement-Learned Atomic Skills for Multi-Stage Robotic Manipulation

Vision-Language-Action (VLA) models have demonstrated strong capabilities in multi-task robotic manipulation.

arXiv: https://arxiv.org/abs/2611.19324

#VLA #robotics
```

</details>

---

### [RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution](https://arxiv.org/abs/2611.19081)

**Authors:** Ran Qi, Yixin Xiao, Dawei Wang, Zhiyuan Li, Jinbang Huang et al. (10 authors)

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.19081) | [PDF](https://arxiv.org/pdf/2611.19081)

<details>
<summary>Abstract</summary>

Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities. However, the improvement of such integrated systems remains largely decoupled across their agent and model components, with advances in one component not necessarily benefiting the other, substantially limiting the capabilities of the combined system. As both MLLMs and robotic foundation models become increasingly capable, fully realizing their combined potential calls for co-evolution, an iterative process in which improvements in agents and robotic fou...

</details>

<details>
<summary>Share</summary>

```
RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution

Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities.

arXiv: https://arxiv.org/abs/2611.19081

#VLA #robotics
```

</details>

---

### [Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)

**Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao et al. (11 authors)

**Published:** 2026-11-13 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.18562) | [PDF](https://arxiv.org/pdf/2611.18562)

<details>
<summary>Abstract</summary>

Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the model observes the environment, reasons in a chain of thought, and generates the next end-effector po...

</details>

<details>
<summary>Share</summary>

```
Training Reasoning Models in Simulation to Natively Use Real Robots

Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control.

arXiv: https://arxiv.org/abs/2611.18562

#VLA #robotics
```

</details>

---

### [Full Rank and Stable Sampling of $\tanh$ Networks](https://arxiv.org/abs/2611.25867)

**Authors:** Philipp Grohs, Matěj Trödler

**Published:** 2026-11-19 | **Categories:** math.NA, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.25867) | [PDF](https://arxiv.org/pdf/2611.25867)

<details>
<summary>Abstract</summary>

We study the recovery of feedforward $\tanh$ networks of fixed architecture with $P$ parameters from finitely many point evaluations. First, we characterize the set of parameters where the differential of the realization map has full rank and show that it coincides with the regular parameters in the sense of Vla{č}i{ć} and B{ö}lcskei (2021). Second, we make use of this characterization to prove that almost every tuple of $2P+1$ sampling points yields uniform-norm Lipschitz stability on compact subsets of this parameter set. Third, we prove that for exact observations, projected gradient descen...

</details>

<details>
<summary>Share</summary>

```
Full Rank and Stable Sampling of $\tanh$ Networks

We study the recovery of feedforward $\tanh$ networks of fixed architecture with $P$ parameters from finitely many point evaluations.

arXiv: https://arxiv.org/abs/2611.25867

#VLA #robotics
```

</details>

---

### [Similar Is Not Useful: Selecting In-Context Demonstrations by Closed-Loop Utility](https://arxiv.org/abs/2611.22295)

**Authors:** Jiachen Li, Zhigen Zhao, Shihao Li, Dongmei Chen, Long Chen et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.22295) | [PDF](https://arxiv.org/pdf/2611.22295)

<details>
<summary>Abstract</summary>

Retrieval-augmented vision-language-action (VLA) policies fill their context with the demonstrations whose frames look most like the current observation under frozen DINOv2 embeddings. We ask whether visual similarity selects the demonstrations that make the policy succeed. For a frozen retrieval-augmented VLA (RICL on $π_0$-FAST, LIBERO), we make the demonstration pool swappable at run time and score each demonstration's utility by regressing the closed-loop success of 60 fixed-size pools on their membership. On initial states disjoint from those used for scoring, pools of the five highest-ut...

</details>

<details>
<summary>Share</summary>

```
Similar Is Not Useful: Selecting In-Context Demonstrations by Closed-Loop Utility

Retrieval-augmented vision-language-action (VLA) policies fill their context with the demonstrations whose frames look most like the current observation under frozen DINOv2 embeddings.

arXiv: https://arxiv.org/abs/2611.22295

#VLA #robotics
```

</details>

---

### [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397)

**Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang et al. (27 authors)

**Published:** 2026-11-13 (updated 2026-11-18) | **Categories:** cs.CL, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.18397) | [PDF](https://arxiv.org/pdf/2611.18397)

<details>
<summary>Abstract</summary>

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens of thousands of hours of device-level keyboard and mouse interaction. These trajectories span simulated games and embodied environments, allowing the model to learn environmental dyn...

</details>

<details>
<summary>Share</summary>

```
Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments.

arXiv: https://arxiv.org/abs/2611.18397

#VLA #robotics
```

</details>

---

### [PAIR: Bringing Household Robots into the Smart Home](https://arxiv.org/abs/2611.23070)

**Authors:** Junseong Pyo, Hyeongjin Kim, Jongwook Han, Seungwon Kook, Sungjib Lim et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.23070) | [PDF](https://arxiv.org/pdf/2611.23070)

<details>
<summary>Abstract</summary>

Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs. Existing embodied AI simulation environments, however, model appliances solely as physical objects. We introduce PAIR, a smart-home simulation environment grounded in the Matter protocol~\footnote{https://csa-iot.org/all-solutions/matter/}, the industry standard for smart-home devices. PAIR provides 84 smart-device assets whose functional control panels and APIs act on a shared device state, with ambient conditions that evolve in response to both. From a survey of 1,443 requests,...

</details>

<details>
<summary>Share</summary>

```
PAIR: Bringing Household Robots into the Smart Home

Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs.

arXiv: https://arxiv.org/abs/2611.23070

#VLA #robotics
```

</details>

---

### [ACiT: Proprioceptive-Prior Action Chunking with Inverted Transformers](https://arxiv.org/abs/2611.20719)

**Authors:** Haixiang Wu, Zhihao Guan, Yang Yang

**Published:** 2026-11-16 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.20719) | [PDF](https://arxiv.org/pdf/2611.20719)

<details>
<summary>Abstract</summary>

Visuomotor policies condition action prediction on visual and proprioceptive observations. While historical proprioceptive sequences carry rich dynamic priors, current methods treat them as equal to high-dimensional vision, causing the proprioceptive signal to be overwhelmed. To identify what is lost in equal-conditioning fusion, we analyze proprioceptive data and find that strong inter-joint coupling is the key action-determining structure. This finding aligns with the neural sensorimotor loop, in which proprioception first forms a body-centered prior and vision is later calibrated via pariet...

</details>

<details>
<summary>Share</summary>

```
ACiT: Proprioceptive-Prior Action Chunking with Inverted Transformers

Visuomotor policies condition action prediction on visual and proprioceptive observations.

arXiv: https://arxiv.org/abs/2611.20719

#VLA #robotics
```

</details>

---

### [ReRead: Wrong Predictions, Useful Representations - Correcting Frozen Robot Policies by Re-reading Their Own Representations](https://arxiv.org/abs/2611.20465)

**Authors:** Xu Su, Shunlong Xiao, Qintao Yi, Mingkuan Zhao, Xinmiao Yu et al. (8 authors)

**Published:** 2026-11-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.20465) | [PDF](https://arxiv.org/pdf/2611.20465)

<details>
<summary>Abstract</summary>

When a pretrained robot policy fails on challenging tasks, common remedies include retraining the backbone, adding an external visual encoder, or introducing a memory module. We argue that wrong predictions do not imply wrong representations: a policy can retain the required information yet fail to read it out as the correct action. To test this view, we propose ReRead: with the backbone frozen, a corrector re-reads the current and two previous caches to predict an action residual. The corrector sees no images, is trained solely on offline demonstrations from all 50 RoboTwin 2.0 tasks, and add...

</details>

<details>
<summary>Share</summary>

```
ReRead: Wrong Predictions, Useful Representations - Correcting Frozen Robot Policies by Re-reading Their Own Representations

When a pretrained robot policy fails on challenging tasks, common remedies include retraining the backbone, adding an external visual encoder, or introducing a memory module.

arXiv: https://arxiv.org/abs/2611.20465

#VLA #robotics
```

</details>

---

### [MetricHand: Geometry-Aware Flow Matching for 4D Hand Reconstruction in Metric World Space](https://arxiv.org/abs/2611.21060)

**Authors:** Yibo Bai, Likui Zhang, Jinglei Zhang, Zhengbin Pang, Xingshen Song et al. (7 authors)

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.21060) | [PDF](https://arxiv.org/pdf/2611.21060)

<details>
<summary>Abstract</summary>

Egocentric hand motion provides physical motion supervision for dexterous manipulation and vision-language-action pretraining. Reliable use of this supervision requires accurate and temporally coherent 4D hand reconstruction in metric world space. Existing methods typically lift framewise estimates produced under weak perspective into world coordinates. By ignoring joint-dependent depth variation at close range, this approximation couples errors in translation, orientation, and articulation that persist after world lifting and worsen under occlusion. We present MetricHand, a geometry-aware flo...

</details>

<details>
<summary>Share</summary>

```
MetricHand: Geometry-Aware Flow Matching for 4D Hand Reconstruction in Metric World Space

Egocentric hand motion provides physical motion supervision for dexterous manipulation and vision-language-action pretraining.

arXiv: https://arxiv.org/abs/2611.21060

#VLA #robotics
```

</details>

---
