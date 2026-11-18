# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-18 22:50 UTC

**Papers shown:** 49 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [SuperGlance: Driving at a Glance with a Vision-Language Model](https://arxiv.org/abs/2611.19138)

**Authors:** Jieyuan Pei, Xin Yan, Mingwei Xu, Haiyi Zhang, Siyu Zou et al. (12 authors)

**Published:** 2026-11-14 | **Categories:** cs.RO | **Relevance:** ★★★★☆

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

### [InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](https://arxiv.org/abs/2611.22584)

**Authors:** Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen et al. (8 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

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

### [VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2611.22666)

**Authors:** Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

### [Scaling VLA Serving Under Robotic Execution Constraints](https://arxiv.org/abs/2611.14969)

**Authors:** Yue Zhang, Zicong Ye, Lufang Chen, Dance Yang, Mingyang Li et al. (17 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14969) | [PDF](https://arxiv.org/pdf/2611.14969) | [Code](https://github.com/X-Square-Robot/xinfer)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation. In our production setting, hundreds of VLA-powered robots are already operating in real-world environments, creating an immediate need for efficient fleet serving. We present XInfer, a production-deployed VLA serving system designed to reduce the inference infrastructure cost of large-scale robotic deployments. XInfer jointly coordinates heterogeneous VLA computation with the evolving response requirements of robotic execution. By exploiting computational parallelism while managin...

</details>

<details>
<summary>Share</summary>

```
Scaling VLA Serving Under Robotic Execution Constraints

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation.

arXiv: https://arxiv.org/abs/2611.14969
Code: https://github.com/X-Square-Robot/xinfer

#VLA #robotics
```

</details>

---

### [RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models](https://arxiv.org/abs/2611.22736)

**Authors:** Shaozhen Liu, Zhiwei Li, Jiayang Sun, Shuangjun Du, Yi Zhong et al. (9 authors)

**Published:** 2026-11-17 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

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

### [SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair](https://arxiv.org/abs/2611.22356)

**Authors:** Tao Zhang, Yi Zhong, Jinhao Ruan, Yipeng Gao, Linfeng Zhong et al. (7 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

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

**Published:** 2026-11-16 (updated 2026-11-17) | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

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

**Published:** 2026-11-16 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

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

### [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](https://arxiv.org/abs/2611.20011)

**Authors:** Nikos Theodoridis, Reenu Mohandas, Sushil Sharma, Ciarán Hogan, Ganesh Sistu et al. (8 authors)

**Published:** 2026-11-15 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

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

**Published:** 2026-11-13 | **Categories:** cs.RO, cs.AI, cs.ET | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Also relevant to:** Egocentric Data

**Links:** [arXiv](https://arxiv.org/abs/2611.18372) | [PDF](https://arxiv.org/pdf/2611.18372)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control. In under 4 years the field has moved from RT-2, the first VLA, to open models that fine-tune on a single consumer GPU and to proprietary generalists that clean unseen homes. This survey reviews 88 works from December 2022 to October 2026, mainly on manipulation and navigation, plus humanoid control, world-action models and evaluation. We follow a VLA through its life cycle, from model design to training and deployment, along seven axes...

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

### [STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models](https://arxiv.org/abs/2611.16589)

**Authors:** Zhuo Han, Yeqiang Wang, Xinran Wang, Hongwei Han, Yi Xiong et al. (11 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16589) | [PDF](https://arxiv.org/pdf/2611.16589) | [Project Page](https://stvla.github.io/)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires both spatial scene understanding and task history. However, many vision-language-action (VLA) policies rely primarily on current observations, without explicitly integrating spatial structure and task history. Appearance-based memories can be sensitive to occlusion and viewpoint changes, while spatial representations of the current scene alone do not preserve how the scene has changed during task execution. We introduce STVLA, a framework that incorporates features from a pretrained visual geometry foundation model into temporal memory alongside visual repre...

</details>

<details>
<summary>Share</summary>

```
STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models

Robotic manipulation often requires both spatial scene understanding and task history.

arXiv: https://arxiv.org/abs/2611.16589
Project page: https://stvla.github.io/

#VLA #robotics
```

</details>

---

### [I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History](https://arxiv.org/abs/2611.16419)

**Authors:** Xiangyi Jia, Kaixian Qu, Shengzhi Wang, Chenyu Yang, Robert Katzschmann et al. (6 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.16419) | [PDF](https://arxiv.org/pdf/2611.16419) | [Project Page](https://see-want.github.io/)

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly inferring the ongoing atomic action and the broader mission it serves from a short visual teleoperation history. To study this, we introduce VI AMO (Vision Intention Action and Mission Ongoing), a dataset of 6,600 episodes from eleven robot so...

</details>

<details>
<summary>Share</summary>

```
I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control.

arXiv: https://arxiv.org/abs/2611.16419
Project page: https://see-want.github.io/

#VLA #robotics
```

</details>

---

### [MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes](https://arxiv.org/abs/2611.15937)

**Authors:** Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15937) | [PDF](https://arxiv.org/pdf/2611.15937) | [Project Page](https://mmahdavian.github.io/MOSAIC/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relationships to be inferred implicitly. This limitation is particularly problematic in cluttered environments, where small spatial errors can lead to unintended contacts or collisions. We propose MOSAIC, a modular spatial- and obstacle-aware framework that can be integrated with pretrained VLA policies to improve object-level scene understanding and action generation. Our method augmen...

</details>

<details>
<summary>Share</summary>

```
MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relati...

arXiv: https://arxiv.org/abs/2611.15937
Project page: https://mmahdavian.github.io/MOSAIC/

#VLA #robotics
```

</details>

---

### [ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490)

**Authors:** Zibin Dong, Yicheng Liu, Shiduo Zhang, Tianyuan Yuan, Baijun Ye et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15490) | [PDF](https://arxiv.org/pdf/2611.15490) | [Project Page](https://zibindong.github.io/actioncodec2-page/)

<details>
<summary>Abstract</summary>

Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We introduce ActionCodec2, a non-neural streaming tokenizer that releases actions incrementally while keeping trajectory reconstruction error within a prescribed tolerance. Its encoder quantizes each step relative to the decoder's reconstructed state, so the selected motion primitive corrects residual error rather than allowing errors from independently quantized increments to accumulate. Finding the smallest such primiti...

</details>

<details>
<summary>Share</summary>

```
ActionCodec2: A Streaming Action Tokenizer

Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable.

arXiv: https://arxiv.org/abs/2611.15490
Project page: https://zibindong.github.io/actioncodec2-page/

#VLA #robotics
```

</details>

---

### [Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning](https://arxiv.org/abs/2611.15381)

**Authors:** Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer, Yung-Hui Li, Donglin Chen et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.15381) | [PDF](https://arxiv.org/pdf/2611.15381) | [Project Page](https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored. We present a low-cost and reproducible mobile bimanual platform integrating two LeRobot SO-101 manipulators with a TurtleBot 4 and a LeRobot-ROS 2 software stack. Using long-horizon toilet cleaning as a case study, we collect 250 real-world demonstrations and evaluate $π_0$, $π_{0.5}$, SmolVLA, and GR00T under the same embodiment and task conditions. We further evaluate variants using SARM-derived task-progress signal...

</details>

<details>
<summary>Share</summary>

```
Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning

Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored.

arXiv: https://arxiv.org/abs/2611.15381
Project page: https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/

#VLA #robotics
```

</details>

---

### [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2611.22880)

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

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

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

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

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; posted in last 2 days

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

### [CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation](https://arxiv.org/abs/2611.22395)

**Authors:** Mehul Arora, Dhruv Agarwal, Ambuj Agrawal

**Published:** 2026-11-17 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

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

### [Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training](https://arxiv.org/abs/2611.17394)

**Authors:** Gongyue Teng, Yuqing Xie, Yixian Zhang, Feng Gao, Shu'ang Yu et al. (13 authors)

**Published:** 2026-11-12 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.17394) | [PDF](https://arxiv.org/pdf/2611.17394)

<details>
<summary>Abstract</summary>

Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning. Coding agents can autonomously generate demonstrations through environment interaction, yet successful execution alone does not ensure effective supervision for VLA learning. We introduce Agentic-Teacher, an autonomous data engine for failure-driven VLA post-training. Given a VLA checkpoint, a task specification, and configured environment tools, the engine analyzes failed rollouts, selects intervention states, and iteratively develops cl...

</details>

<details>
<summary>Share</summary>

```
Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training

Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning.

arXiv: https://arxiv.org/abs/2611.17394

#VLA #robotics
```

</details>

---

### [What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation](https://arxiv.org/abs/2611.16246)

**Authors:** Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu et al. (7 authors)

**Published:** 2026-11-12 (updated 2026-11-17) | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.16246) | [PDF](https://arxiv.org/pdf/2611.16246)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models drive the robot directly from camera views, yet a VLA alone shows three typical failures. It walks past the goal, stops before reaching it, and rarely recovers after going off track. Pairing a VLA with a large language model (LLM) planner fixes these failures, but queries the LLM throughout every episode, adding token costs and latency. We introduce Harness-to-Executor (H2E), a task-level distillation method that pairs an LLM planner and a frozen VLA as a heterogeneous training agent, keeps only sessions that reach the goal, and then trains a VLA alone on th...

</details>

<details>
<summary>Share</summary>

```
What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation

Vision-language-action (VLA) models drive the robot directly from camera views, yet a VLA alone shows three typical failures.

arXiv: https://arxiv.org/abs/2611.16246

#VLA #robotics
```

</details>

---

### [What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491)

**Authors:** Zhuoyue Li, Zhendong Han, Pankhuri Vanjani, Wenting Li, Rudolf Lioutikov

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15491) | [PDF](https://arxiv.org/pdf/2611.15491)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA reactive, using \pihalf{} on two dynamic simulation benchmarks and three real-robot tasks. We vary the prediction and execution horizons, compare synchronous and asynchronous inference, test methods that deliver actions sooner or keep successive chunks continuous, and adapt the policy with motion cues and latent-space reinforcement learning. The best prediction horizon is about one second, and the best execution horizo...

</details>

<details>
<summary>Share</summary>

```
What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation

Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed.

arXiv: https://arxiv.org/abs/2611.15491

#VLA #robotics
```

</details>

---

### [Similar Is Not Useful: Selecting In-Context Demonstrations by Closed-Loop Utility](https://arxiv.org/abs/2611.22295)

**Authors:** Jiachen Li, Zhigen Zhao, Shihao Li, Dongmei Chen, Long Chen et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

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

### [PAIR: Bringing Household Robots into the Smart Home](https://arxiv.org/abs/2611.23070)

**Authors:** Junseong Pyo, Hyeongjin Kim, Jongwook Han, Seungwon Kook, Sungjib Lim et al. (6 authors)

**Published:** 2026-11-17 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

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

**Published:** 2026-11-16 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

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

**Published:** 2026-11-16 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

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

### [PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach](https://arxiv.org/abs/2611.15117)

**Authors:** Heng Li, Yang Li, Yifan Duan, Ren Fang, Matao Duan et al. (9 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15117) | [PDF](https://arxiv.org/pdf/2611.15117)

<details>
<summary>Abstract</summary>

Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectories remains challenging because the controller must determine when and how the base should move, and this decision depends on the mounted-arm morphology. We therefore present PolyMorphWBC, a hierarchical controller that takes an EE trajectory...

</details>

<details>
<summary>Share</summary>

```
PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach

Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base.

arXiv: https://arxiv.org/abs/2611.15117

#VLA #robotics
```

</details>

---

### [MetricHand: Geometry-Aware Flow Matching for 4D Hand Reconstruction in Metric World Space](https://arxiv.org/abs/2611.21060)

**Authors:** Yibo Bai, Likui Zhang, Jinglei Zhang, Zhengbin Pang, Xingshen Song et al. (7 authors)

**Published:** 2026-11-16 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; posted in last 2 days

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

### [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397)

**Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang et al. (27 authors)

**Published:** 2026-11-13 (updated 2026-11-17) | **Categories:** cs.CL, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

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

### [CARE-Drive: Coupled Alternating Refinement for Ego-trajectories](https://arxiv.org/abs/2611.15360)

**Authors:** Xiao Ma, Yijun Chen, Zhiquan Hu, Jicheng Zhao, Ran Ji et al. (7 authors)

**Published:** 2026-11-11 (updated 2026-11-13) | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.15360) | [PDF](https://arxiv.org/pdf/2611.15360)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving. To further improve the quality of predicted trajectories, existing studies introduce candidate refinement, residual denoising, and token correction. However, these methods typically focus on unified refinement of the entire trajectory, paying limited attention to the distinct physical quantities and their interactions. We further investigate physical specialization and coordination in trajectory refinement, centering on position and heading for simpler and more intuitive cor...

</details>

<details>
<summary>Share</summary>

```
CARE-Drive: Coupled Alternating Refinement for Ego-trajectories

Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving.

arXiv: https://arxiv.org/abs/2611.15360

#VLA #robotics
```

</details>

---

### [Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction](https://arxiv.org/abs/2611.15651)

**Authors:** Miao Pan, Kaixiang Yao, Xiaohe Zhou, Xu Wang, Qinfeng Li et al. (7 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.15651) | [PDF](https://arxiv.org/pdf/2611.15651)

<details>
<summary>Abstract</summary>

Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable. During execution, actions deviate from intended effects, constrained by the embodiment and environment. An embodied brain must understand why execution deviates, identify what can be reliably realized, and revise decisions using interaction experience. These correspond to causal failure localization, capability-constrained adaptation, and experience-driven revision. Current embodied foundation models largely lack these capabilities....

</details>

<details>
<summary>Share</summary>

```
Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction

Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable.

arXiv: https://arxiv.org/abs/2611.15651

#VLA #robotics
```

</details>

---
