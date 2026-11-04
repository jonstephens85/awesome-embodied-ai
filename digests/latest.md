# What's New

Papers discovered in the run at **2026-11-04 21:43 UTC**.

**New this run:** 30

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (2)

### [RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)

**Authors:** Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric human" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05163) | [PDF](https://arxiv.org/pdf/2611.05163) | [Project Page](https://ryan-seungyong-lee.github.io/RoboTryOn)

<details>
<summary>Abstract</summary>

Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keeps the person and swaps the garment, RoboTryOn keeps the demonstrated motion and swaps the human for...

</details>

<details>
<summary>Share</summary>

```
RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On

Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations.

arXiv: https://arxiv.org/abs/2611.05163
Project page: https://ryan-seungyong-lee.github.io/RoboTryOn

#egocentric #robotlearning
```

</details>

---

### [EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering](https://arxiv.org/abs/2611.04913)

**Authors:** Guoning Chen, Zhexun Hu, Yifan Wei, Yixuan Weng, Bin Li et al. (6 authors)

**Published:** 2026-11-03 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "Ego4D" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04913) | [PDF](https://arxiv.org/pdf/2611.04913)

<details>
<summary>Abstract</summary>

Long instructional videos are increasingly used in medical education, industrial training, and procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may be missing, ASR noisy, OCR sparse, and decisive actions briefly shown without narration. Existing VideoQA systems typically return labels or free-form text, making answer support difficult to inspect. We study Long Video Moment Question Answering (LVMQA), where a system returns timestamped answer-supporting evidence. We propose EP-LVMQA, an evidence-preserving coarse-to-fine framework comprising an Unce...

</details>

<details>
<summary>Share</summary>

```
EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering

Long instructional videos are increasingly used in medical education, industrial training, and procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may be missing, ASR noisy,...

arXiv: https://arxiv.org/abs/2611.04913

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (19)

### [RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)

**Authors:** Deng-Ke Wu, Yifan Jin, Yida Yang, Lei Qian, Zhaoye Zhou et al. (11 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03850) | [PDF](https://arxiv.org/pdf/2611.03850) | [Project Page](https://roboscope.pages.dev/) | [Code](https://github.com/MINT-SJTU/RoboScope-Kit)

<details>
<summary>Abstract</summary>

Simulation benchmarks are the standard way to compare robot policies, but each benchmark brings its own evaluator, observation layout, and action convention, and evaluation is slow: 500 RoboTwin Easy episodes with one simulator and one model on one GPU take 359.7 minutes. Profiling the official StarVLA evaluator shows that simulation occupies CPU cores while the GPU averages 14.3% utilization. RoboScope Kit wraps each model once in a Python class called a Policy, and each benchmark once in an adapter around the benchmark's own evaluator, so the benchmark's rules and scoring stay unchanged. Sch...

</details>

<details>
<summary>Share</summary>

```
RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation

Simulation benchmarks are the standard way to compare robot policies, but each benchmark brings its own evaluator, observation layout, and action convention, and evaluation is slow: 500 RoboTwin Easy episodes with one...

arXiv: https://arxiv.org/abs/2611.03850
Project page: https://roboscope.pages.dev/
Code: https://github.com/MINT-SJTU/RoboScope-Kit

#VLA #robotics
```

</details>

---

### [Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)

**Authors:** Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04391) | [PDF](https://arxiv.org/pdf/2611.04391) | [Project Page](https://junhyeong-park.me/h2rb/)

<details>
<summary>Abstract</summary>

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB b...

</details>

<details>
<summary>Share</summary>

```
Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations.

arXiv: https://arxiv.org/abs/2611.04391
Project page: https://junhyeong-park.me/h2rb/

#VLA #robotics
```

</details>

---

### [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)

**Authors:** Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05372) | [PDF](https://arxiv.org/pdf/2611.05372) | [Code](https://github.com/Tinaliu0123/PolicyIK)

<details>
<summary>Abstract</summary>

Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depends on hand-tuned controllers, and training data on physical robots are costly to collect. We present PolicyIK, a goal-conditioned reinforcement learning policy for high-precision IK. It updates joint-position references from pose feedback and observes its accumulated reference relative to the measu...

</details>

<details>
<summary>Share</summary>

```
PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning

Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments.

arXiv: https://arxiv.org/abs/2611.05372
Code: https://github.com/Tinaliu0123/PolicyIK

#VLA #robotics
```

</details>

---

### [LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models](https://arxiv.org/abs/2611.05093)

**Authors:** Syed Umer Bukhari, Magnus Almgren, Ahmed Ali-Eldin

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.05093) | [PDF](https://arxiv.org/pdf/2611.05093)

<details>
<summary>Abstract</summary>

Post-training quantization (PTQ) for vision-language-action (VLA) models promises smaller and faster VLA deployments. However, when analyzing existing VLA quantization works, we realised that it is hard to reason about the performance of the suggested quantization method compared to existing, similar, or in many cases, simpler PTQ methods. We present LoopQ, a closed-loop benchmark that compares multiple quantization policies on the same checkpoint, layers and engine, varying only the method and the kernels. We evaluate RTN, AWQ, GPTQ, ActQuant and QuantVLA on four VLAs with more than 180,000 e...

</details>

<details>
<summary>Share</summary>

```
LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models

Post-training quantization (PTQ) for vision-language-action (VLA) models promises smaller and faster VLA deployments.

arXiv: https://arxiv.org/abs/2611.05093

#VLA #robotics
```

</details>

---

### [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)

**Authors:** Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng, Tsung-Wei Ke

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05080) | [PDF](https://arxiv.org/pdf/2611.05080) | [Project Page](https://embodiedai-ntu.github.io/cronos/)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments. However, standard RL pipelines rely on episodic training with frequent scene resets, which is impractical for real-world deployment due to the need for substantial human intervention. While prior work has studied non-episodic RL in relatively small policies trained from scratch, its behavior when fine-tuning modern large-scale pre-trained vision-language-action (VLA) models remains underexplored. In this work, we introduce CRONOS, a simulation benchmark for RL fine-tuning of VLAs under...

</details>

<details>
<summary>Share</summary>

```
CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments.

arXiv: https://arxiv.org/abs/2611.05080
Project page: https://embodiedai-ntu.github.io/cronos/

#VLA #robotics
```

</details>

---

### [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392)

**Authors:** Yeonseok Lee

**Published:** 2026-11-03 | **Categories:** cs.LO, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04392) | [PDF](https://arxiv.org/pdf/2611.04392) | [Code](https://github.com/ylee-sling/Aero-VPA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by streaming billions of parameters from memory. We present Aero-VPA, a lightweight Vision-Predictor-Action architecture for 3D navigation on edge hardware. A compact RGB-D Vision Transformer and a five-head ensemble predictor, trained without pixel reconstruction, forecast the next latent state; a Conditional Flow Matching solver generates a velocity and yaw-rate chunk in two Euler ste...

</details>

<details>
<summary>Share</summary>

```
Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware

Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by str...

arXiv: https://arxiv.org/abs/2611.04392
Code: https://github.com/ylee-sling/Aero-VPA

#VLA #robotics
```

</details>

---

### [AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)

**Authors:** Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa, Jason Wang et al. (20 authors)

**Published:** 2026-11-02 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03815) | [PDF](https://arxiv.org/pdf/2611.03815) | [Project Page](https://a-0.airoa.io)

<details>
<summary>Abstract</summary>

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a...

</details>

<details>
<summary>Share</summary>

```
AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage.

arXiv: https://arxiv.org/abs/2611.03815
Project page: https://a-0.airoa.io

#VLA #robotics
```

</details>

---

### [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](https://arxiv.org/abs/2611.05249)

**Authors:** Asher James Hancock, Boyi Li, Yuxiao Chen, Shuhan Tan, Wenhao Ding et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.05249) | [PDF](https://arxiv.org/pdf/2611.05249)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations. Those representations must carry information useful for control, yet the VLM was never trained for the action expert's flow-matching objective. Two signals can address this: gradients backpropagated from the expert's loss (coupling), or VLM supervision to predict discrete tokens encoding the same target actions. Prominent training recipes forgo the first, blocking expert-to-VLM gradients (insul...

</details>

<details>
<summary>Share</summary>

```
Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs

Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations.

arXiv: https://arxiv.org/abs/2611.05249

#VLA #robotics
```

</details>

---

### [Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training](https://arxiv.org/abs/2611.04873)

**Authors:** Zicheng Kong, Zhenbo Xu, Haoyan Zhang, Jinghan Yang, Zhenzhen Li et al. (10 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.04873) | [PDF](https://arxiv.org/pdf/2611.04873)

<details>
<summary>Abstract</summary>

Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality. We introduce Trusting Imagined Futures (TIF), an offline supervision selection method for vision-language-action (VLA) post-training that audits predicted rewards using execution feedback. A multidimensional reward model predicts a utility score for candidate ranking and five dimensions of execution quality. An auditor uses reward predictions and uncertainty to identify overestimation patterns learned from paired imagined videos a...

</details>

<details>
<summary>Share</summary>

```
Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training

Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality.

arXiv: https://arxiv.org/abs/2611.04873

#VLA #robotics
```

</details>

---

### [RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training](https://arxiv.org/abs/2611.04368)

**Authors:** Shresth Grover, Andrey Kolobov, Dhruv Shah

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04368) | [PDF](https://arxiv.org/pdf/2611.04368)

<details>
<summary>Abstract</summary>

Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training procedure: RAFT first trains low-rank adapters on task-relevant reasoning annotations, then freezes them while fine-tuning the policy on action demonstrations. On a physical DROID robot, RAFT achieves $75.0\%$ out-of-distribution success, compared with $27.9\%$ for plain fine-tuning; on a multi-stage bim...

</details>

<details>
<summary>Share</summary>

```
RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training

Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions.

arXiv: https://arxiv.org/abs/2611.04368

#VLA #robotics
```

</details>

---

### [Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](https://arxiv.org/abs/2611.04166)

**Authors:** Zihao Feng, Qingzhao Zhang, Chunyu Xia, Bo Yu, Z. Morley Mao et al. (6 authors)

**Published:** 2026-11-03 | **Categories:** cs.LG, cs.CR, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04166) | [PDF](https://arxiv.org/pdf/2611.04166)

<details>
<summary>Abstract</summary>

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety. Prior attacks on VLA reasoning corrupt the rationale itself and leave visible evidence in the text. We show that visual perturbations can instead alter the physical action while keeping the generated rationale word-for-word identical. At the shared text/action interface of Alpamayo for driving and InstructVLA for manipulation, our text-neutral action-subspace (TNAS) diagnostic shows that the locally most action-sensitive direction is nearly...

</details>

<details>
<summary>Share</summary>

```
Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety.

arXiv: https://arxiv.org/abs/2611.04166

#VLA #robotics
```

</details>

---

### [Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy](https://arxiv.org/abs/2611.04006)

**Authors:** Ruijie Zhang, Jiayin Zheng, Yequan Zhao, Liyan Tan, Ziyue Liu et al. (11 authors)

**Published:** 2026-11-02 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.04006) | [PDF](https://arxiv.org/pdf/2611.04006)

<details>
<summary>Abstract</summary>

Modern learning systems increasingly combine pretrained models with downstream heads. Despite the growing importance of such modular designs, how the downstream model co-adapts to the geometry of pretrained representations remains relatively underexplored. We study this problem through vision-language-action models (VLAs), where a pretrained vision-language model (VLM) conditions an action model for control. We find that the action model progressively concentrates its sensitivity on high-variance dimensions of the VLM outputs. Through controlled experiments across different backbone-head model...

</details>

<details>
<summary>Share</summary>

```
Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy

Modern learning systems increasingly combine pretrained models with downstream heads.

arXiv: https://arxiv.org/abs/2611.04006

#VLA #robotics
```

</details>

---

### [Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)

**Authors:** Sombit Dey, Luc Van Gool, Danda Pani Paudel

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.05155) | [PDF](https://arxiv.org/pdf/2611.05155)

<details>
<summary>Abstract</summary>

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity. Existing Vision-Language-Action (VLA) architectures execute high-level semantic reasoning and action ex- ecution sequentially within the primary control loop, creating a fundamental tension between semantic-reasoning capability and robot agility. To address this, we propose Asynchronous Robot Policy (ARP), an architectural framework that decouples semantic reasoning from low-level action g...

</details>

<details>
<summary>Share</summary>

```
Asynchronous Robot Policies

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity.

arXiv: https://arxiv.org/abs/2611.05155

#VLA #robotics
```

</details>

---

### [Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture](https://arxiv.org/abs/2611.04972)

**Authors:** Abhijeet M. Kulkarni, Saimouli Katragadda, Yuze Du, Zijun Sha, Guoquan Huang

**Published:** 2026-11-03 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04972) | [PDF](https://arxiv.org/pdf/2611.04972)

<details>
<summary>Abstract</summary>

By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting language-based navigation commands but lack the physical grounding and explicit safety assurance required for real-world operation. Therefore, this paper aims to cage Legged-Vision-Language Navigation (VLN) through a safety architecture that provides physical grounding and ensures navigation safety. The key idea is not to abandon the powerful capabilities of end-to-end VLA planning, b...

</details>

<details>
<summary>Share</summary>

```
Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture

By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting lang...

arXiv: https://arxiv.org/abs/2611.04972

#VLA #robotics
```

</details>

---

### [Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots](https://arxiv.org/abs/2611.04522)

**Authors:** Zhiqian Xia, Lianyang Ma, Haifeng Xia, Siyu Xia, Wei Wang et al. (6 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04522) | [PDF](https://arxiv.org/pdf/2611.04522)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved promising performance for generalized robotic manipulation, yet their reliance on expensive real-robot data remains a fundamental bottleneck. A scalable alternative is to transfer knowledge from off-the-shelf human-centric videos. However, existing methods extract latent action representations that are entangled with scene-specific noise, diluting the transferred knowledge. Motivated by this limitation, we propose Action-Intent Transfer (AIT), a two-stage method that transfers knowledge through a clean action representation shared across humans...

</details>

<details>
<summary>Share</summary>

```
Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots

Vision-Language-Action (VLA) models have achieved promising performance for generalized robotic manipulation, yet their reliance on expensive real-robot data remains a fundamental bottleneck.

arXiv: https://arxiv.org/abs/2611.04522

#VLA #robotics
```

</details>

---

### [DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226)

**Authors:** Renkai Yi, Yuwei Wu, Haoyu Zhang, Penghao Dai, Zhi Gao et al. (7 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04226) | [PDF](https://arxiv.org/pdf/2611.04226)

<details>
<summary>Abstract</summary>

Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework for robot-use agents that uses phase-specific evidence and method preconditions to select program reuse or predefined recovery skills, including bounded vision-language-action (VLA) grasping. After the original program exits, a multimodal large language model (MLLM) can generate corrective code from images and execution...

</details>

<details>
<summary>Share</summary>

```
DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution

Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful.

arXiv: https://arxiv.org/abs/2611.04226

#VLA #robotics
```

</details>

---

### [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](https://arxiv.org/abs/2611.04096)

**Authors:** Kevin Weekly, Alexandre M. Bayen

**Published:** 2026-11-03 | **Categories:** cs.RO, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04096) | [PDF](https://arxiv.org/pdf/2611.04096)

<details>
<summary>Abstract</summary>

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically been performed offline. As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic policies, a deterministic safety layer with formal guarantees is an essential complement. We present a CUDA implementation of the canonical WENO5 + TVD-RK3 + Lax-Friedrichs level-set Hamilton-Jacobi-Isaacs solver for 2D, 3D, and 4...

</details>

<details>
<summary>Share</summary>

```
Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically...

arXiv: https://arxiv.org/abs/2611.04096

#VLA #robotics
```

</details>

---

### [AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241)

**Authors:** Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei et al. (8 authors)

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04241) | [PDF](https://arxiv.org/pdf/2611.04241)

<details>
<summary>Abstract</summary>

Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not necessarily reflect changes in task objectives. We introduce AceAction, a dataset of human gameplay across multiple 3D games for learning skill composition and subgoal transitions. AceAction organizes demonstrations around complete tasks, linking overall instructions, ordered subgoals, and local skill instructions to...

</details>

<details>
<summary>Share</summary>

```
AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds

Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly.

arXiv: https://arxiv.org/abs/2611.04241

#VLA #robotics
```

</details>

---

### [Future Representation Distillation for Imagination-Free World Action Models](https://arxiv.org/abs/2611.04527)

**Authors:** Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah et al. (8 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04527) | [PDF](https://arxiv.org/pdf/2611.04527)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction without generating future videos. We introduce DreamFree, a WAM that repurposes a pretrained video diffusion model as a predictive visual encoder through representation distillation. Th...

</details>

<details>
<summary>Share</summary>

```
Future Representation Distillation for Imagination-Free World Action Models

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

arXiv: https://arxiv.org/abs/2611.04527

#VLA #robotics
```

</details>

---

## World Models (9)

### [Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving](https://arxiv.org/abs/2611.05072)

**Authors:** Junzhe Wang, Jinqing Zhang, Qingjie Liu

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.05072) | [PDF](https://arxiv.org/pdf/2611.05072)

<details>
<summary>Abstract</summary>

Although existing candidate trajectory evaluators have substantially improved end-to-end planning accuracy, their underlying mechanism remains suboptimal. Model-based evaluators typically make scoring future-aware by explicitly predicting candidate-conditioned future states over the planning horizon, which we term rollout. However, rollout incurs high inference cost and accumulates prediction errors. We argue that planning does not require reconstructing a full future scene for each candidate, but only future-relevant information for reliable comparison. We therefore propose RFWorld, a Rollout...

</details>

<details>
<summary>Share</summary>

```
Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving

Although existing candidate trajectory evaluators have substantially improved end-to-end planning accuracy, their underlying mechanism remains suboptimal.

arXiv: https://arxiv.org/abs/2611.05072

#worldmodels #robotics
```

</details>

---

### [Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](https://arxiv.org/abs/2611.04073)

**Authors:** Anh Nguyen, Tianyi Xu, Phat Tran, Harry Yu, Huazheng Wang et al. (6 authors)

**Published:** 2026-11-02 | **Categories:** cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04073) | [PDF](https://arxiv.org/pdf/2611.04073) | [Code](https://github.com/realjoenguyen/RAGPJ-official)

<details>
<summary>Abstract</summary>

Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has not been evaluated in isolation. To fill this gap, we first construct OSWorld-Tutorial and ScienceBoard-Tutorial: two datasets for CUAs with curated multimodal tutorials, covering everyday and scientific domains. We then propose RAG-PolicyJudge (RAG-PJ), a policy-judge framework for CUAs conditioned on task-specific tut...

</details>

<details>
<summary>Share</summary>

```
Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials

Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges.

arXiv: https://arxiv.org/abs/2611.04073
Code: https://github.com/realjoenguyen/RAGPJ-official

#worldmodels #robotics
```

</details>

---

### [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)

**Authors:** Travis Davies, Wentao Ma, Lihao Guo, Tengfei Ma, Xiaowen Chang et al. (13 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04870) | [PDF](https://arxiv.org/pdf/2611.04870)

<details>
<summary>Abstract</summary>

A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon rollouts. We present PrimeSim, an action-conditioned, multiview world model simulator that addresses these challenges through progressive midtraining and posttraining. Starting from a pretrained video generator, we midtrain on 30,110 hours of robot demonstrations spanning 22 platforms. To improve action following, we introduce a unified cross-embodiment action representation and frame...

</details>

<details>
<summary>Share</summary>

```
PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations

A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon roll...

arXiv: https://arxiv.org/abs/2611.04870

#worldmodels #robotics
```

</details>

---

### [Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](https://arxiv.org/abs/2611.04492)

**Authors:** Jimmy Wang, Yifan Chou, Kaifeng Zhang, Yixuan Wang, Binghao Huang et al. (8 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04492) | [PDF](https://arxiv.org/pdf/2611.04492)

<details>
<summary>Abstract</summary>

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future observations in 2D image or video space without explicitly modeling the underlying 3D scene, making spatial consistency across viewpoints and over long-horizon interactions challenging. We introduce 3D World Simulator, an action-conditioned multimodal world modeling framework that jointly predicts appearance, geometry, and tactile observations from a unified 3D representation. Our approach combines a hybrid particle-...

</details>

<details>
<summary>Share</summary>

```
Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning.

arXiv: https://arxiv.org/abs/2611.04492

#worldmodels #robotics
```

</details>

---

### [Physical Experience Builds Continual Spatial World Models](https://arxiv.org/abs/2611.04016)

**Authors:** Yuhang Sun

**Published:** 2026-11-02 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04016) | [PDF](https://arxiv.org/pdf/2611.04016)

<details>
<summary>Abstract</summary>

World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters. Continual operation faces a different problem. A familiar environment may change, and the agent must use previous experience without allowing old expectations to override current physical evidence. This study asks what repeated physical experience must contribute for a spatial world model to become progressively more useful rather than simply more persistent. A physics-grounded dynamic maze separates recurri...

</details>

<details>
<summary>Share</summary>

```
Physical Experience Builds Continual Spatial World Models

World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters.

arXiv: https://arxiv.org/abs/2611.04016

#worldmodels #robotics
```

</details>

---

### [Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence](https://arxiv.org/abs/2611.04371)

**Authors:** Wenhao Xu, Changwei Wang, Shunpeng Chen, Yukun Song, Sifan Zhou et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04371) | [PDF](https://arxiv.org/pdf/2611.04371)

<details>
<summary>Abstract</summary>

Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces. Robot learning builds physical competence, whereas AI for science chooses which experiment to run, each reporting different endpoints. This review treats their interface as one problem, embodied AI for science, where the experiment itself is partially observed: specimen state, apparatus state and measurement processes are latent, actions are costly and irreversible, and missingness depends on execution and outcome. We organize the literature by three closures oper...

</details>

<details>
<summary>Share</summary>

```
Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence

Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces.

arXiv: https://arxiv.org/abs/2611.04371

#worldmodels #robotics
```

</details>

---

### [FlowBench: Counterfactual Imagination Training for Spatial Intelligence](https://arxiv.org/abs/2611.03937)

**Authors:** Yifan Liu, Baihan Zhang, Khai Loong Aw, Klemen Kotar, Daniel L. K. Yamins

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.03937) | [PDF](https://arxiv.org/pdf/2611.03937) | [Code](https://github.com/liuyifan22/FlowBench)

<details>
<summary>Abstract</summary>

Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning. However, this capability remains underexplored in vision-language models and world models. We formalize this capability as Counterfactual Spatial Imagination (CSI) and introduce FlowBench, a resource for training and evaluating both, with 428K training examples spanning simulated and real-world scenes, household environments and tabletop manipulation, and diverse question types. A scalable, fully automatic pipeline pairs each hypothetical motion with spatial questions and, in...

</details>

<details>
<summary>Share</summary>

```
FlowBench: Counterfactual Imagination Training for Spatial Intelligence

Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning.

arXiv: https://arxiv.org/abs/2611.03937
Code: https://github.com/liuyifan22/FlowBench

#worldmodels #robotics
```

</details>

---

### [A research world model of power engineering learns its dynamics and reveals what-ifs](https://arxiv.org/abs/2611.04566)

**Authors:** Fanping Sui, Ying Zhang, Liwei Lin

**Published:** 2026-11-03 | **Categories:** cs.AI, eess.SY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04566) | [PDF](https://arxiv.org/pdf/2611.04566)

<details>
<summary>Abstract</summary>

Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are taken, and existing forecasts of research fields extrapolate a single trajectory. Here we introduce research world models, which treat a research field as a dynamical system that can be acted upon, and establish one for power engineering from 1.1 million papers. A distilled language model reads each paper into role-typed concepts, two sophisticated, high-fidelity graph-temporal ne...

</details>

<details>
<summary>Share</summary>

```
A research world model of power engineering learns its dynamics and reveals what-ifs

Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are...

arXiv: https://arxiv.org/abs/2611.04566

#worldmodels #robotics
```

</details>

---

### [Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028)

**Authors:** Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Kaiwen Geng et al. (8 authors)

**Published:** 2026-11-02 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.04028) | [PDF](https://arxiv.org/pdf/2611.04028)

<details>
<summary>Abstract</summary>

Effective world modeling requires compressing salient history information that facilitates future prediction. However, most existing approaches inherit tokenization and conditioning mechanisms from video generation, where objectives are centered around perceptual realism rather than predictive utility. This discrepancy limits the world model's effectiveness, especially in environments dominated by visual nuisances or task-irrelevant background details. To this end, we introduce Compression Forcing (CF), a general framework that aligns history compression with the predictive objective of world...

</details>

<details>
<summary>Share</summary>

```
Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models

Effective world modeling requires compressing salient history information that facilitates future prediction.

arXiv: https://arxiv.org/abs/2611.04028

#worldmodels #robotics
```

</details>

---
